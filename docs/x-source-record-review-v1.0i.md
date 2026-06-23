# X Source Record Review — V1.0I

## 1. Purpose and boundary

This file reviews the X source leads assembled in V1.0H, V1.0H-B, and V1.0H-C and assigns a source-record-review disposition to every lead group.

This is Source Record Review, not Source Record Creation. A recommendation means only that a bounded proposal may be drafted in a later phase after the listed human checks are completed.

- No source is approved.
- No source record or corpus entry is created.
- No method claim is created or validated.
- No TOC calibration or runtime use is approved.
- No real-company conclusion or investment advice is generated.

## 2. Input set

| source_packet | input file | lead groups | URL references |
| --- | --- | ---: | ---: |
| V1.0H | `docs/x-source-lead-review-packet-v1.0h.md` | 4 | 4 |
| V1.0H-B | `docs/mcc0003-value-capture-source-lead-supplement-v1.0h-b.md` | 23 | 28 |
| V1.0H-C | `docs/invalidation-bear-case-risk-source-lead-supplement-v1.0h-c.md` | 13 | 13 |
| **Total** |  | **40** | **45** |

The AXTI URL `https://x.com/aleabitoreddit/status/2066823176785457323` appears in both V1.0H and V1.0H-C. It is one source with multiple review roles, so the input contains 44 unique URLs.

All URLs, visible dates, authors, excerpts, and context descriptions remain user-provided review inputs. This round performs no independent X verification.

## 3. Review method

Each lead is reviewed for:

1. stable locator and sufficiently clear attribution;
2. methodological signal separable from company-specific factual assertions;
3. need for thread, reply, article, date, or excerpt confirmation;
4. duplication or cross-reference relationships;
5. directness to supply-chain chokepoint, value-capture, or invalidation review; and
6. ability to preserve a `not_distilled` boundary in a later proposal.

Allowed dispositions:

- `recommend_source_record_proposal`
- `needs_more_human_review`
- `defer_as_cross_reference`
- `exclude_for_now`

Source roles are ordered as primary then secondary. `external_factual_claim` never authorizes factual reuse; it flags content that must remain separated and independently sourced.

Every review item inherits these prohibited uses:

- not investment advice
- not company conclusion
- not validated method claim
- not runtime rule
- not TOC calibration

## 4. Disposition summary

| disposition | count | meaning |
| --- | ---: | --- |
| `recommend_source_record_proposal` | 15 | Ready to propose as a bounded source record in a later creation phase, after required checks |
| `needs_more_human_review` | 18 | Useful but requires exact post, thread, date, excerpt, article, or context review |
| `defer_as_cross_reference` | 1 | Same URL reused across packets; review once and reference multiple dimensions |
| `exclude_for_now` | 6 | Do not advance at this stage |

| source_packet | reviewed lead groups | reviewed URLs | recommend | needs_review | cross_reference | exclude |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| V1.0H | 4 | 4 | 2 | 2 | 0 | 0 |
| V1.0H-B | 23 | 28 | 8 | 12 | 0 | 3 |
| V1.0H-C | 13 | 13 | 5 | 4 | 1 | 3 |
| **Total** | **40** | **45** | **15** | **18** | **1** | **6** |

## 5. V1.0H source-record review

```yaml
review_id: V10I-REVIEW-0001
source_packet: V1.0H
lead_id: XLEAD-AXTI-001
post_url: https://x.com/aleabitoreddit/status/2066823176785457323
author_or_origin: "@aleabitoreddit"
visible_date: "Jun 16; year not visible in V1.0H screenshot"
source_basis: "user-provided stable URL plus screenshot-visible text"
related_mcc: [MCC-0002, MCC-0005]
primary_source_role: original_method_expression
secondary_source_roles: [physical_supply_chain_mapping_signal, source_governance_signal, risk_or_invalidation_signal, external_factual_claim]
review_disposition: recommend_source_record_proposal
review_rationale: "The research-process language is methodologically meaningful and can be separated from AXTI, Reuters, pricing, and market-share assertions. V1.0H-C adds a cross-reference, not independent recurrence."
bounded_source_record_potential: method_expression_source_record_candidate
required_before_source_record:
  - confirm exact post body and full date
  - confirm thread context
  - extract a bounded excerpt
  - separate external factual claims from method expression
risk_or_limitation:
  - position and personal-defense language
  - external-source references remain unreviewed
cross_reference:
  - V10I-REVIEW-0028
not_allowed_uses: [not investment advice, not company conclusion, not validated method claim, not runtime rule, not TOC calibration]
```

```yaml
review_id: V10I-REVIEW-0002
source_packet: V1.0H
lead_id: XLEAD-AMD-CW-LASER-001
post_url: https://x.com/aleabitoreddit/status/2067206734427697196
author_or_origin: "@aleabitoreddit"
visible_date: "Jun 17; year not visible in screenshot"
source_basis: "user-provided stable URL plus screenshot-visible text"
related_mcc: [MCC-0001, MCC-0002, MCC-0004]
primary_source_role: physical_supply_chain_mapping_signal
secondary_source_roles: [capacity_or_constraint_release_signal, original_method_expression, external_factual_claim]
review_disposition: recommend_source_record_proposal
review_rationale: "The post contains a bounded multi-party capacity-locking and procurement structure that can be retained as original mapping expression while company claims remain excluded."
bounded_source_record_potential: physical_mapping_source_record_candidate
required_before_source_record:
  - confirm exact post body, year, and thread context
  - extract a bounded excerpt
  - separate TrendForce and company assertions
risk_or_limitation:
  - inferential procurement and capacity statements
  - ticker and company-specific framing
cross_reference: []
not_allowed_uses: [not investment advice, not company conclusion, not validated method claim, not runtime rule, not TOC calibration]
```

```yaml
review_id: V10I-REVIEW-0003
source_packet: V1.0H
lead_id: XLEAD-EML-CW-LASER-001
post_url: https://x.com/aleabitoreddit/status/2068616131129270289
author_or_origin: "@aleabitoreddit"
visible_date: "Jun 21; year not visible in screenshot"
source_basis: "user-provided stable URL plus screenshot-visible reply text"
related_mcc: [MCC-0001, MCC-0002, MCC-0004]
primary_source_role: physical_supply_chain_mapping_signal
secondary_source_roles: [capacity_or_constraint_release_signal, original_method_expression, external_factual_claim]
review_disposition: needs_more_human_review
review_rationale: "The multi-layer bottleneck signal is strong, but the post is a reply and its parent context is essential to attribution and bounded interpretation."
bounded_source_record_potential: physical_mapping_source_record_candidate
required_before_source_record:
  - confirm parent post and reply context
  - confirm exact post body and full date
  - separate earnings-transcript and company claims
risk_or_limitation:
  - probabilistic shortage and supplier claims
  - unavailable context could change meaning
cross_reference: []
not_allowed_uses: [not investment advice, not company conclusion, not validated method claim, not runtime rule, not TOC calibration]
```

```yaml
review_id: V10I-REVIEW-0004
source_packet: V1.0H
lead_id: XLEAD-FOOSUNG-WF6-001
post_url: https://x.com/aleabitoreddit/status/2065736884752703865
author_or_origin: "@aleabitoreddit"
visible_date: "Jun 13; year not visible in screenshot"
source_basis: "user-provided stable URL plus screenshot-visible text"
related_mcc: [MCC-0001, MCC-0002]
primary_source_role: physical_supply_chain_mapping_signal
secondary_source_roles: [risk_or_invalidation_signal, external_factual_claim]
review_disposition: needs_more_human_review
review_rationale: "Policy-to-material tracing is relevant, but beneficiary language and unverified supply-share claims dominate enough that exact context and excerpt separation are required."
bounded_source_record_potential: physical_mapping_source_record_candidate
required_before_source_record:
  - confirm exact post body, full date, and context
  - isolate policy-to-material mapping language
  - independently source export-control and supply-share assertions
risk_or_limitation:
  - promotional beneficiary framing
  - high factual-claim density
cross_reference: []
not_allowed_uses: [not investment advice, not company conclusion, not validated method claim, not runtime rule, not TOC calibration]
```

