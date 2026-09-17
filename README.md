# AQSE paper | Pass 1

Target journal: **IEEE Transactions on Quantum Engineering (TQE)**.

Title: **AQSE: A Hybrid Quantum–Classical Framework for Contextual Sensor-Network Representation**.

This branch contains the first writing pass: Introduction and Related Work. It is a working manuscript, not a submission-ready article. No new experiment or model evaluation was run for this pass.

## Files

- `main.tex`: compilable two-section review manuscript.
- `bibliography.bib`: 22 source records in IEEE numeric citation order. The existing repository filename is preserved.
- `sections/01_introduction.tex`: problem, framework, experimental boundary, contributions, and primary result.
- `sections/02_related_work.tex`: five focused subsections on kernels, optimization, concentration, evaluation, and classical interfaces.
- `editorial/pass1-evidence-and-decisions.md`: source-to-claim map, journal checks, scope constraints, and AI-use record. This file is not included in the manuscript PDF.

## Compile

Use pdfLaTeX with BibTeX, or run:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

Equivalent explicit commands:

```sh
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The draft uses the standard, unmodified `IEEEtran` journal class. It does not reproduce a verified TQE-specific production class or journal branding. The official TQE submission page and template guidance were checked; the final journal-specific submission template must be reconciled before submission. No author list, affiliations, funding, ORCIDs, abstract, publication metadata, or copyright line has been invented. The abstract and author block belong to later integration.

## GitHub and Overleaf

Development branch: `paper/ieee-tqe-v1`.

`main` is intentionally unchanged. Do not assume that Overleaf automatically imports a non-default GitHub branch. For immediate review, upload the provided source ZIP into a separate Overleaf review project and select `main.tex`. For the linked project, review and merge the manuscript branch into the synchronized GitHub branch before importing changes through the existing GitHub integration. Avoid simultaneous edits to the same files in GitHub and Overleaf. No merge is authorized by this writing pass.

## Evidence baseline

Scientific code and canonical report package: `florianocaprio/AQSE`, commit `0ed58cfd4a1680ee111f91bb44af7ab101d4c01a`.

Experiment execution commit: `091acf2e98b2b88720730eea276e253f0c96f5a6`.

Canonical package path: `paper/replicated-study-2026/`.

The 30-replica benchmark tests a single-sensor harmonic white-noise task with TQK-SVC. It must not be described as a 30-replica evaluation of the full network State8–AFSE–MLP demonstrator. The two paths are distinguished in the text. The primary advantage criterion was not met. Spectral observations and retained validation supervision in the training-label permutation control require separate interpretation.

## Writing policy

Concise academic English. No em-dashes, promotional claims, or generic transition filler. Distinguish empirical observations, theoretical guarantees, and hypotheses. Preserve the primary preregistered conclusion. Do not equate absence of a detected difference with equivalence. Cite published versions where verified and label preprints explicitly.

## AI-use and author review

ChatGPT generated this first English draft and its source organization using the cited literature and repository records. Human authors must verify the argument, references, data interpretation, and final wording. An IEEE-compliant acknowledgment of AI-generated content must be finalized before submission. The disclosure record and suggested wording are in `editorial/pass1-evidence-and-decisions.md`.
