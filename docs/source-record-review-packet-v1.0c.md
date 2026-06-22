# Source Record Review Packet v1.0C

## 1. Purpose

This file converts the seven high-priority leads in `docs/source-leads-v1.0b.md` into a bounded draft packet for human review. It records public locators, minimal context, attributed paraphrases, candidate classifications, limitations, and unresolved checks so that a reviewer does not need to rediscover the basic source trail.

This is not a corpus.

This is not a final SourceRecord set.

This is not methodology distillation.

This is not a research report.

Human approval is required before any draft can enter seed source records. Every block below remains a draft regardless of how complete its locator appears. Company, government, and news evidence may test case assertions, but it must not be treated as Serenity's original expression or as proof of Serenity's method.

The review was limited to publicly accessible Reddit pages, USGS material, SEC EDGAR, company investor-relations material, and the publicly visible portion of a news page. It did not preserve a full Reddit thread or a full news article.

## 2. Review status legend

| status | meaning |
| --- | --- |
| `ready_for_human_review` | A stable public locator and enough bounded context are present for a reviewer to approve, narrow, defer, or reject the draft. This status is not acceptance. |
| `needs_stable_permalink` | The current locator is dynamic, broad, incomplete, or not yet reduced to a stable item-level permalink. |
| `needs_date_confirmation` | The visible source did not provide enough reliable date precision; no date should be inferred or rounded into a final record. |
| `needs_excerpt_confirmation` | The proposed excerpt is unavailable, deleted, paywalled, truncated, or otherwise requires a reviewer to compare it with the source. |
| `needs_source_type_confirmation` | The source category or attribution relationship remains ambiguous. |
| `needs_filing_identifier` | A regulatory locator still needs an accession number, form, filing date, or specific document identifier. |
| `reject_candidate` | The lead appears unsuitable for seed source records because provenance, access, content, or scope is inadequate. |

## 3. Draft packet table

