# Cost Estimate and 5-Year TCO

> ⚠️ **Illustrative figures in USD** for the fictional scenario, rounded. Free-tier limits and
> hardware prices change — **verify** before using numbers in a real proposal (assumption A-5).
>
> **Free-only policy ([ADR-0010](../02-options-decisions/adr/0010-free-only-tooling-policy.md)):** all software and
> services are free (open source or free tiers). The only remaining costs are **hardware**,
> **electricity**, **people time** and — if chosen — a **domain name**.

## 1. CAPEX (one-off hardware)

| Item | Qty | Unit | Total | Notes |
|------|----:|-----:|------:|-------|
| Existing server `pve01` | 1 | 0 | 0 | Reused (constraint C-1) |
| NVMe SSD 1.92 TB (enterprise) for `fast` pool | 2 | 200 | 400 | Mirror |
| HDD 8 TB (NAS/enterprise) for `bulk` pool | 2 | 200 | 400 | Mirror |
| `pbs01` small server / mini PC | 1 | 700 | 700 | Separate hardware for backups |
| HDD 8 TB for `pbs01` | 2 | 200 | 400 | Consider 12 TB ([capacity plan §3.3](capacity-planning.md#33-backup-storage--pbs01)) |
| External USB HDD 8 TB for off-site rotation | 2 | 200 | 400 | Replaces paid cloud storage (free-only policy) |
| Managed switch, 24 ports, PoE, VLAN | 1 | 400 | 400 | |
| Wi-Fi access points (multi-SSID/VLAN) | 2 | 150 | 300 | |
| UPS 1 000 VA | 1 | 400 | 400 | With network card or USB for NUT |
| **Total CAPEX** | | | **3 400** | |

**Lab (learning):** USD 0 — nested Proxmox on the existing laptop.

## 2. OPEX (recurring, per year)

| Item | Per year | Notes |
|------|---------:|-------|
| Proxmox VE + PBS (no-subscription repositories) | 0 | Community support only |
| OPNsense Community Edition | 0 | |
| Cloudflare Free + Zero Trust Free + R2 free tier | 0 | Zero Trust Free up to 50 users; R2 10 GB free |
| Tailscale Personal | 0 | Headscale (free, self-hosted) if terms/limits don't fit |
| GitHub Free (private repo) | 0 | See limitations in ADR-0010 |
| External status page (free tier) | 0 | |
| Off-site backup (USB disk rotation) | 0 | Hardware in CAPEX |
| Domain name | 0–15 | **Only non-free item**; optional for the lab (ADR-0010) |
| Electricity (1 930 kWh × USD 0.15) | 290 | See [capacity plan §5](capacity-planning.md#5-power-and-ups) |
| Hardware spares (disks, PSU) | 300 | Replaces vendor support contracts |
| **Total OPEX** | **≈ 590–605** | Software/services: **USD 0** ✅ |

## 3. People cost (often forgotten)

| Activity | Hours | Rate | Per year |
|----------|------:|-----:|---------:|
| Routine operations (patching, reviews, restore tests, disk rotation) | 4 h/month | 40 | 1 920 |
| Incidents and small changes | 2 h/month | 40 | 960 |
| **Total** | | | **2 880** |

Without vendor support, the team relies on documentation, community forums and its own
runbooks — one more reason the runbooks written at handover matter.

## 4. Five-year TCO

| Cost | Year 0 | Years 1–5 (per year) | 5-year total |
|------|-------:|---------------------:|-------------:|
| CAPEX | 3 400 | — | 3 400 |
| OPEX | — | 605 | 3 025 |
| People (operations) | — | 2 880 | 14 400 |
| Disk refresh / expansion (year 3) | — | — | 800 |
| **Total** | | | **≈ 21 625** |

≈ **USD 360 per month** over five years, of which ~67 % is people time — automation (IaC,
alerts, runbooks) mainly reduces that part.

## 5. Value (ROI sketch)

| Benefit | Assumption | Per year |
|---------|------------|---------:|
| Avoided downtime | 10 h/year less × USD 500/h (BIA) | 5 000 |
| Avoided data-loss / ransomware recovery cost | 10 % yearly probability × USD 30 000 impact | 3 000 |
| Less time lost on remote-access workarounds | 25 staff × 5 min/week × 46 weeks × USD 30/h | 2 875 |
| **Total estimated benefit** | | **≈ 10 875** |

Annual cost (OPEX + people + CAPEX/5 + refresh/5) ≈ USD 4 325 → **ROI ≈ (10 875 − 4 325) / 4 325 ≈ 150 %**.
Treat these numbers as a structure for discussion with management, not as precise forecasts.

## 6. Options compared (high level)

| Option | 5-year cost | Pros | Cons |
|--------|------------:|------|------|
| **A. Chosen design** (on-prem + free SaaS edge) | ≈ 22 k | Zero software cost, full control, data on-site | Single host SPOF, no vendor support, needs admin skills |
| B. Add second Proxmox node + HA | ≈ 28–31 k | Survives host failure | Higher CAPEX and complexity; needs replicated storage and quorum device |
| C. Move apps to SaaS (cloud file sharing, hosted wiki/HR) | Varies; per-user subscriptions × 25 users × 5 years | Little infrastructure to run | Violates free-only policy; recurring per-user cost, data residency |

Option B is a candidate future ADR; option C conflicts with ADR-0010.
