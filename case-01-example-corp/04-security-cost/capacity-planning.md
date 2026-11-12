# Capacity Planning

Sizing for 3 years (NFR-P1…P4). Method: **current demand → growth → headroom → compare with
hardware**. Figures are estimates for the fictional scenario; replace them with measured data
(Prometheus) after go-live and review every 6 months.

## 1. Inputs

| Input | Value | Source |
|-------|-------|--------|
| Users | 25 today, design for 40 | NFR-P1 |
| File data | 2.0 TB today, +30 %/year | NFR-P2 |
| Other app data | ~100 GB total, +20 %/year | Estimate |
| Daily data change rate | ~2 % of total data | Typical office file workload |
| Target utilisation | ≤ 70 % average (30 % headroom) | NFR-P4 |
| ZFS rule of thumb | Keep pools < 80 % full | Performance & fragmentation |

## 2. Compute (`pve01`: 16 cores / 32 threads, 128 GB RAM)

| Consumer | vCPU | RAM |
|----------|-----:|----:|
| Guests ([catalogue](../03-design/lld-compute.md#3-guest-catalogue)) | 23 | 54 GB |
| ZFS ARC (capped) | — | 16 GB |
| Proxmox host OS & services | — | 4 GB |
| Reserve for lab/test guests & upgrades (year 3) | 8 | 16 GB |
| **Total planned** | **31** | **90 GB** |
| **Available** | 32 threads | 128 GB |
| **Utilisation** | **~1:1 vCPU:thread** (allocated; actual CPU load expected < 30 %) | **70 %** ✅ |

**Notes**

- vCPUs can be overcommitted (typical safe ratio for office workloads: 2–4 vCPU per thread);
  allocation ≠ usage. Measure actual CPU with Prometheus.
- RAM is **not** overcommitted for production guests (ballooning off for VMs with data).

## 3. Storage

### 3.1 VM storage — `fast` pool

2 × 1.92 TB NVMe, ZFS mirror → ≈ 1.8 TB usable.

| Year | Guest system disks | Snapshots / growth | Total | % of usable |
|-----:|-------------------:|-------------------:|------:|------------:|
| 1 | 410 GB | 100 GB | 510 GB | 28 % |
| 3 | 500 GB | 200 GB | 700 GB | 39 % ✅ |

### 3.2 Data storage — `bulk` pool

2 × 8 TB HDD, ZFS mirror → ≈ 7 TB usable after ZFS overhead.

| Year | File data (+30 %/yr) | Other | Total | % of usable |
|-----:|---------------------:|------:|------:|------------:|
| 1 | 2.0 TB | 0.1 TB | 2.1 TB | 30 % |
| 2 | 2.6 TB | 0.12 TB | 2.7 TB | 39 % |
| 3 | 3.4 TB | 0.14 TB | 3.5 TB | 50 % ✅ |

### 3.3 Backup storage — pbs01

2 × 8 TB HDD, ZFS mirror → ≈ 7 TB usable.

Proxmox Backup Server deduplicates and compresses; stored size ≈ **one full copy + changed
chunks kept by retention**. Retention 14 daily + 8 weekly + 12 monthly ≈ 34 restore points.

| Year | Protected data | Full copy | Changes kept (2 %/day × ~34 points*) | Before compression | After ~1.3× compression | % of usable |
|-----:|---------------:|----------:|------------------------------------:|-------------------:|------------------------:|------------:|
| 1 | 2.5 TB | 2.5 TB | 1.7 TB | 4.2 TB | 3.2 TB | 46 % |
| 3 | 3.9 TB | 3.9 TB | 2.7 TB | 6.6 TB | 5.1 TB | **73 %** ⚠️ |

\* Simplification: weekly/monthly points share many chunks, so real usage is usually lower.

**Finding:** backup storage reaches the 70–80 % zone in **year 3**. Options (decide before the end of year 2):
buy 2 × 12 TB disks for `pbs01` up front (small extra cost), or reduce monthly retention,
or plan a disk upgrade in year 2. This is exactly the kind of trade-off a capacity plan should
surface early.

## 4. Network

| Flow | Estimate | Capacity | OK? |
|------|----------|----------|:---:|
| Office internal (LAN) | Bursty file transfers | 2.5 GbE host, 1 GbE desks | ✅ |
| Remote users downloading files (office **upload**) | 10 concurrent × ~5 Mbit/s | 100 Mbit/s uplink | ✅ (shared; large files slower) |
| Nightly backup `pve01 → pbs01` | ~50–80 GB changed | 2.5 GbE ≈ 280 MB/s → < 10 min | ✅ |
| Weekly off-site sync to USB disk (`pbs01` → removable datastore) | ~0.3–0.5 TB changed/week | USB 3 HDD ≈ 150 MB/s → < 1 h | ✅ |
| Initial off-site seed | ~3 TB | USB 3 HDD ≈ 6 h (local, no internet needed) | ✅ |

## 5. Power and UPS

| Device | Typical draw |
|--------|-------------:|
| `pve01` | 150 W |
| `pbs01` | 30 W |
| Switch (PoE for APs) | 40 W |
| **Total** | **~220 W** |

- Energy: 220 W × 24 h × 365 ≈ **1 930 kWh/year**.
- UPS: ~1 000 VA / 600 W line-interactive gives ~15–20 min at this load — enough for a
  **clean automatic shutdown** (Network UPS Tools on `pve01`), not for riding out long outages.

## 6. Review triggers

Re-run this plan when: users > 35, file data grows > 40 %/year, any pool > 70 %, average RAM
> 75 %, or a new service with significant data is added.
