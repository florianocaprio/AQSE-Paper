# Pass 1 evidence and editorial decisions

Review date: 2026-09-17. This record is editorial support, not part of the manuscript.

## Scope and status

This pass supplies Introduction and Related Work only. It adds no experiment, training run, prediction, TEST access, statistical reanalysis, or repository merge. The numerical summary is taken from canonical published artifacts, not recomputed in this writing pass. Spectral correlations and causal effects of QNG are not asserted.

The draft deliberately separates:

1. The live network demonstrator: simulated observations → local/network State8 → all-eight AngleScaler → VQC/TQK → classical regularized Nyström AFSE → classical MLP.
2. The 30-replica benchmark: single-sensor harmonic features → phase-direct encoding → VQC/TQK → precomputed-kernel SVC. It does not test the complete State8–AFSE–MLP path.

The network demonstrator has its own, less favorable held-out results. Those results must be reported separately if the complete demonstrator is evaluated in the later manuscript. They must not be replaced by the 0.953 benchmark mean.

## Canonical project evidence

All paths below refer to `florianocaprio/AQSE` at frozen commit `0ed58cfd4a1680ee111f91bb44af7ab101d4c01a`.

| Draft statement | Source path | Boundary |
| --- | --- | --- |
| Implemented network, State8, AFSE, compact MLP, explicit training, versioned bundles | `docs/final-delivery.md` | Delivery record, not proof of field validity |
| Benchmark uses fresh white-noise-regime episodes and central harmonic feature window | `backend/app/paper_study/datasets.py` | Single-sensor task, not network-context benchmark |
| Scaler TRAIN-only; QNG bank up to 32; SVC fitted to full TRAIN; validation-only selection | `backend/app/paper_study/study.py` | No paired fixed-versus-trained TEST ablation established by this protocol |
| Main N=30 and controls 12+12; primary RBF criterion | `paper/replicated-study-2026/protocol_snapshot.json` | Protocol versioned in the repository before execution; no external preregistration identifier is asserted |
| Mean TQK and RBF balanced accuracies, paired interval and Wilcoxon p-value | `paper/replicated-study-2026/aggregate_statistics.json` | Use `method_statistics` and `paired_statistics`; do not mix differently seeded duplicate summaries in the report |
| Labels permuted only in TRAIN; VALIDATION remains supervised | `backend/app/paper_study/study.py` | Limited training-signal ablation; retained supervision is verified, its quantitative causal effect is not |
| Main kernel and score records | `paper/replicated-study-2026/replicas.csv`, `kernel_diagnostics.csv`, `main_study.json` | Saved metrics/diagnostics are not fresh experiments |
| Recovery provenance and canonical package | `docs/validation/paper-replicated-study.md` | Cite recovery v2, not the non-canonical v1 package |

The earlier `docs/architecture/canonical-aqse-pipeline.md` is a Milestone 1C design snapshot. It is not used as current implementation evidence because its capability status is outdated.

Primary manuscript numbers, before rounding:

- TQK balanced accuracy: 0.9527777777777777.
- RBF-SVC balanced accuracy: 0.9569444444444444.
- Paired TQK minus RBF delta: -0.004166666666666652.
- Bootstrap interval from `paired_statistics`: [-0.022222222222222192, 0.012500000000000015].
- Two-sided Pratt Wilcoxon p: 0.932805434372276.

These are rounded to four decimal places for effect estimates and three for p in the introduction. The result is not an equivalence or non-inferiority finding. No multiplicity-sensitive secondary superiority claim is made in Pass 1.

## Literature-to-claim map

Published records and original-author sources were checked. The URLs below identify the primary source used to verify the publication or claim. DOI fields are preserved in `bibliography.bib`; the standard IEEEtran bibliography style displays DOI URLs.

