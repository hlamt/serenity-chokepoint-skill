# Serenity Corpus Schema v1.0B — Source Records, Corpus Entries, and Distillation Queue

## 1. Purpose

This document defines the structure and state boundaries for a future Serenity Chokepoint Theory corpus. It specifies how authorized source records may be represented, normalized into corpus entries, reviewed, and prepared as distillation queue items without confusing source material, interpretation, methodology claims, or later research outputs.

V1.0B does not collect source data. V1.0B does not scrape X. V1.0B does not use twscrape. V1.0B does not call external APIs. V1.0B does not add real Serenity corpus entries. V1.0B only defines schemas and state boundaries for future authorized corpus construction.

This document is not corpus data, methodology distillation, TOC calibration, or report generation.

## 2. Relationship to V1.0A Source Acquisition Gate

V1.0A and V1.0B perform different controls:

- V1.0A defines what may enter.
- V1.0B defines how eligible records are represented.
- A source may enter this schema only after passing the V1.0A gate.
- Schema compliance does not make a source true, complete, or sufficient for methodology distillation.

The [V1.0A Source Acquisition Gate](source-acquisition-gate.md) remains authoritative for allowed and disallowed acquisition channels, provenance requirements, excerpt boundaries, and intake readiness. V1.0B begins only after that gate. It does not weaken, bypass, or retroactively authorize any acquisition method.

## 3. Corpus design principles

Future implementations must preserve these principles:

1. **Authorized only**: every represented source must have passed the V1.0A acquisition gate.
2. **Traceable provenance**: every source-derived object must retain a reviewable chain back to its source locator and permission basis.
3. **Minimal excerpt**: store only the bounded quotation needed for terminology, interpretation, or review.
4. **Attribution preserved**: authorship, origin, quotation boundaries, translation, and secondary framing must remain visible.
5. **Paraphrase preferred**: use attributed paraphrase when it preserves meaning and avoids unnecessary copying.
6. **Source type separated**: do not merge original expression, secondary coverage, community interpretation, user notes, or industry evidence into one unlabeled voice.
7. **Assistant inference separated**: generated hypotheses and interpretations must never be represented as source text or Serenity's view.
8. **No source alone supports a real company conclusion**: company conclusions require a separately authorized research workflow and a broader evidence chain.
9. **Distillation requires review**: normalization is not methodology validation; human review is required before an entry becomes distillation-ready.
10. **TOC calibration requires explicit relevance tagging**: any proposed TOC relationship must be labeled as a calibration question, not assumed equivalence.

## 4. Directory proposal

The following is a future directory proposal only:

```text
corpus/
  source-records/
  corpus-entries/
  distillation-queue/
  review-notes/
  rejected/
```

V1.0B does not create these directories. Any future directory creation must occur in a separate, explicitly scoped pull request.

- `corpus/source-records/` would store metadata and bounded excerpts only.
- `corpus/corpus-entries/` would store normalized, attributed corpus units only.
- `corpus/distillation-queue/` would store reviewed tasks awaiting methodology distillation.
- `corpus/review-notes/` would store authorized review dispositions, questions, and audit notes without unnecessary source copying.
- `corpus/rejected/` would record rejected or quarantined source metadata and the reason for disposition, subject to the same minimization boundary.

No proposed directory may store bulk X timelines, complete third-party archives, cookies, sessions, API keys, tokens, credentials, secrets, or access-restricted material.

## 5. Object model overview

The corpus design has three object layers:

1. `source_record`
2. `corpus_entry`
3. `distillation_queue_item`

Their intended progression is:

```text
source_record
→ corpus_entry
→ distillation_queue_item
→ future methodology distillation
→ future TOC calibration matrix
→ future research report template
```

- A `source_record` is the registration record created after a source passes the intake gate. It preserves provenance, access, permission, excerpt, attribution, and review status.
- A `corpus_entry` is a normalized corpus unit derived from one accepted source record. It captures a bounded claim or concept without becoming a full-text archive.
- A `distillation_queue_item` is a reviewed task that groups one or more eligible corpus entries around a methodology question.

