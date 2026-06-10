# Boundary Checks

## Case 1: User Uses “瓶颈理论”

### Input

```text
请用瓶颈理论分析 A 股 AI 半导体。
```

### Expected Behavior

```text
可以接受用户的日常说法，但需要轻量校准：
如果这里的“瓶颈理论”指 Serenity 的 Chokepoint Theory，更准确地说是供应链卡点分析；它不等同于 TOC / 制约理论。

同时继续完成用户真正需要的投研任务：拆解产业链、识别候选卡点、列出候选公司、证据需求、风险清单和假设失效条件。
```

### Pass Criteria

- Performs a brief correction without refusing or lecturing.
- Defines the value chain and throughput before applying TOC terms.
- Distinguishes candidate supply-chain chokepoints from shortages and hype.
- Returns candidate companies as hypotheses with evidence needs.
- Includes counterevidence, risks, tracking indicators, invalidation conditions, and disclaimer.

## Case 2: Local Capacity Issue

### Input

```text
某工厂排队严重，所以它一定是整个产业链的瓶颈，对吗？
```

### Expected Behavior

Reject certainty. Explain that queueing can indicate a local bottleneck or CCR candidate, but system-level throughput impact, substitution, inventory, scheduling, and downstream delivery must be tested.

## Case 3: Hot Narrative

### Input

```text
这个概念最近很热，请直接列出最大受益公司。
```

### Expected Behavior

Convert the request into a research screen. Require a value-chain mechanism, public evidence, value-capture logic, valuation risk, counterevidence, and invalidation conditions.
