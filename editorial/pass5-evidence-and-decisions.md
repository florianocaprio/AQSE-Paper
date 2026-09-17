# Pass 5: interpretation, limitations, and conclusions

Date: 2026-09-17. Target: IEEE Transactions on Quantum Engineering.
Status: core manuscript text completed through Section VIII. Abstract, author
information, submission-specific formatting and final editorial integration are
not completed by this delivery.

## Pinned evidence and preservation

- Manuscript input: `florianocaprio/AQSE-Paper`, branch `paper/ieee-tqe-v1`,
  commit `1ffa0eaf2187a708ca897e6877a6e60f7ea2622e`.
- Git tree returned for that commit: `b1b6bb79ba68dd80e34c370537c7b69a075f92a2`.
  A local reconstruction of all 37 input files produced that exact tree SHA.
- Scientific execution: `florianocaprio/AQSE`, commit
  `091acf2e98b2b88720730eea276e253f0c96f5a6`.
- Published scientific code-and-results snapshot:
  `0ed58cfd4a1680ee111f91bb44af7ab101d4c01a`.
- Reporting-only recovery: `d42965ef6a38791fcdbdc1b7bbb3750a58d1f2f1`.
- Existing result-only manuscript analysis: `analysis/pass4/` at the input
  manuscript revision. Its inputs, script, output records and figures remain
  byte-identical. It was not re-executed in Pass 5.

This pass adds `sections/06_discussion.tex`, `sections/07_limitations.tex`,
`sections/08_conclusion.tex`, and this editorial note. Only `main.tex` and
`README.md` are updated among the existing files. Sections I-V, all 30 bibliography
entries, both TikZ sources, three PDF figures, seven tables, and all previous
editorial notes are unchanged.

## Source-to-interpretation map

| New material | Evidence | What is not inferred |
| --- | --- | --- |
| Primary comparison and its scope | Sections IV.A and V.A; `analysis/pass4/inputs/aggregate_statistics.json` | Equivalence, universal quantum/classical ordering, probability that the null is true |
| Signal available to multiple model families | Sections IV.B, IV.D and V.B; `tables/benchmark_protocol.tex` | A newly evaluated SNR or variance classifier |
| Mean ordering and secondary evidence | Section V.B; `tables/paired_results.tex` | A retrospective confirmatory winner or a newly chosen multiplicity family |
| Rank-one and identity distinctions | Section V.C; stored selected kernel summaries | Expressivity, entanglement, class separability, or asymptotic concentration behavior |
| Distinct state, alignment and Gram geometries | Section III.D, equations for the empirical FS metric and centered alignment; Section IV.G | The FS metric being a unique natural metric for the SVC |
| 19 initial and 11 updated selections | Section V.C; `kernel_initial_selected_final.csv` | 19 failed optimizations or 11 demonstrated TEST improvements |
| Missing QNG ablation | Sections IV.D, IV.G and V.C | TEST predictions for unselected checkpoints or an ordinary-gradient arm |
| Larger observed TQK dispersion | Section V.B; `descriptive_metrics.csv` | A variance significance test or causal attribution to optimizer, split or initialization |
| Unresolved geometry-performance relationships | Section V.D; `geometry_correlations.csv` | Proof of independence or absence of nonlinear/weak relationships |
| Negative control above chance | Sections IV.E and V.E; `control_summary.json` | Established TEST leakage, or a completed full-label-null control |
| Shared negative-control corpus | Section IV.E; execution and control factory recorded in Pass 3 | Twelve newly generated negative-control corpora |
| Mechanism-aligned positive control | Sections IV.E and V.E | Quantum-exclusive representation, physical-sensor evidence, or exact teacher/student equivalence |
| AFSE and live inference limits | Section III.E-F, `aqse2026canonical` | Quantum AFSE algorithm, calibrated confidence, causal fault identification, automatic continual learning |
| Timing and software scope | Sections IV.H and V.F | Method-specific speedup, QPU evidence, independent replication from report recovery |
| Follow-up studies | Explicit research proposals in Section VI.F | Experiments executed or authorized by this writing task |

Sections VI-VIII synthesize the already reported evidence. No training, simulator
run, quantum-state evaluation, prediction, TEST-array read, resampling analysis,
new metric or post-hoc hypothesis test is performed in this pass.

## Interpretation decisions

1. Preserve the primary null finding. No equivalence or non-inferiority margin
   is introduced retrospectively.
2. Distinguish high absolute performance from an incremental quantum benefit.
   The engineering framework is not evidence of an advantage of its quantum
   component.
