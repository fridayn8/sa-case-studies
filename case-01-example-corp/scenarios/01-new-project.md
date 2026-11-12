# Scenario 1 — New project (normal): "Secure remote access and public apps"

| | |
|---|---|
| **Kind** | Planned project (normal) |
| **Playbook stage** | The whole engagement, stages 0–8 |
| **Related Case 01 documents** | [requirements](../01-requirements/requirements.md) · [HLD](../03-design/hld.md) · [ADR-0004](../02-options-decisions/adr/0004-remote-access-tailscale-and-wireguard.md) · [ADR-0005](../02-options-decisions/adr/0005-public-ingress-cloudflare-tunnel.md) |

> Fictional scenario for **Example Corp**. Terms in the right-hand column are explained in the
> [glossary](https://github.com/fridayn8/sa-handbook/blob/main/architecture/glossary.md).

| # | What happens | Terms | Artifact |
|---|--------------|-------|-----------------------|
| 1 | Management asks for proposals to secure remote work | RFP, Stakeholder | — |
| 2 | Architect runs discovery workshops; documents current VPN-less setup | Discovery, As-is, BRD, Constraint, Assumption | [requirements](../01-requirements/requirements.md) |
| 3 | Requirements written; downtime cost estimated | FR, NFR, BIA, RTO/RPO | [requirements](../01-requirements/requirements.md) |
| 4 | Options compared: port-forward vs Cloudflare Tunnel; WireGuard vs Tailscale | Trade-off, ADR, PoC | [ADR-0004](../02-options-decisions/adr/0004-remote-access-tailscale-and-wireguard.md), [ADR-0005](../02-options-decisions/adr/0005-public-ingress-cloudflare-tunnel.md), PoC report |
| 5 | Target design drawn and reviewed | HLD, C4, To-be, SPOF, Threat model | [HLD](../03-design/hld.md), [diagrams](../03-design/diagrams/) |
| 6 | Detailed design: VLANs, IPs, firewall rules, VM sizes | LLD, VLAN, CIDR, Capacity planning | [LLDs](../03-design/), [cost and capacity](../04-security-cost/) |
| 7 | Scope, price and timeline agreed | SOW, BoM, TCO, RACI | — |
| 8 | Built as code via PRs | IaC, GitOps, Golden image, PR, CI | IaC in [`sa-projects`](https://github.com/fridayn8/sa-projects/blob/main/projects/example-corp/) |
| 9 | Tested in lab/staging; pilot with 5 users; sign-off | SIT, UAT, Pilot, Regression | Test notes, issues |
| 10 | Go/No-Go → cutover in maintenance window → smoke test | Go/No-Go, RFC, Cutover, Smoke test | Release tag `v1.0.0` |
| 11 | Two weeks of close support; handover to IT ops | Hypercare, Handover, As-built, Runbook | Runbooks, as-built documents |

---

[All scenarios](README.md) · [Scenario 2 →](02-normal-change-cctv-vlan.md)
