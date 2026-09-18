<h1 align="center">AQSE</h1>
<p align="center"><b>A Hybrid Quantum&ndash;Classical Framework for Contextual Sensor-Network Representation</b></p>

<p align="center">
  <a href="https://florianocaprio.github.io/AQSE-Paper/"><img src="https://img.shields.io/badge/site-live-38bdf8" alt="Site"></a>
  <img src="https://img.shields.io/badge/paper-IEEE%20TQE%20(in%20preparation)-fbbf24" alt="Paper status">
  <img src="https://img.shields.io/badge/corpora-30%20independent-a78bfa" alt="Corpora">
  <img src="https://img.shields.io/badge/qubits-8-0ea5e9" alt="Qubits">
</p>

**Site:** https://florianocaprio.github.io/AQSE-Paper/

AQSE is a hybrid quantum&ndash;classical framework for contextual sensor-data representation. It separates observations, eight-dimensional feature profiles, quantum encoding, and classical prediction, and evaluates a trainable eight-qubit fidelity kernel (TQK) on a controlled magnetometer task. This repository holds the complete IEEE Transactions on Quantum Engineering (TQE) manuscript source, the analysis inputs/outputs behind its reported numbers, and the editorial audit trail of every revision pass.

## Authors

Floriano Caprio<sup>1,\*</sup>, Matteo Tortora<sup>2</sup>, Paolo Soda<sup>1,3</sup>, and Sunil Gentyala<sup>4</sup>

1. Unit of Artificial Intelligence and Computer Systems, Universit&agrave; Campus Bio-Medico di Roma, Italy
2. Department of Naval, Electrical, Electronics and Telecommunications Engineering, University of Genoa, Italy
3. Department of Diagnostics and Intervention, Biomedical Engineering and Radiation Physics, Ume&aring; University, Sweden
4. HCL Technologies, United States

\* Corresponding author: Floriano Caprio ([f.caprio@unicampus.it](mailto:f.caprio@unicampus.it))

Affiliation wording and order are those provided by the corresponding author. No IEEE membership grades, ORCIDs, funding, or conflict-of-interest statement have been invented; see `editorial/submission-checklist.md` for the declarations that remain open.

## Headline result

An eight-qubit variational circuit with 16 trainable parameters (TQK), optimized by quantum natural gradient and read out through an SVC, is compared against an RBF-SVC baseline across 30 independently generated, repository-preregistered corpora (120 episodes each: 72 train / 24 validation / 24 test).

| Model | Mean test balanced accuracy |
|---|---|
| TQK-SVC (quantum kernel) | 0.9528 |
| RBF-SVC (baseline) | 0.9569 |

Paired difference: &minus;0.0042 (95% bootstrap CI [&minus;0.0222, 0.0125]); two-sided Wilcoxon p = 0.9328. **The preregistered predictive-advantage criterion was not met.** All quantum computations use exact classical statevector simulation &mdash; no QPU or physical sensor deployment is evaluated. Full context is in `sections/05_results.tex` and the [site](https://florianocaprio.github.io/AQSE-Paper/#results).

## Scientific boundary

- The network **State8&ndash;AFSE&ndash;MLP** demonstrator and the single-magnetometer harmonic **TQK-SVC** benchmark are separate routes; the 30 corpora test only the latter.
- The TRAIN-label control keeps validation supervision and reuses one teacher dataset &mdash; it is a partial training-signal ablation, not a fully label-null experiment.
- Reported QNG trajectories lack TEST evaluations for the unselected initial models.
- No hardware advantage, field-deployment validity, or causal training benefit is claimed.

Revision passes (tracked in `editorial/`) have only ever defined acronyms, disambiguated units, standardized route/figure names, or removed unsupported references &mdash; never changed a frozen estimate, added an unreported experiment, or altered a displayed equation. `analysis/pass4/` is the single source of truth for every number in the manuscript.

## Repository layout

```
frontmatter/    approved author metadata, abstract, and index terms
sections/       01_introduction .. 08_conclusion, plus availability & acknowledgment
figures/        2 TikZ sources + 3 generated result PDFs
tables/         7 method and result tables
bibliography.bib  30 reference records
analysis/pass4/   inputs, reproduce_results.py, and derived outputs behind every reported number
editorial/      pass-by-pass evidence/decisions log and the author submission checklist
main.tex        root document (IEEEtran journal class, 10pt)
```

## Build

Select `main.tex` as the root document. The source uses the unmodified IEEEtran journal class at 10&nbsp;pt, standard margins, pdfLaTeX, BibTeX, and TikZ. Compilation does not run Python, AQSE, Docker, simulations, or the report-only analysis.

```sh
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Overleaf and a normal TeX Live/MacTeX installation provide the required packages.

## Reproducing the reported numbers

```sh
cd analysis/pass4
python reproduce_results.py
```

The script reads `inputs/` (frozen replicas, aggregate statistics, control summary) and regenerates `derived/` (descriptive metrics, paired comparisons, geometry correlations, results audit) byte-identically to what is cited in the manuscript.

## Status

This is the complete manuscript **prepared for author approval** &mdash; not a declaration that all submission-portal requirements or all co-author approvals are complete. The TQE submission page, author-template guidance, and AI-content policy were checked; TQE states it has no page limit, and the document follows a standard IEEE journal review layout without impersonating the publisher's typeset version. The interactive IEEE template selector did not return a downloadable TQE LaTeX archive during this review, so the current portal/template must be confirmed at upload. Authors must still review the manuscript and acknowledgment, supply ORCIDs where requested, and confirm funding/conflict declarations. No submission or publication license is executed by this repository. See `editorial/submission-checklist.md` for the full list.

## Citing this work

A citable record (DOI, venue, and page numbers) will be added here once the manuscript is accepted. Until then, cite the repository itself &mdash; see [`CITATION.cff`](CITATION.cff).

## Git and Overleaf

The paper was integrated on `paper/ieee-tqe-v1` and merged into `main` at the tagged snapshot `tqe-submission-v1`. Do not assume Overleaf automatically imports a review branch; pull the agreed synchronized branch into the linked Overleaf project after any merge.
