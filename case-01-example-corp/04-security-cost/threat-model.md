# Threat Model — Example Corp Secure Office Platform

| | |
|---|---|
| **Method** | STRIDE per trust boundary |
| **Version** | 0.1 |
| **Scope** | Platform in the [HLD](../03-design/hld.md); laptops and SaaS internals out of scope |
| **Review** | On every architecture change (PR checklist) and at least yearly |

## 1. How to read this

1. Identify **assets** (what we protect) and **trust boundaries** (where trust changes).
2. For each boundary, walk through **STRIDE** (table below).
3. Rate risk = **Likelihood × Impact** (Low / Medium / High) *after* mitigations (residual).
4. Track open actions as GitHub issues labelled `security`.

| Letter | Threat | Violates | Typical mitigation |
|--------|--------|----------|--------------------|
| **S** | Spoofing — pretending to be someone/something else | Authentication | SSO, MFA, keys, certificates |
| **T** | Tampering — modifying data or code | Integrity | Signatures, reviews, access control |
| **R** | Repudiation — denying an action, no evidence | Non-repudiation | Audit logs, signed commits |
| **I** | Information disclosure — data leak | Confidentiality | Encryption, least privilege, segmentation |
| **D** | Denial of service — making it unavailable | Availability | Rate limiting, redundancy, backups |
| **E** | Elevation of privilege — gaining more rights | Authorization | Least privilege, patching, isolation |

## 2. Assets

| ID | Asset | Classification | Why it matters |
|----|-------|----------------|----------------|
| AS-1 | HR data (`hr01`) | **Confidential — personal data** | Legal obligations, privacy |
| AS-2 | Company files (`files01`) | Confidential | Business documents |
| AS-3 | Backups (`pbs01`, off-site) | Confidential | Contain all of the above; last line of defence |
| AS-4 | Admin credentials & API tokens | Secret | Full control of platform |
| AS-5 | Infrastructure code & CI (GitHub, `runner01`) | Internal / high integrity | Code = infrastructure; tampering = compromise |
| AS-6 | Network availability (OPNsense, Proxmox) | Business critical | Office cannot work without it |
| AS-7 | SaaS control planes (IdP, Cloudflare, Tailscale accounts) | Secret / high integrity | Control access to everything |

## 3. Trust boundaries

