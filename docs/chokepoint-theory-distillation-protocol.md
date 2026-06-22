# Chokepoint Theory Distillation Protocol v1.0C — From Reviewed Corpus Entries to Method Claims

## 1. Purpose

This document defines the future protocol for distilling provisional Chokepoint Theory method claims from reviewed Serenity corpus entries. It establishes eligibility checks, the unit of distillation, claim classifications, review states, confidence rules, ambiguity handling, and the handoff boundary for later TOC calibration.

V1.0C does not collect source data. V1.0C does not scrape X. V1.0C does not use twscrape. V1.0C does not call external APIs. V1.0C does not add real Serenity corpus entries. V1.0C does not execute methodology distillation. V1.0C only defines the future distillation protocol.

This protocol does not assert that Serenity's methodology has already been distilled, completed, ordered, validated, or calibrated.

## 2. Relationship to V1.0A and V1.0B

The V1.0 sequence has distinct controls:

- V1.0A defines authorized intake.
- V1.0B defines source records, corpus entries, and distillation queue items.
- V1.0C defines how future queue items may be reviewed and converted into provisional method claims.
- V1.0C cannot bypass V1.0A or V1.0B.
- Only reviewed and `distillation_ready` corpus entries may be used in future distillation.
- Schema compliance does not imply method truth.

The [V1.0A Source Acquisition Gate](source-acquisition-gate.md) remains authoritative for what may enter. The [V1.0B Serenity Corpus Schema](serenity-corpus-schema.md) remains authoritative for upstream object and state boundaries. A future distillation process must preserve the full chain from accepted source record through corpus entry and queue item to each provisional method claim.

## 3. Distillation principles

Future methodology distillation must follow these principles:

1. **Source-grounded**: every candidate claim must be linked to eligible corpus entries and their accepted source records.
2. **Provenance-preserving**: normalization and synthesis must retain source locators, source types, attribution, and permission boundaries.
3. **Minimal quotation**: use only the bounded excerpt required for fidelity or wording review.
4. **Paraphrase-first**: prefer attributed paraphrase when exact wording is unnecessary.
5. **Source-type-aware**: original public expression, quoted secondary coverage, secondary analysis, community interpretation, user notes, and assistant inference have different evidentiary roles.
6. **Assistant inference separated**: generated interpretation must be visibly separated from source-supported language.
7. **Ambiguity preserved**: uncertain wording or scope must not be made artificially precise.
8. **Disagreement recorded**: conflicting sources and competing interpretations must remain visible.
9. **No single source establishes a method rule**: a single source may support a candidate, but not silently establish a general rule.
10. **Method claims remain provisional until reviewed**: extraction does not equal validation.
11. **No method claim can directly generate real company conclusions**: company research requires separate evidence and authorization.
12. **No investment advice**: claims must not become buy/sell instructions, target prices, position-sizing advice, or return promises.

## 4. Distillation input requirements

A future distillation input is eligible only when all of the following are true:

- corpus entry `status = distillation_ready`;
- its source record `status = accepted`;
- `source_type` is known;
- a source locator exists;
- attribution is clear;
- the excerpt boundary is bounded;
- source limitations are recorded;
- `chokepoint_method_dimension` is mapped;
- `toc_calibration_relevance` is tagged or explicitly marked `none_identified`;
- a reviewer note exists;
- assistant inference is separated from source expression.

The linked distillation queue item must also identify its source support, limitations, disagreement or ambiguity, reviewer, and next action. Failure of any requirement means the item must remain outside active distillation until corrected, deferred, or rejected.

Eligibility is a workflow threshold only. It does not establish that a source is complete, a candidate claim is true, or a method rule is generalizable.

## 5. Distillation unit

The future unit of methodology extraction is `method_claim_candidate`. It is a provisional, source-linked object with these fields:

| Field | Definition |
|---|---|
| `method_claim_id` | Stable unique identifier for the candidate claim. |
| `source_queue_id` | Identifier of the eligible distillation queue item. |
| `corpus_entry_ids` | Identifiers of the reviewed, `distillation_ready` entries supporting or challenging the claim. |
| `claim_version` | Version identifier incremented when wording, support, limits, or review status changes. |
| `claim_statement` | Bounded provisional statement that does not exceed its sources. |
| `claim_type` | One controlled value from Section 6. |
| `chokepoint_method_dimension` | One or more candidate dimensions from Section 7. |
| `source_support` | Attributed summary of supporting, contradicting, and contextual corpus entries. |
| `source_limitations` | Provenance, coverage, context, translation, date, and generalization limitations. |
| `disagreement_or_ambiguity` | Conflicting readings, uncertain wording, and unresolved scope. |
| `counterexamples_needed` | Cases or evidence needed to test, narrow, or reject the candidate claim. |
| `toc_calibration_relevance` | Relevant future TOC comparison tags or `none_identified`. |
| `confidence` | Extraction-fidelity level from Section 10. |
| `review_status` | One controlled review state from Section 9. |
| `allowed_use` | Permitted uses, such as methodology review and future calibration preparation. |
| `disallowed_use` | Prohibited uses, including real company conclusions and investment advice. |
| `next_action` | Required source check, ambiguity review, method review, calibration handoff, deferral, or rejection. |

