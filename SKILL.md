---
name: serenity-chokepoint-skill
description: Guide evidence-backed Serenity-style supply-chain chokepoint investment research. Use when an investment researcher or industry-chain analyst needs to map a value chain, define throughput, identify candidate chokepoints and companies, distinguish structural constraints from shortages or hype, apply TOC-informed terminology guardrails, build a traceable evidence plan, and state risks, tracking indicators, and invalidation conditions.
version: 0.2.0
---

# Purpose

Use this Skill to identify possible investment opportunities around supply-chain chokepoints and to build candidate companies, evidence chains, validation paths, risk lists, tracking indicators, and invalidation conditions.

Skill 引入 TOC / 制约理论作为系统性校准框架，帮助投研用户区分真正的供应链卡点、短期短缺、热门叙事与普通“卡脖子”概念，并避免将 Chokepoint Theory 简化误读为 TOC 意义上的“瓶颈理论”。

Treat every result as a research hypothesis. Do not present it as an investment conclusion.

# When to Use

- Map a hot industry theme into a value chain and screen for candidate supply-chain chokepoints.
- Compare a claimed chokepoint with a temporary shortage, local bottleneck, market narrative, or TOC-style constraint.
- Build a candidate-company universe and specify what public evidence would validate or refute it.
- Turn an existing hypothesis into an evidence table, monitoring plan, and invalidation checklist.
- Calibrate Chinese uses of “瓶颈理论” without derailing the user's actual research task.

# When Not to Use

- Do not provide trade instructions, return promises, or individualized asset-allocation conclusions.
- Do not use private, unauthorized, or non-traceable information.
- Do not infer certainty from a single news item, price move, or popular narrative.
- Do not simulate Serenity or imply official endorsement.

# Terminology Guard

1. Do not automatically translate Chokepoint Theory as “瓶颈理论”.
2. Default to “供应链卡点”, “卡点理论”, or “供应链卡点分析”.
3. Use “瓶颈” mainly for TOC comparison, quoted user language, or analysis of translation drift.
4. Whenever “瓶颈” appears, state whether it means a supply-chain chokepoint, local bottleneck, or TOC-style constraint.
5. Use TOC / 制约理论 as a systematic calibration framework, not as a synonym for Chokepoint Theory.

Read [references/concept-boundary.md](references/concept-boundary.md), [references/toc-comparison.md](references/toc-comparison.md), and [references/translation-policy.md](references/translation-policy.md) when terminology is disputed or ambiguous.

# Core Workflow

```text
热点 / 产业主题
→ 定义产业价值链
→ 定义有效产出
→ 识别候选供应链卡点
→ 用 TOC-informed CCR 检查
→ 判断价值捕获能力
→ 构建证据链
→ 输出候选公司与投研假设
→ 跟踪制约释放与制约迁移
→ 标记假设失效条件
```

At each step, separate observed facts, sourced claims, project inferences, and open questions. Prefer public primary sources and record dates because supply-demand conditions can change.

# Output Format

Return these sections in order:

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

Label confidence and missing evidence. For candidate companies, explain exposure, value-capture logic, and evidence still required; do not convert screening into a recommendation.

# Evidence Requirements

- Use [references/evidence-ladder.md](references/evidence-ladder.md) to grade evidence.
- Prefer filings, prospectuses, regulatory records, orders, capacity, certification, customer validation, and cross-source checks.
- Attach a source type, URL or document locator, date, supporting or contradicting role, confidence, and notes to material claims.
- Keep unsupported claims as questions or hypotheses.
- Seek counterevidence before raising confidence.

# Boundary Rules

- Define the system boundary, system goal, and throughput before applying TOC language.
- Test whether scarcity affects system throughput and shows CCR-like characteristics.
- Check substitution difficulty, expansion lead time, customer qualification, pricing power, and value capture.
- Track constraint release and migration; today's chokepoint may disappear or move.
- Distinguish structural scarcity from temporary shortage and narrative momentum.

# Risk and Disclaimer

Use public information only. Public information may be delayed, incomplete, or wrong. Highlight valuation, substitution, capacity expansion, customer bargaining, policy, regulatory, liquidity, and constraint-migration risks. State that the output is a research hypothesis for methodology learning and is not investment advice.

# References

- Use [references/framework-v0.1.md](references/framework-v0.1.md) for the full framework.
- Use [assets/research-prompt-pack.md](assets/research-prompt-pack.md) for reusable prompts.
- Use [assets/thesis-template.md](assets/thesis-template.md) and [assets/evidence-table-template.md](assets/evidence-table-template.md) for outputs.
- Use [assets/toc-boundary-checklist.md](assets/toc-boundary-checklist.md) before finalizing terminology.
- Use [references/risk-and-compliance.md](references/risk-and-compliance.md) for risk checks.

Project version: 0.2.0.
