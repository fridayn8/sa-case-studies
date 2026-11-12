# Case 01 — Handover Checklist

| | |
|---|---|
| **Document** | What operations must receive before accepting the system |
| **Stage** | [8 Handover and operate](../../engagement-playbook/08-handover-and-operate.md) |
| **Template** | [Handover checklist template](../../engagement-playbook/templates/handover-checklist-template.md) |
| **Related** | [Scenario 3: incident](../scenarios/03-incident-app-unreachable.md) · [Scenario 4: security incident](../scenarios/04-security-incident-token-in-git.md) |
| **Status** | Completed with two conditions, closed during hypercare |

> Fictional scenario. A check mark means: **demonstrated**, not "document exists".

## 1. Documentation

| # | Item | Evidence | Done |
|---|------|----------|:----:|
| 1.1 | As-built HLD and LLDs match the running system | Walkthrough with the IT administrator | ☑ |
| 1.2 | Diagrams (context, container, topology, flows) match | Compared on site | ☑ |
| 1.3 | ADR log up to date; ADR-0009 still reserved | Reviewed | ☑ |
| 1.4 | Asset inventory: hosts, addresses, accounts (names only), renewal dates | Reviewed | ☑ |
| 1.5 | Risk register transferred to the IT administrator and the managing director | Meeting | ☑ |

## 2. Runbooks (each executed once by the IT administrator from the text alone)

| # | Runbook | Executed by | Notes |
|---|---------|-------------|-------|
| 2.1 | Restore one VM from the backup server | IT administrator | Timed: 1 h 05 min for `wiki01` |
| 2.2 | Restore the firewall VM, or reinstall it and import the configuration | IT administrator | Timed: 1 h 40 min against an RTO of 2 h |
| 2.3 | Replace a failed disk (fast and bulk pools) | IT administrator and IT partner | Disk swap rehearsed in the lab |
| 2.4 | Rotate an API token and update the encrypted secrets | IT administrator | Done in the pipeline |
| 2.5 | Add or remove a user or group in the edge access policy | IT administrator | |
| 2.6 | Patch the hypervisor in the monthly window | IT administrator | Window announced two working days ahead (NFR-A4) |
| 2.7 | Break-glass test and key custody | IT administrator, MD | Quarterly; alert verified |
| 2.8 | Rotate the off-site backup disks | IT administrator | Weekly schedule on a calendar |
| 2.9 | "A web app is unreachable" (scenario 3), including the "tunnel connector disk full" case | IT partner | |
| 2.10 | "A token was committed to Git" (scenario 4) | IT administrator | Tabletop |
| 2.11 | Certificate, domain and licence renewals calendar | IT administrator | |
| 2.12 | Declare and run a disaster recovery | MD, IT administrator, IT partner | Tabletop on the first Friday of hypercare |

## 3. Access, secrets and accounts

| # | Item | Evidence | Done |
|---|------|----------|:----:|
| 3.1 | Break-glass credentials sealed in the client's password manager; two custodians | Photo of the sealed envelope, entry in the manager | ☑ |
| 3.2 | The architect's administrative access removed; read-only account kept until the end of hypercare | Access review | ☑ (read-only until 7 Sep) |
| 3.3 | API tokens inventoried with scope and next rotation date | Inventory | ☑ |
| 3.4 | Encryption keys for backups held by two people, tested recovery | Test | ☑ |
| 3.5 | Local root accounts sealed; named admin accounts with a second factor | Review | ☑ |

## 4. Training

| # | Session | Audience | Length | Format | Done |
|---|---------|----------|-------:|--------|:----:|
| 4.1 | Operating the platform: daily and weekly routine, alerts and runbooks | IT administrator, IT partner | 3 h | Hands-on | ☑ |
| 4.2 | Restore and recovery exercise | IT administrator, IT partner | 2 h | Hands-on | ☑ |
| 4.3 | New login and apps for staff | All staff | 30 min | Demonstration plus one-page guide | ☑ |
| 4.4 | HR data access and audit logs | HR manager | 45 min | Walkthrough | ☑ |

## 5. Support model

| Situation | Who | How | Hours | Target |
|-----------|-----|-----|-------|--------|
| A user cannot log in or reach an app | IT administrator | Chat or phone | Business hours | Same day |
| A service is down (single app) | IT administrator, then IT partner | Alert, then phone | Business hours | Restore within 1 h (NFR-A2) |
| The firewall or the host is down | IT partner (first), IT administrator | Phone | Business hours, evening on request | Restore within the RTO (2 h / 8 business hours) |
| Security incident | IT administrator, MD, IT partner | Phone | Any time, best effort | Contain and rotate within the day |
| Planned change | IT administrator | Change calendar | Saturday windows | Announced two working days ahead (NFR-A4) |
| Architect questions (after hypercare) | Architect | Email | Time and materials | Within three working days |

There is **no 24/7 on-call** (NFR-O3). Alerts go to email and chat; each alert links to a runbook (NFR-O4).

## 6. Hypercare exit criteria

| # | Criterion | Met? |
|---|-----------|:----:|
| 6.1 | Two weeks without a high-severity incident | ☑ |
| 6.2 | A restore was performed by operations from the runbooks (items 2.1 and 2.2) | ☑ |
| 6.3 | All open questions have owners and dates | ☑ |
| 6.4 | Monitoring has been watched daily, with no alerts ignored | ☑ |
| 6.5 | The old router stays untouched until the end of hypercare, then is cleaned up with a change request | ☑ |

## 7. Acceptance

| | Name / role | Date | Decision |
|---|-------------|------|----------|
| Operations | IT administrator | 24 Aug 2027 | **Accepted with two conditions** (below) |
| Operations | IT partner | 24 Aug 2027 | Accepted |
| Sponsor | Managing director | 7 Sep 2027 | Hypercare ended |

**Conditions at acceptance (closed during hypercare):**

1. Runbook 2.12 (disaster recovery) to be exercised once with the managing director present.
2. The off-site disk rotation to be tested once by the IT administrator alone.
