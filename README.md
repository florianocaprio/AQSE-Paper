# AQSE manuscript for IEEE Transactions on Quantum Engineering

## Complete author-review manuscript

The integrated English manuscript contains an abstract, Index Terms, the eight
scientific sections, data/code availability, an AI-assistance acknowledgment,
and the reference list. The review banner and empty author block have been removed.
This is the complete manuscript prepared for author approval, not a declaration
that all submission-portal requirements or all coauthor approvals are complete.

- Branch: `paper/ieee-tqe-v1`.
- Input manuscript commit: `687978b9f7ca86f4250bef5b3314e5d9681be8eb`.
- Scientific execution: `091acf2e98b2b88720730eea276e253f0c96f5a6`.
- Published scientific snapshot: `0ed58cfd4a1680ee111f91bb44af7ab101d4c01a`.
- Reporting-only recovery: `d42965ef6a38791fcdbdc1b7bbb3750a58d1f2f1`.

## Confirmed authors

Floriano Caprio (affiliation 1, corresponding author), Matteo Tortora (2),
Paolo Soda (1, 3), and Sunil Gentyala (4). Affiliation wording and order are those
provided by the corresponding author. The confirmed email is
`f.caprio@unicampus.it`. See `frontmatter/authors.tex`.

No IEEE membership grades, ORCIDs, funding, conflict-of-interest statement,
publisher copyright, manuscript number, received date, or DOI have been invented.
See `editorial/submission-checklist.md` for the remaining author declarations.

## Build

Select `main.tex` as the root document. The source uses the unmodified IEEEtran
journal class at 10 pt, standard margins, pdfLaTeX, BibTeX and TikZ. The three
result figures are included as vector PDFs. Compilation does not run Python,
AQSE, Docker, simulations, or the report-only analysis.

```sh
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Overleaf and a normal TeX Live/MacTeX installation provide the required packages.
The downloadable delivery also contains `compila_pdf.sh` and a compiled PDF.
A separate clean source ZIP contains only the manuscript dependencies and a
prebuilt `main.bbl`; the full Git package additionally preserves the analyses
and editorial audit trail. No font files or modified IEEE style files are bundled.

## Source organization

- `frontmatter/`: approved author metadata, abstract and Index Terms.
- `sections/01_*` through `08_*`: scientific text.
- `sections/09_availability.tex`, `10_acknowledgment.tex`: closing statements.
- `figures/`: two TikZ sources and three previously generated result PDFs.
- `tables/`: seven method and result tables.
- `bibliography.bib`: the existing 30 reference records, unchanged.
- `analysis/pass4/`: unchanged inputs, report-only script and analysis outputs.
- `editorial/`: prior pass records, final integration audit and author checklist.

## Scientific boundary

The network State8-AFSE-MLP demonstrator and the single-magnetometer harmonic
TQK-SVC benchmark are separate routes. The 30 independent primary corpora test
the latter. The preregistered predictive-advantage criterion was not met.
The TRAIN-label control keeps validation supervision and reuses one teacher
dataset. It is not a fully label-null experiment. The reported QNG trajectories
lack TEST evaluations for the unselected initial models. No hardware advantage,
field-deployment validity, or causal training benefit is claimed.

Pass 6 adds no experiment or statistical test and changes no frozen estimate.
The bibliography, figures, tables, and every file in `analysis/pass4/` remain
byte-identical to Pass 5. Limited prose edits define acronyms, disambiguate units,
standardize route names and figure references, and remove an unexplained
reference to an earlier experiment. All displayed scientific equations are unchanged.

## IEEE/TQE status

The TQE submission page, author-template guidance and AI-content policy were
checked. TQE states that it has no page limit. The document follows a standard
IEEE journal review layout; it does not impersonate the publisher's typeset
version. The linked TQE v4 instructional PDF was available, but the interactive
IEEE template selector did not return a downloadable TQE LaTeX archive during
this review. The current portal/template must therefore be confirmed at upload.
This limitation is recorded rather than replaced with a claimed verification.

The authors must review the manuscript and the acknowledgment, supply ORCIDs
where requested, and confirm funding and conflict declarations. No submission
or publication license is executed by this package.

## Git and Overleaf

The download uploader operates only on `paper/ieee-tqe-v1`, checks the baseline
and file hashes, and requests `PUBBLICA` before copy/commit/push. It does not
merge, change `main` or tags, discard author edits, or run analysis code.
After author approval, a separately authorized merge can consolidate the paper.
Do not assume that Overleaf automatically imports this review branch. Pull the
agreed synchronized branch into the linked Overleaf project after the merge.
