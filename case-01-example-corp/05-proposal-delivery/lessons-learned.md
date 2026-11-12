# Case 01 — Lessons Learned

| | |
|---|---|
| **Document** | Fictional review of the Example Corp engagement: benefits, estimate versus actual, lessons, debt and roadmap |
| **Stage** | [9 Review](../../engagement-playbook/09-review.md) |
| **Template** | [Lessons-learned template](../../engagement-playbook/templates/lessons-learned-template.md) |
| **Status** | Presented to the sponsor on 14 September 2027, accepted; follow-up check booked for November 2027 |

> Fictional scenario. All results are invented for teaching. A real review uses real measurements.

## 1. Summary

The platform went live on **Saturday 7 August 2027**: five weeks later than the plan (3 July), about a week after
the managing director's first wish (before the summer holidays) and **eight weeks before** the insurance renewal;
the review finished 2.5 weeks before it. All Must requirements passed their acceptance tests. The engagement ran **4 days (10 %) over the effort estimate** and
**about 4.5 weeks over the calendar plan**, mostly because of two things the architect does not control:
the contract approval and a late hardware delivery.

## 2. Benefits against the business goals

Measured five weeks after go-live (11 September 2027).

| Goal | KPI | Result | Met? |
|------|-----|--------|:----:|
| BG-1 Secure access from anywhere | 100 % of staff via SSO and MFA; no inbound ports for apps | 23 of 25 staff at the end of hypercare; **25 of 25** after two laptops were re-enrolled in week 5. No inbound application ports | ✅ (after fix) |
| BG-2 Reduce exposure | No admin interface reachable from the internet; network segmented | Confirmed by external scan; six zones in operation; **two administrator accounts without MFA found and fixed** | ✅ |
| BG-3 Recover quickly | RTO and RPO met in a yearly DR test | Firewall restored in 1 h 40 min (RTO 2 h); file service in 3 h 10 min (RTO 8 h); RPO 24 h | ✅ |
| BG-4 Traceable changes | At least 90 % of changes via pull requests | 94 % in the first five weeks; the 6 % were console changes during hypercare, later codified | ✅ |
| BG-5 Predictable cost | Recurring software and service cost USD 0 | USD 0 software; electricity about USD 26 a month against USD 24 planned | ✅ |

The insurance questionnaire was answered truthfully on all four questions that had been problems in
discovery (admin exposure, MFA, segmentation, backups).

## 3. Estimate versus actual

### Effort (days)

| Stage | Expected | Actual | Delta | Why |
|-------|---------:|-------:|------:|-----|
| 0 Pitch | 1.5 | 1.5 | 0 | |
| 1 Discovery | 4.0 | 4.5 | +0.5 | Access to the router and the ISP answer took longer |
| 2 Requirements | 3.5 | 3.5 | 0 | |
| 3 Options and decisions | 4.5 | 5.5 | +1.0 | Lab environment for the PoC took a day to build |
| 4 Design and review | 8.0 | 9.0 | +1.0 | Two review rounds; the threat model fed back into the access design |
| 5 Proposal and commercial | 3.0 | 3.0 | 0 | |
| 6 Build oversight | 6.0 | 7.0 | +1.0 | CR-001 analysis and five deviations |
| 7 Test and go-live | 4.0 | 4.0 | 0 | |
| 8 Handover and operate | 3.5 | 4.0 | +0.5 | Extra training session for HR |
| 9 Review | 1.0 | 1.0 | 0 | |
| **Total** | **39.0** | **43.0** | **+4.0 (+10 %)** | Inside the 25 % contingency (48.75 days) |

**Fixed-price effect:** the discovery fee (fixed, 4 days) and the design agreement (fixed, 19 days)
were exceeded by 0.5 and 2.0 days, absorbed by the architect (about USD 1 000). The delivery fee was billed
on actual days (16 days, USD 6 400) and stayed under the cap (USD 7 250).

### Calendar (days)