| lead_id | title | stable_url_or_locator | author_or_origin | platform | source_type_candidate | captured_context | short_excerpt_or_locator_note | attributed_paraphrase | method_dimension_candidate | toc_relevance_candidate | risk_or_limitation | missing_human_checks | recommended_review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LEAD-002 | The Entire AI Buildout … Is dependent on this … Monopoly | <https://www.reddit.com/r/wallstreetbets/comments/1pyghud/the_entire_ai_buildout_google_nvda_msft_is/> | `u/AleaBito` | Reddit, `r/wallstreetbets` | `serenity_original_public_expression` candidate | Public post remains visible. It presents an asserted chain from AI photonics demand to InP substrates and indium-phosphide materials, identifies AXT as appearing at two claimed bottlenecks, discusses direct exposure, and includes a China export-control downside. | Minimal excerpt: “THE ENTIRE AI INDUSTRY IS BOTTLENECKED TWO TIMES BY THE SAME COMPANY.” | The author argues that rising photonics use makes InP-related supply a constraint and that AXT provides unusually direct exposure, while also acknowledging export-control risk. The market-share, capacity, valuation, and causal claims are unverified within the post. | `value_chain_decomposition`, `chokepoint_identification`, `physical_floor_mapping`, `value_capture`, `thesis_killer` | `constraint_identification`, `local_bottleneck_vs_system_constraint`, `value_capture_vs_throughput`, `false_chokepoint_filter` | Promotional framing, price targets, self-reported positioning, and unsupported numerical claims create advice and factual-verification risk. The Reddit page displays only a relative age in the reviewed view. | Confirm exact publication date; confirm identity/attribution policy; verify excerpt in context; decide whether the post is eligible as original public expression; keep all company assertions separate for corroboration. | `needs_date_confirmation` |
| LEAD-003 | Raspberry Pi is up 40% after TAM expansion … due to OpenClaw | <https://www.reddit.com/r/wallstreetbets/comments/1r7mv0j/raspberry_pi_is_up_40_after_tam_expansion/> | `needs_human_review` | Reddit, `r/wallstreetbets` | `serenity_original_public_expression` candidate | The post body and top-level author are now shown as deleted. The stable Reddit ID, title, public timestamp metadata, and surviving comments remain. Surviving comments labeled `u/AleaBito` discuss Raspberry Pi's public listing, AI-agent orchestration use, product pricing, memory costs, and the materiality of the market move. | Locator note: original body unavailable. One surviving author-labeled comment says, “People are buying them today for AI agent orchestration.” | Surviving context indicates a proposed demand-expansion case linking AI-agent orchestration to Raspberry Pi demand, with memory pricing and alternative hardware as visible counterpoints. The deleted body must not be reconstructed from comments or secondary coverage. | `demand_anchor`, `catalyst_or_earnings_validation`, `value_capture`, `thesis_killer` | `system_boundary`, `throughput_definition`, `false_chokepoint_filter` | Original post text is deleted; top-level author now displays `[deleted]`; comments do not substitute for the missing post; causal and materiality claims are time-sensitive and reflexive. | Confirm original author from an approved source; confirm `2026-02-17T23:45:46Z` public Reddit metadata; decide whether a surviving comment permalink should become a separate record; supply and verify any bounded original excerpt or reject the post-level draft. | `needs_excerpt_confirmation` |
| LEAD-004 | VLN Robotics Chipmaker is Fundamentally Undervalued by 60% | <https://www.reddit.com/r/ValueInvesting/comments/1q8nmlw/vln_robotics_chipmaker_is_fundamentally/> | `needs_human_review` | Reddit, `r/ValueInvesting` | `serenity_original_public_expression` candidate | The post body and top-level author are now shown as deleted. The stable Reddit ID and title remain. Surviving comments labeled `u/AleaBito` discuss valuation, revenue, gross margin, cash, inventory, liabilities versus debt, and reliance on Valens' official quarterly report. | Locator note: original body unavailable. A surviving author-labeled comment points reviewers to Valens' actual financial report and quotes its cash-and-deposits figure. | Surviving context indicates a valuation-gap case built from company-reported financial data and a distinction between liabilities and interest-bearing debt. The deleted original thesis and its “60%” conclusion cannot be verified from the post page. | `valuation_gap`, `catalyst_or_earnings_validation`, `invalidation_condition` | `value_capture_vs_throughput`, `false_chokepoint_filter` | Original post text is deleted; top-level author is unavailable; the headline embeds a valuation conclusion; comments contain disputes over ticker identity and financial definitions. | Confirm original author and publication date; verify whether any original excerpt is lawfully available; compare every financial datapoint with the dated Valens release; decide whether this post-level draft should be rejected in favor of comment-level records. | `needs_excerpt_confirmation` |
| LEAD-018 | USGS Mineral Commodity Summaries 2026 — Indium | <https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-indium.pdf> | Rob Crangle, U.S. Geological Survey | USGS PDF, Mineral Commodity Summaries | `industry_evidence` | Two-page government summary dated February 2026. It reports 2025 estimates for U.S. import reliance, global refinery production, China's share, export restrictions, InP uses, AI-related demand expectations, and substitutes primarily associated with ITO applications. | Minimal excerpt: “China is the leading global producer of indium, accounting for 70% of the world total.” | USGS reports complete estimated U.S. net import reliance, concentrated global refinery production, 2025 Chinese export restrictions, and multiple InP optical-communications uses. It does not establish wafer-grade InP substrate capacity or AXT's company-level position. | `physical_floor_mapping`, `capacity_or_lead_time_constraint`, `substitution_difficulty`, `thesis_killer` | `CCR_characteristics`, `constraint_identification`, `constraint_migration`, `false_chokepoint_filter` | Several figures are estimates; national indium data are broader than InP substrate supply; listed substitutes mainly concern ITO and cannot automatically rebut an InP photonics constraint. | Confirm excerpt punctuation against the PDF; confirm whether the whole summary or only the Indium pages should be the record unit; approve industry-evidence-only use. | `ready_for_human_review` |
| LEAD-020 | AXT SEC filings | SEC company index: <https://www.sec.gov/edgar/browse/?CIK=1051627&owner=exclude>. Focused locators: 2026 Q1 Form 10-Q accession `0001437749-26-017054`; April 20, 2026 Form 8-K accessions `0001213900-26-045652` and `0001213900-26-045867`; April 20, 2026 Form 424B5 accession `0001213900-26-045643`; April 21, 2026 Form 424B5 accession `0001213900-26-046176`. | AXT, Inc. filings submitted to the U.S. Securities and Exchange Commission | SEC EDGAR | `company_evidence` | The index supplies primary regulatory locators for quarterly financials, guidance, corporate structure, risk factors, and financing. The April 21 prospectus supplement offers 8,560,311 shares at $64.25 per share and identifies intended uses of proceeds, subject to the filing's terms and limitations. | Locator note: accession `0001213900-26-046176`, Form 424B5, filed April 21, 2026. Minimal excerpt: “increase its capacity to produce indium phosphide substrates for export worldwide”. | AXT's filings disclose its operating and corporate structure, risks, financial condition, guidance, and a large 2026 equity offering whose stated uses include supporting Tongmei's InP substrate capacity expansion. These disclosures can test case assertions but cannot establish a Serenity method claim or a complete company conclusion. | `value_chain_decomposition`, `capacity_or_lead_time_constraint`, `value_capture`, `thesis_killer`, `invalidation_condition` | `elevation_path`, `value_capture_vs_throughput`, `constraint_release`, `false_chokepoint_filter` | Filings are issuer disclosures with reporting lag, incorporated documents, forward-looking statements, and complex entity structure. The broad lead spans multiple records and should be split if approved. | Confirm which accession numbers should become separate source records; verify excerpt against the final 424B5; identify exact sections needed for structure, risk, guidance, and financing; approve company-evidence-only use. | `ready_for_human_review` |
| LEAD-021 | Valens Semiconductor quarterly results | Quarterly index: <https://investors.valens.com/financials/quarterly-results/default.aspx>. Focused Q3 2025 release: <https://s28.q4cdn.com/438644442/files/doc_financials/2025/q3/PR-NYSE_VLN-Q3_25_Web.pdf> | Valens Semiconductor Ltd. | Company investor relations / Q3 2025 press-release PDF | `company_evidence` | Official release dated November 12, 2025 for the quarter ended September 30, 2025. It reports revenue, GAAP and non-GAAP margins, segment revenue and margins, net loss, adjusted EBITDA, cash and short-term deposits, debt statement, inventory, liabilities, and cash flows. | Minimal excerpt: “Cash balance as of September 30, 2025, was $93.5 million and no debt.” | Valens reported Q3 2025 revenue of $17.3 million, 63.0% GAAP gross margin, $93.5 million of cash and short-term deposits, no debt, a GAAP net loss, and negative operating cash flow. These dated figures can check claims in the deleted VLN post but do not validate its valuation conclusion. | `valuation_gap`, `catalyst_or_earnings_validation`, `invalidation_condition` | `value_capture_vs_throughput`, `false_chokepoint_filter` | Company release includes non-GAAP measures and management framing; “no debt” does not mean no liabilities; figures are period-specific; later results may differ. | Confirm excerpt against the PDF; decide whether the press release or related SEC filing is preferred; verify each Reddit-derived datapoint and definition separately; approve company-evidence-only use. | `ready_for_human_review` |
| LEAD-016 | Barron’s: AXT Stock Drops. What’s Hitting the Hot Photonics Play. | <https://www.barrons.com/articles/axt-stock-price-share-offering-83039818> | Adam Clark, Barron's | Barron's | `public_secondary_analysis` | Public page metadata and visible lead paragraph identify the author, headline, and April 21, 2026 publication. The visible article framing links a share-price decline to an offering and revenue guidance; detailed terms should be checked against AXT's SEC filings. | Minimal excerpt from the visible lead: “tumbling Tuesday on a stock offering and revenue guidance”. | Barron's reports that AXT shares fell after an offering and guidance update. It is useful as secondary event framing for dilution and common-equity value-capture questions, not as Serenity attribution or as primary evidence of offering terms. | `thesis_killer`, `value_capture`, `invalidation_condition` | `elevation_path`, `value_capture_vs_throughput`, `false_chokepoint_filter` | Most article detail is behind a subscription wall; the source does not quote or name Serenity; market-move framing is time-sensitive; offering figures require SEC confirmation. | Confirm publication timestamp and excerpt in the reviewer's accessible view; keep all offering terms anchored to SEC filings; decide whether the limited accessible context is sufficient for a secondary-only record. | `ready_for_human_review` |

