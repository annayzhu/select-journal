---
name: select-journal
description: >-
  Select SCI journal candidates for biomedical manuscripts using the user's SCI
  inclusion list, IF/JCR metric file, warning or exclusion list, manuscript
  portrait, data scale and workload fit, recent 3-6 month same-journal publication portraits,
  article-volume patterns, China-address share, self-citation, indexing, APC,
  review speed, and editorial risk. Requires reasons, recent comparable papers,
  annual article-type volume, self-citation/risk parameters, and verification
  status for recommendations, and resolves available local/LetPub/official
  evidence before asking the user for missing inputs. Use when the user asks to choose, rank, or audit
  SCI journals for a paper, manuscript, abstract, draft, figure set, methods/results
  summary, or Chinese/English submission plan. Also trigger on "请帮我推荐杂志",
  "推荐sci杂志", "推荐SCI杂志", "适合投在什么杂志上", "适合投哪个杂志",
  "这篇文章投什么杂志", "帮我选刊", "SCI选刊", "论文投稿期刊推荐",
  "目标期刊推荐", "recommend journals", "journal fit", and "target journal".
---

# Select Journal

## Overview

Use this skill to build an evidence-grounded SCI journal shortlist for a biomedical manuscript. The main logic is not "aims and scope first"; it is eligibility first, manuscript portrait second, recent accepted-article similarity third, and journal risk/volume metrics fourth.

## Core Rules

- Treat the user's yearly SCI inclusion list as the eligible universe. Do not recommend journals outside it unless the user explicitly asks for exploratory options.
- Treat the user's warning list as a hard exclusion list. A warned journal can appear only in an exclusion/audit table, never in the recommended shortlist.
- Do not rely on aims and scope alone. Use the journal's recent published articles as the strongest practical signal of what the journal is actually accepting.
- For benchmark/comparable papers, use only the last few months by default: prefer the most recent 3 months and do not exceed the most recent 6 months for the core benchmark set unless the user explicitly authorizes expansion. If fewer than 2 comparable papers are found within 6 months, mark the journal as evidence-limited instead of quietly using older papers.
- Use current sources when journal status, impact indicators, indexing, APC, self-citation, review speed, publisher policy, or warning status may have changed.
- Resolve evidence before generating a user checklist. Inspect supplied files, accessible LetPub pages, official journal pages, publication databases, and manuscript materials first; never label a field `not done` merely because it was not supplied in the current prompt.
- Distinguish verified facts, user-provided list data, inferred fit, and unavailable metrics.
- Do not claim acceptance probability as a fact. Report "fit", "risk", and "submission strategy", not a guaranteed outcome.
- Keep biomedical claims conservative. Do not overstate novelty, mechanism, clinical value, or causality from the manuscript portrait.
- When evidence conflicts, prefer official indexing and journal pages for factual status, bibliometric databases for metrics, and recent published papers for actual editorial appetite.
- A journal recommendation is incomplete unless it includes the reason, recent comparable papers from that journal, annual article-type volume, self-citation/risk parameters, and source/verification status.
- Judge data scale and workload explicitly. Separate "large enough data" from "enough work done": cohorts/datasets/cells/samples measure scale, while wet-lab validation, omics layers, perturbation/rescue experiments, clinical validation, figures, and analysis depth measure workload or work-package density.

## Non-Negotiable Output Contract

Do not output a simple recommendation table with only journal name, IF, recommendation level, and subjective judgment. That is an incomplete use of this skill.

Before presenting any journal as `Reach`, `Realistic`, or `Safe`, include these fields for that journal:

- Journal identity and impact context: journal title plus impact factor and Chinese Academy of Sciences partition when available. If CAS partition is not available, show JCR quartile separately and label the missing CAS field as `needs verification`.
- Benchmark/comparable papers: 2-5 comparable papers from the same journal within the most recent 3-6 months, with title, year/date, DOI/PMID/link, article type, and why each paper is a benchmark.
- Comparison with benchmark papers: compare the manuscript against benchmark papers on disease/topic, article type, data type, data scale, workload, novelty, validation depth, clinical/translational level, and main mismatch.
- Publication volume and publication pattern: latest full-year total indexed papers plus article-type mix, and current-year/recent-month volume when obtainable.
- China-address share rough estimate: estimate China-affiliated address share from PubMed/WoS/Scopus/publisher metadata when obtainable; report denominator, search window, and limitation.
- Self-citation/warning status: self-citation rate/status, user's warning-list status, indexing stability, and other bibliometric/editorial red flags.
- Operational information: APC/OA status, publisher, review-time or first-decision information, article-type/word/figure limits, data policy, and submission-system notes when obtainable.
- Source labels for major facts: `user-file provided`, `database verified`, `LetPub-reported`, `officially verified`, `not found`, `not publicly available`, `needs paid database/manual verification`, or `author confirmation required`.

