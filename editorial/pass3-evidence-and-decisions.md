# Pass 3: experimental-methodology source audit

Date: 2026-09-17. Target: IEEE Transactions on Quantum Engineering.
Status: Sections I-IV of a partial English manuscript. Results and final submission checks are not included in this pass.

## Fixed identities and scope

- Manuscript input commit: `6bceb8faf2ce0035769743390b9549c114aff536`, repository `florianocaprio/AQSE-Paper`, branch `paper/ieee-tqe-v1`.
- Scientific execution commit: `091acf2e98b2b88720730eea276e253f0c96f5a6`, repository `florianocaprio/AQSE`.
- Published scientific code-and-results snapshot: `0ed58cfd4a1680ee111f91bb44af7ab101d4c01a`.
- Report-recovery source commit: `d42965ef6a38791fcdbdc1b7bbb3750a58d1f2f1`.
- Canonical report directory in AQSE: `paper/replicated-study-2026/`, containing the recovered `report-recovery-v2` package.
- Protocol document SHA-256 recorded by execution: `db336a0c01880da07e44687a0d6ed937cd1eee4446a6d109b96c3b3f703768c4`.

The execution revision, report-recovery revision, and later publication snapshot serve different purposes. The text does not replace the execution revision with the merge SHA. The historical report-recovery-v1 is not used.

The 12 existing manuscript payloads were verified against the Git blob identities returned for the published Pass 2 tree. The three existing prose sections, the two figures, State8 table, and previous editorial notes are retained byte-for-byte. This pass changes only the LaTeX entry point, README and bibliography, and adds Methodology, two method tables, and this note.

## Requested basis and source hierarchy

The source code at the execution revision defines what was run. The versioned protocol defines the pre-execution decisions. The environment and recovery records report operational provenance. Earlier chat descriptions are not substituted for these sources. Where wording in an earlier description could suggest a stronger design, Section IV gives the implemented behavior without changing code or evidence.

No AQSE experiment, model fit, new prediction, TEST-array load, or aggregation of scientific metrics was performed during Pass 3. Reading released source and administrative JSON records is not a new experimental run. No working installation of the scientific stack is required for the upload package.

## Source-to-method map

Paths below are in `florianocaprio/AQSE` at the execution commit unless otherwise indicated.

