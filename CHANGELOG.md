# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/). The repository has no versioned
releases yet.

## [Unreleased]

### Added

- **Engagement playbook**: ten stage files (pitch, discovery, requirements, options and decisions,
  design, proposal and commercial, build oversight, test and go-live, handover and operate, review)
  with questions, trade-offs, exit gates, common mistakes and "Stop and think" boxes; stage-gate
  diagram; `timeline-and-effort.md` with durations, scale factors, three-point estimation, critical
  path and the Case 01 Gantt chart.
- **Engagement templates**: twelve copy-and-fill templates, each with a mini-example.
- **Case 01 (Example Corp)**: first contact, pitch, discovery plan and questionnaire,
  stakeholders and interviews, as-is assessment, options analysis with sensitivity and PoC,
  solution proposal, SOW outline, risk register, estimate and timeline, change request CR-001 (CCTV),
  cutover plan outline, handover checklist and lessons learned.
- `references.md`: books, frameworks and standards by stage (URLs opened on 2026-11-12).
- Repository configuration: pre-commit hooks (hygiene, gitleaks, markdownlint, link check,
  Conventional Commits, `no-commit-to-branch`), `scripts/check-links.py`, issue forms, pull request
  template, CODEOWNERS.
- `README.md`, `CONTRIBUTING.md`, `BACKLOG.md`, `CHANGELOG.md`.

### Changed

Imported from the former combined repository (source commit `cec06a0`) with these edits:

- Requirements, HLD, LLDs, diagrams, threat model, capacity plan and cost estimate moved to
  `case-01-example-corp/`; relative links follow the new layout; links to `sa-handbook` and
  `sa-projects` are absolute URLs.
- "Phase N" wording and "Implemented in" lines now refer to `sa-projects`; the threat model's
  "Phase" column is now "When".
- The ADR log (0000–0012) moved to `case-01-example-corp/02-options-decisions/adr/`; numbers and
  statuses unchanged; ADR-0009 stays reserved; the README explains the "Phase N" wording.
- Section 4 of the old lifecycle document became six scenario files plus a README; the Phase 1
  learning guide became `exercises/design-first-exercises.md`.

### Fixed

- Mermaid parse error in `traffic-flows.md` (a `;` inside a sequence-diagram message).
