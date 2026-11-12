# Stage 7 — Test and Go-Live

| | |
|---|---|
| **Goal** | Prove with evidence that the solution meets the requirements, agree the point of no return and the way back, and move to production in a controlled window |
| **Typical duration** | 3–5 days effort · 2–3 weeks calendar *(illustrative, see [timeline and effort](timeline-and-effort.md))* |
| **Inputs** | Completed build, requirements and acceptance criteria, verified backups, a maintenance window |
| **Case 01 documents** | [Cutover plan outline](../case-01-example-corp/05-proposal-delivery/cutover-plan-outline.md) · scenarios [5 (disaster)](../case-01-example-corp/scenarios/05-disaster-storage-failure.md) and [6 (major upgrade)](../case-01-example-corp/scenarios/06-major-upgrade-proxmox.md) |

## Activities

1. **Write the test plan** from the requirements: each Must and each NFR gets a test, an expected
   result and an owner. Include functional, integration, performance, **security** and **disaster
   recovery** tests.
2. **Test in the lab or staging first**, then in production before users arrive (smoke tests).
3. **Run user acceptance testing (UAT)** with real users from each group, a pilot group first
   (five users), with a list of tasks they actually do.
4. **Rehearse the cutover** in the lab: every step, timing, owner, checkpoint.
5. **Define rollback and the point of no return**: the last step at which you can go back, and how.
6. **Verify backups before the window**: a restore of the firewall and one data VM, not "the job
   was green".
7. **Hold the Go/No-Go meeting** one hour or one day before, with a checklist and a decision
   owner.
8. **Execute the cutover**, run smoke tests, communicate status, and open hypercare.

## Questions to ask

**Test and UAT**

- What proves each requirement is met? Who runs the test, with what evidence?
- Have we tested the *failure* paths (a disk dies, the identity provider is down, the break-glass
  path)?
- Do the UAT users really do their normal work, or just click through a demo?
- What did performance testing show against the capacity targets?

**Go-live**

- What is the **rollback**, how long does it take, and when does it stop being possible (the point
  of no return)?
- Who is available during the window, including the client and any vendor?
- What is the communication plan for staff before, during and after?
- If something goes wrong at 21:00 on a Saturday, who decides to roll back?

**Yourself**

- Would I be comfortable if the managing director read the test results?
- Am I testing what is easy or what is risky?
- Have I seen a restore work with my own eyes?

## What to think about

- **Test against requirements, not against the build.** The test plan is the traceability table
  turned into actions. If a Must has no test, it is not done.
- **DR is a test, not a document.** The disaster scenario in Case 01 claims a 6-hour recovery
  against an 8-hour target; that figure is a hypothesis until you have restored from backup in a
  rehearsal and timed it.
- **Security testing** includes the negative case: an external port scan finds nothing open, a
  staff laptop cannot reach the management VLAN, the break-glass path raises an alert when used.
- **A rollback is only real if rehearsed.** Know what you revert, in which order, and how long it
  takes. State the **point of no return** in the plan (for example, after the old router's
  configuration has been wiped).
- **Window sizing.** Add time for the unexpected; a cutover planned to the minute has no room
  for the single surprise that always comes.
- **People availability.** UAT users who are on holiday, a vendor with no weekend support or an
  administrator who is also the only tester are all go-live risks.
- **Go/No-Go is a decision, not a ceremony.** The checklist must include conditions that can
  actually say "no": backups verified, rollback rehearsed, support available, staff informed.
- **Communicate early and plainly.** "Wi-Fi will be off from 19:00 to 22:00 on Saturday; Monday you
  will log in with your company account" prevents most support calls.

**Typical red flags**

| Red flag | What to do |
|----------|------------|
| No rollback plan | Do not schedule the window |
| DR never tested | Run a restore rehearsal before go-live and time it |
| UAT users unavailable | Reschedule; do not accept sign-off from a proxy |
| Backups "should be fine" | Restore one VM and the firewall now |
| Pressure to go live to hit a date | Show the residual risk list; ask the sponsor to decide with the facts |

## Documents produced

| Document | Template | Case 01 |
|----------|----------|---------|
| Test plan and results | — | Test matrix in the [cutover plan outline](../case-01-example-corp/05-proposal-delivery/cutover-plan-outline.md#4-checks-before-and-after) |
| UAT sign-off | — | Pilot and sign-off steps in the cutover plan |
| Cutover plan with rollback | [template](templates/cutover-plan-template.md) | [Cutover plan outline](../case-01-example-corp/05-proposal-delivery/cutover-plan-outline.md) |
| Go/No-Go checklist | [template](templates/cutover-plan-template.md) | [Go/No-Go section](../case-01-example-corp/05-proposal-delivery/cutover-plan-outline.md#2-gono-go-checklist) |

## Exit gate

| Criterion | Signed off by |
|-----------|---------------|
| **Go decision** recorded, with the checklist | Sponsor (A), architect and IT owner (C) |
| **Backups verified by restore**, not by job status | IT owner |
| UAT signed by a representative of each user group | Sponsor |
| Rollback rehearsed and the point of no return stated | Architect |

## Common mistakes

- **Treating the backup job status as proof** of recoverability.
- **Going live on Friday afternoon** with nobody available on Saturday.
- **Skipping the pilot** and finding the unusual file share at 08:05 on Monday.
- **Testing only the happy path.** The test of a firewall is the packet that should be dropped.
- **No communication plan.** The first support call tells you the plan was missing.

## Stop and think

> **Stop and think — "the backups ran green"**
>
> The go/no-go meeting is in an hour. The monitoring shows 14 green nightly backup jobs. The
> IT administrator says: "We are good to go." What do you ask for?
>
> <details><summary>Model answer</summary>
>
> **Evidence of restore.** A green job proves that data was written, not that it can be read, is
> complete, decrypts with the key you hold, or restores into a working machine in the time your
> targets require. Ask for: a restore of the **firewall VM** (RTO 2 hours: if it cannot be restored,
> the office stays offline) and of **one data VM** into a lab or a spare location, a time
> measurement, a note on where the encryption key is stored and who has it, and confirmation that
> one copy is not reachable from the production host. If the restore has not been done, the
> checklist answer is **No-Go** (or a deliberately accepted, signed residual risk with a short
> deadline).
>
> **Self-check rubric:** (1) You separated "job green" from "restore works". (2) You asked for the
> firewall restore specifically. (3) You asked about the key. (4) You asked for a timed result.
> (5) You were willing to say No-Go.
> </details>

> **Stop and think — the point of no return**
>
> The cutover plan replaces the old router with the new firewall at 19:30. The old router
> configuration is wiped at 21:00 as the "clean-up step". The window ends at 23:00. Where is
> the point of no return, and does the plan look right?
>
> <details><summary>Model answer</summary>
>
> The point of no return is **21:00**, when the old configuration is erased: after that, rollback
> means rebuilding from backup, hours instead of minutes. The plan is risky because the clean-up
> is inside the window where problems are still likely to appear. Move the wipe **out of the
> window** (days later, after a week of stable operation) and keep the old router powered off but
> intact with its configuration exported. Add checkpoints between 19:30 and 21:00 (internet
> works, VLANs reach the gateway, DNS resolves, the break-glass path answers) and a clear decision
> owner who says "roll back" if a checkpoint fails.
>
> **Self-check rubric:** (1) You identified the irreversible step. (2) You moved it after proof of
> stability. (3) You added checkpoints. (4) You named the decider. (5) You kept the old
> configuration available.
> </details>

## References

See [references — stage 7](../references.md#stage-7-test-and-go-live).
