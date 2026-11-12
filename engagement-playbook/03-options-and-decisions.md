# Stage 3 — Options and Decisions

| | |
|---|---|
| **Goal** | Compare real options against the requirements with explicit criteria, test the riskiest assumption cheaply, and record each decision so that it can be understood and challenged later |
| **Typical duration** | 3–6 days effort · 2–3 weeks calendar *(illustrative, see [timeline and effort](timeline-and-effort.md))* |
| **Inputs** | Signed requirements baseline, constraints, assumptions log, stakeholder priorities |
| **Case 01 documents** | [Options analysis](../case-01-example-corp/02-options-decisions/options-analysis.md) · [ADR log](../case-01-example-corp/02-options-decisions/adr/README.md) |

## Activities

1. **Build a long list** of options for each significant decision, including *do nothing* and
   *buy it as a service*. Do not filter yet.
2. **Pick criteria from the requirements**, not from taste: cost (build and run), security,
   availability, operability by the people who will run it, fit with constraints, exit cost.
3. **Weight the criteria** with the sponsor. The weights are a business decision, not a technical
   one.
4. **Shortlist** to two to four options by removing those that break a constraint (a "knock-out"
   criterion such as the free-only policy).
5. **Score the shortlist** in a [decision matrix](templates/options-decision-matrix.md) and write
   the reasoning next to the numbers.
6. **Find the riskiest assumption** behind the leading option and test it with the smallest
   possible **proof of concept (PoC)**: one app behind the tunnel, one VLAN, one restore.
