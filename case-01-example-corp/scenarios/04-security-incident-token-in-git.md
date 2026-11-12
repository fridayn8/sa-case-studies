# Scenario 4 — Security incident: "API token committed to Git"

| | |
|---|---|
| **Kind** | Security incident |
| **Playbook stage** | 8 Handover and operate |
| **Related Case 01 documents** | [threat model](../04-security-cost/threat-model.md) · [ADR-0007](../02-options-decisions/adr/0007-secrets-sops-age.md) |

> Fictional scenario for **Example Corp**. Terms in the right-hand column are explained in the
> [glossary](https://github.com/fridayn8/sa-handbook/blob/main/architecture/glossary.md).

| # | What happens | Terms |
|---|--------------|-------|
| 1 | gitleaks in CI (or GitHub secret scanning) flags a Cloudflare token in a PR | Secret scanning, Shift left |
| 2 | **Immediately revoke** the token in Cloudflare and create a new, narrower one | Secrets management, Rotation, PoLP |
| 3 | Check Cloudflare audit log for misuse during the exposure window | Audit trail, Incident |
| 4 | Remove secret from branch history (unmerged → rebase/amend; merged → `git filter-repo`) | [Git handbook: troubleshooting](https://github.com/fridayn8/sa-handbook/blob/main/git/13-troubleshooting.md) |
| 5 | Postmortem: why did the local pre-commit hook not catch it? | Postmortem, RCA |
| 6 | Move token to SOPS-encrypted file / CI secret; enforce pre-commit | SOPS, Quality gate |

---

[← Scenario 3](03-incident-app-unreachable.md) · [All scenarios](README.md) · [Scenario 5 →](05-disaster-storage-failure.md)
