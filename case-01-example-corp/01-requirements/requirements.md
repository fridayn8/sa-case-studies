# Requirements — Example Corp Secure Office Platform

| | |
|---|---|
| **Document** | Requirements specification |
| **Version** | 0.1 (draft) |
| **Status** | Proposed |
| **Owner** | Solution Architect (fridayn8) |
| **Related** | [HLD](../03-design/hld.md) · [LLD network](../03-design/lld-network.md) · [LLD compute](../03-design/lld-compute.md) · [LLD access](../03-design/lld-access.md) |

> Fictional scenario. All names, domains and addresses are placeholders.

## 1. Business context

Example Corp is a 25-person professional services company with one office. Staff work hybrid
(about 2 days/week from home). IT today is a single Proxmox server built ad hoc: no VLANs,
no documented design, remote access through a port-forwarded web UI, and backups on a USB
disk in the same room.

**Problems reported by stakeholders**

| # | Problem | Raised by |
|---|---------|-----------|
| P1 | Staff cannot reach internal apps (files, wiki, HR) from home without risky workarounds | Staff, management |
| P2 | Admin interfaces are exposed to the internet through port-forwarding | IT / security |
| P3 | Everything is on one flat network — a compromised laptop or printer can reach the servers | IT / security |
| P4 | Nobody knows exactly how the server is configured; changes are undocumented | IT |
| P5 | A disk failure or ransomware would cause days of downtime and data loss | Management |

## 2. Business goals

| ID | Goal | Measure (KPI) |
|----|------|---------------|
| BG-1 | Secure access to internal apps from anywhere | 100 % of staff access via SSO + MFA; 0 inbound ports for apps |
| BG-2 | Reduce security exposure | No admin interface reachable from the internet; network segmented |
| BG-3 | Recover quickly from failures | RTO/RPO targets (§5) met in a yearly DR test |
| BG-4 | Make IT changes traceable and repeatable | ≥ 90 % of infrastructure changes made through Git PRs |
| BG-5 | Keep costs predictable and low | Recurring SaaS cost within budget (§7) |

## 3. Stakeholders and RACI

| Stakeholder | Interest |
|-------------|----------|
| Managing director | Cost, business continuity |
| Staff (25) | Easy access, reliability |
| IT administrator (1, part-time) | Manageable operations, clear documentation |
| External IT partner | Support for incidents and major changes |
| Data protection officer (part-time role) | Personal data in HR app is protected |

| Activity | Architect | IT admin | IT partner | Director |
|----------|:---------:|:--------:|:----------:|:--------:|
| Design and ADRs | **A/R** | C | C | I |
| Build (IaC, configuration) | A | **R** | C | I |
| Approve production changes | C | R | C | **A** |
| Incident response | C | **R** | R | I (A for disaster declaration) |

*R = Responsible, A = Accountable, C = Consulted, I = Informed.*

## 4. Functional requirements

| ID | Requirement | Priority |
|----|-------------|----------|
| FR-01 | Staff can access the file service, wiki and HR app from the office and from home using company SSO with MFA | Must |
| FR-02 | Access to each app is granted by group membership in the identity provider | Must |
| FR-03 | Administrators can manage Proxmox, OPNsense and servers remotely | Must |
| FR-04 | An emergency (break-glass) admin path exists that does not depend on the identity provider or Tailscale | Must |
| FR-05 | Guests get internet-only Wi-Fi, isolated from company networks | Must |
| FR-06 | Printers and IoT devices are isolated; staff can print | Must |
| FR-07 | Internal DNS names resolve for all internal services (`*.int.example.com`) | Must |
| FR-08 | All VMs/containers are backed up automatically, with an off-site copy | Must |
| FR-09 | Service health is monitored and the admin is alerted on failures | Must |
| FR-10 | Infrastructure (VMs, DNS, access policies, firewall rules) is defined as code in Git | Should |
| FR-11 | A status page informs staff during outages, hosted **outside** the office | Should |
| FR-12 | New VMs are created from a hardened template | Should |
| FR-13 | Infrastructure changes are validated automatically in CI before merge | Could |

## 5. Non-functional requirements

### 5.1 Availability and recovery

| ID | Requirement |
|----|-------------|
| NFR-A1 | Business-hours availability (Mon–Fri 08:00–18:00) of staff apps ≥ 99.5 % per month |
| NFR-A2 | Single-service failure (VM crash, bad change): restore within **1 h** |
| NFR-A3 | Host hardware failure: restore critical services within **8 business hours** (requires next-business-day hardware support or spare parts) |
| NFR-A4 | Planned maintenance outside business hours, announced 2 working days ahead |

Recovery targets per service (from the business impact analysis):

| Service | Criticality | RTO | RPO | Notes |
|---------|-------------|-----|-----|-------|
| OPNsense (internet, DNS, DHCP) | Critical | 2 h | 24 h (config backed up on every change) | Office is offline without it |
| File service | High | 8 h | 24 h | Largest data set |
| HR app | High | 8 h | 24 h | Personal data |
| Wiki | Medium | 24 h | 24 h | |
| Monitoring | Medium | 24 h | 7 days | Metrics history is nice-to-have |
| CI runner, Tailscale router, cloudflared | Low (stateless) | 4 h | n/a | Rebuilt from code |

### 5.2 Security

