# AQSE manuscript for IEEE Transactions on Quantum Engineering

## Current draft

Passes 1-3 are integrated: Introduction, Related Work, AQSE Framework, and
Experimental Methodology. This is a partial English manuscript, not a
submission-ready paper. The experimental repository remains separate.

- Manuscript branch: `paper/ieee-tqe-v1`.
- Input manuscript revision: `6bceb8faf2ce0035769743390b9549c114aff536`.
- Scientific execution revision: `091acf2e98b2b88720730eea276e253f0c96f5a6`.
- Published scientific snapshot: `0ed58cfd4a1680ee111f91bb44af7ab101d4c01a`.
- Reporting recovery revision: `d42965ef6a38791fcdbdc1b7bbb3750a58d1f2f1`.

The three existing prose sections, two TikZ figures, State8 table and prior
editorial notes are unchanged. Pass 3 adds Methodology, two experimental tables,
four bibliography records and a source audit. No scientific data were recomputed.

## Files and compilation

Use `main.tex` as the root document, pdfLaTeX and BibTeX, the unmodified
`IEEEtran` journal class and the `IEEEtran` bibliography style. The source uses
standard packages, including TikZ, without external images or shell escape.

```sh
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Main source files:

```text
main.tex
bibliography.bib
sections/01_introduction.tex
sections/02_related_work.tex
sections/03_aqse_framework.tex
sections/04_methodology.tex
figures/aqse_routes.tex
figures/tqk8_circuit.tex
tables/state8_features.tex
tables/benchmark_protocol.tex
tables/comparator_budget.tex
editorial/pass1-evidence-and-decisions.md
editorial/pass2-evidence-and-decisions.md
editorial/pass3-evidence-and-decisions.md
```

Editorial notes are not included in the compiled PDF. The separate downloadable
package includes a preview, checks and shell scripts. Generated PDFs, auxiliary
files, ZIPs and delivery scripts are not committed to this source branch.

## Scientific and editorial boundaries

The framework's network State8-AFSE-MLP path is not the replicated harmonic
single-sensor TQK-SVC benchmark. The primary study contains 30 newly generated
corpora. The positive control has 12 new teacher datasets; the negative control
has 12 randomized re-splits of one teacher dataset, with only TRAIN labels
permuted. Validation supervision is retained in that control. Neither the
control nor the primary study establishes hardware or field performance.

The Methods describe source behavior, including preprocessing differences,
unequal search budgets, the workflow rather than security meaning of the TEST
ledger, and numerical inference conventions. Frozen statistics must not be
silently replaced by post-hoc variants. Results belong to the next writing pass.

English style: concise academic prose, no em-dashes or promotional claims.
Distinguish measurements, protocol choices, source-derived consequences and
post-hoc interpretation. The four new reference records support method origins;
AQSE-specific numerical procedures are specified by the pinned implementation.

This draft uses IEEEtran journal mode. It is not claimed to be the final
TQE-specific production template. Final template reconciliation, author list,
affiliations, ORCIDs, funding, abstract, Index Terms and AI-assistance disclosure
require human approval during integration. No such details are inferred.

## GitHub and Overleaf workflow

Keep all writing passes on `paper/ieee-tqe-v1` until manuscript review is complete.
The upload script verifies the prior revision and declared source contents,
stages only the allowlisted manuscript files, and performs a normal commit/push.
It does not change `main`, merge, rewrite history, or run the AQSE simulator.
Do not independently edit the same files while applying a delivery update.

GitHub publication and Overleaf compilation are separate. The review branch is
not assumed to synchronize automatically to Overleaf. Read the included preview
or import a source snapshot into a separate review project. Merge to the agreed
synchronized branch only after explicit review, then pull changes using the
existing Overleaf integration.

## Writing plan

1. Introduction + Related Work: delivered.
2. AQSE Framework: delivered.
3. Experimental Methodology: delivered in this update.
4. Results: pending.
5. Discussion, Limitations and Conclusions: pending.
6. Final integration and submission checks: pending.
