# Scenario 3 — Incident (SEV2): "Public web app unreachable"

| | |
|---|---|
| **Kind** | Incident (SEV2) |
| **Playbook stage** | 8 Handover and operate |
| **Related Case 01 documents** | [HLD §7](../03-design/hld.md#7-operations-monitoring-backup-and-recovery) · [LLD compute](../03-design/lld-compute.md) |

> Fictional scenario for **Example Corp**. Terms in the right-hand column are explained in the
> [glossary](https://github.com/fridayn8/sa-handbook/blob/main/architecture/glossary.md).

| Time | What happens | Terms |
|------|--------------|-------|
| 09:02 | Uptime monitor alerts: `app.example.com` returns errors | Monitoring, Alerting, SLI, MTTD |
| 09:05 | On-call engineer acknowledges; internal access still works → SEV2 (major function down, workaround exists) | On-call, Incident, Severity |
| 09:10 | Status page updated; staff told to use Tailscale path | Communication, Workaround |
| 09:20 | Diagnosis: `cloudflared` VM ran out of disk (logs) and crashed | Troubleshooting, Observability |
| 09:25 | Disk cleaned, service restarted (manual — emergency) → service restored | Emergency change, MTTR, ClickOps |
| 09:40 | Monitoring stable; incident resolved | Resolution |
| Next day | Blameless postmortem: no disk alert, no log rotation | Postmortem, RCA (5 Whys) |
| Next week | PR: log rotation in Ansible role, disk alert at 80 %, runbook "cloudflared disk full" | Problem, Permanent fix, Runbook, Drift (manual fix codified) |

**5 Whys example:** app down → `cloudflared` crashed → disk full → logs never rotated →
baseline role lacked logrotate config → no hardening baseline check for log rotation.
→ *Root cause:* missing baseline item. *Fix:* add to the Ansible `base-hardening` role.

---

[← Scenario 2](02-normal-change-cctv-vlan.md) · [All scenarios](README.md) · [Scenario 4 →](04-security-incident-token-in-git.md)
