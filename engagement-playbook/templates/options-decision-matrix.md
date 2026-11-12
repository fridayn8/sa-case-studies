# Template — Options Decision Matrix

**Stage:** [3 Options and decisions](../03-options-and-decisions.md) · **Worked example:** [Case 01 options analysis](../../case-01-example-corp/02-options-decisions/options-analysis.md#3-weighted-criteria-and-decision-matrix)

## How to use

1. List the decision and the **requirements it must meet**. Mark **knock-out criteria** (hard constraints) and remove options that fail them. Record why, so that the sponsor can reopen the constraint.
2. Choose three to seven criteria from the requirements. Agree the **weights with the sponsor before scoring**; weights add up to 100.
3. Score each option 0 to 3 with anchors (3 meets fully, 2 meets with caveats, 1 weak, 0 fails). Write one sentence of evidence for every score.
4. Calculate the weighted total, then run a **sensitivity check**: change weights by ±10 and see whether the leader changes.
5. If the margin is small, do not publish the total as the answer. Find the qualitative difference and ask the sponsor.
6. Record the decision as an ADR.

## Template

**Decision:** _______ **Date:** _______ **Sponsor:** _______

### Long list and knock-outs

| # | Option | Short-listed? | Reason / knock-out criterion |
|---|--------|:-------------:|------------------------------|
| 1 | Do nothing (baseline) | | |
| 2 | | | |
| 3 | | | |

### Criteria and weights (agreed **before** scoring)

| Code | Criterion | Weight | Why |
|------|-----------|-------:|-----|
| | | | |
| | **Total** | **100** | |

### Scores (0–3) with evidence

| Criterion | Weight | Option A | Option B | Option C |
|-----------|-------:|:--------:|:--------:|:--------:|
| | | | | |
| **Weighted total** | | | | |

| Criterion | Evidence for A | Evidence for B | Evidence for C |
|-----------|----------------|----------------|----------------|
| | | | |

### Sensitivity

| Variation | A | B | C | Leader |
|-----------|--:|--:|--:|--------|
| Base weights | | | | |
| Cost +10, security −10 | | | | |

### Riskiest assumption and PoC

| Assumption | Question | Pass criteria | Result |
|------------|----------|---------------|--------|
| | | | |

## Mini-example

| Criterion | Weight | A (on-site, free edge) | D (appliance + VPN) |
|-----------|-------:|:----------------------:|:-------------------:|
| Security | 25 | 3 | 2 |
| Five-year cost | 20 | 2 | 3 |
| **Weighted total (max 300)** | | **245** | **215** |

The margin is 30 points. A leads in every plausible weight change, and D only wins if cost outweighs security by eight to one.
