# Method Claim Review from Distilled Notes — V1.0M

## 1. Purpose and boundary

This document reviews the five V1.0L distilled method notes and proposes five candidate method claims for later review. Promotion here means entry into a candidate-claim review layer only.

Every claim remains unvalidated, not runtime-ready, and not TOC-calibrated. This round changes no existing MCC document, modifies no source record or `SKILL.md` behavior, reaches no real-company conclusion, and provides no investment advice.

## 2. Source basis

The review uses only:

- V1.0L method notes `MN-V10L-0001` through `MN-V10L-0005`;
- bounded source records `SR-V10K-0001` through `SR-V10K-0010`; and
- the existing MCC candidate and review documents for status and wording boundaries.

Raw X leads, screenshots, complete X posts, uncreated source records, and external factual assertions are not claim-review inputs. Source-record factual exclusions and remaining human checks continue to apply.

## 3. Review method

Each method note was reviewed for:

1. traceability to bounded source records;
2. wording narrowness and falsifiability;
3. separation of hypothesis, fact, firm capture, and shareholder capture;
4. source-governance and external-verification boundaries;
5. additional source-record needs;
6. TOC system-boundary or active-constraint questions; and
7. future runtime-design issues.

The review may promote a note to a candidate claim while simultaneously requiring more sources, TOC calibration review, or later runtime design. Those requirements prevent promotion from being mistaken for validation or operational approval.

## 4. Candidate claim review summary

| candidate claim | source note | proposed wording short name | disposition | status | next action |
| --- | --- | --- | --- | --- | --- |
| MCR-V10M-0001 | MN-V10L-0001 | Physical mapping as hypothesis formation | promote; TOC review; later runtime review | candidate_not_validated | send_to_toc_calibration_review |
| MCR-V10M-0002 | MN-V10L-0002 | Firm value-capture separation | promote; more sources; later runtime review | candidate_not_validated | hold_for_more_source_records |
| MCR-V10M-0003 | MN-V10L-0003 | Shareholder-capture boundary | promote; more sources; later runtime review | candidate_not_validated | hold_for_more_source_records |
| MCR-V10M-0004 | MN-V10L-0004 | Inference discipline and source governance | promote; later runtime review | candidate_not_validated | carry_to_v1.0n_method_claim_registry |
| MCR-V10M-0005 | MN-V10L-0005 | False-positive and invalidation control | promote; TOC review; later runtime review | candidate_not_validated | send_to_toc_calibration_review |

## 5. Candidate method claim reviews

### MCR-V10M-0001｜Physical mapping as hypothesis formation

```yaml
candidate_claim_id: MCR-V10M-0001
source_method_note_id: MN-V10L-0001
candidate_claim_title: Physical mapping as hypothesis formation
candidate_claim_status: candidate_not_validated
method_claim_status: not_validated
runtime_status: not_runtime_ready
toc_calibration_status: not_started
investment_advice_status: prohibited
source_basis: bounded_source_records_and_distilled_notes_only
source_record_ids:
  - SR-V10K-0001
  - SR-V10K-0002
  - SR-V10K-0003
related_mcc:
  - MCC-0001
  - MCC-0002
  - MCC-0004
  - MCC-0005
candidate_claim_wording: "Physical supply-chain mapping can generate a chokepoint hypothesis by tracing substrates, components, procurement behavior, supply relationships, qualification, and capacity commitments; however, this mapping remains hypothesis formation and does not by itself prove a durable system constraint."
review_disposition:
  - promote_to_candidate_method_claim
  - requires_toc_calibration_review
  - requires_runtime_design_review_later
claim_strength: candidate_requires_toc_calibration
claim_boundary:
  - "Physical mapping, procurement, and chain location are not proof of an active constraint."
  - "Company, capacity, relationship, pricing, and market-share facts remain independently unverified."
  - "A system boundary and throughput effect must be defined before constraint language is strengthened."
what_this_claim_allows:
  - "Carry a falsifiable physical-mapping candidate into later claim review."
  - "Generate scarcity, substitution, qualification, throughput, and system-boundary tests."
what_this_claim_does_not_allow:
  - "Declare a durable system constraint."
  - "Validate MCC-0001, MCC-0002, MCC-0004, or MCC-0005."
  - "Produce a company conclusion, runtime rule, TOC calibration, or investment advice."
required_future_review:
  - "TOC system-boundary review."
  - "Active-constraint evidence review."
  - "Capacity, substitution, qualification, and throughput evidence review."
  - "Runtime design review later."
runtime_policy: "Not runtime-ready; active-constraint tests and evidence thresholds are unresolved."
toc_calibration_policy: "Requires a separate TOC review before any constraint terminology or operational test is approved."
investment_advice_policy: "Prohibited; no security selection, target price, position, or trade follows."
open_questions:
  - "What observable evidence distinguishes a mapped dependency from the active system constraint?"
  - "What stopping rule governs physical tracing?"
  - "Which substitution or capacity evidence would falsify the hypothesis?"
recommended_next_action: send_to_toc_calibration_review
```