## 6. V1.0H-B source-record review

```yaml
review_id: V10I-REVIEW-0005
source_packet: V1.0H-B
lead_id: XLEAD-LEADERDRIVE-VALUE-CAPTURE-001
post_url: https://x.com/aleabitoreddit/status/2063851425462173726
author_or_origin: "@aleabitoreddit"
visible_date: "Jun 8 2026, user-provided"
source_basis: "user-provided stable URL plus screenshot-visible text"
related_mcc: [MCC-0003, MCC-0005]
primary_source_role: value_capture_signal
secondary_source_roles: [original_method_expression, external_factual_claim, context_only]
review_disposition: needs_more_human_review
review_rationale: "High-value versus low-margin layer differentiation is promising, but the third-party context URL and company claims require careful separation."
bounded_source_record_potential: value_capture_source_record_candidate
required_before_source_record:
  - confirm exact post body and context
  - keep third-party post context-only
  - separate business facts from value-layer expression
risk_or_limitation:
  - related context is not Serenity original expression
  - company-specific valuation implications
cross_reference: []
not_allowed_uses: [not investment advice, not company conclusion, not validated method claim, not runtime rule, not TOC calibration]
```

```yaml
review_id: V10I-REVIEW-0006
source_packet: V1.0H-B
lead_id: XLEAD-SIVE-ARTICLE-CPO-LASER-CHOKEPOINT-001
post_url: https://x.com/aleabitoreddit/article/2056691097594925522
author_or_origin: "@aleabitoreddit"
visible_date: "May 19 2026, user-provided"
source_basis: "user-provided stable article URL plus screenshot-visible signals"
related_mcc: [MCC-0001, MCC-0002, MCC-0003]
primary_source_role: physical_supply_chain_mapping_signal
secondary_source_roles: [value_capture_signal, original_method_expression, external_factual_claim]
review_disposition: needs_more_human_review
review_rationale: "The article may be rich source material, but a long article cannot proceed without accessible-body confirmation and bounded excerpt extraction."
bounded_source_record_potential: physical_mapping_source_record_candidate
required_before_source_record:
  - identify whether article body is accessible
  - review full article context
  - extract one or more bounded excerpts
  - separate factual claims from method expression
risk_or_limitation:
  - long-form source
  - high company and market claim density
cross_reference: []
not_allowed_uses: [not investment advice, not company conclusion, not validated method claim, not runtime rule, not TOC calibration]
```

```yaml
review_id: V10I-REVIEW-0007
source_packet: V1.0H-B
lead_id: XLEAD-SIVE-LPK-VALUE-CHAIN-001
post_url: https://x.com/aleabitoreddit/status/2055822766600016238
author_or_origin: "@aleabitoreddit"
visible_date: "May 17 2026, user-provided"
source_basis: "user-provided stable URL plus screenshot-visible text"
related_mcc: [MCC-0001, MCC-0002, MCC-0003, MCC-0005]
primary_source_role: original_method_expression
secondary_source_roles: [physical_supply_chain_mapping_signal, value_capture_signal, source_governance_signal, external_factual_claim]
review_disposition: recommend_source_record_proposal
review_rationale: "Technical depth, supply-chain mapping, margin expansion, integration, and substrate-level analysis form a reusable expression that can be bounded away from ticker and TAM claims."
bounded_source_record_potential: method_expression_source_record_candidate
required_before_source_record:
  - confirm exact post body and context
  - extract bounded method-language excerpt
  - separate TAM and company claims
risk_or_limitation:
  - portfolio and ticker framing
  - unverified market-size and margin assertions
cross_reference: []
not_allowed_uses: [not investment advice, not company conclusion, not validated method claim, not runtime rule, not TOC calibration]
```

```yaml
review_id: V10I-REVIEW-0008
source_packet: V1.0H-B
lead_id: XLEAD-PHISON-MEMORY-VALUE-CAPTURE-001
post_url: https://x.com/aleabitoreddit/status/2023323844346618010
author_or_origin: "@aleabitoreddit"
visible_date: "Feb 16 2026, screenshot visible"
source_basis: "user-provided stable URL plus screenshot-visible text"
related_mcc: [MCC-0003, MCC-0005]
primary_source_role: value_capture_signal
secondary_source_roles: [original_method_expression, shareholder_capture_signal, external_factual_claim]
review_disposition: recommend_source_record_proposal
review_rationale: "The toll-collector and control-point distinction is methodologically meaningful and can be retained without the long/short directives."
bounded_source_record_potential: value_capture_source_record_candidate
required_before_source_record:
  - confirm exact post body and date
  - remove trading-language dependence
  - separate sector and company claims
risk_or_limitation:
  - direct long/short-style source language
  - unverified bottleneck and value assertions
cross_reference: []
not_allowed_uses: [not investment advice, not company conclusion, not validated method claim, not runtime rule, not TOC calibration]
```

```yaml
review_id: V10I-REVIEW-0009
source_packet: V1.0H-B
lead_id: XLEAD-VPG-HUMANOID-VALUE-CAPTURE-001
post_url: https://x.com/aleabitoreddit/status/2013895541277762034
author_or_origin: "@aleabitoreddit"
visible_date: "Jan 21 2026, screenshot visible"
source_basis: "user-provided stable URL plus screenshot-visible text"
related_mcc: [MCC-0003, MCC-0005]
primary_source_role: value_capture_signal
secondary_source_roles: [shareholder_capture_signal, risk_or_invalidation_signal, external_factual_claim]
review_disposition: needs_more_human_review
review_rationale: "BoM-share and per-unit capture are useful, but scenario, customer, margin, and valuation claims are too intertwined for proposal without exact excerpt review."
bounded_source_record_potential: value_capture_source_record_candidate
required_before_source_record:
  - confirm exact post body and context
  - isolate reusable value-capture expression
  - independently source scenario inputs
risk_or_limitation:
  - scenario-heavy company analysis
  - position and valuation language
cross_reference: []
not_allowed_uses: [not investment advice, not company conclusion, not validated method claim, not runtime rule, not TOC calibration]
```

```yaml
review_id: V10I-REVIEW-0010
source_packet: V1.0H-B
lead_id: XLEAD-IREN-NBIS-DILUTION-001
post_url: https://x.com/aleabitoreddit/status/2069217783746060764
author_or_origin: "@aleabitoreddit"
visible_date: "relative 3h only; calendar date needs_human_review"
source_basis: "user-provided stable URL plus screenshot-visible text"
related_mcc: [MCC-0003, MCC-0005]
primary_source_role: shareholder_capture_signal
secondary_source_roles: [risk_or_invalidation_signal, external_factual_claim]
review_disposition: needs_more_human_review
review_rationale: "The dilution-versus-investor-outcome signal is relevant, but relative date, reply context, and inflammatory wording prevent immediate proposal."
bounded_source_record_potential: shareholder_capture_source_record_candidate
required_before_source_record:
  - confirm calendar date and reply context
  - confirm exact post body
  - extract non-inflammatory bounded excerpt
risk_or_limitation:
  - strong negative company language
  - incomplete date
cross_reference: []
not_allowed_uses: [not investment advice, not company conclusion, not validated method claim, not runtime rule, not TOC calibration]
```