None of these objects can independently generate a real company conclusion, investment advice, a buy/sell instruction, a target price, position-sizing advice, or a return promise.

## 6. Source record schema

A future `source_record` must contain the following fields:

| Field | Definition |
|---|---|
| `record_id` | Stable unique identifier for the source record. |
| `record_version` | Version identifier incremented when the record changes. |
| `source_type` | One controlled taxonomy value from Section 9. |
| `author_or_origin` | Known author, publisher, organization, or user-provided origin. |
| `source_url_or_locator` | Public URL or other reviewable locator; required for acceptance. |
| `platform` | Platform, publication, document type, or note system. |
| `published_at` | Publication date or `unknown`; do not invent precision. |
| `captured_at` | Date and time the bounded record was registered. |
| `acquisition_method` | Allowed method used to obtain the source candidate. |
| `permission_basis` | Public access, user ownership, license, explicit permission, or other authorized basis. |
| `collector` | Human or authorized process responsible for registration; not a credential or secret. |
| `original_language` | Language of the source expression, or `unknown`. |
| `excerpt` | Optional, minimal, bounded quotation required for review. |
| `excerpt_length_note` | Length and justification showing why the excerpt is appropriately bounded. |
| `paraphrase` | Attributed summary that does not strengthen the source claim. |
| `translation_note` | Translation method, uncertainty, and distinction from original wording when applicable. |
| `attribution_note` | How authorship, quotation, secondary framing, and interpretation are separated. |
| `provenance_confidence` | Confidence in origin and traceability, not confidence in an investment outcome. |
| `source_integrity_status` | Review state for authenticity, completeness, alteration risk, and context sufficiency. |
| `access_boundary` | Public-access and access-control conditions observed at intake. |
| `copyright_boundary` | Excerpt, paraphrase, license, retention, and reuse limitations. |
| `allowed_use` | Explicit uses permitted for the record. |
| `disallowed_use` | Explicit uses prohibited for the record. |
| `reviewer_note` | Review findings, unresolved questions, and disposition rationale. |
| `status` | One source-record status defined below. |

### Source record status

| Status | Meaning |
|---|---|
| `candidate` | Identified for possible intake but not yet reviewed against the V1.0A gate. |
| `intake_review` | Under active provenance, permission, classification, attribution, and excerpt review. |
| `accepted` | Passed the intake gate and may be normalized into a corpus entry. Acceptance does not validate every claim. |
| `rejected` | Fails an intake requirement or uses a prohibited source or acquisition method; it must not proceed. |
| `quarantined` | Segregated because provenance, permission, integrity, attribution, or access status is ambiguous and requires resolution. |

Valid forward progression is normally `candidate → intake_review → accepted`. A record may move from `candidate` or `intake_review` to `rejected` or `quarantined`. A quarantined record may return to `intake_review` only after the ambiguity is resolved and documented.

## 7. Corpus entry schema

A future `corpus_entry` must contain the following fields:

| Field | Definition |
|---|---|
| `entry_id` | Stable unique identifier for the normalized unit. |
| `source_record_id` | Identifier of the accepted source record from which the entry is derived. |
| `entry_version` | Version identifier incremented when normalization or review changes. |
| `source_type` | Copied controlled taxonomy value, consistent with the source record. |
| `normalized_claim` | Bounded statement of the source-supported concept without strengthening it. |
| `original_excerpt_reference` | Reference to the bounded excerpt in the source record, not duplicated full text. |
| `paraphrase` | Attributed, normalized paraphrase used for analysis. |
| `language` | Language of the normalized entry. |
| `topic_tags` | Controlled retrieval and review tags. |
| `chokepoint_method_dimension` | One or more candidate tags from Section 10, or `unmapped`. |
| `toc_calibration_relevance` | One or more relevance tags from Section 11, or `none_identified`. |
| `evidence_role` | Role such as direct method evidence, quoted method evidence, secondary context, question source, supporting evidence, or counterevidence. |
| `confidence` | Confidence in normalization and interpretation, with scope stated. |
| `limitations` | Missing context, ambiguity, translation risk, date constraints, and other weaknesses. |
| `counterevidence_needed` | Evidence or competing interpretation required to test the normalized claim. |
| `related_entries` | Identifiers for corroborating, contradicting, duplicate, or context-linked entries. |
| `reviewer` | Human reviewer or authorized review role. |
| `review_status` | Review result and any unresolved conditions. |
| `status` | One corpus-entry status defined below. |

