# Method Distillation and Boundary Update — V1.0L

## 1. Purpose and boundary

This document distills five method notes from the ten approved bounded seed source records created in V1.0K. The notes organize recurring analytical signals and boundaries for later method review.

They are distilled notes, not validated method claims. This round does not perform TOC calibration, approve runtime rules, update `SKILL.md`, establish a final Chokepoint Theory, reach real-company conclusions, or provide investment advice.

## 2. Source basis

Distillation is based only on:

- `SR-V10K-0001`
- `SR-V10K-0002`
- `SR-V10K-0003`
- `SR-V10K-0004`
- `SR-V10K-0005`
- `SR-V10K-0006`
- `SR-V10K-0007`
- `SR-V10K-0008`
- `SR-V10K-0009`
- `SR-V10K-0010`

The source records remain bounded, preserve external-factual-claim exclusions, and retain their original status fields. Raw X leads, screenshots, complete X posts, uncreated proposals, and external factual assertions are not direct distillation inputs.

`docs/method-claim-candidates-v1.0e.md` and `docs/method-claim-review-v1.0f.md` are used only to preserve MCC wording, review dispositions, and status boundaries. They are not altered by this round.

## 3. Distillation method

The distillation pass:

1. reads each bounded record's method signal, usage boundary, excluded factual claims, and remaining human checks;
2. groups related signals without treating repeated source-record references as independent factual corroboration;
3. separates physical mapping, firm capture, shareholder capture, source governance, and invalidation;
4. maps each note back to its bounded source records and existing MCC candidates;
5. preserves uncertainty and counterevidence requirements; and
6. stops at a reviewable method note rather than promoting the note into a claim or runtime instruction.

No method note establishes the factual correctness of its source examples. The notes describe candidate analytical moves and safeguards only.

## 4. Method note summary

| method note | primary method dimension | source records | related MCC | status |
| --- | --- | --- | --- | --- |
| MN-V10L-0001 | physical_supply_chain_mapping | SR-V10K-0001, 0002, 0003 | MCC-0001, 0002, 0004, 0005 | distilled_note_not_validated |
| MN-V10L-0002 | firm_value_capture | SR-V10K-0003, 0004 | MCC-0003, 0005 | distilled_note_not_validated |
| MN-V10L-0003 | shareholder_capture | SR-V10K-0005, 0006, 0007, 0008 | MCC-0003, 0004, 0005 | distilled_note_not_validated |
| MN-V10L-0004 | source_governance | SR-V10K-0001, 0009 | MCC-0002, 0005 | distilled_note_not_validated |
| MN-V10L-0005 | false_positive_invalidation | SR-V10K-0002, 0003, 0008, 0010 | MCC-0001, 0003, 0004, 0005 | distilled_note_not_validated |

## 5. Method notes

### MN-V10L-0001｜Physical Supply-Chain Mapping as Hypothesis Formation

```yaml
method_note_id: MN-V10L-0001
method_note_title: Physical Supply-Chain Mapping as Hypothesis Formation
method_note_status: distilled_note_not_validated
method_claim_status: not_validated
runtime_status: not_runtime_ready
toc_calibration_status: not_started
investment_advice_status: prohibited
source_basis: bounded_source_records_only
source_record_ids:
  - SR-V10K-0001
  - SR-V10K-0002
  - SR-V10K-0003
related_mcc:
  - MCC-0001
  - MCC-0002
  - MCC-0004
  - MCC-0005
primary_method_dimension: physical_supply_chain_mapping
secondary_method_dimensions:
  - source_governance
  - false_positive_invalidation
  - firm_value_capture
distilled_method_signal: "A chokepoint hypothesis can be formed by physically mapping substrates, components, procurement behavior, supply relationships, and capacity commitments, but the map remains a defeasible hypothesis rather than proof of a durable constraint."
method_boundary:
  - "Physical mapping is not proof."
  - "Procurement behavior is not proof."
  - "Supply-chain location is not automatically the active system constraint."
  - "Technical depth and physical participation do not establish value capture."
what_this_note_allows:
  - "Generate a reviewable physical dependency and capacity hypothesis."
  - "Identify scarcity, substitution, qualification, throughput, and system-boundary questions for later evidence review."
  - "Preserve question-form reasoning when procurement or capacity commitments are observed."
what_this_note_does_not_allow:
  - "Treat a dependency map as a validated constraint."
  - "Treat procurement, agreements, or supply relationships as proof of durable scarcity."
  - "Infer a company conclusion, investment view, or runtime rule."
external_factual_claim_policy: "All company, procurement, capacity, market-share, pricing, relationship, and third-party reporting claims remain excluded or require independent verification."
runtime_policy: "Not runtime-ready; requires method review and later runtime-design approval."
toc_calibration_policy: "No TOC calibration is performed; system boundary, throughput impact, and active-constraint tests remain open."
investment_advice_policy: "Prohibited; the note cannot support a security conclusion, target price, position, or trade."
open_questions:
  - "What evidence distinguishes a dependency from an active system constraint?"
  - "When should backward physical tracing stop?"
  - "What substitution, qualification, capacity, and throughput evidence would falsify the map?"
recommended_review_disposition: candidate_method_note_for_review
```

