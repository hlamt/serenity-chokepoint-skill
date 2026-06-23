# V1.2B Installation Matrix / Adapter Layout Review

## 一、Review Scope

This is a review-only and planning-only document for Serenity Chokepoint Skill installation and adapter layout.

It carries forward the V1.2A conclusion: keep `SKILL.md` thin, keep detailed rules in `references/`, use `examples/` and `evals/` for behavior guarantees, use `scripts/` for repeatable checks, and review installation / adapter / symlink / packaging layout before implementation.

This document does not implement installation, create adapters, create symlinks, write install scripts, publish packages, or change runtime behavior.

## 二、Current Canonical Skill Location

The canonical source of truth for Serenity Chokepoint Skill should remain:

```text
hlamt/serenity-chokepoint-skill
```

The repository-owned skill should remain the single canonical copy. Do not copy multiple `SKILL.md` files into separate agent directories. Any future Codex, Claude, OpenClaw, or local-runtime exposure should point back to the repo-owned canonical skill through documentation, symlink, or adapter metadata.

Current canonical files include:

- `SKILL.md`
- `references/`
- `examples/`
- `evals/`
- `scripts/`
- `docs/`
- `assets/`
- `data/seed/source-records/`

## 三、Target Installation Matrix

| Runtime / Agent | Discovery mechanism | Expected skill location | Required files | Optional files | Adapter needed now? | Install method | Validation method | Risk | Recommendation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Codex | Global or workspace skill discovery, potentially via `~/.codex/skills` | Repo-owned skill exposed through shared skills directory or direct workspace path | `SKILL.md`, `references/`, `examples/`, `evals/` | `scripts/`, `docs/`, `assets/` | No | Document symlink-first or direct repo usage; do not implement yet | `python3 scripts/validate_skill.py`, manual load check later | Path depth or skill discovery expectations may differ by Codex surface | Start with installation guide and symlink guide |
| Claude | Global skill discovery, potentially via `~/.claude/skills` | Same repo-owned skill exposed through shared skills directory | `SKILL.md`, `references/`, `examples/`, `evals/` | `scripts/`, `docs/`, `assets/` | No | Document symlink-first; do not copy files | Existing validation plus future Claude load check | Claude skill packaging expectations may require metadata or folder shape changes | Defer adapter until real load tests require it |
| OpenClaw | Shared skill folder or project-local skill discovery | Repo-owned skill or symlink from shared skill registry | `SKILL.md`, `references/`, `examples/`, `evals/` | `scripts/`, `docs/` | Not yet | Document expected layout only | Existing validation plus future OpenClaw compatibility check | Runtime may expect different manifest or package conventions | Do not create adapter until requirements are known |
| Local runtime | Explicit path loading or local harness configuration | Direct path to this repository | `SKILL.md`, `references/` | `examples/`, `evals/`, `scripts/`, `docs/` | No | Manual path configuration in local harness | `validate_skill.py`, future install-check | Local harnesses may ignore examples/evals or require custom manifests | Keep direct path usage documented |
| Manual GitHub repo usage | User reads or clones repository | GitHub repo clone | `SKILL.md`, `references/`, `examples/`, `evals/` | all repo docs and scripts | No | Clone or browse repo; no agent install | `validate_skill.py` after clone | Users may confuse research framework with installable runtime package | Provide clear install/readme guidance later |

## 四、Codex Installation Path

Recommended near-term Codex path:

```text
repo-owned canonical skill
-> shared skills directory
-> ~/.codex/skills discovery path
```

Possible future layout:

```text
agent-scripts/skills/serenity-chokepoint-skill -> ../../serenity-chokepoint-skill
~/.codex/skills -> ~/Projects/agent-scripts/skills
```

Current recommendation:

- Do not copy `SKILL.md` into `~/.codex/skills`.
- Do not create Codex-specific adapter files yet.
- Document how Codex should discover the repo-owned skill.
- Later, run a real Codex load test before adding install automation.

## 五、Claude Installation Path

Recommended near-term Claude path:

```text
repo-owned canonical skill
-> shared skills directory
-> ~/.claude/skills discovery path
```

Possible future layout:

```text
agent-scripts/skills/serenity-chokepoint-skill -> ../../serenity-chokepoint-skill
~/.claude/skills -> ~/Projects/agent-scripts/skills
```

Current recommendation:

- Use the same canonical skill folder where possible.
- Do not maintain a separate Claude copy.
- Do not create `adapters/claude/` until Claude-specific metadata, manifest, path depth, or package requirements are observed.
- Document expected behavior before implementation.

