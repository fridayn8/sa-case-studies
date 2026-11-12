# Backlog

Three sections: **Parked ideas** → **Planned, not executed** → **Done**.

**Rules**

- A new idea goes under *Parked ideas*, in one line. It is **not built**.
- **Before starting any new feature**, review *Planned, not executed* and choose one item.
- Move an item to *Done* with the commit or pull request that completed it.

## Parked ideas

Findings made while importing and writing Case 01 (2026-11-12). Each is a contradiction or gap between
**existing** documents, left unchanged on purpose.

| # | Finding | Where |
|---|---------|-------|
| P-1 | The cost estimate has **no line for the engagement itself** (architect and IT partner fees, about USD 18 k in the [estimate](case-01-example-corp/05-proposal-delivery/estimate-and-timeline.md)); the ROI of about 150 % therefore overstates the return | [cost estimate §4–5](case-01-example-corp/04-security-cost/cost-estimate.md) |
| P-2 | Requirement **C-1** says the budget covers "one small backup appliance only", but the CAPEX buys disks, a switch, access points and a UPS as well | [requirements §6](case-01-example-corp/01-requirements/requirements.md#6-constraints), [cost estimate §1](case-01-example-corp/04-security-cost/cost-estimate.md#1-capex-one-off-hardware) |
| P-3 | **Assumption A-4** (next-business-day support) is treated as true in the LLD hardware table, but the cost estimate replaces vendor support with spare parts; the [as-is assessment](case-01-example-corp/00-pitch-discovery/05-as-is-assessment.md#4-assumptions-log) finds A-4 false | [LLD compute §1](case-01-example-corp/03-design/lld-compute.md) |
| P-4 | **Assumption A-3** (managed switch and access points available) is false in the as-is assessment; requirements v0.1 still lists it as an assumption | [requirements §7](case-01-example-corp/01-requirements/requirements.md#7-assumptions) |
| P-5 | **ADR-0002** says production "should use an Enterprise subscription", which conflicts with the free-only policy (ADR-0010) and NFR-C2 | [ADR-0002](case-01-example-corp/02-options-decisions/adr/0002-hypervisor-proxmox-ve.md) |
| P-6 | **HLD §10** puts hypercare *before* the handover; the playbook, Gantt chart and handover checklist put handover first, then hypercare | [HLD §10](case-01-example-corp/03-design/hld.md#10-transition-from-current-state) |
| P-7 | The **IT partner** (R-7 "IT partner contract") has no cost in the cost estimate | [cost estimate §2–3](case-01-example-corp/04-security-cost/cost-estimate.md) |
| P-8 | The LLD access row for the file service says "upload size limits checked in PoC", but the result is only recorded in the [options analysis](case-01-example-corp/02-options-decisions/options-analysis.md#4-proof-of-concept-the-riskiest-assumption) | [LLD access §3.1](case-01-example-corp/03-design/lld-access.md) |
| P-9 | FR-08 says all VMs and containers are backed up automatically, but the LLD guest catalogue backs up `mon01` weekly and four stateless guests not at all (the HLD speaks of nightly backups) | [LLD compute §3](case-01-example-corp/03-design/lld-compute.md) |
| P-10 | The seed calendar total (21–40 weeks) is 2 weeks below the sum of the stage minima (23 weeks); this repository explains the gap as stage overlap | [timeline §2](engagement-playbook/timeline-and-effort.md#2-seed-figures-for-an-example-corp-sized-engagement) |

## Planned, not executed

- Case 02: brownfield migration with poor documentation
- Case 03: regulated client (compliance-driven requirements)
- ADR-0009: off-site backup target (reserved number)
- Candidate ADRs: second Proxmox node, dedicated firewall, IPv6
- C4 level 3 (component) diagram for one application
- A scoring rubric for the "Stop and think" boxes across all stages
- Owner's personal calibration of the duration table from real experience

## Done

| Item | Done in |
|------|---------|
| Repository configuration, licence, pre-commit, link checker | `chore: add repository configuration and licence` |
| Case 01 requirements, design, diagrams, security and cost imported | `docs(case-01): import requirements, design, diagrams, security and cost` |
| ADR log 0000–0012 imported | `docs(adr): import ADR log (0000–0012)` |
| Scenarios (6) and design-first exercises | `docs(case-01): import scenarios and exercises` |
| Engagement playbook, stages 0–9 | `docs(playbook): add engagement playbook stages 0–9` |
| Timeline, effort and estimation guidance | `docs(playbook): add timeline, effort and estimation guidance` |
| Case 01 pitch, discovery and options analysis | `docs(case-01): add pitch, discovery and options analysis` |
| Case 01 proposal and delivery documents | `docs(case-01): add proposal and delivery documents` |
| Twelve engagement templates and references | `docs(playbook): add engagement templates and references` |
| README, contributing guide, backlog and changelog | `docs: add README, contributing guide, backlog and changelog` |
