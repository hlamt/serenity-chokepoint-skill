# Source Acquisition Gate v1.0A — Authorized Corpus Intake Boundary

## 1. Purpose

This document defines the compliance boundary through which Serenity Chokepoint Theory original public source material may enter a future corpus. It replaces a narrow “no X scraping” rule with a broader requirement: source acquisition must be authorized, traceable, minimal, attributable, and suitable for review before any material is admitted.

V1.0A does not collect source data. V1.0A does not scrape X. V1.0A does not use twscrape. V1.0A does not call external APIs. V1.0A only defines the intake gate for future authorized corpus construction.

This gate does not itself create a corpus, perform methodology distillation, calibrate the methodology against TOC, generate a research report, or authorize conclusions about real companies.

## 2. Why this gate is required

A genuine Chokepoint Theory methodology cannot be distilled without a clearly bounded body of Serenity's original public expression. TOC calibration also requires a clear object of calibration. The object of calibration is Serenity's publicly expressed Chokepoint Theory, represented by traceable and correctly classified source records.

A vague “Serenity-style” framework is insufficient because it can silently mix original expression, secondary reporting, community interpretation, user notes, and assistant inference. That mixture would make it impossible to determine which concepts came from Serenity, which were introduced by others, and which were created during analysis.

Future methodology distillation must therefore be grounded in traceable source records. The intake gate protects provenance, attribution, quotation limits, source-type separation, and the raw-source boundary before any record reaches the distillation queue.

## 3. Allowed source channels

The following channels may be considered in a future, separately authorized acquisition phase. Their inclusion here defines eligibility only; V1.0A does not collect from them.

1. **Manually provided public post URLs**: individual URLs supplied for review, provided the content is publicly accessible and the locator can be recorded.
2. **User-provided short excerpts with source locator**: bounded excerpts supplied by the user together with a URL, publication reference, or other traceable locator.
3. **Public secondary coverage that quotes or analyzes Serenity**: reporting, interviews, articles, or other public coverage, with quoted material and the secondary author's analysis kept distinct.
4. **User-owned research notes, clearly labeled as secondary notes**: notes the user owns or is authorized to use, treated as secondary material rather than Serenity original expression.
5. **Licensed or permissioned exports, if the user has lawful access**: exports whose license or permission basis allows the intended review and storage, subject to data minimization and retention limits.
6. **Official APIs, only if explicitly authorized in a future implementation phase**: use requires separate authorization covering the API, credentials, permitted fields, rate limits, storage, retention, and compliance obligations.
7. **Public webpages that are accessible without bypassing access controls**: pages available through ordinary public access, without defeating authentication, paywalls, technical restrictions, or platform controls.

Every future source candidate must still pass the provenance, permission, excerpt, classification, and readiness checks below. Public availability alone does not authorize bulk collection or unrestricted copying.

## 4. Disallowed source channels

The following channels and methods are prohibited:

1. twscrape;
2. cookie-based scraping;
3. session-token scraping;
4. browser automation used to bypass login walls;
5. scraping behind authentication without permission;
6. bulk copying of X timelines;
7. storing full third-party post archives;
8. using leaked, private, deleted, or access-restricted materials;
9. using secrets, API keys, credentials, cookies, or tokens discovered in local files;
10. de-anonymization attempts;
11. claiming Serenity endorsement, authorization, approval, review, or official status.

The gate also prohibits bypassing rate limits, platform restrictions, robots controls, paywalls, or other access controls. It does not authorize automated collection merely because a source can be viewed manually.

## 5. Source type taxonomy

Each source record must use one source type. If a source contains more than one type, create separately bounded records or clearly separated fields rather than blending them.

