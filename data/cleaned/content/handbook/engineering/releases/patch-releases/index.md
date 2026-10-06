---
title: "Patch Releases"
---

## Patch Release Policy

Patch releases follow [semantic versioning](https://semver.org/): **patch versions contain bug fixes only and are safe to auto-upgrade**. Many customers apply patch releases with minimal testing because they trust this guarantee.

### What Patch Releases Include

- Bug and security fixes per the [maintenance policy](https://docs.gitlab.com/policy/maintenance/)
- Performance regressions fixes

### What Patch Releases Do NOT Include

- New features or feature flag enables
- Incomplete work that "needs to ship"
- Changes requested due to missed monthly release deadlines

This policy exists to protect customers. It is not negotiable based on business pressure. For the general release policy framework including ownership, exception process, and escalation paths, see the [Release Policy](/handbook/engineering/releases/#release-policy) section.

### Why Features Cannot Be Backported

Beyond the [semantic versioning contract](/handbook/engineering/releases#release-policy), there is a practical engineering reason why features must not be included in patch releases: **backporting becomes unreliable when stable branches diverge from the default branch**.

When features are introduced to patch releases:

- New bug fixes can be inadvertently introduced into stable versions, increasing the risk of customers encountering new bugs in production environments they believed were stabilized.
- Customer trust erodes, they can no longer confidently plan upgrades or depend on our release commitments, making them hesitant to adopt updates even when they contain critical fixes.
- Stable branches diverge from the default branch in unpredictable ways
- Future bug fixes may not cherry-pick cleanly because the surrounding code
  differs
- Engineers must manually adapt fixes for each version, increasing risk of
  errors
- What should be a routine backport becomes a custom development effort

This creates a compounding problem: each feature exception makes subsequent backports harder, slower, and more error-prone.
The maintenance burden grows with each policy violation, ultimately affecting our ability to deliver timely security and bug fixes to all customers.

## Patch Release Overview

Patch releases are performed according to the [GitLab Maintenance Policy](https://docs.gitlab.com/ee/policy/maintenance.html)
in order to backport bug fixes and security fixes to the [maintained versions](https://docs.gitlab.com/policy/maintenance/#maintained-versions).

### Relationship to Other Release Types

Patch releases build on the stable branches created during [monthly releases](/handbook/engineering/releases/monthly-releases/):

- Fixes must first be deployed to GitLab.com before inclusion in a patch release
- Backports target the stable branches for [maintained versions](https://docs.gitlab.com/policy/maintenance/#maintained-versions)
- Security fixes included in patch releases may also be delivered earlier to GitLab Dedicated via [internal releases](/handbook/engineering/releases/internal-releases/)

Patches that are outside of our maintenance policy must be requested and agreed upon by the Release Managers and the requester (see [backporting to versions outside the maintenance policy](https://docs.gitlab.com/ee/policy/maintenance.html#backporting-to-older-releases) for details). Refer to the [list of maintained versions](https://docs.gitlab.com/policy/maintenance/#maintained-versions).

Patch releases are prepared in parallel with regular GitLab.com deployments so that continuous deployment is not blocked. In this way we can apply security fixes to GitLab.com instances before the public release.

If you're a GitLab engineer looking to:

- Include a security fix in a patch release, please follow the steps on the [security runbook for GitLab engineers](https://gitlab.com/gitlab-org/release/docs/-/blob/master/general/security/readme.md#security-guides-by-role).
- Include a bug fix in a patch release, please follow the steps on the [patch release runbook for GitLab engineers](https://gitlab.com/gitlab-org/release/docs/-/blob/master/general/patch/engineers.md). Security vulnerabilities in GitLab and its dependencies are to be addressed following the [Security Remediation SLAs](/handbook/security/product-security/vulnerability-management/sla/).

Bug fixes are worked on in the GitLab canonical repositories, while security fixes are worked on in the mirrored GitLab
security repositories to avoid revealing vulnerabilities before the release. An exception is dependency-only version bumps that remediate vulnerabilities already covered by a public CVE or vendor advisory. These can be implemented in the canonical repositories when they follow the [dependency version bumps](/handbook/security/product-security/security-platforms-architecture/application-security/vulnerability-management#dependency-version-bumps) guidance in the Application Vulnerability Management Procedure.

For GitLab team members looking to prepare backports, refer to the [Patch release information dashboard](#patch-release-information-dashboard).

## Patch release cadence

Patch releases are scheduled twice a month, targeting the Wednesdays before and after the [monthly release](/handbook/engineering/releases/monthly-releases/#monthly-release-schedule) (third Thursday). Exact dates vary each month and are best-effort targets that may shift based on operational needs.

For upcoming patch release dates, check the [Release Information dashboard](https://dashboards.gitlab.net/d/delivery-release_info/delivery3a-release-information?orgId=1) (internal).

### SLO Commitments

Scheduled patch releases are designed to meet target release dates without requiring emergency releases.

- For detailed security vulnerability remediation SLAs, see [Security Remediation SLAs](/handbook/security/product-security/vulnerability-management/sla/).
- For detailed bug vulnerability remediation SLAs, see [Bug Remediation SLAs](/handbook/product-development/how-we-work/issue-triage/#severity-slos).

## Patch release types

At GitLab, there are two types of patch releases processes:

1. **Scheduled (default)**: An SLO-driven patch to publish all available bug and vulnerability fixes per
   the [GitLab maintenance policy](https://docs.gitlab.com/ee/policy/maintenance.html). Scheduled twice a month on
   the Wednesday before and after the [monthly release week](/handbook/engineering/releases/monthly-releases/#monthly-release-schedule), planned patches comply
   with the [bug SLO](/handbook/product-development/how-we-work/issue-triage/#severity-slos) and
   the [security remediation SLAs](/handbook/security/product-security/vulnerability-management/sla/). Patches that include
   [`critical` vulnerabilities](/handbook/security/product-security/vulnerability-management/sla/) are considered critical patches.
1. **Out-of-band**: A patch outside of the regular [patch release cadence](#patch-release-cadence)
   reserved strictly for mitigating a high-severity bug or critical vulnerability. Out-of-band patches
   must never be used to accommodate missed deadlines or bypass standard release policy, and are delivered
   on Wednesdays, following the regular patch release cadence.

   All out-of-band patches, whether for bug fixes or security vulnerabilities, must satisfy the
   following, with no exceptions:

   - **Exception process**: An [exception request](/handbook/engineering/releases#exception-process)
     is **mandatory** before any out-of-band patch is executed. Release Managers are authorized to
     decline requests that haven't completed this process, regardless of business pressure.
   - **Incident declaration**: An [incident must be declared](/handbook/engineering/infrastructure-platforms/incident-management/#reporting-an-incident)
     with the following attributes:
     - Marked as "Out-of-Band Patch"
     - Severity S1 or S2
     - A Contributing Factor of 'Inadequate testing or QA' or 'Miscommunication or coordination gap'
   - **Incident review**: For out-of-band patches addressing **bug fixes**, completing an
     [incident review](/handbook/engineering/infrastructure-platforms/incident-review/) is
     **mandatory** to uphold the reliability and availability of the GitLab platform. For
     out-of-band patches addressing **security vulnerabilities**, participating in the SIRT
     incident retrospective issue is strongly encouraged instead.
   - **FCL**: An [FCL](/handbook/engineering/#feature-change-locks) is required for out-of-band
     patches addressing **bug fixes**. Does not apply to security vulnerabilities, which are
     instead reviewed by PSIRT at the overall security incident level.

Additionally, a [security RCA](/handbook/security/root-cause-analysis/) is **required**, with no
exceptions, when a **critical security vulnerability** is tied to a product feature and code
owned by an engineering team, including vulnerabilities in upstream third-party code when a
GitLab decision or delay, such as not applying an available fix promptly or relying on an
end-of-life dependency, contributed to the exposure. The team responsible must complete the
RCA. Otherwise, RCA is optional.

## Patch release process

The process for a patch release is the same for all types with one important distinction: scheduled patches include all bug and security fixes ready at the time
of the patch release preparation, while out-of-band patches will likely only include the fix for high-severity bug or critical vulnerability.

The end-to-end patch release process consists of the following stages:

![patch release overview](/images/engineering/releases/patch-releases/patch-release-overview.jpg)

- [Diagram source - internal](https://docs.google.com/presentation/d/12JXlLnZ8lQp7ATdaSoL4x_oCUv04rmqzYp6dQb8AXHE/edit#slide=id.g2d0bc50ab08_0_5)

At any given time, GitLab Engineers prepare bug fixes and vulnerability fixes to
the respective [maintained versions](https://docs.gitlab.com/policy/maintenance/#maintained-versions):

- **Step 1a: Bug fix prepared** - Merge requests backporting a bug fix to the
[maintained version](https://docs.gitlab.com/policy/maintenance/#maintained-versions) are prepared by GitLab engineers:
  - The merge requests execute end-to-end tests via test-on-omnibus pipeline to guarantee the bug fix meets the quality standards.
  - If the test-on-omnibus pipeline fails, a review from the [Developer Experience](/handbook/engineering/infrastructure-platforms/developer-experience/) team is required.
  - The merge requests are merged by a GitLab maintainer in the stable branch associated to the [maintained version](https://docs.gitlab.com/policy/maintenance/#maintained-versions).
- **Step 1b: Vulnerability fix prepared** - Engineers fix vulnerabilities in the relevant [Security repository](https://gitlab.com/gitlab-org/security). A fix is considered complete only when it has a [security implementation issue](https://gitlab.com/gitlab-org/release/docs/-/blob/master/general/security/terminology.md) with the following:
  - All checkboxes checked to show all steps have been completed.
  - A PSIRT team member and Maintainer approved MR targeting the default branch.
  - A backport MR for each intended version. In most cases this will mean 4 MRs to cover each supported version. Each MR must have passing pipelines, required approvals and be assigned to the release bot for processing.
  - The `~"security-target"` label is applied. This will automatically review the issue and link it to the security tracking issue if it is ready.

Two days before the planned due date, Release Managers start the patch release process, they make sure that
all prepared bug and security fixes are safely released. Deployments to GitLab.com run in parallel.

A patch release has the following phases:

- **Step 2: First steps** Release preparation begins when Release Managers run the `prepare` chatops command to create the new release task issue to guide the patch release. From here they follow the checklist to complete the initial set up and communication issues needed to prepare the release.
- **Step 3: Early Merge Phase** - Release Managers deploy security fixes to GitLab.com. Fixes with the `~"security-target"` label that are linked to the security tracking issue will have the MR targeting the default branch merged. This allows fixes to be deployed to GitLab.com before they are released to self-managed users.
- **Step 4: Merge backports** - The day before the release due date, backports with security fixes targeting the supported versions are merged. At this point, everything included in the patch must be deployed to GitLab.com, and backports must apply to all stable branches.
- **Step 5: Release preparation*** -  When all fixes are deployed and merge, Release Managers prepare and test the packages.
  - **Step 5a: Tag** - Release Managers tag new patch release packages for the [maintained versions](https://docs.gitlab.com/policy/maintenance/#maintained-versions).
  - **Step 5b: Deploy** - The patch release package is deployed and tested to the GitLab release instance.
  - **Step 5c: Release** - Release Managers publish the packages associated with the patch release.
- **Step 6: Final steps** - At this point patch release packages are available to all users. Release Managers wrap up the final steps of the patch release.
  - **Step 6a**: Patch release blog post is published
  - **Step 6b**: Default branches, stable branches, and tags are synced from Security to Canonical to return to our default state of working in the open.

## Patch release information dashboard

GitLab team members can view the [internal Grafana dashboard "Release Information"](https://dashboards.gitlab.net/d/delivery-release_info/delivery3a-release-information?orgId=1) for the following information about the upcoming patch release:

- Upcoming patch release versions (stable version + 2 backport versions)
- Upcoming patch release date
- Current status of the patch release
  - Open: Unmerged security MRs associated with security issues labeled `security-target`, as well as merged bug fix MRs,
  are expected to be included in the next patch release.
  - Warning: Signals that teams should get bug and security fixes ready to merge.
  - Closed: Default branch security MRs have been merged, no further bug or security fixes will be included.

The metrics used to display this information are updated automatically throughout the [patch release process](#patch-release-process).

## Patch release FAQs

### How can I backport a bug fix to the next patch release?

If you're a GitLab engineer looking to include a bug fix in a patch release, please follow the steps on the [patch release runbook for GitLab engineers](https://gitlab.com/gitlab-org/release/docs/-/blob/master/general/patch/engineers.md).

### Where can I find the next patch release information?

Patch release information, including targeted versions, scheduled date and status can be found on the internal Grafana [release dashboard](https://dashboards.gitlab.net/d/delivery-release_info/delivery3a-release-information?orgId=1)

### A security issue was assigned to me, where should I start?

See the [Security process as Engineer](https://gitlab.com/gitlab-org/release/docs/-/blob/master/general/security/engineer.md) documentation for more information.

### Why wasn't my security fix included in the Patch Release?

Security issues created on [GitLab Security](https://gitlab.com/gitlab-org/security/) need to be associated with the Security Tracking issue for them to be included on the Security
Release. Make sure to use the [security issue template](https://gitlab.com/gitlab-org/gitlab/-/blob/master/.gitlab/issue_templates/Security%20developer%20workflow.md) and follow the listed steps.

### How many backports do I need when working on a security issue?

Besides the merge request targeting `master`, backports will be needed targeting the stable branches for the respective [maintained versions](https://docs.gitlab.com/policy/maintenance/#maintained-versions).
For more information, see [security backports](https://gitlab.com/gitlab-org/release/docs/-/blob/master/general/security/engineer.md#backports).

### How can I revert a security merge request?

Reverting a merged security merge request is **strongly discouraged** and requires explicit approval from the [PSIRT team](/handbook/security/product-security/psirt/). Rollback of a security fix has serious consequences:

1. It compromises the integrity of GitLab.com, self-managed and Dedicated instances by removing a live security protection
1. Reverting without a replacement fix risks publicly disclosing the vulnerability the moment the release goes out. This is unacceptable
1. Patch releases operate under strict time constraints; preparing a replacement fix in time to avoid delaying the release is not guaranteed

If a security vulnerability introduced a secondary bug, the response depends on its severity:

- **Non-vulnerability bug (S3 and S4)**: The appropriate path is to fix the issue in the canonical repository after the patch release has been published, following the normal patch release process.
- **Non-vulnerability bug (high severity: S1 and S2)**: Engage immediately with PSIRT and Release Managers to coordinate next steps. Do not attempt to revert unilaterally.

Regardless of whether the security fix has been published, any revert **must have explicit written approval from the [PSIRT team](/handbook/security/product-security/psirt/)** before proceeding. For mitigation options and step-by-step guidance, see the [How to Mitigate Bugs Introduced by Security Merge Request](https://gitlab.com/gitlab-org/release/docs/-/blob/master/general/security/bugs_introduced_by_security_merge_request.md) runbook.
