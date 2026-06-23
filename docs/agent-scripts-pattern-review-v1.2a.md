# V1.2A Agent-Scripts Pattern Review / Installation Layout Review

## 一、Review Scope

This is a review-only installation and packaging layout assessment for `hlamt/serenity-chokepoint-skill`.

The review references the public `steipete/agent-scripts` repository and README as an organizational pattern for shared agent instructions, skills, portable helper scripts, local validation hooks, and symlink-based global discovery.

This review does not change runtime behavior, `SKILL.md`, references, examples, evals, source records, method claims, scripts, README files, or package artifacts.

## 二、Reference Pattern Observed

The `steipete/agent-scripts` repository presents itself as a canonical shared location for agent instructions, reusable skills, small helper scripts, and guardrail hooks. Its public README describes this split:

- `AGENTS.MD` holds shared hard rules for Codex/Claude-style agents.
- `skills/` holds reusable workflow skills, including repo-owned skills exposed by symlink.
- `scripts/` holds dependency-light helpers used across projects.
- `hooks/` holds local guardrails such as skill validation.

The README also states several skill-design norms:

- Keep descriptions short and generic; optimize for routing, not documentation.
- Keep skill bodies terse and operational.
- Prefer helper scripts under a skill when a workflow has repeatable commands.
- Validate after edits.

For discovery, the observed pattern is to point global agent skill locations at the shared skills directory, for example:

- `~/.codex/skills -> ~/Projects/agent-scripts/skills`
- `~/.claude/skills -> ~/Projects/agent-scripts/skills`

Repo-owned skills stay canonical in their owning repositories and are exposed into the shared skills directory through tracked relative symlinks. This avoids copying the same `SKILL.md` into multiple places and reduces version drift.

## 三、Current Serenity Skill Layout

Current Serenity Chokepoint Skill layout already has most of the target layers:

- `SKILL.md`: main skill entry, routing, core workflow, boundary rules, and references.
- `references/`: method maps, evidence ladder, source policy, concept boundaries, translation policy, and risk/compliance notes.
- `examples/`: standard example conversations and minimum usable task examples.
- `evals/`: boundary tests, source tests, smoke tests, and anti-patterns.
- `scripts/`: `validate_skill.py` and `chokepoint_scorecard.py`.
- `docs/`: stage-specific design, review, source governance, method distillation, registry, and workflow notes.
- `data/seed/source-records/`: bounded source records and seed corpus material.
- `assets/`: prompt packs, templates, and scorecard assets.

V1.1E already reduced main `SKILL.md` verbosity and moved more detailed operational guidance into `references/runtime-method-map-v1.1a.md`.

## 四、Fit / Gap Analysis

### Fit

Serenity already fits the agent-scripts pattern in several important ways:

- The main skill entry is moving toward a thin routing and behavior layer rather than a complete paper.
- Detailed guardrails now live primarily in `references/`, especially the runtime method map.
- Examples and evals carry user-facing behavior expectations and boundary tests.
- Scripts already exist for repeatable validation and scorecard template inspection.
- Docs already preserve stage-specific reasoning without making the main skill heavier.

### Gaps

Serenity is not yet installation-ready in the same way as the observed agent-scripts pattern:

- There is no documented installation path for Codex, Claude, OpenClaw, or local runtimes.
- There is no symlink or global discovery guide.
- There is no adapter layout or adapter policy.
- There is no package or release checklist.
- The existing helper scripts are validation-oriented but not yet organized as install-check or package-check commands.
- `README` does not yet explain how a user should install or expose the skill to different agents.

### Still Slightly Thick

`SKILL.md` is slimmer after V1.1E, but it still serves several roles at once:

- trigger description
- workflow description
- core output contract
- terminology guard
- risk disclaimer
- references index

This is acceptable for the current stage, but future additions should avoid expanding the main skill. New detail should go to `references/`, `examples/`, `evals/`, `scripts/`, or installation docs.

## 五、Recommended Target Layout

The recommended target layout is:

```text
SKILL.md
references/
examples/
evals/
scripts/
docs/
```

