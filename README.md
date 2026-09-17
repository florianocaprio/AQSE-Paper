# AQSE manuscript for IEEE Transactions on Quantum Engineering

## Current draft

Passes 1 and 2 are integrated: Introduction, Related Work, and AQSE Framework.
This is a partial working draft in English, not a submission-ready manuscript.
The scientific data repository remains separate from this manuscript repository.

- Manuscript branch: `paper/ieee-tqe-v1`.
- Input manuscript revision for Pass 2: `a96f1bc067c7c1bfbd9be9f77eb3f19c0ebe85ec`.
- Scientific source snapshot: `0ed58cfd4a1680ee111f91bb44af7ab101d4c01a`.
- Experimental execution revision: `091acf2e98b2b88720730eea276e253f0c96f5a6`.

The two existing prose sections are unchanged. The framework, two TikZ vector
figures, one State8 table, and one bibliography entry have been added.
`editorial/pass2-evidence-and-decisions.md` maps equations to source code.

## Files and compilation

Open `main.tex` as the root document. Use pdfLaTeX and BibTeX with the unmodified
`IEEEtran` journal class and `IEEEtran` bibliography style. TikZ draws both
figures directly, so there are no external image or shell-escape dependencies.
A standard TeX Live / MacTeX installation or Overleaf supplies these packages.

```sh
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The download delivery includes a separate `compila_pdf.sh`; it is not committed
into the manuscript. Figures can be edited in `figures/`, the table in `tables/`.
Generated PDFs, auxiliary files, download scripts, and ZIP packages do not belong
in this source branch. Do not add dataset archives to this manuscript repository.

## Template and editorial status

This draft uses `IEEEtran` in journal mode. It does not claim to be the final
TQE-specific production template. Check the journal's current template and
submission instructions before submission. Abstract, authors, affiliations,
funding, ORCIDs, remaining sections, and final AI-assistance disclosure require
later integration and author approval.

English style: concise academic prose, no em-dashes, no promotional language.
Numbers and equations must be tied to evidence. The network State8--AFSE--MLP
path must not be described as the path evaluated by the 30-replica harmonic
TQK--SVC benchmark. No hardware advantage or field validity is claimed.

## Update workflow

All writing passes remain on `paper/ieee-tqe-v1`. The downloadable upload script
checks the exact prior revision and file content, then stages only the declared
manuscript files. It does not modify `main`, merge, rewrite history, or run AQSE.
Do not independently edit the same files while applying a delivery update.

Overleaf compilation and GitHub publication are separate operations. No automatic
branch synchronization is assumed. Use the generated preview PDF while the
manuscript is on the review branch, or import a separate source snapshot into a
review project. Sync the agreed main branch only after explicit merge approval.

## Writing plan

1. Introduction + Related Work: delivered.
2. AQSE Framework: delivered in this update.
3. Experimental Methodology: pending.
4. Results: pending.
5. Discussion, Limitations, Conclusions: pending.
6. Final integration, abstract, references, figures, and submission checks: pending.
