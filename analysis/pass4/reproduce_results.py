#!/usr/bin/env python3
"""Report-only analysis of released AQSE metrics. Never imports the AQSE pipeline.

Default inputs are small, versioned result extracts beside this script.
--canonical-root checks them against the original published report directory.
No observations, labels, kernels, states, models, or predictions are generated.
"""
from __future__ import annotations
import argparse, csv, hashlib, json, platform, sys
from pathlib import Path
import numpy as np
import scipy
from scipy.stats import rankdata, wilcoxon

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
METHODS = ('quantum', 'rbf_svc', 'mlp_11_parameter', 'rff_256', 'gradient_boosting')
LABELS = {'quantum':'TQK','rbf_svc':'RBF-SVC','mlp_11_parameter':'MLP-11','rff_256':'RFF-256','gradient_boosting':'Gradient boosting'}
METRICS = ('balanced_accuracy','macro_f1')
SOURCE_COMMIT = '0ed58cfd4a1680ee111f91bb44af7ab101d4c01a'
RAW_BLOBS = {'replicas.csv':'c62e6aa88d0c8822e27b660a21ea366f7f323eaa',
 'aggregate_statistics.json':'e033ea1b9c3d6cd7c6b1a3d75ea9e8d14841fdb8',
 'kernel_diagnostics.csv':'f1c424c8e9848214e4694f73e9b1210003604e67',
 'final_report.json':'ef8e8b5363c07c392a3e382ea344eacfc28f5330'}


def read_csv(path: Path):
    # csv + float, rather than pandas' default parser, retains the stored floats.
    with path.open(encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))


def blob_hash(data: bytes) -> str:
    return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()


def load_inputs():
    r = read_csv(HERE/'inputs/replicas.csv')
    k = read_csv(HERE/'inputs/kernel_initial_selected_final.csv')
    a = json.loads((HERE/'inputs/aggregate_statistics.json').read_text())
    c = json.loads((HERE/'inputs/control_summary.json').read_text())
    manifest = json.loads((HERE/'input_manifest.json').read_text())
    expected_names = {'replicas.csv', 'aggregate_statistics.json',
                      'kernel_initial_selected_final.csv', 'control_summary.json'}
    if {Path(x['local_path']).name for x in manifest['inputs']} != expected_names:
        raise ValueError('Result input manifest has an unexpected file list')
    for record in manifest['inputs']:
        name = Path(record['local_path']).name
        payload = (HERE/'inputs'/name).read_bytes()
        if len(payload) != record['bytes'] or hashlib.sha256(payload).hexdigest() != record['sha256']:
            raise ValueError('Result input SHA-256 mismatch: '+name)
    for name in ('replicas.csv','aggregate_statistics.json'):
        if blob_hash((HERE/'inputs'/name).read_bytes()) != RAW_BLOBS[name]:
            raise ValueError('Canonical result-file identity mismatch: '+name)
    if len(r)!=150 or len(k)!=30: raise ValueError('Incomplete result extracts')
    if [int(x['replica_index']) for x in k] != list(range(30)):
        raise ValueError('Kernel extract rows must be ordered uniquely from 0 to 29')
    if any(not 0 <= int(x['selected_checkpoint']) <= 10 for x in k):
        raise ValueError('Selected checkpoint outside the frozen trajectory')
    if sorted({int(x['replica_index']) for x in r}) != list(range(30)):
        raise ValueError('Replica identities must be 0..29')
    for i in range(30):
        rr=[x for x in r if int(x['replica_index'])==i]
        if tuple(x['method']for x in rr)!=METHODS: raise ValueError('Method order mismatch')
        if any(x['failure'] or (x['train_size'],x['validation_size'],x['test_size'])!=('72','24','24')for x in rr):
            raise ValueError('Unexpected completion or split record')
        if len({tuple(x[z] for z in ('replica_seed','dataset_seed','split_seed','qng_seed','classical_seed','runtime_seconds'))for x in rr})!=1:
            raise ValueError('Within-replica provenance mismatch')
    return r,k,a,c


