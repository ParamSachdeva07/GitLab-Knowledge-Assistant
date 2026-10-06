---
title: Triage Rotation
---

Application Security team members are alphabetically assigned as the
responsible individual (DRI) for incoming requests to the Application
Security team, typically for a weekly or fortnightly period.

### Who is on rotation?

Automation manages the scheduling and assignment of rotations:

- ["Who is on rotation now?"](https://gitlab.com/gitlab-com/gl-security/product-security/appsec/tooling/rotation-management/-/wikis/who-is-on-now)
- [Rotation Management FAQ & README](https://gitlab.com/gitlab-com/gl-security/product-security/appsec/tooling/rotation-management)
- [Holiday Coverage](/handbook/security/product-security/security-platforms-architecture/application-security/runbooks/holiday-coverage/)

### What are the rotations?

For any request to the Application Security team member during rotation, the [AppSec Triage Dashboard](https://triage-dashboard-2c1ad6.gitlab.io/) is the single-source-of-truth.

The following rotations are defined:

- (Weekly Assignment) Security Dashboard Review
  - Responsible for reviewing [security dashboards](/handbook/security/product-security/security-platforms-architecture/application-security/runbooks/security-dashboard-review/) on a best-effort level
- (Weekly Assignment) Triage Rotation (mentions and issues), by order of priority:
  - First responder to [JiHu Contribution pings](/handbook/finance/jihu-support/jihu-security-review-process/) that come up in the [AppSec Triage Dashboard](https://triage-dashboard-2c1ad6.gitlab.io/)
  - First responder to [merge requests which reference confidential issues](#triaging-merge-requests-that-reference-confidential-issues) in the [AppSec Triage Dashboard](https://triage-dashboard-2c1ad6.gitlab.io/). Most are handled automatically; any alert still open in the dashboard needs action.
  - First responder to mentions of the following group aliases:
    - @gitlab-com/gl-security/product-security/appsec on GitLab.com. These mentions appear as "Ping Triage SLA" items in the [AppSec Triage Dashboard](https://triage-dashboard-2c1ad6.gitlab.io/)
      - PSIRT and/or SIRT are responsible for addressing external reports of a product vulnerability or customer exploit. See [Hand-off to PSIRT/SIRT during triage rotation](#hand-off-to-psirtsirt-during-triage-rotation)
    - @appsec-team in Slack
  - First responder to mentions from the custom SAST bot:
    - All merge requests with the [`~appsec-sast-ping::unresolved` label](https://gitlab.com/groups/gitlab-org/-/merge_requests?label_name%5B%5D=appsec-sast-ping%3A%3Aunresolved) must be reviewed. These appear as "Custom SAST Reports" in the [AppSec Triage Dashboard](https://triage-dashboard-2c1ad6.gitlab.io/)
    - Apply the `~appsec-sast-ping::resolved` label once the bot's findings have been resolved.
    - A dashboard with all the bot's findings can be found [here](https://gitlab.com/gitlab-com/gl-security/product-security/appsec/sast-custom-rules/-/issues/80).
  - First responder to any [Dependency Reviews](/handbook/security/product-security/security-platforms-architecture/application-security/runbooks/dependency-review-guidelines/) showing up in the [AppSec Triage Dashboard](https://triage-dashboard-2c1ad6.gitlab.io/)

- (~Fortnightly Assignment) Security Engineer for [Security & Patch Releases](https://about.gitlab.com/releases/#patch-releases)
- (Fortnightly Assignment, Federal AppSec only) Release Certifications
  - Responsible for the [release certification process](/handbook/finance/jihu-support/release-certification/)
  - This applies to any release that might have JiHu contributions, including monthly and patch releases
- (Quarterly Assignment) AppSec Blog Post

If the Application Security team member has a conflict for the assigned week
they may swap rotation weeks with another team member. This may be done for
any reason including time off or the need for time to focus on a particular task.

Team members should not be assigned on weeks they are responsible for the
scheduled security release.

Team members not assigned as the DRI for the week should continue to triage
reports when possible, especially to close duplicates or handle related reports
to those they have already triaged.

Team members remain responsible for their own assigned reports.

### Triage SLA policies

Without clear SLA targets, requesters don't know when to expect a response, and the AppSec team lacks visibility into which requests are becoming urgent. This results in inefficient communication patterns, duplicate follow-ups, and difficulty prioritizing work based on how long requests have been waiting. Establishing formal SLAs creates transparency for both requesters and the AppSec team, reduces ad-hoc interruptions, and ensures timely responses while providing clear escalation paths when needed.

#### SLA Targets

| Resource Type | Response SLA | Resolution SLA |
|---------------|--------------|----------------|
| Issues        | 4 business days | N/A (issues are tracked for response only) |
| Merge Requests| 2 business days | 5 business days |

#### Issues

**How the bot works:**

When someone pings AppSec (`@gitlab-com/gl-security/product-security/appsec` or `@gitlab-com/gl-security/appsec`) in an issue:

1. The bot automatically responds to acknowledge the ping
2. Adds labels: `~AppSecResponseSLA::pinged`, `~AppSecWorkflow::new`, `~Application Security Team`
3. Starts tracking the 4-day response SLA

**SLA tracking timeline:**

- **Day 2**: Bot adds `~AppSecResponseSLA::at-risk` warning label and posts a reminder
- **Day 3**: Bot adds `~AppSecResponseSLA::near-breach` warning label with urgent notification
- **Day 4**: Bot adds `~AppSecResponseSLA::breached` label and escalates to leadership
- **Weekly**: Bot posts reminders every 7 days after breach

**What you need to do:**

1. When you begin working on the issue, apply one of these labels:
   - `~AppSecWorkflow::planned` - if scheduled for later
   - `~AppSecWorkflow::in-progress` - if actively working on it
2. When complete, apply `~AppSecWorkflow::complete`
3. The bot will automatically update SLA tracking labels based on your workflow updates

#### Merge Requests

**How the bot works:**

When someone pings AppSec in a merge request:

1. The bot automatically responds to acknowledge the ping
2. Adds labels: `~AppSecResponseSLA::pinged`, `~AppSecWorkflow::new`, `~Application Security Team`
3. Starts tracking both response and resolution SLAs

##### Response SLA (2 business days)

**Timeline:**

- **Day 1**: Bot adds `~AppSecResponseSLA::near-breach` warning label
- **Day 2**: Bot adds `~AppSecResponseSLA::breached` warning label and escalates to leadership
- **Weekly**: Bot posts reminders every 7 days after breach

**How to meet the Response SLA:**

Apply one of these workflow labels within 2 business days:

- `~AppSecWorkflow::planned` - if you've reviewed and scheduled it for later
- `~AppSecWorkflow::in-progress` - if you're actively reviewing
- `~AppSecWorkflow::complete` - if review is already done

Once you apply any of these labels:

- The bot stops the response SLA timer
- The bot adds `~AppSecResponseSLA::completed-within-sla` (if not breached)
- For `planned` or `in-progress` labels, the resolution SLA timer begins

##### Resolution SLA (5 business days from when work begins)

**Timeline (starts when `planned` or `in-progress` is applied):**

- **Day 3**: Bot adds `~AppSecResolutionSLA::at-risk` warning label
- **Day 4**: Bot adds `~AppSecResolutionSLA::near-breach` warning label with urgent notification
- **Day 5**: Bot adds `~AppSecResolutionSLA::breached` label and escalates to leadership
- **Weekly**: Bot posts reminders every 7 days after breach

**How to meet the Resolution SLA:**

Complete your review and apply `~AppSecWorkflow::complete` within 5 business days of starting work.

Once you apply the complete label:

- The bot stops the resolution SLA timer
- The bot adds `~AppSecResolutionSLA::completed-within-sla` (if not breached)
- All warning labels (`at-risk`, `near-breach`) are removed

**Important notes:**

- Business days exclude weekends
- Breached labels remain for visibility to leadership
- You can add `~AppSecSLA::ignore` to exclude items from SLA tracking
- The bot will not trigger if an AppSec team member pings the team

### Triaging merge requests that reference confidential issues

Merge requests which reference confidential issues are surfaced in the [AppSec Triage Dashboard](https://triage-dashboard-2c1ad6.gitlab.io/). A work item is created for each alert in the [issue tracker](https://gitlab.com/gitlab-com/gl-security/product-security/appsec/triage-dashboard/-/issues?sort=created_date&state=opened&label_name%5B%5D=pmrcid-alert&label_name%5B%5D=AppSecWorkType%3A%3ATriageRotation&first_page_size=20), with an AI assessment posted as a comment. The automation auto-closes high-confidence verdicts and labels them `~pmrcid-auto-closed`: high-confidence SAFE (for example, a dependency bump) needs no action, and high-confidence UNSAFE notifies the merge request author via an internal note to escalate to SIRT and auto-closes once the merge request is removed. Review auto-closed alerts occasionally on a best-effort basis to confirm the automation is behaving; if too many alerts still need manual triage, the thresholds can be tuned. Closed alerts won't show up on the dashboard, and no human review is normally needed.

**Any alert still open in the dashboard needs action.** Use the AI assessment as a starting point:

1. Close the alert if the merge request can be public (comment any rationale in the work item and assign the `appsec-mrcid-automation` feedback label).
1. If it references a legitimate security issue and the referenced confidential issue has a `~security-fix-in-public` label, indicating it [has been approved by an AppSec team member to be fixed in public](/handbook/security/product-security/security-platforms-architecture/application-security/vulnerability-management#fixing-in-public), link to the comment granting approval (or note in the work item that the label was added). You may also decide it can be public and apply `~security-fix-in-public` retrospectively; fixing in public is acceptable when [behind a feature flag disabled by default](/handbook/security/product-security/psirt/runbooks/hackerone-process/#triaging-features-behind-a-feature-flag). Otherwise, post `/security` in Slack so [SIRT can remove the MR](/handbook/security/product-security/psirt/runbooks/unintended-vuln-disclosure/) from public view (use the `Urgent - SEOC should be paged right away` option if waiting up to 24 hours for a resolution would be too long).
1. An open alert labelled `~"SIRT::Escalation"` means the MR author was asked to escalate (via the internal note) but the target MR has not been removed (yet). From here, AppSec drives it to resolution: review the alert, confirm with the MR author if needed, and post `/security` yourself depending on your investigation. If you instead judge the change is safe to keep public, record that on the work item rather than the public merge request.

### Hand-off to PSIRT/SIRT during triage rotation

When team members are assigned to Triage rotation and are first responder to mentions of @gitlab-com/gl-security/product-security/appsec on GitLab.com or @appsec-team in Slack, assess whether the ping is an external report of a product vulnerability or customer exploit. In these instances, hand off to @gitlab-com/gl-security/product-security/appsec/psirt-group and/or @gitlab-sirt.

Direct reports from customers of vulnerabilities found during container scans to the Vulnerability Mangement team.

### Triaging exposed secrets

Exposure of information and secrets is handled a little differently to vulnerabilities, as there is nothing to patch and therefore no need for a GitLab Project Issue, CVSS, or CVE. When you're pinged during your rotation and you see a leaked secret, follow the process described on the [HackerOne runbook](/handbook/security/product-security/psirt/runbooks/hackerone-process/#triaging-exposed-secrets)