## 4. SourceRecord draft blocks

These YAML blocks are review conveniences only. Field names that go beyond the current minimum schema are candidate review fields, not validated production schema. No block is accepted, distillation-ready, or authorized for `data/seed/source-records/`.

### LEAD-002 draft

```yaml
draft_source_id: DRAFT-SR-V10C-LEAD-002
lead_id: LEAD-002
source_type: serenity_original_public_expression
author_or_origin: u/AleaBito
source_url_or_locator: https://www.reddit.com/r/wallstreetbets/comments/1pyghud/the_entire_ai_buildout_google_nvda_msft_is/
platform: Reddit / r/wallstreetbets
published_at: needs_human_review
captured_at: 2026-06-23
acquisition_method: manual review of a publicly accessible Reddit permalink
permission_basis: public access; bounded quotation and attributed paraphrase only
excerpt: "THE ENTIRE AI INDUSTRY IS BOTTLENECKED TWO TIMES BY THE SAME COMPANY."
excerpt_length_note: 11-word excerpt retained only to preserve the post's stated two-layer bottleneck formulation.
paraphrase: The author proposes that AI photonics demand creates two related InP constraints and argues that AXT appears at both layers, while acknowledging export-control downside.
attribution_note: The claim is attributed to the Reddit author. No numerical, market-share, capacity, valuation, or company claim is endorsed.
topic_tags:
  - AXTI
  - indium_phosphide
  - photonics
  - supply_chain
method_dimension_candidates:
  - value_chain_decomposition
  - physical_floor_mapping
  - chokepoint_identification
  - value_capture
  - thesis_killer
judgment_rule_candidates:
  - "candidate question: does the same entity appear at more than one constrained layer?"
  - "candidate question: is the claimed constraint material to system throughput?"
anti_pattern_candidates:
  - promotional_certainty
  - unsupported_market_share
  - price_target_and_positioning
boundary_candidates:
  - separate_method_expression_from_company_fact
  - no_investment_advice
toc_calibration_relevance:
  - constraint_identification
  - local_bottleneck_vs_system_constraint
  - value_capture_vs_throughput
  - false_chokepoint_filter
case_replay_relevance: candidate primary-expression input for a future approved AXTI/InP replay
confidence: medium on locator and attribution; low on uncorroborated factual claims
limitations:
  - exact publication date requires human confirmation
  - post contains promotional language and self-reported positioning
  - company and industry assertions require independent evidence
allowed_use:
  - human source review
  - provenance and terminology checking
  - candidate method-dimension tagging after approval
disallowed_use:
  - investment advice
  - company conclusion
  - unverified fact reuse
  - automatic methodology distillation
distillation_status: not_approved_draft
reviewer_note: Confirm date, excerpt, source type, and eligibility before any seed-record conversion.
```