A `method_claim_candidate` is not an official Serenity statement, a final method rule, a verified universal law, or a research recommendation.

## 6. Claim type taxonomy

The `claim_type` enum is:

| Claim type | Intended use |
|---|---|
| `definition` | Defines a concept without asserting a broader causal or procedural rule. |
| `distinction` | Distinguishes a chokepoint from a shortage, bottleneck, constraint, narrative, or other neighboring concept. |
| `causal_mechanism` | Explains how a candidate chokepoint may affect effective supply or throughput across an industry chain. |
| `evidence_rule` | Defines what evidence may support, contradict, weaken, or leave a chokepoint hypothesis unresolved. |
| `sequencing_rule` | Describes the order of research steps or checks. |
| `market_behavior_rule` | Addresses market attention, institutional rotation, expectation gaps, or pricing behavior without becoming a trade signal. |
| `value_capture_rule` | Addresses how a chokepoint may translate into revenue, margin, orders, bargaining power, or another economic-capture mechanism. |
| `risk_rule` | Addresses substitution, capacity expansion, demand decline, regulation, valuation crowding, or related risks. |
| `invalidation_rule` | Defines conditions under which a hypothesis should be weakened or rejected. |
| `reporting_rule` | Defines structure, evidence presentation, uncertainty, and boundaries for a future research report. |
| `boundary_rule` | Defines non-investment-advice, non-endorsement, non-impersonation, attribution, and other safety or scope boundaries. |

Claim typing must follow the claim's function, not its preferred conclusion. If a statement contains multiple functions, it should be split into bounded candidates or have one primary type with explicit related candidates.

## 7. Method dimension mapping

The protocol carries forward these candidate method dimension tags from V1.0B:

- `demand_anchor`
- `value_chain_decomposition`
- `physical_floor_mapping`
- `chokepoint_identification`
- `moat_verification`
- `substitution_difficulty`
- `capacity_or_lead_time_constraint`
- `qualification_or_customer_lock_in`
- `value_capture`
- `valuation_gap`
- `institutional_rotation_or_market_attention`
- `catalyst_or_earnings_validation`
- `thesis_killer`
- `monitoring_indicator`
- `position_sizing_or_conviction_boundary`
- `invalidation_condition`

Each `method_claim_candidate` must map to at least one dimension. Multiple dimensions are allowed only when the relationship is explicit; broad tagging must not replace a precise claim statement.

These dimensions remain candidates. Their use does not establish that Serenity's methodology contains every dimension, that the dimensions have been ordered, or that any dimension has been validated. The tag `position_sizing_or_conviction_boundary` records a possible method or safety boundary and does not authorize position-sizing advice.

## 8. Distillation workflow

A future authorized distillation run must follow this sequence:

1. **Select eligible queue item**: choose a queue item whose upstream scope and reviewer are clear.
2. **Verify corpus entry readiness**: confirm every linked entry is `distillation_ready` and every source record is `accepted`.
3. **Read source support summary**: review support, counterevidence, source types, and provenance without expanding the raw-source boundary.
4. **Extract bounded candidate method claim**: write the narrowest statement supported by the eligible entries.
5. **Assign `claim_type`**: select the functional category from Section 6.
6. **Assign method dimension**: map the candidate to one or more Section 7 dimensions.
7. **Preserve source limitations**: carry forward all relevant limitations rather than summarizing them away.
8. **Record ambiguity and disagreement**: state conflicting interpretations, uncertain terms, and unresolved scope.
9. **Identify counterexamples needed**: specify what could narrow, contradict, or invalidate the candidate.
10. **Mark TOC calibration relevance**: assign relevant comparison tags or `none_identified` without asserting equivalence.
11. **Set confidence and review status**: apply Sections 9 and 10 independently of investment outcomes.
12. **Decide `next_action`**: choose source checking, ambiguity review, claim review, calibration handoff, deferral, or rejection.
13. **Keep claim provisional until reviewed**: do not present the candidate as completed methodology.

Every material change to claim wording, support, limitations, confidence, or status must increment `claim_version` and preserve prior review history.

## 9. Review status

The `review_status` enum is:

| Review status | Meaning |
|---|---|
| `draft` | Initial extraction; source fidelity and boundaries have not been fully checked. |
| `source_checked` | Source links, source types, attribution, excerpt boundaries, and support references have been checked. |
| `ambiguity_reviewed` | Translation, context, disagreement, rhetoric, and competing interpretations have been reviewed and retained where unresolved. |
| `method_claim_reviewed` | Claim wording, type, dimension, support, limitations, and counterexamples have received methodology review. |
| `calibration_ready` | The provisional claim has enough review metadata for future V1.0D TOC calibration. |
| `rejected` | The candidate is unsupported, misclassified, overgeneralized, duplicative, or otherwise unsuitable. |
| `deferred` | Review is paused because evidence, context, sequencing, or reviewer capacity is insufficient. |

