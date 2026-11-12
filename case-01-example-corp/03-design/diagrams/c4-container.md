# C4 Level 2 — Containers

**Question answered:** *Which runnable parts make up the platform, where do they run, and how
do they talk to each other?* (In C4, a "container" is any separately running unit — a VM,
an LXC, a service — not only Docker containers.)
**Audience:** architects, engineers, operations.

```mermaid
flowchart TB
  CF["Cloudflare edge"]
  TSC["Tailscale coordination"]
  GH["GitHub"]

  subgraph pve["pve01 — Proxmox VE"]
    direction TB
    OPN["opnsense01 (VM)<br/>routing · firewall · DNS · DHCP · WireGuard"]
    subgraph dmz["DMZ — VLAN 30"]
      CFD["cfd01 + cfd02 (LXC ×2)<br/>cloudflared"]
    end
    subgraph srv["SERVERS — VLAN 20"]
      FILES["files01 (VM)<br/>file service"]
      WIKI["wiki01 (LXC)<br/>wiki"]
      HR["hr01 (VM)<br/>HR app"]
      MON["mon01 (LXC)<br/>Prometheus · Grafana · Uptime Kuma"]
    end
    subgraph mgmt["MGMT — VLAN 10"]
      PVEUI["Proxmox API / UI :8006"]
      TS["ts01 (LXC)<br/>Tailscale subnet router"]
      RUN["runner01 (LXC)<br/>GitHub Actions runner"]
    end
  end
  PBS["pbs01 — Proxmox Backup Server<br/>(separate appliance, VLAN 10)"]

  CF <-->|"tunnel, outbound 7844"| CFD
  CFD -->|"HTTPS 443"| FILES & WIKI & HR
  TSC <-->|"control plane"| TS
  TS -->|"admin traffic per ACL"| PVEUI
  RUN -->|"poll jobs 443"| GH
  RUN -->|"Terraform API"| PVEUI
  MON -->|"scrape metrics"| PVEUI & OPN
  PVEUI -->|"nightly backups"| PBS
```

| Container | Technology | Responsibility | Data | Rebuild strategy |
|-----------|------------|----------------|------|------------------|
| `opnsense01` | OPNsense VM | Inter-zone routing and filtering, NAT, DNS, DHCP, NTP, WireGuard | Config (`config.xml`) | Restore VM or reinstall + import config |
| `cfd01/02` | cloudflared on Debian LXC (2 replicas) | Outbound tunnel to Cloudflare | None (token) | Terraform + Ansible |
| `files01` | File service on Debian VM | Files and sharing | **2 TB+ user files** | Restore from PBS |
| `wiki01` | Wiki on Debian LXC | Documentation | Pages, DB | Restore from PBS |
| `hr01` | HR web app on Debian VM | HR processes | **Personal data** | Restore from PBS |
| `mon01` | Prometheus, Grafana, Uptime Kuma | Metrics, dashboards, alerts | Metrics (30 days) | Restore or rebuild (history optional) |
| `ts01` | Tailscale on Debian LXC | Subnet router for admins | None (auth key) | Terraform + Ansible |
| `runner01` | GitHub Actions runner | Executes IaC pipelines in the lab | None | Terraform + Ansible |
| Proxmox API/UI | Proxmox VE | Guest lifecycle | Host config | Reinstall from docs + IaC |
| `pbs01` | Proxmox Backup Server | Backup storage | **Backups** | Reinstall; data via off-site copy |

Simplified for readability: Tailscale admins also reach SERVERS, the runner also uses SSH (Ansible) to SERVERS, and monitoring also scrapes the apps — see [traffic flows](traffic-flows.md) and the [firewall rule matrix](../lld-network.md#5-firewall-rule-matrix).

Previous level: [C4 context](c4-context.md). Network view: [network topology](network-topology.md).