| ID | Requirement |
|----|-------------|
| NFR-S1 | No inbound ports open on the WAN except the WireGuard break-glass port (UDP) |
| NFR-S2 | All remote access requires SSO + MFA, except break-glass (key-based, audited) |
| NFR-S3 | Admin interfaces (Proxmox, OPNsense, PBS, switch) reachable only from the management VLAN |
| NFR-S4 | Network segmented into zones; inter-zone traffic denied by default (allow-list) |
| NFR-S5 | No secrets in plain text in Git; secrets encrypted with SOPS or held in CI secret stores |
| NFR-S6 | API tokens follow least privilege and are rotated at least yearly and on staff change |
| NFR-S7 | Security patches applied monthly; critical vulnerabilities within 72 h |
| NFR-S8 | Logs of firewall, access and admin actions retained for ≥ 90 days |
| NFR-S9 | Backups encrypted, with at least one copy not deletable from the production host |

### 5.3 Performance and capacity

| ID | Requirement |
|----|-------------|
| NFR-P1 | Support 25 concurrent users (design headroom for 40) |
| NFR-P2 | File service: 2 TB initial data, 30 % yearly growth, 3-year horizon |
| NFR-P3 | Remote file access performance limited only by the office uplink (300/100 Mbit/s) |
| NFR-P4 | Host resources ≤ 70 % average utilisation at year 3 (30 % headroom) |

### 5.4 Operability and maintainability

| ID | Requirement |
|----|-------------|
| NFR-O1 | Every infrastructure component documented (HLD/LLD, runbooks) |
| NFR-O2 | Stateless components rebuildable from Git in < 1 h |
| NFR-O3 | Operable by one part-time administrator; no 24/7 on-call |
| NFR-O4 | Alerts are actionable and linked to a runbook |

### 5.5 Cost

| ID | Requirement |
|----|-------------|
| NFR-C1 | Reuse the existing server where possible |
| NFR-C2 | Recurring software/SaaS cost **USD 0**: only free software and free service tiers ([ADR-0010](../02-options-decisions/adr/0010-free-only-tooling-policy.md)); a domain name is the only accepted exception |
| NFR-C3 | Prefer open-source software and free tiers when they meet requirements |

## 6. Constraints

| ID | Constraint |
|----|------------|
| C-1 | One existing server (see [capacity planning](../04-security-cost/capacity-planning.md)); budget for one small backup appliance only |
| C-2 | One ISP link; no budget for a second link in year 1 |
| C-3 | One part-time IT administrator |
| C-4 | Company identity provider is a cloud suite (Google Workspace or Microsoft Entra ID) |
| C-5 | Public DNS for `example.com` is hosted on Cloudflare |

## 7. Assumptions

| ID | Assumption | Impact if false | Validation |
|----|------------|-----------------|------------|
| A-1 | The ISP provides a public IPv4 address (not CGNAT) | WireGuard break-glass needs a relay (e.g. small VPS) | Check with ISP |
| A-2 | The server supports VLAN-aware bridging and has ≥ 2 NIC ports | Need an extra NIC | Inventory |
| A-3 | A VLAN-capable managed switch and Wi-Fi access points supporting multiple SSIDs/VLANs are available | Purchase required | Inventory |
| A-4 | Next-business-day hardware support exists for the server | NFR-A3 cannot be met → keep spare disks/PSU | Check warranty |
| A-5 | Cloudflare and Tailscale free/low-cost plans cover the user count | Higher OPEX | Verify current pricing |
| A-6 | Apps work behind a reverse proxy with SSO headers / no special client protocols | Some apps may need Tailscale instead of Cloudflare Access | PoC |

## 8. Out of scope

- Email and office productivity (cloud suite)
- Endpoint management (MDM) and antivirus for laptops
- Telephony
- Second site / full high availability (evaluated as a future option in ADR backlog)

## 9. Traceability

| Requirement | Addressed in |
|-------------|--------------|
| FR-01, FR-02, NFR-S1, NFR-S2 | [HLD §5.1](../03-design/hld.md#51-staff-access-to-apps), [LLD access](../03-design/lld-access.md), [ADR-0005](../02-options-decisions/adr/0005-public-ingress-cloudflare-tunnel.md) |
| FR-03, FR-04, NFR-S3 | [HLD §5.2](../03-design/hld.md#52-admin-access), [LLD access](../03-design/lld-access.md), [ADR-0004](../02-options-decisions/adr/0004-remote-access-tailscale-and-wireguard.md) |
| FR-05, FR-06, FR-07, NFR-S4 | [LLD network](../03-design/lld-network.md), [ADR-0003](../02-options-decisions/adr/0003-firewall-opnsense.md) |
| FR-08, NFR-A2, NFR-A3, NFR-S9 | [HLD §7](../03-design/hld.md#7-operations-monitoring-backup-and-recovery), [LLD compute](../03-design/lld-compute.md) |
| FR-10, FR-12, FR-13, NFR-O2 | [ADR-0012](../02-options-decisions/adr/0012-opentofu-and-cloud-image-templates.md), [`sa-projects` roadmap](https://github.com/fridayn8/sa-projects/blob/main/ROADMAP.md), phases 3–7 |
| NFR-S5, NFR-S6 | [ADR-0007](../02-options-decisions/adr/0007-secrets-sops-age.md) |
| NFR-P1…P4, NFR-C1…C3 | [Capacity planning](../04-security-cost/capacity-planning.md), [Cost estimate](../04-security-cost/cost-estimate.md) |
| All security NFRs | [Threat model](../04-security-cost/threat-model.md), [Hardening baseline](https://github.com/fridayn8/sa-projects/blob/main/projects/example-corp/docs/hardening-baseline.md) |
