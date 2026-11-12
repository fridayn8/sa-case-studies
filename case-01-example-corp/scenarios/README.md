# Case 01 — Scenarios

Six short, time-ordered stories about **Example Corp** (25 staff, one office, Proxmox + OPNsense +
WireGuard + Tailscale + Cloudflare). The design documents show *what* was built; the scenarios
show *how the people and processes around it behave*: a new project, a normal change, an
incident, a security incident, a disaster and a planned major upgrade.

Each scenario is a table of steps. The right-hand column names the terms involved; every term
is defined in the [glossary](https://github.com/fridayn8/sa-handbook/blob/main/architecture/glossary.md). The lifecycle and the chains of
terms behind these scenarios are in the
[lifecycle and term chains](https://github.com/fridayn8/sa-handbook/blob/main/architecture/lifecycle-and-term-chains.md) page of the handbook.

| # | Scenario | Kind | Playbook stage |
|---|----------|------|----------------|
| 1 | [New project: secure remote access and public apps](01-new-project.md) | Planned project (normal) | The whole engagement, stages 0–8 |
| 2 | [Add a CCTV VLAN](02-normal-change-cctv-vlan.md) | Normal change (business as usual) | 6 Build oversight (change control) and 7 Test and go-live |
| 3 | [Public web app unreachable](03-incident-app-unreachable.md) | Incident (SEV2) | 8 Handover and operate |
| 4 | [API token committed to Git](04-security-incident-token-in-git.md) | Security incident | 8 Handover and operate |
| 5 | [Proxmox storage failure](05-disaster-storage-failure.md) | Disaster | 7 Test and go-live (DR test) and 8 Handover and operate |
| 6 | [Proxmox major-version upgrade](06-major-upgrade-proxmox.md) | Planned major change | 9 Review (lifecycle debt) and a new change cycle |

## How to use them

1. Read the scenario **before** the matching playbook stage, and underline what surprises you.
2. Read the scenario again after the stage and check which question of the stage it answers.
3. Change one fact (for example "RTO is 2 hours, not 8") and trace what would break.