### Corpus entry status

| Status | Meaning |
|---|---|
| `draft` | Initial normalized unit not yet checked for fidelity, attribution, and boundaries. |
| `normalized` | Structure and wording have been normalized, but review remains incomplete. |
| `reviewed` | A reviewer has checked provenance linkage, fidelity, source-type separation, tags, and limitations. |
| `distillation_ready` | Meets all review rules and may be referenced by a distillation queue item. |
| `retired` | No longer eligible for active use because it was superseded, duplicated, invalidated, or found unsuitable; rationale remains traceable. |

A corpus entry is not a raw-source or original-full-text archive. It is a normalized, bounded, attributed research unit. Normalization must preserve uncertainty and must not convert interpretation into source fact.

## 8. Distillation queue item schema

A future `distillation_queue_item` must contain the following fields:

| Field | Definition |
|---|---|
| `queue_id` | Stable unique identifier for the queue item. |
| `corpus_entry_ids` | One or more reviewed, distillation-ready corpus entry identifiers. |
| `queue_version` | Version identifier incremented when scope or review changes. |
| `distillation_question` | Specific question about Serenity's publicly expressed methodology. |
| `candidate_method_claim` | Provisional method claim to test; never treated as established merely because it is queued. |
| `chokepoint_method_dimension` | Candidate dimension or dimensions from Section 10. |
| `toc_calibration_question` | Explicit TOC comparison question, including possible difference or non-equivalence. |
| `source_support_summary` | Attributed summary of supporting and contradicting eligible entries. |
| `source_limitations` | Combined provenance, context, coverage, translation, and evidence limitations. |
| `disagreement_or_ambiguity` | Competing readings, unresolved wording, source conflicts, and missing checks. |
| `reviewer` | Human reviewer or authorized review role responsible for queue admission. |
| `priority` | Review priority based on methodological relevance and evidence readiness, not investment urgency. |
| `status` | One queue-item status defined below. |
| `next_action` | Required review, sourcing, extraction, calibration, deferral, or rejection step. |

### Distillation queue item status

| Status | Meaning |
|---|---|
| `queued` | Admitted to the methodology distillation backlog. |
| `in_review` | Sources, claim wording, disagreements, and boundaries are under review. |
| `extracted` | A provisional method claim has been extracted with attribution and limitations preserved. |
| `calibration_pending` | Ready for future TOC comparison but not yet calibrated. |
| `calibrated` | Future TOC calibration has recorded overlaps, differences, and boundaries; this status is unavailable in V1.0B itself. |
| `deferred` | Paused because evidence, context, review capacity, or sequencing is insufficient. |
| `rejected` | Unsuitable for methodology distillation because support, provenance, classification, or scope is inadequate. |

A distillation queue item prepares methodology distillation only. It does not generate an investment research report, a real company conclusion, or investment advice.

## 9. Source type taxonomy

The schema uses these `source_type` values:

- `serenity_original_public_expression`
- `serenity_quoted_secondary_coverage`
- `public_secondary_analysis`
- `community_interpretation`
- `user_provided_research_note`
- `assistant_inference`
- `industry_evidence`
- `company_evidence`
- `market_evidence`

Rules:

- Only `serenity_original_public_expression` and carefully attributed `serenity_quoted_secondary_coverage` may directly support methodology distillation.
- `community_interpretation` may generate questions but must not be treated as Serenity's original method.
- `assistant_inference` must never be labeled as Serenity's view.
- `industry_evidence`, `company_evidence`, and `market_evidence` support research hypotheses, not Serenity methodology distillation.
- `public_secondary_analysis` and `user_provided_research_note` may provide context or questions but cannot independently establish a Serenity method claim.

