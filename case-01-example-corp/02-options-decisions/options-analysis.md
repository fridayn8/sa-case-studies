# Case 01 — Options Analysis

| | |
|---|---|
| **Document** | Long list, short list, weighted criteria, decision matrix and PoC |
| **Stage** | [3 Options and decisions](../../engagement-playbook/03-options-and-decisions.md) |
| **Status** | Direction agreed with the sponsor; decisions recorded in the ADRs |
| **Inputs** | [Requirements](../01-requirements/requirements.md) · [As-is assessment](../00-pitch-discovery/05-as-is-assessment.md) |
| **Outputs** | [ADR log](adr/README.md) (this document references ADR-0002…0005 and 0012 instead of repeating them) |
| **Template** | [Options decision matrix](../../engagement-playbook/templates/options-decision-matrix.md) |

> Fictional scenario. Scores and costs are illustrative.

## 1. Decisions in scope and method

Two levels of decision were made:

1. **Overall solution approach**: what kind of solution meets the signed requirements (section 2
   and 3). This document owns this decision.
2. **Component decisions** inside the chosen approach (hypervisor, firewall, remote access, ingress,
   automation). Each has its own ADR; section 5 maps them.

**Method.** (1) Build a long list. (2) Apply knock-out criteria from the requirements. (3) Agree
the criteria and weights with the sponsor **before scoring**. (4) Score the short list with
a one-sentence reason per cell. (5) Test sensitivity. (6) Test the riskiest assumption.
(7) Record the decision.

## 2. Long list and short list

| # | Option | Description | Short-listed? | Reason |
|---|--------|-------------|---------------|--------|
| E | Do nothing | Keep the current setup, patch more often | **No (baseline only)** | Fails NFR-S1, NFR-S3 and NFR-A3: leaves the exposed admin interface and the single USB backup |
| A | **On-site single host, free software and free SaaS edge** | Proxmox + OPNsense VMs, segmented network, Cloudflare Tunnel and Access for staff, Tailscale and WireGuard for administrators, Proxmox Backup Server on a separate appliance | **Yes** | Meets all Musts; the design in this repository |
| B | A plus a second Proxmox node and HA | As A with two nodes, replicated storage and a quorum device | **Yes** | Meets all Musts; higher availability |
| C | SaaS-first | Move files, wiki and HR to subscription SaaS; thin firewall and a managed-device policy | **No (knocked out)** | Violates NFR-C2 (recurring software cost USD 0) and ADR-0010; reopens only if the sponsor relaxes that requirement |
| D | Dedicated firewall appliance and classic VPN | The reseller's idea: an appliance with built-in VPN for everyone, nothing else changes | **Yes** | Meets some Musts; included because the sponsor proposed it |
| F | Cloud-hosted servers | Lift the VMs to a cloud provider; keep a firewall in the office | **No (knocked out)** | Same recurring-cost knock-out as C, plus HR data residency (decision for HR) |
| G | Managed service provider | Outsource the whole platform to the IT partner or a managed provider | **No (knocked out)** | Violates NFR-C2; no budget for a recurring contract |

**Knock-out criteria used:** NFR-C2 (USD 0 recurring software and SaaS cost) and the Must requirements
FR-01…FR-08 and NFR-S1…S4. Options C, F and G are excluded by NFR-C2, **not** because they are bad;
the exclusion is recorded so the sponsor can reopen it.

## 3. Weighted criteria and decision matrix

### 3.1 Criteria and weights (agreed with the managing director before scoring)

| Code | Criterion | Weight | Why this weight |
|------|-----------|-------:|-----------------|
| S | **Security**: exposure reduction, segmentation, MFA | 25 | Insurance deadline, problems P2, P3 |
| R | **Recoverability**: RTO and RPO met | 15 | Problem P5, NFR-A2, NFR-A3 |
| C | **Five-year cost** including people time | 20 | The MD's first priority, tempered by the ranking agreed in discovery |
| O | **Operability** by one part-time administrator | 20 | NFR-O3, the administrator's main fear |
| P | **Data control and privacy** | 10 | HR manager's requirement |
| X | **Exit and reversibility** | 10 | Fear of dependence on one person or vendor |
| | **Total** | **100** | |

