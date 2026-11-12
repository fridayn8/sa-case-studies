# Traffic Flows

Sequence diagrams for the main access paths. Each step names the control that protects it.

## 1. Staff opens a web app (Cloudflare Access + Tunnel)

```mermaid
sequenceDiagram
  autonumber
  actor U as Staff (browser)
  participant CF as Cloudflare edge (Access)
  participant IDP as Identity provider
  participant CFD as cloudflared (DMZ)
  participant OPN as OPNsense
  participant APP as files01 (SERVERS)

  Note over CFD,CF: cloudflared keeps outbound connections open (TCP/UDP 7844)
  U->>CF: GET https://files.example.com
  CF-->>U: Redirect to SSO (no valid Access session)
  U->>IDP: Login + MFA
  IDP-->>U: Assertion (user, groups)
  U->>CF: Return with assertion
  CF->>CF: Policy check: group grp-staff? ✅ → issue Access JWT
  CF->>CFD: Forward request over existing tunnel
  CFD->>OPN: HTTPS to 10.10.20.10:443
  OPN->>OPN: Rule R4: DMZ → ALIAS_APPS:443 ✅
  OPN->>APP: Forward
  APP-->>U: Response (via cloudflared and Cloudflare)
```

**What an attacker sees:** only Cloudflare IPs; the office IP is never in DNS; no inbound port.

## 2. Administrator opens the Proxmox UI (Tailscale)

```mermaid
sequenceDiagram
  autonumber
  actor A as Admin laptop (Tailscale client)
  participant TSC as Tailscale coordination
  participant IDP as Identity provider
  participant TS as ts01 subnet router (MGMT)
  participant PVE as pve01 :8006

  A->>TSC: Connect (device approved, key not expired)
  TSC->>IDP: SSO + MFA (on login / re-auth)
  TSC-->>A: Peer list + routes 10.10.10.0/24, 10.10.20.0/24 (per ACL)
  A->>TS: WireGuard-encrypted packet to 10.10.10.10:8006 (direct or via relay)
  TS->>TS: Tailscale ACL check: group:it-admins → 10.10.10.0/24:8006 ✅
  TS->>PVE: SNAT'd traffic (same VLAN, no firewall hop)
  PVE->>PVE: Proxmox login (named user + TOTP)
  PVE-->>A: Proxmox UI
```

## 3. Break-glass access (WireGuard)

```mermaid
sequenceDiagram
  autonumber
  actor A as Admin laptop (WireGuard)
  participant OPN as OPNsense WAN :51820
  participant MON as Monitoring / alerting
  participant PVE as pve01 :8006

  Note over A: Used ONLY when IdP or Tailscale is down
  A->>OPN: WireGuard handshake (key-based)
  OPN->>MON: Log: break-glass peer handshake
  MON-->>MON: Alert "break-glass used" → incident record
  A->>OPN: Traffic to 10.10.10.10:8006
  OPN->>OPN: Rule R11: WG-BREAKGLASS → MGMT:8006 ✅
  OPN->>PVE: Forward
  PVE->>PVE: Login with local account (sealed credentials)
```

## 4. Infrastructure change through CI (GitOps)

```mermaid
sequenceDiagram
  autonumber
  actor D as Engineer
  participant GH as GitHub (repo + Actions)
  participant HR as GitHub-hosted runner
  participant SR as runner01 (self-hosted, MGMT)
  participant PVE as Proxmox API
  participant CFA as Cloudflare API

  D->>GH: Push branch, open PR
  GH->>HR: Lint, gitleaks, tflint, Checkov
  HR-->>GH: Checks ✅
  GH->>SR: Job: tofu plan (runner polls GitHub, outbound only)
  SR->>PVE: Read state via API token
  SR->>CFA: Read state via scoped token
  SR-->>GH: Plan posted as PR comment
  D->>GH: Review plan, squash merge
  GH->>SR: Job: tofu apply (lab after merge, prod only via manual dispatch)
  SR->>PVE: Create/update guests
  SR->>CFA: Update DNS / Tunnel / Access
  SR-->>GH: Apply result → audit trail
```

## 5. Name resolution inside the office

```mermaid
sequenceDiagram
  autonumber
  participant C as Staff laptop (VLAN 40)
  participant U as OPNsense Unbound (10.10.40.1)
  participant UP as Upstream DNS over TLS

  C->>U: files.int.example.com?
  U-->>C: 10.10.20.10 (host override)
  C->>U: www.github.com?
  U->>UP: Query over TLS (853)
  UP-->>U: Answer (DNSSEC validated)
  U-->>C: Answer (cached)
```
