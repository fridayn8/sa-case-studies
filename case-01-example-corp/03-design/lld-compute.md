# Low-Level Design — Compute and Storage

| | |
|---|---|
| **Document** | LLD — Compute (Proxmox host, storage, VM/LXC catalogue, templates, naming, backup) |
| **Version** | 0.1 (draft) |
| **Status** | Proposed |
| **Parent** | [HLD](hld.md) |
| **Implemented in** | `sa-projects` — [example-corp project](https://github.com/fridayn8/sa-projects/tree/main/projects/example-corp) (OpenTofu modules for VMs and LXCs, Ansible baseline hardening, backup jobs) |

> Fictional scenario. All names, domains and addresses are placeholders.

## 1. Hardware

| Item | `pve01` (existing) | `pbs01` (new) |
|------|--------------------|---------------|
| Role | Proxmox VE hypervisor | Proxmox Backup Server |
| CPU | 1× 16-core / 32-thread server CPU | 4-core mini PC / small server |
| RAM | 128 GB ECC | 16 GB |
| Boot | 2× 240 GB SSD — ZFS mirror (`rpool`) | 1× 240 GB SSD |
| VM storage | 2× 1.92 TB NVMe — ZFS mirror (`fast`) | — |
| Data storage | 2× 8 TB HDD — ZFS mirror (`bulk`) | 2× 8 TB HDD — ZFS mirror (`backup`) |
| NIC | 2× 2.5 GbE (+ BMC port) | 1× 2.5 GbE |
| Power | Redundant PSU if available; on UPS | On UPS |
| Support | Next-business-day (assumption A-4) | Spare-parts strategy |

Sizing rationale: [capacity planning](../04-security-cost/capacity-planning.md).

## 2. Proxmox configuration

| Setting | Value | Reason |
|---------|-------|--------|
| Version | Current Proxmox VE major release | Supported, security updates |
| Repository | `no-subscription` (lab and production) | Free-only policy ([ADR-0010](../02-options-decisions/adr/0010-free-only-tooling-policy.md)); community support only |
| Cluster | None (single node) | Budget; see HLD risk R-1 |
| Storage `local-zfs` | `rpool` — ISO images, templates, snippets (cloud-init) | |
| Storage `fast` | ZFS mirror NVMe — VM/LXC system disks | Low latency |
| Storage `bulk` | ZFS mirror HDD — large data disks (file service) | Capacity |
| ZFS ARC limit | 16 GB (`zfs_arc_max`) | Leave RAM for guests |
| ZFS compression | `lz4` on all pools | Free space savings, negligible CPU |
| Network | `vmbr0` WAN (no host IP), `vmbr1` VLAN-aware trunk, host IP on VLAN 10 | See [LLD network §4.1](lld-network.md#41-proxmox-host-networking) |
| Authentication | Local `root@pam` sealed (break-glass), named admin accounts with TOTP; API tokens per tool | Least privilege, audit |
| API tokens | `terraform@pve!ci` (OpenTofu; role: VM provisioning on pool `managed`), `prometheus@pve!metrics` (read-only `PVEAuditor`) | Scoped automation |
| Resource pools | `managed` (created by OpenTofu), `infra` (OPNsense, manual) | Permission scoping |
| Updates | Monthly patch window; reboot if kernel updated | NFR-S7 |

## 3. Guest catalogue

| Name | Type | VLAN | vCPU | RAM | Disk (fast) | Disk (bulk) | Template | Start order | Backup |
|------|------|-----:|-----:|----:|------------:|------------:|----------|:-----------:|:------:|
| `opnsense01` | VM | WAN + trunk | 4 | 8 GB | 32 GB | — | ISO install | 1 | Daily + config on change |
| `cfd01` | LXC | 30 | 1 | 512 MB | 8 GB | — | debian-lxc | 3 | No (stateless, rebuilt from code) |
| `cfd02` | LXC | 30 | 1 | 512 MB | 8 GB | — | debian-lxc | 3 | No |
| `ts01` | LXC | 10 | 1 | 512 MB | 8 GB | — | debian-lxc | 2 | No |
| `runner01` | LXC | 10 | 4 | 8 GB | 64 GB | — | debian-lxc | 9 | No |
| `files01` | VM | 20 | 4 | 16 GB | 64 GB | 4 TB (grows) | debian-vm | 5 | Daily |
| `wiki01` | LXC | 20 | 2 | 4 GB | 32 GB | — | debian-lxc | 6 | Daily |
| `hr01` | VM | 20 | 4 | 8 GB | 64 GB | — | debian-vm | 5 | Daily |
| `mon01` | LXC | 20 | 2 | 8 GB | 128 GB | — | debian-lxc | 4 | Weekly |
| **Total** | | | **23** | **~54 GB** | **~410 GB** | **4 TB** | | | |

- **VM vs LXC:** VMs for OPNsense (BSD), apps holding sensitive data (stronger isolation) and
  anything needing its own kernel; **unprivileged LXC** for lightweight Linux services.
- **Start order** ensures the network (OPNsense) and DNS are up before apps; `up` delay 60 s
  after OPNsense.
- CPU type `host` for performance (single node, no live migration needed).
- **QEMU guest agent** enabled on all VMs (clean shutdown, consistent backups, IP reporting).

## 4. Templates (golden images)

| Template | Built by | Base | Contents |
|----------|----------|------|----------|
| `tpl-debian-13` | OpenTofu (download + template VM) — [ADR-0012](../02-options-decisions/adr/0012-opentofu-and-cloud-image-templates.md) | Official Debian 13 *genericcloud* image | cloud-init (from the image); baseline applied after first boot by Ansible |
| `tpl-debian-lxc` | Proxmox system template (downloaded by OpenTofu) | Debian 13 standard LXC template | Baseline applied by Ansible |

Both VMs and LXCs receive the **same baseline** from the Ansible role `base-hardening`:
qemu-guest-agent (VMs), unattended-upgrades, SSH hardening, host firewall, node exporter.
Templates are refreshed **monthly**: download the newest cloud image, recreate the template
(existing clones are not affected), and let Ansible patch running guests.
Baseline contents: [hardening baseline](https://github.com/fridayn8/sa-projects/blob/main/projects/example-corp/docs/hardening-baseline.md#3-linux-vms-and-lxc).

**cloud-init** provides per-VM: hostname, static IP/gateway/DNS, SSH public keys, admin user.
No passwords are set by cloud-init.

## 5. Naming conventions

| Object | Pattern | Example |
|--------|---------|---------|
| Physical host | `<role><nn>` | `pve01`, `pbs01` |
| Guest | `<service><nn>` | `files01`, `cfd02` |
| VM ID | `<VLAN><last IP octet, 2 digits>`; templates `9000–9099` | `2010` = `files01` (VLAN 20, `.10`), `9000` = template |
| DNS (internal) | `<name>.int.example.com` | `files01.int.example.com` |
| DNS (published) | `<service>.example.com` | `files.example.com` |
| Tags (Proxmox) | `env-<env>`, `zone-<zone>`, `managed-by-<tool>` | `env-prod`, `zone-servers`, `managed-by-tofu` |
| OpenTofu resource | `<type>_<name>` snake_case | `proxmox_virtual_environment_vm.files01` |

## 6. Backup design

| Item | Value |
|------|-------|
| Backup server | `pbs01` (separate hardware, same building) |
| Datastore | `backup` (ZFS mirror), **client-side encryption** with a key stored in SOPS + offline paper copy |
| Job | Nightly 01:00, mode `snapshot`, all guests with backup = yes |
| Retention (prune) | keep-daily 14, keep-weekly 8, keep-monthly 12 |
| Verify | Weekly verify job on PBS |
| Garbage collection | Weekly |
| Off-site | Two encrypted USB disks used as a PBS *removable datastore*, synced weekly and rotated off-site (free-only policy, ADR-0010); final design in ADR-0009 (reserved, not yet written) |
| Ransomware protection | `pve01` uses a dedicated PBS API token with the minimal `DatastoreBackup` role; pruning runs on PBS itself; the off-site copy is **pulled** by the remote side, so the production host holds no credentials for it |
| OPNsense config | Built-in config backup on every change + nightly VM backup |
| Restore tests | Monthly: restore one VM to an isolated VLAN and check the service; yearly full DR test |

**Restore priority** (disaster): `opnsense01` → `ts01` → `files01`, `hr01` → `wiki01` →
`mon01` → `cfd01/02`, `runner01` (rebuilt from code).

## 7. Lab equivalent (practice environment)

The same design is practised on a laptop with **nested virtualisation**:

| Production | Lab |
|------------|-----|
| `pve01` bare metal | Proxmox VE VM in VirtualBox (or Hyper-V / VMware Workstation), 8 vCPU, 24–32 GB RAM, nested virtualisation enabled |
| ZFS mirrors | Single virtual disk (ZFS single) |
| Physical switch + VLANs | Proxmox VLAN-aware bridge only (internal) |
| `pbs01` appliance | PBS as a VM next to the Proxmox VM |
| ISP WAN | NAT network of the desktop hypervisor |
| Full app catalogue | Subset: OPNsense, cfd01, ts01, one app, mon01 |