| Source type | Allowed use | Disallowed use | May enter methodology distillation? | May support research hypotheses? | May support real company conclusions? |
|---|---|---|---|---|---|
| **Serenity original public expression** | Identify original terminology, reasoning patterns, method steps, boundaries, and examples with clear attribution. | Inferring private intent, current views, portfolio positions, endorsement, or claims stronger than the source. | **Yes**, when provenance and excerpt controls pass. | **Yes**, as methodology context, but not as sufficient industry or company evidence. | **No**, not by itself. |
| **Serenity quoted in secondary coverage** | Use a short, clearly attributed quotation when the secondary source provides a traceable context and the quotation boundary is visible. | Treating the secondary author's framing as Serenity's words or assuming the quotation is complete. | **Conditionally**; only the carefully attributed quoted portion may directly support distillation. | **Yes**, with limitations and verification needs recorded. | **No**, not by itself. |
| **Public secondary analysis** | Identify interpretations, comparisons, criticism, and questions for later testing. | Presenting the analysis as Serenity's original method. | **No** as direct method evidence; it may accompany the queue as context. | **Yes**, as a secondary hypothesis source. | **No**, not by itself. |
| **Community interpretation** | Inspire questions, terminology checks, and possible counterinterpretations. | Treating community retellings, translations, or summaries as Serenity's original expression. | **No** as direct method evidence. | **Yes**, only as a clearly labeled prompt for investigation. | **No**. |
| **User-provided research note** | Preserve user-owned observations, candidate mappings, and research questions with ownership and verification status labeled. | Treating the note as verified primary evidence or Serenity's view. | **No** as direct method evidence unless it embeds a separately recorded, traceable primary excerpt. | **Yes**, as a secondary note. | **No**, not without independent company and industry evidence. |
| **Assistant inference** | State analytical hypotheses, proposed method dimensions, ambiguities, counterarguments, and missing checks. | Labeling or implying the inference is Serenity's view, source text, or official method. | **No** as source evidence; it must remain separate from source-derived material. | **Yes**, as an explicitly labeled hypothesis. | **No**, not by itself. |
| **Industry evidence** | Test supply-chain structure, capacity, substitution, lead times, dependencies, and throughput effects. | Using industry evidence to rewrite or attribute Serenity's methodology. | **No** as direct evidence of Serenity's method. | **Yes**, subject to evidence quality and provenance. | **Conditionally**, only in a separately authorized research workflow with corroboration and limitations. |
| **Company evidence** | Evaluate company-specific disclosures, capabilities, dependencies, risks, and contradictions. | Treating marketing claims or a single disclosure as conclusive; using it to define Serenity's method. | **No**. | **Yes**, subject to evidence quality and corroboration. | **Conditionally**, only in a separately authorized research workflow; never from one source alone. |
| **Market evidence** | Observe prices, volumes, spreads, availability, and other market conditions relevant to a hypothesis. | Converting market evidence into methodology attribution, investment advice, trade instructions, or return promises. | **No**. | **Yes**, as time-bounded supporting or contradicting evidence. | **Conditionally**, only as part of a broader evidence chain in a separately authorized workflow. |

Default rules:

- Only Serenity original public expression and carefully attributed quoted secondary coverage may directly support methodology distillation.
- Community interpretation may inspire questions but must not be treated as Serenity's original method.
- Assistant inference must never be labeled as Serenity's view.
- No source category can support a real company conclusion on its own.

## 6. Source record schema

A future corpus source record must contain, at minimum, the following fields:

