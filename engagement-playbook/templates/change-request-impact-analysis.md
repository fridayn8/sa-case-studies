# Template — Change Request and Impact Analysis

**Stage:** [6 Build oversight](../06-build-oversight.md) · **Worked example:** [Case 01 CR-001: CCTV](../../case-01-example-corp/05-proposal-delivery/change-request-cctv.md)

> For a generic change request used in operations, see the [handbook template](https://github.com/fridayn8/sa-handbook/blob/main/templates/change-request-template.md). This one is for **scope changes during an engagement**.

## How to use

1. Write down the request in the requester's words. Ask: is it **in the baseline**? If yes, it is not a change.
2. Ask what is actually wanted (how many, who, how long, which constraints).
3. Analyse the four dimensions: **design, cost, time, risk**. Leave none out.
4. Give two or three options, including *defer* and *reject*, and a recommendation.
5. The person with authority decides. Record the decision and the reason either way.
6. Update the baseline, estimate, risk register and design.

## Template

| | |
|---|---|
| **ID** | CR-___ |
| **Raised (date, stage)** | |
| **Requested by** | |
| **Approver** | |
| **Request (their words)** | |
| **In the baseline?** | ☐ Yes (not a change) ☐ No |

### Questions asked and answers

| Question | Answer |
|----------|--------|
| | |

### Impact analysis

| Dimension | Impact |
|-----------|--------|
| **Design** (what changes; which documents, requirements, ADRs) | |
| **Cost** (effort, hardware, running cost) | |
| **Time** (critical path? new dependencies?) | |
| **Risk** (security, privacy, delivery, new vendors) | |

### Options

| Option | Cost and time | Risk | Assessment |
|--------|---------------|------|------------|
| 1. Do now | | | |
| 2. Defer | | | |
| 3. Reject | | | |

### Decision

**Decision:** ☐ Approved ☐ Deferred ☐ Rejected **By:** _______ **Date:** _______

**Reason and conditions:**

**Updates made:** ☐ requirements ☐ design ☐ estimate ☐ risk register ☐ SOW change log

## Mini-example

| Dimension | Impact |
|-----------|--------|
| Design | New zone on VLAN 70; rules: cameras to recorder only; a new trust boundary |
| Cost | Architect 1.5 days (about USD 600); the client buys the recorder |
| Time | +1 week if done in the build; 0 if done after hypercare |
| Risk | Vendor remote access; footage is personal data |

**Decision:** Deferred to a normal change after hypercare, approved by the managing director.
