# Case 01 — Solution Proposal

| | |
|---|---|
| **Document** | Solution proposal sent to the managing director |
| **Stage** | [5 Proposal and commercial](../../engagement-playbook/05-proposal-and-commercial.md) |
| **Template** | [Solution proposal template](../../engagement-playbook/templates/solution-proposal-template.md) |
| **Status** | Walked through with the MD, then sent for approval |
| **Companion** | [SOW outline](sow-outline.md) · [Estimate and timeline](estimate-and-timeline.md) · [Risk register](risk-register.md) |

> Fictional scenario. Figures are illustrative and prices must be verified before use.

**To:** the Managing Director, Example Corp
**From:** the Solution Architect
**Subject:** Secure remote work, segmented network and recoverable IT: proposal for delivery

## 1. Executive summary

Your people can work from home safely with their normal company login and a second factor. No
administration page is open to the internet. A failed server, a stolen laptop or ransomware causes
hours, not days, of disruption. Everything is documented so that your IT administrator and your IT
partner can run it without us.

We propose to **deliver this in about ten weeks from signature**: go-live on Saturday 3 July 2027, handover and
support until early August, and the review finished by mid-August, seven weeks before your insurance renewal on
1 October. The external
spend is **about USD 21 800, up to USD 23 250 with contingency**. This is more than the USD 5 000
you first mentioned; section 6 explains why and what that money buys.

## 2. The problem and your goals

| Reported problem | What we found in discovery | Goal | How we will measure it |
|------------------|----------------------------|------|------------------------|
| Staff cannot reach internal apps from home | Workarounds by email; one port-forward | **BG-1** secure access from anywhere | 100 % of staff through single sign-on with a second factor; no inbound port for apps |
| Admin interfaces are exposed | Proxmox page open on the internet with a password only | **BG-2** reduce exposure | No admin interface reachable from the internet; network divided into zones |
| Everything is on one network | A compromised laptop could reach every server | **BG-2** | Same as above |
| Nobody knows how the server is set up | One unknown VM, no documentation | **BG-4** changes traceable and repeatable | At least 90 % of infrastructure changes made through reviewed pull requests |
| A disk failure or ransomware would be a disaster | One USB backup in the same room, never tested | **BG-3** recover quickly | Recovery targets met in a yearly test |
| Cost must stay predictable | Recurring software cost is zero today | **BG-5** keep costs low | Recurring software and service cost of USD 0 |

## 3. The solution in plain language

- **Staff** open their apps (files, wiki, HR) from a link. A company login and a phone prompt
  protect each app. Nothing needs to be installed on staff laptops for the web apps. The office
  network has **no open door** for them.
- **Administrators** reach the management systems through a protected network service that
  checks the person, the device and the permission. If that service or the login provider is
  down, a **sealed emergency path** exists.
- The **office network** is split into six zones (management, servers, public-facing, staff,
  guests, devices). Traffic between zones is blocked unless a rule allows it. Printers and visitors cannot
  reach servers.
- **Backups** go nightly to a separate small server, encrypted, with a weekly copy on a rotated
  disk that is kept off-site. Restores are tested monthly.
- **Everything is written down** and, where possible, defined as code in a repository you own.
  Changes go through review.

Detail for technical readers: [HLD](../03-design/hld.md), [diagrams](../03-design/diagrams/c4-context.md), [ADRs](../02-options-decisions/adr/README.md).

## 4. What you get (deliverables)

| # | Deliverable | Acceptance |
|---|-------------|------------|
| 1 | Network divided into zones with documented rules | FR-05, FR-06, NFR-S4 verified by connection tests |
| 2 | Secure staff access to the three apps | FR-01, FR-02, NFR-S1, NFR-S2 verified; port scan shows no open application ports |
| 3 | Secure administrator access and a tested emergency path | FR-03, FR-04, NFR-S3 verified; break-glass test passes and raises an alert |
| 4 | Backups with an off-site copy and a tested restore | FR-08, NFR-A2, NFR-S9; restore test inside the recovery targets |
| 5 | Monitoring and alerts that link to runbooks | FR-09, NFR-O4 |
| 6 | Documentation, runbooks and a handover with training | NFR-O1; handover test passed |
| 7 | Two weeks of close support after go-live | Hypercare exit criteria met |