See the [network topology](../03-design/diagrams/network-topology.md#2-logical-zones-and-trust-boundaries) diagram.

| ID | Boundary | Crossing |
|----|----------|----------|
| TB-1 | Internet → Cloudflare edge → Tunnel → DMZ | Staff and attackers reaching published apps |
| TB-2 | DMZ → SERVERS | `cloudflared` → apps |
| TB-3 | Tailnet → MGMT / SERVERS | Admins via `ts01` |
| TB-4 | Internet → OPNsense WAN | Any packet from the internet; WireGuard listener |
| TB-5 | STAFF / GUEST / IOT → internal zones | Local devices |
| TB-6 | GitHub → `runner01` → Proxmox / Cloudflare APIs | Pipelines changing infrastructure |
| TB-7 | Admins → SaaS control planes | IdP, Cloudflare, Tailscale, GitHub accounts |
| TB-8 | `pve01` → `pbs01` → off-site | Backup data flows |

## 4. Threat analysis

### TB-1 — Internet → Cloudflare → Tunnel → DMZ

| # | STRIDE | Threat | Mitigations | Residual |
|---|:------:|--------|-------------|:--------:|
| 1.1 | S | Attacker uses stolen staff password | Access requires IdP SSO + MFA; phishing-resistant MFA for HR group; short sessions for HR | Low |
| 1.2 | S | Attacker bypasses Access by reaching origin directly | Origin has no public IP or open port; tunnel only; apps can validate the Access JWT header | Low |
| 1.3 | I | Data visible at Cloudflare (TLS terminated at edge) | Accepted for classification (ADR-0005); re-encrypted to origin; DPA with vendor | Medium (accepted) |
| 1.4 | D | DDoS on public hostnames | Cloudflare DDoS protection, rate limiting rules | Low |
| 1.5 | E | Web app vulnerability (e.g. RCE) exploited by an authenticated user | WAF managed rules; patching (NFR-S7); app runs in SERVERS with no access to MGMT | Medium |
| 1.6 | T | Tunnel token stolen → attacker runs a rogue connector | Token in SOPS / Ansible only; rotate token on suspicion; Cloudflare shows connector list — alert on unknown connector | Low |

### TB-2 — DMZ → SERVERS

| # | STRIDE | Threat | Mitigations | Residual |
|---|:------:|--------|-------------|:--------:|
| 2.1 | E | Compromised `cfd0x` pivots into the internal network | Firewall R4: only TCP 443 to three app IPs; no SSH from DMZ; unprivileged LXC | Low |
| 2.2 | I | Traffic sniffing inside the DMZ | HTTPS to origin with certificate verification | Low |

### TB-3 — Tailnet → MGMT / SERVERS

| # | STRIDE | Threat | Mitigations | Residual |
|---|:------:|--------|-------------|:--------:|
| 3.1 | S | Stolen admin laptop joins tailnet | Device approval, key expiry, disk encryption, remote device removal; MFA on re-auth | Low |
| 3.2 | E | Over-broad ACL gives admins/CI more access than needed | ACL in Git with PR review and ACL `tests`; separate rule for `tag:ci` | Low |
| 3.3 | R | Admin action without trace | Tailscale network flow logs (plan-dependent), Proxmox/OPNsense audit logs to syslog; named accounts only | Medium |

### TB-4 — Internet → OPNsense WAN

| # | STRIDE | Threat | Mitigations | Residual |
|---|:------:|--------|-------------|:--------:|
| 4.1 | S | Brute force / scanning of exposed services | Only UDP 51820 open; WireGuard does not respond to unauthenticated packets | Low |
| 4.2 | S | Stolen break-glass key used | Keys only on 2 encrypted devices; alert on every handshake; access limited to MGMT; key rotation | Low |
| 4.3 | D | Volumetric attack on office IP | Out of our control; IP not published in DNS for apps; ISP support | Medium (accepted) |
| 4.4 | E | Firewall/hypervisor vulnerability | Monthly patching; WAN bridge has no host IP; minimal plugins | Low |

### TB-5 — Local zones → internal

| # | STRIDE | Threat | Mitigations | Residual |
|---|:------:|--------|-------------|:--------:|
| 5.1 | E | Infected staff laptop scans/attacks servers | STAFF → SERVERS only 443 to apps; no access to MGMT | Medium |
| 5.2 | E | Compromised IoT device / printer as pivot | IOT isolated, internet only to vendor endpoints | Low |
| 5.3 | I | Guest sniffs company traffic | Separate SSID/VLAN, client isolation, internet only | Low |
| 5.4 | S | Rogue device plugged into a desk port | Desk ports only in STAFF VLAN; unused ports disabled; (802.1X as future improvement) | Medium |

### TB-6 — GitHub → runner → APIs (supply chain)

| # | STRIDE | Threat | Mitigations | Residual |
|---|:------:|--------|-------------|:--------:|
| 6.1 | T | Malicious change merged into infra code | PR review, CODEOWNERS, CI checks, signed commits; rulesets enforced only if repo is public or on a paid plan (ADR-0010) | Medium |
| 6.2 | E | Untrusted code runs on self-hosted runner (e.g. from a fork PR) | **Private repo only**; runner not used for fork PRs; jobs on runner only after merge / with environment approval | Low |
| 6.3 | T | Compromised third-party GitHub Action | Pin actions to full commit SHA; Dependabot for actions; minimal `permissions:` | Medium |
| 6.4 | I | Secrets leaked in CI logs | GitHub masks secrets; no `set -x` with secrets; scoped tokens | Low |
| 6.5 | E | Runner token/credentials abused | Runner LXC in MGMT with only needed API tokens; ephemeral runner (future) | Medium |

### TB-7 — SaaS control planes

| # | STRIDE | Threat | Mitigations | Residual |
|---|:------:|--------|-------------|:--------:|
| 7.1 | S | Takeover of an admin's IdP/Cloudflare/Tailscale/GitHub account | Phishing-resistant MFA; few admins; separate admin accounts where supported; login alerts | Medium |
| 7.2 | D | SaaS outage locks admins out | Break-glass WireGuard + on-site MGMT port; local accounts | Low |
| 7.3 | R | Changes made in SaaS consoles bypassing Git (ClickOps) | Scheduled `tofu plan` drift detection; audit logs reviewed monthly | Medium |

### TB-8 — Backups

| # | STRIDE | Threat | Mitigations | Residual |
|---|:------:|--------|-------------|:--------:|
| 8.1 | T/D | Ransomware on `pve01` deletes or encrypts backups | `pve01` has backup-only PBS permissions; pruning on PBS; off-site copy pulled by remote side | Low |
| 8.2 | I | Stolen backup disk | PBS client-side encryption; key in SOPS + sealed offline copy | Low |
| 8.3 | D | Backups silently failing / unrestorable | Verify jobs, monitoring of backup status, monthly restore tests | Low |

## 5. Top risks and actions

| Priority | Risk | Action | When |
|:--------:|------|--------|------|
| 1 | 6.3 / 6.5 — CI supply chain and runner privileges | Pin actions by SHA, least-privilege tokens, manual dispatch for production applies (no environment approvals on GitHub Free private repos) | Build (CI/CD) |
| 2 | 7.1 — Admin SaaS account takeover | Enforce security keys/passkeys for all admin accounts | Design and build |
| 3 | 1.5 / 5.1 — App or laptop compromise | Patch cadence, WAF rules, monitoring alerts | Build to operate |
| 4 | 7.3 — Drift through console changes | Nightly drift detection workflow | Build (CI/CD) |
| 5 | 5.4 — Rogue device on wired port | Evaluate 802.1X / port security | Future |

## 6. Assumptions and out of scope

- Laptops are managed and encrypted by the company (endpoint security out of scope).
- SaaS providers' internal security is trusted per their certifications and contracts.
- Physical security of the office/server room is adequate (locked room).
