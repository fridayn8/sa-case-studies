# Case 01 — Example Corp

One continuous, **fictional but realistic** engagement. A 25-person professional services company
asks a solution architect to "fix remote access", and the engagement runs from the first email to the
review after go-live. Every document the architect produces is here.

> Fictional scenario. Example Corp is a composite with real-world patterns. All names, domains
> (`example.com`) and addresses (`10.10.x.x`) are placeholders. Prices, durations and results are
> **illustrative**.

## The story in one page

| | |
|---|---|
| **Client** | Example Corp: 25 staff, one office, hybrid work (about two days a week at home) |
| **Starting point** | One Proxmox server built ad hoc; flat network; admin pages port-forwarded to the internet; backups on a USB disk beside the server; no documentation |
| **First message** | "We need a VPN. It has to be cheap. A reseller offered a big firewall for about USD 5 000." |
| **Real problems** | Exposed admin interface, flat network, undocumented server, untested single-copy backups, no safe access for staff from home |
| **External deadline** | Cyber-insurance renewal on 1 October 2027 |
| **Solution (Option A)** | Proxmox host with OPNsense VM, six network zones, Cloudflare Tunnel and Access for staff, Tailscale and WireGuard break-glass for administrators, a separate backup server, all in Git |
| **Cost (illustrative)** | About USD 21 800 external spend over the engagement; about USD 40 k over five years including the project; recurring software cost USD 0 |
| **Plan versus result** | Planned go-live 3 July 2027; actual 7 August 2027; effort +10 %; calendar +32 days |

### Characters (roles only)

| Role | What they want | What they fear |
|------|----------------|----------------|
| Managing director (sponsor) | A safe, cheap solution without lock-in | Cost, a ransomware headline |
| IT administrator (part-time) | Something simple they can fix alone | Complexity, being blamed |
| HR manager (data protection role) | Personal data protected and provable | A leak of personnel files |
| Staff | Work from home without friction | More steps to log in |
| External IT partner | A supportable, documented platform | Responsibility for a design they did not shape |
| Solution architect | A design that meets the goals and that operations can run | Hidden assumptions, a handover that fails |

## How the stages map to the folders

| Playbook stage | Case 01 folder | Documents |
|----------------|----------------|-----------|
| [0 Pitch](../engagement-playbook/00-pitch.md) | [`00-pitch-discovery/`](00-pitch-discovery/01-first-contact.md) | [First contact](00-pitch-discovery/01-first-contact.md) · [Pitch](00-pitch-discovery/02-pitch.md) |
| [1 Discovery](../engagement-playbook/01-discovery.md) | [`00-pitch-discovery/`](00-pitch-discovery/03-discovery-plan-and-questionnaire.md) | [Plan and questionnaire](00-pitch-discovery/03-discovery-plan-and-questionnaire.md) · [Stakeholders and interviews](00-pitch-discovery/04-stakeholders-and-interviews.md) · [As-is assessment](00-pitch-discovery/05-as-is-assessment.md) |
| [2 Requirements](../engagement-playbook/02-requirements.md) | [`01-requirements/`](01-requirements/requirements.md) | [Requirements](01-requirements/requirements.md) |
| [3 Options and decisions](../engagement-playbook/03-options-and-decisions.md) | [`02-options-decisions/`](02-options-decisions/options-analysis.md) | [Options analysis](02-options-decisions/options-analysis.md) · [ADR log](02-options-decisions/adr/README.md) |
| [4 Design](../engagement-playbook/04-design.md) | [`03-design/`](03-design/hld.md) and [`04-security-cost/`](04-security-cost/threat-model.md) | [HLD](03-design/hld.md) · [LLD network](03-design/lld-network.md) · [LLD compute](03-design/lld-compute.md) · [LLD access](03-design/lld-access.md) · [Diagrams](03-design/diagrams/c4-context.md) · [Threat model](04-security-cost/threat-model.md) · [Capacity](04-security-cost/capacity-planning.md) · [Cost](04-security-cost/cost-estimate.md) |
| [5 Proposal and commercial](../engagement-playbook/05-proposal-and-commercial.md) | [`05-proposal-delivery/`](05-proposal-delivery/solution-proposal.md) | [Solution proposal](05-proposal-delivery/solution-proposal.md) · [SOW outline](05-proposal-delivery/sow-outline.md) · [Risk register](05-proposal-delivery/risk-register.md) · [Estimate and timeline](05-proposal-delivery/estimate-and-timeline.md) |
| [6 Build oversight](../engagement-playbook/06-build-oversight.md) | [`05-proposal-delivery/`](05-proposal-delivery/change-request-cctv.md) | [CR-001: CCTV](05-proposal-delivery/change-request-cctv.md) |
| [7 Test and go-live](../engagement-playbook/07-test-and-go-live.md) | [`05-proposal-delivery/`](05-proposal-delivery/cutover-plan-outline.md) | [Cutover plan outline](05-proposal-delivery/cutover-plan-outline.md) |
| [8 Handover and operate](../engagement-playbook/08-handover-and-operate.md) | [`05-proposal-delivery/`](05-proposal-delivery/handover-checklist.md) and [`scenarios/`](scenarios/README.md) | [Handover checklist](05-proposal-delivery/handover-checklist.md) · [Scenarios](scenarios/README.md) |
| [9 Review](../engagement-playbook/09-review.md) | [`05-proposal-delivery/`](05-proposal-delivery/lessons-learned.md) | [Lessons learned](05-proposal-delivery/lessons-learned.md) |

## Reading order for the case

1. Skim the story above, then read [first contact](00-pitch-discovery/01-first-contact.md) and notice what is said versus what is meant.
2. Follow the stages in order; after each stage file, open its Case 01 documents.
3. Return to the [requirements](01-requirements/requirements.md) after reading the design: can you trace every requirement to a place in the design?
4. Read the [scenarios](scenarios/README.md) last, as the system in operation.
5. Try the [design-first exercises](../exercises/design-first-exercises.md).

## Consistency rule

The requirements, HLD, ADRs, risk register and estimate must agree. If you find a contradiction,
do not change old documents silently: record it in the pull request, or park it in the
[backlog](../BACKLOG.md).

## Related

- [Engagement playbook](../engagement-playbook/README.md) · [Timeline and effort](../engagement-playbook/timeline-and-effort.md) · [Templates](../engagement-playbook/templates/README.md)
- Implementation as code: [`sa-projects`](https://github.com/fridayn8/sa-projects) (private repository)