| Manuscript content | Source and relevant operations |
| --- | --- |
| Primary/control counts, seeds, run order, primary decision rule | `backend/app/paper_study/execution.py`: constants and `execute_preregistered_study` |
| Repository-level preregistration and four-run pilot disclosure | `docs/validation/paper-replicated-study.md` at execution revision |
| Physical nuisance draws and noise ranges | `backend/app/training/generation.py`: `build_episode_plans` |
| One static vector node, background, temperature, bandwidth and clipping | same file: `_network_configuration`, `generate_episode`; default response in `backend/app/network/models.py` |
| Gaussian per-sample noise, response/filter/clipping order | `backend/app/network/simulation.py`: `_apply_node_response`, `_project_and_clip` |
| 100 Hz, 1,000 samples, window and hop | `backend/app/training/generation.py`: constants and `FEATURE_WINDOW` |
| Central ordinal 9, one row per episode, fail on invalid central window | `backend/app/paper_study/datasets.py`: `sensor_replica_dataset` |
| Exact 36/12/12 per-class lineage split | `backend/app/training/splits.py`: `stratified_lineage_split`, `validate_split` |
| Uniform sampling and harmonic quality thresholds | `backend/app/features/models.py`: `FeatureWindowConfiguration`, `MeasuredVectorSeries`; `windowed.py`: `_quality` |
| Phase relative to the start of each window | `backend/app/features/windowed.py`: `local_time = time[start:end] - time[start]` |
| Detrending, Hann PSD, frequency interpolation | `backend/app/preprocessing/signal.py` |
| Harmonic regression, SNR, variance, PSD and temperature features | `backend/app/preprocessing/features.py` |
| Hash-derived replica seed namespaces, encoding and QNG bank | `backend/app/paper_study/study.py`: `_derive_seed`, `_replica_seeds`, `_encode_with_scaler`, `_balanced_bank_indices` |
| QNG trajectory, 33-candidate ceiling, full-TRAIN SVC and tie order | same file: `_fit_quantum` |
| Classical preprocessing, fixed grids and model constructors | `backend/app/paper_study/baselines.py`: `fit_classical_comparators` |
| Positive teacher dataset and strongest-contrast retention | `backend/app/paper_study/datasets.py`: `positive_control_dataset` |
| Control sample hashing and 120/40/40 stratification | same file: `split_binary_dataset` |
| Shared negative-control dataset and TRAIN-only permutation | `execution.py`: `control_X, control_y`; `study.py`: `permutation_control`, `_run_replica` |
| Designated TEST reads and four ledger events | `backend/app/paper_study/storage.py`: `ReplicaStore`; `study.py`: `_run_replica` |
| Metrics and timing scope | `study.py`: `_metric_pair`, `_run_replica`; `execution.py`: `_replica_rows` |
| Bootstrap, unrounded paired Wilcoxon and group statistics | `backend/app/paper_study/statistics.py` |
| Primary report bootstrap seed schedule | `execution.py`: `_method_statistics`, `_paired_statistics`; recovery pins method order |
| Uncentered TRAIN eigenspectrum and tolerances | `backend/app/paper_study/diagnostics.py`: `kernel_diagnostics` |
| Actual recorded software environment | `paper/replicated-study-2026/environment.json` at publication snapshot |
| Report recovery without new scientific operations | `paper/replicated-study-2026/recovery_record.json` at publication snapshot |

Representative immutable source URLs:

- https://github.com/florianocaprio/AQSE/blob/091acf2e98b2b88720730eea276e253f0c96f5a6/backend/app/paper_study/execution.py
- https://github.com/florianocaprio/AQSE/blob/091acf2e98b2b88720730eea276e253f0c96f5a6/backend/app/paper_study/study.py
- https://github.com/florianocaprio/AQSE/blob/091acf2e98b2b88720730eea276e253f0c96f5a6/backend/app/training/generation.py
- https://github.com/florianocaprio/AQSE/blob/091acf2e98b2b88720730eea276e253f0c96f5a6/backend/app/paper_study/baselines.py
- https://github.com/florianocaprio/AQSE/blob/091acf2e98b2b88720730eea276e253f0c96f5a6/backend/app/paper_study/statistics.py
- https://github.com/florianocaprio/AQSE/blob/0ed58cfd4a1680ee111f91bb44af7ab101d4c01a/paper/replicated-study-2026/recovery_record.json

## Distinctions that must survive later editing

### Three different experimental populations

Primary: 30 newly generated sensor corpora, 120 episodes each, split 72/24/24. One central harmonic feature row per episode. QNG bank has 32 rows; the SVC uses all 72 TRAIN rows.

Positive: 12 newly generated 200-example teacher datasets, split 120/40/40. QNG still uses a 32-row bank, while all 120 TRAIN rows fit the final classifier.

Negative: 12 re-splits of one teacher dataset generated once with seed 3004001. Per-run split, permutation, QNG, and classical seeds vary. The dataset seed field is derived but ignored by the negative-control factory. The control is not 12 independently generated corpora. Its variation is conditional on a fixed set of 200 examples, with sample recurrence across runs.

These groups must not be pooled as 54 independent sensor-dataset replications. Their statistical roles and data-generating mechanisms differ.

### Negative-control information boundary

Only TRAIN labels are permuted. VALIDATION labels remain correct and are used by RBF and TQK selection. This is the frozen control definition, not a full pipeline label-null design. Section IV reports it as implemented, including the prespecified chance-interval check. It does not replace that check with a revised control or declare it passed. The possible role of validation-based selection in above-chance performance belongs to Discussion and remains a hypothesis unless separately tested.

