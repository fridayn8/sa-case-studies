# Stage 4 — Design

| | |
|---|---|
| **Goal** | Describe a solution that meets every requirement, show where each requirement is met, and have the design and its security reviewed before anything is promised or built |
| **Typical duration** | 6–10 days effort · 3–4 weeks calendar *(illustrative, see [timeline and effort](timeline-and-effort.md))* |
| **Inputs** | Requirements baseline, ADRs and agreed direction, PoC results, constraints |
| **Case 01 documents** | [HLD](../case-01-example-corp/03-design/hld.md) · LLDs: [network](../case-01-example-corp/03-design/lld-network.md), [compute](../case-01-example-corp/03-design/lld-compute.md), [access](../case-01-example-corp/03-design/lld-access.md) · [diagrams](../case-01-example-corp/03-design/diagrams/c4-context.md) · [threat model](../case-01-example-corp/04-security-cost/threat-model.md) · [capacity plan](../case-01-example-corp/04-security-cost/capacity-planning.md) · [cost estimate](../case-01-example-corp/04-security-cost/cost-estimate.md) |

## Activities

1. **Write the high-level design (HLD)**: context, components, zones, flows, key decisions,
   how each NFR is met, risks and open issues, transition from the current state. The audience is
   the sponsor, the IT owner and the reviewers.
2. **Draw the diagrams at the right zoom level**: C4 context for the sponsor, container view for
   the IT owner, network and flow diagrams for the builders. Diagrams as code stay in step with
   the text.