### MN-V10L-0002｜Control Point and Firm-Level Value Capture Separation

```yaml
method_note_id: MN-V10L-0002
method_note_title: Control Point and Firm-Level Value Capture Separation
method_note_status: distilled_note_not_validated
method_claim_status: not_validated
runtime_status: not_runtime_ready
toc_calibration_status: not_started
investment_advice_status: prohibited
source_basis: bounded_source_records_only
source_record_ids:
  - SR-V10K-0003
  - SR-V10K-0004
related_mcc:
  - MCC-0003
  - MCC-0005
primary_method_dimension: firm_value_capture
secondary_method_dimensions:
  - physical_supply_chain_mapping
  - shareholder_capture
  - source_governance
distilled_method_signal: "A firm may participate in a chokepoint-relevant layer without necessarily capturing disproportionate value; value capture requires testing control point, technical depth, margin structure, integration position, and where economics actually accrue."
method_boundary:
  - "Chain importance is not value capture."
  - "Technical depth is not automatically pricing power."
  - "Control-point language is a hypothesis, not evidence of realized economics."
  - "Firm-level value capture is not shareholder return."
what_this_note_allows:
  - "Separate physical participation from the location of economic capture."
  - "Generate questions about control, margins, integration, bargaining power, and accrual of economics."
what_this_note_does_not_allow:
  - "Infer firm value from technical relevance alone."
  - "Treat rhetorical toll-collector language as demonstrated pricing power."
  - "Infer shareholder return, a company conclusion, or an investment recommendation."
external_factual_claim_policy: "TAM, margins, company capabilities, integration, sector bottlenecks, pricing power, and realized-value claims require independent verification."
runtime_policy: "Not runtime-ready; this separation requires method review before any operational rule is considered."
toc_calibration_policy: "No claim is made that firm economic capture is a TOC construct; the relationship to TOC remains for later calibration."
investment_advice_policy: "Prohibited; no company, sector, asset, or security recommendation follows."
open_questions:
  - "Which observable evidence demonstrates control over an economically important point?"
  - "How should technical depth, bargaining power, margins, and capital requirements be tested separately?"
  - "Where can economics accrue when the physically important participant does not capture them?"
recommended_review_disposition: candidate_method_note_for_review
```

### MN-V10L-0003｜Shareholder-Capture Boundary

```yaml
method_note_id: MN-V10L-0003
method_note_title: Shareholder-Capture Boundary
method_note_status: distilled_note_not_validated
method_claim_status: not_validated
runtime_status: not_runtime_ready
toc_calibration_status: not_started
investment_advice_status: prohibited
source_basis: bounded_source_records_only
source_record_ids:
  - SR-V10K-0005
  - SR-V10K-0006
  - SR-V10K-0007
  - SR-V10K-0008
related_mcc:
  - MCC-0003
  - MCC-0004
  - MCC-0005
primary_method_dimension: shareholder_capture
secondary_method_dimensions:
  - firm_value_capture
  - source_governance
  - false_positive_invalidation
distilled_method_signal: "Operating value, firm-level benefit, or capacity monetization does not automatically become common-shareholder value. Shareholder capture requires reviewing dilution structure, financing quality, equity-appreciation path, priced-in timing, and whether upside is structurally capped."
method_boundary:
  - "Company benefit is not current shareholder benefit."
  - "Dilution is not automatically bad or good."
  - "Financing structure and use of proceeds matter."
  - "Priced-in timing and starting valuation matter."
  - "No target price or trading conclusion follows from this note."
what_this_note_allows:
  - "Separate operating value, firm benefit, and common-shareholder capture."
  - "Generate review questions about dilution, debt, ownership, use of proceeds, valuation, and timing."
  - "Identify financing structure as a possible invalidation or capture boundary."
what_this_note_does_not_allow:
  - "Classify a financing as accretive or predatory without evidence."
  - "Forecast equity appreciation or establish a market-pricing window."
  - "Produce a target price, trade, company conclusion, or investment advice."
external_factual_claim_policy: "Financing terms, ATM use, debt, ownership, float, valuation, market timing, company benefit, and shareholder-impact claims require independent verification."
runtime_policy: "Not runtime-ready; no scoring, recommendation, or automated shareholder-capture rule is approved."
toc_calibration_policy: "No TOC calibration is performed; shareholder capture may be an external analytical overlay rather than a TOC concept."
investment_advice_policy: "Prohibited; no buy, sell, hold, long, short, target price, sizing, or return expectation is allowed."
open_questions:
  - "What evidence connects operating improvement to per-share outcomes?"
  - "How should financing structure, dilution, and use of proceeds be assessed without categorical shortcuts?"
  - "What evidence is required to assess whether an expectation is already reflected in valuation?"
recommended_review_disposition: requires_method_review_before_claim
```

