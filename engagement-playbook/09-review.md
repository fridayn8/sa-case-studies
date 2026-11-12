# Stage 9 — Review

| | |
|---|---|
| **Goal** | Check honestly whether the business goals were met, record what was learned, and write down the debt taken on and the next steps so that the engagement improves the next one |
| **Typical duration** | 1 day effort · 1 week calendar *(illustrative, see [timeline and effort](timeline-and-effort.md))* |
| **Inputs** | Business goals and KPIs from the requirements, estimates versus actuals, change and incident log, hypercare notes |
| **Case 01 documents** | [Lessons learned](../case-01-example-corp/05-proposal-delivery/lessons-learned.md) |

## Activities

1. **Measure the goals**: compare each business goal's KPI with reality after a few weeks of
   operation (for example BG-1: 100 % of staff through SSO and MFA, zero inbound ports).
2. **Compare estimates with actuals** (effort, calendar, cost) in the
   [estimation worksheet](templates/estimation-worksheet.md); calculate the delta per stage.
3. **Run a blameless lessons-learned session** with the client's operations and the team: what
   worked, what did not, what surprised us. Use the
   [lessons-learned template](templates/lessons-learned-template.md).
4. **List the debt**: what was postponed, which risks were accepted, which assumptions stayed
   unvalidated, which shortcuts were taken.
5. **Write a short roadmap**: the next three to six items with owners (for example: second node,
   off-site backup target, DR test, IPv6).
6. **Update your own calibration**: durations, risks that materialised, estimates that were far
   off.
7. **Present the report** to the sponsor and get it accepted. Offer a follow-up check at
   three or six months.

## Questions to ask

**Sponsor and operations**

- Which goals did we reach? Which did we not, and why?
- What would you do differently if you started again?
- What do you now wish you had asked in the first week?
- What is still annoying, slow or risky? What did we leave behind?

**The team and yourself**

- Where was my estimate most wrong, and what did I assume that was false?
- Which decision would I now change? Is there an ADR to supersede?
- Which risk did we accept that is now a bigger problem?
- Which of this should become a template, a checklist or a rule?

## What to think about

- **Measure against the original goals**, not against what was built. "We delivered everything in
  the SOW" and "the business goal was met" are different statements; the review is about the
  second.
- **Blameless means specific.** "The requirement was vague, so two people understood it differently"
  can be fixed; "someone made a mistake" cannot.
- **Technical debt is a decision**, not an accident, when it is recorded: what, why, owner, review
  date. Unrecorded debt becomes surprise cost.
- **Estimate calibration is a skill.** If your estimates are consistently 30 % low in build oversight,
  the factor is a fact about you, not bad luck. Apply it next time.
- **Follow-up is where trust is earned.** A review report with no follow-up reads as a
  closing ritual; a check at three months turns it into the start of the next engagement.
- **Keep the good and the bad.** A lessons-learned file that only lists successes teaches nothing.
- **ADR hygiene.** Decisions that changed during the engagement should have their status updated
  (superseded, deprecated) so the log tells the truth.

**Typical red flags**

| Red flag | What to do |
|----------|------------|
| No follow-up scheduled | Book a three-month check before closing |
| Lessons not recorded | Write three lessons today, even if short |
| Goals measured by deliverables | Re-measure against the KPIs |
| Debt hidden | List it with owners and dates |
| Blame instead of cause | Rewrite as "what in the process allowed this" |

## Documents produced

| Document | Template | Case 01 |
|----------|----------|---------|
| Lessons learned | [template](templates/lessons-learned-template.md) | [Lessons learned](../case-01-example-corp/05-proposal-delivery/lessons-learned.md) |
| Benefits review (KPIs versus actuals) | — | Benefits section of the lessons-learned document |
| Roadmap and debt list | — | Roadmap section of the lessons-learned document |
| Updated estimation worksheet | [worksheet](templates/estimation-worksheet.md) | [Estimate and timeline](../case-01-example-corp/05-proposal-delivery/estimate-and-timeline.md) |

## Exit gate

| Criterion | Signed off by |
|-----------|---------------|
| **Report accepted** by the sponsor | Sponsor |
| Every business-goal KPI has a measured result or a date to measure | Architect |
| Debt, accepted risks and next steps have owners | Sponsor and IT owner |
| Actuals recorded for future estimates | Architect |

## Common mistakes

- **Skipping the review** because the project "went well" or because everyone is tired.
- **Making it a blame session**, so people stop telling you what really happened.
- **Measuring outputs** (documents delivered) rather than outcomes (goals reached).
- **Not recording the estimate versus actual.** You will repeat the same error.
- **Letting the roadmap sit in a document** no one owns.

## Stop and think

> **Stop and think — "we met every deliverable"**
>
> The final report says: "All 14 deliverables in the SOW were delivered on time." Three months after
> go-live, only 60 % of staff use the new access path and two admin accounts still bypass MFA.
> What does the review need to say?
>
> <details><summary>Model answer</summary>
>
> The review must separate **output** (deliverables) from **outcome** (goals): BG-1 was "100 % of
> staff access via SSO and MFA", and 60 % is a miss. Investigate why: training gap, an app that
> does not work well behind the tunnel, old shortcuts still allowed by the firewall? Record the two
> bypassing admin accounts as a **security finding** with an owner and a date, not as a footnote.
> Offer corrective actions (training, remove the old path, enforce MFA) and propose when to
> re-measure. Credit what worked, but let the headline be the KPI.
>
> **Self-check rubric:** (1) You compared against the goal, not the SOW. (2) You looked for causes.
> (3) You treated the MFA bypass as a finding. (4) You proposed actions with owners.
> (5) You scheduled a re-measurement.
> </details>

## References

See [references — stage 9](../references.md#stage-9-review).