```yaml
review_id: V10I-REVIEW-0011
source_packet: V1.0H-B
lead_id: XLEAD-CAMT-NAV-DILUTION-001
post_url: https://x.com/aleabitoreddit/status/2068180134667182470
author_or_origin: "@aleabitoreddit"
visible_date: "Jun 20 2026, user-provided"
source_basis: "user-provided stable URL plus screenshot-visible text"
related_mcc: [MCC-0003, MCC-0005]
primary_source_role: external_factual_claim
secondary_source_roles: [shareholder_capture_signal, source_governance_signal]
review_disposition: exclude_for_now
review_rationale: "Personal notes about NAV, ownership, governance, and ongoing research are company-specific and currently provide weaker reusable method signal than stronger financing leads."
bounded_source_record_potential: shareholder_capture_source_record_candidate
required_before_source_record:
  - no proposal in V1.0J
  - reconsider only if a clearer method excerpt is supplied
risk_or_limitation:
  - incomplete research status
  - ownership and governance facts unverified
cross_reference: []
not_allowed_uses: [not investment advice, not company conclusion, not validated method claim, not runtime rule, not TOC calibration]
```

```yaml
review_id: V10I-REVIEW-0012
source_packet: V1.0H-B
lead_id: XLEAD-AXTI-DILUTION-RISK-001
post_url: https://x.com/aleabitoreddit/status/2064714994403742179
author_or_origin: "@aleabitoreddit"
visible_date: "Jun 10 2026, user-provided"
source_basis: "user-provided stable URL plus screenshot-visible reply"
related_mcc: [MCC-0003, MCC-0005]
primary_source_role: shareholder_capture_signal
secondary_source_roles: [risk_or_invalidation_signal, external_factual_claim]
review_disposition: needs_more_human_review
review_rationale: "Dilution and float structure directly qualify shareholder capture, but the signal is a short reply whose meaning depends on parent context."
bounded_source_record_potential: shareholder_capture_source_record_candidate
required_before_source_record:
  - confirm parent and reply context
  - confirm exact post body
  - identify bounded language independent of position disclosure
risk_or_limitation:
  - short reply
  - position language
cross_reference: []
not_allowed_uses: [not investment advice, not company conclusion, not validated method claim, not runtime rule, not TOC calibration]
```

```yaml
review_id: V10I-REVIEW-0013
source_packet: V1.0H-B
lead_id: XLEAD-DILUTION-STRUCTURE-ACCRETIVE-PREDATORY-001
post_url: https://x.com/aleabitoreddit/status/2063573828928954442
author_or_origin: "@aleabitoreddit"
visible_date: "Jun 7 2026, user-provided"
source_basis: "user-provided stable URL plus screenshot-visible text"
related_mcc: [MCC-0003, MCC-0005]
primary_source_role: original_method_expression
secondary_source_roles: [shareholder_capture_signal, source_governance_signal, risk_or_invalidation_signal, external_factual_claim]
review_disposition: recommend_source_record_proposal
review_rationale: "The distinction between accretive and predatory dilution by structure and use of proceeds is a clear reusable judgment rule."
bounded_source_record_potential: shareholder_capture_source_record_candidate
required_before_source_record:
  - confirm exact post body and context
  - bound the structure and use-of-proceeds language
  - remove dependence on company examples
risk_or_limitation:
  - evaluative terminology requires attribution
  - examples remain unverified
cross_reference: []
not_allowed_uses: [not investment advice, not company conclusion, not validated method claim, not runtime rule, not TOC calibration]
```

```yaml
review_id: V10I-REVIEW-0014
source_packet: V1.0H-B
lead_id: XLEAD-TOXIC-FINANCING-FLOAT-DYNAMICS-001
post_url: https://x.com/aleabitoreddit/status/2063571485739106593
author_or_origin: "@aleabitoreddit"
visible_date: "Jun 7 2026, user-provided"
source_basis: "user-provided stable URL plus screenshot-visible text"
related_mcc: [MCC-0003, MCC-0005]
primary_source_role: shareholder_capture_signal
secondary_source_roles: [risk_or_invalidation_signal, original_method_expression, external_factual_claim]
review_disposition: recommend_source_record_proposal
review_rationale: "Financing, float, ATM overhang, debt, and dilution form a coherent shareholder-capture boundary that can be separated from negative company examples."
bounded_source_record_potential: shareholder_capture_source_record_candidate
required_before_source_record:
  - confirm exact post body
  - extract bounded mechanism language
  - exclude company-specific accusations
risk_or_limitation:
  - strong negative framing
  - factual financing claims require primary evidence
cross_reference: []
not_allowed_uses: [not investment advice, not company conclusion, not validated method claim, not runtime rule, not TOC calibration]
```

```yaml
review_id: V10I-REVIEW-0015
source_packet: V1.0H-B
lead_id: XLEAD-FINANCING-STRUCTURE-EQUITY-APPRECIATION-001
post_url: https://x.com/aleabitoreddit/status/2062119438552572283
author_or_origin: "@aleabitoreddit"
visible_date: "Jun 3 2026, user-provided"
source_basis: "user-provided stable URL plus screenshot-visible reply"
related_mcc: [MCC-0003, MCC-0005]
primary_source_role: shareholder_capture_signal
secondary_source_roles: [original_method_expression, source_governance_signal, external_factual_claim]
review_disposition: recommend_source_record_proposal
review_rationale: "The separation of debt, ATM issuance, ownership, and equity appreciation is directly relevant to common-shareholder capture."
bounded_source_record_potential: shareholder_capture_source_record_candidate
required_before_source_record:
  - confirm reply context and exact text
  - extract bounded financing-structure expression
  - separate company comparisons
risk_or_limitation:
  - reply context
  - external company structures unverified
cross_reference: []
not_allowed_uses: [not investment advice, not company conclusion, not validated method claim, not runtime rule, not TOC calibration]
```

```yaml
review_id: V10I-REVIEW-0016
source_packet: V1.0H-B
lead_id: XLEAD-CAPACITY-MONETIZATION-DILUTION-001
post_url: https://x.com/aleabitoreddit/status/2053928672202268993
author_or_origin: "@aleabitoreddit"
visible_date: "May 12 2026, user-provided"
source_basis: "user-provided stable URL plus screenshot-visible text"
related_mcc: [MCC-0003, MCC-0004, MCC-0005]
primary_source_role: shareholder_capture_signal
secondary_source_roles: [capacity_or_constraint_release_signal, risk_or_invalidation_signal, external_factual_claim]
review_disposition: recommend_source_record_proposal
review_rationale: "The post directly separates operating capacity and monetization from the financing structure through which shareholders may or may not capture value."
bounded_source_record_potential: shareholder_capture_source_record_candidate
required_before_source_record:
  - confirm exact post body and context
  - isolate capacity-versus-shareholder mechanism
  - remove company-specific conclusions
risk_or_limitation:
  - strong company claims
  - financing and capacity facts require independent sources
cross_reference: []
not_allowed_uses: [not investment advice, not company conclusion, not validated method claim, not runtime rule, not TOC calibration]
```

```yaml
review_id: V10I-REVIEW-0017
source_packet: V1.0H-B
lead_id: XLEAD-RETAIL-LIQUIDITY-EQUITY-APPRECIATION-001
post_url: https://x.com/aleabitoreddit/status/2050802865862836381
author_or_origin: "@aleabitoreddit"
visible_date: "May 3 2026, user-provided"
source_basis: "user-provided stable URL plus screenshot-visible text"
related_mcc: [MCC-0003, MCC-0005]
primary_source_role: shareholder_capture_signal
secondary_source_roles: [risk_or_invalidation_signal, external_factual_claim]
review_disposition: needs_more_human_review
review_rationale: "The distinction between shareholder appreciation and liquidity for issuance is useful, but inflammatory source wording and context need manual handling."
bounded_source_record_potential: shareholder_capture_source_record_candidate
required_before_source_record:
  - confirm exact body and thread context
  - extract neutral bounded mechanism
  - exclude inflammatory language
risk_or_limitation:
  - inflammatory wording
  - company financing claims unverified
cross_reference: []
not_allowed_uses: [not investment advice, not company conclusion, not validated method claim, not runtime rule, not TOC calibration]
```

