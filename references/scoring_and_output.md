# Scoring And Output

Use separate dimensions. Do not collapse journal choice into impact factor or aims-and-scope similarity.

## Scoring Dimensions

Score each dimension from 0 to 5, with short evidence notes.

| Dimension | 0 | 3 | 5 |
|---|---|---|---|
| Recent-paper similarity | No recent accepted papers resemble the manuscript | Some same-field or same-design papers | Multiple recent papers closely match field, article type, data scale, and evidence level |
| Article-type fit | Journal rarely accepts this article type | Accepts type but low volume or unclear pattern | Regularly publishes this exact article type |
| Data-scale/workload match | Manuscript has much smaller scale or much lighter work package than recent accepted papers | Scale or workload is comparable in some dimensions but has clear gaps | Cohorts/datasets/samples/cells and experimental/validation workload are comparable to recent accepted papers |
| Evidence-level match | Manuscript evidence is far below recent accepted papers | Evidence level is comparable with some gaps | Evidence level is clearly comparable or stronger |
| Novelty-tier match | Journal expects much higher novelty or broader impact | Manuscript may fit with stronger framing | Manuscript novelty matches recent accepted work |
| Readership/scope fit | Readers unlikely to care | Field-adjacent fit | Clear readership match |
| Operational feasibility | APC/timeline/policy makes submission impractical | Some manageable constraints | APC/timeline/policies fit user constraints |
| Risk profile | Warning hit or serious risk | Some risk requiring verification | Low visible risk |

Risk profile is a gate. A warning-list journal should not receive a positive final tier even if other scores are high.

## Tiering Rules

- `Reach`: strong scope/readership and some recent-paper support, but the manuscript is weaker in novelty, validation, scale, or breadth than typical recent papers.
- `Realistic`: recent accepted-paper portrait is close, article-type volume is credible, evidence level is comparable, and risk is acceptable.
- `Safe`: journal regularly accepts the type and evidence level, risk is acceptable, but prestige/readership may be lower or scope broader.
- `Do not submit`: warning-list hit, indexing/status concern, poor recent-paper similarity, unacceptable APC/timeline, excessive risk, or article type mismatch.

Prefer recommending 3-5 journals total unless the user requests a longlist:

- 1-2 reach options.
- 2-3 realistic options.
- 1 safe option if the user wants practicality.

## Required Evidence Per Recommended Journal

Every recommended journal must include these fields. If a field cannot be verified, keep the field and write `not found`, `not publicly available`, or `needs paid database/manual verification`; do not omit it.

| Required field | Minimum content |
|---|---|
| Recommendation reason | One concise paragraph explaining why the manuscript portrait fits the journal better than nearby alternatives. |
| Recent comparable papers | At least 2-5 papers from the same journal in the most recent 3-6 months when available, with title, date/year, DOI/PMID/link, article type, and the specific comparison dimension. |
| Why each paper is comparable | State whether similarity is by disease/topic, article type, data type, sample size, validation level, novelty tier, clinical/translational framing, or statistical method. |
| Data-scale/workload comparison | State whether the manuscript is lighter, similar, or heavier than recent same-journal papers by cohorts/datasets/samples/cells/events, omics layers, wet-lab assays, functional validation, clinical/protein validation, figure depth, and integration complexity. |
| Why comparison is imperfect | State mismatches, for example larger sample size, stronger validation, different disease, review article rather than original research, or higher novelty. |
| Publication volume and publication pattern | Latest full-year total publication count, current-year or recent-month pattern when obtainable, and counts or estimates for original research, reviews/meta-analyses, case reports, methods/resources, editorials/correspondence. |
| Self-citation and bibliometric context | Self-citation rate or related metric, IF/JCR quartile/category, annual article count trend, and source. |
| China-address rough estimate | China-affiliated address share when obtainable; report method, denominator, time window, whether it is any-author/first-author/corresponding-author based, and limitations. |
| Operational parameters | APC/OA status, publisher, review speed/time-to-first-decision if reported, article-type limits, word/figure limits, data policy, submission-system notes, and key author guideline constraints. |
| Verification status | Label each major fact as `user-file provided`, `LetPub-reported`, `officially verified`, `database verified`, or `needs verification`. |

Apply these completion rules:

- A successfully parsed user IF/JCR workbook resolves its actual fields. It does not resolve a differently named partition system.
- A successfully parsed current supplied institutional warning sheet resolves the local warning check for its stated date. Preserve a freshness note when the submission year is later.
- A visible LetPub value can resolve a field provisionally as `LetPub-reported`; it is not `officially verified`.
- Require paid JCR/InCites verification of self-citation only when the provisional value is suspicious, conflicting, unavailable, or decisive for the ranking.
- Require official author-guideline verification of APC, article limits, and data policy before submission. These fields do not block a scientific-fit shortlist unless cost, length, figure count, or data sharing is a stated hard constraint.
- Keep manuscript-internal uncertainties separate. An unresolved figure/table variable affects only claims and tiers that depend on it.

## Minimum Acceptable Answer

Even when the user asks for a quick recommendation, the answer must include all of the following:

1. A compact manuscript portrait and user constraint line.
2. An eligibility note: SCI/IF source used, warning-list source used, and whether warning-list matches were excluded.
3. A recommendation table with exactly these reader-facing columns unless the user requests a different format: `杂志`, `影响因子/中科院分区`, `对标文章`, `与对标文章的比较情况`, `发文量与发文情况`, `中国地址占比粗估`, `自引/预警`, `运营信息`.
4. A benchmark-paper table with at least 2 recent same-journal papers per recommended journal when available. Use the most recent 3 months first and expand only to 6 months if needed. Include title, date/year, DOI/PMID/link, article type, comparable dimensions, data-scale/workload comparison, mismatch, and implication.
5. A volume/risk table with latest full-year total papers and article-type counts or estimates, current-year/recent-month publication pattern when obtainable, self-citation/risk parameters, China-address rough estimate, APC/review-speed/operation notes, and source/verification status.
6. An evidence-resolution ledger showing completed user-file/database/official fields, provisional LetPub fields, and unresolved items, followed by a user checklist containing only unresolved decision-relevant items.

If there is not enough time or data to collect 3-6 month benchmark papers plus volume/self-citation evidence, do not present a final ranked recommendation. Instead, say `证据包不完整，以下只是候选池，需要补齐近3-6个月对标论文和期刊参数后才能排序`.

Unacceptable output pattern:

```markdown
| 杂志 | 影响因子 | 推荐级别 | 判断 |
|---|---:|---|---|
```

This pattern is incomplete unless it is followed by benchmark-paper evidence and volume/risk parameters for each recommended journal.

## Output Template

```markdown
# Journal Selection Setup

- SCI list used:
- IF/JCR metric file used:
- Warning list used:
- Manuscript input scope:
- User constraints:
- Search/evidence date:
- Evidence boundary:

# Evidence Resolution Ledger

| Evidence item | Status | Value/coverage | Source | Decision impact / next action |
|---|---|---|---|---|
| IF/JCR | resolved / provisional / unresolved |  |  |  |
| Official CAS partition | resolved / unresolved |  |  |  |
| Institutional warning list | resolved / unresolved |  |  |  |
| Self-citation | resolved / provisional / unresolved |  |  |  |
| APC/OA | resolved / provisional / unresolved |  |  |  |
| Review speed | resolved / provisional / unresolved |  |  |  |
| Article limits/data policy | resolved / provisional / unresolved |  |  |  |
| Manuscript-internal facts | resolved / unresolved / not applicable |  |  |  |

# Manuscript Portrait

[Use the portrait template.]

# Eligibility Gate

| Journal universe | Count | Notes |
|---|---:|---|
| User SCI list |  |  |
| Removed by warning list |  |  |
| Removed by identity/status uncertainty |  |  |
| Eligible for scoring |  |  |

# Top Shortlist

| 杂志 | 影响因子/中科院分区 | 对标文章 | 与对标文章的比较情况 | 发文量与发文情况 | 中国地址占比粗估 | 自引/预警 | 运营信息 |
|---|---|---|---|---|---|---|---|
|  | IF; CAS partition; JCR fallback if CAS unavailable | 2-5 papers from recent 3-6 months | topic/type/data scale/workload/validation/novelty/mismatch | annual volume; article-type mix; current/recent pattern | method + denominator + window + limitation | self-citation; warning-list result; indexing/risk | APC/OA; publisher; review time; article limits; data policy |

# Evidence Matrix

| Journal | Recent 3-6 month paper similarity | Data-scale/workload match | Article-type volume/pattern | Evidence-level match | China-address rough estimate | Self-citation/warning | Operational fit | Verification status | Final tier |
|---|---:|---:|---:|---:|---|---|---|---|---|

# Recent Similar-Paper Evidence

For each recommended journal:

| Journal | Benchmark paper | Date/year | DOI/PMID/link | Article type | Comparable dimensions | Data-scale/workload comparison | Important mismatch | Implication |
|---|---|---|---|---|---|---|---|---|

# Annual Volume And Bibliometric Parameters

For each recommended journal:

| Journal | Year/window counted | Total papers | Original articles | Reviews/meta-analyses | Case reports | Methods/resources | Editorial/correspondence | China-address rough estimate | Self-citation/warning/risk parameters | Operational info | Source/verification |
|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|---|

Add notes when counts are estimated from PubMed, publisher archive, LetPub, WoS/Scopus, or manual screening.

# Risk And Exclusion Log

| Journal | Decision | Reason | Verification needed |
|---|---|---|---|

# Submission Strategy

- Recommended first target:
- Backup target:
- Framing changes before submission:
- Method/result additions that would move the manuscript up one tier:
- Formatting or policy checks before submission:

# Missing Evidence / User Verification Checklist

- [x] <resolved item> - <value/window>; source: <source label>.
- [~] <provisional item> - <LetPub-reported value>; verify officially before submission or if decision-sensitive.
- [ ] <genuinely unresolved item> - <where already checked>; needed because <decision impact>.
```

Do not copy a fixed checklist into every report. Suppress resolved items from the user-action list. For an internal manuscript question such as whether a Figure 1D covariate is histology, first inspect the manuscript, legend, methods, table, and source analysis; if still ambiguous, label `author confirmation required` and state exactly which claim or tier depends on it.

## Reporting Language

Use direct, cautious wording:

- "This journal is a realistic candidate because..."
- "The strongest evidence is recent acceptance of papers with..."
- "The closest benchmark papers are..."
- "The annual volume and self-citation parameters suggest..."
- "The main mismatch is..."
- "This should not be selected despite scope fit because..."
- "This metric could not be verified from the available sources."

Avoid:

- "This journal will accept the paper."
- "High IF means best fit."
- "Chinese-author share alone makes the journal unsafe."
- "Aims and scope match, therefore recommended."
- "No warning found" when no current warning-list check was performed.
- Hiding missing benchmark papers, annual volume, or self-citation because they are inconvenient or unavailable.
