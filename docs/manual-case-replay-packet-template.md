# Manual Case Replay Packet Template v1.0F1 — Preparing the First Authorized End-to-End Replay

## 1. Purpose

This document defines the packet template and execution boundaries for a future first authorized manual case replay. It organizes the minimum source packet, review checklists, traceability fields, pass/fail criteria, boundary controls, and future implementation split needed to test the V1.0A–V1.0E workflow end to end.

V1.0F1 does not collect source data. V1.0F1 does not scrape X. V1.0F1 does not use twscrape. V1.0F1 does not call external APIs. V1.0F1 does not add real Serenity corpus entries. V1.0F1 does not extract real method claims. V1.0F1 does not execute real TOC calibration. V1.0F1 does not generate a real investment research report. V1.0F1 only defines the manual replay packet template.

This document is not a source packet, a replay result, an example, a company analysis, or authorization to begin collecting material.

## 2. Relationship to V1.0A–V1.0E

The replay packet depends on every upstream boundary:

- V1.0A defines authorized intake.
- V1.0B defines source records, corpus entries, and distillation queue items.
- V1.0C defines the method claim extraction protocol.
- V1.0D defines the TOC calibration matrix.
- V1.0E defines the research report template.
- V1.0F1 defines how a future manually authorized replay packet should be prepared.
- V1.0F1 cannot bypass any upstream phase.
- A replay packet template does not authorize real source collection or real report generation.

Every future replay object must preserve a traceable chain from bounded source references through source records, corpus entries, method claims, calibration rows, and report sections. Packet completeness does not establish source truth, methodology completeness, company value, or investment merit.

## 3. Replay objective

The future first manual case replay is intended to:

1. test whether the V1.0A–V1.0E stages connect end to end;
2. verify traceability across `source_record → corpus_entry → method_claim_candidate → toc_calibration_matrix_row → report section`;
3. verify that false-equivalence guardrails remain effective;
4. verify that the non-investment-advice boundary remains effective;
5. test whether the workflow can produce an evidence-bounded research hypothesis;
6. not validate real investment returns;
7. not validate a real company's investment value;
8. not validate the completeness or official status of Serenity's methodology.

The replay evaluates workflow integrity, provenance preservation, review discipline, and boundary enforcement. It does not evaluate trading performance or prove a theory.

## 4. Replay packet object schema

The future replay object is `manual_case_replay_packet` with these fields:

| Field | Definition |
|---|---|
| `replay_packet_id` | Stable unique identifier for the replay packet. |
| `replay_packet_version` | Version identifier incremented when scope, objects, review, or disposition changes. |
| `replay_title` | Neutral replay title that does not imply a conclusion or recommendation. |
| `replay_scope` | Included and excluded sources, method questions, systems, report sections, and execution boundaries. |
| `industry_or_theme` | Authorized industry chain or abstract theme; no real company is required. |
| `geography_or_market` | Relevant geographic, regulatory, or market scope, or `not_applicable`. |
| `time_horizon` | Time boundary used for the replay hypothesis and monitoring design. |
| `source_packet_ids` | Manual source packet identifiers admitted to replay review. |
| `source_record_ids` | Reviewed source records created from accepted source packets. |
| `corpus_entry_ids` | Reviewed normalized corpus entries. |
| `distillation_queue_ids` | Eligible distillation queue items. |
| `method_claim_ids` | Reviewed provisional method claim identifiers. |
| `calibration_row_ids` | Reviewed TOC calibration row identifiers. |
| `report_id` | Report-template replay object identifier. |
| `replay_status` | One controlled state defined below. |
| `reviewer` | Human reviewer or authorized review role. |
| `created_at` | Replay-packet creation timestamp. |
| `updated_at` | Most recent material revision timestamp. |
| `limitations` | Source, provenance, excerpt, method, calibration, report, and scope limitations. |
| `next_action` | Required intake, review, preparation, replay, remediation, acceptance, deferral, or rejection step. |

### Replay status

