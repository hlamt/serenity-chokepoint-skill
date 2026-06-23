# V1.2C Minimal Installation / Symlink Guide

## 一、Purpose

This guide turns the V1.2A / V1.2B installation reviews into a minimal manual installation path.

It is documentation-only. It does not create symlinks, install scripts, adapters, package manifests, README changes, or runtime-specific copies.

After V1.2C, the next step is manual installation testing, not another planning document.

## 二、Canonical Source

The canonical source of truth remains `hlamt/serenity-chokepoint-skill`.

Do not copy `SKILL.md` into runtime-specific folders.

Keep the repo-owned skill as the single source of truth:

```text
~/Projects/serenity-chokepoint-skill
```

Agent-specific discovery paths should point to this canonical repository directly or through a shared skills directory.

## 三、Recommended Directory Model

Future/manual example only; this PR does not execute these commands or create these paths.

Recommended model:

```text
~/Projects/serenity-chokepoint-skill
~/Projects/agent-scripts/skills/serenity-chokepoint-skill -> ../../serenity-chokepoint-skill
~/.codex/skills -> ~/Projects/agent-scripts/skills
~/.claude/skills -> ~/Projects/agent-scripts/skills
```

The intended chain is:

```text
repo-owned canonical skill
-> shared skills directory
-> agent global skill discovery path
```

This keeps one canonical `SKILL.md` and avoids version drift between Codex, Claude, OpenClaw, local runtimes, and manual GitHub usage.

## 四、Codex Symlink Option

Codex should discover the repo-owned canonical skill through shared skills discovery, preferably by symlink.

Future/manual example only:

```bash
mkdir -p ~/Projects/agent-scripts/skills
ln -s ../../serenity-chokepoint-skill ~/Projects/agent-scripts/skills/serenity-chokepoint-skill
ln -s ~/Projects/agent-scripts/skills ~/.codex/skills
```

Guidance:

- no separate Codex copy
- no Codex-specific adapter yet
- no copied `SKILL.md`
- run manual discovery tests before automation

If Codex cannot load the symlinked canonical skill, record the exact loader failure before considering an adapter.

## 五、Claude Symlink Option

Claude should discover the same canonical repo-owned skill through shared skills discovery where possible.

Future/manual example only:

```bash
mkdir -p ~/Projects/agent-scripts/skills
ln -s ../../serenity-chokepoint-skill ~/Projects/agent-scripts/skills/serenity-chokepoint-skill
ln -s ~/Projects/agent-scripts/skills ~/.claude/skills
```

Guidance:

- no separate Claude copy
- no Claude-specific adapter yet
- no copied `SKILL.md`
- use the same shared skills directory as Codex if both runtimes support it

If Claude requires different metadata, manifest shape, or path depth, document the incompatibility before implementing `adapters/claude/`.

## 六、OpenClaw Current Position

OpenClaw remains a compatibility target.

Do not create an OpenClaw adapter yet.

Current position:

- document expected folder layout first
- perform a manual load test later
- verify whether OpenClaw can follow symlinked skill folders
- verify whether OpenClaw requires a manifest, metadata file, or package format

Only create `adapters/openclaw/` if a real load test shows that symlink-first discovery or direct-path loading cannot work.

## 七、Local Runtime Current Position

Local runtime can use direct path loading first:

```text
local runtime config -> ~/Projects/serenity-chokepoint-skill
```

Required minimum:

- `SKILL.md`
- `references/`

Recommended:

- `examples/`
- `evals/`
- `scripts/`
- `docs/`

Local runtime should prefer direct path configuration before symlink or adapter work. If the runtime cannot access `references/` from the canonical repo, document that as a possible adapter trigger.

## 八、Manual Validation Checklist

Before any install automation, manually check:

1. repo exists locally
2. `SKILL.md` exists at repo root
3. `references/` exists
4. symlink resolves correctly
5. global skills path points to shared skills directory
6. `validate_skill.py` passes
7. no duplicate `SKILL.md` copies are created

Suggested manual commands for a future install test:

```bash
pwd
ls -la ~/Projects/serenity-chokepoint-skill/SKILL.md
ls -la ~/Projects/serenity-chokepoint-skill/references
readlink ~/Projects/agent-scripts/skills/serenity-chokepoint-skill
readlink ~/.codex/skills
readlink ~/.claude/skills
cd ~/Projects/serenity-chokepoint-skill
python3 scripts/validate_skill.py
python3 scripts/chokepoint_scorecard.py --template
```

These commands are examples for future manual testing. This PR does not run them against user global paths.

## 九、When To Add Adapters

Only consider adapters if manual install tests show one of these real incompatibilities:

1. runtime requires different manifest format
2. runtime rejects symlinked skill
3. runtime requires different path depth
4. runtime requires additional metadata
5. runtime cannot access `references/` from canonical repo

Adapter files should be thin pointers or metadata layers. They should not duplicate the main `SKILL.md` body.

## 十、When To Add Install Scripts

Do not add install scripts yet.

Consider `scripts/install_check.py` only after manual installation testing defines stable checks, such as:

- canonical repo path exists
- expected files exist
- symlink resolves
- global discovery path points to shared skills directory
- no duplicate `SKILL.md` exists in runtime-specific folders
- validation command passes

Consider `scripts/package_check.py` only after a package format is defined.

## 十一、Explicit Non-Goals

This guide explicitly does not:

1. modify `SKILL.md`
2. modify references / examples / evals
3. add adapters
4. create symlinks
5. write install scripts
6. modify README
7. publish a package
8. connect market data APIs
9. create a ticker linker
10. add source records
11. add method claims
12. perform TOC calibration
13. introduce investment advice capability

## 十二、Recommendation

Use the repo-owned canonical skill plus symlink-first discovery as the initial installation model.

Codex and Claude should discover the same canonical skill through a shared skills directory. OpenClaw should remain a compatibility target until manual load testing clarifies requirements. Local runtimes should start with direct path loading.

Do not implement adapters or install scripts now. The next step is manual installation testing using this guide.
