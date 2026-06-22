# TOC Calibration Matrix v1.0D — Comparing Chokepoint Theory Method Claims with Theory of Constraints

## 1. Purpose

This document defines the future structure for systematically calibrating reviewed Chokepoint Theory `method_claim_candidate` objects against concepts from the Theory of Constraints (TOC). It specifies eligibility, matrix-row fields, candidate TOC concepts, relationship types, review states, confidence rules, false-equivalence controls, and output boundaries.

V1.0D does not collect source data. V1.0D does not scrape X. V1.0D does not use twscrape. V1.0D does not call external APIs. V1.0D does not add real Serenity corpus entries. V1.0D does not extract real method claims. V1.0D does not execute real TOC calibration. V1.0D only defines the future TOC calibration matrix structure.

This phase creates no matrix rows containing real claims or calibration results. It does not assert that Chokepoint Theory is equivalent to TOC.

## 2. Relationship to V1.0A, V1.0B, and V1.0C

The V1.0 sequence has four distinct controls before any report generation:

- V1.0A defines authorized intake.
- V1.0B defines source records, corpus entries, and distillation queue items.
- V1.0C defines the `method_claim_candidate` extraction protocol.
- V1.0D defines how future calibration-ready method claims may be compared with TOC.
- V1.0D cannot bypass V1.0A, V1.0B, or V1.0C.
- Only `calibration_ready` `method_claim_candidate` objects may enter future TOC calibration.
- Calibration matrix compliance does not imply truth, investment merit, or TOC equivalence.

The source chain and limitations established upstream must remain traceable through every future calibration row. Structural readiness is not evidence that a method claim is correct, complete, generalizable, or suitable for investment use.

## 3. Calibration principles

Future calibration must follow these principles:

1. **Non-equivalence first**: begin by assuming that neighboring terms may differ in purpose, system boundary, mechanism, and evidence requirements.
2. **TOC as calibration framework, not synonym**: use TOC to test clarity and system logic, not to rename Chokepoint Theory.
3. **Method claim remains source-grounded**: calibration must preserve the source chain and must not turn a TOC interpretation into Serenity source meaning.
4. **TOC concepts must be explicitly mapped, not assumed**: every proposed relationship needs a named concept and a reviewable rationale.
5. **Overlap and difference must both be recorded**: similarity without difference analysis is incomplete.
6. **Investment research purpose must be distinguished from operating-system constraint management**: the two contexts may ask different questions and optimize different outcomes.
7. **No single method claim establishes a general theory**: one candidate row cannot prove a universal framework.
8. **Calibration cannot generate real company conclusions**: company-specific conclusions require separate evidence and authorization.
9. **Calibration cannot generate investment advice**: no row may become a buy/sell instruction, target price, position size, or return promise.
10. **Uncertainty and ambiguity must remain visible**: calibration must not erase disagreement to produce a cleaner mapping.
11. **TOC correction must not overwrite Serenity source meaning**: a guardrail may identify a risk without rewriting the upstream claim.
12. **Serenity source meaning must not be stretched to fit TOC**: unsupported alignment must be marked insufficient, distinct, or not applicable.

## 4. Calibration input requirements

A future input may enter TOC calibration only when all of the following are true:

- the `method_claim_candidate` has `review_status = calibration_ready`;
- `source_queue_id` exists;
- `corpus_entry_ids` exist;
- `source_support` and `source_limitations` are recorded;
- `disagreement_or_ambiguity` is recorded, including an explicit `none identified` when appropriate;
- `claim_type` is known;
- `chokepoint_method_dimension` is mapped;
- `toc_calibration_relevance` is tagged;
- `confidence` is assigned;
- `non_equivalence_warning` exists;
- assistant inference is separated from source expression;
- a reviewer note exists.

If any requirement is missing, the claim must remain outside active calibration until corrected, deferred, or rejected. Input eligibility does not establish a valid TOC mapping.

## 5. Calibration matrix row schema

The future calibration unit is `toc_calibration_matrix_row` with these fields:

| Field | Definition |
|---|---|
| `calibration_row_id` | Stable unique identifier for the calibration row. |
| `method_claim_id` | Identifier of the reviewed, calibration-ready candidate claim. |
| `claim_statement` | Current bounded method-claim wording. |
| `claim_type` | V1.0C claim classification. |
| `chokepoint_method_dimension` | Candidate Chokepoint Theory dimension mapping. |
| `toc_calibration_relevance` | Upstream tags identifying potential TOC comparison areas. |
| `toc_concept_candidate` | One or more controlled candidate concepts from Section 6. |
| `possible_toc_overlap` | Bounded description of a possible similarity to test. |
| `possible_toc_difference` | Bounded description of purpose, scope, mechanism, evidence, or application differences. |
| `calibration_question` | Specific question the calibration review must answer. |
| `toc_correction_or_guardrail` | TOC-informed check that may prevent a category error or overstatement without rewriting the source claim. |
| `investment_research_implication` | Potential implication within supply-chain and investment-research reasoning, stated without a company conclusion or advice. |
| `operating_system_implication` | Potential implication within TOC system improvement, throughput, flow, WIP, subordination, or constraint management. |
| `false_equivalence_risk` | Explicit category-error risk identified using Section 11. |
| `evidence_required_for_calibration` | Additional conceptual, source, operational, or counterexample evidence required to review the mapping. |
| `source_limitations` | Limitations inherited from the method claim and its source chain. |
| `ambiguity_or_disagreement` | Unresolved wording, interpretations, TOC mapping disputes, and scope uncertainty. |
| `confidence` | Calibration-fidelity level from Section 10. |
| `review_status` | One controlled state from Section 9. |
| `allowed_use` | Permitted uses, such as conceptual review and future report-structure preparation. |
| `disallowed_use` | Prohibited uses, including replacing source meaning, real company conclusions, and investment advice. |
| `next_action` | Required source-chain check, TOC mapping review, guardrail review, report handoff, deferral, or rejection. |

