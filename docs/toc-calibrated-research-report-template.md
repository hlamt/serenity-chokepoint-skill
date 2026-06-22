# TOC-Calibrated Chokepoint Research Report Template v1.0E — Evidence-Bounded Investment Research Output

## 1. Purpose

This document defines the future template structure for a TOC-calibrated Chokepoint research report. It specifies report eligibility, object metadata, required section order, evidence-table requirements, candidate-exposure boundaries, calibration fields, confidence rules, and non-investment-advice controls.

V1.0E does not collect source data. V1.0E does not scrape X. V1.0E does not use twscrape. V1.0E does not call external APIs. V1.0E does not add real Serenity corpus entries. V1.0E does not extract real method claims. V1.0E does not execute real TOC calibration. V1.0E does not generate a real investment research report. V1.0E only defines the future report template.

This document is a structural specification, not an example report, company analysis, research conclusion, recommendation, or completed methodology.

## 2. Relationship to V1.0A, V1.0B, V1.0C, and V1.0D

The V1.0 workflow has sequential controls:

- V1.0A defines authorized intake.
- V1.0B defines source records, corpus entries, and distillation queue items.
- V1.0C defines the `method_claim_candidate` extraction protocol.
- V1.0D defines TOC calibration matrix rows.
- V1.0E defines how reviewed calibration rows may be organized into a research report.
- V1.0E cannot bypass any upstream phase.
- Only reviewed and `report_ready` calibration rows may be used in future reports.
- A report template does not authorize real report generation.

Every future report must preserve traceability from report statements to calibration rows, method claims, corpus entries, and accepted source records. Template compliance does not establish source truth, method validity, company merit, or an investment conclusion.

## 3. Report principles

Future reports must follow these principles:

1. **Evidence-bounded**: every material hypothesis must stay within the support and limitations of its evidence chain.
2. **Source-traceable**: claims, contradictions, method basis, and calibration must remain linked to reviewable source records.
3. **TOC-calibrated but not TOC-substituted**: TOC may discipline system reasoning without replacing source-grounded Chokepoint Theory.
4. **Chokepoint Theory and TOC non-equivalence preserved**: overlap and difference must remain visible.
5. **Investment research context separated from operating-system context**: value capture and market expectations must not be collapsed into throughput and constraint management.
6. **Hypotheses instead of conclusions**: the report frames testable research hypotheses, not confirmed winners or guaranteed outcomes.
7. **Counterevidence required**: every candidate chokepoint and exposure pathway must include contradictory evidence and alternatives.
8. **Invalidation conditions required**: every hypothesis must define what would weaken or reject it.
9. **No single source supports a real company conclusion**: company-specific research requires a broader, reviewed evidence chain and separate authorization.
10. **No report section can become investment advice**: no section may recommend a trade, target price, or position size.
11. **Uncertainty and confidence visible**: confidence, limitations, ambiguity, and missing checks must not be hidden.
12. **No Serenity endorsement or impersonation**: the report must not claim official status or present assistant synthesis as Serenity's view.

## 4. Report input requirements

A future calibration row may enter report generation only when:

- calibration row `review_status = report_ready`;
- `method_claim_id` exists;
- `claim_statement` exists;
- the source chain is traceable;
- source limitations are recorded;
- `ambiguity_or_disagreement` is recorded, including an explicit `none identified` where appropriate;
- `possible_toc_overlap` is recorded;
- `possible_toc_difference` is recorded;
- `false_equivalence_risk` is recorded;
- `investment_research_implication` is present;
- `operating_system_implication` is present or explicitly marked `not_applicable`;
- `confidence` is assigned;
- `disallowed_use` includes no investment advice;
- a reviewer note exists.

Any missing condition blocks entry into real report generation. `report_ready` is an upstream workflow status, not proof that a hypothesis, company exposure, or investment case is correct.

## 5. Report object schema

The future report object is `toc_calibrated_chokepoint_report` with these fields:

| Field | Definition |
|---|---|
| `report_id` | Stable unique identifier for the report object. |
| `report_version` | Version identifier incremented when scope, evidence, calibration, or review changes. |
| `research_question` | Specific, testable question addressed by the report. |
| `report_scope` | Included and excluded systems, products, stages, claims, and analytical boundaries. |
| `industry_or_theme` | Industry chain or theme under investigation. |
| `geography_or_market` | Relevant geographic, regulatory, or market scope. |
| `time_horizon` | Time window for the research hypothesis and monitoring plan. |
| `source_record_ids` | Accepted source records used by the evidence chain. |
| `corpus_entry_ids` | Reviewed corpus entries represented in the report. |
| `method_claim_ids` | Reviewed provisional method claims used as method basis. |
| `calibration_row_ids` | Reviewed, `report_ready` TOC calibration rows. |
| `evidence_boundary_note` | Scope, recency, independence, quotation, provenance, and missing-evidence limitations. |
| `toc_calibration_boundary_note` | Explicit statement that calibration is comparison and guardrail, not synonym replacement. |
| `non_investment_advice_note` | Required statement that the output is a research hypothesis and not investment advice. |
| `report_status` | One controlled state defined below. |
| `reviewer` | Human reviewer or authorized review role. |
| `created_at` | Report-object creation timestamp. |
| `updated_at` | Most recent material revision timestamp. |
| `limitations` | Consolidated source, method, calibration, company-evidence, market, and scope limitations. |
| `next_action` | Required sourcing, evidence review, calibration review, report review, monitoring, deferral, or rejection step. |

### Report status

| Status | Meaning |
|---|---|
| `draft_template` | Initial report object; required inputs and sections may be incomplete. |
| `source_chain_ready` | Required source, corpus, method-claim, and calibration identifiers are traceable. |
| `evidence_reviewed` | Supporting, contradicting, alternative, and missing evidence have been reviewed. |
| `calibration_reviewed` | TOC overlap, difference, guardrails, and false-equivalence risks have been reviewed. |
| `report_reviewed` | Structure, wording, confidence, limitations, invalidation conditions, and boundaries have been reviewed. |
| `publishable_research_hypothesis` | The output is suitable for publication as an evidence-bounded research hypothesis under its stated limitations. |
| `rejected` | The report object is unsupported, misleading, outside scope, or unsuitable for publication. |
| `deferred` | Work is paused because sources, evidence, calibration, review, or timing is insufficient. |

`publishable_research_hypothesis` is still not investment advice, a real-company recommendation, or a promise of performance. Reasons for `rejected` and `deferred` must remain traceable.

## 6. Required report sections

Future reports must contain these sections in this order:

1. **Research question / 研究问题**
2. **Scope and system boundary / 范围与系统边界**
3. **Demand anchor / 需求锚**
4. **Value-chain decomposition / 产业链拆解**
5. **Candidate chokepoint / 候选供应链卡点**
6. **Chokepoint Theory method basis / Chokepoint Theory 方法依据**
7. **TOC calibration / TOC 校准**
8. **Evidence table / 证据表**
9. **Candidate exposure map / 候选暴露图谱**
10. **Value capture logic / 价值捕获逻辑**
11. **Counterevidence and alternative explanations / 反证与替代解释**
12. **False-equivalence checks / 误等同检查**
13. **Monitoring indicators / 跟踪指标**
14. **Invalidation conditions / 假设失效条件**
15. **Confidence and limitations / 置信度与限制**
16. **Non-investment-advice disclaimer / 非投资建议声明**

Missing sections must be marked incomplete rather than silently omitted. Section order preserves the progression from question and system boundary through evidence, calibration, exposure hypotheses, counterevidence, monitoring, and invalidation.

## 7. Section requirements

### 1. Research question / 研究问题

- State one primary, testable research question.
- Identify whether the question concerns existence, persistence, substitution, capacity, qualification, value capture, market expectations, or invalidation.
- Avoid embedding a preferred company or trade conclusion in the question.

### 2. Scope and system boundary / 范围与系统边界

- Define included and excluded products, stages, customers, geographies, time windows, and decision context.
- State the system goal used for any TOC comparison.
- Distinguish the investment-research boundary from any enterprise operating-system boundary.

### 3. Demand anchor / 需求锚

- Describe evidence for demand magnitude, persistence, visibility, and timing.
- Separate end demand from orders, inventory restocking, policy narrative, and speculative attention.
- Record demand counterevidence and the conditions under which the anchor weakens.

### 4. Value-chain decomposition / 产业链拆解

- Map major stages, dependencies, qualification paths, capacity links, substitution routes, and information gaps.
- Define effective output or throughput relevant to the research question.
- Avoid treating every scarce component as a system-level constraint.