def verify_canonical(root: Path, r, k, a, c):
    """Read only released results. No TEST arrays or dataset-generation files."""
    for name,h in RAW_BLOBS.items():
        if blob_hash((root/name).read_bytes())!=h: raise ValueError('Source revision mismatch: '+name)
    if read_csv(root/'replicas.csv')!=r: raise ValueError('Main rows changed')
    if json.loads((root/'aggregate_statistics.json').read_text())!=a: raise ValueError('Aggregate changed')
    raw=read_csv(root/'kernel_diagnostics.csv')
    if len(raw)!=330: raise ValueError('Expected 330 checkpoint diagnostics')
    for row in k:
        i=int(row['replica_index']); rr=[x for x in raw if int(x['replica_index'])==i]
        if [int(x['checkpoint_index'])for x in rr]!=list(range(11)): raise ValueError('Incomplete trajectory')
        selected=[x for x in rr if x['selected']=='True']
        if len(selected)!=1 or int(selected[0]['checkpoint_index'])!=int(row['selected_checkpoint']):
            raise ValueError('Selected checkpoint mismatch')
        for prefix,source in (('initial',rr[0]),('selected',selected[0]),('final',rr[10])):
            for field,original in (('effective_rank','effective_rank'),('concentration','spectral_concentration')):
                if float(row[prefix+'_'+field])!=float(source[original]):
                    raise ValueError('Kernel extract mismatch')
    report=json.loads((root/'final_report.json').read_text())
    if report['completed_replicas']!=c['completed_replicas']: raise ValueError('Counts changed')
    cc=report['controls']; neg=cc['negative_permutation_control']['balanced_accuracy']; pos=cc['positive_mechanism_control']['aggregate']
    if c['negative']!=neg: raise ValueError('Negative-control extraction mismatch')
    pp=dict(pos['baseline_balanced_accuracy']); pp['quantum']=pos['quantum_balanced_accuracy']
    if c['positive']!=pp: raise ValueError('Positive-control extraction mismatch')
    for m,item in c['positive_paired'].items():
        original=pos['delta_by_baseline'][m]
        if item['interval']!=original['delta'] or item['wilcoxon_p']!=original['wilcoxon']['p_value']:
            raise ValueError('Positive-control pair mismatch')
    print('Canonical report-only inputs verified. No TEST arrays read.')


def bootstrap_mean(x, seed):
    x=np.sort(np.asarray(x,dtype=float)); rng=np.random.default_rng(seed)
    v=x[rng.integers(0,len(x),size=(2000,len(x)))].mean(axis=1)
    lo,hi=np.quantile(v,[.025,.975]); point=float(x.mean())
    return point,min(float(lo),point),max(float(hi),point)


def holm(pvalues):
    p=np.asarray(pvalues,float); order=np.argsort(p,kind='stable'); m=len(p)
    corrected=np.minimum(1,np.maximum.accumulate((m-np.arange(m))*p[order]))
    out=np.empty(m);out[order]=corrected;return out.tolist()


def corr(x,y):
    a=rankdata(x,method='average'); b=rankdata(y,method='average')
    a=a-a.mean();b=b-b.mean();d=np.linalg.norm(a)*np.linalg.norm(b)
    return float(a@b/d) if d>0 else float('nan')


def correlation_audit(x,y,j):
    """Post hoc. Permute pairings, not labels used in a learning experiment."""
    rho=corr(x,y); a=rankdata(x)-15.5; b=rankdata(y)-15.5
    denom=np.linalg.norm(a)*np.linalg.norm(b)
    rng=np.random.default_rng(4001001+j)
    # 19,999 uniformly sampled pairings, with replacement, add-one Monte Carlo p.
    idx=np.asarray([rng.permutation(30)for _ in range(19999)])
    perm=(a[idx]@b)/denom
    extreme=int(np.count_nonzero(np.abs(perm)>=abs(rho)-1e-14))
    p=(extreme+1)/20000
    rng=np.random.default_rng(4002001+j)
    draws=rng.integers(0,30,size=(2000,30))
    boot=np.array([corr(x[z],y[z])for z in draws]); finite=boot[np.isfinite(boot)]
    lo,hi=np.quantile(finite,[.025,.975])
    return {'rho':rho,'ci_lower':float(lo),'ci_upper':float(hi),
            'permutation_p':p,'permutations':19999,'permutation_seed':4001001+j,
            'bootstrap_resamples':2000,'bootstrap_seed':4002001+j,'valid_bootstrap':len(finite)}