### LEAD-003 draft

```yaml
draft_source_id: DRAFT-SR-V10C-LEAD-003
lead_id: LEAD-003
source_type: needs_human_review
author_or_origin: needs_human_review
source_url_or_locator: https://www.reddit.com/r/wallstreetbets/comments/1r7mv0j/raspberry_pi_is_up_40_after_tam_expansion/
platform: Reddit / r/wallstreetbets
published_at: 2026-02-17T23:45:46Z
captured_at: 2026-06-23
acquisition_method: manual review of a publicly accessible deleted-post permalink and surviving comments
permission_basis: public access; no reconstruction or archive of deleted text
excerpt: needs_human_review
excerpt_length_note: Original post body is deleted. A comment-level excerpt must use its own stable permalink and must not be presented as the deleted post.
paraphrase: Surviving context indicates a proposed Raspberry Pi demand-expansion case tied to AI-agent orchestration, with memory pricing, alternative hardware, and materiality as visible counterquestions.
attribution_note: The top-level post author now displays as deleted. Surviving comments labeled u/AleaBito do not by themselves prove the full deleted post's authorship or content.
topic_tags:
  - Raspberry_Pi
  - OpenClaw
  - AI_agent_orchestration
  - demand_materiality
method_dimension_candidates:
  - demand_anchor
  - catalyst_or_earnings_validation
  - value_capture
  - thesis_killer
judgment_rule_candidates:
  - "candidate question: does a new use case create measurable and durable demand?"
  - "candidate question: is a market move supported by disclosed operating evidence?"
anti_pattern_candidates:
  - reconstructing_deleted_source
  - equating_attention_with_material_revenue
  - ignoring_substitutes_and_input_costs
boundary_candidates:
  - deleted_post_requires_original_confirmation
  - comment_record_must_be_separate
  - no_investment_advice
toc_calibration_relevance:
  - system_boundary
  - throughput_definition
  - false_chokepoint_filter
case_replay_relevance: useful only if authorship and a bounded original expression are approved
confidence: high on stable post ID and deletion state; low on post-level attribution and unavailable body
limitations:
  - original body unavailable
  - top-level author unavailable
  - surviving comments are incomplete context
  - causal and market-impact claims are time-sensitive
allowed_use:
  - human locator review
  - deletion and provenance assessment
  - creation of separate comment-level drafts if approved
disallowed_use:
  - reconstructing the deleted post
  - treating comments as the original body
  - methodology distillation
  - investment advice
distillation_status: not_approved_draft
reviewer_note: Confirm timestamp and author from an approved source, then supply a lawful bounded excerpt or reject the post-level draft.
```

