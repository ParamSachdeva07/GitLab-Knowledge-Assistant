---
title: "Secure Code Review"
description: "How the Application Security team reviews code for security vulnerabilities at GitLab."
---

Secure code review is the practice of examining source code changes with a security focus — looking for exploitable vulnerabilities, logic flaws, and design issues before they reach production. At GitLab, the Application Security team performs secure code reviews as part of our [triage rotation](/handbook/security/product-security/security-platforms-architecture/application-security/runbooks/triage-rotation/), for smaller, ad-hoc MR reviews and as part of the broader [AppSec review process](/handbook/security/product-security/security-platforms-architecture/application-security/appsec-reviews/) and is actively investing in automation to extend that coverage.

## Approaches

### Automated MR Security Review

**This is the preferred method for AppSec's triage rotation / ad-hoc MR security reviews**

The AppSec team is running an experimental AI-driven security review flow that automatically reviews merge requests for security issues. The flow is triggered by mentioning a service account on an MR and runs a multi-step analysis without requiring a human AppSec engineer to initiate it.

See the [Automated MR Security Reviewer](automated-mr-reviewer/) page for full usage and setup details.

### Manual Reviews

Manual AppSec reviews are performed by Application Security engineers in two ways.

**Triage rotation reviews** are ad-hoc, unscheduled MR reviews. If you need a quick security look at an MR that does not warrant a full scheduled review, try our [Automated MR Security Reviewer](automated-mr-reviewer/) before contacting the AppSec engineer on the weekly [triage rotation](/handbook/security/product-security/security-platforms-architecture/application-security/runbooks/triage-rotation/). 

**Scheduled reviews** cover high-priority features, infrastructure changes, and other work submitted through the [AppSec review process](/handbook/security/product-security/security-platforms-architecture/application-security/appsec-reviews/). See the [AppSec Review Template Process](/handbook/security/product-security/security-platforms-architecture/application-security/runbooks/review-process/) for how those reviews are structured and documented.
