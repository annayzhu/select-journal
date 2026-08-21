# Journal Evidence

Use this reference to build an evidence pack for each candidate journal. The user-provided SCI list and warning list control the candidate universe before any ranking.

## Contents

- Evidence resolution before user questions
- Eligibility and warning-list handling
- Source hierarchy and LetPub boundaries
- User-provided IF/JCR files
- Recent-paper similarity
- China-address, volume, and risk metrics
- Evidence-pack template

## Resolve Evidence Before User Questions

Create a field-level evidence ledger before producing a missing-evidence checklist.

| Status | Meaning | Output treatment |
|---|---|---|
| `resolved` | The field is supported by a parsed user file, official source, or appropriate database. | Show `[x]`, source, date/window, and value. Do not ask the user for it again. |
| `provisional` | LetPub or another secondary source provides a usable first-pass value. | Show the value and `LetPub-reported` limitation; verify officially only when it could change the decision. |
| `unresolved` | The field was searched but no adequate source was available. | Keep it in the user checklist with the failed source and decision impact. |
| `not applicable` | The field does not affect this journal/manuscript combination. | Omit from the missing checklist or state `not applicable`. |

Do not equate `not supplied in this prompt` with `unresolved`. Check registered local files, current browser pages, official links, bibliographic databases, and the manuscript first.

## Eligibility Gate

1. Load the user's yearly SCI inclusion list.
2. Load the user's yearly IF/JCR metric file when provided, including PDF, spreadsheet, CSV, or pasted table.
3. Normalize journal title, ISSN, eISSN, publisher, abbreviation, and title variants when available.
4. Join metric fields by ISSN when possible; otherwise use conservative normalized-title matching and flag ambiguous duplicates.
5. Load the user's warning or exclusion list.
6. Exclude exact and high-confidence fuzzy matches to the warning list.
7. Put uncertain matches in `needs user verification`; do not silently recommend them.
8. Keep an exclusion log.

Hard-exclusion examples:

- Journal appears on the user's warning list.
- Journal is no longer in the user-provided SCI inclusion list for the relevant year.
- Journal identity cannot be resolved with enough confidence.
- Official or trusted sources show indexing suspension, delisting, or severe editorial concern.

## Warning-List Workbooks

Use user-provided warning-list workbooks as hard exclusion sources. If the workbook has multiple yearly or dated sheets:

- Identify the latest dated or latest "挂网/更新" sheet as the current warning list unless the user specifies another sheet.
- Treat older sheets as historical context, not as the default current exclusion list. Do not union all historical sheets by default because journals may move in or out of local warning systems.
- Preserve the source sheet name, workbook file name, and extraction date in the report.
- Detect header rows rather than assuming row 1 is the table header; many Chinese warning-list workbooks have title and notes rows above the table.
- Extract at least journal name, monitoring result/status, partition/category if present, remarks, and row number.
- In a workbook titled as an "不建议投稿期刊目录" or equivalent, treat every listed journal in the current sheet as `Do not submit` unless a column clearly states that the item has been removed from the warning list.
- Status terms such as `预警期刊`, `高风险期刊`, `中风险期刊`, `掠夺性期刊`, `on hold期刊`, `论文工厂`, `引用操作`, and `已剔除` should be recorded as the exclusion reason or risk signal.
- Deduplicate case variants and punctuation variants, but keep an audit note when the same journal appears twice, for example `Bioengineered` and `BIOENGINEERED`.
- If the user asks for a historical risk audit, then compare across sheets and report when a journal first appeared, disappeared, or changed risk status.

## Source Hierarchy

Use current sources whenever available because journal metadata changes frequently.

| Evidence type | Preferred sources | Notes |
|---|---|---|
| SCI/JCR status, category, IF, quartile, self-citation | User-provided yearly SCI/JCR files, JCR/Clarivate, Web of Science, Journal Citation Reports exports | Use the user's SCI list as the primary eligible universe; use the user's IF/JCR file as versioned local metric evidence when supplied. |
| LetPub journal summary | LetPub journal detail pages | Use as a convenient secondary source for quick facts, links, Chinese-user experience, and sanity checks; verify important facts against official/JCR/PubMed sources before final recommendation. |
| Scope and article types | Official journal website and author guidelines | Scope is supportive evidence, not the main matching signal. |
| Recent published-paper portrait | Journal website, PubMed, Crossref, Web of Science, Scopus | Prefer the most recent 3 months; expand to 6 months only when needed for enough comparable papers. Do not use papers older than 6 months as core benchmark evidence unless the user asks for historical context. |
| Publication volume and article-type mix | PubMed queries, publisher archive, WoS/Scopus document types | Count original articles separately from reviews, case reports, editorials, etc. |
| China-address share rough estimate | PubMed affiliations, WoS/Scopus country fields, Crossref or publisher metadata when affiliations are available | Report denominator, search window, and whether the estimate is any-author address, first-author address, or corresponding-author address; corresponding-author country usually requires manual checking. |
| OA/APC/license | Official journal website, DOAJ | Verify current APC before final advice. |
| Review speed and acceptance clues | Official journal metrics pages, author reports if disclosed | Treat crowdsourced reports as weak evidence. |
| Red flags | User warning list, institutional warning lists, COPE/DOAJ status, indexing notes, retraction notices, unusual self-citation, special issue dependence | Do not overcall without evidence; mark as risk. |

