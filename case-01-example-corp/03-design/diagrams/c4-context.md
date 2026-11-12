# C4 Level 1 — System Context

**Question answered:** *Who uses the platform, and which external systems does it depend on?*
**Audience:** everyone, including management.

```mermaid
flowchart TB
  staff["👤 Staff<br/><i>25 employees, office + home</i>"]
  hr["👤 HR staff<br/><i>manage personal data</i>"]
  admin["👤 IT administrators<br/><i>operate the platform</i>"]

  platform["🏢 Example Corp Office Platform<br/><i>Proxmox, OPNsense, internal apps,<br/>backup, monitoring</i>"]

  idp["Identity provider<br/><i>SSO + MFA, groups</i>"]
  cf["Cloudflare<br/><i>DNS, Tunnel, Access, WAF</i>"]
  ts["Tailscale<br/><i>admin mesh VPN, ACLs</i>"]
  gh["GitHub<br/><i>IaC repo, pull requests, Actions</i>"]
  isp["ISP<br/><i>internet uplink</i>"]
  offsite["Off-site backup target"]
  status["External status page"]

  staff -->|"uses files, wiki<br/>(HTTPS via Cloudflare)"| platform
  hr -->|"uses HR app"| platform
  admin -->|"manages<br/>(Tailscale / break-glass)"| platform
  admin -->|"changes infra via PRs"| gh

  platform -->|"publishes apps via Tunnel"| cf
  platform -->|"subnet router"| ts
  platform -->|"runner pulls jobs"| gh
  platform -->|"internet access"| isp
  platform -->|"replicates backups"| offsite
  platform -->|"reports health"| status
  cf -->|"authenticates users"| idp
  ts -->|"authenticates admins"| idp

  classDef person fill:#08427b,color:#fff,stroke:#052e56
  classDef system fill:#1168bd,color:#fff,stroke:#0b4884
  classDef external fill:#999,color:#fff,stroke:#6b6b6b
  class staff,hr,admin person
  class platform system
  class idp,cf,ts,gh,isp,offsite,status external
```

| Element | Type | Description |
|---------|------|-------------|
| Staff, HR staff, IT administrators | People | See [requirements §3](../../01-requirements/requirements.md#3-stakeholders-and-raci) |
| Example Corp Office Platform | **The system in scope** | Everything on `pve01` and `pbs01` |
| Identity provider | External SaaS | Source of truth for users, groups and MFA |
| Cloudflare | External SaaS | Public DNS, Tunnel, Access, WAF |
| Tailscale | External SaaS | Coordination server for the admin mesh VPN |
| GitHub | External SaaS | Source of truth for infrastructure code |
| ISP | External | Single internet uplink (HLD risk R-3) |
| Off-site backup target | External | Third backup copy |
| External status page | External SaaS | Outage communication independent of the office |

Next zoom level: [C4 container](c4-container.md).
