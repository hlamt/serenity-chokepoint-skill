# V1.0J — X Source Record Proposals

## 1. Purpose and boundary

This packet converts a bounded subset of the V1.0I review recommendations into source-record proposals for human review. It does not create approved source records, corpus entries, validated method claims, runtime rules, TOC calibration, company conclusions, or investment advice.

All entries remain proposal-only and not distilled. Visible X text and dates are inherited from the existing review packets; this round did not search, scrape, or independently verify X.

## 2. Source basis

The sole source basis is the repository's existing bounded review material:

- `docs/x-source-lead-review-packet-v1.0h.md`
- `docs/mcc-0003-value-capture-dilution-source-leads-v1.0h-b.md`
- `docs/invalidation-bear-case-risk-source-leads-v1.0h-c.md`
- `docs/x-source-record-review-v1.0i.md`

No X timeline was fetched. No X API, `twscrape`, cookie, session, token, API key, secret, login-wall bypass, or third-party full-text archive was used.

## 3. Selection method

Twelve of the fifteen V1.0I recommended candidates were selected to preserve coverage across:

1. physical supply-chain and capacity mapping;
2. firm-level value capture;
3. shareholder-level value capture and dilution structure;
4. source governance, invalidation, false positives, capacity release, and bypass risk.

Selection favors proposals with a bounded visible expression, a distinct later method use, and explicit human-check requirements. Selection is not approval.

## 4. Proposal summary

### Category coverage

| Category | Proposal count | Proposal IDs |
|---|---:|---|
| Physical mapping | 3 | V10J-PROPOSAL-0001–0003 |
| Firm value capture | 1 | V10J-PROPOSAL-0004 |
| Shareholder value capture | 4 | V10J-PROPOSAL-0005–0008 |
| Risk / invalidation / false-positive controls | 4 | V10J-PROPOSAL-0009–0012 |
| Capacity / constraint-release / bypass relevance | 3 | V10J-PROPOSAL-0002, 0011, 0012 |

The final row is an overlapping secondary classification and is not additive to the twelve proposals.

### Source packet coverage

| Source packet | Proposal count |
|---|---:|
| V1.0H | 2 |
| V1.0H-B | 6 |
| V1.0H-C | 4 |

## 5. Source record proposals

### 5.1 Physical mapping proposals

```yaml
proposal_id: V10J-PROPOSAL-0001
source_review_id: V10I-REVIEW-0001
source_packet: V1.0H
lead_id: XLEAD-AXTI-001
source_url: https://x.com/aleabitoreddit/status/2066823176785457323
author_or_origin: aleabito / X
visible_date: "Jun 16; year not visible in the reviewed capture"
source_basis: Existing bounded V1.0H and V1.0I review material only; no fresh X retrieval or independent verification.
proposal_status: proposed_not_approved
source_record_status: proposal_only
distillation_status: not_distilled
method_claim_status: not_validated
runtime_status: not_runtime_ready
primary_source_role: original_method_expression_candidate
secondary_source_roles:
  - physical_supply_chain_mapping_signal
  - source_governance_signal
  - risk_or_invalidation_signal
  - external_factual_claim_container
related_mcc:
  - MCC-0002
  - MCC-0005
bounded_excerpt_signals:
  - "mapping the InP substrate supply chain"
  - "high purity indium pricing"
  - "Gov publications"
  - "could always be wrong"
  - "devil's advocate on the thesis side"
bounded_paraphrase: The reviewed expression describes mapping an InP substrate chain using analyst material, high-purity indium signals, government publications, supply-shock context, and adversarial review.
source_record_potential: method_expression_and_physical_mapping_source_record_candidate
method_use_if_later_approved:
  - Support a bounded example of multi-source physical supply-chain mapping.
  - Support source-governance language that keeps inference defeasible.
external_factual_claims_to_exclude_or_independently_verify:
  - Company-specific supply-chain claims.
  - Market-share, pricing, Reuters-derived, or position-related claims.
required_human_checks_before_approval:
  - Confirm the exact visible post body and full publication date.
  - Confirm thread context and authorship.
  - Approve a bounded excerpt and separate external facts from original expression.
risk_or_limitation:
  - The reviewed capture does not display the year.
  - The expression mixes method language with externally verifiable factual claims.
not_allowed_uses:
  - not investment advice
  - not company conclusion
  - not approved source record
  - not validated method claim
  - not runtime rule
  - not TOC calibration
recommended_proposal_priority: high
proposal_rationale: Strong candidate for preserving Serenity's public expression of physical mapping and explicit uncertainty, subject to date, context, and factual-claim checks.
```