### MCR-V10M-0002｜Firm value-capture separation

```yaml
candidate_claim_id: MCR-V10M-0002
source_method_note_id: MN-V10L-0002
candidate_claim_title: Firm value-capture separation
candidate_claim_status: candidate_not_validated
method_claim_status: not_validated
runtime_status: not_runtime_ready
toc_calibration_status: not_started
investment_advice_status: prohibited
source_basis: bounded_source_records_and_distilled_notes_only
source_record_ids:
  - SR-V10K-0003
  - SR-V10K-0004
related_mcc:
  - MCC-0003
  - MCC-0005
candidate_claim_wording: "A firm's participation in a chokepoint-relevant layer does not automatically imply firm-level value capture; firm-level capture must be separately tested through control point, technical depth, margin structure, integration position, bargaining power, and where economics actually accrue."
review_disposition:
  - promote_to_candidate_method_claim
  - requires_more_source_records_before_claim
  - requires_runtime_design_review_later
claim_strength: candidate_supported_but_needs_more_sources
claim_boundary:
  - "Chain importance and technical depth do not establish pricing power or realized economics."
  - "Firm-level capture remains separate from shareholder capture."
  - "Company and financial facts remain outside this claim."
what_this_claim_allows:
  - "Carry a bounded separation between physical participation and firm economics into later review."
  - "Generate evidence questions about control, margins, integration, bargaining power, and economic accrual."
what_this_claim_does_not_allow:
  - "Conclude that any firm captures disproportionate value."
  - "Treat toll-collector language as evidence."
  - "Create a validated method claim, runtime rule, TOC calibration, company conclusion, or investment advice."
required_future_review:
  - "Additional non-X or independently verified source records."
  - "Company-fact exclusion review."
  - "Value-capture evidence standard review."
  - "Runtime design review later."
runtime_policy: "Not runtime-ready; firm-level value-capture evidence standards and display rules remain unresolved."
toc_calibration_policy: "No TOC calibration is performed; whether firm capture is inside or outside TOC analysis requires later review."
investment_advice_policy: "Prohibited; the claim cannot support company, sector, asset, or security selection."
open_questions:
  - "What observable evidence demonstrates control and retained economics?"
  - "How should margins, bargaining power, capital intensity, and integration be tested across cases?"
  - "What counterexamples show technical importance without firm capture?"
recommended_next_action: hold_for_more_source_records
```

### MCR-V10M-0003｜Shareholder-capture boundary

