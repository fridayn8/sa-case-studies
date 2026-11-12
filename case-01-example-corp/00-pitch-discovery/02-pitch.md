# Case 01 — Pitch

| | |
|---|---|
| **Document** | One-page pitch, discovery proposal and answers to the five hardest objections |
| **Stage** | [0 Pitch / first contact](../../engagement-playbook/00-pitch.md) |
| **Status** | Sent after [first contact](01-first-contact.md); accepted by the managing director |
| **Next** | [Discovery plan and questionnaire](03-discovery-plan-and-questionnaire.md) |

> Fictional scenario. Figures are illustrative and must be verified before use in a real proposal.

## 1. One-page pitch

**To:** the Managing Director, Example Corp
**From:** the Solution Architect
**Subject:** Safe remote work for Example Corp: what we propose for the next three weeks

### The problem, as we understood it

Staff work from home two days a week but cannot reach internal apps safely. The current workaround
publishes an admin page of the server to the internet. Backups sit on a disk in the same room as the
server. Nobody can say exactly how the server is configured. A cyber-insurance questionnaire is due on
**1 October 2027** and will ask about exactly these things.

### What success looks like

- Staff reach the company apps from home with their normal company login and a second factor.
- No administration page is reachable from the internet.
- A failed disk, a stolen laptop or ransomware causes hours, not days, of disruption.
- Everything is written down, so the company does not depend on one person, including us.

### What happens if nothing is done

The exposure stays, the insurance questionnaire cannot be answered truthfully, and the first
serious incident costs more than the whole project. A rough sketch from the first call: ten hours of
downtime at about USD 500 per hour, plus a ransomware recovery with a 10 % yearly chance of
about USD 30 000, is a yearly expected loss in the order of **USD 8 000**. We will replace these
guesses with your numbers in discovery.

### Our approach

We do not start with a product. We start by finding out what you have, who depends on it and what
each group needs. Then we compare options (including your reseller's firewall, a cloud-hosted
version and a more redundant design) on cost over five years, security and how much work they
create for your IT administrator. Only then do we propose a design.

### The next three weeks: discovery

| | |
|---|---|
| **Scope** | Interviews with four groups, inventory of the server, network and backups, risks, assumptions |
| **Deliverables** | As-is assessment, stakeholder map, assumptions log, first risk register, a recommendation on how to continue |
| **Duration** | Three calendar weeks (about four days of effort) |
| **Fee** | USD 1 600, fixed |
| **We need from you** | Read access to the server and the router; backup logs; 30–60 minutes with each of: the IT administrator, HR manager, one staff representative, the IT partner |
| **Decision at the end** | You decide whether to continue, with a priced proposal for the next phase in front of you |

### Budget

The USD 5 000 you mentioned is the price of hardware alone, and the hardware list is only part
of the cost. At the end of discovery we show **total cost of ownership over five years**
(hardware, electricity, spare parts, and the time your administrator spends operating it)
and compare it with the options. That is the number to decide on.

## 2. The five hardest objections

### 2.1 "Why not just use a SaaS drive?"

**Short answer:** a SaaS drive can be the right answer for *files*; it does not solve the other four
problems.

- The problems reported are: remote access to *several* internal apps (files, wiki, HR), exposed
  admin interfaces, a flat network, an undocumented server and weak backups. A SaaS drive removes
  one of them (files) and leaves the rest.
- It is a **recurring cost per user**. As an illustration, 25 users at USD 10–15 per user per month is
  USD 3 000–4 500 per year, forever, for files alone, before the wiki and the HR application.
- HR data would leave the building. That may be fine with the right agreements; it is a decision for the
  HR manager and the data protection role, not a technical detail.
- **Honest trade-off:** a SaaS file service has less to operate. If the company's policy allows
  recurring subscriptions, this option stays on the table for stage 3 (see the
  [options analysis](../02-options-decisions/options-analysis.md)). Under the current free-only policy
  (ADR-0010 and requirement NFR-C2) it is excluded, and the design keeps the file service
  replaceable.

### 2.2 "Why not a bigger firewall?"

**Short answer:** a firewall is part of the solution; a firewall *alone* leaves the other problems open.

- A good firewall helps with the flat network and with remote access for administrators. It does
  not document the server, does not back anything up, and does not give staff a login to the apps.
- The reseller's box will still have to be **configured**: VLANs, rules, a VPN for 25 people, MFA.
  That work is the same on any firewall, including a free one.
- The design uses a firewall function **as software on the existing server** (OPNsense), which costs
  USD 0 to buy. The price is a real risk we state openly: if that server is down for maintenance, the
  network is down too (HLD risk R-2).
- **Honest trade-off:** a dedicated appliance separates failures cleanly and is a legitimate upgrade
  later. We would add it if the risk of network outages during server maintenance becomes
  unacceptable.

### 2.3 "Who supports open source?"

**Short answer:** you, your IT partner and the community, with documentation we write; there is no single
vendor to phone.

- Proxmox and OPNsense have large communities, public documentation and optional paid support
  subscriptions if the company changes its policy.
- The design is built for **one part-time administrator**: automated updates, alerts that link to a
  runbook, a restore you can rehearse monthly.
- Your IT partner already knows the platform (they recommended us); we propose to include them in
  the support model.
- **Honest trade-off:** in a crisis, the vendor hotline you do not have is a loss. We accept it
  because the alternative (paid support for each product) breaks the budget, and we reduce the
  exposure with tested restores and documentation.

### 2.4 "What if you leave?"

**Short answer:** the design is built so that you do not need us, and we measure that at handover.

- Every decision is written down with its reasons (decision records). Everything that can be
  expressed as code is in a repository you own.
- A **handover test**: your IT administrator rebuilds a stateless component and restores a VM
  from the documents alone, while we watch. We do not hand over until that works.
- Our access to your systems is **removed at handover**. Break-glass credentials are sealed in your
  password manager.
- **Honest trade-off:** a custom design can create dependence on its author. Documentation, tests and a
  clear support model are the only reliable cure.

### 2.5 "Why not cloud?"

**Short answer:** cloud hosting is a serious option that we will price, not dismiss.

- The two things that decide it for this company are **recurring cost** (a hosted server and storage
  for 2 TB of files grows every month) and **where HR data lives**. On-site also keeps access
  working when the internet is down.
- The design already uses cloud services where they are strongest: public DNS, the web edge in
  front of the apps (SSO and protection), the admin VPN coordination and the status page.
- **Honest trade-off:** cloud shifts work from your administrator to a provider, and
  removes the single-host risk. It adds a monthly bill and a dependency on bandwidth. We will include
  it in the long list at stage 3 and show the five-year numbers next to the others.

## 3. Discovery proposal (summary)

| Item | Agreed |
|------|--------|
| Scope | As above; **no design and no purchases** during discovery |
| Duration and fee | Three calendar weeks, USD 1 600 fixed (up to four days) |
| Client contributions | Access, interviews, documents, a named contact for the IT administrator |
| Out of scope | Any change to production systems |
| Result | Go / no-go for a full proposal, in writing |
| Terms | Either side may stop discovery after week 1 and pay only for work done |

## 4. Reading notes

- Each objection has a **short answer**, **evidence** and an **honest trade-off**. A pitch that
  cannot name what is worse about its own proposal is not credible.
- The pitch never promises a price. It gives the sponsor a method for getting a trustworthy number.
- The expected-loss figure is deliberately labelled a rough sketch from the first call: it is an
  argument to start, not a claim.
