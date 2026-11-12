# Architecture Decision Records

Decisions are recorded here following [ADR-0001](0001-record-architecture-decisions.md).
> **"Phase N" in the Confirmation sections** refers to the delivery roadmap of the
> [`sa-projects`](https://github.com/fridayn8/sa-projects/blob/main/ROADMAP.md) repository,
> where each decision is implemented and checked. The ADR text itself is kept as accepted.

To propose a new one: copy [`0000-template.md`](0000-template.md), open an issue with the
**ADR proposal** template, and submit the ADR in a PR with `status: proposed`.

| ADR | Title | Status |
|-----|-------|--------|
| [0001](0001-record-architecture-decisions.md) | Record architecture decisions as ADRs in Git (MADR) | Accepted |
| [0002](0002-hypervisor-proxmox-ve.md) | Use Proxmox VE as the hypervisor | Accepted |
| [0003](0003-firewall-opnsense.md) | Use OPNsense, virtualised on Proxmox, as firewall and router | Accepted |
| [0004](0004-remote-access-tailscale-and-wireguard.md) | Tailscale for admin access, WireGuard for break-glass, Cloudflare Access for staff | Accepted |
| [0005](0005-public-ingress-cloudflare-tunnel.md) | Publish internal web apps through Cloudflare Tunnel with Cloudflare Access | Accepted |
| [0006](0006-iac-terraform-packer-ansible.md) | Split Infrastructure as Code between Terraform, Packer and Ansible | Superseded by 0012 |
| [0007](0007-secrets-sops-age.md) | Encrypt secrets in Git with SOPS and age | Accepted |
| [0008](0008-terraform-state-cloudflare-r2.md) | Store Terraform state in Cloudflare R2 using the S3 backend | Accepted |
| 0009 | *(reserved — off-site backup target, left as [exercise 3](../../../exercises/design-first-exercises.md))* | — |
| [0010](0010-free-only-tooling-policy.md) | Use only free software and free service tiers | Accepted |
| [0011](0011-open-source-first.md) | Prefer open-source tools (except the owner's chosen platform services) | Accepted |
| [0012](0012-opentofu-and-cloud-image-templates.md) | Use OpenTofu, and build VM templates from Debian cloud images instead of Packer | Accepted |

## Candidate future ADRs

| Topic | Trigger |
|-------|---------|
| Second Proxmox node / cluster and HA | Budget or availability target increases (HLD risk R-1) |
| Dedicated firewall appliance or HA pair | Network outages during hypervisor maintenance become unacceptable (R-2) |
| Off-site backup target (USB rotation vs remote PBS) — ADR-0009, [exercise 3](../../../exercises/design-first-exercises.md) | Operations phase of the delivery project |
| Self-hosted runner vs Tailscale GitHub Action for CI access | CI/CD proof of concept |
| IPv6 inside the office | ISP offers stable prefix |
