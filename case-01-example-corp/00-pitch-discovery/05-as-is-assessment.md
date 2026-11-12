# Case 01 — As-Is Assessment

| | |
|---|---|
| **Document** | Current-state assessment, findings and assumptions log |
| **Stage** | [1 Discovery](../../engagement-playbook/01-discovery.md) |
| **Status** | **Confirmed by the client** (managing director and IT administrator, end of week 3) |
| **Feeds** | [Requirements](../01-requirements/requirements.md): problems P1–P5, assumptions A-1…A-6 |

> Fictional scenario. All names, domains and addresses are placeholders. The as-is is a
> **photograph of what exists**, not a plan.

## 1. Summary

Example Corp runs everything on **one Proxmox host** built by the part-time IT administrator.
There is one flat network, an ISP router that forwards two ports to internal servers, backups
to a single USB disk beside the server, and no documentation other than the administrator's memory.
The system works day to day; its risk is that **nobody can prove that it is safe, and nobody could
rebuild it quickly**.

## 2. What exists

### 2.1 Hardware

| Item | Today | Notes |
|------|-------|-------|
| Server `pve01` (existing) | 1× 16-core / 32-thread CPU, 128 GB ECC RAM, 2× 240 GB SSD (boot), 3× 4 TB HDD (data), 2× 2.5 GbE, BMC port | The CPU, RAM, boot SSDs and BMC are kept; data disks reach the end of their planned life |
| Switch | One 24-port **unmanaged** switch | No VLAN capability |
| Wi-Fi | The ISP router's built-in Wi-Fi, one network for staff and visitors | No separation |
| Router | ISP-provided router: NAT, DHCP, port-forwards | Admin password has not been changed since installation |
| Backup | One 4 TB external USB disk, attached to the server | In the same room |
| Power | No UPS | One power cut in the last year caused a dirty shutdown |
| Printers | Two network printers, one label printer | On the same flat network |

### 2.2 Network

- One flat network `10.0.0.0/24` for everything: servers, laptops, printers, visitors.
- ISP internet link, 300 Mbit/s down and 100 Mbit/s up, one link, no backup.
- Port-forwards on the ISP router: **TCP 8006** (Proxmox web UI) and **TCP 443** (file service).
- The router's WAN address is in the public range (not in a private or carrier-grade NAT range);
  to be confirmed by the ISP.

### 2.3 Software and data

| System | What | Users | Data | Owner |
|--------|------|------:|------|-------|
| Proxmox VE | Hypervisor | 1 admin | VM images | IT administrator |
| `files` VM | File service (web UI and network share) | 25 | **2 TB** | IT administrator |
| `wiki` VM | Documentation wiki | 25 | about 5 GB | IT administrator |
| `hr` VM | HR application with personnel data | 3 | about 20 GB | HR manager (data), IT administrator (system) |
| `test2` VM | Unknown purpose | 0? | Unknown | **Nobody** |

Dependencies found in interviews: a **monthly payroll export script** on the HR VM sends a file to the
accountant by email; a label printer on the file server's share is used by the warehouse
staff; the wiki's internal links point to a hostname that exists only in the router's DNS table.

### 2.4 Backups

