---
title: Okta Device Posture Checks - iOS
---

GitLab uses Okta device posture checks to ensure iOS devices meet minimum security requirements before accessing GitLab resources. If your device fails a posture check, you will be blocked from accessing GitLab until the issue is resolved. Follow the steps below for the specific check your device failed.

## OS version

Outdated operating systems contain unpatched vulnerabilities that can be exploited to compromise your device and the GitLab resources it accesses. GitLab requires a minimum iOS version to ensure devices are protected by current security patches.

| Remediation |
|-------------|
| 1. Ensure your device has network connectivity and sufficient battery, or is plugged in. <br>2. Go to **Settings** → **General** → **Software Update**. <br>3. Tap **Download and Install** if an update is available. <br>4. Once downloaded, tap **Install Now**. <br>5. Your device may restart with a progress indicator during the update. |

## Lock screen

Without a lock screen passcode, anyone with physical access to your device can access GitLab data. A passcode ensures that only you can unlock and use the device.

| Remediation |
|-------------|
| 1. Open **Settings**. <br>2. Tap **Face ID & Passcode** or **Touch ID & Passcode** (varies by device model). <br>3. Authenticate with your current passcode or biometric if prompted. <br>4. Tap **Turn Passcode On**. <br>5. Enter a 6-digit passcode, or tap **Passcode Options** to choose alphanumeric or 4-digit alternatives. <br>6. Re-enter the passcode to confirm. |

## Biometrics

Biometric authentication provides a stronger and more convenient way to secure your device. Combined with a passcode, it reduces the risk of unauthorized access if your device is lost or stolen.

| Remediation |
|-------------|
| 1. Open **Settings**. <br>2. Tap **Face ID & Passcode** or **Touch ID & Passcode**. <br>3. Authenticate with your existing passcode or biometric. <br>4. For Face ID: tap **Enroll Face** and follow the on-screen instructions. <br>5. For Touch ID: tap **Add a Fingerprint** and follow the scanning instructions. <br>6. Enable biometric unlock when prompted. |

## Device encryption

iOS encrypts all data on your device when a passcode is enabled. Encryption ensures that data cannot be read if the device is lost, stolen, or forensically examined.

| Remediation |
|-------------|
| iOS encryption is enabled automatically when a passcode is set. Follow the lock screen remediation steps above to set a passcode, which will enable encryption. |

## Jailbroken device

Jailbreaking replaces or modifies the official iOS OS, removing security controls that GitLab relies on to verify device integrity. Jailbroken devices cannot be trusted to enforce the same protections as stock iOS.

| Remediation |
|-------------|
| The only remediation is to reset your device to factory settings, which removes the unofficial OS modifications and restores stock iOS. <br><br> **Warning:** A factory reset will **erase all data on the device**. |

## Managed device

GitLab requires that org-owned iOS devices used to access Okta apps are enrolled in device management. This ensures security policies, configurations, and certificates are consistently applied.

| Remediation |
|-------------|
| If you are a GitLab team member, contact IT for enrollment instructions. |

{{% alert title="Note" color="Warning" %}}
Additional device requirements may be enforced beyond those listed on this page.
{{% /alert %}}

{{% alert title="Note" color="info" %}}
If you need assistance resolving a device posture check, please contact IT via the Compass app in Slack (type "Compass" in the top search bar to find it) or it-help@gitlab.com.
{{% /alert %}}