```yaml
proposal_id: V10J-PROPOSAL-0002
source_review_id: V10I-REVIEW-0002
source_packet: V1.0H
lead_id: XLEAD-AMD-001
source_url: https://x.com/aleabitoreddit/status/2067206734427697196
author_or_origin: aleabito / X
visible_date: "Jun 17; year not visible in the reviewed capture"
source_basis: Existing bounded V1.0H and V1.0I review material only; no fresh X retrieval or independent verification.
proposal_status: proposed_not_approved
source_record_status: proposal_only
distillation_status: not_distilled
method_claim_status: not_validated
runtime_status: not_runtime_ready
primary_source_role: physical_supply_chain_mapping_candidate
secondary_source_roles:
  - capacity_constraint_signal
  - original_method_expression_candidate
  - external_factual_claim_container
related_mcc:
  - MCC-0001
  - MCC-0002
  - MCC-0004
bounded_excerpt_signals:
  - "secure CW laser supply"
  - "multiple major procurement orders"
  - "start of bottleneck?"
  - "independent capacity"
  - "multi-year agreements"
bounded_paraphrase: The reviewed expression frames procurement and multi-year capacity commitments as possible evidence of capacity locking around a physical input.
source_record_potential: physical_mapping_and_capacity_constraint_source_record_candidate
method_use_if_later_approved:
  - Illustrate how procurement behavior may signal a physical constraint.
  - Preserve the question form rather than treating a bottleneck as established.
external_factual_claims_to_exclude_or_independently_verify:
  - Procurement orders, agreements, company capacity, and company-relationship claims.
  - TrendForce-derived or ticker-specific claims.
required_human_checks_before_approval:
  - Confirm exact post text, year, authorship, and thread context.
  - Approve the bounded excerpt.
  - Separate the interpretive signal from all company and industry facts.
risk_or_limitation:
  - Procurement activity is not by itself proof of a durable bottleneck.
  - The reviewed capture does not display the year.
not_allowed_uses:
  - not investment advice
  - not company conclusion
  - not approved source record
  - not validated method claim
  - not runtime rule
  - not TOC calibration
recommended_proposal_priority: high
proposal_rationale: Adds a bounded capacity-locking signal while retaining uncertainty and independent-verification requirements.
```