3. **Write the low-level designs (LLD)** only as detailed as builders need: IDs, addresses, rule
   matrices, sizes, names. The handbook has [HLD](https://github.com/fridayn8/sa-handbook/blob/main/templates/hld-template.md)
   and [LLD](https://github.com/fridayn8/sa-handbook/blob/main/templates/lld-template.md) templates.
4. **Threat-model each trust boundary** (STRIDE) and feed findings back into the design.
5. **Plan capacity** for the agreed horizon: demand, growth, headroom, comparison with hardware.
6. **Estimate cost** over the life of the system (capex, opex, people), not only the purchase.
7. **Update the traceability table** so every requirement points at the place where it is met.
8. **Review**: a peer or the client's technical owner reads the design against the requirements;
   plan **two review rounds**.

## Questions to ask

**Stakeholders and reviewers**

- Where does each non-functional requirement show up in the design? Show me.
- Which component is a **single point of failure (SPOF)**, and have we accepted that on purpose?
- What does a compromised laptop, a stolen admin password or a vendor outage allow an attacker
  or a failure to reach?
- What happens at month 18 when the disks are 80 % full?
- What does the operator need to know at 02:00 on a bad day?

**Yourself**

- Can every element of the design be traced to a requirement, and every requirement to the
  design? Is anything here that nobody asked for?
- What am I assuming about the operating team?
- Which parts of the design are **decisions** that deserve an ADR, and which are just detail?
- What is out of scope, and have I written it down?

## What to think about

- **Traceability in both directions.** A requirement with no design response is a gap; a design
  element with no requirement is scope creep or a missing requirement.
- **SPOFs, trust boundaries and capacity limits** are the three places where designs fail. List
  them explicitly. In Case 01 the single host is an accepted SPOF (risk R-1), which is why the
  recovery design, the restore tests and the external status page matter more than any redundancy
  feature.
- **Design for the operator.** A part-time administrator cannot run what only the architect
  understands. Runbooks, alerts that link to them, and rebuild-from-code for stateless parts
  *are* part of the design.
- **Security is designed in per boundary, not added as a checklist at the end.** Default-deny
  between zones, SSO and MFA at the edge, least-privilege tokens, encrypted backups with one copy
  the production host cannot delete.
- **Capacity plans are estimates until measured.** State the inputs, the headroom and the review
  date; replace estimates with measurements after go-live.
- **Cost includes people.** If the design reduces hardware cost but adds weekly manual work, the
  five-year number goes up.
- **Name what is out of scope.** Unspoken scope becomes unpaid scope in stage 6.
- **Iterate.** The capacity plan in Case 01 found backup storage tight in year 3; the threat
  model added handshake alerting to the break-glass path. Findings that flow back into the design
  show the review is working.

**Typical red flags**

| Red flag | What to do |
|----------|------------|
| Design not traceable to requirements | Build the table now; list orphans in both directions |
| An unreviewed SPOF | Document it, price the alternative, get an accepted-risk signature |
| A design only the architect understands | Add the runbook and diagram a new administrator would need |
| Security "to be done in build" | Do the STRIDE pass on the design, not on the code |
| No capacity numbers | Compute them from the inputs; flag the unknowns as assumptions |

## Documents produced

| Document | Template | Case 01 |
|----------|----------|---------|
| High-level design | [handbook HLD template](https://github.com/fridayn8/sa-handbook/blob/main/templates/hld-template.md) | [HLD](../case-01-example-corp/03-design/hld.md) |
| Low-level designs | [handbook LLD template](https://github.com/fridayn8/sa-handbook/blob/main/templates/lld-template.md) | [network](../case-01-example-corp/03-design/lld-network.md) · [compute](../case-01-example-corp/03-design/lld-compute.md) · [access](../case-01-example-corp/03-design/lld-access.md) |
| Diagrams (C4, network topology, flows) | — | [diagrams](../case-01-example-corp/03-design/diagrams/c4-context.md) |
| Threat model | [handbook threat model template](https://github.com/fridayn8/sa-handbook/blob/main/templates/threat-model-template.md) | [Threat model](../case-01-example-corp/04-security-cost/threat-model.md) |
| Capacity plan and cost estimate | — | [capacity](../case-01-example-corp/04-security-cost/capacity-planning.md) · [cost](../case-01-example-corp/04-security-cost/cost-estimate.md) |

## Exit gate

| Criterion | Signed off by |
|-----------|---------------|
| **Design review passed**: every requirement traced, SPOFs and trust boundaries listed | Reviewer (peer or client technical owner) |
| **Security review passed**: threat model covers every trust boundary, high risks have an owner | Reviewer and IT owner |
| Capacity plan shows the agreed headroom, or the finding is recorded | Architect |
| Open issues are in the risk register with owners | Architect |

## Common mistakes

- **Over-detailed LLDs written too early**, before the decisions are stable. Detail ages
  quickly; write the level builders need.
- **Diagrams with no legend or no audience.** One diagram per question, labelled with its
  audience.
- **Designing the happy path only.** The design has to say what happens when a disk fails, a
  certificate expires or the identity provider is down.
- **Treating the threat model as a deliverable** rather than a design activity.
- **Skipping the second review round.** The first review finds the obvious; the second finds
  what you got wrong while fixing it.

## Stop and think

> **Stop and think — the single host**
>
> The design runs everything, including the firewall, on one Proxmox host. A reviewer says: "This
> is a single point of failure. Add a second host." How do you respond?
>
> <details><summary>Model answer</summary>
>
> First agree that it **is** a SPOF; do not argue with the fact. Then use the requirements: the
> recovery targets (restore critical services within 8 business hours, 2 hours for the firewall)
> and the budget constraint (one existing server, no recurring cost). Show what a second node and
> shared storage would cost (Case 01: about USD 6–9 k more over five years plus added operating
> complexity for a part-time administrator) against the cost of the downtime avoided (BIA:
> USD 500 per hour). If the numbers do not justify it, record the risk as **accepted** in the HLD
> (R-1) with its mitigations (next-business-day hardware support or spares, monthly restore tests,
> external status page), and name the **trigger** that reopens the decision (budget increase, a
> tighter availability target). Ask the sponsor to accept the risk in writing.
>
> **Self-check rubric:** (1) You agreed it is a SPOF. (2) You compared cost and impact with
> numbers from the requirements. (3) You listed mitigations. (4) You named the trigger to
> revisit. (5) The sponsor, not you, accepts the residual risk.
> </details>

> **Stop and think — the orphan component**
>
> While tracing requirements you find that the design includes a self-hosted log server that no
> requirement mentions. What are the possible explanations, and what do you do?
>
> <details><summary>Model answer</summary>
>
> Three explanations: (1) a **missing requirement** (a real need nobody wrote down, for example
> NFR-S8 "retain firewall and admin logs for 90 days"); (2) **scope creep** from your own enthusiasm;
> (3) a **leftover** from an earlier option that was rejected. Check the requirements and the ADRs.
> If it serves a real need, write the missing requirement and get it approved through change
> control, then keep the component. If not, remove it from the design: every component costs
> build time, run time and attack surface.
>
> **Self-check rubric:** (1) You listed the three explanations. (2) You checked requirements and
> ADRs. (3) You used change control for a new requirement. (4) You counted the cost of keeping it.
> (5) You left no orphan in the final design.
> </details>

## References

See [references — stage 4](../references.md#stage-4-design).
