# Manuscript Portrait

Use this reference to convert a manuscript into a journal-selection portrait. The goal is to identify what kind of paper editors have to place, not to praise the manuscript.

## Portrait Fields

Extract these fields before looking at candidate journals:

| Field | What to capture | Why it matters for journal fit |
|---|---|---|
| Article type | Original research, review, systematic review/meta-analysis, methods, database/resource, brief report, case series, clinical model, correspondence | Journals accept different article-type mixes. |
| Biomedical field | Disease, organ system, population, mechanism, omics layer, clinical specialty | Used for readership and recent-paper matching. |
| Study design | Retrospective cohort, prospective cohort, case-control, public database, wet-lab experiment, scRNA-seq, spatial, multi-omics, MR/GWAS, ML, trial, etc. | Editors often accept by design pattern, not only topic. |
| Data source | In-house cohort, public database, TCGA/GEO/UKB/MIMIC, multi-center, animal/cell model, clinical registry | Determines credibility, novelty, and audience. |
| Scale | Sample size, cell count, number of datasets, number of centers, number of validation cohorts | Compare against recent papers in the target journal. |
| Workload / work-package density | Number of omics layers, wet-lab assays, perturbation/rescue experiments, in vivo work, clinical/protein validation, figure/supplement depth, and integration complexity | Distinguishes a high-volume but light screening study from a heavier translational/mechanistic paper. |
| Validation | Independent cohort, wet-lab validation, orthogonal platform, external benchmark, prospective validation, calibration, sensitivity analyses | High-selectivity journals expect validation proportional to claim strength. |
| Statistical rigor | Multiple testing, covariate adjustment, batch correction, calibration, external validation, code/data availability | Filters out journals whose recent papers are methodologically stronger. |
| Novelty | New mechanism, new dataset, new model, new biomarker, new clinical association, replication/extension | Match novelty tier to journal tier. |
| Claim boundary | Association, prediction, mechanism, causal inference, diagnostic/prognostic utility, treatment implication | Avoid sending broad clinical claims to journals requiring stronger evidence. |
| Readership | Basic biology, translational medicine, clinical specialty, public health, bioinformatics methods, multi-omics | Determines whether broad or specialty journals are plausible. |
| Practical constraints | APC budget, time pressure, OA preference, word/figure length, data sharing, ethics limits | Prevents recommending unsuitable but otherwise fitting journals. |

## Evidence Boundary Rules

- If only an abstract is provided, mark the portrait as abstract-limited.
- If figures or tables are missing, do not infer data scale, validation, or effect sizes.
- If sample size, dataset source, or validation is unclear, record `AUTHOR_INPUT_NEEDED`.
- If the manuscript is exploratory, do not label it mechanistic or clinically actionable without direct evidence.
- For public-database-only studies, explicitly record whether there is independent validation beyond the source database.
- For ML manuscripts, record train/validation/test split, external validation, calibration, leakage controls, and clinical utility metrics if visible.
- For survival/clinical prediction manuscripts, record event number, censoring, covariates, PH assumption, calibration, DCA, and external validation if visible.
- For single-cell/spatial manuscripts, record sample-level replication, cell-level versus sample-level inference, annotation evidence, batch handling, and validation markers.

## Resolve Manuscript-Internal Uncertainties

Before asking the author about a figure, covariate, endpoint, cohort, or validation step:

1. Check the main text, Methods, Results, figure legend, table footnotes, supplementary material, and available source-analysis labels.
2. Record what is explicit, what is inferred, and what remains ambiguous.
3. Use `author confirmation required` only when the answer cannot be recovered from the supplied materials.
4. State the exact dependent claim. For example, an unresolved Figure 1D covariate blocks the phrase `independent of histology` only if histology is not clearly included in the model.
5. Do not let a claim-specific ambiguity block unrelated journal-fit evidence. Instead, score two bounded scenarios when it could move the tier: `claim retained if confirmed` and `claim removed if not confirmed`.
6. Keep these questions under `Manuscript-internal facts`, separate from IF/JCR, warning-list, APC, review-speed, and other journal metadata.

## Portrait Summary Template

```markdown
## Manuscript Portrait

- Input scope:
- Article type:
- Field/subfield:
- Study design:
- Data sources:
- Scale:
- Workload / work-package density:
- Main claim:
- Evidence assets:
- Validation level:
- Statistical/method rigor:
- Novelty tier:
- Likely readership:
- Practical constraints:
- Missing facts:
- Claim-boundary caution:
```
