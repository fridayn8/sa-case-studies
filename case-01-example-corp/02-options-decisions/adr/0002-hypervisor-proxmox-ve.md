---
status: accepted
date: 2026-11-11
deciders: [fridayn8]
consulted: [IT administrator, IT partner]
informed: [Managing director]
---

# ADR-0002: Use Proxmox VE as the hypervisor

## Context and Problem Statement

Example Corp runs all internal services on one server (constraint C-1). We need a hypervisor
that runs a firewall VM, Linux VMs and lightweight containers, supports backups and
automation, and fits a small budget and a part-time administrator. Which hypervisor should
the platform use?

## Decision Drivers

- Licence cost (NFR-C2, NFR-C3)
- Support for both VMs and lightweight containers on one host
- API and Terraform provider for Infrastructure as Code (FR-10)
- Integrated, efficient backup (FR-08)
- Skills already available (the existing server already runs Proxmox)
- Long-term vendor and community viability

## Considered Options

1. Proxmox VE
2. VMware vSphere / ESXi
3. Microsoft Hyper-V (Windows Server)
4. XCP-ng (with Xen Orchestra)

## Decision Outcome

Chosen option: **"Proxmox VE"**, because it is free to use, runs both KVM VMs and LXC
containers, integrates with Proxmox Backup Server, has a well-maintained Terraform provider
(`bpg/proxmox`), and the team already knows it.

### Consequences

- 👍 Good, because no licence cost; optional subscription only for enterprise repository and support.
- 👍 Good, because LXC containers use far less RAM than VMs for small Linux services.
- 👍 Good, because PBS provides deduplicated, incremental, encrypted backups natively.
- 👎 Bad, because support comes from the vendor subscription or community — no large partner ecosystem like VMware.
- 👎 Bad, because single-node only in this design (no live migration / HA) — accepted in HLD risk R-1.
- ➖ Neutral, because the `no-subscription` repository is fine for the lab; production should use an Enterprise subscription.

### Confirmation

Phase 3 provisions guests through Terraform against the Proxmox API; Phase 8 restore tests
from PBS succeed.

## Pros and Cons of the Options

### Proxmox VE

- 👍 Good, because open source (AGPL), KVM + LXC, built-in ZFS, web UI, REST API.
- 👍 Good, because clustering and HA are available later without changing platform.
- 👎 Bad, because enterprise support depends on subscription tier.

### VMware vSphere / ESXi

- 👍 Good, because industry standard with mature ecosystem and skills market.
- 👎 Bad, because licensing changed significantly after the Broadcom acquisition (bundled
  subscriptions); cost is disproportionate for one small host.
- 👎 Bad, because no native lightweight containers.

### Microsoft Hyper-V

- 👍 Good, because included with Windows Server licences; good Windows integration.
- 👎 Bad, because requires Windows Server licensing and management tooling; Linux/BSD guests are second-class; no LXC.

### XCP-ng

- 👍 Good, because open source with a capable management tool (Xen Orchestra).
- 👎 Bad, because smaller community; no system containers; team has no experience.

## More Information

- Related: [LLD compute](../../03-design/lld-compute.md), [ADR-0006](0006-iac-terraform-packer-ansible.md)
- Amended by [ADR-0010](0010-free-only-tooling-policy.md): no Enterprise subscription; `no-subscription` repository everywhere.
- Revisit if: a second node is purchased (cluster/HA design), or support requirements change.
