---
status: accepted
date: 2026-11-11
deciders: [fridayn8]
consulted: [IT administrator]
informed: [Managing director]
---

# ADR-0005: Publish internal web apps through Cloudflare Tunnel with Cloudflare Access

## Context and Problem Statement

Three internal web apps (files, wiki, HR) must be reachable by staff from anywhere (FR-01),
protected by SSO + MFA, without exposing the office network (NFR-S1). How should web traffic
enter the platform?

## Decision Drivers

- Zero inbound ports for applications (NFR-S1)
- Authentication *before* traffic reaches the app (SSO + MFA, group-based)
- DDoS and web-attack protection without own hardware
- Works even if the ISP changes our IP or uses CGNAT
- Cost (NFR-C2) and operational effort (NFR-O3)

## Considered Options

1. Port-forward 443 on OPNsense to a reverse proxy (e.g. Caddy/Traefik) + SSO proxy
2. Cloudflare Tunnel (`cloudflared` connectors) + Cloudflare Access
3. Small cloud VPS reverse proxy + WireGuard back to the office
4. Tailscale for staff as well (Tailscale Funnel or full tailnet access)

## Decision Outcome

Chosen option: **"Cloudflare Tunnel + Cloudflare Access"**, because it requires no inbound
ports, hides the office IP, authenticates users at the edge with the company IdP, and adds WAF
and DDoS protection — at no extra cost for our user count (assumption A-5).

### Consequences

- 👍 Good, because the office has no internet-reachable web service; attackers only see Cloudflare.
- 👍 Good, because access is granted per app and per IdP group; revoking a user in the IdP revokes app access.
- 👍 Good, because tunnel, DNS and Access policies are manageable with Terraform.
- 👎 Bad, because all staff app traffic depends on Cloudflare availability and the office uplink.
- 👎 Bad, because TLS terminates at Cloudflare (traffic is re-encrypted to origin) — acceptable for this data classification; document in threat model.
- 👎 Bad, because upload size limits and long-lived connections must be validated per app (PoC, assumption A-6).

### Confirmation

Phase 6: apps reachable only through Access; external port scan of the office IP shows no
open TCP ports; Access logs show SSO + MFA for each session.

## Pros and Cons of the Options

### Port-forward + reverse proxy

- 👍 Good, because fully self-hosted, no vendor dependency.
- 👎 Bad, because exposes the office IP and port 443 to the whole internet; we must run and patch the SSO proxy, certificates, WAF and rate limiting ourselves.

### Cloudflare Tunnel + Access (chosen)

- 👍 Good, because outbound-only, edge authentication, WAF, free tier.
- 👎 Bad, because vendor lock-in for ingress.

### VPS reverse proxy + WireGuard

- 👍 Good, because hides the office IP; full control.
- 👎 Bad, because another server to secure and pay for; SSO and WAF still self-managed.

### Tailscale for staff

- 👍 Good, because strong device-level access control.
- 👎 Bad, because every staff device needs a client and network-level access; more support load; broader access than needed.

## More Information

- Related: [LLD access §3](../../03-design/lld-access.md#3-cloudflare), [threat model](../../04-security-cost/threat-model.md)
- Revisit if: data classification requires end-to-end encryption without edge termination, or Cloudflare pricing/terms change.