## 六、OpenClaw Installation Path

OpenClaw should be treated as a compatibility target, not an implementation target yet.

Near-term path:

- document the expected canonical folder shape
- document how OpenClaw would point at the repo-owned skill or symlinked shared skill
- avoid adding an `adapters/openclaw/` directory until concrete loader differences are known

Potential adapter triggers:

- OpenClaw requires a different manifest format
- OpenClaw expects a different skill root path
- OpenClaw requires tool declarations not used by Codex or Claude
- OpenClaw package format cannot follow symlinks

## 七、Local Runtime Installation Path

Local runtime usage should initially be direct-path based:

```text
local runtime config -> /path/to/serenity-chokepoint-skill
```

Required minimum files:

- `SKILL.md`
- `references/`

Recommended files:

- `examples/`
- `evals/`
- `scripts/`
- `docs/`

Local runtime validation can start with:

```bash
python3 scripts/validate_skill.py
python3 scripts/chokepoint_scorecard.py --template
```

Future local checks may include path discovery, frontmatter parsing, reference link checks, and a smoke prompt run, but this round does not implement them.

## 八、Symlink-First Option

The symlink-first option is the preferred near-term installation model to review further.

Proposed chain:

```text
repo-owned canonical skill
-> shared skills directory
-> agent global skill discovery path
```

Example:

```text
agent-scripts/skills/serenity-chokepoint-skill -> ../../serenity-chokepoint-skill
~/.codex/skills -> ~/Projects/agent-scripts/skills
~/.claude/skills -> ~/Projects/agent-scripts/skills
```

Benefits:

- keeps a single source of truth
- avoids multiple `SKILL.md` copies
- lets multiple agents discover the same skill
- keeps references, examples, evals, scripts, and docs together

Risks:

- path assumptions vary across machines
- symlink handling may differ by runtime
- relative symlinks may break if repositories move
- package publishing may not preserve symlinks

Recommendation:

- document symlink-first
- do not create symlinks in this repository yet
- test manually before automation

## 九、Adapter Directory Option

Potential future layout:

```text
adapters/
  codex/
  claude/
  openclaw/
  local-runtime/
```

Do not create this directory now.

Adapter implementation should start only if real runtime tests show incompatible requirements such as:

- different metadata or manifest formats
- different path-depth assumptions
- different allowed file layout
- different tool declaration or permission metadata
- package format that cannot use repo-owned canonical paths

If adapters become necessary, each adapter should be thin and should point back to canonical content rather than duplicating the skill body.

## 十、Recommended Near-Term Path

Recommended next step:

1. Keep Serenity as a repo-owned canonical skill.
2. Do not implement adapters yet.
3. Write `docs/installation-guide-v1.2c.md` before changing README.
4. Include Codex, Claude, OpenClaw, local runtime, and manual GitHub usage in that guide.
5. Document symlink-first as the preferred initial model.
6. Define what an install check should test.
7. Only after manual install tests, decide whether README needs an installation section.

README installation text should wait until the installation guide is stable enough to summarize.

## 十一、Deferred Implementation Work

Defer:

- `adapters/` directory
- symlink creation
- install scripts
- `scripts/install_check.py`
- `scripts/package_check.py`
- README install section
- packaging manifests
- package publishing
- marketplace metadata
- runtime-specific manifests
- automated load tests

Potential future script responsibilities:

- `install_check.py`: verify expected files, symlink resolution, frontmatter parsing, and runtime-visible path.
- `package_check.py`: verify that a packaging candidate includes required files and excludes source-governance-only artifacts if needed.

No such scripts should be added in this round.

## 十二、Explicit Non-Goals

This review explicitly does not:

1. modify `SKILL.md`
2. modify references / examples / evals
3. create an adapter directory
4. create symlinks
5. write installation scripts
6. publish a package
7. connect market data APIs
8. create a ticker linker
9. add source records
10. add method claims
11. perform TOC calibration
12. introduce investment advice capability

It also does not modify scripts, data, assets, README files, source records, or method claim files.

## 十三、Recommendation

Serenity Chokepoint Skill should not enter installation implementation yet.

Recommended direction:

- keep the repo-owned canonical skill in `hlamt/serenity-chokepoint-skill`
- do not copy `SKILL.md` into runtime-specific folders
- do not create `adapters/` yet
- prepare an installation guide or symlink guide next
- document Codex / Claude / OpenClaw / local runtime loading expectations
- run manual install tests before adding adapters or install-check scripts

Only move into adapter implementation when real installation tests reveal incompatibilities that documentation and symlink-first discovery cannot solve.