```yaml
proposal_id: V10J-PROPOSAL-0003
source_review_id: V10I-REVIEW-0007
source_packet: V1.0H-B
lead_id: XLEAD-SIVE-LPK-001
source_url: https://x.com/aleabitoreddit/status/2055822766600016238
author_or_origin: aleabito / X
visible_date: "May 17, 2026; user-provided in the existing packet and not independently verified"
source_basis: Existing bounded V1.0H-B and V1.0I review material only; no fresh X retrieval or independent verification.
proposal_status: proposed_not_approved
source_record_status: proposal_only
distillation_status: not_distilled
method_claim_status: not_validated
runtime_status: not_runtime_ready
primary_source_role: original_method_expression_candidate
secondary_source_roles:
  - physical_supply_chain_mapping_signal
  - firm_value_capture_signal
  - source_governance_signal
  - external_factual_claim_container
related_mcc:
  - MCC-0001
  - MCC-0002
  - MCC-0003
  - MCC-0005
bounded_excerpt_signals:
  - "technical depth"
  - "gross margin expansion"
  - "epiwafer / InP substrate"
  - "value to Western supply chain"
bounded_paraphrase: The reviewed expression links technical depth, photonics-chain mapping, margin potential, vertical integration, and substrate position as distinct analytical layers.
source_record_potential: method_expression_physical_mapping_and_value_capture_source_record_candidate
method_use_if_later_approved:
  - Illustrate separation of technical-chain location from firm-level value capture.
  - Preserve vertical-integration and substrate-position questions for later testing.
external_factual_claims_to_exclude_or_independently_verify:
  - TAM figures, margin claims, company capabilities, portfolio references, and ticker-specific statements.
required_human_checks_before_approval:
  - Confirm exact text, date, authorship, and surrounding context.
  - Approve a bounded excerpt.
  - Separate method expression from TAM and company facts.
risk_or_limitation:
  - Technical mapping and value capture are combined and must not be collapsed into a company conclusion.
  - The date is inherited from user-provided review material.
not_allowed_uses:
  - not investment advice
  - not company conclusion
  - not approved source record
  - not validated method claim
  - not runtime rule
  - not TOC calibration
recommended_proposal_priority: high
proposal_rationale: Useful bridge between physical location and possible value capture, with strong need for factual separation.
```

### 5.2 Firm value capture proposals

```yaml
proposal_id: V10J-PROPOSAL-0004
source_review_id: V10I-REVIEW-0008
source_packet: V1.0H-B
lead_id: XLEAD-PHISON-001
source_url: https://x.com/aleabitoreddit/status/2023323844346618010
author_or_origin: aleabito / X
visible_date: "Feb 16, 2026; visible in the existing reviewed screenshot"
source_basis: Existing bounded V1.0H-B and V1.0I review material only; no fresh X retrieval or independent verification.
proposal_status: proposed_not_approved
source_record_status: proposal_only
distillation_status: not_distilled
method_claim_status: not_validated
runtime_status: not_runtime_ready
primary_source_role: firm_value_capture_candidate
secondary_source_roles:
  - original_method_expression_candidate
  - shareholder_value_capture_signal
  - external_factual_claim_container
related_mcc:
  - MCC-0003
  - MCC-0005
bounded_excerpt_signals:
  - "Toll Collectors"
  - "controller logic/software"
  - "capture massive value"
  - "storage bottleneck not GPUs"
  - "low-margin hardware"
bounded_paraphrase: The reviewed expression distinguishes control-point logic and software from lower-margin hardware when asking where value may be captured.
source_record_potential: firm_value_capture_source_record_candidate
method_use_if_later_approved:
  - Illustrate a toll-collector hypothesis at a control point.
  - Separate chain importance from the identity of the value-capturing layer.
external_factual_claims_to_exclude_or_independently_verify:
  - Named-company, sector-bottleneck, value-capture, and trading claims.
required_human_checks_before_approval:
  - Confirm exact text, date, authorship, and context.
  - Remove or exclude trading language from any approved bounded record.
  - Independently verify sector and company assertions if retained as facts.
risk_or_limitation:
  - Rhetorical value-capture language may overstate evidence.
  - Trading references are outside permitted use.
not_allowed_uses:
  - not investment advice
  - not company conclusion
  - not approved source record
  - not validated method claim
  - not runtime rule
  - not TOC calibration
recommended_proposal_priority: high
proposal_rationale: Provides a compact expression of control-point value capture, bounded away from company and trading conclusions.
```

### 5.3 Shareholder value capture proposals

