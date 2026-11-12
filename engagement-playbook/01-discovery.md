# Stage 1 — Discovery

| | |
|---|---|
| **Goal** | Understand what exists today, who depends on it, what people want and fear, and what limits the solution, well enough that the client confirms your picture is right |
| **Typical duration** | 3–5 days effort · 2–3 weeks calendar *(illustrative, see [timeline and effort](timeline-and-effort.md))* |
| **Inputs** | The signed discovery scope from stage 0, access to people, systems and documents |
| **Case 01 documents** | [Plan and questionnaire](../case-01-example-corp/00-pitch-discovery/03-discovery-plan-and-questionnaire.md) · [Stakeholders and interviews](../case-01-example-corp/00-pitch-discovery/04-stakeholders-and-interviews.md) · [As-is assessment](../case-01-example-corp/00-pitch-discovery/05-as-is-assessment.md) |

## Activities

1. **Plan the discovery**: who to interview, in which order, which systems to inspect, which
   documents to request. Book interviews early; scheduling is what makes discovery slow.
2. **Map the stakeholders** with the [stakeholder map](templates/stakeholder-map.md): interest,
   influence, what they fear, what they want, what they will block.
3. **Interview** each group separately, 30–60 minutes, with the
   [discovery questionnaire](templates/discovery-questionnaire.md) as a guide, not a script.
   Write the summary the same day and send it back for correction.
4. **Assess the as-is state**: inventory (hardware, software, network, data), dependencies,
   owners, backups, access paths, incidents in the last year, contracts and licences.
5. **Keep an assumptions log**: every "I think", every "they told me" that you cannot yet prove
   gets an ID, an impact if false and a way to validate it.
6. **Start the risk register** with what you already see. It will grow in every stage.
7. **Present the as-is picture** to the client and get it confirmed in writing.

## Questions to ask

**Stakeholders**

- What does your day look like, and where does the current system get in your way?
- What are you afraid will happen if we change this?
- If this project were a complete success in a year, what would be different for you?
- Who else should I talk to? Who would be upset if they were not asked?
- What is the thing nobody wants to talk about?

**The current system**

- What exists today, who owns each piece, who last changed it and why?
- What depends on it, including things nobody documented (a script, a spreadsheet, a printer)?
- How do backups work, and when was a restore last tested?
- What incidents happened in the last 12 months, and how were they solved?
- What are the constraints: contracts, licences, compliance duties, skills, hardware, ISP?

**Yourself**

- Whom do I believe, and what can I verify myself?
- Which statements conflict, and who benefits from each version?
- What is in the room that nobody mentioned (a person, a system, a deadline)?

## What to think about

- **Conflicting needs are normal.** In Case 01 the director wants low cost, the IT administrator
  wants simplicity, HR wants privacy and staff want convenience. A design that satisfies only the
  loudest voice fails later. Your job is to make the conflicts visible, not to hide them.
- **Fear is data.** A stakeholder who fears losing control of "their" server will not adopt a
  design that hides it. Ask what control they need and design that in.
- **Nobody owns the current system** is a finding, not an inconvenience. It means decisions were
  made ad hoc and undocumented dependencies exist.
- **Observation beats interviews.** Look at the real network, the real backup log, the real
  firewall rules. People describe the system they intended, not the one they have.
- **Scope the discovery itself.** It ends when the as-is is confirmed, not when you run out of
  curiosity. Park deeper questions in the assumptions log.
- **Treat access as a dependency.** If the client cannot give you read access to the inventory
  within two weeks, that is a schedule risk for the whole project.

**Typical red flags**

| Red flag | What to do |
|----------|------------|
| Nobody owns the current system | Name an owner as an exit-gate condition |
| Undocumented dependencies | Add a dependency discovery task before design |
| Key stakeholders unavailable | Escalate to the sponsor and move the date, not the quality |
| Everyone describes the problem differently | Run a short workshop to agree the problem statement |
| "It just works, do not touch it" | Find out what happens when it does not |

## Documents produced

