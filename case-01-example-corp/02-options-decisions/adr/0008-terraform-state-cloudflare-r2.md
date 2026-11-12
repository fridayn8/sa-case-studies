---
status: accepted
date: 2026-11-11
deciders: [fridayn8]
consulted: []
informed: [IT administrator]
---

# ADR-0008: Store Terraform state in Cloudflare R2 using the S3 backend

## Context and Problem Statement

Terraform records every resource it manages in a **state** file. State is required for every
`plan`/`apply`, may contain sensitive values (tokens, IPs, generated passwords) and must not
be committed to Git ([ADR-0006](0006-iac-terraform-packer-ansible.md),
[ADR-0007](0007-secrets-sops-age.md)). It must be reachable both from an admin laptop and
from the CI runner, and two runs must not corrupt it. Where should state live?

## Decision Drivers

- Never in Git; encrypted at rest; access limited to admins and CI
- Shared between laptop and CI runner
- Protection against concurrent runs (locking) and accidental deletion (versioning/backups)
- Low or zero cost; no extra server to run
- Survives loss of the office (state is needed to rebuild!)

## Considered Options

1. Local state file on the admin laptop
2. Cloudflare R2 bucket via Terraform's S3-compatible backend
3. HCP Terraform (Terraform Cloud) remote backend
4. Self-hosted S3-compatible storage (e.g. MinIO) or PostgreSQL backend in the office
5. AWS S3 (+ DynamoDB/lockfile)

## Decision Outcome

Chosen option: **"Cloudflare R2 via the S3 backend"**, because we already use Cloudflare, the
free tier easily covers a few MB of state, it is off-site (survives office loss), and access
is controlled with a dedicated, bucket-scoped R2 API token.

### Implementation rules

- One bucket `examplecorp-tfstate`; one key per root module/environment
  (`lab/terraform.tfstate`, `bootstrap/…` stays local — see below).
- Backend endpoint and bucket supplied by **partial configuration** (`backend.hcl`, not committed);
  credentials via environment variables from a SOPS-encrypted file — never in `.tf` files.
- R2 token: **Object Read & Write** on this bucket only.
- **Locking:** Terraform's S3 lockfile (`use_lockfile = true`) where supported by the storage;
  in addition CI uses a `concurrency` group so only one pipeline per environment runs at a time.
- **Recovery:** periodic copy of the state (`terraform state pull`) into the encrypted backup;
  object versioning / lifecycle rules where available.
- The R2 bucket itself is created by a tiny **bootstrap** configuration with *local* state
  (chicken-and-egg problem). That local state holds no secrets; if it is lost, the bucket is
  simply re-imported with `terraform import`.

### Consequences

- 👍 Good, because state is shared, off-site and never in Git.
- 👍 Good, because zero additional infrastructure and no cost at this size.
- 👎 Bad, because the S3 backend is generic — some S3 features (e.g. native locking) depend on
  R2 compatibility and must be verified at implementation; CI concurrency is the safety net.
- 👎 Bad, because Terraform does not encrypt state client-side; we rely on R2 encryption at
  rest + strict token scope. (OpenTofu offers client-side state encryption — revisit if needed.)
- ➖ Neutral, because one more Cloudflare dependency; state can be exported with `terraform state pull` at any time.

### Confirmation

Phase 2: `terraform init` against R2 succeeds from laptop and CI; a test resource
(`terraform_data`) appears in remote state; running two applies at once is blocked
(lock or CI concurrency).

## Pros and Cons of the Options

### Local state

- 👍 Good, because simplest possible.
- 👎 Bad, because not shared with CI, lost with the laptop, easy to commit by mistake.

### Cloudflare R2 (chosen)

- 👍 Good, because off-site, cheap/free, already a vendor, S3-compatible.
- 👎 Bad, because locking support must be verified; generic backend.

### HCP Terraform

- 👍 Good, because built-in locking, history, UI, remote runs, encryption.
- 👎 Bad, because another SaaS account and pricing model; remote runs cannot reach the private
  lab without agents — extra complexity.

### Self-hosted MinIO / PostgreSQL

- 👍 Good, because full control, data stays on-site.
- 👎 Bad, because state would live on the platform it describes — lost in the very disaster
  where it is needed most; another service to run and back up.

### AWS S3

- 👍 Good, because the reference implementation of the S3 backend with native locking.
- 👎 Bad, because a new cloud account, IAM setup and billing just for state.

## More Information

- Terraform S3 backend docs: <https://developer.hashicorp.com/terraform/language/backend/s3>
- Cloudflare R2 S3 compatibility: <https://developers.cloudflare.com/r2/api/s3/api/>
- Amended by [ADR-0012](0012-opentofu-and-cloud-image-templates.md): state and plans are encrypted client-side by OpenTofu; commands use `tofu`.
- Related: [secrets management](https://github.com/fridayn8/sa-projects/blob/main/projects/example-corp/docs/secrets-management.md), [Phase 2 guide](https://github.com/fridayn8/sa-projects/blob/main/projects/example-corp/docs/phase-2-secrets-and-state.md)
