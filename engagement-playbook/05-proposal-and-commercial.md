# Stage 5 — Proposal and Commercial

| | |
|---|---|
| **Goal** | Put in writing exactly what will be delivered, what will not, for what price and in what time, in a form the client can approve and a delivery team can build against |
| **Typical duration** | 2–4 days effort · 1–2 weeks calendar **plus 2–6 weeks of client procurement and legal**, which you do not control *(illustrative, see [timeline and effort](timeline-and-effort.md))* |
| **Inputs** | Reviewed design, cost estimate, risk list, the client's budget range and deadline |
| **Case 01 documents** | [Solution proposal](../case-01-example-corp/05-proposal-delivery/solution-proposal.md) · [SOW outline](../case-01-example-corp/05-proposal-delivery/sow-outline.md) · [Risk register](../case-01-example-corp/05-proposal-delivery/risk-register.md) · [Estimate and timeline](../case-01-example-corp/05-proposal-delivery/estimate-and-timeline.md) |

## Activities

1. **Write the solution proposal** for the decision maker: the problem in their words, the
   solution in plain language, benefits against the business goals, timeline, price range,
   assumptions, exclusions, next steps. Two to four pages.
2. **Write the SOW outline**: scope, deliverables with acceptance criteria, responsibilities
   (RACI), change control, out-of-scope list, assumptions the price depends on.
3. **Estimate** each stage with three points (optimistic, likely, pessimistic), add contingency,
   and state the assumptions (see the [estimation worksheet](templates/estimation-worksheet.md)).
4. **Build the bill of materials (BoM)** with prices, lead times and the source of each price.
5. **Update the risk register** with likelihood, impact, owner and mitigation; keep it consistent
   with the HLD risks.
6. **Agree who does what**: client tasks (access, decisions, test users, change windows) are
   dependencies with dates, not courtesies.
7. **Walk the client through the proposal** before sending it. No surprises in a document that
   will be signed.
8. **Support procurement**: answer questions from finance and legal, keep a list of changes made
   during negotiation, update the estimate if scope shifts.

## Questions to ask

**Client**

- Who signs, and what must they see before they can? Is there a procurement or legal review, and
  how long does it take?
- Is the budget a ceiling, a range or a target? Is the capex/opex split important to your
  accounting?
- Which parts of the work can you do yourselves (racking, testing, user communication)?
- Who is allowed to request changes after signing, and who approves them?
- What is the latest acceptable go-live date, and what fixes it?

**Yourself**

- Would I still sign this price if the pessimistic estimates came true?
- Which assumptions, if wrong, change the price? Are they written in the document?
- What is **not** included that the client probably assumes is?
- What will I do when the first change request arrives?

## What to think about

- **A proposal is a risk allocation.** Every vague phrase moves risk onto whoever is more
  careful about the wording. Make scope, exclusions and acceptance criteria specific.
- **Fixed price needs fixed scope.** If the requirements are not fully known, use fixed price for
  the stages with a stable scope and time-and-materials with a cap for the uncertain parts, or
  phase the contract.
- **Contingency is not padding.** Show it as a separate line (20–30 % at this stage), explain what
  it covers, and re-estimate at every gate.
- **Price range, not a point.** At this stage a range with stated assumptions is honest; a single
  number invites an argument about what is and is not in it.
- **Lead times are on the critical path.** Hardware that takes 2–6 weeks, a client budget cycle
  or a contract review decide the calendar. Order or reserve early, in writing, with a refund
  clause if possible.
- **Exclusions are as important as inclusions.** "Telephony, endpoint management and a second site
  are out of scope" saves an argument six months later.
- **Change control starts here.** Describe how a change is requested, assessed (design, cost,
  time, risk) and approved, before anyone asks for one.
- **Brand and relationship.** A proposal full of hedges reads as lack of confidence; a proposal
  with no hedges reads as a risk. State the assumptions plainly and calmly.

**Typical red flags**

| Red flag | What to do |
|----------|------------|
| Fixed price with vague scope | Tighten scope, move to phases, or cap time and materials |
| Hidden assumptions | List every assumption the price depends on in a table |
| No change process | Add one page: request, impact analysis, approval, who pays |
| The client's work is not listed | Add client responsibilities with dates |
| The deadline cannot be met at the stated scope | Re-scope openly; do not hide the gap in the estimate |