3. Treat spectral changes as observations of finite Gram matrices. The statement
   that eigenvalue summaries do not determine label alignment follows directly
   from their definitions; it is not presented as a new theorem or experiment.
4. Do not label checkpoint 0 selections as failed training. The tie rule favors
   earlier checkpoints, and the archive lacks matched TEST scores for unselected
   initial models.
5. Retain the failed chance-compatibility check. Remaining validation supervision
   is a plausible explanation, not a diagnosed cause. The existing control is
   neither silently repaired nor reclassified as successful.
6. Keep the teacher controls separate from the sensor task, and the sensor task
   separate from the full State8-AFSE-MLP network demonstrator.
7. Do not claim that this run is free of every possible leakage path. The local
   ledger guards a designated sequence; it is not a secure holdout service.
8. Keep proposed matched ablations, full-label controls, physical-sensor tests,
   and hardware studies in the future tense. No new experiment is needed to
   truthfully report the completed experiment, and no new one is launched here.
9. Avoid new claims based on prior chat descriptions or related AQSE experiments
   whose outcome was not incorporated in the Results. No earlier favorable or
   unfavorable network score is pooled with the 30 primary replicas.

## Literature support checked for the new prose

The bibliography is unchanged. These primary-source records were checked for
the concepts cited in the new discussion:

- Alvarez-Estevez, TQE 2025: direct empirical quantum-kernel benchmarking context.
  https://tqe.ieee.org/2025/02/13/benchmarking-quantum-machine-learning-kernel-training-for-classification-tasks/
- Schnabel and Roth, Quantum Machine Intelligence 2025: design-dependent kernel
  performance and the role of preprocessing and model choices.
  https://link.springer.com/article/10.1007/s42484-025-00273-5
- Liu, Arunachalam and Temme, Nature Physics 2021: a learning separation for a
  specified construction, not a general claim about sensor data.
  https://www.nature.com/articles/s41567-021-01287-z
- Stokes et al., Quantum 2020: state-space quantum natural gradient.
  https://quantum-journal.org/papers/q-2020-05-25-269/
- Cortes, Mohri and Rostamizadeh, JMLR 2012: centered kernel alignment.
  https://www.jmlr.org/papers/v13/cortes12a.html
- Cawley and Talbot, JMLR 2010: finite-sample model-selection effects. This is
  background, not evidence that selection caused AQSE's observed variation.
  https://www.jmlr.org/papers/v11/cawley10a.html
- Thanasilp et al., Nature Communications 2024: concentration and estimation
  requirements under specified assumptions.
  https://www.nature.com/articles/s41467-024-49287-w
- Williams and Seeger, NIPS 2000 proceedings: classical Nyström approximation.
  https://papers.nips.cc/paper_files/paper/2000/hash/19de10adbaa1b2ee13f77f679fa1483a-Abstract.html

No source is cited for a property not established by that source. AQSE-specific
limitations are supported by the source-to-method and source-to-result audits,
not by extrapolating another paper's experimental outcomes.

## Final integration still required

- Obtain the human-approved author order, affiliations, corresponding author,
  contact details, ORCIDs, funding and conflict declarations. Do not infer them.
- Write and verify the abstract and Index Terms against the completed text.
- Reconcile the exact current TQE submission template and author instructions.
  The present class is unmodified `IEEEtran` in journal mode, not a claimed
  TQE-specific production template.
- Remove the working-draft banner only when author and submission metadata are
  complete. Check figure readability, equation notation, bibliography and all
  cross-references after any final layout change.
- Confirm data/code availability wording and final public repository snapshot.
  Distinguish experiment, recovery, scientific-publication and manuscript SHAs.
- Finalize the journal-required AI-assistance disclosure with the authors. Do not
  list an AI system as an author.
- Review alignment between title, abstract, Results and Conclusions, keeping the
  component-level scope and unsuccessful control visible.
- Merge or synchronize Overleaf only after explicit author approval. This delivery
  neither creates a PR nor changes `main` or tags.

## Assistance and validation record

ChatGPT drafted these three English sections and prepared the cumulative LaTeX
package using the cited sources and the released manuscript. The authors remain
responsible for verification, interpretation and the submitted wording. This note
records assistance; it is not itself the final acknowledgment for the manuscript.

Technical checks, compilation logs, file identities and actual local uploader
fixture results are supplied in the delivery package, outside the manuscript
source tree. No unperformed test should be marked as passed.