`calibration_ready` means only that a claim may enter the future TOC Calibration Matrix. It does not mean TOC calibration has been completed. `method_claim_reviewed` does not mean the claim is final truth. Reasons for `rejected` and `deferred` must be retained with source and reviewer traceability.

## 10. Confidence rules

The `confidence` levels are:

| Level | Meaning |
|---|---|
| `low` | Material uncertainty exists in provenance, wording, context, interpretation, generalization, or source coverage. |
| `medium` | The extraction is reasonably faithful but still limited by source count, context, translation, or unresolved scope. |
| `high` | Multiple consistent eligible sources or exceptionally clear original public expression strongly support the bounded extraction, with material ambiguity addressed. |

Confidence measures claim-extraction fidelity. It is not investment certainty, forecast confidence, or expected return.

Rules:

- High confidence requires multiple consistent sources or exceptionally clear original expression.
- Single-source claims normally remain `low` or `medium`.
- Translated or secondary sources lower or cap confidence unless checked against clear primary material.
- Material disagreement must lower or cap confidence.
- Missing context and metaphorical or time-bound wording must lower confidence when they affect meaning.
- Confidence cannot convert a method claim into a real company conclusion.
- Confidence must be reassessed when source support, wording, ambiguity, or counterevidence changes.

## 11. Ambiguity and disagreement handling

Each candidate claim must record, when applicable:

- conflicting interpretations;
- translation ambiguity;
- missing context;
- time-bound wording;
- rhetorical or metaphorical wording;
- community interpretation drift;
- assistant inference risk;
- source support gaps.

The reviewer must distinguish unresolved ambiguity from harmless wording variation. Ambiguity must not be resolved by inventing missing context or silently choosing the strongest interpretation. Community retellings must not overwrite original attribution, and assistant synthesis must not be labeled as Serenity's view.

Ambiguous claims must remain provisional. If ambiguity prevents a bounded, attributable claim, the candidate must be deferred or rejected rather than promoted.

## 12. TOC calibration handoff

V1.0C does not perform TOC calibration. It prepares a bounded handoff for future V1.0D comparison using these fields:

| Handoff field | Definition |
|---|---|
| `method_claim_id` | Identifier of the reviewed provisional method claim. |
| `claim_statement` | Current bounded candidate wording. |
| `claim_type` | Functional classification from Section 6. |
| `chokepoint_method_dimension` | Candidate method dimension mapping. |
| `toc_calibration_relevance` | Tags indicating possible relevance to TOC comparison. |
| `possible_toc_overlap` | Provisional area of similarity to test, not an equivalence claim. |
| `possible_toc_difference` | Provisional conceptual, operational, evidentiary, or purpose difference to test. |
| `calibration_question` | Specific question the future matrix must answer. |
| `non_equivalence_warning` | Explicit warning against treating Chokepoint Theory and TOC as synonyms. |

Chokepoint Theory must not be automatically equated with TOC. TOC calibration is a future comparison step, not a synonym replacement. A method claim can be relevant to TOC without being TOC.

The handoff must preserve source limitations, ambiguity, confidence, and review status even when those fields are not duplicated in the minimal handoff view.

## 13. Output boundary

V1.0C output is limited to this protocol and the future `method_claim_candidate` schema.

It must not output:

- real Serenity distilled method claims;
- real company analysis;
- real investment research reports;
- buy/sell instructions;
- target prices;
- position sizing;
- return promises;
- claims of Serenity endorsement, authorization, approval, or review;
- claims that the method is complete.

It also must not create corpus data, a corpus directory, machine-readable claim records, TOC calibration results, examples, or validator logic in this phase.

## 14. Future PR split

- **V1.0C1: Chokepoint Theory Distillation Protocol document** — this pull request.
- **V1.0C2: Optional machine-readable method claim schema, no data** — define structure without real claims.
- **V1.0C3: Validator light checks for protocol and schema files** — add bounded structural checks without distillation or collection capability.
- **V1.0D: TOC Calibration Matrix** — compare reviewed provisional method claims with TOC while preserving non-equivalence.
- **V1.0E: TOC-Calibrated Research Report Template** — define a future report structure with evidence and non-investment-advice controls.
- **V1.0F: First Manual Case Replay using manually provided, bounded, authorized source records** — exercise the authorized workflow under separate scope.

Each later phase requires its own authorization and pull request. V1.0C does not pre-authorize real sources, claims, calibration, company analysis, automation, or report generation.

## 15. Final boundary note

This protocol defines future methodology distillation only. It performs no X scraping, uses no twscrape, accesses no secrets, calls no external APIs, imports no real Serenity original text, creates no corpus data, extracts no real method claims, performs no TOC calibration, produces no real company conclusions, and provides no investment advice.
