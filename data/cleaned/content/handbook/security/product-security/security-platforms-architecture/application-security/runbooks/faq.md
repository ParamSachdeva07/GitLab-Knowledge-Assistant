---
title: "AppSec Frequently Asked Questions"
description: "A curated list of the most frequently asked AppSec related questions"
---

This is a curated list of commonly asked questions related to Application Security. If you have a question that is not answered here or in the [handbook page](/handbook/security/product-security/security-platforms-architecture/application-security/) please reach out to the AppSec team in the `#security_help` Slack channel.

---

## What do I do if I accidentally opened a security MR in public ?

Check if the related confidential security issue has the label `~"security-fix-in-public"`. This label means that the security issue is [already accepted](/handbook/security/product-security/security-platforms-architecture/application-security/vulnerability-management/#fixing-in-public) to be addressed in public, so it is ok to have this MR in public. If it does not, escalate to SIRT via `/security` in Slack to have the MR and branch removed. Automation may already have flagged the MR and posted an internal note asking you to do this — the action is the same.

When you intentionally create a public MR that is a dependency-only fix for an already-public vulnerability, make this clear in the MR description and include a link to the public advisory, following the guidance in [Dependency version bumps](/handbook/security/product-security/security-platforms-architecture/application-security/vulnerability-management#dependency-version-bumps). This helps AppSec when the MR is picked up by our monitoring.

## I ran a scan on 3rd party images used by GitLab and found vulnerabilities on them. Can they be updated?

We do not maintain 3rd party images. As appropriate we will follow our [Disclosure Guidelines for Vulnerabilities in 3rd Party Software](https://about.gitlab.com/security/disclosure/#disclosure-guidelines-for-vulnerabilities-in-3rd-party-software), our [Vulnerability Management Policy](../vulnerability-management/), and our [Release and Maintenance Policy](https://docs.gitlab.com/ee/policy/maintenance.html).

## A customer wants to know if a GitLab vulnerability affects them, or if the score is accurate?

In release blog posts after `17.2.2` the CVSS (severity) score links to an explanation page.
It describes the components that make up the CVSS score and provides some _potential_ mitigations that might inform a customer as to how they might reduce the risk for their own organization.
For an example, see [AV:N/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:N](https://gitlab-com.gitlab.io/gl-security/product-security/appsec/cvss-calculator/explain#explain=CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:N).

When a release goes out the content in the blog post is all that GitLab can publicly disclose at that time.
Requests for more detail may be denied until the issue is made public.
Refer to our [Process for disclosing security issues](/handbook/security/engaging-with-security/#process-for-disclosing-security-issues).

---
