# Case 01 — Statement of Work (Outline)

| | |
|---|---|
| **Document** | SOW outline for the delivery stages |
| **Stage** | [5 Proposal and commercial](../../engagement-playbook/05-proposal-and-commercial.md) |
| **Template** | [SOW outline template](../../engagement-playbook/templates/sow-outline-template.md) |
| **Version** | 1.0 (outline) |
| **Status** | Attached to the [solution proposal](solution-proposal.md); signed at the stage 5 gate |

> Fictional scenario. An outline for learning: a real SOW needs legal review.

## 1. Purpose and parties

This statement of work covers the **delivery stages** (build oversight, test and go-live, handover
and review) of the Example Corp Secure Office Platform. Discovery and the design agreement are
complete and invoiced separately. Parties: Example Corp (client, represented by the managing director) and the
Solution Architect (provider).

## 2. Scope

**In scope**

- Oversight of the build against the approved [design](../03-design/hld.md): reviews, deviation log,
  change control, status reports.
- The test plan, user acceptance testing, the cutover plan and the Go/No-Go meeting.
- Handover: as-built documentation, runbooks, training sessions, support model, hypercare.
- The review: KPI measurement, estimate versus actual, lessons learned, roadmap.

**The build itself** is performed by the client's IT administrator with the IT partner. The architect
oversees, reviews and advises; the architect does not hold production administrator rights after
handover.

## 3. Deliverables and acceptance criteria

| # | Deliverable | Acceptance criteria | Requirement IDs |
|---|-------------|--------------------|-----------------|
| D1 | Build review reports (weekly status, deviation log) | Delivered every Friday during stages 6–8 | n/a |
| D2 | Test plan and results | Every Must requirement has a test and an owner; results recorded | FR-01…FR-08, NFR-S1…S4 |
| D3 | Cutover plan with rollback | Rehearsed in the lab; rollback timing measured | n/a |
| D4 | Go/No-Go checklist | Signed, with backups **verified by restore** | NFR-A2, NFR-A3 |
| D5 | As-built documentation | Matches the running system; reviewed by the IT administrator | NFR-O1 |
| D6 | Runbooks (at least the list in the [handover checklist](handover-checklist.md)) | Each executed once by the IT administrator from the text alone | NFR-O1, NFR-O4 |
| D7 | Training sessions (3) | Attendance recorded; hands-on exercises done | n/a |
| D8 | Hypercare (2 weeks) | Exit criteria in the handover checklist met | n/a |
| D9 | Review report | Accepted by the sponsor | BG-1…BG-5 |

**Minimum viable result** (if the schedule is at risk): the Proxmox admin interface is no longer
reachable from the internet, the staff web apps are behind SSO and MFA, and a verified backup exists.
These can be delivered before the insurance renewal even if other items move.

## 4. Responsibilities

| Activity | Architect | IT administrator | IT partner | Managing director |
|----------|:---------:|:----------------:|:----------:|:-----------------:|
| Design review and deviation decisions | **A/R** | C | C | I |
| Build (configuration, code, migration) | A | **R** | C | I |
| Hardware ordering | C | R | I | **A** (budget) |
| UAT participation | C | R | I | **A** |
| Cutover execution | C | **R** | R | I |
| Go/No-Go decision | R | C | C | **A** |
| Approve production changes | C | R | C | **A** |
| Incident response after handover | I | **R** | R | I |

*R = Responsible, A = Accountable, C = Consulted, I = Informed.*

**Client responsibilities** (dependencies with dates): about two days a week of IT administrator time
during the build; access to systems and the ISP; test users from each group; a Saturday maintenance
window agreed in advance; timely answers (two working days) to review questions.

## 5. Change control

1. **Request:** anyone may propose a change; only the managing director (or a delegate named in writing)
   may approve one.
2. **Assess:** the architect completes an impact analysis within three working days: design,
   cost, time, risk (see the [template](../../engagement-playbook/templates/change-request-impact-analysis.md)).
3. **Decide:** approve, reject or defer; the decision and the reason are recorded.
4. **Update:** approved changes update the requirements baseline, design, estimate and risk register.
5. **Pay:** approved changes that add effort are billed on days used at the agreed rate.

Example: [CR-001, CCTV](change-request-cctv.md).

## 6. Commercial terms (summary)

| Item | Terms |
|------|-------|
| Delivery fee | Time and materials at USD 400 per day, **capped at USD 7 250** (expected 14.5 days, 25 % contingency) |
| Invoicing | At end of stage 6, at go-live and at the end of the review, on days used |
| Hardware | Ordered and paid by the client; the architect advises |
| Expenses | Included |
| Payment terms | 30 days |
| Termination | Either party with 14 days' notice; work done is paid |

## 7. Assumptions the price depends on

A-1 (public IPv4), A-4 (spare parts instead of a support contract), A-5 (free-tier terms), A-6 (apps behind
the proxy, partly confirmed), the client signs by 3 May 2027, hardware arrives by 31 May 2027, the IT
administrator is available about two days a week. If one is false, the architect raises a change request.

## 8. Out of scope

- Email, calendar and office tools; laptop management and antivirus; telephony.
- A second site, a second Proxmox node and high availability.
- CCTV equipment and its network (a reserved network zone only), handled by a change request.
- Migration of application data between different products.
- Operation of the system after hypercare (client responsibility).
- Legal and data protection advice (the HR manager holds the data protection role).

## 9. Acceptance and closure

The engagement closes when: the Go decision was taken and the system is live; operations accepted the
handover in writing; hypercare exit criteria are met; and the sponsor accepted the review report.
