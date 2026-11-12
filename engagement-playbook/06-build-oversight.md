# Stage 6 — Build Oversight

| | |
|---|---|
| **Goal** | Make sure what is built is still the design, decide which deviations are acceptable, and keep scope, cost and risk visible while others do the building |
| **Typical duration** | 4–8 days effort (about 10–15 % of the architect's time) · 4–10 weeks calendar *(illustrative, see [timeline and effort](timeline-and-effort.md))* |
| **Inputs** | Signed SOW, approved design, risk register, ordered hardware, a build team and a schedule |
| **Case 01 documents** | [Change request: CCTV](../case-01-example-corp/05-proposal-delivery/change-request-cctv.md) · [Risk register](../case-01-example-corp/05-proposal-delivery/risk-register.md) · build in [`sa-projects`](https://github.com/fridayn8/sa-projects) |

## Activities

1. **Kick off the build** with the IT owner and builders: design walk-through, definition of
   done, who decides what, how to ask questions.
2. **Review work in small pieces**: pull requests, configuration reviews and short demos, not a big
   reveal at the end. Check each piece against the requirement it serves.
3. **Keep a design-deviation log**: every difference between design and build, the reason, the
   decision (accept, fix, change the design) and who decided.
4. **Run change control**: every request is assessed for design, cost, time and risk with a
   [change request impact analysis](templates/change-request-impact-analysis.md), and decided by
   the person with authority.
5. **Report status** on a fixed rhythm: done, next, blocked, risks, decisions needed. Short and
   honest.
6. **Update the design** when an accepted deviation changes it, so that the as-built is true.
7. **Track hardware and client dependencies** (delivery dates, access, test users, change windows).
8. **Re-estimate** at the gate and at any significant change.

## Questions to ask

**Builders and the IT owner**

- Is this what the design says? If not, why, and who agreed?
- Is the blocker a misunderstanding of the design or a real flaw in it?
- Which part would you like to change? What does it fix, and what does it break?
- What did we find that the design did not foresee?

**Client and sponsor**

- Is this request a change to what we agreed, or a part of it that we described badly?
- Who pays for it, in money or in date?
- Can it wait until after go-live as a separate piece of work?

**Yourself**

- Am I reviewing early enough that a correction is cheap?
- Is the build drifting away from the design in small steps that are individually reasonable?
- Am I still the right person to decide this, or should the sponsor?

## What to think about

- **Deviations are information.** Most are fine; the important thing is that they are *seen and
  decided*. Silent drift leaves you with an as-built nobody understands.
- **Is it a change or a misunderstanding?** If the signed requirement covers it, build it. If it
  was never in the baseline, it is a change request. The line between the two is the reason for
  stage 2.
- **Scope creep arrives politely**, as a favour ("while you are in the cupboard, could you also
  add CCTV?"). The right answer is not "no", it is "yes, and here is what it costs and what it
  delays; shall we raise a change request?"
- **The impact analysis has four parts**: design (what changes), cost, time (including the
  critical path) and risk (including security). Leave one out and the decision is made blind.
- **Hardware lead time is the silent killer.** A change that needs new hardware moves the date by
  weeks, not days.
- **Protect the design intent**, not the design text. If a builder finds a simpler way to meet the
  same requirement, accept it and update the document.
- **Keep the sponsor informed before they ask.** A bad-news message in week 4 is a conversation;
  in week 9 it is a dispute.

**Typical red flags**

| Red flag | What to do |
|----------|------------|
| Scope creep ("also add CCTV") | Raise a change request with impact analysis |
| Build drifts from the HLD in small steps | Compare build against design every week; update the design or fix the build |
| Status reports are always green | Ask for the evidence behind the colour |
| Builders stop asking questions | Check whether they understood, or whether they are afraid |
| Hardware late and nobody told the sponsor | Put dependencies on the status report with dates |

## Documents produced

| Document | Template | Case 01 |
|----------|----------|---------|
| Change requests with impact analysis | [template](templates/change-request-impact-analysis.md) | [Change request: CCTV](../case-01-example-corp/05-proposal-delivery/change-request-cctv.md) |
| Status reports | — | One-page format in the [estimate and timeline](../case-01-example-corp/05-proposal-delivery/estimate-and-timeline.md#status-reporting) |
| Design-deviation log | — | Table in the [change request](../case-01-example-corp/05-proposal-delivery/change-request-cctv.md#design-deviations-seen-during-the-build) |
| Updated risk register | [template](templates/risk-register-template.md) | [Risk register](../case-01-example-corp/05-proposal-delivery/risk-register.md) |

## Exit gate

| Criterion | Signed off by |
|-----------|---------------|
| **Build complete against the definition of done** (each Must has passed its acceptance check) | IT owner and architect |
| Every deviation is logged, decided and reflected in the design | Architect |
| All change requests are closed (approved, rejected or parked) | Sponsor |
| Open defects are listed with owners and a plan | IT owner |

## Common mistakes

- **Reviewing only at the end.** The cost of a wrong decision rises with every week it is built on.
- **Approving changes in the corridor.** A verbal "sure" is a commitment you will be asked to honour
  at no cost.
- **Saying no without an alternative.** "Not in scope" ends the conversation; "not in scope, here
  is how and when" continues it.
- **Letting the architect become the builder.** You lose perspective and the team loses ownership.
- **Not updating the design.** The as-built becomes the new design by accident.

## Stop and think

> **Stop and think — "also add CCTV"**
>
> Midway through the build, the facility manager asks the IT administrator to "also add the CCTV
> cameras to the new network". The IT administrator tells you in the hallway. What do you do, and
> what do you want to know before answering?
>
> <details><summary>Model answer</summary>
>
> Do not say yes or no in the hallway. First, is it in the baseline? The requirements list FR-06
> ("printers and IoT are isolated") and the LLD **reserves VLAN 70 for CCTV**, but there is no
> requirement for CCTV itself, so it is a **change**. Ask: how many cameras, which recorder, who
> needs to view footage and from where, how long is footage retained (privacy duties), is the
> vendor remote access required? Then run the impact analysis: **design** (new VLAN rules:
> cameras to recorder only, no internet), **cost** (switch ports, PoE budget, storage), **time**
> (does it touch the critical path? firewall rules have to be changed in a maintenance window),
> **risk** (new vendor device with remote access, footage is personal data). Take it to the person
> with authority (the managing director), and record the decision either way.
>
> **Self-check rubric:** (1) You checked the baseline. (2) You asked what is actually wanted.
> (3) You covered design, cost, time and risk. (4) You sent it to the decision maker.
> (5) You recorded the decision.
> </details>

> **Stop and think — a builder proposes a shortcut**
>
> A builder suggests allowing the administrators' laptops to reach the Proxmox web interface
> from the staff network "just for the build period" because the management VLAN port is
> inconvenient. It would save a day. How do you decide?
>
> <details><summary>Model answer</summary>
>
> Check the requirement: NFR-S3 says admin interfaces are reachable **only from the management
> VLAN**. The shortcut is a deviation from a Must. Ask the question behind it: what makes the
> management path inconvenient? If it is a set-up problem (an access port, a route), fix it, because
> it will be needed in operations. If the team still wants to deviate, treat it as a **temporary
> waiver** with an owner, an expiry date, a log entry and a firewall rule that is removed
> automatically or checked at the gate. A "temporary" rule with no owner is permanent.
>
> **Self-check rubric:** (1) You found the requirement. (2) You looked for the underlying problem.
> (3) You used a time-boxed, logged waiver if at all. (4) You named the person who approves.
> (5) You made removal verifiable.
> </details>

## References

See [references — stage 6](../references.md#stage-6-build-oversight).
