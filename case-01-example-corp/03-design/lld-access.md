# Low-Level Design — Access (Identity, Cloudflare, Tailscale, WireGuard)

| | |
|---|---|
| **Document** | LLD — Access paths for staff and administrators |
| **Version** | 0.1 (draft) |
| **Status** | Proposed |
| **Parent** | [HLD §5](hld.md#5-access-and-traffic-flows) |
| **Implemented in** | `sa-projects` — [example-corp project](https://github.com/fridayn8/sa-projects/tree/main/projects/example-corp) (Tailscale, Cloudflare and WireGuard configuration) |

> Fictional scenario. All names, domains, addresses, IDs and keys are placeholders.

## 1. Access paths overview

| Path | Users | Auth | Reaches | Normal / emergency |
|------|-------|------|---------|--------------------|
| Cloudflare Access + Tunnel | Staff (25) | IdP SSO + MFA + group | Published web apps | Normal |
| Tailscale | Admins (2), CI (tag) | IdP SSO + MFA + device approval + ACL | MGMT, SERVERS (per ACL) | Normal |
| On-site MGMT port | Admins | Physical access + local credentials | MGMT | Normal / emergency |
| WireGuard break-glass | Admins (2 devices) | Private key (+ device disk encryption) | MGMT only | **Emergency only** |
| Local accounts (`root@pam`, OPNsense `root`) | Admins | Password from sealed vault + TOTP where possible | Device itself | **Emergency only** |

## 2. Identity

| Item | Design |
|------|--------|
| Identity provider (IdP) | Company cloud suite (Google Workspace or Microsoft Entra ID) — OIDC/SAML |
| MFA | Enforced for all users; admins use phishing-resistant MFA (security keys / passkeys) |
| Groups | `grp-staff` (all), `grp-hr` (HR app), `grp-it-admins` (admins) |
| Joiner / leaver | Account and group changes only in the IdP → access to Cloudflare apps and Tailscale follows automatically |
| Break-glass accounts | Local accounts with long random passwords, stored in the company password manager + sealed paper copy; usage reviewed after each incident |

## 3. Cloudflare

### 3.1 Tunnel

| Item | Design |
|------|--------|
| Tunnel | One **remotely-managed** tunnel `office-tunnel`, configuration defined in Terraform |
| Connectors | `cfd01`, `cfd02` (DMZ) running `cloudflared` as a service with the **tunnel token** (secret, delivered via SOPS → Ansible) |
| Outbound only | TCP/UDP 7844 + TCP 443 to Cloudflare; no inbound ports |
| Redundancy | 2 replicas; each opens connections to 2 Cloudflare data centres |
| Origin TLS | Apps serve HTTPS with an internal certificate; `cloudflared` verifies it (`originServerName` = internal name) |

**Ingress rules** (evaluated top-down; last rule is the catch-all):

| Public hostname | Origin service | Notes |
|-----------------|----------------|-------|
| `files.example.com` | `https://files01.int.example.com:443` | Upload size limits checked in PoC |
| `wiki.example.com` | `https://wiki01.int.example.com:443` | |
| `hr.example.com` | `https://hr01.int.example.com:443` | |
| *(anything else)* | `http_status:404` | Default deny |

Equivalent local configuration file (for learning; production uses Terraform):

```yaml
# /etc/cloudflared/config.yml  (illustrative — remotely-managed tunnels keep this in Cloudflare)
tunnel: 00000000-0000-0000-0000-000000000000
ingress:
  - hostname: files.example.com
    service: https://files01.int.example.com:443
    originRequest:
      originServerName: files01.int.example.com
  - hostname: wiki.example.com
    service: https://wiki01.int.example.com:443
  - hostname: hr.example.com
    service: https://hr01.int.example.com:443
  - service: http_status:404
```

### 3.2 DNS (public)

| Record | Type | Value | Proxied |
|--------|------|-------|:-------:|
| `files` | CNAME | `<tunnel-id>.cfargotunnel.com` | ✅ |
| `wiki` | CNAME | `<tunnel-id>.cfargotunnel.com` | ✅ |
| `hr` | CNAME | `<tunnel-id>.cfargotunnel.com` | ✅ |
| `@`, `www` | — | Company website (external hosting, out of scope) | ✅ |

No record reveals the office IP address. Optional `vpn.example.com` (DNS-only, not proxied)
points to the office WAN IP for WireGuard break-glass.

### 3.3 Access applications and policies

| Application | Hostname | Policy | Session |
|-------------|----------|--------|---------|
| Files | `files.example.com` | Allow: IdP group `grp-staff` | 12 h |
| Wiki | `wiki.example.com` | Allow: `grp-staff` | 12 h |
| HR | `hr.example.com` | Allow: `grp-hr`; require MFA; optional: require managed device posture | 4 h |
| *(default)* | — | Anything not listed is blocked by the tunnel catch-all | — |

### 3.4 Account security and API tokens

| Item | Design |
|------|--------|
| Cloudflare account members | 2 admins, SSO + MFA, no shared logins |
| Terraform token | Scoped to account `Example Corp` and zone `example.com`: DNS edit, Tunnel edit, Access apps/policies edit — nothing else |
| Token storage | GitHub Actions secret (CI) + SOPS file (local use); rotated yearly |
| Audit | Cloudflare audit log reviewed monthly |

## 4. Tailscale

| Item | Design |
|------|--------|
| Tailnet | Company tailnet, login via IdP (SSO + MFA) |
| Device approval | Enabled — new devices need admin approval |
| Key expiry | Enabled for user devices (e.g. 90 days); disabled only for tagged servers |
| Subnet router | `ts01` (MGMT) advertises `10.10.10.0/24`, `10.10.20.0/24`; routes auto-approved for `tag:subnet-router` |
| Exit node | Not used |
| DNS | Split DNS: `int.example.com` → `10.10.10.1` |
| Tags | `tag:subnet-router` (ts01), `tag:ci` (future cloud CI jobs via Tailscale GitHub Action) |
| Policy file | `tailscale/policy.hujson` in Git, deployed by a GitHub Action |

**ACL policy draft** (HuJSON):

```jsonc
{
  "groups": {
    "group:it-admins": ["admin1@example.com", "admin2@example.com"],
  },
  "tagOwners": {
    "tag:subnet-router": ["group:it-admins"],
    "tag:ci":            ["group:it-admins"],
  },
  "autoApprovers": {
    "routes": {
      "10.10.10.0/24": ["tag:subnet-router"],
      "10.10.20.0/24": ["tag:subnet-router"],
    },
  },
  "acls": [
    // Admins: management UIs and SSH in MGMT, everything in SERVERS
    {"action": "accept", "src": ["group:it-admins"],
     "dst": ["10.10.10.0/24:22,443,8006,8007", "10.10.20.0/24:*"]},
    // CI jobs: Proxmox API only
    {"action": "accept", "src": ["tag:ci"], "dst": ["10.10.10.10:8006"]},
  ],
  "tests": [
    {"src": "admin1@example.com", "accept": ["10.10.10.10:8006", "10.10.20.10:443"]},
    {"src": "tag:ci", "accept": ["10.10.10.10:8006"], "deny": ["10.10.20.12:443"]},
  ],
}
```

Even with a Tailscale ACL allowing a flow, **OPNsense rules still apply** for traffic from
`ts01` into other zones (defense in depth).

## 5. WireGuard break-glass

| Item | Design |
|------|--------|
| Server | OPNsense WireGuard instance `wg-breakglass`, listen UDP 51820 on WAN |
| Tunnel network | `10.10.200.0/24` (see [LLD network §3.5](lld-network.md#35-wireguard-break-glass)) |
| Peers | 2 admin laptops, each with its own key pair; optional pre-shared key |
| Client routing | `AllowedIPs = 10.10.10.0/24` (split tunnel) |
| Firewall | `WG-BREAKGLASS → MGMT` TCP 22, 443, 8006, 8007 only |
| Key storage | Private keys only on the devices (encrypted disk); server key in SOPS; **never in plain Git** |
| Monitoring | Alert when a break-glass peer completes a handshake (unexpected use = incident) |
| Testing | Quarterly test from outside the office; documented in runbook |
| Rotation | Keys rotated yearly and when a device is lost or an admin leaves |

Client configuration template (committed only as `*.conf.example`):

```ini
# wg-breakglass.conf.example — copy, fill in, keep OUT of Git
[Interface]
PrivateKey = <admin-device-private-key>
Address    = 10.10.200.11/32
DNS        = 10.10.10.1

[Peer]
PublicKey           = <opnsense-public-key>
Endpoint            = vpn.example.com:51820
AllowedIPs          = 10.10.10.0/24
PersistentKeepalive = 25
```

## 6. Access matrix (who can reach what, and how)

| Target | Staff (office) | Staff (remote) | HR group | Admin (Tailscale) | Admin (break-glass) | CI runner |
|--------|:-------------:|:--------------:|:--------:|:-----------------:|:-------------------:|:---------:|
| Files / Wiki | ✅ Access or direct | ✅ Access | ✅ | ✅ | ❌ | ❌ |
| HR app | ❌ | ❌ | ✅ Access | ✅ | ❌ | ❌ |
| Proxmox UI/API | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ API token |
| OPNsense UI | ❌ | ❌ | ❌ | ✅ | ✅ | ⚠️ API |
| PBS UI | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ |
| SSH to servers | ❌ | ❌ | ❌ | ✅ | ⚠️ MGMT hosts only | ✅ (Ansible) |