```yaml
proposal_id: V10J-PROPOSAL-0005
source_review_id: V10I-REVIEW-0013
source_packet: V1.0H-B
lead_id: XLEAD-DILUTION-STRUCTURE-001
source_url: https://x.com/aleabitoreddit/status/2063573828928954442
author_or_origin: aleabito / X
visible_date: "Jun 7, 2026; visible in the existing review packet"
source_basis: Existing bounded V1.0H-B and V1.0I review material only; no fresh X retrieval or independent verification.
proposal_status: proposed_not_approved
source_record_status: proposal_only
distillation_status: not_distilled
method_claim_status: not_validated
runtime_status: not_runtime_ready
primary_source_role: original_method_expression_candidate
secondary_source_roles:
  - shareholder_value_capture_signal
  - source_governance_signal
  - invalidation_signal
  - external_factual_claim_container
related_mcc:
  - MCC-0003
  - MCC-0005
bounded_excerpt_signals:
  - "Not all dilution is bad"
  - "depends on structure"
  - "accretive"
  - "predatory"
  - "ATM build capacity"
  - "toxic debt"
bounded_paraphrase: The reviewed expression proposes evaluating dilution by financing structure and use of proceeds rather than treating all issuance as equivalent.
source_record_potential: shareholder_capture_and_dilution_structure_source_record_candidate
method_use_if_later_approved:
  - Support a bounded distinction between potentially accretive and predatory financing.
  - Require analysis of structure and use of proceeds before shareholder-impact judgment.
external_factual_claims_to_exclude_or_independently_verify:
  - Company examples, financing terms, ATM use, listing, M&A, and debt claims.
required_human_checks_before_approval:
  - Confirm exact text, context, authorship, and date.
  - Approve a bounded excerpt without company examples unless verified.
  - Review whether categorical labels are appropriately qualified.
risk_or_limitation:
  - Accretive or predatory classification requires evidence beyond the expression.
not_allowed_uses:
  - not investment advice
  - not company conclusion
  - not approved source record
  - not validated method claim
  - not runtime rule
  - not TOC calibration
recommended_proposal_priority: high
proposal_rationale: Preserves a central shareholder-capture distinction while keeping classification unvalidated.
```

```yaml
proposal_id: V10J-PROPOSAL-0006
source_review_id: V10I-REVIEW-0015
source_packet: V1.0H-B
lead_id: XLEAD-FINANCING-EQUITY-001
source_url: https://x.com/aleabitoreddit/status/2062119438552572283
author_or_origin: aleabito / X
visible_date: "Jun 3, 2026; visible in the existing review packet"
source_basis: Existing bounded V1.0H-B and V1.0I review material only; no fresh X retrieval or independent verification.
proposal_status: proposed_not_approved
source_record_status: proposal_only
distillation_status: not_distilled
method_claim_status: not_validated
runtime_status: not_runtime_ready
primary_source_role: shareholder_value_capture_candidate
secondary_source_roles:
  - original_method_expression_candidate
  - source_governance_signal
  - external_factual_claim_container
related_mcc:
  - MCC-0003
  - MCC-0005
bounded_excerpt_signals:
  - "financing structure different"
  - "debt interest"
  - "little equity appreciation"
  - "excessive ATMs"
  - "sum parts / ownership"
bounded_paraphrase: The reviewed expression separates enterprise financing outcomes from common-equity appreciation by considering debt, ATM issuance, ownership, and sum-of-parts structure.
source_record_potential: shareholder_capture_financing_structure_source_record_candidate
method_use_if_later_approved:
  - Illustrate why firm growth does not automatically imply per-share appreciation.
  - Preserve financing and ownership structure as a separate analytical layer.
external_factual_claims_to_exclude_or_independently_verify:
  - Company financing, debt, ATM, ownership, and valuation claims.
required_human_checks_before_approval:
  - Confirm the reply context, exact text, date, and authorship.
  - Approve a bounded excerpt.
  - Separate company examples from the general expression.
risk_or_limitation:
  - The expression may rely on omitted conversational context.
not_allowed_uses:
  - not investment advice
  - not company conclusion
  - not approved source record
  - not validated method claim
  - not runtime rule
  - not TOC calibration
recommended_proposal_priority: high
proposal_rationale: Directly addresses the gap between financing structure and shareholder-level outcomes.
```

