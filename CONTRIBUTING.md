# Contributing

This is a personal learning repository that follows a professional team workflow. It teaches
**reasoning**, so quality (real questions, trade-offs, examples) matters more than volume.

## Workflow (GitHub Flow)

1. **Create an issue** with a template (Task or ADR proposal).
2. **Create a branch** from an up-to-date `main`:

   ```bash
   git switch main && git pull
   git switch -c <type>/<short-description>
   ```

3. **Commit** small, focused changes with [Conventional Commits](#commit-messages).
4. **Push and open a pull request** when you are asked or ready; fill in the template and write `Closes #<issue>`.
5. **Self-review the diff**, make sure checks pass, resolve all conversations.
6. **Squash and merge.** The pull request title becomes the commit on `main`.
7. **Clean up:** `git switch main && git pull && git branch -d <branch>`.

`main` is protected by a repository ruleset and by the `no-commit-to-branch` hook: never commit to it directly.

## Branch names

`<type>/<short-kebab-description>`, using the same types as commits:

```text
docs/stage-3-sensitivity-example
fix/gantt-dates
chore/update-pre-commit
```

## Commit messages

[Conventional Commits](https://www.conventionalcommits.org/):

```text
<type>(<scope>): <imperative description, lower-case, no period, ≤ 72 chars>

<optional body: why the change is needed>

<optional footer: Closes #12, BREAKING CHANGE: …>
```

| Type | Use |
|------|-----|
| `docs` | New or changed content (most commits here) |
| `fix` | Correction of a wrong or inconsistent statement |
| `refactor` | Restructure without changing meaning |
| `style` | Formatting |
| `chore` / `ci` / `build` | Tooling, configuration, dependency pins |
| `feat` / `perf` / `test` / `revert` | Rarely used in a documentation repository |

**Scopes:** `case-01`, `playbook`, `adr`, `scenarios`, `exercises`, `templates`, `references`,
`tooling`, `github`.

The `commit-msg` pre-commit hook enforces the format.

## Quality gates (before every commit)

```bash
pip install pre-commit
pre-commit install
pre-commit install --hook-type commit-msg
pre-commit run --all-files
python3 scripts/check-links.py .
```

| Gate | What it checks |
|------|----------------|
| `markdownlint` | Markdown style (configuration in `.markdownlint.yaml`) |
| `check-links` | Every relative link **and** `#anchor` resolves |
| Mermaid | Every ` ```mermaid ` block renders (for example with `@mermaid-js/mermaid-cli`) |
| `gitleaks` | No secrets in the diff |

## Writing rules

- **Language:** documents in English; short sentences; no jargon without a definition.
- **Real questions, real trade-offs.** A stage file that lists generic checklists is not finished. Show the
  question, why it matters and what the answer changes.
- **"Stop and think" boxes:** a realistic situation, two to four questions, a collapsed model answer and a
  self-check rubric of three to five lines.
- **Illustrative figures:** label every duration, price and result as illustrative, and show how to adapt it.
- **Consistency:** requirements, HLD, ADRs, risk register and estimate must agree. Do not silently change old
  documents; record the contradiction in the pull request or in [`BACKLOG.md`](BACKLOG.md).
- **ADRs:** significant decisions need an ADR; copy
  [`0000-template.md`](case-01-example-corp/02-options-decisions/adr/0000-template.md), keep numbers
  and statuses, never reuse a number (ADR-0009 is reserved).
- **References:** open every URL and check the title before adding it to `references.md`.

## Data hygiene: never commit

- Secrets: tokens, passwords, private keys, `.env` files.
- Real company names, domains, IP addresses, hostnames, people or anything from a real employer or client.
- Screenshots or logs from real systems.

Use placeholders (`example.com`, `10.10.x.x`, `pve01`, `opnsense01`). If a secret is committed by mistake,
**rotate it first**, then clean the history.

## Cross-repository links

Use absolute URLs (`https://github.com/fridayn8/<repo>/blob/main/<path>`), never relative paths into
another repository. This repository does not change other repositories.

## New ideas

Park them in [`BACKLOG.md`](BACKLOG.md) under *Parked ideas*. Before starting a new feature, review the
*Planned, not executed* list and choose an item.