### LEAD-004 draft

```yaml
draft_source_id: DRAFT-SR-V10C-LEAD-004
lead_id: LEAD-004
source_type: needs_human_review
author_or_origin: needs_human_review
source_url_or_locator: https://www.reddit.com/r/ValueInvesting/comments/1q8nmlw/vln_robotics_chipmaker_is_fundamentally/
platform: Reddit / r/ValueInvesting
published_at: needs_human_review
captured_at: 2026-06-23
acquisition_method: manual review of a publicly accessible deleted-post permalink and surviving comments
permission_basis: public access; no reconstruction or archive of deleted text
excerpt: needs_human_review
excerpt_length_note: Original post body is deleted. Surviving comments may support separate records only after permalink and attribution review.
paraphrase: Surviving context indicates a valuation-gap thesis using Valens financial data and a dispute over cash, liabilities, debt, margins, and ticker identity, but the original “60%” valuation argument is unavailable.
attribution_note: The top-level post author displays as deleted. Comments labeled u/AleaBito are attributed only as comments, not as a recovered copy of the post.
topic_tags:
  - VLN
  - Valens_Semiconductor
  - valuation
  - financial_statement_verification
method_dimension_candidates:
  - valuation_gap
  - catalyst_or_earnings_validation
  - invalidation_condition
judgment_rule_candidates:
  - "candidate question: are valuation inputs tied to the correct issuer and reporting period?"
  - "candidate question: are debt, liabilities, cash, deposits, and cash burn distinguished?"
anti_pattern_candidates:
  - reconstructing_deleted_source
  - ticker_collision
  - mixing_GAAP_and_non_GAAP
  - treating_headline_valuation_as_verified
boundary_candidates:
  - company_evidence_required_for_financial_claims
  - no_investment_advice
toc_calibration_relevance:
  - value_capture_vs_throughput
  - false_chokepoint_filter
case_replay_relevance: possible future anti-error and valuation-input replay if the original expression is approved
confidence: high on stable post ID and deletion state; low on unavailable post content and exact attribution
limitations:
  - original body unavailable
  - original date and author require confirmation
  - surviving discussion contains conflicting financial interpretations
allowed_use:
  - human provenance review
  - comparison against dated company evidence
  - separate comment-level draft preparation if approved
disallowed_use:
  - recovering or inventing deleted text
  - accepting the valuation conclusion
  - company conclusion
  - investment advice
distillation_status: not_approved_draft
reviewer_note: Confirm authorship/date and decide whether to reject this post-level record in favor of specific surviving comments.
```