```yaml
candidate_claim_id: MCR-V10M-0003
source_method_note_id: MN-V10L-0003
candidate_claim_title: Shareholder-capture boundary
candidate_claim_status: candidate_not_validated
method_claim_status: not_validated
runtime_status: not_runtime_ready
toc_calibration_status: not_started
investment_advice_status: prohibited
source_basis: bounded_source_records_and_distilled_notes_only
source_record_ids:
  - SR-V10K-0005
  - SR-V10K-0006
  - SR-V10K-0007
  - SR-V10K-0008
related_mcc:
  - MCC-0003
  - MCC-0004
  - MCC-0005
candidate_claim_wording: "Operating value, firm-level benefit, or capacity monetization does not automatically become common-shareholder value; shareholder capture must be separately reviewed through dilution structure, financing quality, equity-appreciation path, priced-in timing, and whether upside is structurally capped."
review_disposition:
  - promote_to_candidate_method_claim
  - requires_more_source_records_before_claim
  - requires_runtime_design_review_later
claim_strength: candidate_supported_but_needs_more_sources
claim_boundary:
  - "Company benefit is not current-shareholder benefit."
  - "Dilution is not categorically good or bad."
  - "No market-pricing window, equity appreciation, or financing effect is established."
what_this_claim_allows:
  - "Carry the separation of operating, firm, and common-shareholder outcomes into later method review."
  - "Generate financing, dilution, ownership, valuation, and timing evidence questions."
what_this_claim_does_not_allow:
  - "Classify a financing or forecast shareholder returns."
  - "Produce a target price, trade, or company conclusion."
  - "Create a validated method claim, runtime rule, TOC calibration, or investment advice."
required_future_review:
  - "Investment-adjacent language review."
  - "External financial fact verification."
  - "Financing-structure evidence standard review."
  - "Strict no-investment-advice runtime boundary."
runtime_policy: "Not runtime-ready; financial evidence standards and recommendation safeguards require explicit design."
toc_calibration_policy: "No TOC calibration is performed; shareholder capture may remain an external investment-analysis overlay."
investment_advice_policy: "Prohibited; no buy, sell, hold, long, short, target price, sizing, timing, or return expectation is allowed."
open_questions:
  - "What evidence connects operating value to per-share outcomes?"
  - "How should dilution, financing quality, and use of proceeds be reviewed without categorical shortcuts?"
  - "What independently verified records can support a stronger claim review?"
recommended_next_action: hold_for_more_source_records
```

### MCR-V10M-0004｜Inference discipline and source governance

```yaml
candidate_claim_id: MCR-V10M-0004
source_method_note_id: MN-V10L-0004
candidate_claim_title: Inference discipline and source governance
candidate_claim_status: candidate_not_validated
method_claim_status: not_validated
runtime_status: not_runtime_ready
toc_calibration_status: not_started
investment_advice_status: prohibited
source_basis: bounded_source_records_and_distilled_notes_only
source_record_ids:
  - SR-V10K-0001
  - SR-V10K-0009
related_mcc:
  - MCC-0002
  - MCC-0005
candidate_claim_wording: "Source-led chokepoint research must separate original source expression, inference, external factual claims, and later analysis; high-conviction inference must remain falsifiable and cannot be promoted into validated method or factual correctness without independent review."
review_disposition:
  - promote_to_candidate_method_claim
  - requires_runtime_design_review_later
claim_strength: candidate_supported_as_governance_rule_only
claim_boundary:
  - "A source record does not validate facts or method."
  - "Confidence and uncertainty language are not evidence."
  - "External factual claims retain independent-verification requirements."
what_this_claim_allows:
  - "Carry a source-role and inference-separation governance candidate into the registry."
  - "Generate traceability, attribution, falsification, and evidence-display requirements."
what_this_claim_does_not_allow:
  - "Treat a public expression as validated methodology or factual proof."
  - "Remove source limitations or human checks."
  - "Create a validated method claim, runtime rule, TOC calibration, company conclusion, or investment advice."
required_future_review:
  - "Source-governance policy review."
  - "Claim-to-source traceability review."
  - "Runtime evidence-display design later."
runtime_policy: "Not runtime-ready; claim-to-source display, uncertainty, and evidence-role behavior require explicit design and approval."
toc_calibration_policy: "No TOC calibration is performed; this is reviewed as a governance candidate rather than a TOC claim."
investment_advice_policy: "Prohibited; provenance or confidence signals cannot support investment recommendations."
open_questions:
  - "Which claim types require which source roles and corroboration?"
  - "How should runtime output distinguish source expression, inference, fact, and analysis?"
  - "Which governance controls belong in corpus policy versus method policy?"
recommended_next_action: carry_to_v1.0n_method_claim_registry
```

