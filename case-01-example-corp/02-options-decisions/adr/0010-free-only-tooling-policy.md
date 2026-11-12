---
status: accepted
date: 2026-11-11
deciders: [fridayn8]
consulted: []
informed: [IT administrator, Managing director]
---

# ADR-0010: Use only free software and free service tiers

## Context and Problem Statement

The lab is a personal learning project and the Example Corp budget for recurring costs is
small. The owner has set a rule: **every tool and service must be usable for free**.
Several earlier documents assumed small paid items (Proxmox subscription, Tailscale plan,
off-site object storage, Infracost). Which tools and tiers satisfy the rule, what limitations
do free tiers bring, and how does the design change?

> Hardware (server, disks, switch) is a one-off purchase, not a tool or service, and is outside
> this rule. In the lab, the existing laptop is used — zero cost.

## Decision Drivers

- Zero recurring cost for software and services
- No loss of the core learning goals (IaC, GitOps, Zero Trust, backups)
- Free tiers must be allowed for the use case (licence / terms)
- Prefer open source where a SaaS free tier is limiting

## Considered Options

1. Keep the original stack with small paid items
2. Free-only stack: open-source software + free SaaS tiers, with documented limitations
3. Fully self-hosted open source (no SaaS at all: Headscale, own reverse proxy, MinIO…)

## Decision Outcome

Chosen option: **"Free-only stack (option 2)"**, because it keeps the architecture and all
learning goals intact at zero recurring cost; option 3 remains the fallback for any SaaS whose
free tier stops fitting.

### Tool-by-tool review

| Area | Tool / service | Free? | Free-tier limits & notes | Change to earlier docs |
|------|----------------|:-----:|--------------------------|------------------------|
| Hypervisor | Proxmox VE | ✅ | Use the **no-subscription** repository (nag dialog, no vendor support) | Amends ADR-0002: no Enterprise subscription, also in "production" |
| Backup | Proxmox Backup Server | ✅ | No-subscription repository | — |
| Firewall | OPNsense Community Edition | ✅ | — | — |
| VPN | WireGuard | ✅ | — | — |
| Admin access | Tailscale **Personal** plan | ✅ | Small number of users/devices; intended for personal use — fine for this personal lab. For a real company beyond the free terms: switch to **Headscale** (open source) | ADR-0004 fallback documented here |
| Ingress / Zero Trust | Cloudflare Free + Zero Trust Free | ✅ | Zero Trust Free covers up to 50 users; Tunnel free | — |
| Terraform state | Cloudflare R2 free tier | ✅ | 10 GB storage + monthly operation quota free; enabling R2 may require a payment method on file (no charge within free tier) — if not acceptable, use a free alternative backend (e.g. GitLab-managed Terraform state) | ADR-0008 unchanged |
| Domain name | Registrar | ❌ **exception** | A domain (~USD 10/year) is needed for Cloudflare Access hostnames. Free options for learning: Cloudflare *quick tunnels* (`*.trycloudflare.com`, no Access) or Tailscale-only access | **Decision needed before Phase 6** |
| IaC | Terraform, Packer (free to use, BSL) / OpenTofu (MPL) | ✅ | Open-source choice made in ADR-0011/0012: OpenTofu, no Packer | — |
| Config mgmt | Ansible | ✅ | — | — |
| Secrets | SOPS + age | ✅ | — | — |
| Monitoring | Prometheus, Grafana OSS, Uptime Kuma | ✅ | — | — |
| Status page | Free-tier status page / uptime SaaS | ✅ | Must run **outside** the office | — |
| Off-site backup | **Rotated encrypted USB disks** (PBS removable datastore) | ✅ (hardware only) | Weekly rotation → off-site RPO 7 days | Replaces paid object storage |
| Cost in PRs | Infracost | ➖ dropped | Prices only public clouds (AWS/Azure/GCP); not useful for Proxmox/Cloudflare | Use the manual cost model |
| Code hosting / CI | GitHub Free | ✅ | See limitations below | — |
| Quality gates | pre-commit, gitleaks, tflint, Checkov, markdownlint, Spectral, OPA/Conftest | ✅ | — | — |

### GitHub Free limitations for a **private** repository

| Feature | Private repo on GitHub Free | Consequence / workaround |
|---------|:---------------------------:|--------------------------|
| Branch protection / rulesets **enforcement** | ❌ (available for public repos, or with Pro/Team) | Local hooks (`no-commit-to-branch`), PR discipline, CI checks visible on PRs. Making the repo public (content is fictional) would enable rulesets |
| Required reviews / CODEOWNERS enforcement | ❌ | CODEOWNERS still requests reviews; not enforced |
| Environments with required reviewers | ❌ | Production-like applies run via manual `workflow_dispatch` |
| Secret scanning / push protection | ❌ (paid add-on for private repos) | gitleaks in pre-commit and in CI |
| GitHub-hosted Actions minutes | ✅ limited monthly quota | Lint jobs are small; heavy jobs on the self-hosted runner (free, unlimited) |

### Consequences

- 👍 Good, because recurring software/service cost is zero (except the domain, decided separately).
- 👍 Good, because everything used is either open source or has a well-known free tier.
- 👎 Bad, because no vendor support (Proxmox, PBS) — community forums and documentation only.
- 👎 Bad, because GitHub Free private repos cannot *enforce* review rules; process discipline and CI replace enforcement.
- 👎 Bad, because off-site backups are weekly and manual (disk rotation) — off-site RPO 7 days.
- ➖ Neutral, because free-tier terms change; they are re-checked yearly and listed in the validation checklist.

### Confirmation

Cost estimate shows USD 0 for software/services (plus the domain if chosen); the validation
checklist includes re-checking free-tier terms before go-live.

## More Information

- Updated documents: [tools stack](https://github.com/fridayn8/sa-handbook/blob/main/architecture/tools-stack.md), [cost estimate](../../04-security-cost/cost-estimate.md),
  [LLD compute §6](../../03-design/lld-compute.md#6-backup-design), [HLD §7](../../03-design/hld.md#7-operations-monitoring-backup-and-recovery),
  [hardening baseline §6](https://github.com/fridayn8/sa-projects/blob/main/projects/example-corp/docs/hardening-baseline.md#6-github-repository-and-ci), [threat model TB-6](../../04-security-cost/threat-model.md#tb-6--github--runner--apis-supply-chain).
- Revisit if: a free tier changes its terms or limits, or the company accepts a budget for support subscriptions.
