# Release Notes v0.5 — Minimum Safe Callable Skill Baseline

## 1. Status

serenity-chokepoint-skill v0.5 is a minimum safe callable Agent Skill baseline for Serenity-style supply-chain chokepoint investment research framing.

- It is callable as an Agent Skill.
- It is not a complete end-user investment research product.
- It does not collect external data.
- It does not scrape X.
- It does not provide investment advice.

## 2. What this Skill is for

This Skill is designed to:

- frame Serenity-style supply-chain chokepoint research questions;
- distinguish chokepoint hypotheses from shortage narratives, social-media heat, and generic supply constraints;
- structure Source Digest records;
- transfer bounded source claims into evidence-table inputs;
- generate research hypotheses, missing checks, counterevidence, and invalidation conditions.

## 3. What this Skill is not for

This Skill is:

- not a trading system;
- not an investment adviser;
- not a buy/sell signal generator;
- not a Serenity impersonation tool;
- not an official Serenity statement;
- not an X scraper;
- not a bulk social-media ingestion system;
- not a confirmed-company-winner detector.

## 4. Current file structure

| File | Purpose |
| --- | --- |
| `SKILL.md` | Primary Agent Skill entry point, workflow, output contract, and safety boundaries. |
| `README.en.md` | English project overview and usage guidance. |
| `README.zh-CN.md` | Simplified Chinese project overview and usage guidance. |
| `references/source-types.md` | Source-type taxonomy and labeling guidance. |
| `references/serenity-source-policy.md` | Attribution, quotation, paraphrase, endorsement, and impersonation boundaries. |
| `docs/source-evidence-plan.md` | Plan for bounded, traceable source evidence handling. |
| `docs/source-digest-workflow.md` | Workflow for creating and transferring Source Digest records. |
| `assets/source-digest-template.md` | Reusable Source Digest record template. |
| `assets/chokepoint-scorecard.json` | Structured opportunity and risk framing dimensions. |
| `examples/manual-source-digest-example.md` | Synthetic manual Source Digest example. |
| `examples/manual-source-digest-demo-conversation.md` | Demonstration of a bounded manual Source Digest interaction. |
| `evals/source-boundary-test-cases.md` | Test cases for source attribution and usage boundaries. |
| `evals/source-digest-test-cases.md` | Test cases for Source Digest structure and safety behavior. |
| `scripts/validate_skill.py` | Offline structural, consistency, schema, and language-boundary validation. |
| `scripts/chokepoint_scorecard.py` | CLI for inspecting the local scorecard template. |

## 5. Completed baseline history

| Version | Baseline | Main commit |
| --- | --- | --- |
| V0.2 | Contract Consistency Baseline | `894391d` |
| V0.3A | Source Evidence Docs | `ef9df74` |
| V0.3B | Validation Light Checks | `9ffc426` |
| V0.4 | Source Digest Template | `88cee82` |
| V0.4B | Source Digest Validation | `be006c6` |
| V0.5 | Manual Source Digest Example | `5e3caa7` |

## 6. Current callable capabilities

The current Skill can support:

1. chokepoint research framing;
2. source type labeling;
3. Source Digest creation;
4. evidence table transfer;
5. scorecard-based opportunity/risk framing;
6. missing checks generation;
7. counterevidence and invalidation conditions;
8. non-investment-advice boundary enforcement;
9. Serenity attribution / impersonation boundary enforcement.

## 7. Current validation coverage

The current `validate_skill.py` provides offline checks covering:

- basic file presence;
- frontmatter / H1 where applicable;
- output contract consistency;
- evidence schema;
- scorecard structure and polarity;
- source evidence files;
- Source Digest files;
- high-risk language boundary checks.

This is a summary of the current validator and does not imply unimplemented CI or automated test coverage.

## 8. Known non-goals

1. no X scraping;
2. no twscrape integration;
3. no external API collection;
4. no automatic company screening;
5. no real company conclusion;
6. no investment advice;
7. no buy/sell instruction;
8. no return promise;
9. no live market data;
10. no automated Serenity content collection;
11. no claim of Serenity endorsement.

## 9. Recommended invocation boundary

- Default invocation should start from `SKILL.md`.
- Supporting files should be loaded only when needed.
- Examples and evals should not be loaded by default.
- Full invocation contract will be defined in the next V0.7 step.

## 10. Next step

The next step is:

`CP-SERENITY-CHOKEPOINT-SKILL-V07-INVOCATION-CONTRACT-01`

Its objective is to define lightweight calling boundaries so the Skill can be invoked without loading docs, examples, evals, and development materials by default.

## 11. Final boundary note

This release baseline uses no real Serenity original text, performs no X scraping, accesses no secrets, produces no real company conclusions, and is not investment advice.
