---
status: accepted
date: 2026-11-11
deciders: [fridayn8]
consulted: []
informed: [IT administrator]
---

# ADR-0007: Encrypt secrets in Git with SOPS and age

## Context and Problem Statement

Infrastructure code needs secrets: Cloudflare and Proxmox API tokens, Tailscale auth keys,
the tunnel token, WireGuard server keys, PBS encryption key. They must never be committed in
plain text (NFR-S5), yet automation must be able to use them. How do we store and distribute
secrets?

## Decision Drivers

- Secrets versioned alongside the code that uses them (reviewable changes, history)
- Works with Terraform, Ansible and CI
- No additional server to run for a small team
- Supports multiple recipients (admins, CI) and key rotation
- Diffs remain readable (which key changed, not what value)

## Considered Options

1. SOPS + age (encrypt values inside YAML/JSON files in Git)
2. Ansible Vault (encrypt whole files or strings)
3. git-crypt (transparent file encryption in Git)
4. External secrets manager (HashiCorp Vault / OpenBao, Infisical, cloud secret managers)
5. Password manager with CLI (1Password, Bitwarden Secrets Manager)

## Decision Outcome

Chosen option: **"SOPS + age"**, because it encrypts only the *values* in structured files
(keys remain readable in diffs), supports multiple recipients, integrates with Terraform
(`carlpett/sops` provider) and Ansible (`community.sops`), and needs no server.

### Rules

- Encrypted files are named `*.sops.yaml`; plain secret files are git-ignored.
- Recipients are listed in `.sops.yaml` (one age public key per admin + one for CI).
- The CI age **private** key is stored as a GitHub Actions secret; admin private keys stay on
  their devices (encrypted disk) with an offline backup.
- Rotation: on admin departure, remove the recipient, run `sops updatekeys`, **and rotate the
  underlying secrets** (old values remain readable in Git history).
- gitleaks pre-commit hook and CI scan block plain-text secrets.

### Consequences

- 👍 Good, because secrets live next to code with full history and review.
- 👍 Good, because no extra infrastructure.
- 👎 Bad, because history keeps old ciphertexts — a leaked private key exposes all past values → rotate secrets, not only keys.
- 👎 Bad, because no dynamic/short-lived secrets or central audit log like Vault.

### Confirmation

Phase 2: a test secret is encrypted, decrypted by CI and by an admin; `gitleaks` passes on the
whole history.

## Pros and Cons of the Options

### SOPS + age (chosen)

- 👍 Good, because value-level encryption, multi-recipient, tool integrations.
- 👎 Bad, because key management is manual.

### Ansible Vault

- 👍 Good, because built into Ansible.
- 👎 Bad, because Ansible-only; whole-file encryption makes diffs unreadable; single shared password.

### git-crypt

- 👍 Good, because transparent once unlocked.
- 👎 Bad, because whole-file binary diffs; easy to accidentally commit unencrypted if `.gitattributes` is wrong; limited rotation.

### External secrets manager

- 👍 Good, because dynamic secrets, leases, audit logs, fine-grained policies.
- 👎 Bad, because another critical service to run (or pay for) — over-engineered for this size.

### Password manager CLI

- 👍 Good, because the company may already use one; good UX for humans.
- 👎 Bad, because less natural for IaC pipelines; depends on vendor availability during automation.

## More Information

- Related: [secrets in troubleshooting](https://github.com/fridayn8/sa-handbook/blob/main/git/13-troubleshooting.md#secrets), [ADR-0006](0006-iac-terraform-packer-ansible.md)
- Implemented in `sa-projects` (phase 2): [secrets management](https://github.com/fridayn8/sa-projects/blob/main/projects/example-corp/docs/secrets-management.md).
- Revisit if: team grows, or dynamic credentials / central audit become requirements.
