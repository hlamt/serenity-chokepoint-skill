# Candidate Method Claim Registry and Review Queue — V1.0N

## 1. Purpose and boundary

This document registers the five V1.0M candidate method claims and places them into auditable review queues. Registration preserves provenance, blocking gaps, later-use boundaries, and next actions.

Registration is not validation, TOC calibration, runtime approval, or a `SKILL.md` update. It creates no company conclusion, final Chokepoint Theory, or investment advice.

## 2. Source basis

The registry is based only on:

- V1.0M candidate claims `MCR-V10M-0001` through `MCR-V10M-0005`;
- V1.0L method notes `MN-V10L-0001` through `MN-V10L-0005`;
- V1.0K bounded source records `SR-V10K-0001` through `SR-V10K-0010`; and
- existing MCC candidate and review documents for status boundaries.

Raw X leads, screenshots, complete X posts, uncreated source records, and external factual assertions are not registry inputs. All source-record exclusions and human-review requirements remain in force.

## 3. Registry method

Each item:

1. preserves the candidate claim wording and status from V1.0M;
2. maps the claim to its source method note, bounded records, and MCC candidates;
3. assigns one or more review queues based on unresolved evidence, TOC, governance, runtime, or investment-adjacent boundaries;
4. records blocking gaps and permitted later use; and
5. stops at registry and queue management without strengthening the claim.

Queue placement is not approval. An item may appear in multiple queues because source expansion, TOC review, governance policy, and runtime design are separate gates.

## 4. Registry summary

| registry item | candidate claim | category | queue | status | next action |
| --- | --- | --- | --- | --- | --- |
| MCRG-V10N-0001 | MCR-V10M-0001 | physical_mapping | TOC calibration / runtime later | candidate_not_validated | send_to_toc_calibration_review |
| MCRG-V10N-0002 | MCR-V10M-0002 | firm_value_capture | more sources / runtime later | candidate_not_validated | hold_for_more_source_records |
| MCRG-V10N-0003 | MCR-V10M-0003 | shareholder_capture | more sources / investment-adjacent boundary / runtime later | candidate_not_validated | hold_for_more_source_records |
| MCRG-V10N-0004 | MCR-V10M-0004 | source_governance | source-governance policy / runtime later | candidate_not_validated | prepare_source_governance_policy_review |
| MCRG-V10N-0005 | MCR-V10M-0005 | false_positive_invalidation | TOC calibration / runtime later | candidate_not_validated | send_to_toc_calibration_review |

## 5. Candidate method claim registry

### MCRG-V10N-0001｜Physical mapping as hypothesis formation

```yaml
registry_item_id: MCRG-V10N-0001
candidate_claim_id: MCR-V10M-0001
candidate_claim_title: Physical mapping as hypothesis formation
registry_status: registered_candidate_claim
candidate_claim_status: candidate_not_validated
method_claim_status: not_validated
runtime_status: not_runtime_ready
toc_calibration_status: not_started
investment_advice_status: prohibited
source_basis: bounded_source_records_and_distilled_notes_only
source_method_note_id: MN-V10L-0001
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
claim_category: physical_mapping
queue_classification:
  - toc_calibration_review_queue
  - runtime_design_later_queue
required_future_review:
  - "TOC system-boundary review."
  - "Active-constraint evidence review."
  - "Capacity, substitution, qualification, and throughput evidence review."
  - "Runtime design review later."
blocking_gaps:
  - "Active-constraint criteria unresolved."
  - "System boundary unresolved."
  - "Throughput-impact evidence standard unresolved."
allowed_later_use:
  - "Plan TOC and evidence-test review for physical-mapping hypotheses."
  - "Retain traceability to bounded records and method note."
not_allowed_use:
  - "Validated method claim."
  - "TOC-calibrated claim or runtime rule."
  - "Company conclusion or investment advice."
  - "Proof that a mapped dependency is the active constraint."
recommended_next_action: send_to_toc_calibration_review
review_priority: P1_foundational_method_boundary
```

### MCRG-V10N-0002｜Firm value-capture separation

```yaml
registry_item_id: MCRG-V10N-0002
candidate_claim_id: MCR-V10M-0002
candidate_claim_title: Firm value-capture separation
registry_status: registered_candidate_claim
candidate_claim_status: candidate_not_validated
method_claim_status: not_validated
runtime_status: not_runtime_ready
toc_calibration_status: not_started
investment_advice_status: prohibited
source_basis: bounded_source_records_and_distilled_notes_only
source_method_note_id: MN-V10L-0002
source_record_ids:
  - SR-V10K-0003
  - SR-V10K-0004
related_mcc:
  - MCC-0003
  - MCC-0005
candidate_claim_wording: "A firm's participation in a chokepoint-relevant layer does not automatically imply firm-level value capture; firm-level capture must be separately tested through control point, technical depth, margin structure, integration position, bargaining power, and where economics actually accrue."
claim_category: firm_value_capture
queue_classification:
  - additional_source_record_queue
  - runtime_design_later_queue
required_future_review:
  - "Additional non-X or independently verified source records."
  - "Company-fact exclusion review."
  - "Value-capture evidence-standard review."
  - "Runtime design review later."
blocking_gaps:
  - "Firm-level value-capture evidence standard unresolved."
  - "Non-X corroborating source records insufficient."
  - "Company-factual verification outside current source basis."
allowed_later_use:
  - "Plan source expansion and evidence-standard review."
  - "Preserve separation between chain participation and firm economics."
not_allowed_use:
  - "Validated method claim."
  - "Runtime rule or TOC calibration."
  - "Company conclusion or investment advice."
  - "Assertion that a named firm captures value."
recommended_next_action: hold_for_more_source_records
review_priority: P2_requires_source_expansion
```

