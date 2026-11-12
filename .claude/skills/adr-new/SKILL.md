---
name: adr-new
description: >
  Create or supersede an Architecture Decision Record (MADR) in sa-case-studies: pick the next
  number, copy the template, fill it in, update the ADR index, and run the checks. Use when asked
  to write, propose, change or supersede an ADR, or to record an architecture decision for the
  Example Corp case. Triggers: ADR, architecture decision, decision record, supersede, "catat
  keputusan".
---

# New ADR

ADRs live in `case-01-example-corp/02-options-decisions/adr/`. They are a **history**: never
rewrite an accepted ADR. To change a decision, write a new ADR that supersedes it.

## 1. Number

- List the folder; the next number is the highest existing number **plus one** (do not reuse a
  gap). `0009` is **reserved** for the off-site backup decision (exercise 3): leave it alone.
- File name: `NNNN-short-kebab-title.md`.

## 2. Write

1. Copy `0000-template.md` to the new file. Do not edit the template.
2. Front matter: `status: proposed`, `date:` today, `deciders:` the maintainer's GitHub handle
   (see `.github/CODEOWNERS`), `consulted`/`informed` as in the existing ADRs.
3. Fill **every** section: Context and Problem Statement, Decision Drivers, at least **two**
   Considered Options with real pros and cons, Decision Outcome (with the reason), Consequences
   (good, bad, neutral) and Confirmation (how it will be verified).
4. Check the drivers against **ADR-0010 (free only)** and **ADR-0011 (open source first)**. If a
   paid or closed option is chosen, say so and why.
5. Fictional data only (`example.com`, `10.10.x.x`); link other ADRs and documents with
   relative links; link other repositories with absolute URLs.

## 3. Index and links

- Add a row to the table in `adr/README.md` (number, title, `Proposed`).
- **Superseding:** the new ADR starts with a line "Supersedes ADR-NNNN" that links to the old
  file (same folder, relative link); in the old
  ADR change only `status:` to `superseded by ADR-MMMM` and its index row to
  `Superseded by MMMM`. Leave the rest of the old text unchanged.
- If the ADR resolves an entry in "Candidate future ADRs", remove or update that row.

## 4. Check and commit

```bash
pre-commit run --all-files
python3 scripts/check-links.py .
```

Branch `docs/adr-NNNN-short-title`; commit `docs(adr): add ADR-NNNN <title>`. Open a pull request
only when the maintainer asks. If the ADR changes something `sa-projects` implements, tell the
maintainer, because that repository links here by URL and may need an update.