def analyze(r,k,a,c):
    X={m:{met:np.array([float(x[met])for x in r if x['method']==m])for met in METRICS}for m in METHODS}
    verifications=[]; descriptions=[]; pairs=[]
    for im,m in enumerate(METHODS):
        for it,met in enumerate(METRICS):
            x=X[m][met]; recorded=a['method_statistics'][m][met]
            pt,lo,hi=bootstrap_mean(x,3001001+10000+im*10+it)
            target=recorded['mean_interval']
            differences=[abs(pt-target['point']),abs(lo-target['lower']),abs(hi-target['upper']),abs(float(x.std(ddof=1))-recorded['standard_deviation'])]
            if max(differences)>1e-13: raise ValueError('Stored aggregate not reproduced: '+m+' '+met)
            verifications.append({'kind':'method','method':m,'metric':met,'max_abs_error':max(differences)})
            descriptions.append({'method':m,'metric':met,'mean':target['point'],'lower':target['lower'],'upper':target['upper'],
                                 'sd':recorded['standard_deviation'],'median':float(np.median(x)),
                                 'minimum':float(x.min()),'maximum':float(x.max()),
                                 'perfect_count':int(np.count_nonzero(x==1)),
                                 'below_0_9_count':int(np.count_nonzero(x<.9))})
    for ib,m in enumerate(METHODS[1:]):
        for it,met in enumerate(METRICS):
            d=X['quantum'][met]-X[m][met]; recorded=a['paired_statistics'][m][met]
            pt,lo,hi=bootstrap_mean(d,3001001+20000+ib*10+it)
            w=wilcoxon(X['quantum'][met],X[m][met],zero_method='pratt',method='auto',alternative='two-sided')
            target=recorded['delta_mean_interval']
            differences=[abs(pt-target['point']),abs(lo-target['lower']),abs(hi-target['upper']),abs(float(w.pvalue)-recorded['wilcoxon']['p_value']),abs(float(w.statistic)-recorded['wilcoxon']['statistic'])]
            if max(differences)>1e-12:raise ValueError('Stored paired statistic not reproduced: '+m+' '+met)
            verifications.append({'kind':'paired','method':m,'metric':met,'max_abs_error':max(differences)})
            pairs.append({'baseline':m,'metric':met,'delta':target['point'],'lower':target['lower'],'upper':target['upper'],
                          'wilcoxon_p':recorded['wilcoxon']['p_value'],'wilcoxon_W':recorded['wilcoxon']['statistic'],
                          'wins':int(sum(d>1e-12)),'ties':int(sum(abs(d)<=1e-12)),'losses':int(sum(d< -1e-12)),
                          'raw_wins':int(sum(d>0)),'raw_ties':int(sum(d==0)),'raw_losses':int(sum(d<0))})
    p4=[a['paired_statistics'][m]['balanced_accuracy']['wilcoxon']['p_value']for m in METHODS[1:]]
    adjusted4=dict(zip(METHODS[1:],holm(p4)))
    secondary=METHODS[2:];adjusted3=dict(zip(secondary,holm([a['paired_statistics'][m]['balanced_accuracy']['wilcoxon']['p_value']for m in secondary])))
    cp=np.array([int(x['selected_checkpoint'])for x in k])
    kernel={'selected_checkpoint_counts':{str(i):int(sum(cp==i))for i in range(11)},'selected_after_update':int(sum(cp>0)),
            'checkpoint_count_per_replica':11,'checkpoint_records':330}
    for field,canonical_key in [('effective_rank','effective_rank'),('concentration','maximum_eigenvalue_trace_ratio')]:
        ini=np.array([float(x['initial_'+field])for x in k]);sel=np.array([float(x['selected_'+field])for x in k]);end=np.array([float(x['final_'+field])for x in k])
        if abs(sel.mean()-a['kernel_aggregate'][canonical_key]['point'])>1e-12:raise ValueError('Selected geometry aggregate mismatch')
        kernel[field]={'initial_mean':float(ini.mean()),'selected_mean':float(sel.mean()),'selected_min':float(sel.min()),'selected_max':float(sel.max()),'final_mean':float(end.mean()),
                       'final_minus_initial_mean':float(np.mean(end-ini)),'mean_absolute_change':float(np.mean(abs(end-ini))),
                       'min_change':float(min(end-ini)),'max_change':float(max(end-ini)),
                       'increased':int(sum(end>ini)),'decreased':int(sum(end<ini))}
    # TEST has exactly 12 examples/class; BA is an integer number correct /24.
    # This display/rank-only quantization does not modify the canonical Wilcoxon.
    ticks={m:np.rint(24*X[m]['balanced_accuracy']).astype(int)for m in METHODS}
    for m in METHODS:
        if np.max(np.abs(X[m]['balanced_accuracy']-ticks[m]/24))>1e-12:raise ValueError('Non-grid BA in fixed cohort')
    correlations=[]
    endpoints=[('TQK_BA',ticks['quantum']),('TQK_minus_RBF',ticks['quantum']-ticks['rbf_svc'])]
    for field in ('effective_rank','concentration'):
        xx=np.array([float(x['selected_'+field])for x in k])
        for endpoint,yy in endpoints:
            correlations.append(dict(predictor=field,endpoint=endpoint,**correlation_audit(xx,yy,len(correlations))))
    for row,pvalue in zip(correlations,holm([q['permutation_p']for q in correlations])):row['holm_p_four_geometry_tests']=pvalue
    times=np.array([float(x['runtime_seconds'])for x in r if x['method']=='quantum'])
    runtime={'sum_seconds':float(sum(times)),'median_seconds':float(np.median(times)),'min_seconds':float(min(times)),'max_seconds':float(max(times)),
             'scope':'joint dataset generation, training/selection and TEST evaluation of all methods per replica; not per-method'}
    return dict(schema='aqse.pass4.report-only-audit.v1',source_commit=SOURCE_COMMIT,
        descriptive_metrics=descriptions,paired_comparisons=pairs,kernel=kernel,exploratory_correlations=correlations,
        exploratory_holm_all_four_BA=adjusted4,exploratory_holm_three_secondary_BA=adjusted3,
        runtime=runtime,verification=verifications,verification_max_abs_error=max(x['max_abs_error']for x in verifications),
        primary_conclusion='preregistered predictive-advantage criterion not met',
        posthoc_policy={'geometry_tests':4,'replica_count':30,'score_ties':'integer BA ticks at 1/24 for rank analysis; 1e-12 for descriptive W/T/L; original floats unchanged for canonical inference','scientific_reexecution':False},
        analysis_environment=dict(python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__))


