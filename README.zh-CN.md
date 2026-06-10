# serenity-chokepoint-skill

> Serenity 式供应链卡点投研 Skill：找卡点，建证据，校准“瓶颈理论”。

Skill 引入 TOC / 制约理论作为系统性校准框架，帮助投研用户区分真正的供应链卡点、短期短缺、热门叙事与普通“卡脖子”概念，并避免将 Chokepoint Theory 简化误读为 TOC 意义上的“瓶颈理论”。

这是一个面向投研用户与产业链研究者的 Agent Skill。它把产业热点拆成可验证的研究流程，帮助识别可能被市场低估的供应链卡点，并组织候选公司、证据链、验证路径、风险清单、跟踪指标与假设失效条件。

项目默认使用“供应链卡点 / 卡点理论 / 供应链卡点分析”，并在需要时明确区分 local bottleneck 与 TOC-style constraint。

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
git clone https://github.com/<your-org>/serenity-chokepoint-skill.git
```

1. 将仓库作为 Skill 目录使用。
2. 让 Agent 首先读取 `SKILL.md`。
3. 根据问题按需读取 `references/`，不要一次加载全部资料。
4. 使用 `assets/research-prompt-pack.md` 中的 Prompt，或套用 `assets/thesis-template.md`。
5. 运行本地校验：`python scripts/validate_skill.py`。

不同客户端的 Skill 加载方式可能不同；本项目只声明面向 Agent Skills-compatible clients，不承诺自动兼容所有客户端。

## 可复制 Prompt

```text
请对【产业主题】进行供应链卡点投研。先定义产业价值链与有效产出，再识别候选供应链卡点，并用 TOC-informed CCR 检查其对系统有效产出的影响、短期替代难度、扩产周期与制约迁移风险。

请输出：候选供应链卡点、候选公司类型或公司池、证据链与待验证事项、验证路径、风险清单、跟踪指标、假设失效条件和免责声明。区分事实、推断与待验证问题；不要把 Chokepoint Theory 自动等同于 TOC 意义上的“瓶颈理论”；不要给出确定性投资结论。
```

更多场景见 [assets/research-prompt-pack.md](assets/research-prompt-pack.md)。

## 输出格式示例

```markdown
# 研究问题
要验证的产业主题、时间范围与系统边界。

# 产业价值链与有效产出
列出关键环节，并说明系统真正要提升的有效产出。

# 候选供应链卡点
逐项说明影响、CCR 特征、替代难度、扩产周期与置信度。

# 候选公司
只形成候选池；说明暴露度、价值捕获逻辑和待验证证据。

# 证据表
记录来源、日期、证据等级、支持或反证关系。

# 反证与风险
列出替代、扩产、需求回落、估值、政策及制约迁移风险。

# 跟踪指标与假设失效条件
给出可观察指标、频率、阈值以及明确的失效信号。

# 免责声明
本输出是研究假设，不构成投资建议。
```

## 仓库结构

```text
SKILL.md       Agent 使用入口
references/    概念边界、TOC 对照、证据与风险参考
assets/        Prompt、研究模板、评分表与检查清单
scripts/       离线校验和 scorecard CLI
examples/      不含真实公司结论的示例骨架
evals/         边界测试、测试问题和反模式
agents/        研究 Agent 行为说明
data/          本地原始与处理数据占位目录
docs/          项目 SoT、蒸馏规则与开发流程
```

## 本地校验

```bash
python scripts/validate_skill.py
python scripts/chokepoint_scorecard.py --template
```

校验只读取本仓库文件，不联网、不读取 cookie，也不需要任何 API key。

## 免责声明

本项目非 Serenity 官方授权，非 TOC 官方认证，也不进行人格模拟。所有输出仅用于公开资料研究与方法论学习，属于研究假设，不构成投资建议、收益承诺或个性化资产配置建议。公开资料可能滞后、不完整或存在错误，用户应独立判断并自行承担投资风险。详见 [DISCLAIMER.md](DISCLAIMER.md)。
