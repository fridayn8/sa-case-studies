---
status: accepted
date: 2026-11-11
deciders: [fridayn8]
consulted: []
informed: [IT administrator]
---

# ADR-0011: Prefer open-source tools (except the owner's chosen platform services)

## Context and Problem Statement

[ADR-0010](0010-free-only-tooling-policy.md) requires every tool to be free. The owner adds a
second rule: **tools should be open source wherever possible**, except the platform products
already used in their daily work — Proxmox VE, OPNsense, WireGuard, Tailscale and Cloudflare —
and GitHub as the code platform. Free-of-charge is not the same as open source (e.g. Terraform
and Packer are free to use but source-available under the Business Source License). Which
tools change?

## Decision Drivers

- OSI-approved licence (or clearly free/open-source software)
- No loss of learning value; skills transferable to industry
- Fewer tools are better when an open-source replacement also simplifies the stack
- Owner-chosen platform services stay as they are

## Considered Options

1. Keep free-but-not-open tools (Terraform, Packer, SaaS status page)
2. Replace them with open-source equivalents where one exists and is mature
3. Go fully open source including the platform services (Headscale instead of Tailscale, own ingress instead of Cloudflare, Forgejo instead of GitHub)

## Decision Outcome

Chosen option: **"Option 2"**. Option 3 contradicts the owner's explicit choice of platform
services; open-source fallbacks for them are documented instead.

### Licence review

| Area | Tool | Licence | Status |
|------|------|---------|--------|
| **Owner-chosen platform** | Proxmox VE / PBS | AGPL-3.0 | ✅ open source |
| | OPNsense | BSD-2-Clause | ✅ open source |
| | WireGuard | GPL-2.0 / MIT | ✅ open source |
| | Tailscale (client) / control plane | BSD-3-Clause / proprietary SaaS | Kept (owner's choice); OSS fallback **Headscale** (BSD-3) |
| | Cloudflare (DNS, Tunnel, Access, R2) / `cloudflared` | Proprietary SaaS / Apache-2.0 | Kept (owner's choice) |
| | GitHub | Proprietary SaaS | Kept (code platform); OSS fallback **Forgejo** (GPL-3.0) |
| **IaC** | Terraform → **OpenTofu** | BUSL-1.1 → **MPL-2.0** | 🔄 **Replaced** ([ADR-0012](0012-opentofu-and-cloud-image-templates.md)) |
| | Packer → **Debian cloud image + OpenTofu + Ansible** | BUSL-1.1 → n/a | 🔄 **Replaced** ([ADR-0012](0012-opentofu-and-cloud-image-templates.md)) |
| | Ansible | GPL-3.0 | ✅ |
| | Providers `bpg/proxmox`, `cloudflare/cloudflare`, `tailscale/tailscale` | MPL-2.0 | ✅ |
| **Secrets** | SOPS / age | MPL-2.0 / BSD-3 | ✅ |
| **Quality gates** | pre-commit, gitleaks, markdownlint | MIT | ✅ |
| | tflint / Checkov / OPA (Conftest) / Spectral | MPL-2.0 / Apache-2.0 / Apache-2.0 / Apache-2.0 | ✅ |
| | release-please | Apache-2.0 | ✅ |
| **Docs & diagrams** | Markdown, MkDocs Material, Mermaid | MIT | ✅ |
| | Structurizr → **C4-PlantUML** (only if Mermaid is not enough) | → MIT | 🔄 Replaced |
| **Monitoring** | Prometheus / Grafana OSS / Uptime Kuma | Apache-2.0 / AGPL-3.0 / MIT | ✅ |
| | SaaS status page → **Upptime** (GitHub Actions + Pages, runs outside the office) | → MIT | 🔄 Replaced |
| **Lab** | VMware Workstation / Hyper-V → **VirtualBox** (base package) | Proprietary → GPL-3.0 | 🔄 Preferred (others remain fallbacks) |
| **OS** | Debian | DFSG free software | ✅ |
| **Example apps** | Nextcloud / BookStack / OrangeHRM | AGPL-3.0 / MIT / GPL-3.0 | ✅ |
| **Identity (lab)** | Login with existing GitHub/Google account; OSS option **Keycloak** (Apache-2.0) for a self-hosted IdP | — | Documented option |

### Consequences

- 👍 Good, because the toolchain is fully open source apart from the owner's chosen services.
- 👍 Good, because dropping Packer removes one tool; VMs and LXCs share one baseline (Ansible).
- 👍 Good, because OpenTofu adds client-side **state encryption** (improves ADR-0008).
- 👎 Bad, because Terraform remains more common in job ads — mitigated: same language and
  workflow; commands differ only in the binary name (`tofu` vs `terraform`).
- ➖ Neutral, because Upptime needs its own public repository for its status page.

### Confirmation

[Tools stack](https://github.com/fridayn8/sa-handbook/blob/main/architecture/tools-stack.md) lists a licence column with no unexplained
non-open-source tools; the validation checklist checks the OpenTofu-specific features.

## More Information

- OpenTofu: <https://opentofu.org/> · Upptime: <https://upptime.js.org/> · Headscale: <https://headscale.net/>
- Related: [ADR-0010](0010-free-only-tooling-policy.md), [ADR-0012](0012-opentofu-and-cloud-image-templates.md)