def write_csv(path: Path, rows):
    with path.open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)


def tex_interval(i):return f"[{i['lower']:.4f}, {i['upper']:.4f}]"


def export_tables(a,c,result):
    tables=ROOT/'tables';tables.mkdir(exist_ok=True)
    text=r'''% Generated from canonical aggregate_statistics.json. Do not hand-edit numbers.
\begin{table*}[t]
\caption{Held-out performance across 30 primary replicas. Brackets are the canonical 95\% percentile-bootstrap intervals for the mean; SD is the sample standard deviation across replicas.}
\label{tab:main-performance}
\centering
\small
\setlength{\tabcolsep}{5pt}
\begin{tabular}{lcccccc}
\toprule
& \multicolumn{3}{c}{Balanced accuracy} & \multicolumn{3}{c}{Macro-F1} \\
\cmidrule(lr){2-4}\cmidrule(lr){5-7}
Method & Mean & 95\% interval & SD & Mean & 95\% interval & SD \\
\midrule
'''
    for m in METHODS:
        q=a['method_statistics'][m];b=q['balanced_accuracy'];f=q['macro_f1']
        text+=f"{LABELS[m]} & {b['mean_interval']['point']:.4f} & {tex_interval(b['mean_interval'])} & {b['standard_deviation']:.4f} & {f['mean_interval']['point']:.4f} & {tex_interval(f['mean_interval'])} & {f['standard_deviation']:.4f} \\\\\n"
    text+='\\bottomrule\n\\end{tabular}\n\\end{table*}\n';(tables/'main_performance.tex').write_text(text)
    text=r'''% Canonical unadjusted inference; W/T/L is a descriptive post hoc count.
\begin{table*}[t]
\caption{Paired TEST comparisons. Differences are TQK minus baseline. Intervals and unadjusted two-sided Pratt--Wilcoxon $p$-values are canonical. W/T/L denotes balanced-accuracy wins, ties, and losses with tolerance $10^{-12}$; this tolerance is not used to recompute the canonical tests.}
\label{tab:paired-results}
\centering
\small
\setlength{\tabcolsep}{4.5pt}
\begin{tabular}{lccccl}
\toprule
Baseline & Metric & Mean difference & 95\% interval & $p$ & BA W/T/L \\
\midrule
'''
    for m in METHODS[1:]:
        for j,metric in enumerate(METRICS):
            rr=next(x for x in result['paired_comparisons']if x['baseline']==m and x['metric']==metric)
            name=LABELS[m]+(' (primary)' if m=='rbf_svc' else '') if j==0 else ''
            text+=f"{name} & {('BA' if j==0 else 'Macro-F1')} & {rr['delta']:+.4f} & [{rr['lower']:+.4f}, {rr['upper']:+.4f}] & {rr['wilcoxon_p']:.4f} & {str(rr['wins'])+'/'+str(rr['ties'])+'/'+str(rr['losses']) if j==0 else ''} \\\\\n"
        if m!=METHODS[-1]: text+='\\addlinespace[2pt]\n'
    text+='\\bottomrule\n\\end{tabular}\n\\end{table*}\n';(tables/'paired_results.tex').write_text(text)
    text=r'''% Exact control-summary extract, no new control evaluation.
\begin{table}[t]
\caption{Control balanced accuracy. Each cell gives the canonical mean and 95\% bootstrap interval. The negative-control intervals condition on one shared dataset.}
\label{tab:control-results}
\centering
\footnotesize
\setlength{\tabcolsep}{3pt}
\renewcommand{\arraystretch}{1.15}
\begin{tabular}{lcc}
\toprule
Method & TRAIN-label control & Positive control \\
\midrule
'''
    for m in METHODS:
        n=c['negative'][m];p=c['positive'][m]
        label='Grad. boosting'if m=='gradient_boosting' else LABELS[m]
        text+=f"{label} & \\shortstack{{{n['point']:.4f}\\\\{tex_interval(n)}}} & \\shortstack{{{p['point']:.4f}\\\\{tex_interval(p)}}} \\\\\n"
    text+='\\bottomrule\n\\end{tabular}\n\\end{table}\n';(tables/'control_results.tex').write_text(text.replace('\\\\[', '\\\\{}['))
    text=r'''% Exploratory analysis; not part of the preregistered criterion.
\begin{table}[t]
\caption{Post-hoc associations between selected-kernel geometry and TEST performance ($n=30$). $\rho_s$ is Spearman correlation; $p_{\rm MC}$ uses 19,999 random pairings with the add-one correction. All four Holm-adjusted values are 1.}
\label{tab:geometry-associations}
\centering
\small
\setlength{\tabcolsep}{4pt}
\begin{tabular}{llrr}
\toprule
Predictor & Endpoint & $\rho_s$ & $p_{\rm MC}$ \\
\midrule
'''
    for x in result['exploratory_correlations']:
        predictor='$r_{\\rm eff}$'if x['predictor']=='effective_rank'else'$c_{\\rm spec}$'
        endpoint='TQK BA'if x['endpoint']=='TQK_BA'else'$\\Delta_{\\rm TQK-RBF}$'
        text+=f"{predictor} & {endpoint} & {x['rho']:+.3f} & {x['permutation_p']:.3f} \\\\\n"
    text+='\\bottomrule\n\\end{tabular}\n\\end{table}\n';(tables/'geometry_associations.tex').write_text(text)


