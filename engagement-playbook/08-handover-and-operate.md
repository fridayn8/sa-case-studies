# Stage 8 — Handover and Operate

| | |
|---|---|
| **Goal** | Make sure the people who will run the system can do it without the architect: they have the documents, the access, the skills and a support model they accept |
| **Typical duration** | 3–4 days effort · 2 weeks calendar **plus 2 weeks of hypercare** *(illustrative, see [timeline and effort](timeline-and-effort.md))* |
| **Inputs** | Live system, as-built design, runbooks drafts, operations team, support model |
| **Case 01 documents** | [Handover checklist](../case-01-example-corp/05-proposal-delivery/handover-checklist.md) · scenarios [3 (incident)](../case-01-example-corp/scenarios/03-incident-app-unreachable.md) and [4 (security incident)](../case-01-example-corp/scenarios/04-security-incident-token-in-git.md) |

## Activities

1. **Involve operations early**, not only at the end: they should have reviewed the runbooks and
   done a restore before the formal handover.
2. **Finish the as-built documentation**: what is actually running (addresses, accounts, tokens,
   backups, schedules), with diagrams that match the build. Update the HLD and LLDs.
3. **Write runbooks** for the situations that will actually happen: restore a VM, rotate a token,
   add a user, patch the hypervisor, a service is down. Use the
   [handbook runbook template](https://github.com/fridayn8/sa-handbook/blob/main/templates/runbook-template.md).
4. **Train** operations and key users: short sessions that include doing the task, not watching.
5. **Define the support model**: who answers, how, during which hours, response targets, how the
   IT partner is called, what is out of hours.
6. **Run hypercare** (two weeks in Case 01): the architect is on call for questions, issues are
   tracked, and the monitoring is watched.
7. **Complete the [handover checklist](templates/handover-checklist-template.md)** and get
   written acceptance from operations.
8. **End hypercare** formally when the exit criteria are met, not when the calendar says so.

## Questions to ask

**Operations**

- If I am unreachable for a week, can you restore a VM, rotate a token and add a user?
- Which of these runbooks would you not trust at 02:00? What is missing?
- What alert would you ignore? Why?
- What do you need from me that you do not have yet (access, contacts, a contract)?

**Business and users**

- What do users need to learn, and in which format will they actually read it?
- How should they report problems, and what will they be told in return?

**Yourself**

- Is anything only in my head? Is every password, key and procedure in a place the client controls?
- Have I shown a **new administrator** the documents and watched them follow one?
- What is the support model if the part-time administrator is ill?

## What to think about

- **The handover test**: can a competent person who did not build the system rebuild a stateless
  component and restore a stateful one using only the documents? If not, the handover is not done.
- **Knowledge in the architect's head** is the most common reason for failed handovers and for
  dependency complaints later. Move every decision to an ADR and every procedure to a runbook.
- **Operations involved too late** will reject, or quietly work around, what they did not help
  shape. Involve them in stages 4 and 6.
- **The support model must match the people.** A model that needs 24/7 on-call fails for a
  company with one part-time administrator (NFR-O3). Agree business-hours support, alerts that
  link to runbooks, and a contract with the IT partner for the rest.
- **Secrets handover**: keys, recovery codes and break-glass credentials are transferred through
  the client's password manager or sealed procedure, never by email, and the architect's own
  access is removed or reduced.
- **Hypercare is about learning**, not about hiding defects. Track every question; repeated ones
  are missing documentation.
- **Maintenance, patching and certificate renewal** are the quiet failures of month 6. Put them on
  a calendar owned by operations.
- **Exit on criteria.** Hypercare ends when there have been no incidents of a given severity for a
  set period, the restore test was done by operations, and open questions have owners.

**Typical red flags**

| Red flag | What to do |
|----------|------------|
| Operations involved too late | Hold a joint walk-through before the handover meeting |
| Knowledge lives in the architect's head | List what only you know; write it down or build a runbook |
| No tested restore by operations | Schedule it inside hypercare |
| Support model unclear | Draw who is called for what, when, and write contact paths |
| Admin credentials still held by the architect | Hand over, rotate, remove |

## Documents produced

| Document | Template | Case 01 |
|----------|----------|---------|
| As-built documentation (updated HLD and LLDs) | [HLD](https://github.com/fridayn8/sa-handbook/blob/main/templates/hld-template.md) · [LLD](https://github.com/fridayn8/sa-handbook/blob/main/templates/lld-template.md) | [Design](../case-01-example-corp/03-design/hld.md) |
| Runbooks | [handbook runbook template](https://github.com/fridayn8/sa-handbook/blob/main/templates/runbook-template.md) | Runbook list in the [handover checklist](../case-01-example-corp/05-proposal-delivery/handover-checklist.md) |
| Handover checklist | [template](templates/handover-checklist-template.md) | [Handover checklist](../case-01-example-corp/05-proposal-delivery/handover-checklist.md) |
| Training notes | — | Training section of the handover checklist |
| Support model | — | Support model section of the handover checklist |

## Exit gate

| Criterion | Signed off by |
|-----------|---------------|
| **Operations accepts** the system, in writing, against the checklist | IT administrator and IT partner |
| **Hypercare has ended** by its exit criteria | Sponsor and architect |
| Secrets and administrative access are transferred; the architect's access is removed or reduced | IT administrator |
| A restore was performed by operations from the documents | IT administrator |

## Common mistakes

- **Handing over a pile of documents** with no walkthrough. Documents do not teach; practice does.
- **Treating the handover as a meeting** instead of a verifiable test.
- **Leaving the architect in the access list** "just in case". It is a standing risk for both sides.
- **No named owner for patching and renewals.**
- **Closing hypercare on a calendar date** when open questions remain.

## Stop and think

> **Stop and think — the handover meeting is tomorrow**
>
> The IT administrator has read the runbooks but never run one. The IT partner is not invited
> because "they only handle emergencies". The architect proposes to hand over tomorrow as planned.
> What would you change?
>
> <details><summary>Model answer</summary>
>
> A runbook that has not been executed by its intended user is untested. Before the meeting,
> schedule one **hands-on session** where the administrator restores a VM and rotates a token from
> the runbooks while you watch and take notes on what is unclear. Invite the **IT partner**: they
> will be called at 02:00 and must know the system's shape, the contacts and the escalation path.
> Turn the meeting from a presentation into an acceptance against the checklist, and give the
> administrator the right to say "not yet" for named items, with dates. If the date cannot move,
> sign an **acceptance with conditions**: a list of open items, owners and a deadline inside
> hypercare.
>
> **Self-check rubric:** (1) You asked for a hands-on run, not a read-through. (2) You included the
> IT partner. (3) You made the meeting an acceptance, with the right to decline items.
> (4) You recorded conditions and dates. (5) You used hypercare to close gaps.
> </details>

## References

See [references — stage 8](../references.md#stage-8-handover-and-operate).