7. **Record each decision** as an ADR (context, drivers, options, outcome, consequences, how we
   will confirm it) using the [handbook ADR template](https://github.com/fridayn8/sa-handbook/blob/main/templates/adr-template.md).
8. **Walk the sponsor through** the direction and get agreement before the design starts.

## Questions to ask

**Client and stakeholders**

- Which criterion matters most if two options conflict: cost, security, simplicity, independence
  from a vendor?
- What is your appetite for a service you do not control (a SaaS) versus something you run?
- Who will operate each option on a bad day? Do they have the skills, or can they get them?
- What is the cost of leaving this choice in three years?

**Yourself**

- Did I include an option I dislike, and did I describe it fairly?
- Which assumption, if wrong, flips the decision? Can a PoC test it in a day?
- Am I scoring options, or justifying a choice I already made?
- What does each option cost to **run**, not only to build?

## What to think about

- **Options are real or they are theatre.** A comparison where three options are strawmen is a
  decision made in advance. If you cannot write a fair pro for each option, you do not understand
  it yet.
- **Weights before scores.** If you agree the weights *before* scoring, the matrix protects you from
  your own preference. If you tune weights afterwards to get the answer you want, you have written
  a decoration.
- **Run cost beats build cost.** In Case 01 about two thirds of the five-year cost is people time.
  An option that saves hardware but needs weekly manual work for a part-time administrator is
  expensive. Add skills and operating effort as criteria.
- **Knock-out criteria** (a hard constraint such as free-only tooling or no inbound ports) shorten
  the list honestly. Use them; do not score an option that cannot be accepted.
- **Pet technology** is the most common bias, yours and the client's. Make it visible: "the
  administrator likes X" is a legitimate input, as a weighted criterion, not as a veto.
- **Reversibility.** Prefer the choice that is cheap to change later when you are unsure, and
  spend design effort on the choices that are expensive to undo (hypervisor, identity, network
  layout).
- **A PoC answers one question.** "Do our three apps work behind the tunnel with 200 MB uploads?"
  is a PoC. "Let us build a prototype" is a project. Time-box it and write the result down,
  including when it failed.
- **ADRs are a conversation with a future reader** (including you in a year). Write the
  *consequences* honestly, bad ones included, and the way you will confirm the decision.

**Typical red flags**

| Red flag | What to do |
|----------|------------|
| Only one option on the table | Add *do nothing*, *buy a service* and the client's own idea |
| Pet technology | Weight "team skills" explicitly; show the cost of the preference |
| Run cost ignored | Add a five-year cost column with people time |
| The decision matrix "confirms" what was already said in stage 0 | Re-run with weights agreed before scoring |
| Decisions only in chat or in your head | Write the ADR now; it takes 30 minutes |

## Documents produced

| Document | Template | Case 01 |
|----------|----------|---------|
| Options analysis (long list → shortlist → matrix) | [decision matrix](templates/options-decision-matrix.md) | [Options analysis](../case-01-example-corp/02-options-decisions/options-analysis.md) |
| Architecture decision records | [handbook ADR template](https://github.com/fridayn8/sa-handbook/blob/main/templates/adr-template.md) | [ADR log](../case-01-example-corp/02-options-decisions/adr/README.md) |
| PoC report (question, set-up, result, what it changes) | — | Section 4 of the [options analysis](../case-01-example-corp/02-options-decisions/options-analysis.md#4-proof-of-concept-the-riskiest-assumption) |

## Exit gate

| Criterion | Signed off by |
|-----------|---------------|
| Every significant decision has an ADR with **at least three options** | Architect |
| The riskiest assumption has been tested, or its risk is accepted in writing | Sponsor |
| The **sponsor agrees with the direction** (not the details yet) | Sponsor |
| Weights were agreed before scoring | Architect and sponsor |

## Common mistakes

- **Choosing the product first** and writing the matrix afterwards.
- **Scoring on a 1–10 scale** without defining what a 3 or an 8 means. Use short anchors
  ("meets / partly meets / does not meet") and a sentence of evidence.
- **Comparing list prices** and ignoring licence changes, support, exit cost and skills. A product
  whose licence terms changed after an acquisition is a real risk you can name.
- **PoC creep**: the PoC becomes the first sprint of the build with no baseline and no rollback.
- **Not recording the rejected options.** The next architect re-opens the same debate.

## Stop and think

> **Stop and think — the weights are doing the deciding**
>
> You score three options for remote access. The totals are 71, 70 and 68. Changing the weight of
> "operational simplicity" from 3 to 4 reverses the ranking. What does that tell you, and what do
> you do?
>
> <details><summary>Model answer</summary>
>
> A margin that small is **noise**: the matrix cannot discriminate, and the result is driven by one
> judgement call. Do not publish the total as if it were an answer. Show the sensitivity ("the
> ranking flips if simplicity matters a little more") and go back to *what is different* between
> the options: which has a risk the others do not? Often the deciding factor is a single
> qualitative difference (for example, one needs an extra open port, or only one has an
> emergency path that does not depend on the identity provider). Ask the sponsor which of the two
> trade-offs they prefer, and record that as the decision driver in the ADR.
>
> **Self-check rubric:** (1) You treated the narrow margin as inconclusive. (2) You ran a
> sensitivity check. (3) You looked for a qualitative differentiator. (4) You asked the sponsor
> instead of choosing. (5) The ADR names the real driver.
> </details>

> **Stop and think — the riskiest assumption**
>
> You lean towards publishing three web apps through a tunnel with SSO at the edge (Case 01,
> ADR-0005). Assumption A-6 says the apps work behind a reverse proxy without special client
> protocols. Design a PoC of at most one day. What question does it answer, what is the pass
> criterion, and what happens if it fails?
>
> <details><summary>Model answer</summary>
>
> **Question:** can each of the three apps be used end to end through the tunnel and the identity
> check, including the heaviest operation (large upload, long-lived connection)? **Set-up:** one
> test hostname, one connector, the real apps in the lab, one test user in the identity provider.
> **Pass criteria:** login with MFA, a 500 MB upload completes, a session stays open for the
> longest realistic task, the app's own authentication still works behind the proxy, and an
> external port scan shows nothing open. **If it fails:** record which app and why, and choose per
> app: keep it behind the tunnel with a limit, move that one app to the admin-style network path,
> or change the option. Either way the **ADR consequence** ("upload size limits and long-lived
> connections must be validated per app") now has evidence behind it.
>
> **Self-check rubric:** (1) One question, not "build a prototype". (2) The test uses the hardest
> case, not the easy one. (3) Pass criteria are measurable. (4) You wrote down what happens on
> failure. (5) The result feeds the ADR.
> </details>

## References

See [references — stage 3](../references.md#stage-3-options-and-decisions).