### 5. Candidate chokepoint / 候选供应链卡点

- State the candidate as a research hypothesis.
- Record why it may constrain effective supply, how the constraint could be released or migrate, and what evidence is missing.
- Distinguish persistent structural characteristics from a temporary shortage or popular narrative.

### 6. Chokepoint Theory method basis / Chokepoint Theory 方法依据

- List the relevant `method_claim_ids`, claim types, dimensions, confidence, limitations, and review status.
- Preserve source attribution and distinguish Serenity original expression from secondary interpretation and assistant inference.
- Do not claim the method is complete or officially endorsed.

### 7. TOC calibration / TOC 校准

- Include the required fields from Section 10.
- Record both overlap and difference; neither may be omitted.
- Explain the reasoning guardrail without substituting TOC terminology for the source-grounded method claim.

### 8. Evidence table / 证据表

- Use the fields and rules in Section 8.
- Include supporting, contradicting, alternative, and missing evidence.
- Keep source strength separate from hypothesis confidence.

### 9. Candidate exposure map / 候选暴露图谱

- Describe candidate exposure types and causal pathways only.
- Do not provide a real-company conclusion or recommendation.
- For every exposure type, list required evidence, material risks, counterevidence, and invalidation conditions.

### 10. Value capture logic / 价值捕获逻辑

- Describe the mechanism by which a candidate exposure could affect orders, utilization, pricing, bargaining power, revenue, margin, or strategic position.
- Separate operational constraint effects from market valuation and expectation effects.
- Do not promise profit, share-price appreciation, or investment return.

### 11. Counterevidence and alternative explanations / 反证与替代解释

- Present the strongest contradictory evidence and plausible alternatives.
- Test substitution, hidden capacity, inventory effects, demand timing, regulation, qualification failure, customer concentration, and constraint migration where relevant.
- Do not relegate counterevidence to a generic risk paragraph.

### 12. False-equivalence checks / 误等同检查

- Check that a supply-chain chokepoint is not automatically treated as a TOC constraint.
- Check that a shortage is not automatically treated as a chokepoint.
- Check that market narrative is not treated as evidence.
- Check that valuation gap is not treated as throughput.
- Record any remaining equivalence risk and its effect on confidence.

### 13. Monitoring indicators / 跟踪指标

- Define observable indicators tied to demand, queues, lead times, qualification, capacity, substitution, pricing, utilization, orders, customer behavior, and constraint migration as applicable.
- State source, cadence, interpretation boundary, and what change would matter.
- Indicators monitor hypotheses; they are not trading signals.

### 14. Invalidation conditions / 假设失效条件

- Define specific conditions that would weaken or reject the candidate chokepoint, value-capture, or exposure hypothesis.
- Include time, magnitude, substitution, capacity, qualification, demand, and evidence-quality thresholds where appropriate.
- State what report status or next action follows invalidation.

### 15. Confidence and limitations / 置信度与限制

- Assign report-hypothesis confidence using Section 11.
- Consolidate source, translation, evidence, calibration, company, market, and time-horizon limitations.
- Confidence is research-hypothesis confidence, not investment certainty.

### 16. Non-investment-advice disclaimer / 非投资建议声明

- State explicitly that the report is an evidence-bounded research hypothesis and does not constitute investment advice.
- Prohibit buy/sell instructions, personalized recommendations, target prices, position sizing, and return promises.
- State that Serenity has not endorsed, authorized, reviewed, or approved the report unless independently documented.

## 8. Evidence table requirements

The future report evidence table must contain:

| Field | Definition |
|---|---|
| `evidence_id` | Stable identifier for the evidence item. |
| `source_type` | Controlled source taxonomy value. |
| `source_locator` | Reviewable URL or other authorized provenance locator. |
| `source_date` | Publication or observation date with uncertainty preserved. |
| `claim_supported` | Bounded report or method claim the evidence supports. |
| `claim_contradicted` | Bounded report or method claim the evidence contradicts or weakens. |
| `evidence_role` | Primary method evidence, secondary context, industry evidence, company evidence, market evidence, counterevidence, or missing check. |
| `evidence_strength` | Strength assessment based on provenance, directness, recency, independence, and relevance. |
| `source_limitations` | Attribution, context, translation, access, scope, date, independence, and completeness limitations. |
| `confidence` | Confidence in the evidence interpretation, not investment certainty. |
| `review_note` | Reviewer findings, ambiguity, disagreement, and next checks. |

