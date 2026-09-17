# Pass 4: result-only reconstruction and exploratory analysis

This directory supports Section V. It reads released experiment results, not
sensor observations or TEST labels. It never imports AQSE, constructs circuits,
fits a model, generates a prediction, or changes an experimental artifact.
The original scientific execution is not repeated.

## Evidence identities

- Source repository: `florianocaprio/AQSE`.
- Published snapshot: `0ed58cfd4a1680ee111f91bb44af7ab101d4c01a`.
- Experiment revision: `091acf2e98b2b88720730eea276e253f0c96f5a6`.
- Source directory: `paper/replicated-study-2026/`.
- Canonical reporting package: `report-recovery-v2`, not v1.
- `input_manifest.json` records local SHA-256 and source Git-blob identities.

Two inputs are byte-identical copies of released files: `replicas.csv` and
`aggregate_statistics.json`. Their full Git blob identities were verified.
The other two inputs are explicitly identified extracts:

- `kernel_initial_selected_final.csv`: initial, selected, and checkpoint-10
  effective rank/concentration for each of 30 primary replicas. It is not the
  complete 330-row kernel-diagnostics CSV. Its field mapping and original blob
  identity are recorded in the manifest.
- `control_summary.json`: the exact reported control intervals, positive paired
  statistics, and completion counts extracted from `final_report.json`.

The extracts retain the source values. They are not new experiments or new
bootstrap estimates of the controls. The optional verification below checks
them against all four original released files.

## Reproduce tables and analysis

Use Python 3.10 or later with NumPy and SciPy. The delivered reconstruction used
Python 3.13.5, NumPy 2.3.5, and SciPy 1.17.0. These are the manuscript-analysis
versions, not the scientific-execution environment recorded in the paper.

From the manuscript root:

```sh
python3 analysis/pass4/reproduce_results.py
```

This recreates four table sources and four files in `derived/`. It verifies
10 method/metric summaries and 8 paired summaries against the canonical
report. Bootstrap seeds, sorted inputs, unrounded score differences and the
Pratt signed-rank convention match the reporting code. It does not replace
canonical estimates with a newly preferred statistical convention.

To check the extracts against the original local AQSE result package:

```sh
python3 analysis/pass4/reproduce_results.py \
  --canonical-root "$HOME/Projects/AQSE/paper/replicated-study-2026"
```

Only `replicas.csv`, `aggregate_statistics.json`, `kernel_diagnostics.csv`, and
`final_report.json` are read from that path. Original Git blob hashes are
checked before the extraction comparisons. A changed source file causes an
error. No `.npy` file, raw measurement, TEST label, or model is loaded.

With Matplotlib installed, regenerate the three vector figures:

```sh
python3 analysis/pass4/reproduce_results.py --figures
```

Figure PDFs are included in the manuscript repository. LaTeX and Overleaf do
not need Python, SciPy, or Matplotlib to compile the manuscript.

## Canonical versus post-hoc outputs

- Main means, SDs, intervals, and Wilcoxon outputs in the tables come from
  `aggregate_statistics.json`. The report-only calculation checks them rather
  than overwriting their scientific source.
- Controls use the intervals in `final_report.json/controls`. The primary
  `controls/primary_study/aggregate` is not substituted for the separate
  top-level reporting aggregation, which has a different bootstrap seed path.
- Win/tie/loss uses a descriptive tolerance of `1e-12`. Raw float counts are
  retained beside these counts. One BA TQK-MLP pair is a numerical near-tie;
  canonical inference continues to use the unrounded source floats.
- Kernel endpoint changes and selection counts are descriptive.
- Four geometry-performance correlations are new **post-hoc** analyses, not
  preregistered endpoints. Each uses one selected kernel summary per replica.
  BA is mapped to verified correct-count ticks on the 1/24 grid only for rank
  analysis. Permutation seeds are 4001001 through 4001004. There are 19,999
  sampled pairings with replacement and an add-one Monte Carlo p-value.
  Absolute-statistic ties use a numerical tolerance of 1e-14.
- Correlation intervals use 2,000 paired row bootstrap resamples, seeds
  4002001 through 4002004. All 2,000 resamples were finite in each analysis.
- Holm correction is reported separately for the four geometry tests.
  A BA multiplicity sensitivity analysis reports both the all-four-baseline
  family and the three-secondary-baseline family. Neither was preregistered.
  Their different decisions must not be hidden or selected retrospectively.

The kernel records do not contain TEST predictions for unselected checkpoints.
No trained-versus-initial TEST improvement can be reconstructed from them.
The per-method CSV repeats a joint per-replica runtime and cannot establish a
method-specific speed comparison.

## Output status

`derived/results_audit.json` records the analysis environment and all checks.
The script is deterministic within its recorded numerical environment.
A different library version may alter signed-rank implementation or numeric
roundoff; an identity/reconstruction error is not permission to change a
frozen result. Inspect the discrepancy instead.
