---
status: accepted
date: 2026-11-11
deciders: [fridayn8]
consulted: []
informed: []
---

# ADR-0001: Record architecture decisions as ADRs in Git (MADR format)

## Context and Problem Statement

This lab will involve many design decisions — hypervisor, firewall, remote access, ingress,
IaC tooling, secrets handling. Without a record, the reasoning behind each choice is lost,
the same questions get re-debated, and it is impossible to tell whether a decision still
holds when circumstances change. How should we capture architecture decisions?

## Decision Drivers

- Decisions must be **reviewable** in the same workflow as code (pull requests).
- The format must be **lightweight** so it actually gets used.
- History of decisions must be **preserved**, including reversed ones.
- Readable on GitHub without extra tooling.

## Considered Options

1. No formal record (rely on commit messages and memory)
2. A wiki (GitHub Wiki / Confluence / Notion)
3. Architecture Decision Records as Markdown files in the repo, using the MADR template

## Decision Outcome

Chosen option: **"ADRs as Markdown in the repo, using MADR"**, because it is the only option
that keeps decisions versioned next to the code, reviewed through PRs, and readable on GitHub
with zero tooling.

### Rules

- Location: `case-01-example-corp/02-options-decisions/adr/`, file name `NNNN-short-kebab-title.md`, numbers never reused.
- Start from [`0000-template.md`](0000-template.md).
- New ADRs are proposed via PR with `status: proposed`; merged as `accepted` or `rejected`.
- Accepted ADRs are **immutable** except for status/links. To change a decision, write a new
  ADR and mark the old one `superseded by ADR-NNNN`.
- Write an ADR when a decision is hard to reverse, affects several components, or had real
  alternatives. Don't write one for trivial choices.

### Consequences

- 👍 Good, because rationale is preserved and discoverable (`git log -- case-01-example-corp/02-options-decisions/adr/`).
- 👍 Good, because PR review gives a natural place to discuss options.
- 👎 Bad, because writing ADRs takes discipline and time.
- ➖ Neutral, because a docs site (MkDocs) may be added later to make browsing easier.

### Confirmation

The PR template contains the checklist item *"Architecture decision needed? → ADR added/updated"*.

## Pros and Cons of the Options

### No formal record

- 👍 Good, because zero effort.
- 👎 Bad, because reasoning is lost; commit messages are too short for trade-off analysis.

### Wiki

- 👍 Good, because easy for non-developers to edit.
- 👎 Bad, because it is separated from the code, not reviewed through PRs, and drifts out of date.

### ADRs in repo (MADR)

- 👍 Good, because versioned, reviewable, close to code, standard format.
- 👎 Bad, because non-technical stakeholders need GitHub access to read them.

## More Information

- Michael Nygard, *Documenting Architecture Decisions* (2011):
  <https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions>
- MADR: <https://adr.github.io/madr/>