```yaml
proposal_id: V10J-PROPOSAL-0007
source_review_id: V10I-REVIEW-0020
source_packet: V1.0H-B
lead_id: XLEAD-CPO-PRICING-001
source_url: https://x.com/aleabitoreddit/status/2054412992000012555
author_or_origin: aleabito / X
visible_date: "May 13, 2026; visible in the existing review packet"
source_basis: Existing bounded V1.0H-B and V1.0I review material only; no fresh X retrieval or independent verification.
proposal_status: proposed_not_approved
source_record_status: proposal_only
distillation_status: not_distilled
method_claim_status: not_validated
runtime_status: not_runtime_ready
primary_source_role: shareholder_value_capture_candidate
secondary_source_roles:
  - original_method_expression_candidate
  - capacity_constraint_signal
  - external_factual_claim_container
related_mcc:
  - MCC-0003
  - MCC-0004
  - MCC-0005
bounded_excerpt_signals:
  - "Markets don't know yet"
  - "valuation priced in"
  - "rerating potential less"
  - "markets price 8–12 months"
bounded_paraphrase: The reviewed expression asks how exposure type, legacy revenue, cannibalization, starting valuation, and a forward pricing window affect shareholder capture.
source_record_potential: shareholder_capture_and_priced_in_risk_source_record_candidate
method_use_if_later_approved:
  - Preserve starting valuation and priced-in expectations as shareholder-level checks.
  - Separate physical exposure from the remaining scope for rerating.
external_factual_claims_to_exclude_or_independently_verify:
  - Company exposure, revenue, cannibalization, valuation, timing-window, and alpha claims.
required_human_checks_before_approval:
  - Confirm exact text, context, date, and authorship.
  - Approve a bounded excerpt.
  - Separate company-specific and market-efficiency assertions.
risk_or_limitation:
  - The stated market-pricing window is an external empirical claim, not an accepted rule.
not_allowed_uses:
  - not investment advice
  - not company conclusion
  - not approved source record
  - not validated method claim
  - not runtime rule
  - not TOC calibration
recommended_proposal_priority: medium
proposal_rationale: Adds a necessary priced-in boundary between business relevance and shareholder appreciation.
```

```yaml
proposal_id: V10J-PROPOSAL-0008
source_review_id: V10I-REVIEW-0026
source_packet: V1.0H-B
lead_id: XLEAD-ATM-SHAREHOLDER-001
source_url: https://x.com/aleabitoreddit/status/2030733860607250833
author_or_origin: aleabito / X
visible_date: needs_human_review
source_basis: Existing bounded V1.0H-B and V1.0I review material only; no fresh X retrieval or independent verification.
proposal_status: proposed_not_approved
source_record_status: proposal_only
distillation_status: not_distilled
method_claim_status: not_validated
runtime_status: not_runtime_ready
primary_source_role: shareholder_value_capture_candidate
secondary_source_roles:
  - original_method_expression_candidate
  - invalidation_signal
  - external_factual_claim_container
related_mcc:
  - MCC-0003
  - MCC-0005
bounded_excerpt_signals:
  - "ATM wipes current shareholder value"
  - "better for company"
bounded_paraphrase: The reviewed expression distinguishes a financing action that may benefit the company from its possible effect on current shareholders.
source_record_potential: company_benefit_versus_shareholder_value_source_record_candidate
method_use_if_later_approved:
  - Preserve the company-benefit versus current-shareholder-effect distinction.
  - Add a dilution-related invalidation check to shareholder capture.
external_factual_claims_to_exclude_or_independently_verify:
  - Company financing, ATM impact, and shareholder-value claims.
required_human_checks_before_approval:
  - Confirm exact post text, full date, authorship, and context.
  - Review categorical wording and approve a bounded excerpt.
  - Separate any company example from the general distinction.
risk_or_limitation:
  - The date is unresolved.
  - The visible wording is categorical and may omit financing-specific context.
not_allowed_uses:
  - not investment advice
  - not company conclusion
  - not approved source record
  - not validated method claim
  - not runtime rule
  - not TOC calibration
recommended_proposal_priority: high
proposal_rationale: Captures a core shareholder boundary, but requires especially careful context and wording review.
```