A bootstrap interval over control runs does not include uncertainty from generating a new control corpus. The check that an interval contains 0.5 is not an equivalence test and does not prove absence of residual supervision.

### Positive-control enrichment

The teacher uses the same circuit family, but its labels are created before the student's fitted encoding. At least 100 candidates per class are accumulated and then the 100 largest absolute fidelity contrasts are kept. The resulting samples are margin-enriched, not an unbiased sample of the whole coordinate cube.

The fixed prototypes, in source order, are:

```text
p_- = (-1.15,  0.75, -0.85,  1.05, -0.65,  0.95, -1.25,  0.55)
p_+ = ( 1.10, -0.80,  0.90, -1.00,  0.70, -0.90,  1.20, -0.60)
```

Success is a mechanism-aligned software check. It does not establish field validity, hardware advantage, or exclusive representation by the student TQK.

### Input and capacity fairness

The replicated classical models use the eight raw harmonic features. RBF, MLP and RFF standardize them on TRAIN; boosting does not. The classical phase coordinate stays scalar. The earlier nine-coordinate circular classical baseline belongs to a different AQSE experiment and is not imported into this methodology.

TQK can select up to 33 checkpoint/C pairs. RBF selects nine C/gamma combinations. MLP, RFF and boosting each have one fixed configuration. Shared data do not equalize search or compute budgets. The 11-weight MLP comparison is with 16 circuit parameters, not with the parameter count of the complete kernel classifier. The fidelity density-operator feature space should not be described as equivalent to 256 RFF coordinates.

### TEST ledger versus memory access

The dataset constructor and validator have test arrays in memory, and structural validation inspects shapes and label class support before fitting. The loader ledger is a designated evaluation sequence. It cannot be described as proving that TEST labels never existed or were never inspected for structural checks before the final label loader. The reviewed fitting code does not pass test arrays into scaler fitting, QNG, classical fitting or selection. No security or distributed-sealing claim is made.

### Numerical inference conventions

The paired Wilcoxon wrapper passes the two unrounded score arrays directly to SciPy with `zero_method="pratt"`, `alternative="two-sided"`, and `method="auto"`. It has an explicit all-exact-zeros return value of p=1. It does not round paired differences to the finite TEST-grid resolution. Small floating-point distinctions can affect tie grouping. Preserve the frozen output for confirmatory reporting. Any future tolerance-aware sensitivity calculation must be labelled post hoc rather than silently replacing its p-values.

The bootstrap sorts scalar inputs before random index sampling. Quantiles use the default linear convention. The reported bounds are expanded to contain the observed mean if needed. No BCa or studentization is implemented.

Two reporting layers use different seed namespaces: the group `aggregate_replicas` records and the primary final report. They estimate the same types of quantities but need not have identical finite-resample interval endpoints. The final primary effect uses `_paired_statistics`, not a control/group interval chosen after inspecting results. During report recovery the method order is fixed to its original construction order, preventing JSON key sorting from changing bootstrap seeds.

For future reproduction of group seeds:

- `g = _derive_seed(base_seed, 0, "aggregate-bootstrap")`.
- Baselines in `aggregate_replicas` are alphabetically sorted. Score intervals use `g+offset`, paired effects `g+100+offset`, with offset starting at 1.
- Selected-kernel diagnostics use `g+500+index` after sorting diagnostic names.
- Negative-control chance intervals have their own `permutation-...-bootstrap` namespaces, as implemented in `permutation_control`.

Do not present a secondary Holm adjustment or a spectral-performance correlation as preregistered. This writing pass does not compute either.

### Available evidence limits

Only one selected quantum configuration is evaluated on TEST for each replica. Per-checkpoint TRAIN spectra cannot provide test accuracy for the unselected initial circuit. The data are insufficient for a new paired TEST comparison of QNG versus an independently selected fixed-kernel arm without a separate experiment.

