# Pass 6: final integration and consistency audit

Review date: 2026-09-18. Target: IEEE Transactions on Quantum Engineering.
Status: complete English manuscript for author approval. Submission declarations
and the live portal are not completed by this delivery.

## Input identity

The live manuscript branch was checked at
`687978b9f7ca86f4250bef5b3314e5d9681be8eb`. Its Git tree is
`6d02a4a5af8a5a78117a4bd77fe37c5701bb6099`. Reconstructing a Git index from all
41 delivered Pass 5 source files produced that exact tree. This verifies the
baseline bytes, including the three binary figure PDFs, rather than relying
only on the user's upload log.

Scientific execution: `091acf2e98b2b88720730eea276e253f0c96f5a6`.
Published scientific snapshot: `0ed58cfd4a1680ee111f91bb44af7ab101d4c01a`.
Reporting-only recovery: `d42965ef6a38791fcdbdc1b7bbb3750a58d1f2f1`.
These revisions have distinct roles and are not relabelled as a single run.

## Author metadata

The corresponding author supplied the author order and four affiliations in
this conversation and confirmed `f.caprio@unicampus.it`. The mappings are Caprio
1; Tortora 2; Soda 1 and 3; Gentyala 4. Universita and Umea accents are encoded in
LaTeX. No affiliation is substituted from a web search. No IEEE member grades,
ORCIDs, funding, conflict declarations, or publishing metadata are inferred.

## Integrated front and back matter

The new abstract is a single paragraph of 215 whitespace-delimited words,
without citations, displayed equations, or unexplained acronyms. It states the
framework/benchmark distinction, the 30-corpus design, primary quantitative
result, unresolved exploratory relationships, failed control check and exact
simulation scope. Five alphabetized Index Terms follow. The full title is kept.
The working-draft banner is removed and PDF metadata identify the approved authors.

Data and Code Availability points to the scientific frozen record and manuscript
repository. It does not promise a DOI, permanent external archive, raw field data,
or release of all local measurement arrays. The acknowledgment identifies
ChatGPT/OpenAI, Codex and the user-reported preliminary Claude Sonnet analysis,
without inventing model versions or claiming completed coauthor review.

## Cross-section scientific checks

| Item | Coherence decision |
| --- | --- |
| Title and abstract | Network representation is the framework; the replicated evidence is the single-sensor TQK-SVC component benchmark. |
| Sensing versus computation | Encoded classical observations are not the microscopic sensor state; no enhanced hardware sensitivity is claimed. |
| Feature routes | State8 local/network and the eight harmonic features are not interchanged. |
| Units | B in tesla/nanotesla is explicitly magnetic flux density; harmonic spectral peak is PSD, not frequency. |
| Data split | 120 episodes, balanced 72/24/24, one fixed central window per episode, no independence claim for overlapping windows. |
| Circuit and training | Eight qubits, 16 circuit parameters, seven CZ gates, shared theta derivatives, mean FS metric, binary surrogate loss are unchanged. |
| Search budgets | QNG bank 32; SVC TRAIN 72; 33 maximum quantum candidates versus nine RBF points; other configurations fixed. |
| Primary estimate | BA 0.9528 versus 0.9569; delta -0.0042; interval [-0.0222,0.0125]; p=0.9328. No equivalence inference. |
| Secondary inference | Raw comparisons and both disclosed post-hoc family choices remain separate from the primary criterion. |
| Spectral inference | Finite Gram-matrix summaries are not expressivity, entanglement, or generalization guarantees. |
| Checkpoint interpretation | 19 initial and 11 updated selections do not identify a TEST benefit of QNG without matched initial TEST predictions. |
| Controls | Twelve new positive datasets; twelve rerandomizations of one negative dataset, TRAIN labels only permuted, VALIDATION supervision retained. |
| Runtime | Repeated method-level CSV duration is a joint replica duration, not per-method speed. |
| Conclusions | No QPU, finite-shot, field-validity or quantum-advantage claim is introduced. |

