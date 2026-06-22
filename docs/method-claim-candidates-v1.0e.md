# Method Claim Candidates v1.0E

## 1. Purpose

This file generates a first bounded set of candidate method claims from the five approved seed source records. It is a review artifact for testing wording, source support, recurrence, generative power, distinctiveness, counterevidence needs, and future TOC calibration questions.

These are candidate method claims, not validated method claims. Candidate extraction does not establish a complete Serenity Chokepoint Theory, a universal research rule, a TOC equivalence, a real company conclusion, or an investment recommendation. Every candidate remains subject to additional original-source support, cross-case testing, human review, and separate validation.

## 2. Source base

This pass reads only the following seed source records:

| source_record_id | source role in this pass | direct Serenity-method support allowed? |
| --- | --- | --- |
| `SRC-0001` | Provisionally approved Serenity original public expression candidate concerning an asserted two-layer AXTI/InP bottleneck and physical supply-chain tracing. | Yes, but only as a single, provisionally approved expression whose publication date remains unresolved. |
| `SRC-0002` | USGS industry evidence concerning indium concentration, import reliance, restrictions, uses, and substitution boundaries. | No. It may corroborate, contradict, narrow, or boundary-check a case premise. |
| `SRC-0003` | AXT company evidence from the April 21, 2026 Form 424B5 concerning intended offering uses and possible capacity expansion. | No. It may test elevation, constraint-release, financing, and value-capture questions. |
| `SRC-0004` | Valens Q3 2025 company evidence concerning period-specific financial data and evidence-definition boundaries. | No. It may support cross-case evidence hygiene and overclaim filters. |
| `SRC-0005` | Barron's public secondary analysis concerning offering, guidance, and market-reaction framing. | No. It may provide secondary context and questions but cannot establish offering terms or Serenity attribution. |

Only `SRC-0001` can directly support a candidate about Serenity's expression. `SRC-0002` through `SRC-0005` are limited to case evidence, boundary checking, corroboration, contradiction, and question generation. Their agreement with a candidate does not convert that candidate into a Serenity method rule.

The present source base contains one Serenity original public expression candidate and four non-Serenity evidence records. That is insufficient for final Serenity Chokepoint Theory distillation.

## 3. Candidate claim table

| claim_id | claim_text | source_record_ids | source_support_level | confidence | status | main limitation |
| --- | --- | --- | --- | --- | --- | --- |
| `MCC-0001` | A candidate chokepoint review should test whether the same entity appears at more than one constrained layer rather than assuming that one claimed bottleneck is the whole system constraint. | `SRC-0001` | Single Serenity original-expression candidate; no cross-case recurrence. | low | `candidate_not_validated` | One rhetorical Reddit case cannot establish a general two-layer method rule. |
| `MCC-0002` | A candidate research sequence may trace demand downward through the value chain until it reaches physical materials, capacity, or other hard supply floors, while separately testing whether each mapped layer is actually constraining. | `SRC-0001`, `SRC-0002` | One Serenity expression plus industry corroboration of selected physical premises. | medium-low | `candidate_not_validated` | Industry evidence supports case facts, not the distinctiveness or generality of Serenity's sequence. |
| `MCC-0003` | Identifying a supply-chain constraint is not sufficient to infer common-shareholder value capture; financing, dilution, entity structure, operating conversion, and market expectations require separate review. | `SRC-0001`, `SRC-0003`, `SRC-0005` | One Serenity expression with company and secondary boundary evidence. | medium-low | `candidate_not_validated` | The value-capture distinction is plausible but has not recurred across multiple Serenity original expressions or approved cases. |
| `MCC-0004` | A financing purpose or capacity-expansion plan is only a candidate elevation path; it does not show that a constraint has been released or that new capacity is qualified, utilized, profitable, or value-accretive. | `SRC-0003` | Company-evidence hypothesis only; no direct Serenity support. | medium | `insufficient_serenity_support` | Clear case boundary, but it cannot be attributed to Serenity from the current source base. |
| `MCC-0005` | No single industry, company, or secondary source should independently establish a company-level chokepoint conclusion; source roles, periods, definitions, and primary-versus-secondary status must remain separated. | `SRC-0002`, `SRC-0003`, `SRC-0004`, `SRC-0005` | Recurrent boundary across four non-Serenity records; no direct Serenity support. | medium | `insufficient_serenity_support` | Strong evidence-hygiene candidate, but distinctiveness to Serenity is unestablished. |
| `MCC-0006` | Deleted or unavailable post bodies should not be reconstructed or used in a method-support chain; only separately reviewable surviving records may contribute support. | `SRC-0004` | Seed-record boundary evidence only; no direct Serenity support. | medium | `insufficient_serenity_support` | This is primarily a provenance and safety rule, not yet evidence of a distinctive Serenity method. |