def make_figures(r,k,a):
    # Matplotlib defaults; no chosen colors, palette, or style. Each is a separate plot.
    import matplotlib.pyplot as plt
    plt.rcParams['pdf.fonttype'] = 42
    out=ROOT/'figures';out.mkdir(exist_ok=True)
    data=[np.array([float(x['balanced_accuracy'])for x in r if x['method']==m])for m in METHODS]
    fig=plt.figure(figsize=(3.5,2.65));ax=fig.add_axes([.16,.23,.81,.74])
    ax.boxplot(data,positions=np.arange(1,6),widths=.48,showfliers=False)
    for j,x in enumerate(data,1):
        # Deterministic spreading within identical score levels, for display only.
        grid=np.rint(x*24).astype(int); jitter=np.zeros(len(x))
        for val in np.unique(grid):
            inds=np.flatnonzero(grid==val);jitter[inds]=np.linspace(-.13,.13,len(inds)) if len(inds)>1 else 0
        ax.scatter(j+jitter,x,s=10,alpha=.7,marker='o')
    ax.set_xticks(range(1,6),['TQK','RBF','MLP-11','RFF','Boosting'],rotation=25,ha='right',fontsize=8)
    ax.set_ylabel('TEST balanced accuracy',fontsize=9);ax.set_ylim(.77,1.025);ax.tick_params(labelsize=8)
    fig.savefig(out/'results_performance.pdf',metadata={'CreationDate':None,'ModDate':None});plt.close(fig)
    fig=plt.figure(figsize=(3.5,2.25));ax=fig.add_axes([.29,.25,.67,.70])
    for j,m in enumerate(METHODS[1:]):
        e=a['paired_statistics'][m]['balanced_accuracy']['delta_mean_interval']
        p=100*e['point'];ax.errorbar(p,3-j,xerr=[[100*(e['point']-e['lower'])],[100*(e['upper']-e['point'])]],fmt='o',capsize=3,markersize=4)
    ax.axvline(0,linestyle=':',linewidth=1)
    ax.set_yticks([3,2,1,0],['RBF-SVC','MLP-11','RFF-256','Boosting'],fontsize=8)
    ax.set_xlabel('TQK minus baseline (percentage points)',fontsize=8);ax.tick_params(labelsize=8);ax.set_ylim(-.5,3.5);ax.set_xlim(-5.3,3.5)
    fig.savefig(out/'results_paired_delta.pdf',metadata={'CreationDate':None,'ModDate':None});plt.close(fig)
    fig=plt.figure(figsize=(3.5,2.75));ax=fig.add_axes([.16,.18,.80,.77])
    ini=np.array([float(x['initial_effective_rank'])for x in k]);end=np.array([float(x['final_effective_rank'])for x in k]);cp=np.array([int(x['selected_checkpoint'])for x in k])
    ax.plot([24,33],[24,33],linestyle=':',linewidth=1)
    for keep,mark,label in ((cp==0,'o','Selected checkpoint 0'),(cp>0,'s','Selected checkpoint > 0')):
        ax.scatter(ini[keep],end[keep],s=22,marker=mark,label=label)
    ax.set_xlim(24,33);ax.set_ylim(24,33);ax.set_xlabel('Effective rank at checkpoint 0',fontsize=9);ax.set_ylabel('Effective rank at checkpoint 10',fontsize=9);ax.tick_params(labelsize=8)
    ax.legend(fontsize=7,loc='upper left',frameon=False)
    fig.savefig(out/'results_rank_change.pdf',metadata={'CreationDate':None,'ModDate':None});plt.close(fig)


def run(canonical_root=None, figures=False):
    r,k,a,c=load_inputs()
    if canonical_root is not None:verify_canonical(Path(canonical_root),r,k,a,c)
    result=analyze(r,k,a,c);out=HERE/'derived';out.mkdir(exist_ok=True)
    (out/'results_audit.json').write_text(json.dumps(result,indent=2,sort_keys=True,allow_nan=False)+'\n')
    for name,key in [('descriptive_metrics.csv','descriptive_metrics'),('paired_comparisons.csv','paired_comparisons'),('geometry_correlations.csv','exploratory_correlations')]:write_csv(out/name,result[key])
    export_tables(a,c,result)
    if figures:make_figures(r,k,a)
    print('Report-only audit complete:',len(result['verification']),'reconstruction checks; maximum error',result['verification_max_abs_error'])
    print('No simulation, state evaluation, fitting, prediction, or TEST-array access.')
    return result


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--canonical-root',type=Path,help='Directory of the released original result files; read-only')
    parser.add_argument('--figures',action='store_true',help='Regenerate the three manuscript vector figures')
    args=parser.parse_args();run(args.canonical_root,args.figures)