The total runtime in `replicas.csv` is copied into each method row. It is the total for that replica across all methods, not the runtime of the named method. The source separately records joint training/selection and joint test timings. No per-method speed or QPU-cost comparison is inferred.

### Provenance and preregistration

The preregistration is a repository-level record with a before-execution protocol snapshot. It is not an OSF registration or third-party registry record. The four-run negative pilot informed the 12-run count. The original document's wording that four runs demonstrated insufficient stability is not adopted as a universal statistical fact; the manuscript reports the actual pilot-to-count decision. The source specifies no prospective power calculation.

The environment record is transcribed as recorded: Python 3.12.14, NumPy 2.5.3, SciPy 1.18.1, scikit-learn 1.9.0, Qiskit 2.5.2, Linux/aarch64. These versions were not installed or used to rerun science during this pass. The local LaTeX/compiler environment is separate.

## New bibliography records

Four sources were added without modifying the earlier 23 entries. These support terminology and method origins, not a claim that the implemented pipeline inherits theoretical guarantees.

1. B. Efron, "Bootstrap methods: Another look at the jackknife," Ann. Statist., vol. 7, no. 1, pp. 1-26, 1979, DOI 10.1214/aos/1176344552. Publisher DOI resolves to Project Euclid. The publisher page was not fully retrievable in this session; publication metadata was cross-checked against the Institute of Mathematical Statistics record. The exact AQSE percentile algorithm is grounded in its source code, not asserted to be a full derivation from this article.
2. F. Wilcoxon, "Individual comparisons by ranking methods," Biometrics Bull., vol. 1, no. 6, pp. 80-83, 1945, DOI 10.2307/3001968. Metadata verified against the original journal issue on JSTOR.
3. J. W. Pratt, "Remarks on zeros and ties in the Wilcoxon signed rank procedures," J. Amer. Statist. Assoc., vol. 54, no. 287, pp. 655-667, 1959, DOI 10.1080/01621459.1959.10501526. Publisher abstract describes ranking zeros and omitting their signed contributions. The 2012 online date is not used as publication year.
4. O. Roy and M. Vetterli, "The effective rank: A measure of effective dimensionality," Proc. 15th EUSIPCO, Poznan, Poland, pp. 606-610, 2007. IEEE Xplore record 7098875 and conference metadata were checked. No IEEE DOI is invented. The definition implemented in AQSE uses entropy-normalized nonnegative Gram eigenvalues.

Source links checked on 2026-09-17:

- https://doi.org/10.1214/aos/1176344552
- https://imstat.org/2015/11/17/model-free-inference-in-statistics-how-and-why/
- https://www.jstor.org/stable/i350470
- https://www.tandfonline.com/doi/abs/10.1080/01621459.1959.10501526
- https://ieeexplore.ieee.org/document/7098875/
- https://zenodo.org/records/40328
- https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.wilcoxon.html

The current SciPy documentation describes subtraction-roundoff sensitivity and is used as an editorial warning only. The actual computation is defined by the pinned AQSE call and the recorded experiment environment.

## Editorial and delivery checks

No new experiment was authorized or run. No raw TEST observations or label arrays were loaded. No author, affiliation, funding, ORCID, abstract, or publication metadata was inferred. The chapter distinguishes confirmed source behavior from methodological interpretation. It contains no performance result table or new result claim.

The generated delivery records document actual compilation, citation resolution, source preservation, layout inspection, package hashes and local upload-script tests. Tests of the uploader use isolated local Git remotes. They do not prove network authentication on the author's Mac.

The shared IEEEtran journal layout is retained. It is not asserted to be the final TQE production template. No custom margin or font-size compression is used. An IEEE/TQE template reconciliation and human review of author information and AI-assistance disclosure remain part of final integration.

ChatGPT drafted this section and prepared the source-to-method mapping, bibliography additions, and delivery scripts with human-provided study code and records. The authors must review these outputs and finalize the AI-assistance acknowledgment before submission. This note is editorial and is not compiled into the manuscript.