### MCRG-V10N-0003｜Shareholder-capture boundary

```yaml
registry_item_id: MCRG-V10N-0003
candidate_claim_id: MCR-V10M-0003
candidate_claim_title: Shareholder-capture boundary
registry_status: registered_candidate_claim
candidate_claim_status: candidate_not_validated
method_claim_status: not_validated
runtime_status: not_runtime_ready
toc_calibration_status: not_started
investment_advice_status: prohibited
source_basis: bounded_source_records_and_distilled_notes_only
source_method_note_id: MN-V10L-0003
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
claim_category: shareholder_capture
queue_classification:
  - additional_source_record_queue
  - investment_adjacent_boundary_queue
  - runtime_design_later_queue
required_future_review:
  - "Investment-adjacent language review."
  - "External financial-fact verification."
  - "Financing-structure evidence-standard review."
  - "Strict no-investment-advice runtime boundary."
blocking_gaps:
  - "Financial-fact verification outside current source basis."
  - "Shareholder-capture evidence standard unresolved."
  - "Investment-adjacent phrasing requires stricter policy."
allowed_later_use:
  - "Plan additional source records and boundary-policy review."
  - "Preserve separation of operating, firm, and shareholder outcomes."
not_allowed_use:
  - "Validated method claim."
  - "Runtime rule or TOC calibration."
  - "Company conclusion or investment advice."
  - "Target price, trade, timing, return expectation, or recommendation."
recommended_next_action: hold_for_more_source_records
review_priority: P2_requires_source_expansion
```

### MCRG-V10N-0004｜Inference discipline and source governance

```yaml
registry_item_id: MCRG-V10N-0004
candidate_claim_id: MCR-V10M-0004
candidate_claim_title: Inference discipline and source governance
registry_status: registered_candidate_claim
candidate_claim_status: candidate_not_validated
method_claim_status: not_validated
runtime_status: not_runtime_ready
toc_calibration_status: not_started
investment_advice_status: prohibited
source_basis: bounded_source_records_and_distilled_notes_only
source_method_note_id: MN-V10L-0004
source_record_ids:
  - SR-V10K-0001
  - SR-V10K-0009
related_mcc:
  - MCC-0002
  - MCC-0005
candidate_claim_wording: "Source-led chokepoint research must separate original source expression, inference, external factual claims, and later analysis; high-conviction inference must remain falsifiable and cannot be promoted into validated method or factual correctness without independent review."
claim_category: source_governance
queue_classification:
  - source_governance_policy_queue
  - runtime_design_later_queue
required_future_review:
  - "Source-governance policy review."
  - "Claim-to-source traceability review."
  - "Runtime evidence-display design later."
blocking_gaps:
  - "Claim-to-source display behavior unresolved."
  - "Source-role taxonomy not yet runtime-approved."
  - "Inference, fact, and analysis display policy unresolved."
allowed_later_use:
  - "Prepare a source-governance policy review."
  - "Define traceability and evidence-display design requirements."
not_allowed_use:
  - "Validated method claim."
  - "Runtime rule or TOC calibration."
  - "Company conclusion or investment advice."
  - "Treating public expression or confidence as factual proof."
recommended_next_action: prepare_source_governance_policy_review
review_priority: P1_foundational_method_boundary
```

### MCRG-V10N-0005｜False-positive and invalidation control

```yaml
registry_item_id: MCRG-V10N-0005
candidate_claim_id: MCR-V10M-0005
candidate_claim_title: False-positive and invalidation control
registry_status: registered_candidate_claim
candidate_claim_status: candidate_not_validated
method_claim_status: not_validated
runtime_status: not_runtime_ready
toc_calibration_status: not_started
investment_advice_status: prohibited
source_basis: bounded_source_records_and_distilled_notes_only
source_method_note_id: MN-V10L-0005
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
claim_category: false_positive_invalidation
queue_classification:
  - toc_calibration_review_queue
  - runtime_design_later_queue
required_future_review:
  - "TOC active-constraint calibration."
  - "False-positive test design."
  - "Constraint-release, substitution, and bypass evidence review."
  - "Runtime checklist design later."
blocking_gaps:
  - "Active constraint versus beneficiary distinction unresolved."
  - "False-positive test design unresolved."
  - "Release, substitution, and bypass evidence thresholds unresolved."
allowed_later_use:
  - "Plan TOC calibration and evidence-test design."
  - "Preserve false-positive and invalidation questions for review."
not_allowed_use:
  - "Validated method claim."
  - "Runtime rule or completed TOC calibration."
  - "Company conclusion or investment advice."
  - "Company ranking or preferred-beneficiary selection."
recommended_next_action: send_to_toc_calibration_review
review_priority: P1_foundational_method_boundary
```

