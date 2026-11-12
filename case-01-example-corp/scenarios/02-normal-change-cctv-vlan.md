# Scenario 2 — Normal change (BAU): "Add a CCTV VLAN"

| | |
|---|---|
| **Kind** | Normal change (business as usual) |
| **Playbook stage** | 6 Build oversight (change control) and 7 Test and go-live |
| **Related Case 01 documents** | [LLD network](../03-design/lld-network.md) · [threat model](../04-security-cost/threat-model.md) |

> Fictional scenario for **Example Corp**. Terms in the right-hand column are explained in the
> [glossary](https://github.com/fridayn8/sa-handbook/blob/main/architecture/glossary.md).

| # | What happens | Terms |
|---|--------------|-------|
| 1 | Facility manager requests isolated network for cameras | Service request, Stakeholder |
| 2 | Issue created; small design update (reserved VLAN 70, firewall rules: cameras → NVR only) | LLD, Segmentation, PoLP |
| 3 | Branch `feat/opnsense-cctv-vlan`, Ansible + docs changed, PR opened | Branch, PR, Conventional Commits, IaC |
| 4 | CI: lint, policy checks; reviewer checks rule matrix | Quality gate, Policy as code, Code review |
| 5 | Merged → applied to LAB → verified | GitOps, Environment, Smoke test |
| 6 | RFC (normal change, low risk) scheduled for Saturday window; rollback = revert PR + re-apply | RFC, Change type, Maintenance window, Rollback |
| 7 | Applied to production, verified, RFC closed; minor version tag | Deployment, SemVer |

---

[← Scenario 1](01-new-project.md) · [All scenarios](README.md) · [Scenario 3 →](03-incident-app-unreachable.md)
