# Case 01 — First Contact

| | |
|---|---|
| **Document** | First contact notes and lead qualification |
| **Stage** | [0 Pitch / first contact](../../engagement-playbook/00-pitch.md) |
| **Date** | Week 1 of the engagement (Monday 4 January 2027 in the [timeline](../05-proposal-delivery/estimate-and-timeline.md)) |
| **Status** | Done: go for discovery, with conditions |
| **Next** | [Pitch](02-pitch.md) |

> Fictional scenario. Example Corp is a composite with real-world patterns. All names, domains and
> addresses are placeholders.

## 1. The first message

The managing director (MD) of Example Corp writes to the architect after a recommendation from the
company's external IT partner.

> **Subject:** Remote access to our server, can you help?
>
> Hello,
>
> About half of our 25 people now work from home two days a week and they cannot reach our internal
> apps without sending files by email. Our IT administrator set up a port-forward from the office
> router to the admin page of the server, which makes me nervous after reading about a firm that
> was hit by ransomware. We need a VPN. It has to be cheap, I do not want it over-engineered.
>
> A reseller offered a big firewall box for about USD 5 000 and said it would "fix everything". I
> would like your opinion, and I would like it all done before the summer holidays, because our
> cyber-insurance renews in the autumn and the questionnaire asks about these things.
>
> Can we talk this week?

## 2. What is said versus what is meant

| Said | Probably meant | What to find out |
|------|----------------|------------------|
| "We need a VPN" | Staff must reach a few internal apps from home safely | Which apps, which people, which devices. A VPN may be the wrong tool for staff |
| "Port-forward... makes me nervous" | The admin interface is exposed; the MD has a risk feeling and a story | Which ports are open, who knows about them, since when |
| "It has to be cheap" | A fixed number in mind (USD 5 000) based on the reseller's quote | Whether the number is a ceiling, and whether it covers only hardware |
| "Do not over-engineer it" | Fear of cost and complexity, possibly of dependence on a consultant | What "simple" means to the IT administrator who must run it |
| "The reseller's box will fix everything" | The solution is half-chosen by someone with a commission | What the box actually does, and what remains after it |
| "Before the summer holidays" | A wish, not an event | The real fixed date is the **insurance renewal in autumn**; summer is a preference |
| "The questionnaire asks about these things" | There is an external requirement (MFA, exposed admin interfaces) | The actual questions and the renewal date |

## 3. First call (30 minutes) — notes

- **Sponsor:** the MD, who also holds the budget. Decisions about "IT stuff" are normally taken
  with the external IT partner's advice.
- **Problem in the MD's words:** "People cannot work from home and I do not trust the setup."
- **Not mentioned by the MD, mentioned when asked:** backups are on a USB disk in the same room;
  nobody knows exactly how the server is configured; HR keeps personnel files on it.
- **Budget:** "around USD 5 000, I assumed that is what a good firewall costs". Not tested against
  the rest of the work yet.
- **Deadline:** "summer holidays" (about the end of July); insurance renewal on **1 October 2027**.
- **Decision process:** the MD decides; the IT partner and the IT administrator are consulted.
- **What if nothing is done?** The MD: "Then I wait for the ransomware, I suppose." (Said lightly,
  meant seriously.)

## 4. Lead qualification

Applied with the [lead qualification checklist](../../engagement-playbook/templates/lead-qualification-checklist.md).

| Question | Answer | Assessment |
|----------|--------|------------|
| What is the problem and why now? | Remote work is established, admin exposure is a worry, insurance renewal in autumn | ✅ Real, with an external date |
| Who sponsors and holds the budget? | The MD, both | ✅ Named sponsor |
| Who decides? | The MD, advised by the IT partner and the IT administrator | ✅ Clear, but the advisers must be heard |
| Budget range | "Around USD 5 000" | ⚠️ **Blocker until reframed.** The expectation is hardware only; a design with segmentation, backups and documentation is a larger project |
| Deadline | Wish: end of July. Event: 1 October (insurance) | ⚠️ A realistic go-live is in August (see timeline); the event date is achievable |
| What happens if nothing is done? | Continued exposure; insurance questionnaire fails | ✅ Painful enough to fund |
| Is a solution already chosen? | A reseller box is proposed, not bought | ⚠️ Treat as an assumption to test in discovery |
| Are we the right fit? | Small company, open-source-friendly IT administrator, willingness to document | ✅ Good fit |
| Capacity | Part-time architect, shared with other work, 50–70 % of a day | ✅ Possible for a three-week discovery |
| Conflict of interest | None: no reseller or product relationship | ✅ |

## 5. Go / no-go reasoning

**Decision: go for discovery only**, on three conditions:

1. **The budget expectation is tested openly.** The pitch compares total cost over five years of
   the options (including the reseller's box) and the cost of doing nothing, so that the USD 5 000
   figure is replaced by an informed range before any design is promised.
2. **Discovery is time-boxed** to three weeks, with a fixed fee (USD 1 600, four days) and a clear
   list of what the client must provide: interviews, read access to the server and network,
   the backup logs.
3. **All four stakeholder groups are heard**, including the IT administrator and HR, not only the
   MD and the IT partner.

**Why not simply say no?** The sponsor is named, the pain is real, the fit is good and the budget
expectation can be corrected with evidence. A reasoned *no* would be the right answer if the MD
insisted on the reseller's box as a fixed decision, or refused an interview with the IT
administrator.

**Why not say yes to a full project?** Too little is known. The MD's budget and the deadline are
both guesses, and the "problem" is described as a VPN while the underlying issues (exposed admin
interfaces, flat network, undocumented server, one-copy backups) are larger than a VPN.

## 6. Next steps

| Step | Owner | When |
|------|-------|------|
| Send the [one-page pitch](02-pitch.md) with the discovery proposal | Architect | Within two days |
| Ask the reseller for the quote and the technical sheet of the box (to understand what it does) | MD | Before discovery starts |
| Ask the insurer's renewal questionnaire from last year | MD | Before discovery starts |
| Book interviews with the IT administrator, HR manager, a staff representative and the IT partner | IT administrator | Week 2 |

## 7. What this shows

- The MD described a **solution** (a VPN, a big firewall). The problem is risk, access and recovery.
- A **budget** said aloud is a hypothesis. The five-year view and the cost of doing nothing are the
  tools that move it.
- The date had two layers: a wish and an event. Only the event is a constraint.