| Field | Requirement |
|---|---|
| `source_id` | Stable unique identifier for the record. |
| `source_type` | One taxonomy value from Section 5. |
| `author_or_origin` | Known author, publisher, organization, or user-provided origin. |
| `source_url_or_locator` | Public URL or another reviewable source locator. |
| `platform` | Publication platform, site, document type, or note system. |
| `published_at` | Publication date or `unknown`, without inventing precision. |
| `captured_at` | Date and time the bounded record was created. |
| `acquisition_method` | Manual URL review, user-provided excerpt, permissioned export, or another explicitly allowed method. |
| `permission_basis` | Public access, user ownership, license, explicit permission, future API authorization, or other lawful basis. |
| `excerpt` | Optional bounded quotation containing only what is necessary for review. |
| `excerpt_length_note` | Length and rationale showing that the excerpt is minimal. |
| `paraphrase` | Attributed summary that does not strengthen the source's claim. |
| `attribution_note` | How authorship, quotation, translation, and secondary framing are distinguished. |
| `topic_tags` | Controlled tags for retrieval and review. |
| `chokepoint_method_dimension` | Candidate method dimension, or `unmapped`. |
| `toc_calibration_relevance` | Possible TOC comparison point, difference, ambiguity, or `none identified`. |
| `confidence` | Confidence in provenance, classification, and interpretation, not confidence in an investment outcome. |
| `limitations` | Missing context, unavailable original, translation risk, date limits, ambiguity, or verification needs. |
| `allowed_use` | Explicit permitted uses for the record. |
| `disallowed_use` | Explicit prohibited uses for the record. |
| `hash_or_checksum_optional` | Optional integrity aid; it does not replace provenance or permission. |
| `reviewer_note` | Human review result, open questions, and disposition. |

V1.0A defines this schema only. It does not add a data file, corpus file, source record, real excerpt, or real Serenity source material.

## 7. Corpus intake workflow

A future authorized intake process must follow this sequence:

1. **Identify source candidate**: describe the candidate and why it may be relevant without copying it in bulk.
2. **Confirm allowed channel**: verify that the source and acquisition method are allowed and that no access control is bypassed.
3. **Record provenance**: capture the locator, origin, dates, acquisition method, and permission basis.
4. **Store only bounded excerpt or paraphrase**: prefer an attributed paraphrase; retain only the minimum quotation necessary for terminology or review.
5. **Label source type**: keep original expression, secondary coverage, community interpretation, user notes, and assistant inference separate.
6. **Map to possible Chokepoint Theory dimension**: assign a candidate dimension or mark it `unmapped`; do not force a fit.
7. **Mark TOC calibration relevance**: state the possible calibration question without assuming equivalence between Chokepoint Theory and TOC.
8. **Add limitations and missing checks**: record ambiguity, missing context, verification needs, and competing interpretations.
9. **Queue for methodology distillation**: queue only records that meet every readiness criterion in Section 8.
10. **Keep raw-source boundary intact**: do not turn the repository into a full-text archive or mix raw source, interpretation, and generated conclusions.

## 8. Distillation readiness criteria

Before a source record enters the distillation queue, all of the following must be true:

1. a source locator exists;
2. the source type is labeled;
3. the acquisition method is allowed;
4. the excerpt is bounded;
5. attribution is clear;
6. assistant inference is separated;
7. a possible method dimension is tagged or explicitly marked `unmapped`;
8. TOC relevance is noted, including `none identified` when appropriate;
9. limitations are recorded;
10. no investment conclusion is generated from the source alone.

A record that fails any criterion remains outside the distillation queue. It may be rejected, returned for clarification, or retained only as an unverified lead if a future authorized schema provides such a status.

## 9. Relationship to V1.0 roadmap

The planned sequence is:

- **V1.0B Serenity Corpus Schema**: define the structured corpus representation and validation rules.
- **V1.0C Chokepoint Theory Distillation Protocol**: define how eligible source records are converted into method claims while preserving attribution and uncertainty.
- **V1.0D TOC Calibration Matrix**: compare distilled Chokepoint Theory dimensions with TOC concepts, overlaps, differences, and non-equivalences.
- **V1.0E TOC-Calibrated Chokepoint Research Report Template**: define a research output that uses the calibrated method and maintains evidence and non-investment-advice boundaries.
- **V1.0F First Manual Case Replay**: manually replay the complete workflow under explicit scope and source controls.

V1.0A is the gate. It is not a corpus, not methodology distillation, and not a report generator.

## 10. Final boundary note

This gate authorizes no scraping, no twscrape integration, no secret access, no automatic X collection, no bulk copying of third-party text, no real company conclusions, and no investment advice. It only defines the authorized intake boundary for future corpus construction.
