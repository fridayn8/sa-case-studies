# Stage 2 — Requirements

| | |
|---|---|
| **Goal** | Turn what stakeholders said into a **measurable, prioritised, signed** baseline that design, estimate and acceptance can all point back to |
| **Typical duration** | 3–4 days effort · 1–2 weeks calendar *(illustrative, see [timeline and effort](timeline-and-effort.md))* |
| **Inputs** | Confirmed as-is, stakeholder map, interview notes, assumptions log |
| **Case 01 documents** | [Requirements](../case-01-example-corp/01-requirements/requirements.md) |

## Activities

1. **Write business goals first** with a measure each (a KPI). Everything below must serve one.
2. **Separate functional requirements (FR)** from **non-functional requirements (NFR)**:
   what the system does versus how well, how safely, how fast, how recoverable, at what cost.
3. **Make every NFR measurable**: a number, a unit, a period, how it is checked.
4. **Prioritise with MoSCoW** (Must, Should, Could, Won't). Agree "Won't this time" explicitly.
5. **Run a business impact analysis (BIA)**: what does an hour of downtime cost, per service?
   From it derive **RTO** (how long can it be down) and **RPO** (how much data can be lost).
6. **List constraints and assumptions.** Constraints remove options; assumptions are risks until
   validated.
7. **Define acceptance criteria**: how will we know each Must is met?
8. **Seed the traceability table** (requirement → where it is addressed) and keep it alive in every
   later stage.
9. **Get the baseline signed** and start change control: from now on, changes go through a
   [change request](templates/change-request-impact-analysis.md).

## Questions to ask

**Sponsor and stakeholders**

- Which goals are **musts**, and what is the consequence if each is missed?
- What does an hour of downtime cost, per service? Who notices first?
- How much data can you afford to lose: an hour, a day, a week? (RPO)
- How long can the service be unavailable before it hurts? (RTO)
- Who has to accept the result, by which test?
- What is explicitly **not** part of this project?

**Yourself**

- Can I test this requirement? If two people could read it differently, it is not done.
- Is this a requirement or a design decision in disguise ("must use product X")?
- Is the number a real need or a guess someone made up in the meeting?
- Do two requirements conflict? Which one wins?

## What to think about

- **NFRs drive architecture.** Features rarely decide the shape of the solution; availability,
  security, recoverability and cost do. In Case 01 the 8-business-hour restore target
  (NFR-A3) is what justifies next-business-day hardware support or spare parts instead of a second
  host.
- **Measurable beats adjectival.** "Highly available" is a wish; "≥ 99.5 % per month during
  Monday–Friday 08:00–18:00" is a requirement. The difference between the two is a fixed amount
  of money.
- **Each extra nine costs more than the last.** Ask what the business loses at 99.5 % versus
  99.9 %; often the answer is "not much", and that changes the design and the price.
- **RTO and RPO per service, not per company.** The firewall VM has a 2-hour RTO because the
  office is offline without it; the wiki has 24 hours. One number for everything over-spends on
  the wiki or under-protects the firewall.
- **Priority has to hurt.** If everything is a Must, nothing is. Ask "if we could only deliver
  half, which half?"
- **Assumptions are debts.** A-1 in Case 01 (no CGNAT at the ISP) is cheap to check now and
  expensive to discover during cutover.
- **Requirements change.** Plan for it: version the baseline, record who approved each change, and
  show the impact on cost and time before approving.

**Typical red flags**

| Red flag | What to do |
|----------|------------|
| "Everything is a must" | Force a ranking, or price each item |
| Unmeasurable NFR ("fast", "secure", "user friendly") | Rewrite with a number, a period and a test |
| A requirement that names a product | Ask which need the product serves, record that instead |
| No acceptance criteria | The project cannot be closed; write them now |
| The sponsor will not sign | Find out what they do not trust, not what they want to change |

## Documents produced

| Document | Template | Case 01 |
|----------|----------|---------|
| Requirements specification (goals, FR, NFR, constraints, assumptions, out of scope) | [handbook requirements template](https://github.com/fridayn8/sa-handbook/blob/main/templates/requirements-template.md) | [Requirements](../case-01-example-corp/01-requirements/requirements.md) |
| Business impact analysis (RTO/RPO per service) | — | [Requirements §5.1](../case-01-example-corp/01-requirements/requirements.md#51-availability-and-recovery) |
| Prioritised list (MoSCoW) | — | Priority column in [requirements §4](../case-01-example-corp/01-requirements/requirements.md#4-functional-requirements) |
| Traceability table (seed) | — | [Requirements §9](../case-01-example-corp/01-requirements/requirements.md#9-traceability) |

## Exit gate

| Criterion | Signed off by |
|-----------|---------------|
| **Requirements baseline signed**, version recorded | Sponsor |
| Every NFR is measurable and every Must has an acceptance criterion | Architect and IT owner |
| Every assumption has an impact and a validation plan | Architect |
| Change control is agreed: who may request, who approves | Sponsor |

## Common mistakes

- **Writing solutions as requirements** ("the system must use a VPN"). You remove options before
  you have compared them.
- **Copying NFR numbers** from another project or a template without asking what this business
  loses.
- **Letting priorities stay vague** so that later scope arguments have no reference point.
- **Forgetting the people NFRs**: who operates this, how many hours per month, with what skills
  (NFR-O3 in Case 01).
- **Skipping the signature** because the relationship is good. Goodwill does not survive a
  scope dispute; a baseline does.

## Stop and think

> **Stop and think — "99.99 % availability"**
>
> The managing director reads that "four nines" is standard and asks for **99.99 %**
> availability. Your design is one host with fast restore. What do you do?
>
> <details><summary>Model answer</summary>
>
> Translate the number: 99.99 % over a month is about **4 minutes** of downtime; 99.5 % during
> business hours (Case 01) is about **1 hour per month** of allowed outage inside the
> roughly 217 business hours (10 hours × about 21.7 working days). Ask what a minute of downtime costs, which hours matter (a 3 a.m. outage
> of a file server costs almost nothing) and whether the MD would pay for a second host, replicated
> storage, a second ISP link and 24/7 on-call. Use the BIA numbers: with a USD 500 per hour impact
> and an expected 10 hours of downtime avoided, there is a ceiling on what is reasonable to spend.
> Offer two or three priced levels and let the sponsor choose, then record the choice as NFR-A1 with
> the measurement window and method.
>
> **Self-check rubric:** (1) You converted the percentage into minutes. (2) You tied it to a
> business cost. (3) You separated hours that matter from hours that do not. (4) You presented
> priced options. (5) You wrote the final number with period and measurement method.
> </details>

> **Stop and think — a requirement that is a solution**
>
> A draft requirement says: "FR-03: administrators connect through the OpenVPN server." What is
> wrong with it, and what would you write instead?
>
> <details><summary>Model answer</summary>
>
> It names a **product** and so removes options before the options stage. Ask what need it
> serves: administrators must manage Proxmox, the firewall and the servers remotely, with strong
> authentication, without exposing admin interfaces to the internet. Write FR-03 as that need
> ("Administrators can manage Proxmox, OPNsense and servers remotely") and add NFRs for the
> constraints (SSO and MFA, interfaces reachable only from the management network). Record
> "client prefers OpenVPN" as a stakeholder preference to be weighed in the options analysis, not
> as a requirement. It may still win.
>
> **Self-check rubric:** (1) You spotted the product name. (2) You recovered the underlying need.
> (3) You split the need into FR and NFR. (4) You kept the preference visible. (5) You deferred
> the choice to stage 3.
> </details>

## References

See [references — stage 2](../references.md#stage-2-requirements).
