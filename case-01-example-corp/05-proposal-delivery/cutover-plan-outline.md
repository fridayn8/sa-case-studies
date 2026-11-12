# Case 01 — Cutover Plan (Outline)

| | |
|---|---|
| **Document** | Cutover plan outline: steps, timings, owners, checkpoints and rollback |
| **Stage** | [7 Test and go-live](../../engagement-playbook/07-test-and-go-live.md) |
| **Template** | [Cutover plan template](../../engagement-playbook/templates/cutover-plan-template.md) |
| **Related** | [HLD §10 transition](../03-design/hld.md#10-transition-from-current-state) · [Scenario 6: major upgrade](../scenarios/06-major-upgrade-proxmox.md) |
| **Status** | Outline, rehearsed in the lab; to be finalised one week before the window |

> Fictional scenario. Times are planned values.

## 1. Purpose, window and scope

**Purpose:** move the office from the current flat network and port-forwarded access to the new platform
(segmented network, staff access through the edge, administrator access through Tailscale and the
break-glass path) with a tested way back.

| | |
|---|---|
| **Window** | **Saturday 3 July 2027, 19:00–23:00** (planned; four hours); agreed with the managing director four weeks in advance. The window moved to 7 August when the contract and hardware slipped (see [lessons learned](lessons-learned.md#3-estimate-versus-actual)) |
| **Scope** | Steps 3–6 of the [HLD transition](../03-design/hld.md#10-transition-from-current-state): VLANs, OPNsense in place, apps behind the edge, port-forwards closed, administrator access |
| **Not in scope** | Retiring the old router configuration and the unknown VM `test2` (after hypercare) |
| **Decision owner** | Managing director (A); Go/No-Go recorded by the architect |
| **Dependencies** | Hardware installed and tested; backups verified; pilot users signed off; staff informed |

## 2. Go/No-Go checklist

Held **on the Thursday before** and confirmed **one hour before the window**. Any "No" in a **blocker** row
means No-Go or a signed, time-limited acceptance by the managing director.

| # | Check | Blocker? | Evidence | Status |
|---|-------|:--------:|----------|--------|
| 1 | **Backups verified by restore**: the OPNsense VM and one data VM restored in the lab from the PBS copy, timed | **Yes** | Restore log with times | ☐ |
| 2 | Off-site copy exists and its decryption key is held by two people | **Yes** | Signed note | ☐ |
| 3 | Rollback rehearsed in the lab; timing recorded | **Yes** | Rehearsal log | ☐ |
| 4 | The old router configuration is exported and the router is available as fallback | **Yes** | File hash, device in place | ☐ |
| 5 | Pilot (five users) completed with no open high issues | **Yes** | Pilot sign-off | ☐ |
| 6 | Break-glass path tested from outside the office; alert raised | **Yes** | Test log | ☐ |
| 7 | External port scan of the office address shows only the WireGuard UDP port | **Yes** | Scan result | ☐ |
| 8 | IT administrator and IT partner available during the window and the following Sunday | **Yes** | Confirmation | ☐ |
| 9 | Staff informed (Wi-Fi off 19:00–22:00; Monday login instructions) | No | Message sent | ☐ |
| 10 | Support contact and escalation path published | No | Message | ☐ |
| 11 | All deviations have an owner and an expiry (see [CR-001 deviations](change-request-cctv.md#6-design-deviations-seen-during-the-build)) | No | Log | ☐ |
| 12 | Edge free-plan limits re-verified (assumption A-5) | No | Screenshot with date | ☐ |

## 3. Roles

| Role | Person | Responsibility |
|------|--------|----------------|
| Decision owner | Managing director | Go, No-Go, rollback authority |
| Cutover lead | IT administrator | Runs the steps |
| Technical second | IT partner | Second pair of eyes, on the phone |
| Architect | Solution architect | Runs checkpoints, keeps the log, advises on rollback |
| Communications | Managing director's assistant | Staff messages |

## 4. Checks before and after

Smoke and security checks run at each checkpoint (the test matrix that answers requirement IDs).

| ID | Check | Expected | Requirement |
|----|-------|----------|-------------|
| T-1 | Internet from each zone | Staff, guest and servers reach the internet; IoT limited | FR-05, FR-06 |
| T-2 | Guest isolation | A guest device cannot reach any internal address | FR-05, NFR-S4 |
| T-3 | Zone rules | Connection tests per the rule matrix pass and deny | NFR-S4 |
| T-4 | Internal DNS | `files.int.example.com` resolves from STAFF | FR-07 |
| T-5 | Staff access | Test user with MFA reaches the three apps from outside | FR-01, FR-02 |
| T-6 | Admin access | Admin reaches the management zone through Tailscale | FR-03 |
| T-7 | Break-glass | WireGuard from outside reaches only the management zone; alert raised | FR-04 |
| T-8 | Exposure | External scan shows no open application ports | NFR-S1 |
| T-9 | Backups | Night after cutover: backup completes; restore of one VM later in hypercare | FR-08 |
| T-10 | Monitoring | Alert fires on a test condition and links to a runbook | FR-09, NFR-O4 |
| T-11 | Performance | 25 users on the file service meet the capacity target | NFR-P1…P4 |

## 5. Cutover steps

| Time | Step | Owner | Checkpoint | Rollback available? |
|------|------|-------|------------|--------------------|
| 19:00 | Final Go/No-Go; announce start; take final backups and export the router configuration | Architect, IT administrator | Backups complete; hashes recorded | Yes |
| 19:20 | Configure switch VLANs and access points (zones, SSIDs) | IT administrator | Management port still reachable | Yes: revert the switch configuration |
| 19:40 | Bring OPNsense online next to the old router (not yet the default gateway) | IT administrator, IT partner | **CP-1:** OPNsense reachable on each VLAN; DHCP and DNS answer on a test port | Yes |
| 20:00 | Move the default gateway and DHCP to OPNsense; WAN to OPNsense | IT administrator | **CP-2:** internet from STAFF and SERVERS (T-1), DNS (T-4) | **Yes** (re-point the gateway to the old router; about 10 min) |
| 20:30 | Start the cloudflared connectors; enable the edge policies for the three apps | IT administrator | **CP-3:** staff test user reaches the apps (T-5) | Yes: disable the edge policies |
| 21:00 | Close the old port-forwards (Proxmox page, file service) | IT administrator | **CP-4:** external scan (T-8) | Yes: re-create the forwards |
| 21:20 | Enable Tailscale and WireGuard break-glass; remove the old admin exposure | IT administrator, IT partner | **CP-5:** T-6, T-7 | Yes |
| 21:45 | Run T-2, T-3, T-10; compare with the rule matrix | Architect | **CP-6:** all checks pass | Yes |
| 22:15 | Decide: **stay on the new platform** (Go-confirm) or roll back | Managing director | Decision recorded | Last easy decision point |
| 22:30 | Announce completion; record deviations and open issues | Architect | Log saved | — |
| 23:00 | End of window | | | |

**Float:** 30 minutes between steps and the end of the window were left on purpose; the rehearsal
took 2 h 40 min for the same steps.

## 6. Rollback and point of no return

**Rollback procedure (until CP-6):**

1. Announce the rollback decision (managing director).
2. Re-point the default gateway and DHCP to the old router (about 10 minutes).
3. Re-create the old port-forwards if needed; disable edge policies; stop the cloudflared connectors.
4. Revert switch VLANs if the network does not recover.
5. Confirm with the checks T-1 and T-4; inform staff.

**Total rollback time (rehearsed): about 35 minutes.**

**Point of no return:** there is none inside the window **by design**. The old router configuration
is exported and the router stays installed, powered and **unchanged for 14 days** (until the end of hypercare). The
clean-up (factory reset, removal) happens only after the exit criteria of hypercare are met. A
cutover whose last step destroys the fallback has no real rollback.

## 7. Communication

| When | Audience | Message |
|------|----------|---------|
| T−7 days | All staff | Date, time, what changes, what to do on Monday |
| T−1 day | All staff | Reminder; Wi-Fi off 19:00–22:00; support contact |
| During | MD, IT partner | Messages at each checkpoint |
| T+0 | All staff | "Done" and what to do if something fails |
| Monday 08:00 | IT administrator on site | First-day support, extended hours until Wednesday |