If a required field cannot be verified, keep the field in the output and mark it explicitly. Do not omit missing benchmark papers, article-type volume, self-citation, China-address context, APC, or review-speed fields because they are inconvenient.

If recent comparable papers and volume/self-citation evidence cannot be obtained for a candidate, present it as `candidate needing evidence`, not as a final recommended journal. A quick answer may be shorter, but it must still include an abbreviated evidence table with benchmark papers and volume/self-citation fields.

## Accepted Inputs

The user may provide any combination of:

- Yearly SCI inclusion list: spreadsheet, CSV, PDF, text table, or journal names.
- Yearly IF/JCR metric file: PDF, spreadsheet, CSV, or text table with journal name, impact factor, JCR quartile, category, or related ranking fields.
- Warning or exclusion list: official warning list, institutional list, local blacklist, publisher-level concerns, or manually named journals.
- Manuscript material: title, abstract, full draft, cover-letter summary, figures, figure legends, methods/results notes, supplementary methods, or Chinese research summary.
- User constraints: target tier, time pressure, APC limit, OA preference, region preference, article type, field, avoidance rules, or desired "reach/realistic/safe" balance.
- Candidate journals the user already wants audited.

If the SCI inclusion list or warning list is missing, continue only with a bounded exploratory assessment and clearly mark that final recommendations require those lists.

## Workflow

### 0. Resolve Available Evidence

Read `references/local_evidence_sources.md` and `references/journal_evidence.md` before asking the user for files or verification.

1. Check whether registered local evidence files exist and whether the user supplied newer replacements.
2. Parse each source and identify what it actually contains. Keep JCR quartile, Chinese Academy of Sciences partition, and third-party Chinese partition systems as separate fields.
3. Build an evidence-resolution ledger with one status per requested field: `resolved`, `provisional`, `unresolved`, or `not applicable`.
4. Use LetPub as a secondary source for fields it displays, then follow its official links for high-impact operational checks when possible.
5. Inspect the manuscript, figures, legends, and tables for manuscript-internal uncertainties before asking the author. Do not mix manuscript-internal questions with missing journal metadata.
6. Ask the user only for unresolved items that materially affect eligibility, tier, cost, timeline, or claim positioning.

### 1. Build The Eligibility Gate

Read `references/journal_evidence.md` for eligibility and source rules.

1. Normalize journal names, ISSN/eISSN, publisher, title variants, and abbreviations from the user's SCI list.
2. If the user supplies an IF/JCR file, parse it as user-provided metric evidence and join by normalized title or ISSN.
3. Normalize the warning list in the same way.
4. Remove all warning-list matches before scoring.
5. Flag uncertain matches for human verification instead of silently keeping them.
6. Preserve an exclusion log with the reason each journal was removed.

### 2. Create The Manuscript Portrait

Read `references/manuscript_portrait.md` before evaluating the manuscript.

Extract a compact manuscript portrait:

- Article type: original research, review, meta-analysis, methods, resource, case series, clinical prediction model, translational study, bioinformatics analysis, or other.
- Field and subfield: disease area, organ system, omics layer, clinical area, mechanism, method, or data resource.
- Study design: cohort, case-control, cross-sectional, experimental, public-database mining, single-cell, spatial, multi-omics, ML model, survival analysis, MR, GWAS, trial, etc.
- Evidence assets: sample size, independent cohorts, validation cohorts, wet-lab validation, external datasets, prospective/retrospective design, figures, statistical rigor, data/code availability.
- Data scale and workload: cohorts/datasets/samples/cells/events, omics layers, number and type of wet-lab experiments, perturbation/rescue or in vivo work, clinical/protein validation, figures/supplements, and whether the work package is light, moderate, or heavy for the target tier.
- Novelty level: incremental, field-useful, methodologically strong, translationally plausible, broad-interest, or high-risk overclaimed.
- Fit constraints: article length, figure count, data type, ethics/data-sharing constraints, APC limit, urgency, and region/publisher preferences.

Mark missing manuscript facts explicitly. Do not infer validations, sample size, datasets, or statistics that are not present.

### 3. Build A Journal Evidence Pack

For each eligible candidate journal, collect a bounded evidence pack:

- Recent publication portrait: sample papers from the most recent 3 months when possible; expand to 6 months only when needed. Do not use papers older than 6 months in the core benchmark set unless the user explicitly asks for a broader historical view.
- Similarity evidence: how close recent accepted papers are to the manuscript on disease, data type, sample size, novelty, validation, statistics, clinical/translational level, and article type.
- Data-scale/workload evidence: whether recent accepted papers have comparable cohorts, datasets, sample/cell/event counts, omics layers, wet-lab validation, functional depth, clinical validation, figure count, and total work-package density.
- Volume evidence: annual total publications and, where possible, article-type counts such as original articles, reviews, brief reports, meta-analyses, case reports, methods, and resources.
- Author-origin evidence: China corresponding-author or China-affiliated paper share when obtainable from publication metadata; report method and limitations.
- Bibliometric/risk evidence: JCR/SCI status, quartile/category, impact factor or equivalent, self-citation, citation distribution, publisher, APC, review time, acceptance clues, special issue dependence, retraction/expression-of-concern signals, DOAJ/COPE status for OA journals.
- Scope evidence: official aims and scope, article types accepted, exclusions, data availability and ethics requirements.