### MCR-V10M-0005｜False-positive and invalidation control

```yaml
candidate_claim_id: MCR-V10M-0005
source_method_note_id: MN-V10L-0005
candidate_claim_title: False-positive and invalidation control
candidate_claim_status: candidate_not_validated
method_claim_status: not_validated
runtime_status: not_runtime_ready
toc_calibration_status: not_started
investment_advice_status: prohibited
source_basis: bounded_source_records_and_distilled_notes_only
source_record_ids:
  - SR-V10K-0002
  - SR-V10K-0003
  - SR-V10K-0008
  - SR-V10K-0010
related_mcc:
  - MCC-0001
  - MCC-0003
  - MCC-0004
  - MCC-0005
candidate_claim_wording: "A downstream beneficiary, adjacent participant, local shortage, or temporarily tight capacity is not automatically the active system constraint; a chokepoint hypothesis must test false positives, capacity release, substitution, bypass, and whether value capture persists after the constraint shifts."
review_disposition:
  - promote_to_candidate_method_claim
  - requires_toc_calibration_review
  - requires_runtime_design_review_later
claim_strength: candidate_requires_toc_calibration
claim_boundary:
  - "Beneficiary is not constraint."
  - "Local bottleneck and temporary shortage are not durable system constraints."
  - "Capacity expansion, substitution, or bypass may release or move the constraint."
what_this_claim_allows:
  - "Carry false-positive and invalidation questions into later claim and TOC review."
  - "Generate release, substitution, bypass, persistence, and beneficiary-quality tests."
what_this_claim_does_not_allow:
  - "Rank companies or identify a preferred beneficiary."
  - "Treat temporary tightness or local scarcity as proof."
  - "Create a validated method claim, runtime rule, TOC calibration, company conclusion, or investment advice."
required_future_review:
  - "TOC active-constraint calibration."
  - "False-positive test design."
  - "Constraint-release, substitution, and bypass evidence review."
  - "Runtime checklist design later."
runtime_policy: "Not runtime-ready; no automatic rejection, scoring, ranking, or checklist has been approved."
toc_calibration_policy: "Requires separate calibration of active constraint, local bottleneck, release, elevation, and constraint movement."
investment_advice_policy: "Prohibited; the claim cannot rank beneficiaries or support security selection."
open_questions:
  - "What evidence distinguishes a temporary local bottleneck from the active system constraint?"
  - "Which milestones establish release, substitution, bypass, or constraint migration?"
  - "How should capture be retested after the constraint changes?"
recommended_next_action: send_to_toc_calibration_review
```

## 6. Relationship to existing MCCs

V1.0M creates five reviewed candidate method claims from V1.0L method notes. It strengthens candidate-level support for MCC-0001 through MCC-0005, but validates none of them and does not alter existing MCC documents.

| Existing MCC | V1.0M relationship | Status after V1.0M |
| --- | --- | --- |
| MCC-0001 | Supported by MCR-V10M-0001 and MCR-V10M-0005 as physical mapping / false-positive candidate logic | not_validated |
| MCC-0002 | Supported by MCR-V10M-0001 and MCR-V10M-0004 as physical mapping / source-governance candidate logic | not_validated |
| MCC-0003 | Supported by MCR-V10M-0002, MCR-V10M-0003, and MCR-V10M-0005 as value-capture / shareholder-capture / invalidation candidate logic | not_validated |
| MCC-0004 | Supported by MCR-V10M-0001, MCR-V10M-0003, and MCR-V10M-0005 as capacity, release, substitution, and bypass review logic | not_validated / not_runtime_ready |
| MCC-0005 | Supported by all five MCR items as source-governance, boundary, and overclaim-control logic | not_validated |