## 6. Review queue summary

### 6.1 TOC calibration review queue

Items:

- `MCRG-V10N-0001`
- `MCRG-V10N-0005`

These items require TOC system-boundary, active-constraint, constraint-release, substitution, bypass, and throughput-impact review before any claim can be strengthened or considered for runtime design.

### 6.2 Additional source record queue

Items:

- `MCRG-V10N-0002`
- `MCRG-V10N-0003`

These items need additional non-X or independently verified source records before stronger method-claim review, because firm value capture, financing quality, and shareholder-capture claims depend on external financial and company-specific evidence that remains outside the current bounded source basis.

### 6.3 Source governance policy queue

Item:

- `MCRG-V10N-0004`

This item can proceed as a governance candidate, but claim-to-source traceability, source-role taxonomy, uncertainty display, and inference/fact/analysis separation require explicit policy review before any runtime design.

### 6.4 Runtime design later queue

Items:

- `MCRG-V10N-0001`
- `MCRG-V10N-0002`
- `MCRG-V10N-0003`
- `MCRG-V10N-0004`
- `MCRG-V10N-0005`

None of the registry items are runtime-ready. Runtime design may only occur after the relevant method review, source expansion, TOC calibration, and governance policy review have been completed.

### 6.5 Investment-adjacent boundary queue

Item:

- `MCRG-V10N-0003`

The shareholder-capture boundary is useful as an analytical safeguard, but it is investment-adjacent and requires strict language control to prevent target price, trade, timing, return expectation, or recommendation outputs.

## 7. MCC relationship summary

V1.0N registers five V1.0M candidate method claims and places them into review queues. It strengthens candidate-level traceability for MCC-0001 through MCC-0005, but validates none of them and does not alter existing MCC documents.

| Existing MCC | Related registry items | Status after V1.0N |
| --- | --- | --- |
| MCC-0001 | MCRG-V10N-0001, MCRG-V10N-0005 | not_validated |
| MCC-0002 | MCRG-V10N-0001, MCRG-V10N-0004 | not_validated |
| MCC-0003 | MCRG-V10N-0002, MCRG-V10N-0003, MCRG-V10N-0005 | not_validated |
| MCC-0004 | MCRG-V10N-0001, MCRG-V10N-0003, MCRG-V10N-0005 | not_validated / not_runtime_ready |
| MCC-0005 | MCRG-V10N-0001, MCRG-V10N-0002, MCRG-V10N-0003, MCRG-V10N-0004, MCRG-V10N-0005 | not_validated |

## 8. Runtime readiness matrix

| registry item | runtime readiness | reason | required before runtime |
| --- | --- | --- | --- |
| MCRG-V10N-0001 | not_runtime_ready | active-constraint and system-boundary criteria unresolved | TOC calibration review |
| MCRG-V10N-0002 | not_runtime_ready | firm value-capture evidence standard unresolved | more source records and method review |
| MCRG-V10N-0003 | not_runtime_ready | investment-adjacent boundary and financial evidence unresolved | source expansion and strict no-investment-advice policy |
| MCRG-V10N-0004 | not_runtime_ready | source-governance display policy unresolved | governance policy and runtime display review |
| MCRG-V10N-0005 | not_runtime_ready | false-positive and invalidation tests unresolved | TOC calibration and test-design review |

## 9. What remains outside registry layer

- validated method claims
- TOC calibration claims
- runtime rules
- SKILL.md behavior
- final Chokepoint Theory
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

Factual verification, security selection, company ranking, return expectations, and the assertion that a specific dependency is the active system constraint also remain outside the registry layer.

## 10. Recommended next step

The recommended next round is **V1.0O — TOC Calibration Review Plan and Evidence-Test Design**.

V1.0O should focus on:

1. `MCRG-V10N-0001` physical mapping as hypothesis formation;
2. `MCRG-V10N-0005` false-positive and invalidation control;
3. system-boundary definition;
4. active-constraint evidence tests;
5. constraint-release, substitution, and bypass tests;
6. throughput-impact evidence requirements; and
7. no runtime or `SKILL.md` changes.

`MCRG-V10N-0002` and `MCRG-V10N-0003` should remain in the additional source-record queue until non-X or independently verified source records are added.

`MCRG-V10N-0004` should remain in source-governance policy review until runtime display and claim-to-source policy are separately designed.

## 11. Final boundary note

This document registers V1.0M candidate method claims and places them into review queues only. It validates no method claims, changes no existing MCC document, performs no TOC calibration, approves no runtime rules, modifies no SKILL.md behavior, reaches no real-company conclusions, and provides no investment advice.
