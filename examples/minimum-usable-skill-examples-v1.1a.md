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