| Status | Meaning |
|---|---|
| `draft_packet` | Initial packet structure; required inputs and boundaries may be incomplete. |
| `source_packet_ready` | Manual source references and authorization metadata are ready for intake review. |
| `source_records_reviewed` | Source records have passed the replay-specific source checklist. |
| `corpus_entries_prepared` | Normalized corpus entries have been reviewed and prepared. |
| `method_claims_prepared` | Provisional method claims have been reviewed and prepared. |
| `calibration_rows_prepared` | Calibration rows have been reviewed and prepared without asserting equivalence. |
| `report_template_replayed` | The reviewed objects have been placed through the report template without creating an investment recommendation. |
| `replay_reviewed` | End-to-end traceability, boundaries, pass/fail checks, limitations, and remediation have been reviewed. |
| `accepted_as_replay_evidence` | The packet is accepted as evidence that the bounded workflow replay was executed under its stated conditions. |
| `rejected` | The replay is invalid, misleading, out of scope, or failed without adequate remediation. |
| `deferred` | The replay is paused because sources, authorization, review, evidence, or sequencing is insufficient. |

`accepted_as_replay_evidence` means process-replay evidence only. It does not establish a real investment conclusion, validate a real company, confirm investment performance, prove method completeness, or imply Serenity endorsement.

## 5. Manual source packet schema

The future source-input object is `manual_source_packet` with these fields:

| Field | Definition |
|---|---|
| `source_packet_id` | Stable unique identifier for the manual source packet. |
| `source_packet_version` | Version identifier incremented when scope, references, authorization, or review changes. |
| `packet_scope` | Included and excluded source references and intended replay use. |
| `source_locator_list` | Reviewable public URLs or other authorized locators. |
| `source_type_list` | Controlled source-type classifications corresponding to each locator. |
| `acquisition_method` | Manual, allowed method used to provide the references. |
| `permission_basis` | Public access, user ownership, license, explicit permission, or another lawful basis. |
| `excerpt_boundary_note` | Statement of bounded excerpt limits and why each excerpt is necessary. |
| `attribution_note` | Authorship, origin, quotation, secondary framing, and interpretation separation. |
| `translation_note` | Translation method and uncertainty, or `not_applicable`. |
| `user_provided_context` | User-owned context clearly separated from source expression. |
| `disallowed_use` | Explicit prohibitions, including no investment advice and no unauthorized reuse. |
| `reviewer_note` | Intake findings, ambiguity, missing checks, and disposition rationale. |
| `status` | One source-packet state defined below. |

### Manual source packet status

| Status | Meaning |
|---|---|
| `draft` | References and authorization metadata are incomplete or not yet reviewed. |
| `intake_review` | The packet is under V1.0A channel, provenance, permission, attribution, and excerpt review. |
| `accepted_for_replay` | The bounded references may be used in the separately authorized replay. |
| `rejected` | A source, method, permission basis, or intended use fails the intake boundary. |
| `quarantined` | Provenance, permission, integrity, attribution, or access status is unresolved. |

A source packet may contain only manually provided, bounded, authorized source references. It must not contain bulk-copied source text, secrets, complete third-party archives, access-restricted material, or unauthorized scraped content. Community interpretation must not be classified as Serenity original public expression.

## 6. Source record checklist

Before a source record enters the replay:

1. a source locator exists;
2. `source_type` is known;
3. the acquisition method is allowed;
4. `permission_basis` is recorded;
5. the excerpt is bounded;
6. attribution is clear;
7. assistant inference is separated;
8. source limitations are recorded;
9. `disallowed_use` includes no investment advice;
10. a reviewer note exists.

The source record must also have passed the V1.0A gate. A missing or ambiguous requirement prevents acceptance and requires rejection, quarantine, or further intake review.

## 7. Corpus entry checklist

Before a corpus entry advances in the replay:

1. its source record has `status = accepted`;
2. `normalized_claim` is bounded;
3. `original_excerpt_reference` exists;
4. the paraphrase does not strengthen the source claim;
5. `source_type` is preserved;
6. `chokepoint_method_dimension` is mapped;
7. `toc_calibration_relevance` is tagged;
8. limitations are recorded;
9. `counterevidence_needed` is recorded;
10. status can become `distillation_ready` only after review.

The entry must remain a normalized, attributed research unit rather than a raw full-text archive. Review must preserve ambiguity and source-type separation.

## 8. Method claim candidate checklist

Before a method claim candidate advances in the replay:

1. every linked corpus entry has `status = distillation_ready`;
2. `claim_statement` is bounded;
3. `claim_type` is assigned;
4. `source_support` is recorded;
5. `source_limitations` are recorded;
6. `disagreement_or_ambiguity` is recorded;
7. `counterexamples_needed` is recorded;
8. `toc_calibration_relevance` is recorded;
9. confidence is assigned;
10. `review_status` can become `calibration_ready` only after review.

