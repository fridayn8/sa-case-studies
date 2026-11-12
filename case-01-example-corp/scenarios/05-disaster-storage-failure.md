# Scenario 5 — Disaster: "Proxmox server storage failure"

| | |
|---|---|
| **Kind** | Disaster |
| **Playbook stage** | 7 Test and go-live (DR test) and 8 Handover and operate |
| **Related Case 01 documents** | [requirements (RTO/RPO)](../01-requirements/requirements.md) · [LLD compute (backup)](../03-design/lld-compute.md) · [capacity plan](../04-security-cost/capacity-planning.md) |

> Fictional scenario for **Example Corp**. Terms in the right-hand column are explained in the
> [glossary](https://github.com/fridayn8/sa-handbook/blob/main/architecture/glossary.md).

| # | What happens | Terms |
|---|--------------|-------|
| 1 | All VMs down, including OPNsense → office offline. SEV1 | Incident, Severity, SPOF |
| 2 | Incident commander declares a **disaster**; DR plan invoked | DR, DRP, Escalation |
| 3 | Business switches to manual workarounds (mobile hotspots, cloud email continues) | BCP |
| 4 | Replacement hardware/disks installed; Proxmox reinstalled from documented build | As-built, Runbook, IaC |
| 5 | VMs restored from Proxmox Backup Server, most critical first (OPNsense → DNS → apps) | Backup, RTO, Restore priority |
| 6 | Data from last night's backup → up to 24 h of changes lost (within RPO) | RPO |
| 7 | Service restored in 6 h (target RTO 8 h ✅) | RTO, MTTR |
| 8 | Postmortem; ADR to evaluate second node / off-site replica | Postmortem, ADR, HA, Trade-off |

---

[← Scenario 4](04-security-incident-token-in-git.md) · [All scenarios](README.md) · [Scenario 6 →](06-major-upgrade-proxmox.md)
