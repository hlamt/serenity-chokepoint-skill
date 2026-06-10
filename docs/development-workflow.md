# Development Workflow

Every authorization upgrade requires explicit user approval.

| Level | Scope | Examples |
| --- | --- | --- |
| L0 | 只读诊断 | Read files, inspect structure, report findings |
| L1 | 本地修改 | Create or edit local project files and run offline checks |
| L2 | 联网抓取 | Access websites, APIs, repositories, X, or external data |
| L3 | commit | Create a git commit or perform related publishing actions |

## Authorization Rule

每轮任务必须在用户明确授权的级别内执行；授权级别随任务而定，不在文档中固定当前状态。超出当轮授权范围的联网、抓取、凭据访问、提交或发布操作，必须先获得新的明确授权。

## Change Loop

1. Confirm the current authorization level.
2. Inspect the local workspace and preserve unrelated user changes.
3. Make narrowly scoped edits.
4. Run offline validation and relevant script checks.
5. Review for secrets, unsupported investment conclusions, and terminology drift.
6. Report files changed, checks run, missing evidence, and the authorization needed for any next phase.
