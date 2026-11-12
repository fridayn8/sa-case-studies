# Case 01 — Change Request CR-001: CCTV

| | |
|---|---|
| **Document** | A scope-creep example: the request, the impact analysis and the decision |
| **Stage** | [6 Build oversight](../../engagement-playbook/06-build-oversight.md) |
| **Template** | [Change request impact analysis](../../engagement-playbook/templates/change-request-impact-analysis.md) |
| **Related** | [Scenario 2: add a CCTV VLAN](../scenarios/02-normal-change-cctv-vlan.md) · [LLD network §2](../03-design/lld-network.md#2-zones-and-vlans) |
| **Status** | **Decided: deferred** to a normal change after hypercare |

> Fictional scenario. Figures are illustrative.

## 1. The request

| | |
|---|---|
| **ID** | CR-001 |
| **Raised** | Build week 3 |
| **Requested by** | Facility manager, via the IT administrator, in the corridor |
| **Request** | "While the network is being rebuilt, can you also put the new CCTV cameras on it? We are fitting six cameras in the warehouse next month." |
| **Approver** | Managing director (authority for scope and budget) |
| **Is it in the baseline?** | **No.** The requirements mention IoT isolation (FR-06) and the LLD reserves VLAN 70 for a future CCTV zone, but there is no requirement for CCTV itself |

**Classification:** a **change**, not a misunderstanding: nothing in the signed baseline obliges the project
to deliver it.

## 2. Questions asked before assessing

| Question | Answer |
|----------|--------|
| How many cameras, and which recorder? | Six IP cameras and one network video recorder (NVR) bought by the facility manager |
| Who views the footage, and from where? | Facility manager, from the office; occasionally from home |
| How long is footage kept? | 30 days; the HR manager must confirm the legal basis and notice to staff |
| Does the vendor need remote access? | The vendor asked for remote support access to the NVR |
| Is a date fixed? | Cameras are installed next month; the facility manager would like them live at once |

## 3. Impact analysis

| Dimension | Impact |
|-----------|--------|
| **Design** | New zone on VLAN 70 (reserved). Firewall rules: cameras → NVR only; NVR → no internet; viewers → NVR by specific ports; vendor access only through the admin path, time-limited. A new trust boundary in the [threat model](../04-security-cost/threat-model.md). The NVR needs its own storage: 6 cameras × 2 Mbit/s ≈ 130 GB per day, **about 4 TB for 30 days**, which must not use the backup appliance or the file storage pools |
| **Cost** | Architect: 1.5 days (design update, threat model, review) ≈ USD 600. IT administrator: 1 day. Hardware bought by the client: NVR with disks (client's own quote), PoE budget already in the 24-port PoE switch. Capacity plan: no change to `pve01` |
| **Time** | If added to the build: firewall rules must be rehearsed and applied inside the already tight cutover window (stage 7). Estimated **+1 week** on the critical path. If done after hypercare: **0** |
| **Risk** | Cameras and NVRs are a common route for attackers; vendor remote access is a new exposure; footage is personal data (legal basis, notice, retention); more rules in the go-live window raise the chance of a failed Go/No-Go (risk R-10) |

## 4. Options

| Option | Cost and time | Risk | Assessment |
|--------|---------------|------|------------|
| **1. Add to the build now** | +USD 600 architect, +1 week, more changes in the cutover window | Higher: new zone and vendor access while the main change is in progress | Not recommended |
| **2. Defer; do as a normal change after hypercare** | Same cost, no delay to go-live; the zone is already reserved | Lower: the platform is stable and monitored; the change follows the normal process | **Recommended** |
| **3. Reject** | None | Cameras get connected to the staff or IoT network informally | Not recommended: creates the very flat-network problem we are removing |

**Interim measure (no cost):** the cameras and NVR stay **unconnected to the office network** until the change
is done; the facility manager may use the NVR's local display.

## 5. Decision

**Option 2: deferred.** Approved by the managing director on the day the analysis was delivered
(two working days after the request). Conditions:

1. The facility manager provides the NVR model, the vendor's remote-access requirements and the
   retention requirement.
2. The HR manager confirms the legal basis and the staff notice for footage.
3. The change follows the [normal change process](../scenarios/02-normal-change-cctv-vlan.md):
   issue, small design update, review, lab, maintenance window, rollback by reverting the change.
4. The request, analysis and decision are recorded in the SOW change log.

**What this shows:** the answer was not "no". It was "yes, and here is what it costs and what it
delays", and the person with authority chose the date.

## 6. Design deviations seen during the build

The same stage also produced smaller deviations. Each was logged, decided and reflected in the design.

| # | Deviation | Reason | Decision | Decided by |
|---|-----------|--------|----------|------------|
| DV-1 | `mon01` disk raised from 128 GB to 192 GB | The 90-day log retention (NFR-S8) needs more space than estimated | **Accepted**; capacity plan updated, still inside the 70 % target | Architect |
| DV-2 | Builder proposes allowing admin laptops on the staff network to reach the Proxmox page "for the build period" | Management-network access port inconvenient | **Rejected**: it breaks NFR-S3; instead a second access port was configured | Architect |
| DV-3 | The cloudflared containers get 1 GB of RAM instead of 512 MB | Image pulls failed with the lower limit | **Accepted**; LLD compute updated; still inside the capacity plan | Architect |
| DV-4 | Switch port numbering changed from the LLD | Delivered switch has a different uplink layout | **Accepted**; LLD network table updated | IT administrator |
| DV-5 | Break-glass peer list reduced from two devices to one at the start | Second device not yet enrolled | **Accepted with an expiry date** (before go-live); logged in the Go/No-Go | Architect |

**Rule applied:** a deviation is either *accepted and the design updated*, *fixed in the build*, or
*accepted for a limited time with an owner and an expiry*.
