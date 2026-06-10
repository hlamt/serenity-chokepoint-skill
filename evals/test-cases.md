# Test Cases

For every case, assess terminology, workflow completeness, evidence discipline, risk disclosure, and absence of deterministic investment conclusions.

Every generated research response must keep these ten sections separate:

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

## 1. A 股 AI 半导体供应链卡点分析

Prompt: Map the value chain, define throughput, identify candidate chokepoints and company types, and build an evidence and monitoring plan.

## 2. AI 基建价值链卡点分析

Prompt: Compare power, construction, compute, networking, cooling, and deployment constraints under an explicit system boundary.

## 3. 真卡点还是短期短缺

Prompt: Test persistence, throughput impact, substitution, qualification, expansion lead time, inventory, and price normalization.

## 4. 中文文章术语校准

Prompt: Separate quoted wording, source facts, project inference, supply-chain chokepoint, local bottleneck, and TOC-style constraint.

## 5. 生成证据表与跟踪指标

Prompt: Turn a candidate chokepoint into a dated evidence table, counterevidence plan, monitoring dashboard, and explicit invalidation conditions.

## Common Pass Criteria

- Uses “供应链卡点 / 卡点理论 / 供应链卡点分析” by default.
- Treats TOC as a calibration framework.
- Returns all required output sections.
- Uses the unified evidence schema: `evidence_id`, `claim`, `source_type`, `source_title`, `source_url`, `date`, `evidence_level`, `supports`, `contradicts`, `confidence`, and `notes`.
- Labels missing evidence and confidence.
- Includes a non-investment-advice disclaimer.