## 4. Candidate claim blocks

### MCC-0001 — Two-layer bottleneck candidate

```yaml
claim_id: MCC-0001
claim_text: A candidate chokepoint review should test whether the same entity appears at more than one constrained layer rather than assuming that one claimed bottleneck is the whole system constraint.
claim_type: causal_mechanism
source_record_ids:
  - SRC-0001
source_support_level: single_provisional_serenity_expression
serenity_original_support: SRC-0001 explicitly frames one company as appearing at two asserted bottleneck layers, but the wording is rhetorical and tied to one case.
industry_or_company_support: none_direct; no industry or company record can establish that this is a Serenity method rule.
secondary_support: none
cross_case_recurrence: insufficient; observed in one AXTI/InP Reddit expression only.
generative_power: candidate_only; it can generate a multi-layer constraint-mapping question but has not been tested across cases.
distinctiveness: needs_more_serenity_original_support; multi-layer dependency analysis is not shown to be unique to Serenity.
confidence: low
counterevidence_needed:
  - Serenity original expressions where a claimed two-layer structure is rejected or narrowed
  - cases where one entity appears at multiple layers but does not constrain system throughput
  - cases showing independent constraints at separate layers
toc_calibration_question: How should an entity appearing at multiple constrained layers be distinguished from a single system constraint, multiple local bottlenecks, or multiple CCRs?
status: candidate_not_validated
reviewer_note: Preserve the narrow test question. Do not generalize the Reddit post's company claims or treat the two-layer formulation as a validated rule.
```

### MCC-0002 — Physical-floor mapping candidate

```yaml
claim_id: MCC-0002
claim_text: A candidate research sequence may trace demand downward through the value chain until it reaches physical materials, capacity, or other hard supply floors, while separately testing whether each mapped layer is actually constraining.
claim_type: sequencing_rule
source_record_ids:
  - SRC-0001
  - SRC-0002
source_support_level: one_serenity_expression_plus_industry_case_corroboration
serenity_original_support: SRC-0001 traces an asserted AI-photonics demand chain toward InP substrates and source materials.
industry_or_company_support: SRC-0002 supports selected case premises about indium concentration, restrictions, and InP uses, while warning that broad indium data do not establish wafer-grade substrate constraints or company value capture.
secondary_support: none
cross_case_recurrence: insufficient; the sequence has not been observed in multiple approved Serenity expressions or independent case replays.
generative_power: candidate_only; it can generate upstream-decomposition, physical-floor, substitution, and capacity questions.
distinctiveness: needs_more_serenity_original_support; upstream physical mapping is not shown to be uniquely Serenity without additional original expressions.
confidence: medium-low
counterevidence_needed:
  - Serenity cases that stop above the raw-material layer
  - cases where the physical input is abundant but qualification, equipment, software, regulation, or another layer is constraining
  - application-specific substitution and recycling evidence
toc_calibration_question: When does upstream physical-floor mapping identify the system constraint rather than merely another dependency inside the system boundary?
status: candidate_not_validated
reviewer_note: Industry corroboration raises case plausibility only. It does not validate the proposed sequence as Serenity methodology.
```

### MCC-0003 — Constraint versus company-value-capture candidate

