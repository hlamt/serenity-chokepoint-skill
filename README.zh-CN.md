
```markdown README.zh-CN.md
# serenity-chokepoint-skill

> Serenity 式供应链卡点投研 Skill：找卡点，建证据，校准“瓶颈理论”。

Skill 引入 TOC / 制约理论作为系统性校准框架，帮助投研用户区分真正的供应链卡点、短期短缺、热门叙事与普通“卡脖子”概念，并避免将 Chokepoint Theory 简化误读为 TOC 意义上的“瓶颈理论”。

这是一个面向投研用户与产业链研究者的 Agent Skill。它把产业热点拆成可验证的研究流程，帮助识别可能被市场低估的供应链卡点，并组织候选公司、证据链、验证路径、风险清单、跟踪指标与假设失效条件。

项目默认使用“供应链卡点 / 卡点理论 / 供应链卡点分析”，并在需要时明确区分 local bottleneck 与 TOC-style constraint。


## V0.3 来源证据边界

Skill 使用可追溯公开来源，并要求区分标注 Serenity 原始公开表达、产业链证据与社区解读。本项目不代表 Serenity 官方授权或认可；所有输出均为研究假设，不构成投资建议。

## 十段输出结构

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

## 核心价值

- 从“热门赛道”回到产业价值链、有效产出和真实供给约束。
- 区分结构性供应链卡点、短期短缺、局部产能问题、热门叙事与普通“卡脖子”概念。
- 用 TOC-informed CCR 检查校准系统边界、有效产出、制约释放与制约迁移。
- 把候选公司与可追溯证据绑定，明确支持证据、反证、验证路径和置信度。
- 保留估值、替代、扩产、客户压价、政策监管及研究假设失效风险。

Chokepoint Theory 关注供应链中的关键卡点与价值捕获，不宜自动等同于 TOC / 制约理论。只有在定义系统目标、系统边界和有效产出后，才能判断某环节是否构成 TOC-style constraint；日常所说的“瓶颈”也可能只是 local bottleneck 或 supply-chain chokepoint。

## 适用场景

- A 股 AI 半导体或其他产业链的卡点扫描。
- AI 基建价值链中的供需错配、替代难度和扩产周期分析。
- 判断某环节是真正卡点，还是短期短缺或市场叙事。
- 为候选卡点生成公司筛选框架、证据表与持续跟踪指标。
- 校准中文文章中对 Chokepoint Theory 与“瓶颈理论”的混用。

## 使用方式

### Agent Skills-compatible clients

```bash
git clone https://github.com/hlamt/serenity-chokepoint-skill.git