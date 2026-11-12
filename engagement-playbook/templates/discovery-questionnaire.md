# Template — Discovery Questionnaire

**Stage:** [1 Discovery](../01-discovery.md) · **Worked example:** [Case 01 questionnaire](../../case-01-example-corp/00-pitch-discovery/03-discovery-plan-and-questionnaire.md#3-the-questionnaire-as-used)

## How to use

- It is a **guide, not a script**. Pick the sections that fit the interviewee; ask "what else?" and "can you show me?".
- Take notes in the right-hand column and send a summary back within 24 hours for correction.
- Mark questions ★ that you ask everybody. Record **claims** and **evidence** separately.
- Remove sections that do not apply; add the questions that your client's situation needs.

## Template

| # | Question | Answer / notes | Evidence seen? | Follow-up |
|---|----------|----------------|:--------------:|-----------|
| **Business** | | | | |
| ★ B1 | What does your day look like, and where does the current system get in your way? | | | |
| ★ B2 | What happened last year that you would like never to repeat? | | | |
| B3 | What does an hour of downtime cost? A day? | | | |
| B4 | Which services must work during office hours; which can wait? | | | |
| B5 | What would make this project a failure in your eyes? | | | |
| **Users and access** | | | | |
| ★ U1 | Which systems do you use, from where, with which device? | | | |
| U2 | How do you work when the system is not available? | | | |
| U3 | Who needs access to sensitive data, and who should not have it? | | | |
| **Current system** | | | | |
| S1 | What exists, who owns each part, who last changed it and why? | | | |
| S2 | What depends on it that nobody wrote down (scripts, spreadsheets, devices)? | | | |
| S3 | How are updates, accounts and secrets handled? | | | |
| S4 | What incidents happened in the last 12 months? | | | |
| **Security and data** | | | | |
| D1 | What personal or sensitive data is stored, where, and for how long? | | | |
| D2 | Which contracts, laws or insurance duties apply? | | | |
| **Backup and recovery** | | | | |
| R1 | What is backed up, where is the copy, who checks it? | | | |
| R2 | When was a restore last tested, and what happened? | | | |
| R3 | What happens if the main system does not start tomorrow? | | | |
| **Contracts, skills and constraints** | | | | |
| C1 | Which contracts exist (ISP, hardware, licences, support partner)? | | | |
| C2 | Which skills exist in-house, and how much time can they spend? | | | |
| C3 | What budget and timing constraints exist? | | | |

## Mini-example

| # | Question | Answer / notes | Evidence seen? | Follow-up |
|---|----------|----------------|:--------------:|-----------|
| R2 | When was a restore last tested? | "We have never needed to." | ✅ log shows no restore | Assumption: restore one VM in the lab |
| S2 | What depends on it that nobody wrote down? | A monthly payroll export script on the HR server | ✅ seen in cron | Add to the dependency list |