### 5.4 Risk and invalidation proposals

```yaml
proposal_id: V10J-PROPOSAL-0009
source_review_id: V10I-REVIEW-0029
source_packet: V1.0H-C
lead_id: XLEAD-DISCRETIONARY-INFERENCE-001
source_url: https://x.com/aleabitoreddit/status/2063465386960736396
author_or_origin: aleabito / X
visible_date: "Jun 7, 2026; visible in the existing review packet"
source_basis: Existing bounded V1.0H-C and V1.0I review material only; no fresh X retrieval or independent verification.
proposal_status: proposed_not_approved
source_record_status: proposal_only
distillation_status: not_distilled
method_claim_status: not_validated
runtime_status: not_runtime_ready
primary_source_role: source_governance_candidate
secondary_source_roles:
  - risk_or_invalidation_signal
  - original_method_expression_candidate
  - external_factual_claim_container
related_mcc:
  - MCC-0001
  - MCC-0002
  - MCC-0003
  - MCC-0005
bounded_excerpt_signals:
  - "inherently discretionary"
  - "guessing unstructured relationships"
  - "seeing if right later"
  - "LLM hallucinate"
  - "high conviction inference"
  - "could be wrong"
bounded_paraphrase: The reviewed expression characterizes relationship mapping as discretionary inference that should remain falsifiable and be checked against later evidence.
source_record_potential: source_governance_and_invalidation_source_record_candidate
method_use_if_later_approved:
  - Support explicit labeling of inference, uncertainty, and future validation.
  - Guard against presenting generated relationships as established facts.
external_factual_claims_to_exclude_or_independently_verify:
  - All company examples and asserted real-world relationships.
  - Any generalized claim about LLM behavior presented as empirical fact.
required_human_checks_before_approval:
  - Confirm the exact long-form body, context, date, and authorship.
  - Approve a bounded excerpt that preserves uncertainty.
  - Separate examples from the source-governance expression.
risk_or_limitation:
  - Acknowledging uncertainty does not itself make an inference reliable.
not_allowed_uses:
  - not investment advice
  - not company conclusion
  - not approved source record
  - not validated method claim
  - not runtime rule
  - not TOC calibration
recommended_proposal_priority: high
proposal_rationale: Strong boundary source for discretionary inference, falsifiability, and hallucination risk.
```

```yaml
proposal_id: V10J-PROPOSAL-0010
source_review_id: V10I-REVIEW-0032
source_packet: V1.0H-C
lead_id: XLEAD-PCB-FALSE-POSITIVE-001
source_url: https://x.com/aleabitoreddit/status/2037085574813942094
author_or_origin: aleabito / X
visible_date: "Mar 26, 2026; visible in the existing review packet"
source_basis: Existing bounded V1.0H-C and V1.0I review material only; no fresh X retrieval or independent verification.
proposal_status: proposed_not_approved
source_record_status: proposal_only
distillation_status: not_distilled
method_claim_status: not_validated
runtime_status: not_runtime_ready
primary_source_role: risk_or_invalidation_candidate
secondary_source_roles:
  - original_method_expression_candidate
  - firm_value_capture_signal
  - capacity_constraint_release_signal
  - external_factual_claim_container
related_mcc:
  - MCC-0001
  - MCC-0003
  - MCC-0004
  - MCC-0005
bounded_excerpt_signals:
  - "second optical bottleneck"
  - "downstream benefit less"
  - "company too large"
  - "capacity expansion eases"
  - "could be wrong"
  - "laser more compelling"
bounded_paraphrase: The reviewed expression compares stronger and weaker bottleneck candidates using beneficiary quality, company mix, downstream exposure, and the possibility that capacity expansion eases the constraint.
source_record_potential: false_positive_and_beneficiary_quality_source_record_candidate
method_use_if_later_approved:
  - Support false-positive checks after a physical bottleneck is identified.
  - Preserve beneficiary quality and capacity easing as separate invalidation dimensions.
external_factual_claims_to_exclude_or_independently_verify:
  - Company size, mix, exposure, capacity, bottleneck, and comparative-attractiveness claims.
required_human_checks_before_approval:
  - Confirm exact text, quotation context, date, and authorship.
  - Approve a bounded excerpt.
  - Separate company and capacity facts from the analytical comparison.
risk_or_limitation:
  - Comparative language can be mistaken for a company ranking or investment conclusion.
not_allowed_uses:
  - not investment advice
  - not company conclusion
  - not approved source record
  - not validated method claim
  - not runtime rule
  - not TOC calibration
recommended_proposal_priority: high
proposal_rationale: Adds a valuable false-positive control between bottleneck detection and beneficiary quality.
```

