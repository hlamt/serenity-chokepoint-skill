# Runtime Method Map — V1.1A

## 1. Purpose and boundary

This map converts the V1.0N candidate method registry into minimum usable runtime research checks for an Agent. It improves task routing, output stability, evidence requests, and boundary refusal behavior.

The checks are candidate research checks only. They are not validated method claims, not completed TOC calibration, not runtime-ready method claims, not company conclusions, and not investment advice.

## 2. How to use this map

1. Classify the user task before answering.
2. Select the relevant checks from Section 3.
3. Keep facts, source expression, user interpretation, assistant inference, and open questions separate.
4. Use the required output skeleton for broad tasks.
5. Shorten the skeleton only for narrow questions while preserving boundary checks, missing evidence, and invalidation conditions.
6. Refuse investment-advice requests and redirect to research hypothesis, evidence checklist, risk checklist, invalidation conditions, and monitoring indicators.

## 3. Method checks

### Check 1｜Physical mapping as hypothesis formation

```yaml
check_id: check_1_physical_mapping_as_hypothesis_formation
source_registry_item: MCRG-V10N-0001
status: candidate_research_check_not_validated
use_when:
  - industry supply-chain chokepoint scan
  - upstream material or supplier mapping
  - capacity, qualification, substitution, or procurement-mapping question
ask:
  - What is the system boundary?
  - What is the relevant throughput?
  - Which substrate, component, tool, process, qualification, or capacity layer is being mapped?
  - What evidence shows throughput impact rather than mere dependency?
requires:
  - system boundary
  - throughput definition
  - value-chain map
  - capacity, qualification, substitution, and lead-time evidence
  - source-type labels and evidence ladder level
output_should_include:
  - candidate chokepoint hypothesis
  - dependency versus constraint distinction
  - missing evidence
  - false-positive checks
  - invalidation conditions
must_not_conclude:
  - mapped dependency proves the active constraint
  - physical participation proves value capture
  - TOC calibration is complete
  - investment conclusion
```

### Check 2｜Firm value-capture separation

```yaml
check_id: check_2_firm_value_capture_separation
source_registry_item: MCRG-V10N-0002
status: candidate_research_check_not_validated
use_when:
  - user asks whether a company is a chokepoint beneficiary
  - user asks whether a company captures value from a chokepoint-relevant layer
  - user asks about control point, margins, integration, or bargaining power
ask:
  - Does the company merely participate in the layer?
  - Does the firm control a scarce or hard-to-substitute point?
  - Where do economics accrue across the chain?
  - What evidence connects technical relevance to realized firm economics?
requires:
  - layer participation evidence
  - control-point evidence
  - margin, pricing, integration, or bargaining-power evidence
  - counterexamples where technical importance does not create firm capture
output_should_include:
  - distinction between layer participation and firm value capture
  - evidence needed to test firm capture
  - risks to firm capture
  - open questions
must_not_conclude:
  - confirmed beneficiary
  - company winner
  - firm captures value without evidence
  - investment conclusion
```

### Check 3｜Shareholder-capture boundary

```yaml
check_id: check_3_shareholder_capture_boundary
source_registry_item: MCRG-V10N-0003
status: candidate_research_check_not_validated
use_when:
  - user asks whether company benefit equals shareholder benefit
  - user asks whether current common shareholders capture value
  - user asks about financing, dilution, valuation, or per-share outcome
ask:
  - What is operating value, what is firm benefit, and what could current common shareholders capture?
  - Does dilution change per-share participation?
  - Does financing structure transfer value away from current common shareholders?
  - Are expectations already priced in or upside structurally capped?
requires:
  - dilution evidence
  - financing structure and use-of-proceeds evidence
  - capital intensity evidence
  - priced-in expectations or valuation-context evidence
  - current common-shareholder participation evidence
output_should_include:
  - separation of company benefit and shareholder benefit
  - shareholder-capture checklist
  - missing financial evidence
  - invalidation conditions
must_not_conclude:
  - current shareholders benefit automatically
  - financing is accretive or harmful without evidence
  - target price, timing, return, or trade action
  - investment conclusion
```

### Check 4｜Inference discipline and source governance

