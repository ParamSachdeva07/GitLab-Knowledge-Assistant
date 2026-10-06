---
title: Okta Device Posture Checks - Android
---

GitLab uses Okta device posture checks to ensure Android devices meet minimum security requirements before accessing GitLab resources. If your device fails a posture check, you will be blocked from accessing GitLab until the issue is resolved. Follow the steps below for the specific check your device failed.

> **Note:** Steps may differ based on your device manufacturer, model, and Android version.

## OS version

Outdated operating systems contain unpatched vulnerabilities that can be exploited to compromise your device and the GitLab resources it accesses. GitLab requires a minimum Android version to ensure devices are protected by current security patches.

| Remediation |
|-------------|
| 1. Navigate to **Settings**. <br>2. Select **System**. <br>3. Choose **Software update** or **System update** (varies by manufacturer). <br>4. Tap **Download and install** if available. <br>5. Your device will restart automatically once complete. <br><br> **Note:** Some devices have a separate app for checking updates. |

## Lock screen

Without a lock screen, anyone with physical access to your device can access GitLab data. A lock screen ensures that only you can unlock and use the device.

| Remediation |
|-------------|
| 1. Open **Settings**. <br>2. Tap **Security** or **Lock screen and security**. <br>3. Select **Screen lock** or **Screen lock type**. <br>4. Choose Pattern, PIN, or Password and complete the setup. <br>5. Configure auto-lock timing for additional protection. |

## Biometrics

Biometric authentication provides a stronger and more convenient second factor for unlocking your device. Combined with a lock screen, it reduces the risk of unauthorized access if your device is lost or stolen.

| Remediation |
|-------------|
| 1. Open **Settings**. <br>2. Tap **Security** or **Lock screen and security**. <br>3. Tap **Biometrics** or **Biometric preferences**. <br>4. Enable your preferred biometric method (fingerprint or face unlock). <br>5. Return to **Lock screen and security** and set up a **Screen lock** if not already configured. <br>6. Re-enable biometrics for lock screen authentication. |

## Device encryption

Encryption protects the data stored on your device so that it cannot be read if the device is lost, stolen, or forensically examined. Without encryption, sensitive GitLab data on your device is accessible to anyone who can physically access the storage.

| Remediation |
|-------------|
| 1. Open **Settings**. <br>2. Navigate to **Security** or **Lock screen and security**. <br>3. Tap **Encrypt phone** or **Encrypt tablet**. <br>4. Enter your lock screen credentials if prompted. <br>5. Review the information and confirm. <br>6. Allow the process to complete — this may take an hour or more. <br>7. Enter your credentials to access the device once complete. |

## Rooted device

Rooting replaces the official Android OS with an unofficial version, removing security controls that verify device integrity. Rooted devices cannot be trusted to enforce the same protections as stock Android.

| Remediation |
|-------------|
| The only remediation is to reset your device to factory settings, which removes the unofficial OS and restores stock Android. <br><br> **Warning:** A factory reset will **erase all data on the device**. |

## Managed device

GitLab requires that org-owned android devices used to access Okta apps are enrolled in device management. This ensures security policies, configurations, and certificates are consistently applied.

| Remediation |
|-------------|
| If you are a GitLab team member, contact IT for enrollment instructions. |

{{% alert title="Note" color="Warning" %}}
Additional device requirements may be enforced beyond those listed on this page.
{{% /alert %}}

{{% alert title="Note" color="info" %}}
If you need assistance resolving a device posture check, please contact IT via the Compass app in Slack (type "Compass" in the top search bar to find it) or it-help@gitlab.com.
{{% /alert %}}
