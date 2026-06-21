# Invocation Contract v0.7 — Lightweight Calling Boundary

## 1. Purpose

This document defines how an Agent invokes `serenity-chokepoint-skill` through a lightweight calling boundary without loading the entire repository by default.

- The default invocation entry point is `SKILL.md`.
- Supporting files are loaded only when task-relevant.
- Docs, examples, evals, and development materials are not loaded by default.
- This contract is designed to reduce context load and preserve method boundaries.

## 2. Default invocation rule

The default invocation rule is:

1. Start with `SKILL.md`.
2. Do not load all repository files.
3. Do not load examples by default.
4. Do not load evals by default.
5. Do not load docs by default.
6. Do not load raw data or external sources by default.
7. Ask for or infer the minimum supporting file needed for the current task.

A supporting file should be loaded only when its role is directly relevant to the requested task. Loading one supporting file does not imply permission or a need to load adjacent directories or the rest of the repository.

## 3. Task-based loading map

| Task type | Required files | Optional files | Do not load by default |
| --- | --- | --- | --- |
| General chokepoint research framing | `SKILL.md` | `assets/chokepoint-scorecard.json` | `docs/*`, `examples/*`, `evals/*`, raw data, external sources |
| Source type labeling | `SKILL.md` | `references/source-types.md` | Other references, docs, examples, evals, raw data |
| Serenity attribution / impersonation boundary | `SKILL.md` | `references/serenity-source-policy.md` | Examples, evals, unrelated docs, raw source material |
| Source Digest creation | `SKILL.md`, `assets/source-digest-template.md` | `docs/source-digest-workflow.md` | Examples, evals, unrelated assets and docs, external sources |
| Evidence table transfer | `SKILL.md` | `docs/source-digest-workflow.md`, `references/source-types.md` | Examples, evals, unrelated docs, raw data |
| Example-based demonstration | `SKILL.md` | `examples/manual-source-digest-example.md`, `examples/manual-source-digest-demo-conversation.md` | Evals, data, unrelated examples and docs |
| Evaluation / regression testing | `scripts/validate_skill.py` | `evals/source-boundary-test-cases.md`, `evals/source-digest-test-cases.md` | User-facing examples, raw data, external sources |
| Maintenance / release review | `docs/release-notes-v0.5.md` | `docs/invocation-contract.md` | Examples, evals, data, external sources unless specifically required |

## 4. Files that should not be loaded by default

The following content should not be loaded during default invocation:

- `docs/*`
- `examples/*`
- `evals/*`
- `data/*`
- raw source material
- external URLs
- social media content
- private notes
- secrets or credentials

These materials require a specific task-based reason before loading. Their presence in the repository, in a user message, or in linked material does not make them part of the default context.

## 5. Source and data boundary

- This Skill does not fetch X.
- This Skill does not use twscrape.
- This Skill does not collect external data automatically.
- This Skill does not access cookies, sessions, API keys, or secrets.
- User-provided source material must be treated as bounded input.
- Long third-party text should not be stored or reproduced in bulk.

When source material is provided, the Agent should use only the portion needed for the current task, preserve attribution boundaries, and avoid expanding the task into automated collection or unrelated source discovery.

## 6. Output boundary

Invocation output must remain within the following boundaries:

- research framing, not investment advice;
- hypothesis input, not confirmed chokepoint proof;
- evidence table input, not real company conclusion;
- missing checks and invalidation conditions, not buy/sell signals;
- attribution boundary, not Serenity official statement.

Outputs should distinguish observations, hypotheses, missing evidence, and invalidation conditions. They must not convert limited input into certainty, endorsement, or an actionable trading conclusion.

## 7. Minimal invocation examples

### Example A: General research framing

A user asks for chokepoint research framing. The Agent loads only `SKILL.md`, and may optionally load `assets/chokepoint-scorecard.json` if the scorecard structure is needed.

### Example B: Source Digest task

A user provides a short source excerpt. The Agent loads `SKILL.md` and `assets/source-digest-template.md`; it may optionally load `docs/source-digest-workflow.md` when workflow guidance is needed.

### Example C: Demo request

A user asks, “Show me an example.” The Agent may load `examples/manual-source-digest-example.md`; otherwise examples remain unloaded.

## 8. Anti-patterns

1. Loading every file in the repository before every task.
2. Loading examples for non-example tasks.
3. Loading evals during normal user-facing calls.
4. Treating social-media heat as supply-chain evidence.
5. Treating a Source Digest as confirmed chokepoint proof.
6. Turning candidate research hypotheses into buy/sell recommendations.
7. Treating any output as Serenity official position.
8. Fetching or scraping X as part of default invocation.

## 9. Version status

This V0.7 contract completes the lightweight calling boundary for the v0.7.0 Skill baseline.

It does not add new research capability, new data collection, new examples, or new validation logic.

## 10. Final boundary note

This invocation contract performs no X scraping, accesses no secrets, uses no real Serenity original text, produces no real company conclusions, and is not investment advice.