```yaml
review_id: V10I-REVIEW-0018
source_packet: V1.0H-B
lead_id: XLEAD-IREN-NBIS-EQUITY-APPRECIATION-THREAD-001
post_urls:
  - https://x.com/aleabitoreddit/status/2038672101717274941
  - https://x.com/aleabitoreddit/status/2038163974437659019
  - https://x.com/aleabitoreddit/status/2037907569742856353
  - https://x.com/aleabitoreddit/status/2037896456179438049
  - https://x.com/aleabitoreddit/status/2031810360882446636
  - https://x.com/aleabitoreddit/status/2030702563902083150
cluster_requires_per_url_review: true
author_or_origin: "@aleabitoreddit"
visible_date: "Mar 9–31 2026, user-provided range"
source_basis: "user-provided stable URLs plus screenshot-visible thread cluster"
related_mcc: [MCC-0003, MCC-0005]
primary_source_role: shareholder_capture_signal
secondary_source_roles: [source_governance_signal, external_factual_claim]
review_disposition: needs_more_human_review
review_rationale: "Repeated financing and shareholder-capture language is promising, but six URLs cannot be flattened into one record or treated as six independent recurrences before individual review."
bounded_source_record_potential: shareholder_capture_source_record_candidate
required_before_source_record:
  - review each URL in cluster separately
  - confirm thread relationships and exact dates
  - deduplicate repeated wording
  - decide whether multiple records are justified
risk_or_limitation:
  - cluster aggregation
  - repeated company-specific and inflammatory language
cross_reference: []
not_allowed_uses: [not investment advice, not company conclusion, not validated method claim, not runtime rule, not TOC calibration]
```

```yaml
review_id: V10I-REVIEW-0019
source_packet: V1.0H-B
lead_id: XLEAD-EUROPEAN-PHOTONICS-PRICED-IN-001
post_url: https://x.com/aleabitoreddit/status/2066535221554733278
author_or_origin: "@aleabitoreddit"
visible_date: "Jun 15 2026, user-provided"
source_basis: "user-provided stable URL plus screenshot-visible text"
related_mcc: [MCC-0003, MCC-0004, MCC-0005]
primary_source_role: shareholder_capture_signal
secondary_source_roles: [capacity_or_constraint_release_signal, external_factual_claim]
review_disposition: needs_more_human_review
review_rationale: "Ramp, qualification, re-rating, and timing are relevant, but holdings and upside comparisons are too intertwined for immediate proposal."
bounded_source_record_potential: shareholder_capture_source_record_candidate
required_before_source_record:
  - confirm exact body and context
  - isolate timing and re-rating expression
  - remove holdings and upside language
risk_or_limitation:
  - personal holdings
  - company valuation comparisons
cross_reference: []
not_allowed_uses: [not investment advice, not company conclusion, not validated method claim, not runtime rule, not TOC calibration]
```

```yaml
review_id: V10I-REVIEW-0020
source_packet: V1.0H-B
lead_id: XLEAD-CPO-PRICED-IN-VALUATION-WINDOW-001
post_url: https://x.com/aleabitoreddit/status/2054412992000012555
author_or_origin: "@aleabitoreddit"
visible_date: "May 13 2026, user-provided"
source_basis: "user-provided stable URL plus screenshot-visible text"
related_mcc: [MCC-0003, MCC-0004, MCC-0005]
primary_source_role: shareholder_capture_signal
secondary_source_roles: [original_method_expression, capacity_or_constraint_release_signal, external_factual_claim]
review_disposition: recommend_source_record_proposal
review_rationale: "The distinction among exposure type, legacy revenue, cannibalization, starting valuation, and forward-pricing window is a bounded shareholder-capture signal."
bounded_source_record_potential: shareholder_capture_source_record_candidate
required_before_source_record:
  - confirm exact post body
  - extract bounded pricing-window expression
  - separate company and alpha claims
risk_or_limitation:
  - front-running and alpha language
  - asserted market window is unvalidated
cross_reference: []
not_allowed_uses: [not investment advice, not company conclusion, not validated method claim, not runtime rule, not TOC calibration]
```

```yaml
review_id: V10I-REVIEW-0021
source_packet: V1.0H-B
lead_id: XLEAD-CPO-FORWARD-PRICING-WINDOW-001
post_url: https://x.com/aleabitoreddit/status/2052278391928500502
author_or_origin: "@aleabitoreddit"
visible_date: "May 7 2026, user-provided"
source_basis: "user-provided stable URL plus screenshot-visible text"
related_mcc: [MCC-0003, MCC-0004]
primary_source_role: shareholder_capture_signal
secondary_source_roles: [capacity_or_constraint_release_signal, external_factual_claim]
review_disposition: needs_more_human_review
review_rationale: "Financial-recognition lag is useful, but transcript context and company-specific timing claims require exact review and may overlap with the stronger valuation-window lead."
bounded_source_record_potential: shareholder_capture_source_record_candidate
required_before_source_record:
  - confirm exact post and cited transcript context
  - compare duplication with V10I-REVIEW-0020
  - extract bounded recognition-lag language
risk_or_limitation:
  - front-running framing
  - external timing claims
cross_reference:
  - V10I-REVIEW-0020
not_allowed_uses: [not investment advice, not company conclusion, not validated method claim, not runtime rule, not TOC calibration]
```

```yaml
review_id: V10I-REVIEW-0022
source_packet: V1.0H-B
lead_id: XLEAD-GLASS-SUBSTRATE-PRICED-IN-DILUTION-COMPARISON-001
post_url: https://x.com/aleabitoreddit/status/2052184498620834237
author_or_origin: "@aleabitoreddit"
visible_date: "May 7 2026, user-provided"
source_basis: "user-provided stable URL plus screenshot-visible text"
related_mcc: [MCC-0003, MCC-0005]
primary_source_role: external_factual_claim
secondary_source_roles: [shareholder_capture_signal]
review_disposition: exclude_for_now
review_rationale: "Market-cap and company dilution comparisons dominate; the incremental method signal is weaker than clearer priced-in and financing-structure leads."
bounded_source_record_potential: shareholder_capture_source_record_candidate
required_before_source_record:
  - no proposal in V1.0J
  - reconsider only with clearer method wording
risk_or_limitation:
  - company-comparison dependence
  - unverified market and financial facts
cross_reference:
  - V10I-REVIEW-0020
not_allowed_uses: [not investment advice, not company conclusion, not validated method claim, not runtime rule, not TOC calibration]
```

```yaml
review_id: V10I-REVIEW-0023
source_packet: V1.0H-B
lead_id: XLEAD-CONFIDENTIAL-BOM-NOT-PRICED-IN-001
post_url: https://x.com/aleabitoreddit/status/2049767690425016780
author_or_origin: "@aleabitoreddit"
visible_date: "Apr 30 2026, user-provided"
source_basis: "user-provided stable URL plus screenshot-visible text"
related_mcc: [MCC-0002, MCC-0003, MCC-0005]
primary_source_role: physical_supply_chain_mapping_signal
secondary_source_roles: [shareholder_capture_signal, source_governance_signal, external_factual_claim]
review_disposition: needs_more_human_review
review_rationale: "The mapping and delayed-recognition signal is promising, but confidential-BOM and customer assertions are highly inferential and require exact source separation."
bounded_source_record_potential: physical_mapping_source_record_candidate
required_before_source_record:
  - confirm exact post body and context
  - identify public evidence basis
  - separate confidential-relationship assertions
risk_or_limitation:
  - highly inferential
  - private-company and customer mapping claims
cross_reference: []
not_allowed_uses: [not investment advice, not company conclusion, not validated method claim, not runtime rule, not TOC calibration]
```

