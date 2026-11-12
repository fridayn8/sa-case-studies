---
status: superseded by ADR-0012
date: 2026-11-11
deciders: [fridayn8]
consulted: [IT partner]
informed: [IT administrator]
---

# ADR-0006: Split Infrastructure as Code between Terraform, Packer and Ansible

> **Superseded by [ADR-0012](0012-opentofu-and-cloud-image-templates.md)** — OpenTofu replaces
> Terraform, and official cloud images replace Packer. Kept unchanged below for history.

## Context and Problem Statement

All infrastructure should be defined in Git and changed through pull requests (FR-10, BG-4).
The platform has three kinds of things to automate: **resources in APIs** (Proxmox guests,
Cloudflare DNS/Tunnel/Access, Tailscale settings), **machine images**, and **configuration
inside machines** (packages, services, OPNsense settings). Which tools should own what?

## Decision Drivers

- Declarative, reviewable plans before changes (`plan` in PRs)
- Mature providers for Proxmox, Cloudflare and Tailscale
- Idempotent configuration of Linux hosts and OPNsense
- Industry relevance (learning goal) and community support
- Clear ownership — each setting managed by exactly one tool (avoid fights and drift)

## Considered Options

1. Terraform + Packer + Ansible (each for its strength)
2. Terraform only (with provisioners / cloud-init for everything inside machines)
3. Ansible only (including API modules for Proxmox and Cloudflare)
4. Pulumi (general-purpose language) + Ansible

## Decision Outcome

Chosen option: **"Terraform + Packer + Ansible"** with a strict ownership split:

| Layer | Tool | Owns |
|-------|------|------|
| Images | **Packer** | Proxmox VM templates (`tpl-debian-vm-YYYY-MM`) |
| Resources via APIs | **Terraform** | Proxmox VMs/LXCs, pools, tags; Cloudflare DNS, Tunnel, Access; Tailscale settings & keys |
| Inside machines | **Ansible** | OS baseline, app installation, `cloudflared`/Tailscale services, OPNsense (via `ansibleguy.opnsense`) |
| Policy files | **Git + CI action** | Tailscale ACL (`policy.hujson`) |

Terraform passes outputs (IPs, hostnames) to Ansible through a generated inventory.

### Consequences

- 👍 Good, because each tool does what it is best at; plans are readable for reviewers.
- 👍 Good, because the three tools are widely used — strong learning and career value.
- 👎 Bad, because three tools to learn and keep updated; hand-off between Terraform and Ansible must be designed.
- 👎 Bad, because Terraform state must be stored securely (remote backend, Phase 2).
- ➖ Neutral, because OPNsense automation coverage is partial; settings not covered stay manual and are documented in the LLD.

### Confirmation

Phase 3–6: a second `terraform plan` and a second Ansible run after apply both report
**no changes** (idempotency check in CI).

## Pros and Cons of the Options

### Terraform + Packer + Ansible (chosen)

- 👍 Good, because clear separation of provisioning, imaging and configuration.
- 👎 Bad, because more tooling.

### Terraform only

- 👍 Good, because one tool and one state.
- 👎 Bad, because provisioners are a last resort; in-guest configuration and OPNsense settings are poorly covered.

### Ansible only

- 👍 Good, because one tool, agentless, procedural flexibility.
- 👎 Bad, because no plan/state model — harder to preview changes and detect drift for API resources.

### Pulumi + Ansible

- 👍 Good, because real programming languages, testing.
- 👎 Bad, because smaller community for Proxmox; less common in infrastructure job market than Terraform.

## More Information

- Related: [tools stack](https://github.com/fridayn8/sa-handbook/blob/main/architecture/tools-stack.md), [ADR-0007](0007-secrets-sops-age.md), [roadmap](https://github.com/fridayn8/sa-projects/blob/main/ROADMAP.md)
- OpenTofu is a drop-in open-source alternative to Terraform; revisit if licensing matters.
