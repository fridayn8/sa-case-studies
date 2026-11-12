---
status: accepted
date: 2026-11-11
deciders: [fridayn8]
consulted: [IT administrator]
informed: [Staff]
---

# ADR-0004: Tailscale for admin access, WireGuard for break-glass, Cloudflare Access for staff

## Context and Problem Statement

Administrators need remote access to management interfaces (FR-03) and must still get in when
central services fail (FR-04). Staff need remote access to a few web apps (FR-01). Today admin
UIs are port-forwarded (P2). Which remote access approach should each group use?

## Decision Drivers

- SSO + MFA for normal access (NFR-S2)
- No admin interface exposed to the internet (NFR-S3)
- Fine-grained, reviewable access rules (policy as code)
- An emergency path independent of the IdP and third-party coordination services
- Works behind NAT / CGNAT for remote users without opening many ports
- Low operational effort for one part-time admin (NFR-O3)

## Considered Options

1. Classic remote-access VPN for everyone (OpenVPN or WireGuard on OPNsense)
2. Tailscale for admins + WireGuard break-glass + Cloudflare Access for staff apps
3. Headscale (self-hosted Tailscale control server)
4. Cloudflare Zero Trust (Access + WARP) for everyone, including admins
5. NetBird / ZeroTier

## Decision Outcome

Chosen option: **"Option 2"**, because each group gets the narrowest suitable access:
staff reach only specific web apps through Cloudflare Access (no network-level access at all),
admins get network-level access through Tailscale with SSO, MFA, device approval and ACLs in
Git, and a plain WireGuard tunnel on OPNsense provides a **break-glass** path that depends on
neither the IdP nor Tailscale.

### Consequences

- 👍 Good, because staff devices never join the internal network (smaller blast radius).
- 👍 Good, because Tailscale handles NAT traversal and key rotation; ACLs are versioned and testable.
- 👍 Good, because break-glass keeps admins in control during SaaS or IdP outages.
- 👎 Bad, because two admin access mechanisms must be maintained and the break-glass path must be tested quarterly.
- 👎 Bad, because dependency on two SaaS vendors (Cloudflare, Tailscale) — mitigated by break-glass and on-site access.
- 👎 Bad, because break-glass needs one open UDP port and a reachable public IP (assumption A-1).

### Confirmation

Phase 5: Tailscale ACL `tests` pass in CI; Phase 4: break-glass test from outside the office
succeeds and triggers the "break-glass used" alert.

## Pros and Cons of the Options

### Classic VPN for everyone

- 👍 Good, because simple, self-hosted, well understood.
- 👎 Bad, because grants network-level access to all users; per-app control and SSO/MFA need extra components; one more port and client config per user.

### Tailscale + WireGuard break-glass + Cloudflare Access (chosen)

- 👍 Good, because least privilege per user group; SSO everywhere in normal operation.
- 👎 Bad, because more moving parts.

### Headscale

- 👍 Good, because no dependency on the Tailscale SaaS control plane.
- 👎 Bad, because another critical service to host, secure and back up; fewer features.

### Cloudflare Zero Trust for everyone

- 👍 Good, because one vendor, one policy engine.
- 👎 Bad, because if Cloudflare or the IdP is unavailable, admins have no way in; private-network routing for admins is less flexible than Tailscale ACLs for this use case.

### NetBird / ZeroTier

- 👍 Good, because similar mesh concepts; NetBird is fully open source.
- 👎 Bad, because smaller ecosystem and less documentation for learners; no strong advantage here.

## More Information

- Related: [LLD access](../../03-design/lld-access.md), [traffic flows](../../03-design/diagrams/traffic-flows.md), [ADR-0005](0005-public-ingress-cloudflare-tunnel.md)
- Free tiers only ([ADR-0010](0010-free-only-tooling-policy.md)): Tailscale Personal for the lab; Headscale is the free fallback.
- Verify Tailscale and Cloudflare plan limits and pricing at implementation time (assumption A-5).
- Revisit if: the number of admins grows, or a self-hosted control plane becomes a requirement.