## 5. Timeline

| Milestone | Date (planned) |
|-----------|----------------|
| Proposal and walkthrough | Early April 2027 |
| Contract signed | 3 May 2027 |
| Hardware delivered | End of May 2027 |
| Build complete | 21 June 2027 |
| Go-live (Saturday window) | Saturday 3 July 2027 |
| Handover (2 weeks), then two weeks of close support (hypercare) | 9 July to 6 August 2027 |
| Review finished | 13 August 2027 |
| **Insurance renewal** | **1 October 2027** |

The plan has seven weeks of float before the renewal. The biggest unknowns are the **contract
signature** and the **hardware delivery**; both depend on dates outside our control. Detail:
[estimate and timeline](estimate-and-timeline.md).

## 6. Price range

| Item | USD |
|------|----:|
| Architect: discovery (done, fixed) | 1 600 |
| Architect: design agreement (fixed) | 7 600 |
| Architect: delivery, billed on days used, capped | 5 800 expected, **cap 7 250** |
| Hardware (disks, backup server, managed switch, access points, UPS) | 3 400 |
| IT partner support during build (quoted separately by the partner) | 3 400 |
| **External spend** | **≈ 21 800 expected, up to ≈ 23 250** |

Your IT administrator's time (about 14 days) is an internal cost, about USD 4 500.

**Why not USD 5 000?** That figure buys one piece of hardware. The recurring risk and cost sit
elsewhere: backups, documentation, network design and the hours your administrator spends
operating the system. Over five years, **about two thirds of the total cost is people's time**.
The design is built to reduce that part.

**Five-year view:** about USD 40 000 including this project, against an estimated benefit of about USD 54 000
(avoided downtime, avoided ransomware recovery, less time lost on workarounds). This is a **sketch
for discussion**, not a forecast; the insurance renewal is not valued.

Software and service costs are **USD 0** (free software and free service tiers). The only recurring
costs are electricity (about USD 290 a year), spare parts (about USD 300 a year) and an optional domain
name.

## 7. Assumptions the price depends on

| # | Assumption | If false |
|---|------------|----------|
| A-1 | The ISP provides a public IPv4 address | A small relay server is added, estimated USD 100 per year and 1 day of work |
| A-4 | Spare parts replace a hardware support contract | A support contract costs about USD 1 400 per year |
| A-5 | Free plans of Cloudflare and Tailscale cover 25 users and remain free | Operating cost rises; Headscale is a documented fallback |
| A-6 | The three apps work behind the edge proxy | Partly confirmed: large browser uploads need the sync client or the internal name |
| E-1 | The IT administrator is available about two days a week during the build | The build calendar stretches |
| E-2 | The client signs by 3 May and hardware arrives by 31 May | Every later date moves, one week for one week |

## 8. Exclusions

Not part of this proposal (see the [SOW outline](sow-outline.md) for the full list):

- Email, calendar and office tools (cloud suite)
- Laptop management and antivirus
- Telephony
- A second site and high availability (a future option, see ADR backlog)
- CCTV (reserved network zone only; handled as a change request, see [CR-001](change-request-cctv.md))
- Migration of data between old and new applications beyond moving the existing virtual machines

## 9. Main risks

| Risk | What we do |
|------|-----------|
| One server is a single point of failure (R-1) | Accepted for cost; spare parts, tested restore, external status page |
| Network outage when the server is serviced (R-2) | Maintenance windows, emergency port, restore runbook |
| Scope creep (R-10) | Change control from day one |
| One builder, no backup (R-11) | Named IT partner backup |
| Restore never tested (R-13) | Tested before go-live and monthly |

The full list with owners is in the [risk register](risk-register.md).

## 10. Next steps

1. **Walkthrough** of this document with you and your IT administrator (done).
2. **Questions** from you, finance and legal; we answer within two working days.
3. **Signature** of the SOW by 3 May 2027; we then order hardware.
4. **Kick-off** with your IT administrator and the IT partner in the same week.

## 11. Acceptance

| | Name / role | Date | Signature |
|---|-------------|------|-----------|
| Client (budget holder) | Managing director | | |
| Provider | Solution architect | | |
