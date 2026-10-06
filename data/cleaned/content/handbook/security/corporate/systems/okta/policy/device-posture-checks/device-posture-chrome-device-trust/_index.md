---
title: Okta Device Posture Checks - Chrome Device Trust
---

## What is Chrome Device Trust?

Chrome Device Trust is a Google Chrome security features that verifies the security posture of a device via the Chrome browser before granting access to protected applications. GitLab uses it as an additional layer of assurance on top of standard Okta device posture checks — rather than relying solely on device enrollment or OS-level signals, Chrome Device Trust collects real-time security signals directly from the Chrome browser at the point of authentication.

## How it works

When you sign in to a Okta-protected apps through Chrome, Okta requests device signals from the Chrome browser. Chrome collects and transmits signals back to Okta. Okta evaluates these signals against GitLab's device assurance policies and either grants access, requires additional authentication, or blocks access if the device does not meet requirements.

This happens transparently during the normal sign-in flow. There is no user action required if your device is compliant.

## Where it is enforced

Chrome Device Trust is only enforced on corporate-managed devices. Personal devices are not in scope.

| Platform | Device State | Enforced |
|----------|--------------|----------|
| macOS | Managed | ✅ |
| | Unmanaged | |
| Windows | Managed | ✅ |
| | Unmanaged | |
| Linux | Managed | |
| | Unmanaged | |
| iOS | Managed | |
| | Unmanaged | |
| Android | Managed | |
| | Unmanaged | |

## Incognito mode and embedded browsers

Chrome Device Trust does not support incognito (private browsing) mode. If you attempt to sign in to a app in an incognito window, you may see a remediation warning. You can dismiss this warning and continue — it is expected behavior and not a sign that your device is non-compliant. You must authenticate through a non-incognito window before the remediation deadline is reached.

The same is true for apps which use embedded browsers. If you attempt to sign in to a app in an incognito window, you may see a remediation warning. You can dismiss this warning and continue — it is expected behavior and not a sign that your device is non-compliant.

## Access from non-Chrome browsers

Accessing GitLab resources from a non-Chrome browser (such as Safari or Firefox) is still possible, but Chrome Device Trust signals cannot be collected from these browsers. You will receive a remediation warning during sign-in when accessing from a non-Chrome browser.

To avoid being blocked, you must authenticate at least once through a managed Chrome browser before your remediation deadline has passed. Failure to do so will result in access being restricted until Chrome Device Trust can be verified.

{{% alert title="Note" color="success" %}}
To support adoption of Chrome Device Trust and accommodate various user workstreams and business needed - a temporary automated 90-day exemption from Chrome Device Trust can be requested via [Lumos](https://app.lumosidentity.com/app_store?domainAppId=1719028).
{{% /alert %}}

{{% alert title="Note" color="info" %}}
If you need assistance resolving a device posture check, please contact IT via the Compass app in Slack (type "Compass" in the top search bar to find it) or it-help@gitlab.com.
{{% /alert %}}