## 7. Method claim boundary matrix

| candidate claim | allowed later use | not allowed use | required future review |
| --- | --- | --- | --- |
| MCR-V10M-0001 | Candidate physical-mapping and active-constraint evidence review. | Validated method claim; runtime rule; TOC calibration; company conclusion; investment advice. | TOC system boundary, active constraint, capacity, substitution, qualification, and runtime design. |
| MCR-V10M-0002 | Candidate firm-capture evidence-standard review. | Validated method claim; runtime rule; TOC calibration; company conclusion; investment advice. | More independently verified records, control-point evidence, economics, and runtime design. |
| MCR-V10M-0003 | Candidate shareholder-capture boundary review. | Validated method claim; runtime rule; TOC calibration; company conclusion; investment advice. | More financial records, financing standards, investment-adjacent safeguards, and runtime design. |
| MCR-V10M-0004 | Candidate source-governance and traceability policy review. | Validated method claim; runtime rule; TOC calibration; company conclusion; investment advice. | Claim-to-source policy, evidence display, uncertainty treatment, and runtime design. |
| MCR-V10M-0005 | Candidate false-positive and invalidation test review. | Validated method claim; runtime rule; TOC calibration; company conclusion; investment advice. | TOC active-constraint calibration, release/substitution/bypass tests, and runtime checklist design. |

## 8. Claims not ready for runtime

None of the V1.0M candidate claims are runtime-ready. They may become inputs to future runtime design only after additional method review, TOC calibration review where relevant, and explicit V1.1 runtime approval.

- **MCR-V10M-0001:** active-constraint tests and system-boundary criteria remain unresolved.
- **MCR-V10M-0002:** firm-level value-capture evidence standards remain unresolved.
- **MCR-V10M-0003:** financial and investment-adjacent boundaries require stricter review.
- **MCR-V10M-0004:** source-governance display and claim-to-source policy require design review.
- **MCR-V10M-0005:** false-positive, release, substitution, and bypass tests require TOC calibration and runtime design.

## 9. Claims requiring more sources

MCR-V10M-0002 and MCR-V10M-0003 require additional non-X or independently verified source records before stronger claim review.

MCR-V10M-0001 and MCR-V10M-0005 require TOC calibration and evidence-test design before runtime.

MCR-V10M-0004 can proceed as a governance candidate but still requires runtime policy design before use.

Additional records do not automatically validate a claim. They must retain provenance, source roles, factual-verification boundaries, counterevidence, and separate review.

## 10. What remains outside method claim layer

- company-specific conclusions
- ticker conclusions
- market-share claims
- capacity figures
- customer/supplier relationship claims
- pricing claims
- valuation claims
- TAM claims
- financing terms
- target prices
- long/short calls
- portfolio references
- investment recommendations
- runtime rules
- TOC calibration claims
- final Chokepoint Theory

Factual verification, security selection, company ranking, return expectations, and any assertion that a specific dependency is the active constraint also remain outside the method claim layer.

## 11. Recommended next step

The recommended next round is **V1.0N — Candidate Method Claim Registry and Review Queue**.

V1.0N should:

1. create a registry of V1.0M candidate method claims;
2. preserve every claim as `not_validated`;
3. mark which claims require more source records;
4. mark which claims require TOC calibration review;
5. mark which claims may later feed V1.1 runtime design; and
6. avoid `SKILL.md` or runtime changes.

The project should not jump directly to V1.1 before V1.0N is completed.

## 12. Final boundary note

This document reviews candidate method claims from V1.0L distilled method notes only. It validates no method claims, changes no existing MCC document, performs no TOC calibration, approves no runtime rules, modifies no SKILL.md behavior, reaches no real-company conclusions, and provides no investment advice.
