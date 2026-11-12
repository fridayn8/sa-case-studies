# Case 01 — Stakeholders and Interviews

| | |
|---|---|
| **Document** | Stakeholder map and four interview summaries with conflicting needs |
| **Stage** | [1 Discovery](../../engagement-playbook/01-discovery.md) |
| **Status** | Interview summaries confirmed by each interviewee |
| **Related** | [Discovery plan and questionnaire](03-discovery-plan-and-questionnaire.md) · [Requirements](../01-requirements/requirements.md) |

> Fictional scenario. Roles only; no real people. Quotes are invented for the case.

## 1. Stakeholder map

| Stakeholder | Interest | Influence | Main wish | Main fear | Likely behaviour |
|-------------|----------|-----------|-----------|-----------|------------------|
| Managing director (MD) | High | **High**: sponsor and budget holder | A safe, cheap solution that does not need a consultant forever | Cost, being locked in, a ransomware headline | Will push for the lowest price; trusts the IT partner |
| IT administrator (part-time) | **High** | Medium: runs the system | Something simple they can fix at 8 a.m. alone | Complexity, being blamed, losing control of "their" server | Quietly resists what is not understood |
| HR manager (data protection role) | Medium | Medium: can block the HR app | Personal data under control, an audit trail | A leak of personnel files | Will ask hard questions late if not included early |
| Staff (25), represented by a project manager | High | Low individually, high collectively | Work from home without friction | More steps to log in, slower file access | Will use workarounds if the secure path is annoying |
| External IT partner | Medium | Medium: advises the MD | A supportable platform, a clear contract | Being responsible for something they did not design | Supportive if involved, sceptical if surprised |
| Cyber-insurer (external) | Low | Medium: sets the autumn deadline | Evidence of MFA, no exposed admin interfaces | — | Reads the questionnaire answers literally |

## 2. Interview summaries

Each summary was sent back to the interviewee and corrected before it was used.

### 2.1 Managing director — "Cost and not being held hostage"

- **Says:** "I want my people to work from anywhere and I want to sleep at night. And I do not want a
  system that only one consultant understands."
- **Priorities:** (1) cost, (2) no ransomware disaster, (3) staff happy.
- **Budget:** still "about USD 5 000"; asked what the real number is after the pitch. When shown the
  five-year view the MD said the extra cost is acceptable *if* the insurance renewal is secured and the decision can
  be explained to the board.
- **Concern about the IT partner:** pays them an hourly rate; does not want an open-ended support
  bill.
- **Decision rights:** will decide alone up to a limit; larger sums with the other director.

### 2.2 IT administrator — "Keep it simple, and I must be able to fix it"

- **Says:** "I built this server in my spare time. It works. I do not want a thing I cannot restart
  myself." Also: "Please do not make me learn five new tools."
- **Pain:** every change is manual; there is no time for patching; when the MD asks "is it safe?" the
  administrator cannot give an evidence-based answer.
- **Fears:** a complicated design, being judged for the current setup, being on call all night.
- **Facts volunteered:** the router forwards ports for the Proxmox web UI and the file service; the
  backups go to a USB disk next to the server; one VM named `test2` is of unknown purpose and nobody
  dares to switch it off; a monthly payroll export script runs from the HR VM.
- **What they want:** documentation they can follow, alerts that say what to do, a safe way to try
  changes in a lab.

### 2.3 HR manager (data protection role) — "Personal data must be protected and provable"

- **Says:** "If someone's personnel file leaks, that is my name on the report. I need to know who can
  open what."
- **Pain:** the HR app is reachable by anyone on the office network; the HR manager cannot see who accessed a
  record; HR documents travel by email attachment when staff work from home.
- **Requirements voiced:** only HR staff may open personnel data; access should be logged; backups of
  HR data must be encrypted; deletion rules (retention) must be possible.
- **Concerns about the project:** "Do not move my data to somewhere I cannot name." Not opposed to a
  cloud login in front of the HR app, if it is MFA-protected and the data stays in the office.

### 2.4 Staff representative — "Make it as easy as my banking app"

- **Says:** "I do not want a VPN client I have to start before I can open a document. I want to
  click a link."
- **Pain:** working from home means copying files to a laptop, emailing them, and merging later;
  once they lost a day of changes. The wiki is only reachable in the office.
- **Fears:** more steps to log in; a slower file service at home; being locked out on a day with
  a deadline.
- **Acceptable:** a second factor if it is quick (phone prompt), a bookmark for each app.
- **Devices:** mostly company laptops; some use a personal phone for the second factor.

### 2.5 External IT partner (short call)

- Willing to support whatever platform is documented and monitored; wants to be told early what
  they will be asked to do at 02:00; billing by the hour; skeptical about a design only one person can
  operate; supportive of segmentation and backups; no opinion on the reseller's box beyond "it is a
  fine box".

## 3. Conflicts and how they were handled

| # | Conflict | Between | Why it matters | Resolution (and where it went) |
|---|----------|---------|----------------|--------------------------------|
| C-1 | Lowest cost vs a resilient, documented platform | MD ↔ IT administrator, HR | Cost drives skipped backups and skipped documentation | MD ranked **recovery and exposure above price**; cost kept as a hard recurring-cost constraint (USD 0 software). → NFR-C2, NFR-A2/A3 |
| C-2 | Simplicity vs segmentation and extra security layers | IT administrator ↔ HR, insurer | More zones and rules mean more to maintain | Agreed: **six zones only**, everything as code with a lab, runbooks, one part-time operator as a design constraint. → NFR-S4, NFR-O3 |
| C-3 | Convenience (click a link) vs strong control | Staff ↔ HR, MD | A convenient path may be a weak one | Resolved by reframing: **SSO with MFA at the web edge** is convenient *and* auditable. → FR-01, FR-02, NFR-S2 |
| C-4 | Personal data privacy vs staff access from home | HR ↔ staff | HR app must be reachable from home, but with logs | **Per-app access policy by group**; HR app only for the HR group; audit log retained. → FR-02, NFR-S8 |
| C-5 | Admin independence vs dependence on cloud services | IT administrator ↔ MD | Cloud edge adds third parties | Agreed a **break-glass path** that depends on neither the identity provider nor Tailscale. → FR-04 |
| C-6 | Support by the IT partner vs the administrator's autonomy | IT partner ↔ IT administrator | Who calls whom at night | Defined in the support model (stage 8), runbooks written for both. → NFR-O1, NFR-O4 |

The conflicts were brought to the MD in the final workshop. The sponsor chose the ranking in
C-1; the other conflicts were resolved by design choices that serve both sides.

## 4. What this shows

- Each group described a **different problem**: cost, complexity, privacy, convenience.
- Two of the six conflicts disappeared when reframed (C-3, C-4); the others became explicit
  constraints and ranked priorities.
- The IT administrator's fear is a design requirement: the design must be operable by one person, alone,
  in business hours (NFR-O3). Ignoring it would have meant a build nobody maintains.
- Some information came only because the interview was one-to-one: the unexplained VM, the payroll
  script and the USB disk would not have been mentioned in a group meeting.