All equation environments were compared with Pass 5; their contents are identical.
Every figure source/PDF, table, bibliography record and `analysis/pass4/` file is
byte-identical. The primary estimates were checked by reading the existing
canonical-summary inputs and manuscript text; no bootstrap, permutation,
simulation, quantum-state evaluation, model fit or TEST prediction was rerun.

## Limited prose harmonization

1. `sections/01_introduction.tex`: Define MLP on first prose use.
2. `sections/01_introduction.tex`: Use one name for the demonstrator route.
3. `sections/01_introduction.tex`: Define QPU before later abbreviated use.
4. `sections/01_introduction.tex`: Define RFF before later abbreviated use.
5. `sections/03_aqse_framework.tex`: Use Fig. for figure cross-references, per TQE instructions.
6. `sections/05_results.tex`: Use Fig. for figure cross-references, per TQE instructions.
7. `sections/03_aqse_framework.tex`: Disambiguate B measured in T from field strength H in A/m.
8. `sections/03_aqse_framework.tex`: Define CZ and preserve the identical gate order.
9. `sections/03_aqse_framework.tex`: Define PSD on its first abbreviated use.
10. `sections/03_aqse_framework.tex`: Define the optimizer name without changing its setting.
11. `sections/03_aqse_framework.tex`: Define OOD before the Limitations section.
12. `sections/02_related_work.tex`: Avoid an undefined journal abbreviation in the prose.
13. `sections/01_introduction.tex`: Avoid conflating a one-hidden-layer MLP with a linear perceptron.
14. `sections/04_methodology.tex`: Make Methods self-contained without citing an unreported prior AQSE experiment.

These changes clarify nomenclature and cross-references. They do not alter the
implemented experiment or any scientific estimate. Prior pass notes remain
historical records and are not silently rewritten to say the final text was
already complete at an earlier stage.

## Reference and publication guidance review

All 30 BibTeX keys are unique, cited, and resolved by BibTeX. The bibliography is
retained byte-identically. Published versions remain distinguished from the
Bowles et al. arXiv preprint. The recent TQE 2025, Quantum Machine Intelligence
2025, PRR 2025 and PRR 2026 records were checked against primary publisher records.
Older references were checked against publisher/proceedings or author-repository
records where accessible. `reference-review.csv` records access distinctions;
this is not a claim to have freshly read all full texts.

TQE's official page states no page limit. The IEEE template page points to the
interactive selector; the available TQE v4 instructional PDF specifies a
150-250-word abstract, a single paragraph, alphabetized Index Terms, affiliation
and corresponding-author information, standard text dimensions, numbered IEEE
references, and readable figure lettering. Its first page was inspected. The
interactive selector did not provide a downloadable TQE LaTeX archive in this
environment. The document therefore retains the standard, unmodified IEEEtran
10-pt journal review layout. It is not called a verified TQE production class.
No publisher logo, issue, DOI, copyright line, publication date, or license is
fabricated. The final portal/template check is explicitly left in the checklist.

## Compilation and delivery validation

The cumulative PDF was built with pdfLaTeX and BibTeX. In this container the
`bibtex` symlink was broken, so the installed `bibtex.original` executable was
used. The bibliography step was run in the build directory with BIBINPUTS set
to the source directory; no TeX security setting was relaxed. Both are local
build details, not scientific changes. The Mac build script uses standard
BibTeX with a fallback when available.

The 15 rendered pages were inspected in three contact sheets and the author page
and references/acknowledgment page were also inspected individually. The artifact
checks record page count, font embedding, cross-reference resolution, equation
preservation and source hashes. Underfull spacing advisories are retained in the
log; no overfull boxes or unresolved references were detected. Actual uploader
fixture results are in the delivery folder, outside the manuscript repository.

No repository write, merge, tag change or submission was performed here. The
Mac uploader requires the author's explicit confirmation and publishes only the
allowlisted manuscript sources to the same review branch.