### MN-V10L-0004｜Inference Discipline and Source Governance

```yaml
method_note_id: MN-V10L-0004
method_note_title: Inference Discipline and Source Governance
method_note_status: distilled_note_not_validated
method_claim_status: not_validated
runtime_status: not_runtime_ready
toc_calibration_status: not_started
investment_advice_status: prohibited
source_basis: bounded_source_records_only
source_record_ids:
  - SR-V10K-0001
  - SR-V10K-0009
related_mcc:
  - MCC-0002
  - MCC-0005
primary_method_dimension: source_governance
secondary_method_dimensions:
  - physical_supply_chain_mapping
  - false_positive_invalidation
distilled_method_signal: "Source-led chokepoint research requires explicit uncertainty, adversarial review, and separation between original method expression, inference, and independently verifiable factual claims."
method_boundary:
  - "A source record does not validate factual correctness."
  - "A public expression does not validate a method."
  - "High-conviction inference must remain falsifiable."
  - "External factual claims require independent verification."
  - "Acknowledging uncertainty does not make an inference reliable."
what_this_note_allows:
  - "Label source role, inference, uncertainty, and future validation explicitly."
  - "Generate adversarial questions and define evidence that could change the hypothesis."
  - "Keep original expression separate from external facts and later analysis."
what_this_note_does_not_allow:
  - "Treat confidence language as evidence."
  - "Promote a public expression directly into a validated method claim."
  - "Use a bounded record as factual verification, a company conclusion, or a runtime rule."
external_factual_claim_policy: "Company examples, relationships, forecasts, market-share, pricing, and third-party claims remain excluded or independently unverified."
runtime_policy: "Not runtime-ready; future runtime governance requires a separate reviewed claim-to-source policy."
toc_calibration_policy: "Source governance is not treated as TOC calibration; its relationship to TOC is unresolved."
investment_advice_policy: "Prohibited; source confidence and inference framing cannot support an investment recommendation."
open_questions:
  - "What corroboration is appropriate for each claim type?"
  - "What evidence would falsify or materially narrow a high-conviction inference?"
  - "Which source-governance rules belong in method review versus corpus governance?"
recommended_review_disposition: requires_method_review_before_claim
```

### MN-V10L-0005｜False-Positive and Invalidation Control

```yaml
method_note_id: MN-V10L-0005
method_note_title: False-Positive and Invalidation Control
method_note_status: distilled_note_not_validated
method_claim_status: not_validated
runtime_status: not_runtime_ready
toc_calibration_status: not_started
investment_advice_status: prohibited
source_basis: bounded_source_records_only
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
primary_method_dimension: false_positive_invalidation
secondary_method_dimensions:
  - physical_supply_chain_mapping
  - firm_value_capture
  - shareholder_capture
  - source_governance
distilled_method_signal: "A downstream beneficiary, adjacent participant, local shortage, or temporarily tight capacity is not automatically the active system constraint. A chokepoint hypothesis must test false positives, capacity release, substitution, bypass, and whether value capture persists after the constraint shifts."
method_boundary:
  - "Beneficiary is not constraint."
  - "Local bottleneck is not system constraint."
  - "Temporary shortage is not a durable chokepoint."
  - "Capacity expansion may release or move the constraint."
  - "Substitution or bypass risk can invalidate value capture."
what_this_note_allows:
  - "Generate false-positive, constraint-release, substitution, bypass, and persistence tests."
  - "Compare physical importance, beneficiary quality, and value-capture durability as separate questions."
  - "Define evidence that would narrow or reject a chokepoint hypothesis."
what_this_note_does_not_allow:
  - "Rank companies or identify a preferred beneficiary."
  - "Treat temporary tightness, procurement, or local scarcity as durable constraint proof."
  - "Infer persistent firm or shareholder value capture."
external_factual_claim_policy: "Company mix, relationships, capacity, supply constraints, beneficiary effects, financing effects, and comparative-attractiveness claims require independent verification."
runtime_policy: "Not runtime-ready; no automatic rejection, scoring, or company-selection rule is approved."
toc_calibration_policy: "No TOC calibration is performed; the distinction between local bottleneck and active system constraint requires later review."
investment_advice_policy: "Prohibited; the note cannot rank beneficiaries or support any security recommendation."
open_questions:
  - "What evidence distinguishes a temporary local bottleneck from a persistent system constraint?"
  - "Which capacity, substitution, and bypass milestones would invalidate the hypothesis?"
  - "How should value capture be retested after a constraint moves or is elevated?"
recommended_review_disposition: candidate_method_note_for_review
```

