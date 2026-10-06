---
title: Linux Desktop OS
---

Linux is available as an alternative to macOS for GitLab team members, but is not encouraged due to limited support. By choosing Linux, you accept full responsibility for maintaining your environment and understand that IT does not provide support. There is a `#linux` channel in Slack for exchanging tips and tricks, but it is not an official helpdesk resource.

## Approved Distribution

**Ubuntu LTS (latest version) is the only approved Linux distribution.** Dell is the only approved Linux laptop vendor. Ubuntu LTS is required to support the necessary software packages for remote management and EDR solutions.

## Requirements

All Linux endpoints must meet the following security and compliance standards:

| Requirement | Details |
| :--- | :--- |
| **Fleet Enrollment** | Mandatory for all Linux endpoints. [Enrollment instructions](https://internal.gitlab.com/handbook/security/corporate/tooling/fleet/#enrolling-in-fleet) (internal link) |
| **EDR Agent** | CrowdStrike or SentinelOne (region-dependent, installed automatically via Fleet) |
| **Full-Disk Encryption** | LUKS encryption required |
| **Firewall** | Must be enabled (`ufw`) |
| **OS Version** | Ubuntu LTS (Latest) |
| **Security Patches** | Must be applied within 7 days of release |
| **User Account** | Must be a regular user account; use `sudo` for administrative actions |
| **YubiKey** | YubiKey 5 FIPS required for authentication |

For YubiKey setup, see the [ordering guide](/handbook/security/corporate/systems/yubikey/purchasing/) and [user guide](/handbook/security/corporate/systems/yubikey/2fa/).

## EDR Requirements by Region

EDR deployment is required on all team member endpoint systems, including virtual machines. Docker containers are excluded from MDM/EDR enrollment requirements.

| EDR Solution | Regions |
| :--- | :--- |
| **SentinelOne** | Netherlands, Germany, Italy, Austria |
| **CrowdStrike** | All other regions |

**Note:** Virtual hosts on laptops must also have the EDR agent installed.

## Fleet Enrollment

Fleet is our osquery-based device management and visibility platform for Linux endpoints. It is used to:

- Confirm security settings
- Verify encryption and firewall status
- Deploy the EDR solution
- Enable remote wipe capability
- Provide real-time queries of device state
- Software inventory and vulnerability detection

All Linux endpoints must be enrolled in Fleet. Visit the [Fleet handbook page](https://internal.gitlab.com/handbook/security/corporate/tooling/fleet/) for enrollment instructions.

## Firewall

Linux machines use their built-in firewall (`ufw`), managed through Fleet. This differs from macOS and Windows devices which use the CrowdStrike integrated firewall.

## Your Responsibilities

As a Linux user, you are responsible for:

- Maintaining your Linux environment
- Applying security patches and version upgrades
- Ensuring compliance with all endpoint management policies
- Keeping your system enrolled in Fleet and running the required EDR agent

## Support

- **Slack Channel:** `#linux` - for tips and tricks (not official helpdesk)
- **Security Support:** `#security_help` - for Fleet and EDR assistance
- **EDR Help:** `#crowdstrike` or `#sentinelone` (depending on your region)

## Additional Resources

- [Linux Setup Guide](/handbook/security/corporate/systems/linux/setup/)
- [Linux Security Standards](/handbook/security/corporate/systems/linux/security/)
- [Linux Tools & Tips](/handbook/tools-and-tips/linux/)
- [Fleet Documentation](https://fleetdm.com/docs)