A future extension may add `calibration_relationship_type` from Section 7 as a dedicated field. Until then, any relationship label must remain explicit and reviewable rather than hidden in prose.

## 6. TOC concept candidate taxonomy

Future rows may use these `toc_concept_candidate` values:

- `system_boundary`
- `system_goal`
- `throughput`
- `inventory`
- `operating_expense`
- `constraint`
- `CCR`
- `non_constraint`
- `local_bottleneck`
- `market_constraint`
- `five_focusing_steps`
- `drum_buffer_rope`
- `choke_the_release`
- `subordination`
- `elevation`
- `buffer_management`
- `constraint_release`
- `constraint_migration`
- `throughput_accounting`
- `necessary_condition`
- `sufficient_condition`
- `evaporating_cloud`
- `current_reality_tree`
- `strategy_and_tactics_tree`

These candidate TOC concepts are comparison tools only. Their selection does not mean Chokepoint Theory contains, adopts, or is derived from those concepts. A row may identify multiple candidates when their roles are separated, or `not_applicable` through the relationship type when no useful mapping exists.

## 7. Calibration relationship types

The future `calibration_relationship_type` enum is:

| Relationship type | Meaning |
|---|---|
| `strong_overlap` | Substantial functional and conceptual similarity is supported, while remaining differences and non-identity are recorded. |
| `partial_overlap` | Some elements align, but scope, purpose, mechanism, evidence, or application materially differs. |
| `analogy_only` | The TOC concept is useful as an explanatory analogy but cannot support theoretical identity. |
| `adjacent_but_distinct` | The concepts address neighboring problems but should remain separately defined. |
| `conflicting_frame` | The TOC framing and candidate claim use materially incompatible goals, boundaries, assumptions, or causal models. |
| `TOC_guardrail_needed` | TOC supplies a check that can prevent a local-optimum, bottleneck, throughput, or system-boundary error. |
| `Chokepoint_specific` | The judgment primarily belongs to investment research, supply-chain positioning, market expectations, or value-capture analysis. |
| `insufficient_evidence` | Available support cannot sustain a calibration relationship and must block over-calibration. |
| `not_applicable` | No meaningful TOC comparison is identified for the bounded claim. |

`strong_overlap` still does not mean the concepts are completely identical. `analogy_only` must not be presented as theoretical sameness. `TOC_guardrail_needed` means TOC may help prevent a misclassification, not replace Chokepoint Theory. `Chokepoint_specific` preserves the investment-research or supply-chain context. `insufficient_evidence` must stop promotion to stronger calibration language.

## 8. Calibration workflow

A future authorized calibration review must follow this sequence:

1. **Select `calibration_ready` `method_claim_candidate`**: choose one with complete upstream review metadata.
2. **Verify source chain**: confirm queue, corpus entries, accepted source records, attribution, inference separation, and reviewer notes.
3. **Read `claim_statement` and source limitations**: preserve the bounded wording and uncertainty.
4. **Identify candidate TOC concept**: select from Section 6 or determine that no useful mapping applies.
5. **State possible overlap**: describe the narrowest supported similarity.
6. **State possible difference**: compare goals, system boundaries, mechanisms, evidence, and use contexts.
7. **Form `calibration_question`**: ask a specific question that could confirm, narrow, or reject the mapping.
8. **Identify false-equivalence risk**: apply Section 11 controls.
9. **Add TOC correction or guardrail**: record any TOC-informed check without overwriting the claim.
10. **Separate investment research implication from operating-system implication**: complete both fields independently.
11. **Record evidence required for calibration**: state missing TOC, source, operational, or counterexample checks.
12. **Assign confidence**: use Section 10 calibration-fidelity rules.
13. **Assign review status**: use Section 9.
14. **Decide `next_action`**: choose further review, future report handoff, deferral, or rejection.
15. **Preserve non-equivalence warning**: retain it through every version and downstream handoff.

Every material change to mapping, overlap, difference, guardrail, confidence, or review state must be versioned in a future machine-readable implementation.

## 9. Review status

The `review_status` enum is:

| Review status | Meaning |
|---|---|
| `draft` | Initial matrix row; mapping and boundaries have not been fully checked. |
| `source_chain_checked` | Upstream claim, source links, support, limitations, and inference separation have been checked. |
| `toc_mapping_reviewed` | Candidate TOC concepts and their definitions have been reviewed for relevance. |
| `overlap_difference_reviewed` | Both similarity and difference analyses have been reviewed. |
| `guardrail_reviewed` | False-equivalence risks and TOC correction or guardrail have been reviewed. |
| `report_ready` | The row has enough reviewed structure for a future V1.0E report template. |
| `deferred` | Review is paused because sources, concepts, evidence, sequencing, or reviewer capacity are insufficient. |
| `rejected` | The mapping is unsupported, misleading, duplicative, outside scope, or otherwise unsuitable. |

`report_ready` means only that a row can enter a future report template; it does not establish an investment conclusion. `guardrail_reviewed` does not mean TOC has replaced Chokepoint Theory. Reasons for `rejected` and `deferred` must be retained with reviewer and source-chain traceability.

## 10. Confidence rules

The calibration `confidence` levels are:

| Level | Meaning |
|---|---|
| `low` | Material uncertainty exists in the method claim, TOC concept, mapping, context, evidence, or false-equivalence risk. |
| `medium` | The mapping is reasonably clear but remains limited by source support, ambiguity, concept scope, or unresolved differences. |
| `high` | The method claim is clear, the TOC concept is explicit, overlap and difference are well bounded, and ambiguity and false-equivalence risk are low. |

Confidence measures calibration fidelity. It is not investment certainty, forecast confidence, or expected return.

Rules:

- High confidence requires a clear method claim, an explicit TOC concept, clear overlap and difference, and low material ambiguity.
- Single-source or ambiguous method claims normally remain `low` or `medium`.
- Translated, secondary, or community-derived claims lower or cap confidence.
- Material false-equivalence risk lowers confidence.
- Missing TOC concept evidence or unclear system boundaries lowers confidence.
- Confidence cannot convert calibration into a real company conclusion or investment advice.
- Confidence must be reassessed when the upstream claim, source limitations, TOC mapping, or disagreement changes.

## 11. False equivalence controls

Every future calibration row must actively test and preserve risks such as:

- treating Chokepoint Theory as equivalent to TOC;
- supply-chain chokepoint = TOC constraint;
- local bottleneck = system constraint;
- shortage = chokepoint;
- market narrative = evidence;
- valuation gap = operational throughput;
- position sizing = TOC decision rule;
- company winner = confirmed chokepoint owner;
- Serenity-style synthesis = Serenity original method.

Any identified risk must remain visible in `false_equivalence_risk`, even if a reviewer later finds meaningful overlap. A row must not hide the risk merely because it receives a higher confidence or later review status.

TOC can correct a system-boundary or local-optimum mistake without converting an investment-research claim into an operations-management rule. Likewise, a Chokepoint Theory claim may expose supply-chain value capture or market expectation dynamics that are outside TOC's intended meaning.

## 12. Investment research vs operating system distinction

Every future row must separately complete:

- `investment_research_implication`
- `operating_system_implication`

Chokepoint Theory often operates in investment research and supply-chain value-capture context. TOC often operates in system improvement, throughput, work-in-process, subordination, and constraint-management context. A concept may be useful across both contexts but must not be collapsed into one meaning.

The investment-research field may describe what a calibrated distinction changes about a research question, evidence requirement, or value-capture hypothesis. It must not name a real company conclusion or recommend a trade. The operating-system field may describe implications for flow, throughput, buffers, constraints, subordination, or elevation within a defined system.

A “chokepoint” in an investment research report does not automatically equal a TOC constraint in an enterprise operating system.

## 13. Output boundary

V1.0D output is limited to the TOC Calibration Matrix structure and future calibration protocol defined in this document.

It must not output:

- real TOC calibration results;
- real Serenity distilled method claims;
- real company analysis;
- real investment research reports;
- buy/sell instructions;
- target prices;
- position sizing;
- return promises;
- claims of Serenity endorsement, authorization, approval, or review;
- claims that Chokepoint Theory equals TOC;
- claims that the method is complete.

It also must not create corpus data, a corpus directory, machine-readable calibration rows, examples, scraper or API integration, or validator logic in this phase.

## 14. Future PR split

- **V1.0D1: TOC Calibration Matrix document** — this pull request.
- **V1.0D2: Optional machine-readable calibration row schema, no data** — define structure without real calibration rows.
- **V1.0D3: Validator light checks for calibration matrix and schema files** — add bounded structural validation without executing calibration.
- **V1.0E: TOC-Calibrated Chokepoint Research Report Template** — define a future report structure using reviewed calibration rows.
- **V1.0F: First Manual Case Replay using manually provided, bounded, authorized source records** — exercise the separately authorized workflow.

Each later phase requires separate authorization and scope review. V1.0D does not pre-authorize real sources, method claims, calibration results, company analysis, report generation, or investment outputs.

## 15. Final boundary note

This matrix defines future TOC calibration structure only. It performs no X scraping, uses no twscrape, accesses no secrets, calls no external APIs, imports no real Serenity original text, creates no corpus data, extracts no real method claims, performs no real TOC calibration, produces no real company conclusions, and provides no investment advice.
