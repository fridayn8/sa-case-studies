# Template — Handover Checklist

**Stage:** [8 Handover and operate](../08-handover-and-operate.md) · **Worked example:** [Case 01 handover checklist](../../case-01-example-corp/05-proposal-delivery/handover-checklist.md)

## How to use

1. A check mark means **demonstrated** (someone did it from the documents), not "the document exists".
2. Involve operations from the beginning; ask them to run each runbook.
3. Transfer secrets and admin access through the client's own password manager, and remove or reduce your own access.
4. Operations may **accept with conditions**; record the conditions and close them inside hypercare.
5. End hypercare on criteria, not on a date.

## Template

### 1. Documentation

| # | Item | Evidence | Done |
|---|------|----------|:----:|
| 1.1 | As-built design matches the running system | | ☐ |
| 1.2 | Decision records up to date | | ☐ |
| 1.3 | Asset inventory and renewal dates | | ☐ |
| 1.4 | Risk register transferred to an owner | | ☐ |

### 2. Runbooks (each executed once by operations from the text)

| # | Runbook | Executed by | Time | Notes |
|---|---------|-------------|-----:|-------|
| 2.1 | Restore a service from backup | | | |
| 2.2 | Restore the most critical component | | | |
| 2.3 | Rotate a credential or token | | | |
| 2.4 | Patch in the maintenance window | | | |
| 2.5 | Respond to the most likely incident | | | |

### 3. Access and secrets

| # | Item | Evidence | Done |
|---|------|----------|:----:|
| 3.1 | Emergency credentials stored with two custodians | | ☐ |
| 3.2 | Provider's administrative access removed or reduced | | ☐ |
| 3.3 | Tokens and keys inventoried with scope and rotation date | | ☐ |

### 4. Training

| # | Session | Audience | Format | Done |
|---|---------|----------|--------|:----:|
| 4.1 | | | | ☐ |

### 5. Support model

| Situation | Who | How | Hours | Target |
|-----------|-----|-----|-------|--------|
| | | | | |

### 6. Hypercare exit criteria

| # | Criterion | Met? |
|---|-----------|:----:|
| 6.1 | A period with no high-severity incident | ☐ |
| 6.2 | A restore performed by operations | ☐ |
| 6.3 | Open questions have owners and dates | ☐ |

### 7. Acceptance

| | Name / role | Date | Decision (accepted / with conditions / declined) |
|---|-------------|------|--------------------------------------------------|
| Operations | | | |
| Sponsor | | | |

## Mini-example

| # | Runbook | Executed by | Time | Notes |
|---|---------|-------------|-----:|-------|
| 2.2 | Restore the firewall VM | IT administrator | 1 h 40 min | Against an RTO of 2 h; one path in the text corrected |