```yaml
review_id: V10I-REVIEW-0024
source_packet: V1.0H-B
lead_id: XLEAD-IREN-STRUCTURALLY-CAPPED-001
post_url: https://x.com/aleabitoreddit/status/2056750124798464203
author_or_origin: "@aleabitoreddit"
visible_date: "not provided; needs_human_review"
source_basis: "user-provided stable URL plus screenshot-visible search result"
related_mcc: [MCC-0003, MCC-0005]
primary_source_role: shareholder_capture_signal
secondary_source_roles: [risk_or_invalidation_signal, external_factual_claim]
review_disposition: needs_more_human_review
review_rationale: "Structurally capped upside is relevant, but a search-result signal without date and reply context is insufficient for proposal."
bounded_source_record_potential: shareholder_capture_source_record_candidate
required_before_source_record:
  - confirm exact post body and full date
  - confirm thread or reply context
  - verify financing structure separately
risk_or_limitation:
  - screenshot search-result basis
  - categorical company-specific wording
cross_reference:
  - V10I-REVIEW-0025
  - V10I-REVIEW-0027
not_allowed_uses: [not investment advice, not company conclusion, not validated method claim, not runtime rule, not TOC calibration]
```

```yaml
review_id: V10I-REVIEW-0025
source_packet: V1.0H-B
lead_id: XLEAD-ACTIVE-ATM-CAPS-UPSIDE-001
post_url: https://x.com/aleabitoreddit/status/2036519173367726527
author_or_origin: "@aleabitoreddit"
visible_date: "not provided; needs_human_review"
source_basis: "user-provided stable URL plus screenshot-visible text"
related_mcc: [MCC-0003]
primary_source_role: shareholder_capture_signal
secondary_source_roles: [risk_or_invalidation_signal, external_factual_claim]
review_disposition: needs_more_human_review
review_rationale: "An active ATM as a structural ceiling is methodologically meaningful, but date, context, amount, and terms must be confirmed."
bounded_source_record_potential: shareholder_capture_source_record_candidate
required_before_source_record:
  - confirm exact body, date, and thread context
  - verify ATM terms independently
  - deduplicate overlapping capped-upside leads
risk_or_limitation:
  - missing date
  - financing amount unverified
cross_reference:
  - V10I-REVIEW-0024
  - V10I-REVIEW-0027
not_allowed_uses: [not investment advice, not company conclusion, not validated method claim, not runtime rule, not TOC calibration]
```

```yaml
review_id: V10I-REVIEW-0026
source_packet: V1.0H-B
lead_id: XLEAD-ATM-WIPES-CURRENT-SHAREHOLDER-VALUE-001
post_url: https://x.com/aleabitoreddit/status/2030733860607250833
author_or_origin: "@aleabitoreddit"
visible_date: "not provided; needs_human_review"
source_basis: "user-provided stable URL plus screenshot-visible text"
related_mcc: [MCC-0003, MCC-0005]
primary_source_role: shareholder_capture_signal
secondary_source_roles: [original_method_expression, risk_or_invalidation_signal, external_factual_claim]
review_disposition: recommend_source_record_proposal
review_rationale: "The explicit separation between possible company benefit and current shareholder value is a high-value MCC-0003 boundary."
bounded_source_record_potential: shareholder_capture_source_record_candidate
required_before_source_record:
  - confirm exact post body, full date, and context
  - retain categorical wording as attributed expression
  - separate company-specific facts
risk_or_limitation:
  - missing date
  - categorical claim requires context
cross_reference: []
not_allowed_uses: [not investment advice, not company conclusion, not validated method claim, not runtime rule, not TOC calibration]
```

```yaml
review_id: V10I-REVIEW-0027
source_packet: V1.0H-B
lead_id: XLEAD-STRUCTURALLY-CAPPED-BY-ACTIVE-ATM-001
post_url: https://x.com/aleabitoreddit/status/2036535069150773452
author_or_origin: "@aleabitoreddit"
visible_date: "not provided; needs_human_review"
source_basis: "user-provided stable URL plus screenshot-visible text"
related_mcc: [MCC-0003]
primary_source_role: shareholder_capture_signal
secondary_source_roles: [risk_or_invalidation_signal, external_factual_claim]
review_disposition: exclude_for_now
review_rationale: "This formulation overlaps heavily with stronger active-ATM and company-versus-shareholder leads and adds insufficient independent method value at present."
bounded_source_record_potential: shareholder_capture_source_record_candidate
required_before_source_record:
  - no separate proposal in V1.0J
  - retain only as possible context for stronger ATM records
risk_or_limitation:
  - missing date and context
  - duplicative method signal
cross_reference:
  - V10I-REVIEW-0025
  - V10I-REVIEW-0026
not_allowed_uses: [not investment advice, not company conclusion, not validated method claim, not runtime rule, not TOC calibration]
```

## 7. V1.0H-C source-record review

```yaml
review_id: V10I-REVIEW-0028
source_packet: V1.0H-C
lead_id: XLEAD-AXTI-THESIS-DEVILS-ADVOCATE-001
post_url: https://x.com/aleabitoreddit/status/2066823176785457323
author_or_origin: "@aleabitoreddit"
visible_date: "Jun 16 2026, user-provided"
source_basis: "same URL as V1.0H AXTI lead; additional review role"
related_mcc: [MCC-0005, MCC-0002, MCC-0001]
primary_source_role: source_governance_signal
secondary_source_roles: [risk_or_invalidation_signal, original_method_expression, physical_supply_chain_mapping_signal]
review_disposition: defer_as_cross_reference
review_rationale: "This is the same URL as V10I-REVIEW-0001. It should be reviewed and proposed once, with multiple source roles, and must not count as independent recurrence."
bounded_source_record_potential: source_governance_source_record_candidate
required_before_source_record:
  - incorporate this role into the review of V10I-REVIEW-0001
  - do not create a duplicate source record
risk_or_limitation:
  - duplicate URL across packets
cross_reference:
  - V10I-REVIEW-0001
not_allowed_uses: [not investment advice, not company conclusion, not validated method claim, not runtime rule, not TOC calibration]
```

```yaml
review_id: V10I-REVIEW-0029
source_packet: V1.0H-C
lead_id: XLEAD-DISCRETIONARY-INFERENCE-COULD-BE-WRONG-001
post_url: https://x.com/aleabitoreddit/status/2063465386960736396
author_or_origin: "@aleabitoreddit"
visible_date: "Jun 7 2026, user-provided"
source_basis: "user-provided stable URL plus screenshot-visible text"
related_mcc: [MCC-0005, MCC-0001, MCC-0002, MCC-0003]
primary_source_role: source_governance_signal
secondary_source_roles: [risk_or_invalidation_signal, original_method_expression, external_factual_claim]
review_disposition: recommend_source_record_proposal
review_rationale: "The explicit treatment of discretionary inference, unstructured relationships, uncertainty, and later validation is a strong epistemic boundary."
bounded_source_record_potential: source_governance_source_record_candidate
required_before_source_record:
  - confirm exact long-post body and context
  - extract a bounded uncertainty and validation excerpt
  - separate forecasts and company examples
risk_or_limitation:
  - long post
  - forward-looking examples require independent review
cross_reference: []
not_allowed_uses: [not investment advice, not company conclusion, not validated method claim, not runtime rule, not TOC calibration]
```

```yaml
review_id: V10I-REVIEW-0030
source_packet: V1.0H-C
lead_id: XLEAD-SIVE-PUBLIC-INFO-UNCERTAINTY-001
post_url: https://x.com/aleabitoreddit/status/2049032343974007088
author_or_origin: "@aleabitoreddit"
visible_date: "Apr 28 2026, user-provided"
source_basis: "user-provided stable URL plus screenshot-visible text"
related_mcc: [MCC-0005, MCC-0002, MCC-0003]
primary_source_role: source_governance_signal
secondary_source_roles: [physical_supply_chain_mapping_signal, risk_or_invalidation_signal, external_factual_claim]
review_disposition: recommend_source_record_proposal
review_rationale: "The public-information, website-research, relationship-mapping, and could-be-wrong boundary is reusable if customer claims are excluded."
bounded_source_record_potential: source_governance_source_record_candidate
required_before_source_record:
  - confirm exact post body and context
  - extract bounded public-source inference language
  - separate customer and supplier relationship claims
risk_or_limitation:
  - highly inferential relationship mapping
  - market-pricing assertions unverified
cross_reference: []
not_allowed_uses: [not investment advice, not company conclusion, not validated method claim, not runtime rule, not TOC calibration]
```

