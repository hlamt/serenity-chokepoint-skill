# Development Workflow

Every authorization upgrade requires explicit user approval.

| Level | Scope | Examples |
| --- | --- | --- |
| L0 | 只读诊断 | Read files, inspect structure, report findings |
| L1 | 本地修改 | Create or edit local project files and run offline checks |
| L2 | 联网抓取 | Access websites, APIs, repositories, X, or external data |
| L3 | commit | Create a git commit or perform related publishing actions |

## Current Authorization

Current level: **L1 local modification only**.

Allowed:

- Create the requested project skeleton and documentation.
- Run local scripts that operate only on repository files.
- Inspect git status and local file structure.

Not allowed without a new explicit authorization:

- Network access or external repository lookup.
- X scraping or cookie/session access.
- LLM or external API calls from project scripts.
- Reading or writing secrets.
- Git commit, push, release, or publication.

## Change Loop

1. Confirm the current authorization level.
2. Inspect the local workspace and preserve unrelated user changes.
3. Make narrowly scoped edits.
4. Run offline validation and relevant script checks.
5. Review for secrets, unsupported investment conclusions, and terminology drift.
6. Report files changed, checks run, missing evidence, and the authorization needed for any next phase.
