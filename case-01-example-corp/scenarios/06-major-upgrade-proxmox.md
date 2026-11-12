# Scenario 6 — Planned major change: "Proxmox major-version upgrade"

| | |
|---|---|
| **Kind** | Planned major change |
| **Playbook stage** | 9 Review (lifecycle debt) and a new change cycle |
| **Related Case 01 documents** | [ADR-0002](../02-options-decisions/adr/0002-hypervisor-proxmox-ve.md) · [LLD compute](../03-design/lld-compute.md) |

> Fictional scenario for **Example Corp**. Terms in the right-hand column are explained in the
> [glossary](https://github.com/fridayn8/sa-handbook/blob/main/architecture/glossary.md).

| # | What happens | Terms |
|---|--------------|-------|
| 1 | Vendor announces end of support for current version | Lifecycle, Risk |
| 2 | Upgrade rehearsed in nested lab; issues documented | PoC/rehearsal, Environment parity |
| 3 | Plan: full backups, step-by-step cutover, checkpoints, rollback point (restore from backup) | Cutover plan, Rollback, Runbook |
| 4 | RFC (normal, high risk) → CAB approval; scheduled outside month-end freeze | RFC, CAB, Change freeze, Maintenance window |
| 5 | Go/No-Go one hour before: backups verified, staff informed | Go/No-Go |
| 6 | Upgrade executed; smoke tests per VM; monitoring watched | Smoke test, Hypercare |
| 7 | Docs and ADR updated; RFC closed | As-built, ADR |

---

[← Scenario 5](05-disaster-storage-failure.md) · [All scenarios](README.md)
