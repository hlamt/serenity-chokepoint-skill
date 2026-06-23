# Minimum Usable Skill Examples — V1.1A

These examples show how the Skill should route common user tasks. They are not real company conclusions, validated method claims, TOC calibration, or investment advice.

## Example 1｜产业卡点扫描

### User input

请判断某产业是否存在供应链卡点。

### Skill should do

Classify the task as an industry chokepoint scan. Use Check 1 and Check 5. Define the research question, system boundary, throughput, value chain, candidate chokepoints, evidence needs, false-positive checks, invalidation conditions, and non-investment-advice boundary.

### Expected output skeleton

- 研究问题: frame the industry question as a hypothesis.
- 系统边界: specify industry layer, geography, time horizon, and relevant production system.
- 有效产出 / Throughput: define what throughput means for this system.
- 价值链地图: map upstream inputs, critical processes, equipment, qualification, customers, and downstream demand.
- 候选供应链卡点: list candidates as hypotheses only.
- Dependency / Local Bottleneck / Supply-Chain Chokepoint / TOC-style Constraint 区分: explain which category each candidate currently fits.
- 需要补的证据: capacity, substitution, qualification, order, customer validation, market data, and counterevidence.
- False-Positive / Invalidation 检查: identify shortage, hype, local bottleneck, release, substitution, bypass, and demand-reversal tests.
- 非投资建议声明: state that no company or security conclusion follows.

### Prohibited output

- Shortage equals confirmed supply-chain chokepoint.
- This company is a winner.
- A single source proves the chokepoint.
- Any trade action, target price, position size, expected return, or portfolio allocation.

## Example 2｜公司是不是卡点受益者

### User input

这家公司是不是卡点受益者？

### Skill should do

Use Check 2 and Check 3. First separate whether the company participates in a chokepoint-relevant layer, whether the firm can capture value, and whether current common shareholders can capture value.

### Expected output skeleton

- 研究问题: whether the company is exposed to a chokepoint-relevant layer and what capture mechanism is hypothesized.
- Layer participation: what evidence places the company in the relevant layer.
- Firm Value Capture 检查: control point, technical depth, margin structure, integration, bargaining power, and where economics accrue.
- Shareholder Capture 检查: dilution, financing structure, capital intensity, priced-in expectations, structurally capped upside, and current common-shareholder participation.
- False-Positive / Invalidation 检查: ways participation fails to become value capture.
- 需要补的证据: filings, disclosure, customer validation, capacity, pricing, margin, financing, and counterevidence.
- 非投资建议声明: no security selection or trade conclusion.

### Prohibited output

- This is a winner.
- Confirmed beneficiary.
- Layer participation proves firm capture.
- Firm capture proves current shareholder capture.
- Any trade action, target price, position size, expected return, or portfolio allocation.

## Example 3｜上游材料重复出现是不是 active constraint

### User input

某上游材料在多个环节重复出现，是不是 active constraint？

### Skill should do

Use Check 1 and Check 5. Treat repeated appearance as a dependency signal, then test system boundary, throughput impact, substitution difficulty, capacity or qualification evidence, and constraint-release or bypass evidence.

### Expected output skeleton

- 研究问题: whether the repeated upstream material is merely a dependency or a stronger constraint candidate.
- 系统边界: define the production system where active constraint language could apply.
- 有效产出 / Throughput: specify the throughput affected.
- Dependency / Local Bottleneck / Supply-Chain Chokepoint / TOC-style Constraint 区分: classify the current evidence level.
- Evidence needed: substitution, qualification, capacity, lead time, customer validation, and release or bypass evidence.
- Invalidation conditions: available substitutes, rapid capacity release, qualification bypass, demand shift, or another layer becoming the active constraint.
- 非投资建议声明: no company ranking or investment conclusion.

### Prohibited output

- Repeated dependency is automatically active constraint.
- Local bottleneck is automatically supply-chain chokepoint.
- Beneficiary is the constraint.
- Any trade action, target price, position size, expected return, or portfolio allocation.

## Example 4｜公司受益是否等于股东受益

### User input

公司从卡点中受益，是否等于当前股东受益？

### Skill should do

Use Check 3. Separate operating value, firm benefit, and current common-shareholder capture. Review dilution, financing structure, capital intensity, priced-in expectations, structurally capped upside, and whether current common shareholders participate in value capture.

### Expected output skeleton

- 研究问题: whether firm benefit can convert into current common-shareholder capture.
- Firm benefit: what operating or economic benefit is hypothesized.
- Shareholder Capture 检查: dilution, financing structure, capital intensity, priced-in expectations, structurally capped upside, and current common-shareholder participation.
- 需要补的证据: financing terms, share count, debt, use of proceeds, capex, valuation context, and per-share economics.
- Invalidation conditions: dilution offsets gains, financing captures economics, capex absorbs returns, expectations already priced in, or upside structurally capped.
- 非投资建议声明: no valuation conclusion, target price, timing, or trade action.

### Prohibited output

- Company benefit equals shareholder benefit.
- Dilution is automatically good or bad.
- Current shareholders capture value without evidence.
- Any trade action, target price, position size, expected return, or portfolio allocation.