| Stage | Planned | Actual | Delta | Why |
|-------|--------:|-------:|------:|-----|
| 0 Pitch | 10 | 11 | +1 | |
| 1 Discovery | 18 | 21 | +3 | Interview scheduling; ISP answer |
| 2 Requirements | 10 | 10 | 0 | |
| 3 Options and decisions | 18 | 20 | +2 | PoC environment |
| 4 Design and review | 25 | 30 | +5 | Two review rounds |
| 5 Proposal | 10 | 10 | 0 | |
| **Client approval and contract** | 28 | 42 | **+14** | Second director's approval; legal review of the SOW |
| 6 Build oversight | 49 | 56 | +7 | **Hardware arrived one week late**; builder availability |
| 7 Test and go-live | 18 | 18 | 0 | |
| 8 Handover | 14 | 14 | 0 | |
| Hypercare | 14 | 14 | 0 | |
| 9 Review | 7 | 7 | 0 | |
| **Total** | **221** | **253** | **+32 days (about 4.5 weeks)** | About 17 of the 49 planned float days to the insurance date were left |

**Reading:** 14 of the 32 days were the **client approval**, the item the playbook marks as outside
the architect's control. The plan's seven weeks of float to the insurance date was mostly used (2.5 weeks were left); it was
the right amount, but only just.

## 4. What worked

- **Weights agreed before scoring** in the options analysis; nobody argued with the result later.
- **The PoC** found the upload limit before the build, and the sync client mitigation was in place by go-live.
- **The change request** for CCTV took two days and ended with a clear decision, not an argument.
- **Restore tests before the Go/No-Go** found one wrong path in a runbook; it was fixed before the window.
- **Leaving the old router untouched** meant the first Saturday had a real way back (it was not needed).
- **One-to-one interviews** surfaced the payroll script and the unknown VM.

## 5. What did not work

| Lesson | Evidence | Change for next time |
|--------|----------|----------------------|
| Fixed prices on stages with open dependencies cost the architect days | Discovery +0.5 d, design agreement +2.0 d | Price the design agreement with an assumptions list and a cap, or a range |
| The client approval was planned at 4 weeks; it took 6 | +14 days | Ask for the signature date and the approval chain in stage 0; plan six weeks |
| Hardware lead time was taken from the supplier's first answer | +7 days | Ask for the delivery date in writing and add a one-week buffer |
| Two administrator accounts without MFA were found only at the five-week check | BG-2 finding | Add an account audit to the Go/No-Go checklist |
| Two staff laptops were not enrolled in time | BG-1 shortfall | Add a device-enrolment step to UAT, with a list of names |
| Runbook 2.12 (disaster recovery) was only a tabletop at handover | Condition at acceptance | Include a timed DR test in stage 7 |

## 6. Debt, accepted risks and unvalidated assumptions

| Item | Owner | Review date |
|------|-------|-------------|
| Single host (R-1), network outage when the host is serviced (R-2) | Managing director | At the first anniversary or if the availability target changes |
| ADR-0009 (off-site backup target) still reserved: weekly rotated USB disks in use | IT administrator | Before the first disk refresh |
| Edge free-plan limit: re-verify at each renewal (A-5, R-16) | IT administrator | Every six months |
| CCTV zone: pending change (CR-001, deferred) | Facility manager, IT administrator | Booked for October |
| Old router and unknown VM `test2`: clean-up pending | IT administrator | Two weeks after hypercare |
| Capacity: backup storage reaches 70–80 % in year 3 | IT administrator | Before the end of year 2 |

## 7. Roadmap

| # | Item | Trigger | Owner |
|---|------|---------|-------|
| 1 | DR test with the managing director present (yearly) | Condition at handover | IT administrator |
| 2 | CCTV zone via the normal change process | CR-001 deferred | Facility manager |
| 3 | Decision on the off-site backup target (ADR-0009) | Before the first disk refresh | Architect, IT administrator |
| 4 | Second Proxmox node and HA | Budget increase or a tighter availability target (R-1) | Managing director |
| 5 | A dedicated firewall appliance | Network outages during host maintenance become a problem (R-2) | IT administrator |
| 6 | IPv6 | ISP offers a stable prefix | IT administrator |

## 8. Calibration for the next engagement

| Stage | Observation | Personal factor |
|-------|-------------|-----------------|
| 1 Discovery | Waiting for access; calendar +17 % | Plan 3 weeks, not 2.5 |
| 4 Design | Two review rounds needed | Plan two reviewers' slots in advance |
| 5 Approval | +50 % over plan | Plan six weeks of approval and legal, or ask for a date |
| 6 Build oversight | Effort +17 % because of change requests | Multiply by 1.2 if the client is new to change control |
| Overall effort | +10 % | A 25 % contingency was sufficient; 15 % would not have been |

## 9. Follow-up

A check is booked for **November 2027**: re-measure BG-1 to BG-5, review the first quarterly
break-glass test, confirm the first disk rotation and update this register.