```yaml
proposal_id: V10J-PROPOSAL-0011
source_review_id: V10I-REVIEW-0036
source_packet: V1.0H-C
lead_id: XLEAD-CAPACITY-BEAR-001
source_url: https://x.com/aleabitoreddit/status/2023738495903351200
author_or_origin: aleabito / X
visible_date: "Feb 17, 2026; visible in the existing review packet"
source_basis: Existing bounded V1.0H-C and V1.0I review material only; no fresh X retrieval or independent verification.
proposal_status: proposed_not_approved
source_record_status: proposal_only
distillation_status: not_distilled
method_claim_status: not_validated
runtime_status: not_runtime_ready
primary_source_role: risk_or_invalidation_candidate
secondary_source_roles:
  - capacity_constraint_signal
  - original_method_expression_candidate
  - external_factual_claim_container
related_mcc:
  - MCC-0001
  - MCC-0004
  - MCC-0005
bounded_excerpt_signals:
  - "biggest question / bear case"
  - "no answer"
  - "scale capacity"
  - "memory shortages upstream"
  - "next earnings"
  - "backlog"
bounded_paraphrase: The reviewed expression identifies unresolved scale capacity and upstream shortages as a bear case to be tested against later operating evidence.
source_record_potential: capacity_scale_up_bear_case_source_record_candidate
method_use_if_later_approved:
  - Preserve unresolved capacity scale-up as an explicit invalidation question.
  - Link a hypothesis to future evidence without claiming the future result.
external_factual_claims_to_exclude_or_independently_verify:
  - Capacity, shortage, earnings, backlog, and company-specific claims.
required_human_checks_before_approval:
  - Confirm exact text, context, date, and authorship.
  - Approve a bounded excerpt.
  - Separate factual premises from the unresolved-question structure.
risk_or_limitation:
  - A future checkpoint is not evidence until the relevant data exists and is reviewed.
not_allowed_uses:
  - not investment advice
  - not company conclusion
  - not approved source record
  - not validated method claim
  - not runtime rule
  - not TOC calibration
recommended_proposal_priority: high
proposal_rationale: Strong candidate for encoding a capacity-scale bear question and later-validation discipline.
```