### LEAD-018 draft

```yaml
draft_source_id: DRAFT-SR-V10C-LEAD-018
lead_id: LEAD-018
source_type: industry_evidence
author_or_origin: Rob Crangle / U.S. Geological Survey
source_url_or_locator: https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-indium.pdf
platform: U.S. Geological Survey / Mineral Commodity Summaries PDF
published_at: 2026-02
captured_at: 2026-06-23
acquisition_method: manual review of a publicly accessible government PDF
permission_basis: public access; bounded quotation and attributed paraphrase
excerpt: "China is the leading global producer of indium, accounting for 70% of the world total."
excerpt_length_note: 15-word excerpt retained to identify the document's concentration estimate.
paraphrase: USGS reports estimated complete U.S. import reliance, concentrated refinery production, 2025 Chinese export restrictions, and InP uses in optical communications and specialized chip materials.
attribution_note: Government industry evidence only. It is not Serenity expression and does not establish AXT's market share, qualification barriers, or value capture.
topic_tags:
  - indium
  - indium_phosphide
  - import_reliance
  - export_restrictions
  - substitution
method_dimension_candidates:
  - physical_floor_mapping
  - capacity_or_lead_time_constraint
  - substitution_difficulty
  - thesis_killer
judgment_rule_candidates:
  - not_applicable_as_direct_method_evidence
anti_pattern_candidates:
  - mapping_ITO_substitutes_directly_to_InP
  - inferring_company_share_from_national_data
boundary_candidates:
  - industry_evidence_cannot_define_serenity_method
  - no_single_source_company_conclusion
toc_calibration_relevance:
  - CCR_characteristics
  - constraint_identification
  - constraint_migration
  - false_chokepoint_filter
case_replay_relevance: corroborating or contradicting evidence for an approved AXTI/InP replay
confidence: high on provenance and document date; medium on application-level relevance
limitations:
  - data include estimates
  - indium market is broader than InP substrate supply
  - substitutes section focuses mainly on ITO applications
allowed_use:
  - industry premise checking
  - concentration and substitution review
  - corroborating or contradicting case evidence
disallowed_use:
  - Serenity methodology attribution
  - stand-alone AXT conclusion
  - investment advice
distillation_status: not_approved_draft
reviewer_note: Confirm excerpt and approve only as industry evidence.
```

### LEAD-020 draft