```yaml
review_id: V10I-REVIEW-0031
source_packet: V1.0H-C
lead_id: XLEAD-BORROWED-CONVICTION-RISK-001
post_url: https://x.com/aleabitoreddit/status/2039729176144711989
author_or_origin: "@aleabitoreddit"
visible_date: "Apr 2 2026, user-provided"
source_basis: "user-provided stable URL plus screenshot-visible text"
related_mcc: [MCC-0005]
primary_source_role: risk_or_invalidation_signal
secondary_source_roles: [external_factual_claim]
review_disposition: exclude_for_now
review_rationale: "Borrowed conviction and volatility are general risk-management observations with limited direct value for chokepoint evidence sufficiency or falsification."
bounded_source_record_potential: risk_invalidation_source_record_candidate
required_before_source_record:
  - no proposal in V1.0J
risk_or_limitation:
  - too remote from chokepoint method
  - market-movement context
cross_reference: []
not_allowed_uses: [not investment advice, not company conclusion, not validated method claim, not runtime rule, not TOC calibration]
```

```yaml
review_id: V10I-REVIEW-0032
source_packet: V1.0H-C
lead_id: XLEAD-OPTICAL-PCB-FALSE-POSITIVE-RISK-001
post_url: https://x.com/aleabitoreddit/status/2037085574813942094
author_or_origin: "@aleabitoreddit"
visible_date: "Mar 26 2026, user-provided"
source_basis: "user-provided stable URL plus screenshot-visible text"
related_mcc: [MCC-0005, MCC-0001, MCC-0003, MCC-0004]
primary_source_role: risk_or_invalidation_signal
secondary_source_roles: [original_method_expression, value_capture_signal, capacity_or_constraint_release_signal, external_factual_claim]
review_disposition: recommend_source_record_proposal
review_rationale: "The post compares stronger and weaker bottleneck candidates using beneficiary quality, company mix, and capacity easing, making it the clearest false-positive-control lead."
bounded_source_record_potential: risk_invalidation_source_record_candidate
required_before_source_record:
  - confirm exact post and external quotation context
  - extract bounded false-positive language
  - separate company and capacity facts
risk_or_limitation:
  - external quotation
  - company and supply-chain assertions unverified
cross_reference: []
not_allowed_uses: [not investment advice, not company conclusion, not validated method claim, not runtime rule, not TOC calibration]
```

```yaml
review_id: V10I-REVIEW-0033
source_packet: V1.0H-C
lead_id: XLEAD-HIMS-BEAR-BULL-CASE-LAYERING-001
post_url: https://x.com/aleabitoreddit/status/2031177724015063487
author_or_origin: "@aleabitoreddit"
visible_date: "Mar 10 2026, user-provided"
source_basis: "user-provided stable URL plus screenshot-visible text"
related_mcc: [MCC-0005, MCC-0003]
primary_source_role: risk_or_invalidation_signal
secondary_source_roles: [value_capture_signal, external_factual_claim]
review_disposition: needs_more_human_review
review_rationale: "Testing whether a bear case attacks the correct layer is useful, but this non-supply-chain example requires exact cross-case framing before proposal."
bounded_source_record_potential: risk_invalidation_source_record_candidate
required_before_source_record:
  - confirm exact post body
  - establish cross-case relevance
  - separate valuation claims
risk_or_limitation:
  - non-supply-chain example
  - company valuation dependence
cross_reference: []
not_allowed_uses: [not investment advice, not company conclusion, not validated method claim, not runtime rule, not TOC calibration]
```

```yaml
review_id: V10I-REVIEW-0034
source_packet: V1.0H-C
lead_id: XLEAD-RDDT-BEAR-CASE-INDICATOR-MISPRICING-001
post_url: https://x.com/aleabitoreddit/status/2031057996395233426
author_or_origin: "@aleabitoreddit"
visible_date: "Mar 10 2026, user-provided"
source_basis: "user-provided stable URL plus screenshot-visible text"
related_mcc: [MCC-0005, MCC-0003]
primary_source_role: external_factual_claim
secondary_source_roles: [risk_or_invalidation_signal, value_capture_signal]
review_disposition: exclude_for_now
review_rationale: "The advertising example is remote from supply-chain chokepoint review and adds weaker method value than other system-specific bear-case leads."
bounded_source_record_potential: risk_invalidation_source_record_candidate
required_before_source_record:
  - no proposal in V1.0J
risk_or_limitation:
  - remote cross-case example
  - market-pricing and advertiser claims
cross_reference: []
not_allowed_uses: [not investment advice, not company conclusion, not validated method claim, not runtime rule, not TOC calibration]
```

```yaml
review_id: V10I-REVIEW-0035
source_packet: V1.0H-C
lead_id: XLEAD-GRID-UPGRADE-BEAR-CASE-REFRAME-001
post_url: https://x.com/aleabitoreddit/status/2025227339408490717
author_or_origin: "@aleabitoreddit"
visible_date: "Feb 21 2026, user-provided"
source_basis: "user-provided stable URL plus screenshot-visible text"
related_mcc: [MCC-0005, MCC-0003]
primary_source_role: risk_or_invalidation_signal
secondary_source_roles: [value_capture_signal, external_factual_claim]
review_disposition: needs_more_human_review
review_rationale: "Reframing an apparent bear case as pricing power is relevant, but the macro-sector example requires evidence that it transfers to chokepoint review."
bounded_source_record_potential: risk_invalidation_source_record_candidate
required_before_source_record:
  - confirm exact post body
  - establish cross-case method relevance
  - separate pricing-power claims
risk_or_limitation:
  - macro-sector example
  - possible investment-exposure framing
cross_reference: []
not_allowed_uses: [not investment advice, not company conclusion, not validated method claim, not runtime rule, not TOC calibration]
```

```yaml
review_id: V10I-REVIEW-0036
source_packet: V1.0H-C
lead_id: XLEAD-CAPACITY-SCALE-UP-BEAR-CASE-001
post_url: https://x.com/aleabitoreddit/status/2023738495903351200
author_or_origin: "@aleabitoreddit"
visible_date: "Feb 17 2026, user-provided"
source_basis: "user-provided stable URL plus screenshot-visible text"
related_mcc: [MCC-0005, MCC-0004, MCC-0001]
primary_source_role: risk_or_invalidation_signal
secondary_source_roles: [capacity_or_constraint_release_signal, original_method_expression, external_factual_claim]
review_disposition: recommend_source_record_proposal
review_rationale: "The author explicitly identifies an unanswered capacity and upstream-shortage bear case and names future earnings as a validation point."
bounded_source_record_potential: risk_invalidation_source_record_candidate
required_before_source_record:
  - confirm exact post body and context
  - extract bounded unresolved-question and validation language
  - separate backlog and capacity facts
risk_or_limitation:
  - company-specific capacity claims
  - later validation event not reviewed
cross_reference: []
not_allowed_uses: [not investment advice, not company conclusion, not validated method claim, not runtime rule, not TOC calibration]
```