```yaml
claim_id: MCC-0003
claim_text: Identifying a supply-chain constraint is not sufficient to infer common-shareholder value capture; financing, dilution, entity structure, operating conversion, and market expectations require separate review.
claim_type: value_capture_rule
source_record_ids:
  - SRC-0001
  - SRC-0003
  - SRC-0005
source_support_level: one_serenity_expression_with_company_and_secondary_boundary_evidence
serenity_original_support: SRC-0001 links an asserted physical constraint to direct listed-company exposure, but also contains promotional framing, positioning, valuation assertions, and explicit downside.
industry_or_company_support: SRC-0003 shows an equity financing and intended capacity use, while explicitly not proving completed capacity, qualification, utilization, profitability, or shareholder value capture.
secondary_support: SRC-0005 supplies bounded secondary framing of an offering, guidance, and market reaction; it is not primary evidence for terms and does not attribute a method to Serenity.
cross_case_recurrence: insufficient; no second approved Serenity original-expression case demonstrates the same constraint-to-equity separation.
generative_power: candidate_only; it can generate financing, dilution, structure, conversion, and expectation checks after a physical constraint is proposed.
distinctiveness: needs_more_serenity_original_support; the distinction may be generally sound research hygiene rather than a uniquely supported Serenity rule.
confidence: medium-low
counterevidence_needed:
  - Serenity original expressions explicitly separating system constraint from listed-equity capture
  - cases where a real constraint failed to benefit existing shareholders
  - cases where value capture occurred elsewhere in the chain
  - evidence about demand conversion, qualification, margins, capital intensity, and financing terms
toc_calibration_question: How should system throughput impact be compared with firm-level and shareholder-level economic capture without treating them as equivalent goals?
status: candidate_not_validated
reviewer_note: Keep operating scarcity, corporate capture, and common-shareholder capture as separate analytical layers.
```

### MCC-0004 — Constraint-release and elevation candidate

```yaml
claim_id: MCC-0004
claim_text: A financing purpose or capacity-expansion plan is only a candidate elevation path; it does not show that a constraint has been released or that new capacity is qualified, utilized, profitable, or value-accretive.
claim_type: risk_rule
source_record_ids:
  - SRC-0003
source_support_level: company_evidence_hypothesis_only
serenity_original_support: none
industry_or_company_support: SRC-0003 records intended use of offering proceeds for capacity expansion and explicitly preserves the boundary between a stated plan and a completed operating outcome.
secondary_support: none
cross_case_recurrence: insufficient; one company filing and no approved Serenity recurrence.
generative_power: candidate_only; it can generate milestones for financing, construction, qualification, ramp, utilization, economics, and constraint migration.
distinctiveness: unsupported_as_serenity_method; the current record supports a general evidence boundary, not attribution to Serenity.
confidence: medium
counterevidence_needed:
  - completed capacity-ramp evidence
  - qualification and customer-adoption evidence
  - throughput data before and after expansion
  - evidence of substitution, demand change, or constraint migration
toc_calibration_question: What evidence distinguishes an announced elevation action from actual constraint release, and when does the constraint migrate after elevation?
status: insufficient_serenity_support
reviewer_note: Retain as a hypothesis candidate and calibration question. Do not label it a Serenity method claim without original support.
```

### MCC-0005 — Single-source overclaim filter candidate

```yaml
claim_id: MCC-0005
claim_text: No single industry, company, or secondary source should independently establish a company-level chokepoint conclusion; source roles, periods, definitions, and primary-versus-secondary status must remain separated.
claim_type: evidence_rule
source_record_ids:
  - SRC-0002
  - SRC-0003
  - SRC-0004
  - SRC-0005
source_support_level: recurrent_non_serenity_boundary_evidence
serenity_original_support: none
industry_or_company_support: SRC-0002 limits national indium evidence; SRC-0003 limits planned-capacity inference; SRC-0004 separates period-specific financial definitions from valuation conclusions.
secondary_support: SRC-0005 requires offering terms to remain anchored to SEC filings and cannot establish Serenity attribution.
cross_case_recurrence: partial_boundary_recurrence_across_non_serenity_sources; not recurrence of a Serenity original method expression.
generative_power: candidate_only; it can generate source-role, period, definition, corroboration, and contradiction checks.
distinctiveness: unsupported_as_serenity_method; the rule currently appears as repository evidence hygiene rather than a distinctively sourced Serenity principle.
confidence: medium
counterevidence_needed:
  - multiple approved Serenity expressions about evidence sufficiency and source hierarchy
  - cases testing when one exceptionally authoritative source is sufficient for a narrow fact
  - examples distinguishing fact verification from company-level chokepoint conclusions
toc_calibration_question: What evidence threshold is required before a local resource issue may be treated as a system constraint, and how should contradicting evidence change that classification?
status: insufficient_serenity_support
reviewer_note: Useful as a hypothesis and safety filter, but not attributable to Serenity from the present source base.
```