Rules:

- Social media virality is not evidence by itself.
- Community interpretation cannot be treated as Serenity original method.
- Assistant inference cannot be treated as source evidence.
- Company evidence supports research hypotheses, not Serenity methodology distillation.
- No evidence item alone supports an investment conclusion.
- Evidence supporting a claim must not erase contradictory evidence or missing checks.

## 9. Candidate exposure map boundary

The candidate exposure map may identify exposure types, not recommendations.

Possible exposure types include:

- upstream supplier;
- bottleneck tool;
- bottleneck material;
- qualification owner;
- capacity owner;
- data owner;
- customer validator;
- standards holder;
- substitute pathway.

The map must not say “buy,” “sell,” “winner,” “guaranteed beneficiary,” “target price,” or “position size.” It must include the evidence required to establish each exposure pathway, material risks, competing pathways, and invalidation conditions.

An exposure type does not establish that a real company has the exposure, can capture value, or is investable. Real-company mapping requires separate authorization and reviewed company evidence.

## 10. TOC calibration section requirements

The future TOC calibration section must contain:

- `method_claim_id`;
- `calibration_row_id`;
- `possible_toc_overlap`;
- `possible_toc_difference`;
- `toc_correction_or_guardrail`;
- `false_equivalence_risk`;
- `investment_research_implication`;
- `operating_system_implication`;
- `non_equivalence_warning`.

TOC improves the discipline of reasoning. TOC does not replace Serenity's source-grounded Chokepoint Theory. A TOC constraint is not automatically the same as a supply-chain chokepoint.

If the operating-system implication is not relevant, record `not_applicable` and explain why. If overlap or difference cannot be supported, the calibration row must not be presented as complete.

## 11. Report confidence rules

The report-hypothesis `confidence` levels are:

| Level | Meaning |
|---|---|
| `low` | Material gaps exist in the source chain, evidence, calibration, counterevidence, scope, or invalidation design. |
| `medium` | The hypothesis has meaningful support but remains limited by source concentration, ambiguity, missing checks, or unresolved alternatives. |
| `high` | The source chain, evidence review, calibration review, counterevidence review, and invalidation conditions are strong and mutually consistent within the stated scope. |

Confidence means report-hypothesis confidence. It is not investment certainty, a probability of return, or a recommendation strength.

Rules:

- High confidence requires a traceable source chain, evidence review, calibration review, counterevidence review, and explicit invalidation conditions.
- Single-source reports remain `low` or `medium`.
- Unresolved false-equivalence risk lowers or caps confidence.
- Missing company evidence prevents company-specific confidence.
- Material disagreement, translation ambiguity, stale evidence, or unclear system boundaries lowers confidence.
- Confidence cannot create investment advice or convert a candidate exposure into a real-company conclusion.

## 12. Output boundary

V1.0E output is limited to the report template defined in this document.

It must not output:

- real investment research reports;
- real company analysis;
- real company conclusions;
- buy/sell instructions;
- target prices;
- position sizing;
- return promises;
- claims of Serenity endorsement, authorization, approval, or review;
- claims that Chokepoint Theory equals TOC;
- claims that the method is complete;
- claims that a candidate chokepoint is confirmed without evidence review.

It also must not create corpus data, a corpus directory, real method claims, real calibration rows, examples, scraper or API integration, or validator logic in this phase.

## 13. Future PR split

- **V1.0E1: TOC-Calibrated Chokepoint Research Report Template document** — this pull request.
- **V1.0E2: Optional machine-readable report schema, no data** — define report structure without real report objects.
- **V1.0E3: Validator light checks for report template and schema files** — add bounded structural validation without generating reports.
- **V1.0F: First Manual Case Replay using manually provided, bounded, authorized source records** — exercise the workflow under separate authorization.

Each later phase requires separate authorization and scope review. V1.0E does not pre-authorize real sources, claims, calibration, company mapping, reports, recommendations, or investment outputs.

## 14. Final boundary note

This template defines future TOC-calibrated Chokepoint research report structure only. It performs no X scraping, uses no twscrape, accesses no secrets, calls no external APIs, imports no real Serenity original text, creates no corpus data, extracts no real method claims, performs no real TOC calibration, produces no real company conclusions, generates no real investment research report, and provides no investment advice.
