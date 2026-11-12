---
status: accepted
date: 2026-11-11
deciders: [fridayn8]
consulted: [IT administrator, IT partner]
informed: [Managing director]
---

# ADR-0003: Use OPNsense, virtualised on Proxmox, as firewall and router

## Context and Problem Statement

The office network is flat (problem P3) and the ISP router port-forwards admin interfaces
(P2). We need a stateful firewall that routes between six VLANs, provides DNS/DHCP, runs a
WireGuard endpoint and can be automated. Which firewall, and should it run on dedicated
hardware or as a VM?

## Decision Drivers

- Inter-VLAN routing with default-deny rules (NFR-S4)
- Built-in WireGuard for break-glass (FR-04)
- DNS resolver with host overrides and DNSSEC (FR-07)
- API / automation support (FR-10)
- Cost — no budget for an appliance in year 1 (C-1)
- Availability impact of placement (HLD risk R-2)

## Considered Options

1. OPNsense as a VM on Proxmox
2. OPNsense on a dedicated small appliance
3. pfSense (CE or Plus)
4. Proxmox built-in firewall only (no separate router)
5. MikroTik RouterOS hardware router

## Decision Outcome

Chosen option: **"OPNsense as a VM on Proxmox"**, because it meets all functional needs at
zero extra cost, has a documented REST API and an Ansible collection, and runs WireGuard
natively. The availability downside is accepted for year 1 and mitigated (see below).

### Consequences

- 👍 Good, because full-featured firewall (aliases, VLANs, Unbound DNS, WireGuard, syslog) for free.
- 👍 Good, because snapshots and PBS backups of the firewall VM make changes reversible.
- 👎 Bad, because Proxmox host maintenance or failure takes the whole network down
  (mitigations: maintenance windows, on-site MGMT access port, restore runbook).
- 👎 Bad, because a hypervisor vulnerability could in theory expose the firewall
  (mitigation: WAN on a dedicated bridge with no host IP, patching).
- ➖ Neutral, because migrating to a dedicated appliance later is a config export/import.

### Confirmation

Phase 4: firewall rules match the [rule matrix](../../03-design/lld-network.md#5-firewall-rule-matrix),
verified with connection tests from each zone; config managed through Ansible.

## Pros and Cons of the Options

### OPNsense as VM

- 👍 Good, because no hardware cost; easy snapshot/rollback.
- 👎 Bad, because shares fate with the hypervisor.

### OPNsense on dedicated appliance

- 👍 Good, because network survives hypervisor maintenance; clearer separation.
- 👎 Bad, because extra hardware cost (and it becomes its own SPOF without HA pair).

### pfSense

- 👍 Good, because very mature, large community.
- 👎 Bad, because product direction and licensing differences between CE and Plus; OPNsense
  has a more frequent release cadence and a cleaner API for automation.

### Proxmox firewall only

- 👍 Good, because nothing extra to run.
- 👎 Bad, because it filters guest traffic but is not a router/NAT/DNS/DHCP/VPN gateway for the office.

### MikroTik

- 👍 Good, because cheap, capable hardware.
- 👎 Bad, because different skill set, less friendly for learners, weaker WireGuard/DNS UX in comparison.

## More Information

- Related: [LLD network](../../03-design/lld-network.md), [ADR-0004](0004-remote-access-tailscale-and-wireguard.md)
- Revisit if: budget allows a dedicated appliance or an HA pair (CARP), or availability targets increase.