## 6. Method boundary matrix

| method note | allowed later use | not allowed use | required future review |
| --- | --- | --- | --- |
| MN-V10L-0001 | Candidate physical-mapping and constraint-testing questions. | Validated method claim; runtime rule; TOC calibration; company conclusion; investment advice. | Test scarcity, throughput, substitution, qualification, and system boundary across cases. |
| MN-V10L-0002 | Candidate separation of physical importance from firm economic capture. | Validated method claim; runtime rule; TOC calibration; company conclusion; investment advice. | Review control-point evidence, margins, bargaining power, integration, and economic accrual. |
| MN-V10L-0003 | Candidate separation of operating value, firm benefit, and shareholder capture. | Validated method claim; runtime rule; TOC calibration; company conclusion; investment advice. | Review financing structure, dilution, ownership, valuation, timing, and per-share conversion across cases. |
| MN-V10L-0004 | Candidate inference, uncertainty, attribution, and source-role discipline. | Validated method claim; runtime rule; TOC calibration; company conclusion; investment advice. | Review corroboration thresholds, falsification practice, and whether rules belong to method or corpus governance. |
| MN-V10L-0005 | Candidate false-positive, release, substitution, bypass, and persistence tests. | Validated method claim; runtime rule; TOC calibration; company conclusion; investment advice. | Review counterexamples, constraint migration, effective capacity, substitution, and beneficiary-quality evidence. |

## 7. MCC relationship update

V1.0L strengthens method-note support for MCC-0001, MCC-0002, MCC-0003, MCC-0004, and MCC-0005 at the bounded-record distillation level, but validates none of them.

| MCC | Current status before V1.0L | V1.0L effect | Status after V1.0L |
| --- | --- | --- | --- |
| MCC-0001 | not_validated | strengthened as candidate method note support | not_validated |
| MCC-0002 | not_validated | strengthened as candidate method note support | not_validated |
| MCC-0003 | not_validated | strengthened as candidate method note support | not_validated |
| MCC-0004 | not_validated / not_runtime_ready | clarified as release / capacity / bypass boundary | not_validated |
| MCC-0005 | not_validated / source governance rule | strengthened as source-governance and invalidation discipline | not_validated |

This update does not alter the source files, candidate-claim document, method-claim review, or any MCC status. Strengthened support means that bounded records now support reviewable note formulations; it does not mean the formulations are general, distinctive, cross-case validated, TOC-calibrated, or runtime-ready.

## 8. What remains outside method layer

The following remain outside the method layer and are not distilled into method claims:

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

Also outside the method layer are factual verification, company ranking, security selection, market-timing forecasts, complete source text, and any claim that a specific dependency is the active system constraint.

## 9. Recommended next step

The recommended next round is **V1.0M — Method Claim Review from Distilled Notes**.

V1.0M should:

1. review whether any method notes can become candidate method claims;
2. keep all method claims unvalidated unless explicitly reviewed;
3. decide which notes are ready for V1.1 runtime design;
4. decide which notes require additional source records; and
5. avoid `SKILL.md` runtime updates.

The project should not jump directly to V1.1 before V1.0M is completed.

## 10. Final boundary note

This document distills method notes from bounded seed source records only. It validates no method claims, changes no MCC status to validated, performs no TOC calibration, approves no runtime rules, modifies no SKILL.md behavior, reaches no real-company conclusions, and provides no investment advice.
