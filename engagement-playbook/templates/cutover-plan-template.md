# Template — Cutover Plan and Go/No-Go Checklist

**Stage:** [7 Test and go-live](../07-test-and-go-live.md) · **Worked example:** [Case 01 cutover plan](../../case-01-example-corp/05-proposal-delivery/cutover-plan-outline.md)

## How to use

1. Write the plan, then **rehearse it** in the lab and record timings. A plan nobody rehearsed is a hope.
2. Put **checkpoints** between steps, with a clear pass criterion and a decision owner.
3. Define the **rollback** and the **point of no return**. If there is none inside the window, say so; if there is one, move it as late as possible.
4. The **Go/No-Go checklist** must contain rows that can actually say no (backups verified by restore, rollback rehearsed, people available).
5. Leave float in the window (about 25 % of the time).

## Template

**Window:** _______ **Decision owner:** _______ **Cutover lead:** _______ **Architect:** _______

### Scope and dependencies

| In scope | Not in scope | Dependencies |
|----------|--------------|--------------|
| | | |

### Go/No-Go checklist

| # | Check | Blocker? | Evidence | Status |
|---|-------|:--------:|----------|--------|
| 1 | Backups verified **by restore** | Yes | | ☐ |
| 2 | Rollback rehearsed; timing recorded | Yes | | ☐ |
| 3 | Required people available during and after the window | Yes | | ☐ |
| 4 | Users informed | No | | ☐ |

### Steps

| Time | Step | Owner | Checkpoint and pass criterion | Rollback available? |
|------|------|-------|------------------------------|--------------------|
| | | | | |

### Rollback

| Trigger | Procedure | Time needed | Decider |
|---------|-----------|------------:|---------|
| | | | |

**Point of no return:** _______ (state when it happens, or "none inside the window")

### Communication

| When | Audience | Message |
|------|----------|---------|
| | | |

## Mini-example

| Time | Step | Owner | Checkpoint | Rollback available? |
|------|------|-------|------------|--------------------|
| 20:00 | Move the default gateway to the new firewall | IT administrator | CP-2: internet from staff and servers | Yes, re-point to the old router (10 min) |

Point of no return: none inside the window; the old router stays untouched for 14 days.