### 3.2 Scores (0 to 3)

Anchors: **3** meets fully · **2** meets with caveats · **1** weak · **0** fails. For **cost** the anchors are
relative: 3 = lowest five-year cost on the short list, 2 = within 25 % of the lowest, 1 = more than 25 % above.

| Criterion | Weight | A | B | D |
|-----------|-------:|:-:|:-:|:-:|
| S Security | 25 | 3 | 3 | 2 |
| R Recoverability | 15 | 2 | 3 | 1 |
| C Five-year cost incl. people | 20 | 2 | 1 | 3 |
| O Operability | 20 | 2 | 1 | 2 |
| P Data control, privacy | 10 | 3 | 3 | 3 |
| X Exit, reversibility | 10 | 3 | 2 | 2 |
| **Weighted total (max 300)** | | **245** | **210** | **215** |
| **Percent** | | **82 %** | **70 %** | **72 %** |

### 3.3 Why these scores

| Criterion | A | B | D |
|-----------|---|---|---|
| **S** | Admin interfaces off the internet, six zones, SSO and MFA at the edge | Same as A | Appliance and VPN help with admin access, but staff still get network-level VPN access and no per-app control; the flat network remains until someone designs VLANs |
| **R** | Restore within 8 h from a separate backup appliance, monthly restore tests; a host failure still means downtime | Host failure survived; backups still required | Backups and restore are not addressed by the appliance |
| **C** | About USD 22 k over five years (cost estimate), about 10 % above D | About USD 28–31 k over five years, more than 25 % above D | Lowest five-year cost as offered (about USD 20 k), but backups and documentation are not included; adding them would bring it to about USD 24–26 k |
| **O** | Fits one part-time admin if automated and documented; two access mechanisms to maintain | Cluster, quorum and replicated storage add skills the company does not have | One product to learn, but VPN accounts for 25 users are manual work |
| **P** | Data stays on-site; only the web edge is external | Same as A | Same as A |
| **X** | Open source, everything in Git, replaceable components | A plus a more complex migration path | Appliance licences and a proprietary configuration |

### 3.4 Sensitivity

The margin between A (245) and D (215) is **30 points of 300**, about one tenth. Do the weights
decide the outcome? Variations of the weights (each adds up to 100):

| Variation | A | B | D | Leader |
|-----------|--:|--:|--:|--------|
| Base weights | 245 | 210 | 215 | **A** |
| Cost +10, security −10 | 235 | 190 | 225 | **A** (narrow) |
| Cost +10, operability −10 | 245 | 210 | 225 | **A** |
| Recoverability +10, security −10 | 235 | 210 | 205 | **A** |
| Operability +10, cost −10 | 245 | 210 | 205 | **A** |
| Security +10, privacy −5, exit −5 | 245 | 215 | 210 | **A** |
| **Extreme:** cost 40, security 5 | 225 | 170 | 235 | **D** |

**Reading.** A stays ahead in every plausible variation. D only wins if cost outweighs security by
eight to one, which contradicts the ranking the MD gave in discovery (recovery and exposure above
price). The deciding qualitative difference is also clear: D leaves the backup, recovery and
documentation problems (P4, P5) unsolved, and those are the two that frighten the sponsor most.

