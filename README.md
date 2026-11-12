# SA Case Studies

**Learn to think like a Solution Architect.** This repository follows one realistic engagement, from
the first contact with a client to the review after go-live, and shows for every stage what to
think about, which questions to ask, which documents to produce, how long it usually takes and what
commonly goes wrong.

It is about **reasoning**, not only artefacts: every stage has real questions, trade-offs, worked
examples and "Stop and think" boxes where you answer first and read the model answer second.

> **Fictional data only.** The client, *Example Corp*, is a composite with real-world patterns:
> placeholders such as `example.com` and `10.10.x.x`, no real company, person, domain or address.
> **Figures are illustrative.** Durations, prices and results are rules of thumb for teaching, not
> facts and not quotes.

## Where to start

Read in this order:

1. **[Engagement playbook](engagement-playbook/README.md)**: the ten stages at a glance, the stage-gate diagram.
2. **[Case 01: Example Corp](case-01-example-corp/README.md)**: the story, the characters and a map of every document.
3. **The stage files**, one at a time, next to the matching Case 01 documents:
   [0 Pitch](engagement-playbook/00-pitch.md) ·
   [1 Discovery](engagement-playbook/01-discovery.md) ·
   [2 Requirements](engagement-playbook/02-requirements.md) ·
   [3 Options and decisions](engagement-playbook/03-options-and-decisions.md) ·
   [4 Design](engagement-playbook/04-design.md) ·
   [5 Proposal and commercial](engagement-playbook/05-proposal-and-commercial.md) ·
   [6 Build oversight](engagement-playbook/06-build-oversight.md) ·
   [7 Test and go-live](engagement-playbook/07-test-and-go-live.md) ·
   [8 Handover and operate](engagement-playbook/08-handover-and-operate.md) ·
   [9 Review](engagement-playbook/09-review.md)

## I want to…

| I want to… | Open |
|------------|------|
| See how a whole engagement fits together | [Playbook README](engagement-playbook/README.md) |
| Know how long each stage takes and why the calendar is longer than the effort | [Timeline and effort](engagement-playbook/timeline-and-effort.md) |
| See a real set of documents from pitch to lessons learned | [Case 01](case-01-example-corp/README.md) |
| Practise reasoning on a scenario | The "Stop and think" boxes in the stage files, the [scenarios](case-01-example-corp/scenarios/README.md), the [exercises](exercises/design-first-exercises.md) |
| Start my own engagement from a template | [Engagement templates](engagement-playbook/templates/README.md) |
| Read about a decision and its alternatives | [Options analysis](case-01-example-corp/02-options-decisions/options-analysis.md) and the [ADR log](case-01-example-corp/02-options-decisions/adr/README.md) |
| Find books and standards by stage | [References](references.md) |
| Propose a change or see what is planned | [CONTRIBUTING](CONTRIBUTING.md), [BACKLOG](BACKLOG.md) |

## What is in the repository

```text
sa-case-studies/
├── engagement-playbook/        # ten stages, timeline and estimation, 12 templates
├── case-01-example-corp/       # one worked case: pitch to lessons learned
│   ├── 00-pitch-discovery/  01-requirements/  02-options-decisions/ (with adr/)
│   ├── 03-design/  04-security-cost/  05-proposal-delivery/  scenarios/
├── exercises/                  # reasoning exercises on the design documents
├── scripts/check-links.py      # relative link and anchor check
├── references.md  BACKLOG.md  CONTRIBUTING.md  CHANGELOG.md  LICENSE
└── .github/  .pre-commit-config.yaml  .markdownlint.yaml  .editorconfig  .gitignore
```

## Scope and sibling repositories

| This repository | Elsewhere |
|-----------------|-----------|
| The **engagement playbook** (stages 0–9), durations and estimation, Case 01 and its documents, engagement templates, reasoning exercises, references | **Generic reference** (Git, glossary, tools stack, design templates): [`sa-handbook`](https://github.com/fridayn8/sa-handbook) |
| | **Code and infrastructure** for the example (private repository): [`sa-projects`](https://github.com/fridayn8/sa-projects) |

Links to other repositories are absolute URLs; they may not resolve for readers without access to
a private repository.

## Quality checks

Run these before every commit (the same checks are in [`.pre-commit-config.yaml`](.pre-commit-config.yaml)):

```bash
pip install pre-commit && pre-commit install && pre-commit install --hook-type commit-msg
pre-commit run --all-files          # markdownlint, gitleaks, hygiene, link and anchor check
python3 scripts/check-links.py .    # relative links and #anchors resolve
```

Every Mermaid diagram must render (check with `@mermaid-js/mermaid-cli` or the GitHub preview).

## Licence

[MIT](LICENSE). If you reuse the material, keep the "illustrative and fictional" labels: they are
part of the teaching.
