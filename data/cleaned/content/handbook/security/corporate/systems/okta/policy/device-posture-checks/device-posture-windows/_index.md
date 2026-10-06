---
title: Okta Device Posture Checks - Windows
---

GitLab uses Okta device posture checks to ensure Windows devices meet minimum security requirements before accessing GitLab resources. If your device fails a posture check, you will be blocked from accessing GitLab until the issue is resolved. Follow the steps below for the specific check your device failed.

## OS version

Outdated operating systems contain unpatched vulnerabilities that can be exploited to compromise your device and the GitLab resources it accesses. GitLab requires a minimum Windows version to ensure devices are protected by current security patches.

| Remediation |
|-------------|
| **Windows 10:** <br>1. Go to **Start** → **Settings** → **Update & Security** → **Windows Update**. <br>2. Windows will automatically check for and download available updates. <br>3. Click **Restart now** once the download completes. <br><br> **Windows 11:** <br>1. Go to **Start** → **Settings** → **Windows Update**. <br>2. Click **Download and install** if updates are available. <br>3. Follow the on-screen instructions. Your device may restart multiple times. |

## Lock screen (Windows Hello)

Windows Hello secures your device with a PIN, fingerprint, or face recognition, ensuring only you can unlock it. Without it, anyone with physical access to your device can access GitLab data.

| Remediation |
|-------------|
| 1. Go to **Start** → **Settings** → **Accounts** → **Sign-in options**. <br>2. Under **Windows Hello**, click **Set up** next to your preferred method (PIN, fingerprint, or face). <br>3. Follow the on-screen instructions to complete setup. <br>4. For face recognition: position your face in front of the camera as directed. <br>5. For fingerprint: place your finger on the scanner multiple times until recognition is complete. |

## Screen lock

Requiring a password after the screen saver begins ensures your device is automatically secured when left unattended, preventing unauthorized access to GitLab data.

| Remediation |
|-------------|
| 1. Go to **Start** → **Settings** → **Personalization** → **Lock screen**. <br>2. Click **Screen saver settings**. <br>3. Set a screen saver and configure a short wait time. <br>4. Check **On resume, display logon screen**. <br>5. Click **OK**. |

## Disk encryption (BitLocker)

BitLocker encrypts all data on your device's disk, ensuring it cannot be read if the device is lost, stolen, or forensically examined. Without encryption, sensitive GitLab data on your device is accessible to anyone who can access the storage.

| Remediation |
|-------------|
| 1. Search for **Manage BitLocker** in the taskbar and open it. <br>2. Locate the drive to encrypt and click **Turn on BitLocker**. <br>3. Choose your unlock method (password or smart card). <br>4. Select where to save your recovery key and store it securely. <br>5. Choose whether to encrypt the entire drive or used space only. <br>6. Click **Start Encrypting**. <br><br> **Note:** Encryption duration varies by drive size. Your device can continue to be used during the process. |

## Trusted Platform Module (TPM)

TPM is a hardware security chip built into modern PCs that protects cryptographic keys and credentials at the hardware level. GitLab requires TPM to ensure device-level security operations cannot be tampered with. Older hardware that lacks a TPM chip cannot meet this requirement.

| Remediation |
|-------------|
| Your device does not have a supported TPM chip and cannot meet this requirement. You will need to use a supported device. Contact IT for assistance with a replacement. |

## Managed device

GitLab requires that devices used to access corporate resources are enrolled in device management. This ensures security policies, configurations, and certificates are consistently applied.

| Remediation |
|-------------|
| If you are a GitLab team member, contact IT for enrollment instructions. |

{{% alert title="Note" color="Warning" %}}
Additional device requirements may be enforced beyond those listed on this page.
{{% /alert %}}

{{% alert title="Note" color="info" %}}
If you need assistance resolving a device posture check, please contact IT via the Compass app in Slack (type "Compass" in the top search bar to find it) or it-help@gitlab.com.
{{% /alert %}}
