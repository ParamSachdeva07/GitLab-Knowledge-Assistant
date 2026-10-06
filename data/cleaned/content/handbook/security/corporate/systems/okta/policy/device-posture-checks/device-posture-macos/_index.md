---
title: Okta Device Posture Checks - macOS
---

GitLab uses Okta device posture checks to ensure macOS devices meet minimum security requirements before accessing GitLab resources. If your device fails a posture check, you will be blocked from accessing GitLab until the issue is resolved. Follow the steps below for the specific check your device failed.

## OS version

Outdated operating systems contain unpatched vulnerabilities that can be exploited to compromise your device and the GitLab resources it accesses. GitLab requires a minimum macOS version to ensure devices are protected by current security patches.

| Remediation |
|-------------|
| 1. Ensure your Mac has a network connection and is plugged in or has sufficient battery. <br>2. From the Apple menu, go to **System Settings** → **General** → **Software Update**. <br>3. Click **Upgrade Now** if an update is available. <br>4. Follow any on-screen prompts to complete the update. |

## Lock screen

Without a lock screen password, anyone with physical access to your Mac can access GitLab data. A password ensures that only you can unlock and use the device.

| Remediation |
|-------------|
| 1. From the Apple menu, go to **System Settings** → **Users & Groups**. <br>2. Select your user account. <br>3. Click **Change Password** and follow the prompts to set a password. |

## Screen lock

Requiring a password after the screen saver begins ensures your device is automatically secured when left unattended, preventing unauthorized access to GitLab data.

| Remediation |
|-------------|
| 1. From the Apple menu, go to **System Settings** → **Lock Screen**. <br>2. Set **Require password after screen saver begins or display is turned off** to an appropriate interval (immediately is recommended). |

## Disk encryption (FileVault)

FileVault encrypts all data on your Mac's disk, ensuring it cannot be read if the device is lost, stolen, or forensically examined. Without encryption, sensitive GitLab data on your device is accessible to anyone who can access the storage.

| Remediation |
|-------------|
| 1. From the Apple menu, go to **System Settings** → **Privacy & Security** → **FileVault**. <br>2. Click **Turn On FileVault**. <br>3. Create and verify a recovery key when prompted, and store it securely. <br>4. Restart your Mac when prompted to begin encryption. <br><br> **Note:** Encryption duration varies by disk size and Mac speed. Your Mac can be used during the process. |

## Managed device

GitLab requires that devices used to access Okta apps are enrolled in device management. This ensures security policies, configurations, and certificates are consistently applied.

| Remediation |
|-------------|
| If you are a GitLab team member, contact IT for enrollment instructions. |

## Secure Enclave

Secure Enclave is a dedicated security chip built into Apple Silicon and Intel Macs with a T2 chip. GitLab requires it to ensure cryptographic operations and credentials are protected by hardware-level security. Older Mac hardware that predates this chip cannot meet this requirement.

| Remediation |
|-------------|
| Your Mac does not have a Secure Enclave chip and cannot meet this requirement. You will need to use a supported Mac. |

{{% alert title="Note" color="Warning" %}}
Additional device requirements may be enforced beyond those listed on this page.
{{% /alert %}}

{{% alert title="Note" color="info" %}}
If you need assistance resolving a device posture check, reach out to IT using Compass or email `it-help@gitlab.com`.
{{% /alert %}}