```yaml
review_id: V10I-REVIEW-0037
source_packet: V1.0H-C
lead_id: XLEAD-CUSTOMER-VERTICAL-INTEGRATION-BEAR-CASE-001
post_url: https://x.com/aleabitoreddit/status/2019315806245646768
author_or_origin: "@aleabitoreddit"
visible_date: "Feb 5 2026, user-provided"
source_basis: "user-provided stable URL plus screenshot-visible text"
related_mcc: [MCC-0005, MCC-0003, MCC-0004]
primary_source_role: risk_or_invalidation_signal
secondary_source_roles: [capacity_or_constraint_release_signal, value_capture_signal, external_factual_claim]
review_disposition: recommend_source_record_proposal
review_rationale: "Customer self-supply and vertical integration are clear, transferable thesis-failure conditions for supplier value capture and apparent constraints."
bounded_source_record_potential: risk_invalidation_source_record_candidate
required_before_source_record:
  - confirm exact post body and context
  - extract bounded vertical-integration risk language
  - separate customer and supplier assertions
risk_or_limitation:
  - external relationship claims
  - company example may dominate context
cross_reference: []
not_allowed_uses: [not investment advice, not company conclusion, not validated method claim, not runtime rule, not TOC calibration]
```

```yaml
review_id: V10I-REVIEW-0038
source_packet: V1.0H-C
lead_id: XLEAD-REGULATION-BEAR-CASE-OVERHANG-001
post_url: https://x.com/aleabitoreddit/status/2018809577861730505
author_or_origin: "@aleabitoreddit"
visible_date: "Feb 4 2026, user-provided"
source_basis: "user-provided stable URL plus screenshot-visible text"
related_mcc: [MCC-0005, MCC-0003]
primary_source_role: risk_or_invalidation_signal
secondary_source_roles: [value_capture_signal, external_factual_claim]
review_disposition: needs_more_human_review
review_rationale: "Regulation as a mechanism-removal condition is useful, but the financial-product example is remote and needs explicit cross-case justification."
bounded_source_record_potential: risk_invalidation_source_record_candidate
required_before_source_record:
  - confirm exact post body and context
  - establish cross-case relevance
  - separate regulatory factual claims
risk_or_limitation:
  - non-supply-chain financial-product example
  - regulatory probability unverified
cross_reference: []
not_allowed_uses: [not investment advice, not company conclusion, not validated method claim, not runtime rule, not TOC calibration]
```

```yaml
review_id: V10I-REVIEW-0039
source_packet: V1.0H-C
lead_id: XLEAD-POLICY-RISK-MULTI-SECTOR-FRAMEWORK-001
post_url: https://x.com/aleabitoreddit/status/2017919446296437037
author_or_origin: "@aleabitoreddit"
visible_date: "Feb 1 2026, user-provided"
source_basis: "user-provided stable URL plus screenshot-visible text"
related_mcc: [MCC-0005]
primary_source_role: context_only
secondary_source_roles: [risk_or_invalidation_signal, external_factual_claim]
review_disposition: exclude_for_now
review_rationale: "The macro policy decomposition is too remote from the current chokepoint source-record proposal priorities and was already marked optional low priority."
bounded_source_record_potential: risk_invalidation_source_record_candidate
required_before_source_record:
  - no proposal in V1.0J
risk_or_limitation:
  - low direct relevance
  - long macro-policy post
cross_reference: []
not_allowed_uses: [not investment advice, not company conclusion, not validated method claim, not runtime rule, not TOC calibration]
```

```yaml
review_id: V10I-REVIEW-0040
source_packet: V1.0H-C
lead_id: XLEAD-CAPEX-BEAR-CASE-ROI-REFRAME-001
post_url: https://x.com/aleabitoreddit/status/2016973892674630066
author_or_origin: "@aleabitoreddit"
visible_date: "Jan 30 2026, user-provided"
source_basis: "user-provided stable URL plus screenshot-visible text"
related_mcc: [MCC-0005, MCC-0003]
primary_source_role: risk_or_invalidation_signal
secondary_source_roles: [value_capture_signal, external_factual_claim]
review_disposition: needs_more_human_review
review_rationale: "Testing capex bear cases against revenue and return conversion is useful, but the large-cap example requires cross-case justification and precise excerpt review."
bounded_source_record_potential: risk_invalidation_source_record_candidate
required_before_source_record:
  - confirm exact post body
  - establish cross-case relevance
  - separate company and return claims
risk_or_limitation:
  - non-chokepoint large-cap example
  - ROI claims unverified
cross_reference: []
not_allowed_uses: [not investment advice, not company conclusion, not validated method claim, not runtime rule, not TOC calibration]
```

## 8. Cross-reference and deduplication notes

- `V10I-REVIEW-0001` and `V10I-REVIEW-0028` are the same AXTI URL. Review once; preserve physical-mapping, source-governance, and invalidation roles in one future proposal.
- `V10I-REVIEW-0018` is a six-URL cluster. Every URL requires independent review and may result in zero, one, or several proposals.
- `V10I-REVIEW-0020` and `V10I-REVIEW-0021` overlap on forward-pricing and recognition lag. The former is the stronger proposal candidate.
- `V10I-REVIEW-0024`, `V10I-REVIEW-0025`, and `V10I-REVIEW-0027` overlap on structurally capped upside and active ATMs. They must not be counted as three independent method recurrences without context review.
- Related third-party context, quotations, analyst work, filings, earnings calls, or media references remain `context_only` or `external_factual_claim`, not Serenity original expression.

## 9. Recommended source-record proposal candidates

This section recommends source-record proposal candidates only. It does not create or approve source records.

| review_id | lead_id | post URL | source role | related MCC | why recommended | required before creation |
| --- | --- | --- | --- | --- | --- | --- |
| V10I-REVIEW-0001 | XLEAD-AXTI-001 | `2066823176785457323` | method expression / physical mapping / governance | MCC-0002, MCC-0005 | Explicit research process and devil's-advocate boundary | Confirm body, date, thread; separate external claims; merge cross-reference |
| V10I-REVIEW-0002 | XLEAD-AMD-CW-LASER-001 | `2067206734427697196` | physical mapping / capacity | MCC-0001, MCC-0002, MCC-0004 | Multi-party capacity-locking structure | Confirm year/context; isolate mapping; separate company claims |
| V10I-REVIEW-0007 | XLEAD-SIVE-LPK-VALUE-CHAIN-001 | `2055822766600016238` | method expression / physical mapping / value capture | MCC-0001, MCC-0002, MCC-0003 | Links technical depth, supply chain, margin, and integration | Bound excerpt; remove TAM and portfolio claims |
| V10I-REVIEW-0008 | XLEAD-PHISON-MEMORY-VALUE-CAPTURE-001 | `2023323844346618010` | firm-level value capture | MCC-0003 | Toll-collector and control-point layer distinction | Confirm body/date; exclude long/short directives |
| V10I-REVIEW-0013 | XLEAD-DILUTION-STRUCTURE-ACCRETIVE-PREDATORY-001 | `2063573828928954442` | shareholder capture / governance | MCC-0003, MCC-0005 | Clear structure-and-use-of-proceeds judgment | Confirm context; bound wording; remove company examples |
| V10I-REVIEW-0014 | XLEAD-TOXIC-FINANCING-FLOAT-DYNAMICS-001 | `2063571485739106593` | shareholder capture / invalidation | MCC-0003, MCC-0005 | Financing and float mechanisms affecting equity capture | Confirm body; exclude accusations; independently source facts |
| V10I-REVIEW-0015 | XLEAD-FINANCING-STRUCTURE-EQUITY-APPRECIATION-001 | `2062119438552572283` | shareholder capture | MCC-0003, MCC-0005 | Direct financing-structure versus equity-appreciation distinction | Confirm reply context; isolate expression |
| V10I-REVIEW-0016 | XLEAD-CAPACITY-MONETIZATION-DILUTION-001 | `2053928672202268993` | shareholder capture / capacity | MCC-0003, MCC-0004, MCC-0005 | Separates operating capacity from shareholder monetization | Confirm body; remove company conclusion |
| V10I-REVIEW-0020 | XLEAD-CPO-PRICED-IN-VALUATION-WINDOW-001 | `2054412992000012555` | shareholder capture / valuation timing | MCC-0003, MCC-0004, MCC-0005 | Bounded priced-in and forward-window signal | Confirm exact wording; remove alpha framing |
| V10I-REVIEW-0026 | XLEAD-ATM-WIPES-CURRENT-SHAREHOLDER-VALUE-001 | `2030733860607250833` | shareholder capture | MCC-0003, MCC-0005 | Explicit company-benefit versus shareholder-value boundary | Confirm date/context; preserve attribution |
| V10I-REVIEW-0029 | XLEAD-DISCRETIONARY-INFERENCE-COULD-BE-WRONG-001 | `2063465386960736396` | source governance / invalidation | MCC-0005 | Strong uncertainty and later-validation boundary | Extract bounded long-post excerpt |
| V10I-REVIEW-0030 | XLEAD-SIVE-PUBLIC-INFO-UNCERTAINTY-001 | `2049032343974007088` | source governance / physical mapping | MCC-0005, MCC-0002 | Public-source inference boundary | Confirm context; separate relationships |
| V10I-REVIEW-0032 | XLEAD-OPTICAL-PCB-FALSE-POSITIVE-RISK-001 | `2037085574813942094` | false-positive / invalidation | MCC-0005, MCC-0001 | Stronger-versus-weaker bottleneck comparison | Confirm external quote and isolate method language |
| V10I-REVIEW-0036 | XLEAD-CAPACITY-SCALE-UP-BEAR-CASE-001 | `2023738495903351200` | invalidation / capacity response | MCC-0005, MCC-0004 | Explicit unanswered bear case and future validation point | Confirm body/context; separate company facts |
| V10I-REVIEW-0037 | XLEAD-CUSTOMER-VERTICAL-INTEGRATION-BEAR-CASE-001 | `2019315806245646768` | invalidation / bypass | MCC-0005, MCC-0003, MCC-0004 | Transferable vertical-integration failure condition | Confirm body; separate relationship claims |

