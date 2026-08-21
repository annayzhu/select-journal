# Local Evidence Sources

Use these files as the user's default local evidence when they exist. A newer user-provided file overrides the registered source. Reinspect workbook sheets and headers at run time because yearly lists change.

## Registered IF/JCR Workbook

- Path: `/Users/annayzhu/Downloads/DOC-20260618-WA0000..xlsx`
- Inspected: 2026-08-05
- Sheet: `2026 JCR`
- Visible columns: `期刊名`, `ISSN号`, `eISSN号`, `Wos学科信息`, `引用索引版本`, `总引用`, `2025影响因子`, `分区`
- Observed scale: 32,215 category rows and 22,642 normalized journal titles. Preserve category duplicates until ISSN/title identity is resolved.
- Use as: `user-file provided` evidence for 2025 impact factor, JCR quartile, WoS category, citation index, total citations, ISSN, and eISSN.
- Eligibility rule: filter or label the `引用索引版本` explicitly; do not assume every row is SCIE.
- Critical boundary: the `分区` values are JCR quartiles (`Q1`-`Q4` or `N/A`). This workbook does not contain the official Chinese Academy of Sciences partition. Never convert `Q1/Q2` into `1区/2区`.

## Registered Institutional Warning Workbook

- Path: `/Users/annayzhu/Downloads/不建议投稿杂志-预警杂志.xlsx`
- Inspected: 2026-08-05
- Current supplied sheet: `2025.12.22挂网`
- Sheet title: `2025年度医院不建议投稿期刊目录（2025.12.23更新版）`
- Observed scale: 169 rows and 168 normalized titles; `Bioengineered` appears twice as a case variant.
- Observed statuses: 101 `预警期刊`, 7 `on hold期刊`, 24 `掠夺性期刊`, and 37 `已剔除`.
- Use as: `user-file provided` hard-exclusion evidence for every journal listed on the current supplied sheet. Preserve the exact status as the exclusion reason.
- Coverage boundary: this is the latest institutional sheet supplied by the user, but it is dated 2025-12-23. Report that date and check for a newer institutional list when a 2026 final submission decision is being made.
- Historical sheets: use older sheets only for trend/audit context unless the user explicitly requests a historical union.

## Unresolved Source Gap

- No official current-year Chinese Academy of Sciences partition workbook is registered here.
- LetPub's `新锐期刊分区表` is a separate third-party partition product and must not be relabeled as the official Chinese Academy of Sciences partition.
- Until an official/current CAS file is supplied, output `CAS partition: unresolved` and show the user-file JCR quartile separately. Missing CAS partition alone does not invalidate a shortlist when JCR and warning evidence are otherwise adequate.

## Runtime Resolution Rule

Before displaying a missing-evidence checklist:

1. Confirm each registered path exists.
2. Reinspect the workbook title row, header row, latest dated sheet, and visible year.
3. Mark IF/JCR and warning-list items `resolved - user-file provided` when these files are successfully parsed.
4. Mark the CAS partition item `unresolved` unless a distinct official/current CAS source is available.
5. List only failed parsing, stale coverage that materially affects the decision, or genuinely absent sources as user actions.