## LetPub As A Secondary Source

Use LetPub when the user asks for Chinese-facing SCI journal background or when a fast first-pass evidence pack is useful. LetPub can be especially useful for:

- Journal title variants, ISSN, publisher, country or region, publication language, publication cycle, and official journal links.
- JCR/SCIE display status, impact-factor snapshots, CiteScore/SJR/SNIP, self-citation, h-index, broad subject categories, and LetPub's named partition product when shown.
- OA status, Gold OA share, APC, waiver links, author-guideline links, submission links, editorial-board links, and contact information.
- Annual article count, research-article share, review/article mix when displayed, and trend links for article count or self-citation.
- LetPub warning-list display, but do not let this override the user's warning list.
- Official or user-reported review speed, user comments, and user-reported acceptance experience.
- Recent China-affiliated papers listed by LetPub, including titles, authors, journal year/volume, DOI, and PubMed/DOI links.
- Similar-journal suggestions and same-category journals for candidate expansion.

Reliability rules:

- Treat LetPub as an aggregator, not the source of truth for final eligibility.
- Record the exact partition label shown by LetPub. In particular, `新锐期刊分区表` is not the official Chinese Academy of Sciences partition and cannot fill a requested CAS field.
- Treat LetPub self-citation as `provisional - LetPub-reported`. Require JCR/InCites or another authoritative export only when the value is high, conflicting, or materially changes exclusion/ranking.
- Treat LetPub annual article count and `文章/(文章+综述)` share as aggregate publication-pattern evidence. They do not replace a document-type count from PubMed/WoS/Scopus.
- Treat LetPub's list of recent Chinese-authored papers as examples, not a China-address percentage. A percentage requires an explicit denominator and search window.
- LetPub can resolve a first-pass APC/OA, publisher, annual volume, self-citation, and user-reported review-speed field. Word limits, figure limits, article-type rules, and data-sharing policy normally require the linked official author instructions.
- Use LetPub to speed up extraction, then verify high-impact fields: current SCIE/JCR status, IF/quartile/self-citation, APC, author instructions, article type, review time, and warning status.
- Separate `LetPub-reported`, `officially verified`, `database verified`, and `user-list provided` in the evidence notes.
- Treat user comments and user-reported acceptance or speed as anecdotal. They can inform risk and timeline expectations but cannot decide fit alone.
- Do not scrape aggressively or bypass login/paywall/VIP restrictions. Use accessible pages and user-provided exports/screenshots when available.
- If LetPub says a metric comes from网友提供 or requires login, mark it as unverified unless the user supplies an export or it is checked elsewhere.
- If LetPub and official/JCR/PubMed sources conflict, report the conflict and use official/JCR/PubMed for the final factual value.

## User-Provided IF/JCR Files

Use user-provided IF/JCR files as versioned local evidence. They are especially useful when the user supplies a yearly PDF or spreadsheet that reflects the current evaluation cycle.

Read `local_evidence_sources.md` for the user's registered default files and their verified schema boundaries.

Extraction rules:

- For PDFs, first try text extraction with layout preservation. If columns are unstable, use OCR or ask the user for the source spreadsheet.
- Record the file name, file date if available, extraction date, and visible columns.
- Preserve duplicate journal rows until identity is resolved; many journal-name duplicates reflect category duplication, formatting artifacts, or repeated entries.
- Join by ISSN/eISSN when available. If only journal title is available, normalize case, punctuation, ampersands, hyphens, and common abbreviations, then flag uncertain matches.
- Treat IF and quartile from the user file as `user-file provided`; verify against JCR/Clarivate only when the value affects a high-stakes ranking decision or conflicts with another source.
- Inspect the actual values and headers before naming the partition system. `Q1-Q4` is JCR quartile evidence; `1区-4区` is not automatically official CAS evidence unless the source explicitly identifies the official CAS edition.
- Do not use IF/quartile alone to rank journals. Use them as tier context after recent-paper similarity, warning-list status, and evidence-level fit.

## Recent Accepted-Paper Similarity

For each candidate journal, inspect recent papers before using aims and scope. For recommended journals, provide 2-5 recent comparable published papers when available.

