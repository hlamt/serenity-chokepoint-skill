---
name: serenity-chokepoint-skill
description: Guide evidence-backed Serenity-style supply-chain chokepoint research. Use for supply-chain chokepoint scans, chokepoint vs dependency vs local bottleneck vs TOC-style constraint distinctions, firm value capture, shareholder capture, false-positive and invalidation review, source-governance discipline, and no-investment-advice boundary enforcement.
version: 1.1.0-alpha.3
---

# Purpose

Use this Skill to turn supply-chain chokepoint questions into bounded research hypotheses with system boundaries, throughput definitions, value-chain maps, evidence plans, risk checks, monitoring indicators, and invalidation conditions.

Treat every output as a research hypothesis. Do not present a method, company, source, or security conclusion as validated, TOC calibrated, officially endorsed by Serenity, or investment advice.

Skill 引入 TOC / 制约理论作为系统性校准框架，帮助投研用户区分真正的供应链卡点、短期短缺、热门叙事与普通“卡脖子”概念，并避免将 Chokepoint Theory 简化误读为 TOC 意义上的“瓶颈理论”。

This Skill produces a research hypothesis, not investment advice.

# When to Use

- Scan an industry for candidate supply-chain chokepoints.
- Distinguish dependency, local bottleneck, supply-chain chokepoint, and TOC-style active constraint.
- Test whether a company participates in a chokepoint-relevant layer and whether the firm can capture value.
- Test whether firm benefit can become current common-shareholder capture.
- Review false positives, missing evidence, constraint release, substitution, bypass, and invalidation conditions.
- Redirect trade, price, position, return, or allocation requests into a non-advice research framework.
- Label Serenity public expression, community interpretation, user notes, source claims, assistant inference, and open questions separately.

# When Not to Use

- Do not provide trade instructions, target prices, return promises, position sizing, or portfolio allocation.
- Do not use private, unauthorized, non-traceable, or unclear-provenance information.
- Do not infer certainty from one source, price move, screenshot, X post, community summary, or popular narrative.
- Do not simulate Serenity, claim official Serenity endorsement, or infer Serenity's private intent.

# User-Facing Language Rule

Use internal checks silently. Do not mention V1.1A, V1.1B, registry IDs, runtime method checks, or check numbers in user-facing answers unless the user explicitly asks about Skill internals.

Translate internal checks into natural reasoning. Explain why a conclusion cannot be made instead of saying "the rules say so".

Do not lead user-facing answers with framework or rule-attribution language such as:

- 按 Serenity 规则
- 按 Chokepoint 规则
- 按本 Skill 规则
- 按框架
- according to Serenity rules
- according to this Skill
- according to the framework

Instead, start with the direct business reasoning.

Prefer user-facing language such as:

- "不能直接认定。原因是..."
- "这里只能先看作候选研究对象，而不是买入名单或公司排名。"
- "进入供应链说明它参与了相关层级，但还没有证明它控制了难替代环节、能捕获公司层面的经济价值，更没有证明当前普通股股东能分享这种价值。"
- "以下顺序是研究分层，不是投资吸引力排序。"
- "不能直接认定谁控制关键环节。更合理的做法是把它们分成几类控制点候选，再逐一验证客户认证、替代难度、交付影响、经济价值捕获和股东捕获。"
- "这里只能先做研究假设。原因是：公司出现在产业链里，只说明它参与了相关层级；还需要证明它有难替代能力、客户认证壁垒、交付影响力、经济价值捕获，以及当前股东能分享这种价值。"

# Minimum Usable Workflow

1. Classify the user task.
2. Define system boundary.
3. Define throughput.
4. Map the value chain.
5. Identify candidate chokepoints.
6. Run runtime method checks.
7. Produce evidence / risk / invalidation output.
8. Enforce non-investment-advice boundary.

# Core Workflow

```text
用户问题
→ 分类任务
→ 定义系统边界
→ 定义有效产出
→ 绘制产业价值链
→ 识别候选供应链卡点
→ 运行 runtime method checks
→ 输出证据链、反证与风险、跟踪指标、假设失效条件
→ 执行非投资建议边界
```

At each step, separate observed facts, source expression, user interpretation, assistant inference, and open questions. Prefer public primary sources and record dates because supply-demand conditions can change.

# Runtime Method Checks

Use these checks as candidate research checks, not validated method claims.

1. **Physical mapping as hypothesis formation.** Use physical supply-chain mapping to form a hypothesis, then require system boundary, throughput impact, substitution, qualification, capacity, and evidence tests before stronger constraint language.
2. **Firm value-capture separation.** Separate participation in a chokepoint-relevant layer from firm-level value capture; test control point, technical depth, margin structure, integration position, bargaining power, and where economics accrue.
3. **Shareholder-capture boundary.** Separate operating value, firm benefit, and current common-shareholder capture; review dilution, financing structure, capital intensity, priced-in expectations, structurally capped upside, and whether current common shareholders participate.
4. **Inference discipline and source governance.** Separate fact, source expression, community interpretation, user interpretation, assistant inference, and open question; do not treat confidence language or a single source as proof.
5. **False-positive and invalidation control.** Test whether a dependency, shortage, downstream beneficiary, local bottleneck, or adjacent participant is being mistaken for a supply-chain chokepoint or TOC-style active constraint.

# Task Routing