V1.0J should select only 8–12 of these 15 candidates, prioritizing complementary coverage over volume.

## 10. Needs-more-human-review list

| review_id | lead_id | missing review |
| --- | --- | --- |
| V10I-REVIEW-0003 | XLEAD-EML-CW-LASER-001 | Parent/reply context, full date, exact excerpt |
| V10I-REVIEW-0004 | XLEAD-FOOSUNG-WF6-001 | Full date, context, policy and share-claim separation |
| V10I-REVIEW-0005 | XLEAD-LEADERDRIVE-VALUE-CAPTURE-001 | Third-party context separation and exact body |
| V10I-REVIEW-0006 | XLEAD-SIVE-ARTICLE-CPO-LASER-CHOKEPOINT-001 | Accessible article body and bounded excerpt |
| V10I-REVIEW-0009 | XLEAD-VPG-HUMANOID-VALUE-CAPTURE-001 | Scenario inputs and method-expression isolation |
| V10I-REVIEW-0010 | XLEAD-IREN-NBIS-DILUTION-001 | Calendar date, reply context, neutral excerpt |
| V10I-REVIEW-0012 | XLEAD-AXTI-DILUTION-RISK-001 | Parent context and exact reply body |
| V10I-REVIEW-0017 | XLEAD-RETAIL-LIQUIDITY-EQUITY-APPRECIATION-001 | Context and non-inflammatory bounded language |
| V10I-REVIEW-0018 | XLEAD-IREN-NBIS-EQUITY-APPRECIATION-THREAD-001 | Six independent URL reviews and deduplication |
| V10I-REVIEW-0019 | XLEAD-EUROPEAN-PHOTONICS-PRICED-IN-001 | Separate holdings/upside from timing signal |
| V10I-REVIEW-0021 | XLEAD-CPO-FORWARD-PRICING-WINDOW-001 | Transcript context and overlap review |
| V10I-REVIEW-0023 | XLEAD-CONFIDENTIAL-BOM-NOT-PRICED-IN-001 | Public basis and confidential relationship separation |
| V10I-REVIEW-0024 | XLEAD-IREN-STRUCTURALLY-CAPPED-001 | Exact body, date, reply context |
| V10I-REVIEW-0025 | XLEAD-ACTIVE-ATM-CAPS-UPSIDE-001 | Exact body, date, ATM terms, deduplication |
| V10I-REVIEW-0033 | XLEAD-HIMS-BEAR-BULL-CASE-LAYERING-001 | Cross-case relevance and exact excerpt |
| V10I-REVIEW-0035 | XLEAD-GRID-UPGRADE-BEAR-CASE-REFRAME-001 | Cross-case relevance and pricing-power evidence |
| V10I-REVIEW-0038 | XLEAD-REGULATION-BEAR-CASE-OVERHANG-001 | Cross-case relevance and regulatory context |
| V10I-REVIEW-0040 | XLEAD-CAPEX-BEAR-CASE-ROI-REFRAME-001 | Cross-case relevance and ROI evidence |

Common manual checks include exact visible post body, full date and year, reply/thread context, whether an external quotation is original expression or cited text, and whether a cluster should split into several source records.

## 11. Exclude-for-now list

| review_id | lead_id | reason |
| --- | --- | --- |
| V10I-REVIEW-0011 | XLEAD-CAMT-NAV-DILUTION-001 | Company-specific personal notes with weaker reusable method signal |
| V10I-REVIEW-0022 | XLEAD-GLASS-SUBSTRATE-PRICED-IN-DILUTION-COMPARISON-001 | Company and market comparison dominates; stronger valuation leads exist |
| V10I-REVIEW-0027 | XLEAD-STRUCTURALLY-CAPPED-BY-ACTIVE-ATM-001 | Duplicate method value without sufficient context |
| V10I-REVIEW-0031 | XLEAD-BORROWED-CONVICTION-RISK-001 | General risk-management observation too remote from chokepoint review |
| V10I-REVIEW-0034 | XLEAD-RDDT-BEAR-CASE-INDICATOR-MISPRICING-001 | Advertising example too remote from current proposal priorities |
| V10I-REVIEW-0039 | XLEAD-POLICY-RISK-MULTI-SECTOR-FRAMEWORK-001 | Optional macro-policy context with low direct relevance |

Third-party context is also excluded as a Serenity original expression even when retained to understand a reviewed post.

## 12. Remaining gaps

V1.0I does not complete Serenity Chokepoint Theory.

Remaining gaps:

- No source records are created yet.
- No source records are approved yet.
- Exact post bodies, dates, replies, and threads remain to be verified before source-record creation.
- External factual claims require independent public sources.
- Multi-URL clusters and overlapping formulations require per-URL review and deduplication.
- MCCs remain unvalidated.
- TOC calibration is not yet performed.
- Runtime rules are not yet approved.
- Visual model / framework artifact source leads remain a possible later supplement if needed.

## 13. Recommended next step

The recommended next step is:

**V1.0J — X Source Record Proposal Creation**

V1.0J should create only a limited number of bounded source record proposals from the V1.0I recommended candidates. It should not attempt to convert every lead into a source record and must preserve `not_distilled` status.

Recommended scope: **8–12 high-quality source record proposals**, prioritizing:

1. physical supply-chain mapping / bottleneck framing;
2. firm-level value capture;
3. shareholder-capture boundary;
4. risk / invalidation discipline; and
5. false-positive control.

## 14. Final boundary note

This file contains source-record-review dispositions only. It creates and approves no source records or corpus entries, validates no method claims, performs no TOC calibration, approves no runtime rules, reaches no real-company conclusions, and provides no investment advice, trading instruction, target price, position sizing, return expectation, or buy/sell/hold recommendation. It performs no continued X search, X scraping, twscrape integration, X API call, secret access, login-wall bypass, deleted-post reconstruction, or independent verification of post bodies, dates, authors, replies, threads, or factual assertions.
