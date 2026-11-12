# Case 01 — Discovery Plan and Questionnaire

| | |
|---|---|
| **Document** | Discovery plan, interview agenda and the questionnaire that was actually used |
| **Stage** | [1 Discovery](../../engagement-playbook/01-discovery.md) |
| **Status** | Used in weeks 1–3 |
| **Related** | [Stakeholders and interviews](04-stakeholders-and-interviews.md) · [As-is assessment](05-as-is-assessment.md) · [questionnaire template](../../engagement-playbook/templates/discovery-questionnaire.md) |

> Fictional scenario. Names, domains and addresses are placeholders.

## 1. Plan

| Week | Focus | Activities | Output |
|------|-------|------------|--------|
| 1 | Documents and inventory | Request access, collect the inventory, router and server configuration, backup logs, last year's insurance questionnaire; book interviews | Inventory draft, interview calendar |
| 2 | Interviews | Four interview groups plus the IT partner; observe the real network and backup logs | Interview summaries, first conflicts list |
| 3 | As-is and confirmation | Write the as-is assessment and assumptions log; workshop with the MD and IT administrator; correct and confirm | Confirmed as-is, assumptions log, first risk register |

**Effort:** 4 days: about 1 day of inventory work, 1.5 days of interviews and write-up, 1 day of
assessment, 0.5 day of workshop and confirmation.

**Dependencies:** access to the server and router by day 5 (otherwise week 2 slips); the IT
administrator's availability for two sessions of about two hours; the MD for the final workshop.

### Interview plan

| Group | Who | Length | Place | Purpose |
|-------|-----|-------:|-------|---------|
| Managing director | Sponsor | 45 min | Office | Goals, budget, risk appetite, priorities |
| IT administrator | Part-time administrator | 2 × 2 h | Server room and office | The real current system, daily pain, fears about change |
| HR manager (also data protection role) | | 45 min | Office | Personal data, retention, who may see what |
| Staff representative | A project manager who works from home two days a week | 30 min | Video call | What staff really do remotely, what is annoying |
| External IT partner | Support contact | 45 min | Video call | History, contract, what they would be asked to support |

### Agenda for each interview (45 minutes)

1. **Purpose and ground rules** (3 min): confidential, no judgement, summary sent back for correction.
2. **Their day** (10 min): what they do, which systems they touch.
3. **Pain and worries** (12 min): what does not work, what could go wrong.
4. **The current system** (10 min): what exists, who owns it, what depends on it.
5. **Wishes and constraints** (7 min): what a good result looks like, what must not change.
6. **Close** (3 min): who else to ask, what we missed.

## 2. Access and documents requested

| Item | From | Needed by | Status at end of week 1 |
|------|------|-----------|-------------------------|
| Read-only account on the Proxmox host | IT administrator | Day 3 | Granted day 4 |
| Router admin page (screenshot or read-only) | IT administrator | Day 3 | Screenshots on day 3 |
| Backup job log, last 90 days | IT administrator | Day 3 | Received |
| Hardware inventory (server, switch, access points, printers) | IT administrator | Day 5 | Partial: switch and AP models missing |
| ISP contract summary (WAN type, static address, bandwidth) | MD or office manager | Day 5 | Requested; ISP confirmation of public address pending |
| Insurance questionnaire from the previous renewal | MD | Day 5 | Received |
| Reseller quote and datasheet | MD | Day 5 | Received |
| App list with owners and user counts | IT administrator | Day 5 | Received |

## 3. The questionnaire as used

The questions are a guide, not a script. Notes were taken in the right-hand column of the working
copy. Questions marked ★ were asked of everyone.

### 3.1 Business

- **Q1.** ★ What does your day look like, and where does the current IT get in your way?
- **Q2.** ★ What happened last year that you would like never to repeat?
- **Q3.** What does an hour without the file server cost the company? A day?
- **Q4.** Which services must work during office hours? Which could wait until the next day?
- **Q5.** Is there a peak period (month end, audit, tender deadlines) when changes must not happen?
- **Q6.** What would make this project a failure in your eyes?

### 3.2 Users and access

- **Q7.** ★ Which apps do you use, from where, with which device?
- **Q8.** How do you reach them from home today? What do you do when that does not work?
- **Q9.** Do you use personal devices for work? Which?
- **Q10.** Who needs access to personal data (HR files), and who should not?
- **Q11.** Do external people (contractors, the accountant) need access to anything?

### 3.3 The current system (IT administrator)

- **Q12.** What exists: hosts, VMs, apps, switches, access points, router, printers, other devices?
- **Q13.** Who installed each, when, and who changes them? Is there any documentation?
- **Q14.** Which ports are forwarded on the router, since when and why?
- **Q15.** What accounts and passwords exist? Where are they kept? Who has admin rights?
- **Q16.** How are updates applied? When were they last applied?
- **Q17.** What alerts or monitoring exist? Who looks at them?
- **Q18.** Which scripts, cron jobs or manual routines does the company depend on?
- **Q19.** Which incidents happened in the last 12 months, and how were they solved?

### 3.4 Security and data

- **Q20.** What personal data is stored, where, and for how long?
- **Q21.** Are there contractual or legal obligations (retention, location, audits)?
- **Q22.** What does the insurance questionnaire ask about access control, MFA and backups?
- **Q23.** Has the company had a security incident, a phishing event or a lost device?

### 3.5 Network

- **Q24.** Describe the network: how many segments, which devices, which Wi-Fi networks?
- **Q25.** What is the internet connection (type, speed, static IP, backup link)?
- **Q26.** What does a visitor connect to? Where are the printers and other devices?

### 3.6 Backup and recovery

- **Q27.** What is backed up, how often, where is the copy, who checks it?
- **Q28.** When was a restore last tested? What was restored, and how long did it take?
- **Q29.** What happens if the server does not start tomorrow morning?

### 3.7 Contracts, skills and constraints

- **Q30.** What contracts exist (ISP, hardware, software licences, the IT partner)?
- **Q31.** Which skills does the company have in-house and which do they buy?
- **Q32.** What is the IT administrator's time budget? Is there someone who can cover for them?
- **Q33.** What budget and timing constraints exist for this year?

## 4. Ground rules that were agreed

- Interview notes are shared with the interviewee for correction within 24 hours.
- Anything that sounds like a criticism of a person is recorded as a **process finding**.
- Discovery makes **no changes** to production systems; read-only access only.
- Conflicts between stakeholders are recorded and brought to the MD in the final workshop.