```yaml
draft_source_id: DRAFT-SR-V10C-LEAD-020
lead_id: LEAD-020
source_type: company_evidence
author_or_origin: AXT, Inc. / U.S. Securities and Exchange Commission EDGAR
source_url_or_locator: "SEC CIK 1051627; focused accessions 0001437749-26-017054, 0001213900-26-045652, 0001213900-26-045867, 0001213900-26-045643, 0001213900-26-046176"
platform: SEC EDGAR
published_at: multiple_filings_2026-04-20_to_2026-05-14
captured_at: 2026-06-23
acquisition_method: manual review of public SEC company index and filing documents
permission_basis: public regulatory filings; bounded quotation and attributed paraphrase
excerpt: "increase its capacity to produce indium phosphide substrates for export worldwide"
excerpt_length_note: 10-word excerpt from the April 21, 2026 Form 424B5 use-of-proceeds language.
paraphrase: AXT's filings provide dated primary disclosures on its structure, risks, financial condition, guidance, and an equity offering whose stated uses include supporting Tongmei's InP substrate capacity expansion.
attribution_note: Issuer statements filed with the SEC are company evidence. They do not establish Serenity methodology or a complete company conclusion.
topic_tags:
  - AXTI
  - SEC
  - 10-Q
  - 8-K
  - 424B5
  - equity_offering
  - Tongmei
method_dimension_candidates:
  - value_chain_decomposition
  - capacity_or_lead_time_constraint
  - value_capture
  - thesis_killer
  - invalidation_condition
judgment_rule_candidates:
  - not_applicable_as_direct_method_evidence
anti_pattern_candidates:
  - treating_use_of_proceeds_as_completed_capacity
  - ignoring_dilution_and_entity_structure
  - combining_multiple_filings_without_dates
boundary_candidates:
  - split_distinct_filings_into_distinct_records
  - company_evidence_cannot_define_serenity_method
toc_calibration_relevance:
  - elevation_path
  - constraint_release
  - value_capture_vs_throughput
  - false_chokepoint_filter
case_replay_relevance: primary company evidence for future approved financing, capacity, structure, and risk checks
confidence: high on CIK, forms, filing dates, and accession locators; medium on which filing sections should become records
limitations:
  - lead spans several filings and reporting periods
  - forward-looking statements are not completed outcomes
  - issuer disclosure requires section-level context
allowed_use:
  - company disclosure verification
  - financing and risk-factor review
  - corroborating or contradicting case evidence
disallowed_use:
  - Serenity methodology attribution
  - automatic aggregation into one accepted record
  - stand-alone company conclusion
  - investment advice
distillation_status: not_approved_draft
reviewer_note: Select and split approved filing units; verify final 424B5 excerpt and section references.
```

### LEAD-021 draft

```yaml
draft_source_id: DRAFT-SR-V10C-LEAD-021
lead_id: LEAD-021
source_type: company_evidence
author_or_origin: Valens Semiconductor Ltd.
source_url_or_locator: https://s28.q4cdn.com/438644442/files/doc_financials/2025/q3/PR-NYSE_VLN-Q3_25_Web.pdf
platform: Valens investor relations / Q3 2025 press-release PDF
published_at: 2025-11-12
captured_at: 2026-06-23
acquisition_method: manual review of a publicly accessible company IR PDF
permission_basis: public access; bounded quotation and attributed paraphrase
excerpt: "Cash balance as of September 30, 2025, was $93.5 million and no debt."
excerpt_length_note: 14-word excerpt retained to check a central financial claim in the VLN discussion.
paraphrase: Valens reported Q3 2025 revenue of $17.3 million, 63.0% GAAP gross margin, $93.5 million in cash and short-term deposits, no debt, a GAAP net loss, and negative operating cash flow.
attribution_note: Company-reported period data only. The figures do not validate the deleted Reddit post's valuation conclusion.
topic_tags:
  - VLN
  - Q3_2025
  - revenue
  - gross_margin
  - cash
  - liabilities
  - cash_flow
method_dimension_candidates:
  - valuation_gap
  - catalyst_or_earnings_validation
  - invalidation_condition
judgment_rule_candidates:
  - not_applicable_as_direct_method_evidence
anti_pattern_candidates:
  - mixing_cash_with_short_term_deposits
  - equating_no_debt_with_no_liabilities
  - ignoring_net_loss_and_cash_flow
  - mixing_GAAP_and_non_GAAP
boundary_candidates:
  - period_specific_company_evidence
  - no_valuation_conclusion_from_single_release
toc_calibration_relevance:
  - value_capture_vs_throughput
  - false_chokepoint_filter
case_replay_relevance: primary company evidence for checking dated financial inputs in a future approved VLN replay
confidence: high on provenance, date, and reported figures
limitations:
  - issuer-produced release
  - includes non-GAAP measures and forward guidance
  - later quarters may differ
allowed_use:
  - financial datapoint verification
  - support or contradiction of dated case assertions
  - source-type boundary review
disallowed_use:
  - Serenity methodology attribution
  - accepting a valuation conclusion
  - stand-alone company conclusion
  - investment advice
distillation_status: not_approved_draft
reviewer_note: Confirm the excerpt and choose between this release and the corresponding SEC filing as the preferred record.
```