The candidate must remain provisional and source-grounded. It must not be labeled as an official Serenity statement or a final universal method rule.

## 9. TOC calibration row checklist

Before a calibration row advances in the replay:

1. the `method_claim_candidate` has `review_status = calibration_ready`;
2. a TOC concept candidate is selected;
3. `possible_toc_overlap` is recorded;
4. `possible_toc_difference` is recorded;
5. `calibration_question` is recorded;
6. `toc_correction_or_guardrail` is recorded;
7. `false_equivalence_risk` is recorded;
8. `investment_research_implication` is recorded;
9. `operating_system_implication` is recorded or marked `not_applicable`;
10. `review_status` can become `report_ready` only after review.

The row must preserve a non-equivalence warning. TOC may improve reasoning discipline but must not overwrite source meaning or substitute for Chokepoint Theory.

## 10. Report template replay checklist

The report-template replay must verify that:

1. the report uses only `report_ready` calibration rows;
2. the source chain is traceable;
3. the evidence table includes support and counterevidence;
4. the candidate exposure map does not recommend;
5. value-capture logic does not promise profit;
6. false-equivalence checks are visible;
7. monitoring indicators are hypotheses, not trading signals;
8. invalidation conditions are explicit;
9. confidence is report-hypothesis confidence;
10. the non-investment-advice disclaimer is present.

Missing checklist items block replay acceptance. A report-template replay tests structure and boundaries only; it does not become a real report or authorize publication.

## 11. Replay pass/fail criteria

### Pass criteria

A future replay passes only when:

- files and objects remain traceable;
- the source boundary is preserved;
- no unauthorized source is used;
- no raw bulk source is copied;
- no assistant inference is mislabeled as source;
- no community interpretation is mislabeled as Serenity original method;
- Chokepoint Theory is not treated as equivalent to TOC;
- no exposure map is turned into a recommendation;
- no report section becomes investment advice;
- limitations and invalidation conditions remain visible.

All pass criteria must be supported by reviewer notes or object links. Silence or missing evidence does not count as a pass.

### Fail criteria

A future replay fails if any of the following occurs:

- missing source locator;
- missing `source_type`;
- unclear attribution;
- unbounded excerpt;
- disallowed acquisition method;
- source-chain break;
- method claim overstates its source;
- TOC calibration overwrites source meaning;
- false-equivalence risk is hidden;
- a real company conclusion is generated without separate authorization;
- a buy/sell instruction, target price, position size, or return promise appears.

A failed replay must record the failing object, affected downstream objects, reviewer, remediation requirement, and final disposition. It must not be relabeled as accepted by deleting the failure evidence.

## 12. Manual replay output boundary

V1.0F1 output is limited to the packet template defined in this document.

It must not output:

- a real source packet;
- real Serenity excerpts;
- real corpus entries;
- real method claims;
- real TOC calibration rows;
- a real investment research report;
- real company analysis;
- real company conclusions;
- buy/sell instructions;
- target prices;
- position sizing;
- return promises;
- claims of Serenity endorsement, authorization, approval, or review;
- claims that the method is complete.

It also must not create corpus or data directories, machine-readable replay objects, examples, scraper or API integration, or validator logic in this phase.

## 13. Future PR split

- **V1.0F1: Manual Case Replay Packet Template document** — this pull request.
- **V1.0F2: Optional machine-readable replay packet schema, no data** — define structure without real replay objects.
- **V1.0F3: Validator light checks for replay packet schema** — add bounded structural checks without executing a replay.
- **V1.0F4: First authorized manual source packet, only if the user provides bounded authorized sources** — create a source packet under separate explicit authorization.
- **V1.0F5: First manual replay output, only after the source packet is reviewed** — execute and review the first replay under separate explicit authorization.

Each later phase requires separate authorization and scope review. V1.0F1 does not pre-authorize source collection, source import, corpus data, method extraction, calibration, company analysis, report generation, publication, or investment outputs.

## 14. Final boundary note

This packet template defines future manual case replay preparation only. It performs no X scraping, uses no twscrape, accesses no secrets, calls no external APIs, imports no real Serenity original text, creates no corpus data, extracts no real method claims, performs no real TOC calibration, produces no real company conclusions, generates no real investment research report, and provides no investment advice.
