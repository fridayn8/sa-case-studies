# Case 01 — Risk Register

| | |
|---|---|
| **Document** | Risk register for the Example Corp engagement and the solution |
| **Stage** | Started in [discovery](../../engagement-playbook/01-discovery.md); maintained from [proposal](../../engagement-playbook/05-proposal-and-commercial.md) onwards |
| **Template** | [Risk register template](../../engagement-playbook/templates/risk-register-template.md) |
| **Consistent with** | [HLD §9](../03-design/hld.md#9-risks-and-open-issues) (R-1…R-7) · [Threat model](../04-security-cost/threat-model.md) |
| **Status** | Baseline at the stage 5 gate; reviewed at every gate |

> Fictional scenario. Likelihood and impact are judgements on a three-level scale (Low, Medium,
> High). Score = likelihood × impact with Low = 1, Medium = 2, High = 3.

## 1. Solution risks (from the HLD, unchanged)

| ID | Risk | Likelihood | Impact | Score | Owner | Mitigation | Status |
|----|------|:----------:|:------:|:-----:|-------|------------|--------|
| R-1 | Single host is a **single point of failure**: a host failure stops everything including the internet | Low | High | 3 | Sponsor (accepted), IT administrator | **Accepted** (cost). Spare parts, tested restore, external status page. Reopen with a second node (future ADR) if budget or availability target changes | Accepted |
| R-2 | OPNsense runs as a VM: Proxmox maintenance means a network outage | Medium | Medium | 4 | IT administrator | Maintenance windows, on-site management port, restore runbook; a physical firewall later if outages become a problem | Accepted |
| R-3 | Single ISP link | Medium | Medium | 4 | Sponsor | Accepted for year 1; an LTE backup router is a low-cost option | Accepted |
| R-4 | Dependence on Cloudflare, Tailscale and the identity provider | Low | Medium | 2 | Architect | Break-glass WireGuard; internal names work on-site | Mitigated by design |
| R-5 | CGNAT at the ISP would break the WireGuard break-glass path (assumption A-1) | Low | Medium | 2 | IT administrator | Confirm with the ISP in writing; fallback is a small relay server | **Open** until ISP confirms |
| R-6 | The self-hosted runner has admin rights in the lab | Medium | High | 6 | Architect | Private repository only, management-zone ACLs, protected branches, required reviews | Open |
| R-7 | A part-time administrator means slower incident response | Medium | Medium | 4 | IT administrator, IT partner | Runbooks, alerting, IT partner contract | Open |

## 2. Delivery and commercial risks (new at the proposal stage)

| ID | Risk | Likelihood | Impact | Score | Owner | Mitigation | Status |
|----|------|:----------:|:------:|:-----:|-------|------------|--------|
| R-8 | Hardware lead time is longer than 4 weeks and delays test and go-live | Medium | Medium | 4 | Architect, supplier | Order as soon as the contract is signed; ask for the delivery date in writing; keep a buffer before the insurance date | Open |
| R-9 | Client approval and contract take longer than 4 weeks | Medium | Medium | 4 | Sponsor | Walk the MD through the proposal first; agree a signature date; note that every extra week moves go-live | Open |
| R-10 | Scope creep during the build ("also add CCTV") | High | Medium | 6 | Architect, sponsor | Change control from day one; impact analysis for each request; see [CR-001](change-request-cctv.md) | **Materialised** (CR-001) |
| R-11 | The IT administrator is the only builder and is unavailable (illness, holiday, other work) | Medium | High | 6 | Sponsor, IT partner | Named backup from the IT partner; builder time agreed in the SOW | Open |
| R-12 | Large browser uploads fail through the edge limit (assumption A-6, found in the PoC) | High | Low | 3 | Architect | Sync client for large files; internal name in the office; re-verify the edge limit before go-live | Mitigated |
| R-13 | A backup restore has never been tested and fails when needed | Medium | High | 6 | IT administrator | Restore tests before go-live and monthly after; verify in the cutover Go/No-Go | Open |
| R-14 | Knowledge stays with the architect and the administrator | Medium | High | 6 | Architect | Handover test, runbooks written with operations, ADRs | Open |
| R-15 | The insurance renewal date (1 October 2027) is missed by a slipping schedule | Low | High | 3 | Sponsor, architect | Seven weeks of float in the plan; **minimum viable result** (admin exposure closed, MFA at the edge) defined in the SOW | Open |
| R-16 | Free-tier terms or limits change (Cloudflare, Tailscale; assumption A-5) | Low | Medium | 2 | Architect | Verify current terms before signing and before go-live; Headscale as a documented fallback | Open |
| R-17 | The recurring-cost constraint (USD 0) forces a worse option than a paid one | Medium | Medium | 4 | Sponsor | Revisit the constraint with numbers at the review; options C, F and G are documented | Open |

## 3. Risk heat map

| | **Impact Low** | **Impact Medium** | **Impact High** |
|---|:---:|:---:|:---:|
| **Likelihood High** | R-12 | R-10 | |
| **Likelihood Medium** | | R-2, R-3, R-7, R-8, R-9, R-17 | R-6, R-11, R-13, R-14 |
| **Likelihood Low** | | R-4, R-5, R-16 | R-1, R-15 |

**Top risks for the next gate** (score 6): R-6, R-10, R-11, R-13, R-14.

## 4. Assumptions linked to risks

| Assumption | Risk | Validation |
|------------|------|------------|
| A-1 public IPv4 at the ISP | R-5 | ISP confirmation |
| A-4 hardware support | R-1 | Spare parts instead (see cost estimate) |
| A-5 free-plan limits cover 25 users | R-16 | Check terms again before signing |
| A-6 apps work behind the proxy | R-12 | PoC (done; partly true) |

## 5. Review log

| Gate | Changes |
|------|---------|
| Stage 1 (discovery) | R-1…R-7 started from the as-is findings |
| Stage 3 (options) | R-12 added from the PoC; R-17 added after the knock-out of paid options |
| Stage 5 (proposal) | R-8…R-11, R-13…R-15 added; owners agreed with the MD |
| Stage 6 (build) | R-10 materialised (CCTV request) |
| Stage 8 (handover) | Residual risks transferred to the IT administrator |