| BibTeX key | Verified source | Claim used |
| --- | --- | --- |
| `hall1997fusion` | https://ieeexplore.ieee.org/document/554205/ | Multisensor information fusion as measurement-processing context |
| `degen2017sensing` | https://doi.org/10.1103/RevModPhys.89.035002 | Physical quantum sensing is distinct from encoding classical readout features |
| `schuld2019feature` | https://doi.org/10.1103/PhysRevLett.122.040504 | Quantum feature maps and kernel learning |
| `havlicek2019supervised` | https://doi.org/10.1038/s41586-019-0980-2 | Quantum-enhanced feature-space experiment, not universal predictive superiority |
| `huang2021power` | https://doi.org/10.1038/s41467-021-22539-9 | Classical access to training data matters in advantage comparisons |
| `alvarez2025benchmarking` | https://tqe.ieee.org/2025/02/13/benchmarking-quantum-machine-learning-kernel-training-for-classification-tasks/ | Direct TQE precedent comparing kernel estimation/training; task-dependent training effects |
| `schnabel2025scrutiny` | https://doi.org/10.1007/s42484-025-00273-5 | Design and hyperparameter effects in quantum-kernel benchmarking; volume 7, article 58 |
| `williams2001nystrom` | https://www.research.ed.ac.uk/en/publications/using-the-nyström-method-to-speed-up-kernel-machines/ | Classical landmark approximation; proceedings volume 13, pp. 682–688, publication 2001 |
| `stokes2020qng` | https://quantum-journal.org/papers/q-2020-05-25-269/ | Geometry-aware parameter optimization through the quantum geometric tensor |
| `liu2021rigorous` | https://doi.org/10.1038/s41567-021-01287-z | Constructed learning separation under a hardness assumption |
| `glick2024covariant` | https://doi.org/10.1038/s41567-023-02340-9 | Group structure as a kernel-design inductive bias |
| `shin2026tensor` | https://doi.org/10.1103/c53t-rybw | Entangled tensor-kernel characterization; published 2026 version, not only the 2025 preprint |
| `schuld2021encoding` | https://doi.org/10.1103/PhysRevA.103.032430 | Encoding controls accessible Fourier structure |
| `hubregtsen2022training` | https://doi.org/10.1103/PhysRevA.106.042431 | Trainable embedding kernels and kernel-target alignment; published in Physical Review A |
| `rodriguez2025neural` | https://doi.org/10.1103/xphb-x2g4 | QNN-trained quantum kernels; distinct from AQSE's classical downstream MLP |
| `mcclean2018barren` | https://doi.org/10.1038/s41467-018-07090-4 | Conditional gradient-concentration result, not diagnosis of an arbitrary eight-qubit model |
| `thanasilp2024concentration` | https://doi.org/10.1038/s41467-024-49287-w | Kernel-concentration mechanisms and estimation limitations |
| `shaydulin2022bandwidth` | https://doi.org/10.1103/PhysRevA.106.042407 | Input/kernel bandwidth affects generalization |
| `bowles2024benchmarking` | https://arxiv.org/abs/2403.07059 | Benchmark design dependence; explicitly cited as a preprint |
| `cawley2010selection` | https://www.jmlr.org/papers/v11/cawley10a.html | Finite-sample model-selection bias and performance evaluation |
| `rahimi2007random` | https://proceedings.neurips.cc/paper/2007/hash/013a006f03dbc5392effeb8f18fda755-Abstract.html | Random features for stationary classical kernels |
| `aqse2026canonical` | https://github.com/florianocaprio/AQSE/tree/0ed58cfd4a1680ee111f91bb44af7ab101d4c01a | Frozen project code, protocol and canonical results |

The related-work section is focused rather than a systematic review. It does not claim exhaustive coverage or priority for quantum kernel benchmarking, Nyström approximation, or QNG. The 2025 TQE benchmark is discussed explicitly because it overlaps the intended contribution.

## Journal and template checks

- Official submission page: https://tqe.ieee.org/submission-process/ . The journal states no page limit. Any 12–16-page target discussed in project planning is an internal writing budget, not a journal rule.
- Official template guide: https://journals.ieeeauthorcenter.ieee.org/wp-content/uploads/sites/7/TQE_Template_v4.pdf . This is the TQE Word-oriented guide, including general abstract, reference, and layout instructions. It points to a separate LaTeX-template resource.
- A TQE-specific LaTeX class/archive was not successfully retrieved in this pass. The review source therefore uses the installed unmodified `IEEEtran` journal class. This is stated explicitly rather than labelling a generic class as a verified TQE production template.
- The working manuscript has only the two requested sections. Author information, abstract, index terms, funding, full results, limitations, acknowledgments, and final journal production metadata remain for subsequent passes.
- Local compilation completed with pdfLaTeX and BibTeX using the unmodified IEEEtran class and bibliography style. The three-page PDF was rendered and inspected on every page. No unresolved citations, references, or overfull boxes remain. Three underfull-box warnings arise from narrow-column text/URLs. They do not clip content. The container's generic `bibtex` symlink was unavailable; the installed `bibtex.original` binary was used for this local check. Standard BibTeX commands remain correct for Overleaf and a normal TeX installation.

## Style and claim checks

- Direct academic English; no em-dashes or decorative transition adverbs.
- No claim that a high empirical kernel rank proves computational hardness, entanglement, causal identification, or scaling advantage.
- No claim that a loss decrease or a changed Gram spectrum proves QNG improves generalization.
- No claim that 16 VQC parameters fully describe the predictor capacity. The SVC is a separately fitted component.
- No claim that RFF-256 matches the capacity of a fidelity kernel merely because an eight-qubit state has 256 amplitudes.
- No claim that the published report itself constitutes a new independent statistical reproduction by the drafting assistant.

## AI-use record

Tool: ChatGPT. Task: literature search assistance, first drafting of Introduction and Related Work, bibliography preparation, source organization, and LaTeX compilation checks. Date: 2026-09-17.

Human scientific and bibliographic review is pending. Human authors remain responsible for all submitted content; the system is not an author. Before submission, reconcile the disclosure with the latest IEEE policy and the final extent of AI assistance:

https://open.ieee.org/author-guidelines-for-artificial-intelligence-ai-generated-text/

Suggested acknowledgment to finalize after author review:

> ChatGPT was used to assist in drafting and editing the Introduction and Related Work and in organizing the bibliography. The authors verified the cited sources and revised the text. The authors are responsible for the content of the manuscript.

The sentence asserting author verification must be used only after that verification has occurred. This draft note is not a substitute for the final acknowledgment.
