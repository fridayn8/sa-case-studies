# Template — Solution Proposal

**Stage:** [5 Proposal and commercial](../05-proposal-and-commercial.md) · **Worked example:** [Case 01 solution proposal](../../case-01-example-corp/05-proposal-delivery/solution-proposal.md)

## How to use

- The reader is the **decision maker**: write in their words, plain language, two to four pages plus tables.
- Walk the client through it **before** sending it. There should be no surprises in a document that will be signed.
- Every number needs an assumption, and every assumption needs a consequence if it is false.
- Keep the technical detail in linked documents (HLD, ADRs).

## Template

```markdown
# <Project name> — Proposal

To: <decision maker>   From: <architect>   Date: <date>   Version: <n>

## 1. Executive summary
What the client gets, when, and for how much, in five sentences.

## 2. The problem and your goals
| Reported problem | What we found | Goal | How we measure it |
|------------------|---------------|------|-------------------|

## 3. The solution in plain language
Five or six bullets. Link to HLD and ADRs for the technical readers.

## 4. What you get (deliverables and acceptance)
| # | Deliverable | Acceptance (requirement IDs) |
|---|-------------|------------------------------|

## 5. Timeline
| Milestone | Date | Depends on |
|-----------|------|------------|

## 6. Price range
| Item | Amount | Basis |
|------|-------:|-------|
Explain why the range is what it is, and what is not included.

## 7. Assumptions the price depends on
| # | Assumption | If false |
|---|------------|----------|

## 8. Exclusions
Things the client might assume are included, and are not.

## 9. Main risks
| Risk | What we do |
|------|------------|

## 10. Next steps
Who does what by when.

## 11. Acceptance
Name, role, date, signature for client and provider.
```

## Mini-example (section 6, shortened)

| Item | USD |
|------|----:|
| Architect: delivery (billed on days used, capped) | 5 800 expected, **cap 7 250** |
| Hardware | 3 400 |
| **External spend** | **≈ 21 800 expected, up to ≈ 23 250** |

*Why not USD 5 000?* That figure buys one piece of hardware; the recurring risk and cost sit elsewhere.
