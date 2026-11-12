# Network Topology and Trust Boundaries

Details (IP plan, rule matrix, switch ports): [LLD network](../lld-network.md).

## 1. Physical topology

```mermaid
flowchart TB
  ISP["ISP modem / ONT"] -->|"WAN"| NIC0
  subgraph pve01["pve01 (Proxmox VE)"]
    NIC0["nic0 → vmbr0<br/>(WAN, no host IP)"]
    NIC1["nic1 → vmbr1<br/>(VLAN-aware trunk)"]
    OPN["opnsense01 VM"]
    NIC0 --- OPN
    OPN --- NIC1
  end
  NIC1 ===|"trunk: VLAN 10,20,30,40,50,60"| SW["sw01 managed switch"]
  SW -->|"access VLAN 10"| PBS["pbs01"]
  SW -->|"access VLAN 10"| BMC["pve01 BMC"]
  SW -->|"access VLAN 10"| ADMINPORT["On-site admin port"]
  SW ===|"trunk 10,40,50,60"| AP["ap01 / ap02<br/>SSIDs: Staff · Guest · IoT"]
  SW -->|"access VLAN 40"| DESKS["Staff desks"]
  SW -->|"access VLAN 60"| PRN["Printers"]
  UPS["UPS"] -.-> pve01 & SW & PBS
```

## 2. Logical zones and trust boundaries

Dashed boxes are **trust boundaries** — every arrow that crosses one passes through a
control (Cloudflare Access, OPNsense rule, Tailscale ACL). Each boundary (TB-n) is analysed in
the [threat model](../../04-security-cost/threat-model.md).

```mermaid
flowchart LR
  subgraph INTERNET["Internet (untrusted)"]
    USERS([Remote staff])
    ATTACKER([Anyone])
    CFE[Cloudflare edge]
    TSN[Tailnet]
  end

  subgraph FW["OPNsense — policy enforcement point"]
    direction TB
    RULES{{"Default deny<br/>+ allow-list"}}
  end

  subgraph HIGH["High trust"]
    MGMT["MGMT 10.10.10.0/24"]
    SRV["SERVERS 10.10.20.0/24"]
  end
  subgraph LOW["Low trust"]
    DMZ["DMZ 10.10.30.0/24"]
    IOT["IOT 10.10.60.0/24"]
  end
  subgraph MED["Medium trust"]
    STAFF["STAFF 10.10.40.0/24"]
  end
  subgraph NONE["Untrusted"]
    GUEST["GUEST 10.10.50.0/24"]
  end

  USERS -->|"TB-1: Access SSO+MFA"| CFE
  CFE -->|"tunnel (outbound)"| DMZ
  DMZ -->|"TB-2: 443 to apps only"| RULES --> SRV
  TSN -->|"TB-3: ACL"| MGMT
  ATTACKER -->|"TB-4: only UDP 51820"| RULES
  STAFF -->|"TB-5: 443 to apps"| RULES
  GUEST -->|"internet only"| RULES
  IOT -->|"vendor cloud only"| RULES
  RULES --> MGMT
```

## 3. Zone summary

| Zone | Trust | Who/what lives there | Can initiate to |
|------|-------|----------------------|-----------------|
| MGMT | Highest | Hypervisor, backup, admin tooling | Everything it manages |
| SERVERS | High | Business apps, monitoring | Internet (updates), MGMT (metrics only) |
| DMZ | Low | Internet-facing connectors | Apps on 443, Cloudflare |
| STAFF | Medium | Laptops | Apps on 443, printers, internet |
| IOT | Low | Printers, devices | Vendor clouds only |
| GUEST | Untrusted | Visitors | Internet only |