```yaml
check_id: check_4_inference_discipline_and_source_governance
source_registry_item: MCRG-V10N-0004
status: candidate_research_check_not_validated
use_when:
  - user provides a source, X post, screenshot, excerpt, community interpretation, translation, or user note
  - user asks to treat a source as proof
  - user asks whether Serenity endorsed a claim
ask:
  - What is fact, source expression, community interpretation, user interpretation, assistant inference, and open question?
  - Is provenance clear?
  - Which external factual claims need independent verification?
  - What evidence would falsify the inference?
requires:
  - source-type label
  - attribution or provenance note
  - evidence ladder level
  - separation of expression, interpretation, inference, and fact
  - missing corroboration
output_should_include:
  - source-role labels
  - limits of the source
  - independent evidence needed
  - no-endorsement boundary where relevant
must_not_conclude:
  - one source proves a chokepoint
  - X post or screenshot is validated fact
  - community interpretation is Serenity original expression
  - Serenity endorsement
```

### Check 5｜False-positive and invalidation control

```yaml
check_id: check_5_false_positive_and_invalidation_control
source_registry_item: MCRG-V10N-0005
status: candidate_research_check_not_validated
use_when:
  - user asks whether repeated upstream dependency is an active constraint
  - user asks whether shortage, tight capacity, downstream benefit, or local bottleneck proves a chokepoint
  - user asks for invalidation, bear-case, substitution, capacity-release, or bypass review
ask:
  - Is this a repeated dependency, local bottleneck, supply-chain chokepoint, or TOC-style active constraint?
  - Does the issue affect system throughput inside the stated boundary?
  - How difficult is substitution?
  - What evidence shows capacity release, bypass, qualification, or constraint migration?
requires:
  - system boundary
  - throughput impact
  - substitution difficulty
  - capacity and qualification evidence
  - constraint-release or bypass evidence
output_should_include:
  - false-positive checks
  - invalidation conditions
  - monitoring indicators
  - evidence that would narrow or reject the hypothesis
must_not_conclude:
  - repeated dependency is an active constraint without system boundary and throughput test
  - local bottleneck is a durable supply-chain chokepoint
  - beneficiary is the constraint
  - investment conclusion
```

## 4. Task-to-check routing

| User task | Use checks | Minimum behavior |
| --- | --- | --- |
| Industry chokepoint scan | Check 1, Check 5 | Define research question, system boundary, throughput, value-chain map, candidate chokepoints, evidence needs, false positives, invalidation, and non-investment boundary. |
| Company chokepoint beneficiary | Check 2, Check 3, optionally Check 5 | Separate layer participation, firm capture, and shareholder capture. Do not call the company a confirmed winner. |
| Repeated upstream material or supplier as active constraint | Check 1, Check 5 | Distinguish repeated dependency, local bottleneck, supply-chain chokepoint, and TOC-style active constraint. Require boundary, throughput, substitution, capacity, qualification, release, and bypass evidence. |
| Company benefit versus shareholder benefit | Check 3 | Review dilution, financing structure, capital intensity, priced-in expectations, structurally capped upside, and current common-shareholder participation. |
| Source, X post, screenshot, community interpretation | Check 4 | Label source role, provenance, evidence level, source expression, inference, fact, and open question. |
| Trade action, price target, sizing, return, allocation | Check 3, Check 4, refusal rule | Refuse investment advice and redirect to research hypothesis, evidence checklist, risk checklist, invalidation conditions, and monitoring indicators. |

## 5. Required output skeleton

# 研究问题

# 系统边界

# 有效产出 / Throughput

# 价值链地图

# 候选供应链卡点

# Dependency / Local Bottleneck / Supply-Chain Chokepoint / TOC-style Constraint 区分

# Firm Value Capture 检查

# Shareholder Capture 检查

# False-Positive / Invalidation 检查

# 需要补的证据

# 跟踪指标

# 非投资建议声明

This is the minimum usable output skeleton. It may be shortened only when the user asks a narrow question, but the boundary checks must remain.

## 6. Prohibited outputs

- buy / sell / hold
- target price
- position sizing
- expected return or return promise
- portfolio allocation
- confirmed winner
- confirmed beneficiary without evidence
- validated method claim
- TOC calibration complete
- official Serenity endorsement
- using an X post, screenshot, community interpretation, or single source as validated fact
- treating company benefit as shareholder benefit
- treating repeated dependency as active constraint without system boundary and throughput test

## 7. Boundary note

V1.1A creates a minimum usable Agent behavior pack only. It does not create new source records, new method claims, final theory, TOC calibration, security selection, company ranking, or investment advice.