| Item | Finding |
|------|---------|
| What is backed up | All VMs except `test2`, nightly, to the USB disk |
| Where the copy lives | Attached to the server, in the same room |
| Encryption | None |
| Last restore test | **Never** (from the log and the administrator's account) |
| Last successful backup | Last night; the last failed backup was 11 days ago (disk full) and was not noticed for 3 days |

### 2.5 Access, identity and operations

- Staff log in to the file service with local accounts; the identity provider (a cloud suite) is not
  integrated with any internal app.
- Remote work happens by emailing files or by using the port-forwarded file service over HTTPS.
- The Proxmox web UI is reachable from the internet through port 8006, protected by a single
  administrator account with a password; no second factor.
- Updates are applied by hand when the administrator has time; the last Proxmox update was seven
  months ago.
- There is no monitoring and no alerting; problems are discovered by users.
- Documentation does not exist beyond a short list of VM names and their IP addresses.

### 2.6 Contracts and constraints

| Item | Finding |
|------|---------|
| ISP | One business line, 300/100 Mbit/s, contract renews in 14 months |
| Hardware support | The server's vendor warranty **ended** 14 months ago; a renewal quote is about USD 1 400 per year, which conflicts with the recurring-cost constraint |
| IT partner | Hourly support contract, response next business day |
| Skills | One part-time administrator, about two days a week; the IT partner for incidents |
| Identity provider | Cloud office suite already in use for email and calendars |
| DNS | The public zone for `example.com` is hosted at Cloudflare |

## 3. Findings

| # | Finding | Severity | Related problem | Evidence |
|---|---------|:--------:|-----------------|----------|
| F-1 | The Proxmox admin interface is reachable from the internet, protected by a password only | **High** | P2 | Router port-forward table; admin interview |
| F-2 | One flat network: any compromised laptop or printer reaches all servers | **High** | P3 | Router configuration; network walk |
| F-3 | Backups are on one unencrypted USB disk attached to the server; no restore test | **High** | P5 | Backup log; interviews |
| F-4 | Nobody documents or fully understands the server; one unknown VM | Medium | P4 | Inventory; VM list |
| F-5 | The HR application is reachable from every device on the network; access is not logged | **High** | P3 | HR manager interview; configuration |
| F-6 | No monitoring: a failed backup went unnoticed for three days | Medium | P5 | Backup log |
| F-7 | Staff cannot reach internal apps from home without workarounds | Medium | P1 | Staff interview |
| F-8 | No UPS; no hardware support contract; single power and internet path | Medium | P5 | Walk-through; warranty |
| F-9 | Router and switch are consumer-grade with no VLAN capability | Medium | P3 | Inventory |
| F-10 | Updates are applied irregularly; last Proxmox update seven months ago | Medium | P2 | Update log |

Findings **F-1, F-2, F-3 and F-5** are the ones the insurance questionnaire asks about.

## 4. Assumptions log

The assumptions below were carried into the [requirements](../01-requirements/requirements.md#7-assumptions)
(A-1…A-6) with their status at the end of discovery.

| ID | Assumption | Status at end of discovery | How to validate | Owner |
|----|------------|----------------------------|-----------------|-------|
| A-1 | The ISP provides a public IPv4 address (not CGNAT) | **Likely true**: the router's WAN address is public; ISP confirmation pending | Written confirmation from the ISP | IT administrator |
| A-2 | The server supports VLAN-aware bridging and has at least two NIC ports | **True** for the ports (2× 2.5 GbE); VLAN-aware bridge to be proven in the lab | Create a VLAN-aware bridge in the nested lab | Architect |
| A-3 | A managed VLAN-capable switch and multi-SSID access points are available | **False**: unmanaged switch and consumer Wi-Fi; purchase required (in the CAPEX) | Inventory (done) | Architect |
| A-4 | Next-business-day hardware support exists for the server | **False**: warranty ended; the requirement is met with spare parts instead (see cost estimate) | Warranty check (done) | Architect |
| A-5 | Cloudflare and Tailscale free plans cover 25 users | **Likely true** (limits are above 25 users); verify pricing and terms before signing | Check the current plan limits | Architect |
| A-6 | The three apps work behind a reverse proxy with SSO and no special client protocols | **Unknown**; riskiest assumption | One-day PoC (stage 3) | Architect |

## 5. Confirmation

The assessment was read in the final workshop; the IT administrator corrected two items (the
last Proxmox update date and the fact that `test2` is used by nobody, not unknown to everybody). The
managing director **confirmed the as-is in writing** by email the same day. Condition: the IT
administrator becomes the named **owner of the current system** until handover.

## 6. What this shows

- The most valuable facts were not in the first call: the unexplained VM, the payroll script and
  the failed backup came from observation and one-to-one interviews.
- Two assumptions (A-3, A-4) turned out to be **false**, and it cost nothing to learn that now. They
  explain two lines in the cost estimate: purchased switch and access points, and spare parts in place
  of a support contract.
- The findings map to the five reported problems; each requirement in the next stage can be traced
  back to a finding.
