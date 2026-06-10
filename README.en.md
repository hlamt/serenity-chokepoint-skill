# serenity-chokepoint-skill

An evidence-backed Agent Skill for Serenity-style supply-chain chokepoint investment research, with TOC-informed terminology guardrails.

## Purpose

Map an industry value chain, define throughput, identify candidate supply-chain chokepoints and exposed companies, and build a traceable evidence and monitoring plan. Outputs remain research hypotheses.

## Use Cases

- Screen AI semiconductor or infrastructure value chains for candidate chokepoints.
- Distinguish structural constraints from temporary shortages and market hype.
- Build candidate-company, evidence, risk, indicator, and invalidation tables.
- Review Chinese terminology around Chokepoint Theory and TOC.

## Terminology Guard

Do not automatically translate Chokepoint Theory as “瓶颈理论”. Default to “供应链卡点”, “卡点理论”, or “供应链卡点分析”. Treat TOC / Theory of Constraints as a systematic calibration framework. When using “bottleneck”, specify whether it means a supply-chain chokepoint, a local bottleneck, or a TOC-style constraint.

## Installation

For Agent Skills-compatible clients:

```bash
git clone https://github.com/<your-org>/serenity-chokepoint-skill.git
python scripts/validate_skill.py
```

Use the repository as a Skill directory, ask the Agent to read `SKILL.md`, load relevant files from `references/` as needed, and reuse prompts from `assets/research-prompt-pack.md`. Compatibility is client-dependent.

## Output Format

1. Research question
2. Value chain
3. Throughput definition
4. Candidate supply-chain chokepoints
5. Candidate companies
6. Evidence table
7. Counterevidence and risks
8. Tracking indicators
9. Invalidation conditions
10. Disclaimer

## Disclaimer

This independent project is not officially authorized by Serenity and is not TOC certification or personality simulation. It uses public information for research and methodology learning. It does not provide investment advice, return promises, or individualized asset allocation. Users bear their own investment risk, and public information may be delayed, incomplete, or wrong.
