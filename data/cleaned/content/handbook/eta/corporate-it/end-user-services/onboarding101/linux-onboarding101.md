---
title: "GitLab Linux Onboarding 101"
---

## Welcome to the GitLab Linux Community

Linux is available as an alternative to macOS, but is not encouraged due to limited support. By choosing Linux, you accept full responsibility for maintaining your environment and understand that IT does not provide support.

We expect Linux users to be familiar with the platform and self-sufficient in setting up their work environments while staying compliant with our security policies. This guide addresses common issues encountered when setting up new machines.

>**NOTE**: We do not provide in-depth technical support for Linux, but we can assist with Okta login issues. The #linux Slack channel is available for exchanging tips and tricks, but it is not an official helpdesk resource.

## Table of Contents

1. [Before You Begin](#before-you-begin)
1. [Security Requirements](#security-requirements)
1. [Initial Installation and Disk Encryption](#initial-installation-and-disk-encryption)
1. [Initial Okta Login](#initial-okta-login)
1. [Device Management and Endpoint Security](#device-management-and-endpoint-security)
   1. [SentinelOne Installation - Germany, the Netherlands, Italy, and Austria Only](#sentinelone-installation---germany-the-netherlands-italy-and-austria-only)
1. [Additional Resources](#additional-resources)

## Before You Begin

To get set up on your new Linux laptop, you will need to have the following:

1. Your GitLab-provided Dell laptop
1. A boot-capable USB drive (At least 8GB)
1. An up-to-date iOS or Android device with a camera OR a YubiKey
1. The Okta activation email sent to your personal email on your first day

## Security Requirements

>**Note**: Ubuntu LTS (latest version) is the only approved Linux distribution. This ensures GitLab meets all regulatory and compliance standards, and Ubuntu has proven highly reliable for running the required security tools.

Before being able to log into Okta, the following security requirements must be met:

1. **Full-Disk Encryption:** LUKS encryption must be enabled
1. **Hostname:** The laptop's hostname must match our standard naming convention. See the [Linux Hostname Rename Script](https://gitlab.com/gitlab-com/gl-security/corp/engineering/corpsecdevices.gitlab.io/-/blob/main/docs/Tech_Stack/Fleet/Linux_Rename_Script.md) for instructions
1. **Fleet:** Device management must be installed
1. **EDR:** CrowdStrike Falcon or SentinelOne (Germany, the Netherlands, Italy, and Austria only) must be installed

## Initial Installation and Disk Encryption

The default version of Ubuntu that ships on Dell laptops does not have disk encryption enabled. Encrypting a disk after OS installation is not recommended and may cause issues. You will need to reinstall the OS with encryption enabled.

1. Download the latest Ubuntu LTS release [here](https://ubuntu.com/download/desktop)
1. Create a bootable USB drive using [balenaEtcher](https://etcher.balena.io/) or similar
1. Follow [this guide](https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview) to erase the disk and install a fresh copy of Ubuntu.
   1. Install third-party for graphics and Wi-Fi
   1. **Make sure to select `Use LVM and encryption` when prompted**
   1. Complete the installation and boot into your desktop
1. Enable the firewall:
   1. Open the terminal and run `sudo ufw status`
   1. If the response is `Status: inactive` run `sudo ufw enable`
   1. If ufw is not installed, run `sudo apt install ufw` first.
1. Update your system:
   1. Open the terminal and run `sudo apt update && sudo apt upgrade`
1. Enable fingerprint verification for fast logins - [Log in with a fingerprint](https://help.ubuntu.com/stable/ubuntu-help/session-fingerprint.html.en)
   1. Additional resources: [fprint](https://fprint.freedesktop.org/)

## Initial Okta Login

>**IMPORTANT**: As a new-hire, you will be able to perform your initial Okta login without all security requirements being met. However, all required steps must be completed on your first day or you will no longer be able log in.

Complete all required steps [here](/handbook/eta/corporate-it/end-user-services/onboarding101/#laptop-setup-linux) before continuing.

## Device Management and Endpoint Security

We utilize Fleet to manage all of our Linux devices. Fleet will enable you to access Okta, provides a central repository for some of our most commonly used applications (e.g. Zoom), and will let you know about any  potential security issues on your laptop.

Please use [this page](https://internal.gitlab.com/handbook/security/corporate/tooling/fleet/#enrolling-in-fleet) for the installation files and guide.

Enrolling your laptop in Fleet will also automatically install CrowdStrike Falcon on your machine unless you are based in Germany, the Netherlands, Italy, or Austria.

### SentinelOne Installation - Germany, the Netherlands, Italy, and Austria Only

As CrowdStrike has not yet been approved for the above regions, users there will need to manually install SentinelOne Endpoint security in addition to Fleet.

Please click [here](/handbook/security/corporate/systems/sentinelone/setup/) for the necessary files and set-up instructions.

## Additional Resources

- [Linux tools and tips](/handbook/tools-and-tips/linux/)
- [CrowdStrike - Endpoint Detection and Response](https://internal.gitlab.com/handbook/security/corporate/tooling/crowdstrike/)
- [YubiKey Self-Service Purchasing Guide](/handbook/security/corporate/systems/yubikey/purchasing/)
- [1Password for Linux](https://1password.com/downloads/linux)
- #linux in Slack for questions and discussions

## Need Help?

If you need further assistance with setting up your laptop please join our weekly onboarding call scheduled every Tuesday (Check your Calendar!) or please contact IT via the Compass app in Slack (type "Compass" in the top search bar to find it) or it-help@gitlab.com.