If current web/database access is unavailable, state which evidence fields are stale or missing and avoid final ranking beyond the user-supplied data.

### 4. Score Fit And Risk

Read `references/scoring_and_output.md` for the rubric.

Score only eligible, non-warning journals. Use separate dimensions rather than one opaque number:

- Manuscript-journal similarity from recent accepted papers.
- Technical and evidence-level match.
- Data-scale and workload match.
- Article-type and volume match.
- Field/readership match.
- Novelty-tier match.
- Operational feasibility: APC, timeline, formatting, OA policy, data policy.
- Risk: warning proximity, self-citation, indexing instability, special issue dependence, unusually high China-address concentration, publisher or editorial red flags.

Classify candidates into:

- `Reach`: plausible but demanding; manuscript may need stronger novelty, validation, or framing.
- `Realistic`: best balance of portrait similarity, evidence level, readership, and risk.
- `Safe`: lower selectivity or broader acceptance pattern, used when speed or acceptance practicality matters.
- `Do not submit`: warning-list hit, status uncertainty, high risk, or poor fit despite superficial scope match.

### 5. Produce The Journal Selection Report

Do not output a recommendation-only list. For every recommended journal, include the recommendation reason, recent comparable published papers, annual article-type volume, self-citation/risk parameters, and verification status so the user can judge independently.

Before finalizing, run this mental checklist:

- Does every recommended journal have at least 2 comparable papers, or an explicit `not found` explanation?
- Are the comparable papers within the most recent 3-6 months, or is any expansion beyond that explicitly labeled and not used as core evidence?
- Does every recommended journal state whether the manuscript's data scale and workload are comparable to recent same-journal papers?
- Does every recommended journal have annual article-type volume, or an explicit source limitation?
- Does every recommended journal have self-citation/risk parameters, or an explicit `needs paid database/manual verification` note?
- Does the output show why each benchmark paper is comparable and why it is imperfect?
- Does the output separate user-provided IF/JCR evidence, database/PubMed evidence, LetPub-reported fields, and unverified fields?
- Does the evidence-resolution ledger mark supplied IF/JCR and warning files as resolved instead of repeating them as missing?
- Does the user checklist contain only unresolved, decision-relevant items and explain why each still matters?

If any answer is no, revise the output before responding.

Default output:

```markdown
# Journal Selection Setup
# Evidence Resolution Ledger
# Manuscript Portrait
# Eligibility Gate
# Top Shortlist
# Evidence Matrix
# Recent Similar-Paper Evidence
# Annual Volume And Bibliometric Parameters
# Risk And Exclusion Log
# Submission Strategy
# Missing Evidence / User Verification Checklist
```

Always include a concise table with:

- Journal
- Impact factor / Chinese Academy of Sciences partition: show IF and CAS partition when available; show JCR quartile as a separate fallback, not as a hidden substitute.
- Benchmark papers: title, date/year, DOI/PMID/link, and article type for recent 3-6 month same-journal benchmark papers.
- Comparison with benchmark papers: concise comparison across topic, article type, data type, data scale, workload, validation, novelty, and mismatch.
- Publication volume and publication pattern: annual volume plus article-type mix and recent/current-year pattern when obtainable.
- China-address share rough estimate: method, denominator, window, and limitation.
- Self-citation / warning: self-citation, user's warning-list result, indexing/risk notes.
- Operational information: APC/OA, publisher, review time, article-type limits, submission or data-policy notes.
- Verification status and required user verification.

Do not print a boilerplate all-`not done` checklist. Show resolved items as completed with the source and date/window, show provisional LetPub items with their limitations, and list only genuinely unresolved items under `Missing Evidence / User Verification Checklist`.

## Reference Files

- `references/manuscript_portrait.md`: how to extract the manuscript portrait from drafts, abstracts, figures, and methods/results notes.
- `references/local_evidence_sources.md`: registered user-provided files, their verified schemas, and rules for deciding whether they satisfy IF/JCR, partition, and warning-list requirements.
- `references/journal_evidence.md`: how to use SCI lists, warning lists, recent papers, volume metrics, China-address share, self-citation, indexing, and risk sources.
- `references/scoring_and_output.md`: scoring dimensions, tiering rules, output templates, and verification checklist.
