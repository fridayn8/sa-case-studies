# Low-Level Design — Network

| | |
|---|---|
| **Document** | LLD — Network (zones, VLANs, IP plan, firewall, DNS, DHCP, switching) |
| **Version** | 0.1 (draft) |
| **Status** | Proposed |
| **Parent** | [HLD](hld.md) |
| **Implemented in** | `sa-projects` — [example-corp project](https://github.com/fridayn8/sa-projects/tree/main/projects/example-corp) (OPNsense configuration as code); the switch is configured manually and documented here |

> Fictional scenario. All names, domains and addresses are placeholders.

## 1. Design principles

1. **Default deny** between zones; every allowed flow is listed in the [rule matrix](#5-firewall-rule-matrix).
2. **One zone = one VLAN = one /24 subnet** — simple to reason about and to firewall.
3. Addressing from `10.10.0.0/16`; avoids common home ranges (`192.168.0.0/24`, `192.168.1.0/24`)
   so VPN users never have overlapping networks.
4. VLAN ID = third octet (VLAN 20 → `10.10.20.0/24`) — easy to remember.
5. Gateway is always `.1` (OPNsense); static servers `.10–.99`; DHCP `.100–.249`.

## 2. Zones and VLANs

| VLAN | Zone | Subnet | Gateway | Purpose | Trust |
|-----:|------|--------|---------|---------|-------|
| — | WAN | ISP-assigned | ISP | Internet uplink | Untrusted |
| 10 | MGMT | `10.10.10.0/24` | `10.10.10.1` | Proxmox, PBS, switch, AP management, BMC, Tailscale router, CI runner | Highest |
| 20 | SERVERS | `10.10.20.0/24` | `10.10.20.1` | Internal apps and monitoring | High |
| 30 | DMZ | `10.10.30.0/24` | `10.10.30.1` | `cloudflared` connectors | Low |
| 40 | STAFF | `10.10.40.0/24` | `10.10.40.1` | Staff laptops (wired + Wi-Fi) | Medium |
| 50 | GUEST | `10.10.50.0/24` | `10.10.50.1` | Visitor Wi-Fi | Untrusted |
| 60 | IOT | `10.10.60.0/24` | `10.10.60.1` | Printers, TVs, smart devices | Low |
| 70 | *(reserved)* | `10.10.70.0/24` | — | Future: CCTV | — |
| — | WG-BREAKGLASS | `10.10.200.0/24` | `10.10.200.1` | WireGuard tunnel addresses | High (key-based) |
| — | TAILNET | `100.64.0.0/10` | — | Tailscale addresses (assigned by Tailscale) | Per ACL |

## 3. IP address plan

### 3.1 MGMT — VLAN 10

| Host | IP | Notes |
|------|----|-------|
| `opnsense01` (LAN interface) | `10.10.10.1` | Gateway |
| `sw01` | `10.10.10.2` | Managed switch |
| `ap01`, `ap02` | `10.10.10.3–4` | Wi-Fi access points |
| `pve01-bmc` | `10.10.10.9` | Server out-of-band management (IPMI/iDRAC/iLO) |
| `pve01` | `10.10.10.10` | Proxmox VE host |
| `pbs01` | `10.10.10.11` | Proxmox Backup Server appliance |
| `ts01` | `10.10.10.20` | Tailscale subnet router (LXC) |
| `runner01` | `10.10.10.21` | GitHub Actions self-hosted runner (LXC) |
| DHCP pool | `10.10.10.200–.220` | Small pool for on-site admin laptops only |

### 3.2 SERVERS — VLAN 20

| Host | IP | Service | Ports |
|------|----|---------|-------|
| `files01` | `10.10.20.10` | File service | 443 |
| `wiki01` | `10.10.20.11` | Wiki | 443 |
| `hr01` | `10.10.20.12` | HR app | 443 |
| `mon01` | `10.10.20.20` | Prometheus 9090, Grafana 3000, Uptime Kuma 3001 | as listed |

### 3.3 DMZ — VLAN 30

| Host | IP | Service |
|------|----|---------|
| `cfd01` | `10.10.30.10` | cloudflared replica 1 |
| `cfd02` | `10.10.30.11` | cloudflared replica 2 |

### 3.4 Client zones

| Zone | DHCP range | Lease | DNS server |
|------|-----------|-------|------------|
| STAFF | `10.10.40.100–.249` | 8 h | `10.10.40.1` |
| GUEST | `10.10.50.100–.249` | 2 h | `10.10.50.1` (filtered) |
| IOT | `10.10.60.100–.249` (printers reserved `.10–.29`) | 24 h | `10.10.60.1` |

### 3.5 WireGuard break-glass

| Peer | Tunnel IP | Allowed IPs on OPNsense |
|------|-----------|-------------------------|
| OPNsense (server) | `10.10.200.1/24` | — |
| `admin-laptop-1` | `10.10.200.11/32` | `10.10.200.11/32` |
| `admin-laptop-2` | `10.10.200.12/32` | `10.10.200.12/32` |

Clients route only `10.10.10.0/24` (MGMT) through the tunnel (split tunnel).

## 4. Physical and virtual switching

### 4.1 Proxmox host networking

| Proxmox bridge | Physical port | Mode | Connected to |
|----------------|---------------|------|--------------|
| `vmbr0` | `nic0` | Untagged, no host IP | ISP modem/ONT → OPNsense WAN only |
| `vmbr1` | `nic1` | **VLAN-aware**, trunk (VLANs 10–70) | Switch trunk port; Proxmox host IP on `vmbr1.10` |

- VMs/LXCs attach to `vmbr1` with a **VLAN tag** (e.g. `files01` tag 20).
- OPNsense attaches to `vmbr0` (WAN) and `vmbr1` **without tag** (receives the trunk, VLAN
  interfaces created inside OPNsense).
- The Proxmox host itself has **no IP on WAN**.

### 4.2 Switch port plan (`sw01`)

| Port | Mode | VLANs | Device |
|------|------|-------|--------|
| 1 | Trunk | 10 (native: none), 20, 30, 40, 50, 60 | `pve01` `nic1` |
| 2 | Access | 10 | `pbs01` |
| 3 | Access | 10 | `pve01` BMC |
| 4 | Access | 10 | **On-site admin port** (labelled; break-glass when OPNsense is down) |
| 5–6 | Trunk | 10 (native, for AP management), 40, 50, 60 | `ap01`, `ap02` |
| 7–20 | Access | 40 | Staff desks |
| 21–22 | Access | 60 | Printers |
| 23–24 | Disabled | — | Spare (shut down) |

### 4.3 Wi-Fi

| SSID | VLAN | Security |
|------|------|----------|
| `ExampleCorp` | 40 STAFF | WPA3-Enterprise (or WPA2/3-Personal with rotated key if no RADIUS) |
| `ExampleCorp-Guest` | 50 GUEST | WPA2/3-Personal, client isolation, rotated monthly |
| `ExampleCorp-IoT` | 60 IOT | WPA2-Personal (device compatibility), hidden |

## 5. Firewall rule matrix

Rows = **source**, columns = **destination**. ✅ allow (as listed), ❌ deny, ⚠️ limited.
All rules are **stateful** — return traffic is allowed automatically. Every deny is logged.

| From ↓ / To → | MGMT | SERVERS | DMZ | STAFF | GUEST | IOT | Internet |
|---------------|:----:|:-------:|:---:|:-----:|:-----:|:---:|:--------:|
| **MGMT** | ✅ | ✅ | ✅ | ❌ | ❌ | ⚠️ R1 | ✅ |
| **SERVERS** | ⚠️ R2 | ✅ | ❌ | ❌ | ❌ | ❌ | ⚠️ R3 |
| **DMZ** | ❌ | ⚠️ R4 | ✅ | ❌ | ❌ | ❌ | ⚠️ R5 |
| **STAFF** | ❌ | ⚠️ R6 | ❌ | ❌ R7 | ❌ | ⚠️ R8 | ✅ |
| **GUEST** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ R9 |
| **IOT** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ⚠️ R10 |
| **WG-BREAKGLASS** | ⚠️ R11 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **TAILNET** (via `ts01`) | ⚠️ ACL | ⚠️ ACL | ❌ | ❌ | ❌ | ❌ | ❌ |
| **WAN** (inbound) | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | — R12 |

### Rule details

| Rule | Source | Destination | Ports | Reason |
|------|--------|-------------|-------|--------|
| R1 | MGMT | IOT printers | TCP 80/443 | Printer administration |
| R2 | `mon01` | MGMT hosts | TCP 9100, 9221, 8006, 8007 | Metrics scraping (node exporter, PVE exporter, Proxmox/PBS APIs) |
| R3 | SERVERS | Internet | TCP 80/443, UDP 123 | Updates, NTP, SaaS APIs |
| R4 | `cfd01–02` | `files01`, `wiki01`, `hr01` | TCP 443 | Tunnel → apps only |
| R5 | DMZ | Internet | TCP 443/7844, UDP 7844 | cloudflared → Cloudflare edge; DNS via OPNsense only |
| R6 | STAFF | `files01`, `wiki01`, `hr01` | TCP 443 | Direct internal access (optional; Access path preferred) |
| R7 | STAFF | STAFF | — | Client isolation on Wi-Fi; wired peer traffic not routed |
| R8 | STAFF | IOT printers | TCP 631, 9100, 443; mDNS via repeater | Printing |
| R9 | GUEST | Internet | Any, except RFC 1918 destinations | Internet only |
| R10 | IOT | Internet | TCP 443 to vendor endpoints (alias), UDP 123 | Firmware/cloud only |
| R11 | `10.10.200.0/24` | MGMT | TCP 22, 443, 8006, 8007 | Break-glass admin only |
| R12 | WAN | OPNsense | UDP 51820 | WireGuard break-glass listener; everything else dropped |

All zones may reach **OPNsense on their own gateway IP** for DNS (UDP/TCP 53) and DHCP; the
OPNsense web UI and SSH listen **only on the MGMT interface**.

**Aliases (OPNsense)** keep rules readable and are managed as code:
`ALIAS_APPS` (files01, wiki01, hr01), `ALIAS_CFD` (cfd01, cfd02), `ALIAS_PRINTERS`,
`ALIAS_RFC1918` (`10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`), `ALIAS_IOT_VENDORS`.

## 6. DNS

| Function | Design |
|----------|--------|
| Public zone `example.com` | Cloudflare (managed by Terraform). App records are **Tunnel CNAMEs** (`files`, `wiki`, `hr`); no A records pointing to the office |
| Internal zone `int.example.com` | OPNsense Unbound host overrides (e.g. `files.int.example.com → 10.10.20.10`) |
| Resolution | Clients → OPNsense Unbound (per-zone interface) → upstream DNS over TLS (e.g. Cloudflare `1.1.1.1` / Quad9) |
| Guest DNS | Same resolver with blocklists; no internal names answered |
| Tailscale clients | Split DNS: `int.example.com` → `10.10.10.1` via subnet router |
| DNSSEC | Enabled on Cloudflare zone; validation on Unbound |

## 7. NAT and routing

- **Outbound NAT:** automatic, all internal zones → WAN address.
- **No port forwards** (inbound NAT) — only the WireGuard listener on the firewall itself.
- **Static routes:** none needed; Tailscale subnet router `ts01` advertises
  `10.10.10.0/24` and `10.10.20.0/24`, with SNAT so return traffic needs no route
  (default Tailscale behaviour).

## 8. Time, logging and monitoring

| Item | Design |
|------|--------|
| NTP | OPNsense serves NTP to all zones; upstream `pool.ntp.org` |
| Firewall logs | Local + remote syslog to `mon01` (retention 90 days) |
| Metrics | OPNsense exporter / SNMP scraped by Prometheus on `mon01` |

## 9. Open points

- Confirm ISP provides public IPv4 (assumption A-1) — affects WireGuard break-glass.
- IPv6: disabled internally in phase 1 (documented decision to revisit).
- RADIUS for WPA3-Enterprise — depends on IdP capabilities; fallback WPA2/3-Personal.