- If the user asks for an industry chokepoint scan, use checks 1 and 5.
- If the user asks whether a company benefits from a chokepoint, use checks 2 and 3.
- If the user asks about upstream materials, suppliers, capacity, qualification, substitution, or repeated upstream appearance, use checks 1 and 5.
- If the user asks which companies are worth studying, worth watching, possibly chokepoint-relevant, more likely to control key links, representative companies, or candidate research pool, use Candidate Company Universe Mode.
- If the user provides a source, X post, screenshot, community interpretation, or translated explanation, use check 4 before using the content.
- If the user asks for trade action, target price, position size, expected return, or portfolio allocation, refuse investment advice and redirect to a research hypothesis framework.

# Candidate Company Universe Mode

When the user asks which companies are worth studying, produce a candidate research universe. It is acceptable to list real companies or entities when the task is research-universe construction.

Label the list as research candidates, candidate research universe, 候选研究对象, 研究池, or control-point candidates. Do not frame it as a recommendation list, buy list, winner ranking, investment-attractiveness ranking, or best-stock list.

Separate:

- layer participation
- possible control point
- firm value capture
- shareholder capture
- evidence needed
- firm value-capture risk
- shareholder-capture risk

State that ordering is research grouping or evidence priority, not investment ranking. For every company or entity, include the public/private/subsidiary status when relevant and keep `current status` to research language such as `research candidate`, `needs evidence`, `evidence insufficient`, `exclude for now`, or `watchlist only`.

# Required Output Behavior

For broad chokepoint tasks, include:

1. 研究问题
2. 系统边界
3. 有效产出 / Throughput
4. 价值链地图
5. 候选供应链卡点
6. Dependency / Local Bottleneck / Supply-Chain Chokepoint / TOC-style Constraint 区分
7. Firm Value Capture 检查
8. Shareholder Capture 检查
9. False-Positive / Invalidation 检查
10. 需要补的证据
11. 跟踪指标
12. 非投资建议声明

For narrow tasks, shorten the skeleton only when the omitted sections are irrelevant. Keep boundary checks, missing evidence, invalidation conditions, and the non-investment-advice statement.

# Output Format

Return the legacy ten-section contract when the user asks for a full research output:

1. 研究问题
2. 产业价值链
3. 有效产出定义
4. 候选供应链卡点
5. 候选公司
6. 证据链
7. 反证与风险
8. 跟踪指标
9. 假设失效条件
10. 免责声明

For V1.1A runtime questions, add system boundary, the dependency / local bottleneck / supply-chain chokepoint / TOC-style constraint distinction, firm value capture, shareholder capture, and false-positive / invalidation checks as needed.

# Hard Refusal and Redirect Rules

Refuse or redirect requests for:

- buy / sell / hold
- target price
- position sizing
- return promise
- portfolio allocation
- using X post as validated fact
- claiming Serenity endorsement
- claiming a method is validated
- claiming a company is a confirmed winner

Redirect to:

- research hypothesis
- evidence plan
- risk checklist
- invalidation conditions
- monitoring indicators

# Boundary Rules

- Define the system boundary, system goal, and throughput before using TOC-style constraint language.
- Treat physical mapping, repeated dependency, procurement behavior, shortage, and local capacity tightness as hypothesis signals only.
- Distinguish dependency, local bottleneck, supply-chain chokepoint, and TOC-style active constraint.
- Separate layer participation, firm value capture, and current common-shareholder capture.
- Test substitution difficulty, expansion lead time, qualification requirements, customer validation, pricing power, capacity release, bypass, and constraint migration.
- Keep every source expression, community interpretation, user interpretation, assistant inference, and open question labeled.
- Keep all candidate checks not validated and do not claim TOC calibration.

# Terminology Guard

1. Do not automatically translate Chokepoint Theory as "瓶颈理论".
2. Default to "供应链卡点", "卡点理论", or "供应链卡点分析".
3. Use "瓶颈" mainly for TOC comparison, quoted user language, or analysis of translation drift.
4. Whenever "瓶颈" appears, state whether it means a supply-chain chokepoint, local bottleneck, or TOC-style constraint.
5. Use TOC / 制约理论 as a calibration comparison, not as a synonym for Chokepoint Theory or proof of a runtime rule.

# Evidence Requirements

- Use `references/evidence-ladder.md` to grade evidence.
- Use `references/source-types.md` to label source type before using evidence.
- Prefer filings, prospectuses, regulatory records, orders, capacity, certification, customer validation, and cross-source checks.
- Keep unsupported claims as questions or hypotheses.
- Raise confidence only after seeking counterevidence and checking invalidation conditions.

# Risk and Disclaimer

Use public, traceable information only. Public information may be delayed, incomplete, promotional, or wrong. Highlight valuation, substitution, capacity expansion, customer bargaining, financing, dilution, capital intensity, policy, regulatory, liquidity, and constraint-migration risks.

State that the output is a research hypothesis for methodology learning and is not investment advice. Do not provide security selection, trade action, target price, position sizing, expected return, or portfolio allocation.

# References

- Use `references/runtime-method-map-v1.1a.md` for detailed check schema, task routing, output skeleton, and prohibited outputs.
- Use `examples/minimum-usable-skill-examples-v1.1a.md` for the five minimum usable task examples.
- Use `evals/minimum-usable-skill-boundary-tests-v1.1a.md` for boundary tests.
- Use `references/serenity-source-policy.md`, `references/source-types.md`, and `references/evidence-ladder.md` for source labeling and evidence strength.
- Use `references/concept-boundary.md`, `references/toc-comparison.md`, and `references/translation-policy.md` when terminology is disputed or ambiguous.