Use this benchmark-paper time window:

1. First search the most recent 3 months.
2. If fewer than 2 same-journal comparable papers are found, expand to the most recent 6 months.
3. Do not use papers older than 6 months in the core benchmark set unless the user explicitly authorizes expansion.
4. If the 6-month window still yields fewer than 2 suitable benchmark papers, mark the journal as `recent benchmark evidence limited`; do not hide the gap by silently using older papers.
5. If an older paper is useful as background, put it in a separate historical-context note and do not score it as core recent-paper evidence.

Compare papers from the 3-6 month window against the manuscript portrait on:

- Topic/disease/biological system.
- Article type.
- Study design.
- Data type and platform: clinical cohort, scRNA-seq, spatial, RNA-seq, proteomics, metabolomics, microbiome, imaging, EHR, public database, wet lab, ML, etc.
- Data scale: sample size, number of cohorts, number of cells, number of datasets, number of centers.
- Workload / work-package density: number of omics layers, wet-lab assays, perturbation/rescue experiments, in vivo work, clinical/protein validation, figures/supplements, and analysis integration depth.
- Validation depth: internal only, external cohort, wet-lab, multi-platform, prospective, functional validation.
- Novelty tier: incremental association, biomarker screening, mechanistic finding, method/resource, broad translational insight.
- Statistical rigor: adjustment, multiple testing, batch effects, calibration, sensitivity analyses, reproducibility.
- Region/authorship pattern: China-affiliated articles, international collaborations, domestic single-center dominance if relevant.
- Framing: specialty clinical, translational, basic mechanism, computational method, public health, broad biomedical.

Do not treat a single similar paper as proof. Use it as evidence of editorial appetite, and state whether it is strong, moderate, or weak evidence.

For each comparable paper, record:

- Title.
- Year and publication date when available.
- DOI, PMID, or journal URL.
- Article type.
- Study design and data type.
- Sample/data scale.
- Workload / work-package density.
- Validation level.
- Why it is comparable to the user's manuscript.
- Why it is not a perfect comparison.
- What it implies for submission positioning.

## China-Address Share Rough Estimate

When the user asks for Chinese-address context, or when it is part of the journal recommendation output, provide a rough estimate instead of omitting the field.

Preferred method:

1. Define the denominator clearly, such as PubMed-indexed articles in the latest full year, current year to date, or the same 3-6 month benchmark window.
2. Count records with at least one China-affiliated author address when available.
3. If possible, separately note whether corresponding-author China share was checked; if not, write `corresponding-author share needs manual verification`.
4. Report the result as an estimate, for example `about 42/120 PubMed records with at least one China address; not corresponding-author specific`.
5. Do not treat high China-address share as a standalone red flag. Combine it with warning-list status, self-citation, article volume, indexing stability, special issue dependence, and recent-paper quality.

## Volume And Risk Metrics

Collect these when possible:

- Annual publication count for the latest full year and current partial year.
- Counts by document type: article, review, systematic review/meta-analysis, case report, editorial, correspondence, methods/resource.
- Estimated China-address share and how it was measured.
- Self-citation rate and whether it is unusually high for the category.
- Special issue or collection dependence.
- APC and waiver options.
- Median time to first decision or acceptance if officially reported.
- JCR category/quartile and whether the category matches the manuscript field.
- Indexing stability or recent delisting/suppression concerns.

Interpretation rules:

- High China-address share is not automatically bad; combine it with quality, self-citation, editorial pattern, and warning-list status.
- High volume is not automatically bad; distinguish broad legitimate scope from paper-mill-like patterns or special issue inflation.
- Low impact factor is not automatically bad; judge whether the journal accepts the manuscript's exact design and evidence level.
- A strong aims-and-scope match cannot rescue warning-list status or lack of recent accepted-paper similarity.
- Missing official article-format limits or data policy should block submission-readiness, not the scientific-fit shortlist, unless the manuscript visibly exceeds likely limits or has a data-sharing constraint.
- A manuscript-internal uncertainty should block only claims and journal tiers that depend on that fact. Keep it separate from journal-metadata gaps.

## Evidence Pack Template

```markdown
## Journal Evidence Pack: <Journal>

- Eligibility status:
- Warning-list status:
- Official scope fit:
- LetPub summary:
- Recent similar papers reviewed:
- Comparable benchmark papers:
- Similarity summary:
- Data-scale/workload fit:
- Annual publication volume:
- Article-type mix:
- China-address rough estimate:
- Self-citation / bibliometric risk:
- Volume/self-citation source and verification status:
- Operational information:
- Review speed:
- Indexing status:
- Main fit reason:
- Main mismatch:
- Risk notes:
- Evidence gaps:
- Evidence-resolution status:
```
