---
title: "Internal Releases"
---

## Internal Release Policy

> [!IMPORTANT]
> All internal releases **require** a declared [incident](/handbook/engineering/infrastructure-platforms/incident-management/#reporting-an-incident)
> and a post-release [incident review](/handbook/engineering/infrastructure-platforms/incident-review/). **These are not optional**.
>
> Internal releases addressing critical bug fixes **additionally require** a [Feature Change Lock (FCL)](/handbook/engineering/#feature-change-locks) driven
> by the engineering team of the affected area.

Internal releases adhere to the same policy requirements as [patch releases](/handbook/engineering/releases/patch-releases/#patch-release-policy):
they are limited to critical bug fixes and security patches only. Internal releases do not contain new features, feature flag changes, or
incomplete work, nor may be used for testing purposes.

For the general release policy framework including ownership, exception process, and escalation paths, see the [Release Policy](/handbook/engineering/releases/#release-policy) section.

If the internal release is not the result of a security incident or another already declared incident, an [incident must be declared](/handbook/engineering/infrastructure-platforms/incident-management/#reporting-an-incident).

## Internal release overview

Internal releases are private GitLab releases for our single-tenant SaaS instances. They remediate high-severity issues
(S1 or S2) on Dedicated instances:

* As quickly and efficiently as on GitLab.com
  ([SLA driven](/handbook/security/product-security/vulnerability-management/sla/#vulnerability-management-slas-and-labels))
* Without disclosing vulnerabilities before a public patch release
* Without introducing version gaps in the public packages

Internal releases are performed according to a specific criteria:

* Address S1 or S2 issues (bug or security vulnerabilities) that impact GitLab Dedicated availability. Lower severity issues
should be addressed via patch release.
* Target the current minus one (N-1) and current minus two (N-2) GitLab versions.
* Deliver fixes through a private channel before public disclosure.

If you're looking to fix a high-severity issue on Dedicated instances, [request an internal release](https://gitlab.com/gitlab-org/release/tasks/-/work_items/new?description_template=Internal-Release-Request) and follow the steps in the [internal release runbook for GitLab engineers](https://gitlab.com/gitlab-org/release/docs/-/blob/master/general/internal-releases/engineers.md).

### Relationship to Other Release Types

Internal releases follow the same process as [patch releases](/handbook/engineering/releases/patch-releases/) but serve a different purpose:

* Both use stable branches created during [monthly releases](/handbook/engineering/releases/monthly-releases/)
* Internal releases deliver fixes to GitLab Dedicated *before* public patch releases
* After an internal release, the same fixes are included in the next scheduled patch release for all self-managed customers

### Timeline

Internal releases have two phases with different time characteristics:

| Phase | Duration | Notes |
|-------|----------|-------|
| **Request and approval** | Variable | Depends on issue severity validation, stakeholder availability, and fix readiness |
| **Execution** | ~8 hours | Once the internal release request has been approved, Release Managers can complete the release process |

The request phase includes:

* Issue detection and Dedicated severity assessment
* Stakeholder notification and alignment
* Fix development and validation on GitLab.com
* Backport preparation with passing pipelines

Only after these prerequisites are met can Release Managers begin the ~8 hour execution phase.

## Request process

> [!IMPORTANT]
> Every approved internal release for a **critical bug fix** requires a [Feature Change Lock (FCL)](/handbook/engineering/#feature-change-locks) and a post-release [incident review](/handbook/engineering/infrastructure-platforms/incident-review/). These are **not optional**. Every
> approved internal release for a **critical security vulnerability** strongly encourages participation in the post-release SIRT/PSIRT retrospective, and **requires** a [Root Cause Analysis (RCA)](/handbook/security/root-cause-analysis/) if the vulnerability is tied to a product feature, including vulnerabilities in upstream third-party code, when a GitLab decision or delay contributed to the exposure. There are no exceptions to the RCA requirement when it applies.

Internal releases are reserved for high-severity bugs or security vulnerabilities that impact Dedicated availability and cannot wait for the next scheduled patch release.

**Release Managers are authorized to decline requests that do not meet these criteria.** Pressure from Customer Success, Sales, or other teams does not constitute approval for an internal release.

**Requests are automatically rejected** if they target a version outside N-1 or N-2, or if the severity is S3 or lower.

If an internal release is necessary:

1. **Requestor** [opens an internal release request issue](https://gitlab.com/gitlab-org/release/tasks/-/work_items/new?description_template=Internal-Release-Request), documenting the Dedicated impact
   assessment and completing all required steps
1. **Requestor** contacts the **Engineering Manager** of the affected area, assigns them to the issue, and ensures they start the [Feature Change Lock (FCL)](/handbook/engineering/#feature-change-locks)
   process for bug fixes (**mandatory**).
1. **Dedicated Engineering Manager** (sponsor) provides written approval on the issue.
1. **[Software Delivery Engineering Leadership](/handbook/engineering/infrastructure-platforms/gitlab-delivery/delivery/#software-delivery-engineering-leadership)** (or above) provides written approval.
1. **Requestor** assigns the [active Release Managers](/handbook/engineering/releases/release-managers/) to the issue for final review and execution once all items above are complete.
1. **Post-release, for bug fixes:** [Incident review](/handbook/engineering/infrastructure-platforms/incident-review/) to investigate how this escaped detection before release (**mandatory**).
1. **Post-release, for security vulnerabilities:** Participation in the SIRT/PSIRT retrospective issue is **strongly encouraged**. If the vulnerability is tied to a product feature, the team responsible for introducing it must complete a [Root Cause Analysis (RCA)](/handbook/security/root-cause-analysis/). There are no exceptions to this requirement.
   * For vulnerabilities in upstream third-party code, RCA is required only if a GitLab decision or delay, such as not applying an available fix or relying on an end-of-life dependency, contributed to the exposure. Otherwise, RCA is optional.

Internal releases approved outside this process set precedent that undermines release stability and the reliability of GitLab Dedicated.

## Internal release process

An internal release moves through six phases, from initial identification to deployment.

![internal release overview](/images/engineering/releases/internal-releases/internal-release-overview.jpg)

* [Diagram source - internal](https://docs.google.com/presentation/d/1rI47asPEzIaAGZ6t4rQASv88jnJJ17y55k3yD9IVkVI/edit?usp=sharing)

1. **Request**: A high-severity issue is identified and a [request process](#request-process) starts. The trigger depends on the issue type:
   * **Security vulnerability**: The SIRT team investigates and confirms the issue is S1 or S2.
   * **Critical bug**: The Dedicated team reports a high-severity issue causing availability degradation.
2. **Prepare**: Once the request is approved, initial implementation steps begin and the
   [GitLab Dedicated Group](/handbook/engineering/infrastructure-platforms/gitlab-dedicated) is notified.
3. **GitLab.com remediation**: The team responsible for the vulnerability or bug prepares and merges the fix
   into the appropriate GitLab repositories, then ensure it is deployed to GitLab.com.
   For security vulnerabilities:
   * Only Release Managers can merge to the security repository.
   * The [PSIRT team](/handbook/security/product-security/psirt) validates the fix on GitLab.com before moving forward.
4. **Backports**: The responsible team prepares merge requests targeting the N-1 and N-2 stable branches.
   * Engineers ensure backports are reviewed and approved with green pipelines
   * Engineers merge the backports into the stable branches once they're ready.
   * For security vulnerabilities, only Release Managers can merge to the security repository.
5. **Release**: The internal CNG images and Omnibus packages are built and uploaded to the pre-release channel.
6. **Final Steps**: Roll out the internal release packages to GitLab single-tenant SaaS instances.
   * The GitLab Dedicated Group is notified.
   * A [Dedicated emergency maintenance](https://docs.gitlab.com/administration/dedicated/maintenance/#emergency-maintenance) process starts.