### LEAD-016 draft

```yaml
draft_source_id: DRAFT-SR-V10C-LEAD-016
lead_id: LEAD-016
source_type: public_secondary_analysis
author_or_origin: Adam Clark / Barron's
source_url_or_locator: https://www.barrons.com/articles/axt-stock-price-share-offering-83039818
platform: Barron's
published_at: 2026-04-21
captured_at: 2026-06-23
acquisition_method: manual review of publicly visible page metadata and lead paragraph
permission_basis: public visible access; bounded quotation and attributed paraphrase only
excerpt: "tumbling Tuesday on a stock offering and revenue guidance"
excerpt_length_note: 9-word excerpt from the publicly visible lead; no paywalled article body was copied.
paraphrase: Barron's attributes an AXT share-price decline to an equity offering and guidance update, providing secondary event framing that should be checked against primary SEC filings.
attribution_note: Secondary reporting by Adam Clark. The article does not establish Serenity attribution and is not the primary source for offering terms.
topic_tags:
  - AXTI
  - secondary_coverage
  - equity_offering
  - dilution
  - guidance
method_dimension_candidates:
  - thesis_killer
  - value_capture
  - invalidation_condition
judgment_rule_candidates:
  - not_applicable_as_direct_method_evidence
anti_pattern_candidates:
  - treating_market_reaction_as_operating_proof
  - using_secondary_figures_without_SEC_confirmation
boundary_candidates:
  - secondary_case_coverage_not_serenity_attribution
  - no_paywall_bypass
toc_calibration_relevance:
  - elevation_path
  - value_capture_vs_throughput
  - false_chokepoint_filter
case_replay_relevance: secondary event framing for a future approved AXTI financing and value-capture review
confidence: high on headline and author; medium on date metadata; low on inaccessible article detail
limitations:
  - article body is substantially paywalled
  - does not name or quote Serenity
  - market reaction is time-sensitive
  - terms require SEC confirmation
allowed_use:
  - secondary event context
  - question generation
  - triangulation against SEC filings
disallowed_use:
  - Serenity methodology attribution
  - primary evidence of offering terms
  - full-text storage
  - investment advice
distillation_status: not_approved_draft
reviewer_note: Confirm the date and visible excerpt, then decide whether limited access is sufficient for a secondary-only seed record.
```

## 5. Human review checklist

For each draft, the reviewer only needs to decide:

1. Can the URL or filing locator be opened?
2. Is the author or origin correct?
3. Is the publication date correct?
4. Is the short excerpt accurate and sufficiently bounded?
5. Is the source type correct?
6. May the draft enter seed source records?
7. Must it remain only secondary or corroborating evidence?
8. Should it be excluded?

For LEAD-003 and LEAD-004, the reviewer should additionally decide whether the deleted post-level draft must be rejected and replaced by separately reviewed comment permalinks. No deleted body should be reconstructed.

For LEAD-020, the reviewer should select discrete filing units rather than approve the broad SEC index as one undifferentiated record.

## 6. Recommended next step

After human review, a separately authorized round may create:

`data/seed/source-records/`

That round should convert only explicitly approved drafts into formal source records, preserve reviewer identity and disposition, split multi-filing locators into appropriate record units, and keep rejected or deferred drafts out of seed data. Approval for this packet does not pre-authorize that directory or any formal record.

## 7. Final boundary note

This review packet contains draft records only. It contains no approved corpus entries, no finalized source records, no method claims, no TOC calibration conclusions, no real company conclusions, and no investment advice. It performs no X scraping, no twscrape integration, no secret access, no login-wall bypassing, no full-thread archive, and no bulk copying of third-party text.