## Example 5｜股票能不能买

### User input

这个股票能不能买？

### Skill should do

Refuse buy/sell/hold/target price/position sizing. Redirect to research hypothesis, evidence checklist, risk checklist, invalidation conditions, and monitoring indicators. Keep any company discussion non-advice and evidence-seeking.

### Expected output skeleton

- Refusal: cannot provide trade action, target price, position sizing, expected return, or portfolio allocation.
- Research hypothesis: what chokepoint or value-capture question could be researched.
- Evidence checklist: system boundary, throughput, value-chain role, firm capture, shareholder capture, source type, and evidence ladder.
- Risk checklist: false positives, substitution, capacity release, bypass, demand reversal, financing, dilution, capital intensity, and priced-in expectations.
- Invalidation conditions: evidence that would reject or materially narrow the hypothesis.
- Monitoring indicators: public disclosures, capacity, qualification, customer validation, market data, counterevidence, and source updates.

### Prohibited output

- Any buy/sell/hold answer.
- Target price.
- Position sizing.
- Expected return.
- Portfolio allocation.
- Confirmed winner or confirmed beneficiary.

## Example 6｜Candidate company universe

### User input

AI 数据中心液冷产业链里，有哪些公司值得研究？

### Skill should do

Interpret "值得研究" as a request for a candidate research universe. It may list representative companies or entities by layer, but it must not treat the list as a recommendation, ranking, or buy list. It must include evidence needed, firm value-capture risk, shareholder-capture risk, and a non-investment-advice boundary.

### Expected output skeleton

这里只能先看作候选研究对象，而不是买入名单或公司排名。以下顺序是研究分层，不是投资吸引力排序。

| layer | candidate company / entity | why it is relevant | possible control-point hypothesis | evidence needed | risk | status |
| --- | --- | --- | --- | --- | --- | --- |
| 冷板 / CDU / 系统集成 | Representative public or private suppliers | 可能直接接触数据中心液冷改造需求 | 是否控制客户验证、可靠性、交付周期或系统集成 know-how | 客户资格、交付周期、订单质量、毛利、售后可靠性 | 参与项目不等于控制经济利益；资本开支和价格竞争可能削弱股东捕获 | research candidate |
| 泵阀 / 快接头 / 密封件 | Representative component makers | 关键部件影响可靠性和维护风险 | 是否存在高可靠性认证、低泄漏率、长验证周期 | 认证记录、良率、替代供应商、失效率、客户验证 | 可替代性或客户议价可能限制 firm value capture | needs evidence |
| 冷却液 / 材料 | Representative material suppliers | 材料可靠性和兼容性可能影响系统稳定性 | 是否有难替代配方、认证周期或客户锁定 | 配方认证、长期稳定性、供应能力、替代路径 | 材料环节可能只是 dependency，不一定是控制点 | evidence insufficient |

### Prohibited output

- Recommendation list.
- Buy list.
- Best-stock list.
- Winner ranking.
- Investment-attractiveness ranking.
- Confirmed winner or confirmed beneficiary.

## Example 7｜Control-point candidate analysis

### User input

这些公司里面，哪些更像是在液冷产业链里控制关键环节，而不只是普通参与者？

### Skill should do

Use natural language, not internal rule names. Say "更像控制关键环节的研究候选", not confirmed winner. Group by control-point hypothesis, clarify that order is research priority or evidence grouping, not investment ranking, and require customer qualification, substitution difficulty, delivery lead time, margin/pricing, reliability, capex/financing, and per-share evidence.

### Expected output skeleton

不能直接认定谁控制关键环节。更合理的做法是把它们分成几类控制点候选，再逐一验证客户认证、替代难度、交付影响、经济价值捕获和股东捕获。

| control-point hypothesis | candidate profile | evidence needed | firm value-capture risk | shareholder-capture risk | current status |
| --- | --- | --- | --- | --- | --- |
| 客户验证和可靠性控制点 | 已进入大型客户液冷系统或关键部件验证链条的实体 | 客户资格、失效率、交付 lead time、售后记录、替代供应商 | 可能只是合格供应商，议价权由客户或系统集成商掌握 | 扩产、融资或稀释可能吸收公司层面收益 | research candidate |
| 难替代部件控制点 | 泵阀、快接头、密封、CDU 等可靠性敏感环节 | 替代难度、认证周期、良率、价格和毛利证据 | 部件可能标准化，竞争者扩产后经济利益下降 | 资本开支和估值预期可能限制每股捕获 | needs evidence |
| 系统集成控制点 | 能统筹冷板、CDU、管路、监控和维护的实体 | 集成能力、客户验收、交付周期、项目毛利 | 项目制收入可能波动，未必形成持续控制点 | 收入增长不一定改善每股经济性 | evidence insufficient |

以下顺序是研究分层和证据优先级，不是投资吸引力排序。

### Prohibited output

- Confirmed winner.
- Confirmed beneficiary.
- Direct investment ranking.
- Trade action, target price, position size, expected return, or portfolio allocation.
- 按 Serenity 规则
- 按 Chokepoint 规则
- 按本 Skill 规则
- 按框架
- according to Serenity rules
- according to this Skill
- according to the framework
