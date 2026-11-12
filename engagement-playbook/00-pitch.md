# Stage 0 — Pitch / First Contact

| | |
|---|---|
| **Goal** | Decide whether to start discovery at all, and agree with a named sponsor what discovery will cost and deliver |
| **Typical duration** | 1–2 days effort · 1–2 weeks calendar *(illustrative, see [timeline and effort](timeline-and-effort.md))* |
| **Inputs** | An email, call or referral; whatever the client says they want; your own capacity and track record |
| **Case 01 documents** | [First contact](../case-01-example-corp/00-pitch-discovery/01-first-contact.md) · [Pitch](../case-01-example-corp/00-pitch-discovery/02-pitch.md) |

## Activities

1. **Listen, do not solve.** Take the first call or email and write down *what is said* and, in a
   second column, *what is probably meant*. "We need a VPN" is a solution; the problem is
   hidden behind it.
2. **Qualify the lead** with the [lead qualification checklist](templates/lead-qualification-checklist.md):
   problem, sponsor, budget range, deadline, decision process, fit.
3. **Reflect the problem back** in two sentences and ask the client to correct you. This is the
   cheapest alignment you will ever buy.
4. **Write a one-page pitch** that names the problem, the outcome, the approach to discovery and
   what happens if nothing is done.
5. **Propose a small, paid or explicitly bounded discovery** rather than a full solution. At this
   point you know too little to promise anything else.
6. **Decide go or no-go**, and write down why. A reasoned *no* protects your reputation.

## Questions to ask

**The client**

- What happened that made this a priority *now* and not last year?
- Who is paying, who will use it, and who can say no? Are those the same person?
- What budget range and deadline do you have in mind? Is the deadline tied to an event
  (audit, contract, move, renewal) or is it a wish?
- What have you already tried or bought? Why did it not solve the problem?
- What happens if nothing is done for 12 months?
- Is a solution already chosen? By whom, and on what basis?

**Yourself**

- Do I understand the business well enough to be useful, or am I selling hours?
- Do I have the capacity? An architect shared across engagements delivers 50–70 % of a calendar
  day to each (see [timeline and effort](timeline-and-effort.md)).
- Is there a conflict of interest (a vendor I resell, a person I would have to criticise)?
- What would make me walk away?

## What to think about

- **Problem versus solution.** A client who arrives with a solution has already made decisions you
  are expected to ratify. Your first job is to find the problem it was meant to solve; sometimes
  the solution is right, often it is half right.
- **Sponsor, budget holder and user are three roles.** If nobody owns the budget, nothing will be
  decided; if the user is not in the room, adoption fails later.
- **Budget and deadline are requirements too.** A fixed budget with a vague scope is a risk
  transfer to you. A deadline tied to an external event is a hard constraint; a "nice to have by
  summer" is not.
- **Fit.** Your skills, your availability and the client's culture all matter. Open-source-first
  and automation-heavy designs fit a client with someone who can operate them; they are a poor
  fit for a client who wants to phone one vendor.
- **The cost of doing nothing** is your best sales and qualification argument. If the client
  cannot describe it, the problem may not be painful enough to fund.
- **Political reality.** Who loses power or workload if this succeeds? That person will appear in
  discovery as a stakeholder with concerns.

**Typical red flags**

| Red flag | Why it matters |
|----------|----------------|
| No named sponsor | Nobody can accept the result or release budget |
| "The solution is already chosen" | You are being hired to sign off, not to design |
| Unrealistic deadline or budget | You will pay for the gap |
| Several people give contradictory descriptions of the problem | Discovery will be the real work; price it accordingly |
| Pressure to start before scope or fee is agreed | Unpaid work and unclear expectations |

## Documents produced

| Document | Template | Case 01 |
|----------|----------|---------|
| Lead qualification checklist | [template](templates/lead-qualification-checklist.md) | [First contact](../case-01-example-corp/00-pitch-discovery/01-first-contact.md) |
| One-page pitch | — | [Pitch](../case-01-example-corp/00-pitch-discovery/02-pitch.md) |
| Discovery proposal (scope, duration, fee, what the client must provide) | — | Last section of the pitch |

## Exit gate

| Criterion | Signed off by |
|-----------|---------------|
| A **sponsor is named** and agrees to the discovery scope and fee | Sponsor |
| The qualification checklist has no unresolved *blocker* | Architect |
| Go/no-go decision is written down with its reasons | Architect |

## Common mistakes

- **Pitching a product** instead of a way of working out whether there is a problem worth solving.
- **Starting discovery for free and open-ended.** It becomes a consulting engagement with no
  contract. Time-box it and say what it delivers.
- **Agreeing to the first date** the client names without asking what the date is for.
- **Accepting a pre-chosen solution** and hiding the doubt. Write the doubt down as an
  assumption to test in discovery, politely, in the proposal.
- **Skipping the "what if nothing is done" question**, which is the one that finds the real budget.

## Stop and think

> **Stop and think — the managing director says "just make it cheap"**
>
> In the first call, the managing director of a 25-person company says: "We need remote access to
> our servers, and it has to be cheap. Do not over-engineer it." What do you ask before you accept
> *cheap* as a requirement? Which non-functional requirement might it conflict with? What do you
> write in the pitch?
>
> <details><summary>Model answer</summary>
>
> **Ask first:** cheap compared to what (a number, a previous quote, a competitor)? Cheap to buy or
> cheap to run for five years? What does an hour of downtime or a leaked HR file cost the company?
> Who will operate it, and how many hours per month can they spend? Is "remote access" for staff
> to apps, or for administrators to servers? Those are different problems with different costs.
>
> **Conflicts:** low cost tends to push against availability (no second host, no support
> contract), security (skipping segmentation or MFA) and operability (the cheapest tools need the
> most manual work from a part-time administrator). People cost usually dominates: in Case 01
> about two thirds of the five-year cost is administrator time, so a design that is cheap to buy
> but expensive to run is not cheap.
>
> **In the pitch:** restate the goal as measurable outcomes ("staff reach three apps from home
> with MFA; no admin interface open to the internet"), name the budget as a *range* you will
> test in discovery, and propose to compare total cost over five years for two or three options.
>
> **Self-check rubric:** (1) You asked what *cheap* is measured against. (2) You separated build
> cost from run cost. (3) You named at least one requirement it could conflict with.
> (4) You turned the wish into something testable. (5) You did not promise a price yet.
> </details>

> **Stop and think — "we already decided on a firewall appliance"**
>
> The sponsor tells you the company has chosen a branded firewall appliance and wants you to
> "design around it". You think the real problem (admin interfaces exposed, flat network) can be
> solved without it. How do you respond, and do you take the work?
>
> <details><summary>Model answer</summary>
>
> Do not argue in the first call. Ask what the appliance is expected to solve and who chose it
> (a vendor visit? a past incident?). Treat the choice as a **constraint to examine**, not an
> insult: write it as an assumption ("the appliance is mandatory") and add a discovery question
> that tests it. Take the work if discovery is allowed to compare at least two options and the
> sponsor accepts that the appliance may stay, move or be dropped by evidence. Decline, or price
> the risk, if the decision is final and you would only be rubber-stamping it.
>
> **Self-check rubric:** (1) You asked about the reasoning behind the choice. (2) You separated
> *problem* from *product*. (3) You wrote the decision down as an assumption. (4) You set a
> condition for taking the work. (5) You stayed polite.
> </details>

## References

See [references — stage 0](../references.md#stage-0-pitch-and-first-contact).