### MCC-0006 — Deleted-source exclusion rule candidate

```yaml
claim_id: MCC-0006
claim_text: Deleted or unavailable post bodies should not be reconstructed or used in a method-support chain; only separately reviewable surviving records may contribute support.
claim_type: boundary_rule
source_record_ids:
  - SRC-0004
source_support_level: provenance_boundary_only
serenity_original_support: none
industry_or_company_support: SRC-0004 explicitly states that no deleted Reddit post body is incorporated and limits its use to company-reported, period-specific evidence.
secondary_support: none
cross_case_recurrence: not_applicable_as_method_recurrence; the boundary arose from provenance and source-availability controls.
generative_power: candidate_only; it can prevent invented context, unsupported attribution, and contaminated support chains.
distinctiveness: not_a_distinctive_serenity_claim_on_current_evidence; primarily a source-governance and safety rule.
confidence: medium
counterevidence_needed:
  - separately reviewable surviving comment permalinks
  - lawful, provenance-preserving copies supplied by an authorized human reviewer
  - evidence that clearly distinguishes original text from reconstruction or secondary recollection
toc_calibration_question: none_identified; this is a provenance boundary rather than a current TOC concept-comparison claim.
status: insufficient_serenity_support
reviewer_note: Keep this rule outside substantive Serenity-method attribution unless future original support explicitly establishes it as part of the method.
```

## 5. Validation gaps

The current candidates cannot be upgraded to validated claims because:

1. Serenity original expression is insufficient: the source base contains only one provisionally approved original-expression record.
2. Cross-case recurrence is insufficient: the candidate structures have not been reproduced across multiple approved Serenity cases.
3. X original expressions have not systematically entered the seed source base.
4. A single AXTI Reddit post cannot represent the complete Chokepoint Theory.
5. Industry and company evidence can test case premises and boundaries but cannot directly define Serenity's methodology.
6. Secondary coverage cannot be treated as original expression or primary evidence when a primary filing is available.
7. `SRC-0001` has unresolved publication-date metadata and includes rhetorical, promotional, and unverified company assertions.
8. Generative power has been proposed as review questions only; it has not been demonstrated through repeated manual case replays.
9. Distinctiveness remains unresolved because several candidates overlap with general supply-chain, evidence-quality, and research-governance practices.
10. No candidate has completed separate human method review or TOC calibration.

## 6. Recommended next step

The recommended next step is **V1.0F — Manual Review of Method Claim Candidates**.

Manual review should come before X Locator Seed Expansion because the current six candidates need wording, attribution, duplication, and scope decisions before the project gathers more material around them. Reviewers should decide which candidates are genuinely Serenity-method hypotheses, which are general evidence or safety rules, which should be split or narrowed, and what precise original-source gaps would change each status.

After that review produces an explicit, bounded source-gap list, a separately authorized X Locator Seed Expansion may target only the missing original expressions. It must not imply authorization to scrape timelines, use `twscrape`, call the X API, access secrets, or bypass login controls.

## 7. Final boundary note

This file contains candidate method claims only. It contains no validated method claims, no final Chokepoint Theory distillation, no TOC calibration conclusions, no real company conclusions, and no investment advice. All claims require further source support, human review, and separate validation before use in the Skill runtime.