Layer responsibilities:

- `SKILL.md`: short, thin, responsible for routing, core behavior, and non-negotiable boundaries.
- `references/`: method mapping, boundary notes, detailed guardrails, source policy, evidence policy, and installation-adjacent details that are too verbose for the main skill.
- `examples/`: standard output samples and user-facing behavior patterns.
- `evals/`: boundary tests, smoke tests, failure modes, and regression checks.
- `scripts/`: validation, install checks, package checks, and other repeatable helper workflows.
- `docs/`: stage reviews, packaging design, installation plans, adapter decisions, and migration notes.

The target should not create duplicate `SKILL.md` files for each agent. The repo-owned skill should remain canonical here, with future adapters or symlinks exposing it elsewhere.

## 六、Installation / Adapter Options

### Option A: Repo-Owned Skill With Symlink Exposure

Keep Serenity Chokepoint Skill canonical in this repository and expose it to shared skill discovery through symlinks.

Possible future pattern:

```text
agent-scripts/skills/serenity-chokepoint-skill -> ../../serenity-chokepoint-skill
~/.codex/skills -> ~/Projects/agent-scripts/skills
~/.claude/skills -> ~/Projects/agent-scripts/skills
```

Advantages:

- avoids copying `SKILL.md`
- preserves one source of truth
- keeps source records and references close to the skill
- works with a shared agent-scripts style discovery layer

Risks:

- consumers need clear path assumptions
- relative symlinks can be brittle across machines
- agent-specific loaders may expect different folder depth or metadata conventions

### Option B: Documented Adapters Only

Add documentation that explains how Codex, Claude, OpenClaw, or local runtimes should discover the repo-owned skill, without creating adapter directories yet.

This is the recommended near-term option.

Advantages:

- low maintenance
- avoids premature adapter abstractions
- keeps the next work review-oriented
- lets real install attempts reveal actual needs

### Option C: Adapter Directories

Possible future layout:

```text
adapters/
  codex/
  claude/
  openclaw/
  local-runtime/
```

This should be deferred until there are concrete differences between agent runtimes that cannot be handled by README instructions, symlinks, or small install-check scripts.

## 七、What To Do Now

Recommended next steps:

1. Do not continue adding rules to `SKILL.md`.
2. Keep `SKILL.md` thin and stable.
3. Add an installation review or matrix document before implementing adapters.
4. Document a symlink-first installation option.
5. Define what a successful local install check should verify.
6. Keep validation scripts as the first repeatable operational surface.
7. Consider a future `docs/installation-matrix.md` before adding `adapters/`.

Near-term script review should consider whether existing helpers can be wrapped or documented as:

```text
validate
scorecard
install-check
package-check
```

This round should not implement those wrappers.

## 八、What To Defer

Defer:

- `adapters/` directory creation
- agent-specific skill copies
- package publishing
- marketplace metadata
- install scripts that mutate user global directories
- symlink automation
- ticker linker
- market data or quote API integration
- new runtime behavior
- new source records
- new method claims
- TOC calibration

Defer README installation edits until the installation matrix is clearer.

## 九、Explicit Non-Goals

This review explicitly does not:

1. add investment advice capability
2. connect market data APIs
3. create a ticker linker
4. implement installation
5. modify `SKILL.md`
6. modify examples or evals
7. create source records
8. create method claims
9. perform TOC calibration
10. publish a package

It also does not change scripts, references, README files, data, assets, or runtime behavior.

## 十、Recommendation

Serenity Chokepoint Skill should not continue thickening `SKILL.md` as the next step.

The recommended direction is:

- keep the main Skill thin and stable
- keep detailed rules in `references/`
- keep behavior guarantees in `examples/` and `evals/`
- keep repeatable checks in `scripts/`
- review installation, adapter, symlink, and packaging layout before implementation

The next practical planning artifact should be an installation or adapter layout document, not another main-skill rule patch. A symlink-first, repo-owned canonical skill model appears suitable, but implementation should wait until installation requirements across Codex, Claude, OpenClaw, and local runtimes are documented.