| Document | Template | Case 01 |
|----------|----------|---------|
| Discovery plan and questionnaire | [questionnaire](templates/discovery-questionnaire.md) | [Plan and questionnaire](../case-01-example-corp/00-pitch-discovery/03-discovery-plan-and-questionnaire.md) |
| Stakeholder map and interview notes | [stakeholder map](templates/stakeholder-map.md) | [Stakeholders and interviews](../case-01-example-corp/00-pitch-discovery/04-stakeholders-and-interviews.md) |
| As-is assessment with findings | — | [As-is assessment](../case-01-example-corp/00-pitch-discovery/05-as-is-assessment.md) |
| Assumptions log | — | Section 4 of the as-is assessment; becomes [requirements §7](../case-01-example-corp/01-requirements/requirements.md#7-assumptions) |
| First risk register | [risk register](templates/risk-register-template.md) | Grows into the [risk register](../case-01-example-corp/05-proposal-delivery/risk-register.md) |

## Exit gate

| Criterion | Signed off by |
|-----------|---------------|
| The as-is assessment is **confirmed by the client** (read, corrected, accepted) | Sponsor or IT owner |
| Every stakeholder group was heard, or the gap is recorded as a risk | Architect |
| Every assumption has an owner and a validation method | Architect |
| The current system has a named owner | Sponsor |

## Common mistakes

- **Interviewing everyone together.** People do not say "I do not trust the IT administrator"
  in front of the IT administrator.
- **Taking the first answer** as the whole answer. Ask "what else?" and "can you show me?".
- **Documenting what should be instead of what is.** The as-is is a photograph, not a plan.
- **Letting discovery become design.** If you are choosing products in week one, you stopped
  listening.
- **Not writing down what you could not verify.** Unlogged assumptions become surprises in
  stage 6.

## Stop and think

> **Stop and think — "the backups work, do not worry"**
>
> The IT administrator says backups run every night to a USB disk and "they work". The disk sits
> next to the server. What do you do with that statement during discovery, and what would you
> record?
>
> <details><summary>Model answer</summary>
>
> Treat it as a **claim**, not a finding. Ask to see the backup log, the job configuration and the
> date of the **last successful restore**. Ask where the disk is when the office burns, floods or
> is burgled; ask whether the backups are encrypted and whether ransomware on the server could
> reach the disk (it is attached). Record: *Backups exist (claimed)*, *restore never tested
> (to verify)*, *single copy in the same room (finding: fails 3-2-1)*, and add an assumption with
> a validation step ("restore one VM from the USB disk in the lab"). Be careful in tone: the
> administrator may be doing their best with no budget.
>
> **Self-check rubric:** (1) You separated claim from evidence. (2) You asked for a restore test.
> (3) You identified location and ransomware exposure. (4) You logged an assumption with a
> validation step. (5) You protected the relationship.
> </details>

> **Stop and think — four interviews, four different problems**
>
> The director says the problem is cost, the IT administrator says it is complexity, the HR
> manager says it is privacy of personnel files, and staff say it is not being able to work from
> home. Can one design satisfy all of them? What do you do with the conflicts?
>
> <details><summary>Model answer</summary>
>
> Not fully; but the conflicts can be **made explicit and prioritised**. Write each need as a
> candidate requirement with an owner, then look for pairs that pull against each other: low cost
> versus resilience, simplicity versus segmentation, convenience versus privacy controls. Bring
> the pairs to the sponsor in a short workshop and ask for a ranking, because only the sponsor can
> trade one interest against another. Record the ranking as the basis of the requirements (stage
> 2) and as decision drivers for the ADRs (stage 3). Some needs are compatible once reframed: SSO
> with MFA gives staff convenience *and* gives HR an audit trail.
>
> **Self-check rubric:** (1) You listed the conflicts as pairs. (2) You did not pick a winner
> yourself. (3) You used the sponsor to prioritise. (4) You found at least one reframing that
> satisfies two parties. (5) You recorded the outcome where later stages can use it.
> </details>

## References

See [references — stage 1](../references.md#stage-1-discovery).