## 10. Chokepoint method dimension tags

Future corpus entries and queue items may use these candidate method dimension tags:

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

These are candidate indexing and review tags. Their presence does not mean Serenity's methodology has already been distilled, validated, ordered, or proven to contain each dimension. In particular, `position_sizing_or_conviction_boundary` may identify a boundary or discussion topic; it does not authorize position-sizing advice.

## 11. TOC calibration relevance tags

Future corpus entries and queue items may use these TOC calibration relevance tags:

- `system_boundary`
- `system_goal`
- `throughput_definition`
- `constraint_identification`
- `CCR_characteristics`
- `subordination_evidence`
- `elevation_path`
- `constraint_release`
- `constraint_migration`
- `local_bottleneck_vs_system_constraint`
- `value_capture_vs_throughput`
- `false_chokepoint_filter`

These tags record why an entry may be relevant to a future TOC calibration question. They do not automatically equate Chokepoint Theory with TOC, establish conceptual identity, or resolve differences between investment research concepts and system constraints.

## 12. Review and status rules

The following rules apply to all future implementations:

1. A record without a source locator cannot be accepted.
2. A record without `source_type` cannot be accepted.
3. A record using a disallowed acquisition method must be rejected or quarantined.
4. A record with unclear attribution must not enter distillation.
5. Assistant inference must be separated before review.
6. A corpus entry must have method dimension tagging before entering the distillation queue; `unmapped` is not sufficient for queue admission.
7. A distillation queue item must include source limitations and ambiguity.
8. No single source record can support a real company conclusion.
9. No queue item can produce investment advice.
10. Any ambiguous source must remain `candidate` or `quarantined`.

Additional state controls:

- Only an `accepted` source record may produce a corpus entry.
- Only a `distillation_ready` corpus entry may be included in `corpus_entry_ids`.
- Status changes must preserve reviewer identity, date, rationale, and prior version traceability.
- Rejected, quarantined, retired, deferred, and contradicted objects must not be silently deleted to improve apparent support.
- A status indicates workflow readiness, not truth, completeness, endorsement, or investment merit.

## 13. Validation boundary

V1.0B does not modify `scripts/validate_skill.py`. It defines a documentation-level schema only and creates no validator logic.

A future, separately scoped pull request may add lightweight checks such as:

- required file check for `docs/serenity-corpus-schema.md`;
- required keyword check for object models;
- future schema JSON validation;
- future status enum validation;
- future no-bulk-source-data check.

Any machine-readable validation must be introduced only after its schema files and directory scope are separately authorized. Passing future validation would establish structural compliance, not source truth, methodology validity, or suitability for real company conclusions.

## 14. Future PR split

- **V1.0B1: Serenity Corpus Schema document** — this pull request.
- **V1.0B2: Optional machine-readable schema files, no data** — define structural files without corpus entries.
- **V1.0B3: Validator light checks for schema files** — add bounded structural validation without collection capability.
- **V1.0C: Chokepoint Theory Distillation Protocol** — define reviewed methodology extraction.
- **V1.0D: TOC Calibration Matrix** — record overlaps, differences, calibration questions, and non-equivalence boundaries.
- **V1.0E: TOC-Calibrated Research Report Template** — define report structure with evidence and non-investment-advice controls.
- **V1.0F: First Manual Case Replay using manually provided, bounded, authorized source records** — exercise the workflow under explicit authorization and review.

Each phase requires its own scope review. V1.0B does not pre-authorize the files, data, automation, collection, or conclusions of any later phase.

## 15. Final boundary note

This schema defines future corpus structure only. It performs no X scraping, uses no twscrape, accesses no secrets, calls no external APIs, imports no real Serenity original text, creates no corpus data, produces no real company conclusions, and provides no investment advice.
