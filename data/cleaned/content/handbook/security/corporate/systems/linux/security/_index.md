---
title: Linux Desktop OS Security Standards
---

Linux is available as an alternative to macOS, but is not encouraged due to limited support. By choosing Linux, you accept full responsibility for maintaining your environment and understand that IT does not provide support. There is a #linux channel in Slack for exchanging tips and tricks, but it is not an official helpdesk resource.

**Ubuntu LTS (latest version) is the only approved Linux distribution.**

## Security Requirements

All Linux endpoints must meet the following security standards:

| Requirement | Details |
| :--- | :--- |
| **Fleet Enrollment** | Mandatory for all Linux endpoints |
| **EDR Agent** | CrowdStrike or SentinelOne (region-dependent) |
| **Full-Disk Encryption** | LUKS encryption required |
| **OS Version** | Ubuntu LTS (Latest) |
| **Security Patches** | Must be applied within 7 days of release |
| **User Account** | Must be a regular user account; use `sudo` for administrative actions |
| **YubiKey** | YubiKey 5 FIPS required for authentication |

For YubiKey setup, see the [ordering guide](/handbook/security/corporate/systems/yubikey/purchasing/) and [user guide](/handbook/security/corporate/systems/yubikey/2fa/).

Fleet is used to confirm security settings, verify encryption and firewall status, deploy the EDR solution, and enable remote wipe capability.
