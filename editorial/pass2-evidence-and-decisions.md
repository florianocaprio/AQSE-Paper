# Pass 2: source-to-equation audit and editorial decisions

Date: 2026-09-17. Target journal: IEEE Transactions on Quantum Engineering.
Status: partial manuscript, Sections I-III. This is not a submission-ready paper.

## Pinned sources

- Manuscript input: `florianocaprio/AQSE-Paper`, commit
  `a96f1bc067c7c1bfbd9be9f77eb3f19c0ebe85ec`, branch `paper/ieee-tqe-v1`.
- Scientific implementation and published artifacts: `florianocaprio/AQSE`, commit
  `0ed58cfd4a1680ee111f91bb44af7ab101d4c01a`.
- The 30-replica experiment itself used source commit
  `091acf2e98b2b88720730eea276e253f0c96f5a6`. The later merge is the repository
  snapshot that contains code and recovered results. These identities are not interchangeable.
- The protected `tqk8.py` SHA-256 used for equation checks is
  `cef11f0d0617e5e12b2904c0aa65868ef655a853db48a99c73a803440d371689`.

All seven local Pass 1 payloads were checked against their published Git blob
identities before integration. Sections I and II are unchanged byte-for-byte.
The existing IEEEtran journal class and bibliography filename are retained.
No author, affiliation, funding, ORCID, or final abstract was invented.

## Source map

All paths below are relative to the scientific repository at the pinned merge.

| Manuscript material | Authoritative implementation |
| --- | --- |
| State preparation, path edges, 16 parameters, overlap circuit | `backend/app/quantum/user_pipeline/tqk8.py`: `build_vqc`, `overlap_circuit` |
| AngleScaler, population variance, scale floor | same file: `AngleScaler.fit`, `AngleScaler.transform` |
| Exact wavefunction shift prefactor, both overlap derivatives | same file: `StateEngine.differential`, `loss_grad_metric` |
| Centered alignment and norm rejection | same file: `alignment_loss` |
| Full empirical FS metric, damping, norm bound, Armijo | same file: `loss_grad_metric`, `fit_qng` |
| Observation rotation and initial observed means | `backend/app/features/state8.py`: `_world_north_nt`, observed-reference construction |
| Four-second features and peer requirements | same file: `_common_features`, `_record`, `_band_power_ratio_db` |
| Harmonic feature names and actual units | `backend/app/preprocessing/features.py`: `MAGNETOMETER_FEATURE_UNITS`, `extract_magnetometer_features` |
| Binary objective used in the four-class demonstrator | `backend/app/demo/evaluation.py`: `fit_demo_task_candidates` |
| Separate local/network task classes and budgets | `backend/app/demo/protocol.py` |
| Symmetric ridge Nyström basis and residual | `backend/app/embeddings/nystrom.py`: `_regularized_basis`, `_embedding_and_residuals` |
| Balanced landmarks, distinct lineages, reduced reference size | same file: `_select_landmark_indices` |
| TRAIN empirical p99 threshold, query invariance | same file: `fit_nystrom_afse`, `NystromAFSE.transform` |
| Numeric MLP inference and score thresholds | `backend/app/classical/mlp.py`: `NumpyMLPClassifier`, `uncertainty_gate` |
| Runtime scope, restart behavior, buffers and bundle semantics | `docs/final-delivery.md` plus the component contracts above |
| Direct-kernel study with no AFSE | `backend/app/paper_study/study.py`, `backend/app/paper_study/datasets.py` |

Representative source URLs:

- https://github.com/florianocaprio/AQSE/blob/0ed58cfd4a1680ee111f91bb44af7ab101d4c01a/backend/app/quantum/user_pipeline/tqk8.py
- https://github.com/florianocaprio/AQSE/blob/0ed58cfd4a1680ee111f91bb44af7ab101d4c01a/backend/app/features/state8.py
- https://github.com/florianocaprio/AQSE/blob/0ed58cfd4a1680ee111f91bb44af7ab101d4c01a/backend/app/embeddings/nystrom.py
- https://github.com/florianocaprio/AQSE/blob/0ed58cfd4a1680ee111f91bb44af7ab101d4c01a/backend/app/demo/evaluation.py

## Decisions that prevent scientific conflation

1. **State8 is not the harmonic profile.** State8 scales all eight features. The
   harmonic benchmark overrides coordinate 1 with wrapped observed phase.
   The 7th harmonic coordinate `spectral_peak` is a peak PSD in nT^2/Hz,
   not another frequency. Its actual units were checked against the extractor.
2. **A node is not a qubit.** Eight features represent one analysis window.
   Node count, measured channels, and qubit count are independent quantities.
3. **The two graphs in the manuscript are schematic source descriptions.** The
   circuit figure preserves every gate and CZ ordering. Its sequential drawing
   is not a claim about compiled hardware depth or hardware scheduling.
