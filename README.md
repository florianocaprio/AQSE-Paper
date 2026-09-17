# AQSE manuscript for IEEE Transactions on Quantum Engineering

## Current draft

Passes 1-5 are integrated: Introduction, Related Work, AQSE Framework,
Experimental Methodology, Results, Discussion, Limitations, and Conclusions.
The core English manuscript is complete. Abstract, author information, final
editorial integration and submission checks are still pending. This is not a
submission-ready paper.

- Manuscript branch: `paper/ieee-tqe-v1`.
- Input manuscript revision: `1ffa0eaf2187a708ca897e6877a6e60f7ea2622e`.
- Scientific execution revision: `091acf2e98b2b88720730eea276e253f0c96f5a6`.
- Published scientific snapshot: `0ed58cfd4a1680ee111f91bb44af7ab101d4c01a`.
- Reporting recovery revision: `d42965ef6a38791fcdbdc1b7bbb3750a58d1f2f1`.

The five previous prose sections, all 30 bibliography records, figures,
tables, previous editorial notes, and `analysis/pass4/` are byte-identical to
the published Pass 4. This update adds three prose sections and a Pass 5 source
and interpretation audit, and changes only this README and `main.tex` among
the existing files. No scientific calculation was repeated.

New manuscript files:

```text
sections/06_discussion.tex
sections/07_limitations.tex
sections/08_conclusion.tex
editorial/pass5-evidence-and-decisions.md
```

## Compile

Use `main.tex`, pdfLaTeX and BibTeX, with the unmodified IEEEtran journal class
and bibliography style. TikZ draws the two framework diagrams. The three
results plots are included as vector PDFs, so Python is not needed to compile.
No shell escape is required.

```sh
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

A separate download script `compila_pdf.sh` provides the equivalent local
build. Generated manuscript PDFs and LaTeX auxiliary files are not committed.
Only the three named result-figure PDFs are source assets.

## Reproduce results material

`analysis/pass4/README.md` describes the result-only reconstruction. Its inputs
are two byte-identical canonical result files and two explicitly identified
extracts. It recreates tables, CSV/JSON summaries, and optionally the plots.
Original file and source identities are recorded in `input_manifest.json`.

```sh
python3 analysis/pass4/reproduce_results.py
# Optional, if NumPy, SciPy and Matplotlib are installed:
python3 analysis/pass4/reproduce_results.py --figures
```

This never imports AQSE, fits models, generates states, accesses raw TEST
arrays, or starts Docker. A separate `--canonical-root` check can compare the
extracts against the published original report directory in a local AQSE clone.
The paper's canonical statistics remain distinct from the new post-hoc tests.

## Scientific boundaries

The network State8-AFSE-MLP demonstrator is not the replicated harmonic
single-sensor TQK-SVC benchmark. The primary study has 30 new corpora. The
positive control has 12 new teacher datasets. The negative control re-splits
one teacher dataset 12 times, permutes only TRAIN labels, and retains true
VALIDATION labels for selection.

The primary predictive-advantage criterion was not met. Kernel rank and
concentration do not establish expressivity, field validity or hardware
advantage. The data do not contain TEST predictions from unselected initial
checkpoints, so they do not identify a QNG-versus-fixed-kernel TEST effect.
The extra geometry-performance associations and multiplicity sensitivities
in Section V are explicitly post hoc, with scripts and seeds included.

## Writing, template, and source workflow

Use concise academic English without em-dashes or promotional claims. Preserve
observations, hypotheses, and limitations as separate statements. Source maps
and editorial decisions are in `editorial/pass*-evidence-and-decisions.md`.

This uses IEEEtran journal mode, not a verified final TQE production template.
Final template reconciliation, author list, affiliations, ORCIDs, funding,
abstract, Index Terms and AI-assistance disclosure require author approval.

All writing passes stay on `paper/ieee-tqe-v1`. The download uploader verifies
the prior revision and allowlisted files, then performs a normal commit/push.
It does not modify main, tags, experiment code or data, and does not merge.
Avoid concurrent edits while applying a delivery. Unreviewed edits stop the
uploader rather than being overwritten.

GitHub publication does not automatically compile or synchronize Overleaf.
Use the preview PDF or a separate review project before the final approved
merge and pull into the connected Overleaf project.

## Remaining integration

Pass 6 covers the abstract, Index Terms, author-approved metadata, reference and
cross-reference review, figure/layout checks, TQE template reconciliation, data
and code availability wording, and AI-assistance disclosure. It does not authorize
new experiments or replacement of the frozen results. Merge and Overleaf sync
require explicit approval after review.
