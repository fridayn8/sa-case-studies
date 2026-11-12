---
status: accepted
date: 2026-11-11
deciders: [fridayn8]
consulted: []
informed: [IT administrator]
---

# ADR-0012: Use OpenTofu, and build VM templates from Debian cloud images instead of Packer

Supersedes [ADR-0006](0006-iac-terraform-packer-ansible.md).

## Context and Problem Statement

ADR-0006 split Infrastructure as Code between Terraform, Packer and Ansible. Under the
open-source-first rule ([ADR-0011](0011-open-source-first.md)) Terraform and Packer
(BUSL-1.1) should be replaced. We need (a) an open-source provisioning tool for Proxmox,
Cloudflare and Tailscale, and (b) a way to produce VM templates without Packer.

## Decision Drivers

- Open-source licence
- Compatible with existing `.tf` code, providers and the S3/R2 backend (ADR-0008)
- Fewer tools and one hardening path for VMs and LXCs
- Reproducible templates that are easy to refresh monthly

## Considered Options

**Provisioning**

1. Keep Terraform (BUSL-1.1)
2. **OpenTofu** (MPL-2.0, Linux Foundation fork of Terraform)
3. Pulumi (Apache-2.0)

**VM templates**

1. Keep Packer
2. **Official Debian *genericcloud* image → template VM created by OpenTofu → baseline by Ansible**
3. Customise the cloud image offline with `virt-customize` (libguestfs) on the Proxmox host

## Decision Outcome

Chosen options: **OpenTofu** and **Debian cloud image + OpenTofu + Ansible**.

| Layer | Tool | Owns |
|-------|------|------|
| Base image | Debian project (official cloud image) | Minimal, cloud-init enabled OS |
| Template + resources via APIs | **OpenTofu** | Image download, template VM, VMs/LXCs, pools; Cloudflare; Tailscale |
| Inside machines | **Ansible** | `base-hardening` role for **all** guests (VMs and LXCs), apps, OPNsense |
| Policy files | Git + CI action | Tailscale ACL |

- The repository folder stays `terraform/` and files stay `*.tf`: OpenTofu uses the
  Terraform language. "Terraform" in older documents means *the language/workflow*, executed
  with `tofu`.
- **State encryption**: OpenTofu encrypts state and plan files client-side (AES-GCM, key
  derived from a passphrase in SOPS) before they reach R2 — this closes the weakness noted in
  ADR-0008.
- Cloud images ship without `qemu-guest-agent`; VMs start with the agent **disabled** in
  Proxmox until the Ansible baseline installs it (Phase 4), then it is enabled in code.

### Consequences

- 👍 Good, because the IaC toolchain is fully open source.
- 👍 Good, because one tool less (no Packer) and one baseline path for VMs and LXCs.
- 👍 Good, because official cloud images are maintained, small and boot in seconds.
- 👍 Good, because state is encrypted at rest *by us*, not only by the storage provider.
- 👎 Bad, because hardening happens after first boot (short window with an un-hardened VM) —
  acceptable: VMs are on internal VLANs and the cloud image has password login disabled.
- 👎 Bad, because losing the state encryption passphrase makes the state unreadable → store it
  in SOPS **and** the password manager.
- ➖ Neutral, because some community docs/examples show `terraform` commands; they work with `tofu` unchanged in most cases.

### Confirmation

`tofu plan` shows *No changes* after apply; the state object in R2 is not readable JSON
(encrypted); a cloned VM has the hardening baseline after the Ansible run.

## Pros and Cons of the Options

### OpenTofu

- 👍 Good, because MPL-2.0, community governance, drop-in for the Terraform language, state encryption.
- 👎 Bad, because a few newer Terraform-only features may differ.

### Pulumi

- 👍 Good, because general-purpose languages.
- 👎 Bad, because a rewrite of all code; smaller Proxmox ecosystem.

### Packer

- 👍 Good, because fully baked images (hardening before first boot).
- 👎 Bad, because BUSL-1.1; preseed/boot-command builds are slow and fragile.

### virt-customize

- 👍 Good, because bakes packages into the image offline; open source.
- 👎 Bad, because a manual step on the Proxmox host outside the IaC workflow.

## More Information

- OpenTofu state encryption: <https://opentofu.org/docs/language/state/encryption/>
- Debian cloud images: <https://cloud.debian.org/images/cloud/>
- bpg/proxmox: cloning from templates and downloading images — provider documentation
