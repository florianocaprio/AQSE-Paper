# Pass 4: Results, evidence audit, and post-hoc analysis record

Date: 2026-09-17. Target: IEEE Transactions on Quantum Engineering.
This is a partial manuscript, Sections I-V. No submission or merge is authorized.

## Pinned revisions

- Input manuscript: `b86bed0523914ceac74c0d59ccebd8e5e884b0c5` on
  `florianocaprio/AQSE-Paper`, `paper/ieee-tqe-v1`.
- Its complete 16-file tree is `4cfea1b69296d4b76374c8480faa5d55df007b23`.
  The previous delivery was reconstructed locally and its Git tree identity
  matches this published tree, before any change for Pass 4.
- Scientific execution: `091acf2e98b2b88720730eea276e253f0c96f5a6`.
- Published AQSE evidence snapshot: `0ed58cfd4a1680ee111f91bb44af7ab101d4c01a`.
- Reporting recovery: `d42965ef6a38791fcdbdc1b7bbb3750a58d1f2f1`.
- Canonical source directory: `paper/replicated-study-2026/` in AQSE.

The first four prose sections, existing TikZ figures, three method tables, and
prior editorial notes are preserved byte-for-byte. Main, README, bibliography,
and the ignore file are updated. No experiment source or artifact is modified.

## Source-to-claim map

All scientific paths below refer to the pinned AQSE evidence snapshot.

| Material | Evidence |
| --- | --- |
| Main counts, primary conclusion, control intervals and positive paired tests | `paper/replicated-study-2026/final_report.json` |
| Main mean/SD/CI, paired delta/CI/Wilcoxon, selected kernel aggregates | `paper/replicated-study-2026/aggregate_statistics.json` |
| All 150 method-replica rows, seeds, split sizes, runtimes and failure fields | `paper/replicated-study-2026/replicas.csv` |
| Initial/selected/final kernel summaries and selection flags | `paper/replicated-study-2026/kernel_diagnostics.csv` |
| Bootstrap seed order and canonical numerical handling | `backend/app/paper_study/execution.py`, `statistics.py`, and reporting recovery |
| Why no initial-versus-trained TEST estimate is available | `backend/app/paper_study/study.py`: only the selected model predicts TEST |
| Shared negative corpus, true validation labels | `execution.py` and `study.py`: control factory and TRAIN-only permutation |
| Margin-enriched positive control | `backend/app/paper_study/datasets.py`: strongest fidelity-contrast retention |
| Timer attribution | `study.py` joint stage timers; `execution.py` repeats total per method row |

## Local evidence and extraction boundaries

The manuscript sources include two byte-identical files and two small extracts
under `analysis/pass4/inputs/`. Their SHA-256 hashes and source Git blob IDs
are in `input_manifest.json`.

The two full-file Git blob identities checked against GitHub are:

- `replicas.csv`: `c62e6aa88d0c8822e27b660a21ea366f7f323eaa`.
- `aggregate_statistics.json`: `e033ea1b9c3d6cd7c6b1a3d75ea9e8d14841fdb8`.

The full kernel CSV was inspected in source ranges, but the included table is
an explicit 30-row endpoint/selected extract, not a byte-identical copy of
that 330-row file. The control extract retains exact values from the report.
The optional `--canonical-root` path compares both extracts to the source
files and checks all four full source Git identities. That optional check
requires the original files on the user's computer; it is not falsely
reported as an already executed whole-file check in this delivery.

The report's completion metadata and the primary CSV show the completed runs.
This pass did not reload the original 54 TEST ledgers or re-audit the 335-file
local experiment directory. Completion/integrity statements attributed to the
recovery remain source-reported rather than new independent filesystem audits.

## Reconstruction and measured outcomes

The independent result-only script reconstructed ten method/metric means,
standard deviations and percentile intervals, and eight paired mean intervals
and Pratt-Wilcoxon outputs. All 18 checks passed. The largest absolute error
was `2.7755575615628914e-17`. The delivered tables use canonical numbers rather
than replacing them with the reconstructed values.

The source contains more than one bootstrap aggregation path. Section V uses
`aggregate_statistics.json` for primary comparisons, not the differently
seeded `controls/primary_study/aggregate` nested inside the final report.
Control summaries use their own canonical group intervals.

Descriptive findings include:

- 19 selected initial checkpoints and 11 selected updated checkpoints.
- Selection counts: 0:19, 1:1, 2:4, 3:1, 4:2, 5:1, 7:2.
- 13 effective-rank increases and 17 decreases between checkpoints 0 and 10.
- TQK perfect BA in 13/30; below 0.9 in 5/30; all replicas retained.
- TQK-RBF BA win/tie/loss: 10/10/10.
- TQK-MLP BA win/tie/loss with 1e-12 tolerance: 4/13/13; strict float counts
  are 4/12/14. Both are stored. Canonical tests retain raw floats.
- Per-replica joint runtimes sum to 312.9414299320197 seconds, not five times
  that sum. Method-specific compute comparisons are unsupported.

These are descriptive analyses, not additional preregistered hypotheses.
No outlier was excluded. Checkpoint subgroups were not used to infer a causal
QNG benefit. The analysis cannot isolate data, split and initialization variance.

## New exploratory associations

Four tests relate the selected effective rank or spectral concentration to
TQK BA or its paired difference from RBF, using one row per primary replica.
This is explicitly post hoc and not part of the preregistered decision rule.

- Spearman average ranks.
- Correct-count integer BA ticks are verified against the 1/24 grid before
  rank analysis; raw experiment floats are retained for canonical tests.
- 19,999 random pairings, with replacement, seeds 4001001-4001004.
- Two-sided add-one Monte Carlo p-value, absolute-statistic tie tolerance 1e-14.
- 2,000 paired bootstrap resamples, seeds 4002001-4002004; all are finite.
- Holm family: these four geometry tests, separately from BA comparisons.

The four rho/p pairs are 0.1538437043/0.41005, 0.0694556309/0.71210,
-0.1402416694/0.45075, and -0.0926841697/0.62500. Adjusted p-values are all 1.
Intervals are reported in `derived/geometry_correlations.csv`; they are broad.
This is not evidence that geometry cannot matter, nor a discovered geometry
threshold for choosing models.

The BA multiplicity check reports both possible families rather than choosing
one after inspection: all four comparisons give adjusted p=0.0664 for boosting
and 0.0932 for MLP; the three-secondary family gives 0.0498 and 0.0621. Neither
family was preregistered. This sensitivity does not change the primary result.

## Figures and tables

- `main_performance.tex`: five methods, two metrics, canonical mean/CI/SD.
- `paired_results.tex`: eight canonical paired comparisons, descriptive BA W/T/L.
- `control_results.tex`: five methods in both control groups.
- `geometry_associations.tex`: four post-hoc association tests.
- `results_performance.pdf`: all 150 observed scores are plotted. Boxplot
  fliers are not separately drawn because every score already has a point.
- `results_paired_delta.pdf`: canonical BA intervals in percentage points.
- `results_rank_change.pdf`: all 30 initial/checkpoint-10 rank pairs. Symbols
  indicate selection status; they do not define a randomized optimizer ablation.

Each graph is an individual Matplotlib figure with embedded TrueType text.
No plot truncates the plotted observations. The results figures are required
source assets, not the compiled manuscript PDF. The ignore-file update permits
these three exact PDFs while retaining the exclusion of build outputs.

## Bibliography and editorial status

Three references are appended without changing the 27 prior records:
Holm (1979), Spearman (1904), and Phipson/Smyth (2010). Metadata was checked
against the original JSTOR records and publisher/PubMed record. Access to the
full article rendering was limited by the publisher pages; no extended direct
quotation or unverified paper-specific theorem is introduced.

The compiled document uses standard IEEEtran journal layout, not a verified
final TQE production class. It remains a partial manuscript without final
abstract, author block, affiliations, funding or submission metadata.
Results report observations and bounded interpretations; Discussion is Pass 5.

AI-assistance record: ChatGPT drafted Section V, supporting sources, result
analysis and delivery tooling. Human authors remain responsible for verifying
claims, numerical conventions, authorship and IEEE disclosure requirements.

## Verification scope

The delivery records include compilation, visual page checks, prior-source
preservation and isolated upload-script tests. They do not claim any new AQSE
software suite, physical sensor measurement, QPU use or local-Mac acceptance.
One local plot-generation attempt initially failed on a filesystem permission;
permissions on the delivery workspace were corrected and figure generation
completed. The first TeX pass exposed a table line-break/bracket parsing issue;
the table generator was corrected and the final document compiled cleanly.
Neither correction changed scientific inputs or statistics.

The uploader fixture exposed CRLF whitespace warnings in the byte-identical
canonical CSV. Its original bytes are retained with a scoped Git attribute
(-text, cr-at-eol). Newly generated CSV tables use LF. This is a packaging
change only; input identity and numerical results are unchanged.
