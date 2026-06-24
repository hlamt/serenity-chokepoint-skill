# Runtime Method Map — V1.1A

## 1. Purpose and boundary

This map converts the V1.0N candidate method registry into minimum usable runtime research checks for an Agent. It improves task routing, output stability, evidence requests, and boundary refusal behavior.

The checks are candidate research checks only. They are not validated method claims, not completed TOC calibration, not runtime-ready method claims, not company conclusions, and not investment advice.

For the V1.3 Chokepoint Theory core, use `references/chokepoint-theory-core-v1.3a.md` as the method-core reference.

## 2. How to use this map

1. Classify the user task before answering.
2. Select the relevant checks from Section 3.
3. Keep facts, source expression, user interpretation, assistant inference, and open questions separate.
4. Use the required output skeleton for broad tasks.
5. Shorten the skeleton only for narrow questions while preserving boundary checks, missing evidence, and invalidation conditions.
6. Refuse investment-advice requests and redirect to research hypothesis, evidence checklist, risk checklist, invalidation conditions, and monitoring indicators.
7. Use internal identifiers silently. In user-facing answers, translate checks, registry items, and version labels into natural reasoning unless the user explicitly asks about Skill internals.

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
| Candidate company universe or representative companies | Candidate Company Universe Mode, Check 2, Check 3, optionally Check 5 | Build a candidate research universe by layer. Label companies as research candidates, not recommendations, and separate layer participation, possible control point, firm capture, and shareholder capture. |
| Company benefit versus shareholder benefit | Check 3 | Review dilution, financing structure, capital intensity, priced-in expectations, structurally capped upside, and current common-shareholder participation. |
| Source, X post, screenshot, community interpretation | Check 4 | Label source role, provenance, evidence level, source expression, inference, fact, and open question. |
| Trade action, price target, sizing, return, allocation | Check 3, Check 4, refusal rule | Refuse investment advice and redirect to research hypothesis, evidence checklist, risk checklist, invalidation conditions, and monitoring indicators. |

# Candidate Company Universe Mode

## User intent

Use this mode when the user asks:

- 有哪些公司值得研究？
- 哪些公司值得关注？
- 哪些公司可能在这个产业链里有卡点相关性？
- 哪些公司更像控制关键环节？
- 可以列代表公司吗？
- 哪些公司进入候选研究池？

## Output posture

The output may list real companies or entities when the task is research-universe construction. Frame the list as a candidate research universe, 候选研究对象, 研究池, or control-point candidates.

Do not frame the list as a recommendation list, buy list, best-stock list, winner ranking, or investment-attractiveness ranking.

For natural user questions, do not attribute the answer to Serenity rules, Chokepoint rules, this Skill, or the framework. Use the framework silently and answer with direct reasoning.

Keep detailed wording guardrails here so the main Skill entry can stay slim and portable.

Bad opening:

```text
按 Serenity 规则，这里只能做 research hypothesis。
```

Good opening:

```text
这里只能先做研究假设。原因是：判断一家公司是否控制关键环节，需要同时验证它是否具备难替代能力、客户认证壁垒、交付影响力、经济价值捕获和股东捕获。
```

## Company universe table

| layer | candidate company / entity | public/private/subsidiary status | why it is relevant | possible control-point hypothesis | evidence needed | firm value-capture risk | shareholder-capture risk | current status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <value-chain layer> | <company or entity> | <public / private / subsidiary / unclear> | <why it belongs in the research universe> | <possible scarce or hard-to-substitute control point> | <evidence required before upgrading confidence> | <why layer participation may not become firm economics> | <why firm benefit may not reach current common shareholders> | <research candidate / needs evidence / evidence insufficient / exclude for now / watchlist only> |

## Required language

- "这里只能先看作候选研究对象，而不是买入名单或公司排名。"
- "以下顺序是研究分层，不是投资吸引力排序。"
- "进入供应链说明它参与了相关层级，但还没有证明它控制了难替代环节、能捕获公司层面的经济价值，更没有证明当前普通股股东能分享这种价值。"
- "更像控制关键环节" means a control-point candidate, not a confirmed winner.

Allowed `current status` values include:

- research candidate
- needs evidence
- evidence insufficient
- exclude for now
- watchlist only

## Boundary

Do not use:

- winner
- confirmed beneficiary
- buy candidate
- top pick
- best stock
- recommendation list
- investment-attractiveness ranking

Candidate universe output must include evidence needed, firm value-capture risk, shareholder-capture risk, and a non-investment-advice boundary.

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