## Documents produced

| Document | Template | Case 01 |
|----------|----------|---------|
| Solution proposal | [template](templates/solution-proposal-template.md) | [Solution proposal](../case-01-example-corp/05-proposal-delivery/solution-proposal.md) |
| SOW outline | [template](templates/sow-outline-template.md) | [SOW outline](../case-01-example-corp/05-proposal-delivery/sow-outline.md) |
| Bill of materials | — | Capex table in the [cost estimate](../case-01-example-corp/04-security-cost/cost-estimate.md#1-capex-one-off-hardware) |
| Risk register | [template](templates/risk-register-template.md) | [Risk register](../case-01-example-corp/05-proposal-delivery/risk-register.md) |
| Estimate and timeline | [worksheet](templates/estimation-worksheet.md) | [Estimate and timeline](../case-01-example-corp/05-proposal-delivery/estimate-and-timeline.md) |

## Exit gate

| Criterion | Signed off by |
|-----------|---------------|
| **SOW or contract signed** | Sponsor (budget holder) and architect or their company |
| Scope, deliverables and acceptance criteria are specific enough to test | Architect and IT owner |
| Client responsibilities and change control are in the document | Sponsor |
| Hardware ordering is authorised, or an explicit decision to wait is recorded | Sponsor |

## Common mistakes

- **Sending the proposal by email and waiting.** Walk through it, answer questions, adjust.
- **Quoting hardware prices from memory.** Prices change; state the date and the source.
- **Hiding contingency** inside line items so that the client sees a padded price. Make it a visible,
  explained line.
- **Promising a go-live date** before the client approval and hardware lead times are on the plan.
- **Giving away the change process.** Without it, every extra request is a favour and every refusal
  is a conflict.

## Stop and think

> **Stop and think — "can you do it for a fixed price?"**
>
> The managing director likes the design and asks for a single fixed price for everything, including
> build. The requirements are signed but the as-is has two unknowns: whether the ISP gives a public
> IPv4 address (A-1), and whether the three apps work behind the tunnel (A-6). What do you
> propose?
>
> <details><summary>Model answer</summary>
>
> A fixed price is possible only where the scope is stable. Offer a **phased structure**: a fixed
> price for the stages that do not depend on the unknowns (design, firewall and network build,
> backups), and a clearly bounded **capped time-and-materials** line (or a fixed price with a stated
> assumption) for the parts that depend on A-1 and A-6. Write the assumptions into the SOW with the
> consequence if false ("if the ISP uses CGNAT, a small relay server is added, estimated cost X,
> change request"). Better still, **resolve the unknowns first**: A-1 is a phone call to the ISP;
> A-6 is the one-day PoC from stage 3. Then offer the fixed price for what is known.
>
> **Self-check rubric:** (1) You tied price type to scope stability. (2) You listed the assumptions
> that affect price. (3) You wrote the consequence if an assumption is false. (4) You considered
> removing the unknown before pricing. (5) You protected both sides.
> </details>

> **Stop and think — the contingency line**
>
> Your three-point estimates sum to 39 architect-days. The client says: "Take out the contingency,
> we trust you." Do you? Why or why not?
>
> <details><summary>Model answer</summary>
>
> Do not remove it silently. Contingency covers **known unknowns** (assumptions not yet validated,
> review rounds, client delays). Removing it does not remove the risk; it moves it to you, and
> it will show up as shortcuts or unpaid hours. Offer alternatives: keep the line and promise to
> release the unused part at the end (a shared-risk model), reduce it **in exchange for fewer
> unknowns** (the client validates A-1 and A-6 before signing), or reduce scope. If the client
> insists on a lower number, state which risks they are now carrying and write them into the
> assumptions.
>
> **Self-check rubric:** (1) You explained what contingency covers. (2) You did not simply agree.
> (3) You offered at least two alternatives. (4) You tied a reduction to a reduced risk.
> (5) You wrote the consequence into the assumptions.
> </details>

## References

See [references — stage 5](../references.md#stage-5-proposal-and-commercial).
