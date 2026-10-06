---
title: Okta Verify
---

Okta Verify is a multifactor authentication (MFA) app. When you sign in to Okta or an Okta-protected application, Verify confirms that it's really you by requiring a second form of proof.

## What it does

Beyond MFA, Okta Verify enables [Okta Device Trust](https://internal.gitlab.com/handbook/security/corporate/tooling/okta/okta-device-security/) — it registers your device with Okta so that device posture checks (such as OS version, encryption, and screen lock) can be evaluated at sign-in. This allows GitLab to enforce access policies based on the security state of your device, not just your credentials.