B scores well on recoverability but is penalised for cost and operability. It is **not rejected
forever**: the trigger for reopening it is in HLD risk R-1 and the
[ADR log](adr/README.md#candidate-future-adrs) (budget increase or a tighter availability target).

### 3.5 Five-year cost comparison

| Option | Five-year cost (illustrative) | Source |
|--------|------------------------------:|--------|
| A | ≈ USD 22 k | [Cost estimate §4](../04-security-cost/cost-estimate.md#4-five-year-tco) |
| B | ≈ USD 28–31 k | [Cost estimate §6](../04-security-cost/cost-estimate.md#6-options-compared-high-level) |
| D | ≈ USD 19–21 k as offered (appliance about USD 4.8 k, people time unchanged, no backup appliance); about USD 24–26 k once backup and documentation are added | Estimate made in discovery; **not** in the cost estimate |
| C | Per-user subscriptions (excluded by the free-only policy) | Cost estimate §6 |

## 4. Proof of concept: the riskiest assumption

**Assumption A-6:** the three internal apps (files, wiki, HR) work behind a reverse proxy with SSO
at the edge. If false, ADR-0005 (staff access through a tunnel) does not hold for that app and the
whole staff-access path changes.

| | |
|---|---|
| **Question** | Can each app be used end to end through the tunnel and the identity check, including the heaviest realistic operation? |
| **Set-up** | Lab host (nested), the three real apps restored from backup, one tunnel connector, one test hostname per app, one test user with MFA, no production data |
| **Time-box** | One day of effort |
| **Pass criteria** | 1. Login with MFA works. 2. A 500 MB upload completes (file service). 3. A session stays open for 30 minutes of editing (wiki, HR). 4. The app's own login still works behind the proxy. 5. An external port scan of the office address shows no open TCP port |
| **Failure plan** | Per app: keep behind the tunnel with a limit, move to the admin-style network path, or change the option |

**Result (recorded):**

| Criterion | Files | Wiki | HR app |
|-----------|-------|------|--------|
| Login with MFA | ✅ | ✅ | ✅ |
| Large upload | ⚠️ Browser uploads above the edge request-size limit failed; the file app's **sync client uses chunked uploads and worked** | n/a | n/a |
| Long session | ✅ | ✅ | ✅ |
| App login behind proxy | ✅ | ✅ | ✅ (after setting the trusted proxy header) |
| Port scan | ✅ no open TCP ports | | |

**Outcome:** ADR-0005 stands. **A-6 is partly true:** large browser uploads through the edge need
a different path. Mitigations recorded: staff use the sync client for large files remotely, and the
internal name (`files.int.example.com`) is used for large transfers inside the office (HLD §5.1).
The limit is on the edge provider's free plan and **must be re-verified** before go-live (assumption
A-5).

## 5. Component decisions and their ADRs

| Decision | Options considered | Chosen | ADR |
|----------|--------------------|--------|-----|
| Hypervisor | Proxmox VE, VMware vSphere/ESXi, Hyper-V, XCP-ng | Proxmox VE | [ADR-0002](adr/0002-hypervisor-proxmox-ve.md) |
| Firewall and router | OPNsense VM, OPNsense appliance, pfSense, Proxmox firewall only, MikroTik | OPNsense as a VM | [ADR-0003](adr/0003-firewall-opnsense.md) |
| Remote access | Classic VPN, Tailscale + WireGuard + Cloudflare Access, Headscale, Cloudflare Zero Trust for all, NetBird/ZeroTier | Tailscale for admins, WireGuard break-glass, Cloudflare Access for staff | [ADR-0004](adr/0004-remote-access-tailscale-and-wireguard.md) |
| Public ingress | Port-forward + reverse proxy, Cloudflare Tunnel + Access, VPS reverse proxy, Tailscale for staff | Cloudflare Tunnel with Access | [ADR-0005](adr/0005-public-ingress-cloudflare-tunnel.md) |
| Automation | Terraform, OpenTofu, Pulumi; Packer, cloud image, `virt-customize` | OpenTofu with Debian cloud-image templates and Ansible | [ADR-0012](adr/0012-opentofu-and-cloud-image-templates.md) (supersedes ADR-0006) |
| Policy | Free-only, open-source-first | Both | [ADR-0010](adr/0010-free-only-tooling-policy.md) · [ADR-0011](adr/0011-open-source-first.md) |

## 6. Recorded decision

**Direction agreed with the sponsor:** Option A, with B as a documented future trigger and C, F, G
excluded by the free-only policy (reopenable). The sponsor accepted the following residual risks:
single host (R-1), network outage during hypervisor maintenance (R-2), and dependence on
Cloudflare and Tailscale (R-4). See the [risk register](../05-proposal-delivery/risk-register.md).

## 7. What this shows

- Weights were set **before** scoring. The sensitivity table then shows how far they would have to
  move to change the answer.
- Knock-out criteria shortened the list honestly: three attractive options are excluded by one
  requirement the sponsor can relax.
- The PoC tested the riskiest assumption with the hardest case, and the result changed a
  consequence in the ADR (uploads), not the decision.