```yaml
proposal_id: V10J-PROPOSAL-0012
source_review_id: V10I-REVIEW-0037
source_packet: V1.0H-C
lead_id: XLEAD-VERTICAL-INTEGRATION-RISK-001
source_url: https://x.com/aleabitoreddit/status/2019315806245646768
author_or_origin: aleabito / X
visible_date: "Feb 5, 2026; visible in the existing review packet"
source_basis: Existing bounded V1.0H-C and V1.0I review material only; no fresh X retrieval or independent verification.
proposal_status: proposed_not_approved
source_record_status: proposal_only
distillation_status: not_distilled
method_claim_status: not_validated
runtime_status: not_runtime_ready
primary_source_role: risk_or_invalidation_candidate
secondary_source_roles:
  - capacity_bypass_signal
  - firm_value_capture_signal
  - external_factual_claim_container
related_mcc:
  - MCC-0003
  - MCC-0004
  - MCC-0005
bounded_excerpt_signals:
  - "downside risk"
  - "creating own sensors"
  - "vertically integrating away"
  - "bear case"
  - "risk management"
bounded_paraphrase: The reviewed expression treats customer self-supply and vertical integration as a possible bypass that may reduce supplier value capture.
source_record_potential: customer_vertical_integration_bypass_source_record_candidate
method_use_if_later_approved:
  - Support explicit testing of customer bypass and self-supply risk.
  - Separate a physical constraint from durable supplier capture.
external_factual_claims_to_exclude_or_independently_verify:
  - Customer-supplier relationships, sensor development, integration plans, and company-impact claims.
required_human_checks_before_approval:
  - Confirm exact text, context, date, and authorship.
  - Approve a bounded excerpt.
  - Independently verify all relationship and integration facts if retained.
risk_or_limitation:
  - A possible bypass path is not evidence that integration will occur or succeed.
not_allowed_uses:
  - not investment advice
  - not company conclusion
  - not approved source record
  - not validated method claim
  - not runtime rule
  - not TOC calibration
recommended_proposal_priority: high
proposal_rationale: Preserves a central bypass mechanism that can invalidate durable supplier capture.
```

## 6. Not selected

The following V1.0I recommended candidates were not converted in this round:

| Source review ID | Disposition | Reason |
|---|---|---|
| V10I-REVIEW-0014 | covered_by_selected_proposal | Toxic-financing and float-dynamics signals substantially overlap the selected dilution-structure, financing-equity, and company-versus-shareholder proposals. |
| V10I-REVIEW-0016 | reserve_for_later_source_record_proposal | Capacity-monetization dilution remains relevant, but the selected set already covers capacity and dilution separately; a later record can test whether the combined expression adds distinct bounded value. |
| V10I-REVIEW-0030 | covered_by_selected_proposal | Public-information uncertainty is represented by the selected discretionary-inference proposal, while the selected SIVE-LPK proposal preserves the physical/value-chain expression requiring factual separation. |

Non-selection is not rejection and does not approve or disapprove the underlying source.

## 7. Remaining human checks

Before any proposal can become an approved source record, a human reviewer must:

1. confirm exact visible text, authorship, full date, URL, and relevant reply/thread context;
2. approve a minimal bounded excerpt;
3. distinguish original expression from external factual claims;
4. independently verify any external factual claim proposed for retention;
5. remove trading language, portfolio references, company conclusions, and investment implications;
6. confirm permission and attribution treatment;
7. decide whether the proposal adds distinct evidentiary value without duplicating an existing record;
8. record approval explicitly rather than inferring it from inclusion in this packet.

## 8. Boundary preservation

This packet:

- does not search or scrape X;
- does not use `twscrape` or the X API;
- does not read cookies, sessions, tokens, API keys, or secrets;
- does not bypass a login wall;
- does not archive complete posts, threads, timelines, or third-party articles;
- does not claim independent verification of X content;
- does not create approved source records or files under `data/seed/`;
- does not create a corpus or distill any proposal;
- does not validate method claims;
- does not produce TOC calibration or runtime rules;
- does not produce company conclusions or investment advice.

## 9. Recommended next step

The recommended next round is:

**V1.0K — Bounded Source Record File Creation**

That round should:

1. create actual source-record files only for proposals that pass explicit manual approval;
2. not auto-convert every proposal;
3. preserve `not_distilled` status;
4. consider a bounded set of only 6–10 approved records;
5. retain independent-verification and prohibited-use boundaries in every record.

## 10. Final boundary note

These twelve entries are source-record proposals only. They are not approved source records, validated method claims, runtime rules, TOC calibration conclusions, company conclusions, or investment advice. No proposal enters distillation through this document.