4. **The state derivative has denominator 2 sqrt(2).** Substituting the
   probability parameter-shift prefactor 1/2 would be incorrect here.
5. **The QNG geometry is the full empirical mean FS matrix.** No QFI factor of
   four is inserted. No uniqueness claim about the natural metric of the SVC
   or kernel matrix is made.
6. **The network representation is trained with a binary surrogate.** Only
   environment-compatible and device-compatible examples enter its QNG bank.
   The final MLP still learns all four network classes. We do not describe this
   as joint four-class end-to-end quantum-neural optimization.
7. **Nyström coordinates use the stored symmetric inverse square root.** The
   implementation is K_XZ B, not an arbitrarily rotated eigenvector coordinate
   map. This matters because the MLP is tied to the actual frozen coordinates.
8. **AFSE dimension is recorded, not always assumed.** Requested dimension 32,
   reduced with insufficient balanced lineage support. It is m for m landmarks.
9. **Residual is not calibrated OOD probability.** The empirical threshold uses
   TRAIN residuals including landmarks. It does not identify physical causes.
10. **No unpublished spectral-performance result is inserted.** Pass 2 defines
    the model. Statistical inference belongs in later sections and must be
    supported by the persisted study evidence.

## Mathematical definitions and scope

The manuscript translates the implementation into notation. Hilbert--Schmidt
positive semidefiniteness, the cancellation of a common terminal unitary, and
z(x)^T z(x') = k_Z(x)^T B^2 k_Z(x') are direct mathematical consequences of the
specified formulas. They are not new experimental claims. No claim of quantum
advantage, classical intractability, improved sensor sensitivity, physical QPU
execution, or field-deployment validity is made.

The original generic fidelity-kernel equation in Related Work is referenced
rather than relabelled, avoiding duplicate LaTeX labels. Figure 1 separates
frozen inference from the explicit training loop and shows the state-derivative
route to the FS metric independently of the loss-gradient route.

## Primary literature verified for this pass

- J. Stokes, J. Izaac, N. Killoran, and G. Carleo, "Quantum natural gradient,"
  Quantum, vol. 4, p. 269, 2020, DOI 10.22331/q-2020-05-25-269.
  https://quantum-journal.org/papers/q-2020-05-25-269/
- C. Cortes, M. Mohri, and A. Rostamizadeh, "Algorithms for learning kernels
  based on centered alignment," JMLR, vol. 13, pp. 795-828, 2012.
  https://www.jmlr.org/papers/v13/cortes12a.html
- C. K. I. Williams and M. Seeger, "Using the Nyström method to speed up kernel
  machines," Advances in Neural Information Processing Systems 13,
  pp. 682-688, 2001. Author-institution record:
  https://www.inf.ed.ac.uk/publications/report/1036.html

Only the Cortes reference is new in the bibliography. Existing verified
references retain their keys. The specific ridge, clipping thresholds, and
residual rule are AQSE implementation choices, not claims about what the
original Nyström paper prescribes.

## Independent editorial checks

Synthetic fixtures only. No experimental dataset, TEST file, classifier fit,
optimizer update, or QPU job was used. The protected NumPy state engine was
checked against a separate dense-gate construction. Finite differences checked
the wavefunction and loss derivatives. A projected-derivative expression
checked the FS metric. A linear solve checked the Nyström inverse identity.
Qiskit was not installed in this editorial runtime and was not re-executed.
Historical Qiskit checks are not attributed to this pass.

Measured maximum absolute differences:

| Check | Difference |
| --- | ---: |
| Gate sequence versus independent dense matrices | 1.6653345369377348e-16 |
| Wavefunction shift derivative versus finite difference | 2.782956065303299e-10 |
| Centered-alignment expression | 0.0 |
| Loss gradient versus finite difference | 1.4984936208550792e-10 |
| Mean FS metric versus projected derivatives | 9.236192399485706e-17 |
| Nyström induced kernel versus ridge linear solve | 1.7208456881689926e-15 |
| Query reordering | 0.0 |

These are equation-consistency checks on a fixed synthetic fixture. They are
not additions to the preregistered study, nor evidence of predictor accuracy.
The delivery archive includes the check script and machine-readable results.

## Remaining manuscript work

Pass 3 must describe harmonic feature extraction, experimental seeds, actual
selection budgets, and the TRAIN-only label-permutation control in detail.
Results and Discussion must distinguish the replicated component benchmark
from the network demonstrator. No manuscript completeness or final TQE
production-template claim is implied by the successful partial compilation.
The author must review the equations and their fidelity to the intended method.
The AI-assistance disclosure remains an author-verified submission item, as
recorded in the Pass 1 editorial file.
