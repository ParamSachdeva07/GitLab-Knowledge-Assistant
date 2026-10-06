---
title: "Application Security"
description: Application Security home page
---
<!-- markdownlint-disable MD052 -->
Last updated: May 27, 2025

## Application Security Mission

**The Product Application Security subdepartment works with GitLab engineers and product teams to anticipate and prevent the introduction of vulnerabilities during design and development, ensuring delivery of high quality software GitLab customers can trust. We also identify, assess, and respond to security vulnerabilities discovered in GitLab products and services that are reported through [Coordinated Vulnerability Disclosure practices](https://about.gitlab.com/security/disclosure/).**

## Value Proposition

The Application Security subdepartment provides operational application of DevSecOps engineering and methodology, as well as data insights and security consultation that enables GitLab engineers to easily deliver high quality secure products and services to customers, while maintaining feature capabilities and velocity to market.

## Scope & Responsibilities

We organize our work into five pillars that emphasize Developer UX in the context of traditional DevSecOps programs. We call this the Secure Developer eXperience, or SDX.

- **SDX: Learn**: security training, governance, policy, documentation, and standards.
- **SDX: Design**: [threat modeling](threat-modeling/_index.md), feature design guidance and consultation, and [design reviews](appsec-reviews.md).
- **SDX: Code**: static analysis, software component analysis and supply chain security, use of approved tools and methodologies in development, deprecation of unsafe functions, etc.
- **SDX: Verify**: dynamic analysis testing, penetration testing, remediation of critical vulnerabilities, and [final security reviews](appsec-reviews.md) prior to release.
- **SDX: Maintain**: establishment of an incident response plan, managing [Coordinated Vulnerability Disclosure](https://about.gitlab.com/security/disclosure/), [bug bounty program administration](https://hackerone.com/gitlab?type=team), and critical product security incident response [release](https://about.gitlab.com/releases/categories/releases/) and post-release operations.

The Application Security sub-department includes two teams, the [*Secure Design & Development Team*](appsec-operations/sdd-services.md) and the [*Product Security Incident Response Team (PSIRT)*](appsec-operations/psirt-services.md).

### Shared Accountabilities & Collaborations

The Application Security team partners with several other teams across the Security Division to deliver end-to-end security solutions that work for GitLab engineers. The following strategic security programs have multiple stakeholders across the Security Division and company.

#### Supply Chain Security

Application Security's accountability is shared by both [SD&D](appsec-operations/sdd-services.md) and [PSIRT](appsec-operations/psirt-services.md). Additional Product Security teams involved in Supply Chain Security include [Security Platforms & Architecture](../../security-platforms-architecture/), [Vulnerability Management](vulnerability-management.md), and [Infrastructure Security](../../infrastructure-security/).

#### Dogfooding

Application Security's accountability is to use GitLab security products in our work and be participants in providing actionable Customer Zero feedback through the [Security Platforms & Architecture team](../../security-platforms-architecture/), who is the Dogfooding DRI for Product Security.

#### Vulnerability Management

The Application Security Team's accountability is shared by both [SD&D](appsec-operations/sdd-services.md) and [PSIRT](appsec-operations/psirt-services.md). The [Vulnerability Management](../../vulnerability-management/) is DRI for Vuln Management tooling development and implementation.

#### Secure by design

The Secure Design and Development Team's accountability is feature focused, assessing threats through [Threat Modeling](threat-modeling/_index.md) and [feature design reviews](appsec-reviews.md). (SDX: Design). The [Security Platforms & Architecture team](../../security-platforms-architecture/) is DRI for Threat Modeling strategy company-wide, while AppSec is a critical stakeholder in this strategy.

#### Security Response

The [Product Security Incident Response Team's](appsec-operations/psirt-services.md) accountability is to triage and technically assesses critical and exploitable vulnerabilities, determine company and customer risk, and coordinate external communications regarding these issues.  PSIRT has several partners across the company including:

- [Security Operations](/handbook/security/security-operations/) is DRI for Incident Command and Threat Detection (IOCs, TTPs)
- [Security Research](/handbook/security/product-security/security-platforms-architecture/security-research/) is a key partner on exploitability and POC development
- [PR and Communications](/handbook/security/external-security-communications-procedure/)
- [Legal](/handbook/legal/)
- [Delivery](/handbook/engineering/infrastructure-platforms/gitlab-delivery/delivery/)
- [Customer Support Systems](/handbook/eta/css/)

## Out of Scope

- [SBOM production](/handbook/security/security-assurance/security-compliance/sbom-plan/)
- Container Scanning
- [Customer Escalations regarding security scanner findings](/handbook/security/product-security/vulnerability-management/customer-scan-review-requests.md)
- [Security Compliance](/handbook/security/security-assurance/)

## Application Security Organization

Review our [team organization](appsec-organization.md) to understand how we plan our work and which repositories we use daily.

## Contacting us

Team members can reach the AppSec team by:

- Mentioning `@gitlab-com/gl-security/product-security/appsec` on GitLab
- Submit an issue in the [AppSec Team repository](https://gitlab.com/gitlab-com/gl-security/product-security/appsec/appsec-team/-/issues)
- Asking in `#security_help` or mentioning `@appsec-team` on Slack
- For cross team collaboration improvement opportunities, use [this template for collaboration improvement opportunities](https://gitlab.com/gitlab-com/gl-security/product-security/appsec/appsec-team/-/issues/new?issuable_template=cross-team-collaboration-improvement)

## FY26 Primary Focus Areas

In FY26, our key focus areas are:

**Organizational Upleveling:**

- Establish [Product Security Incident Response Team (PSIRT)](appsec-operations/psirt-services.md)
- Expand [Security Design & Development](appsec-operations/sdd-services.md) team services at scale

**Support Company and [Division](/handbook/security/) Priorities:**

- Authorization & Authentication
- AI Security & Safety
- Supply Chain security
- [Security Interlock](../../security-platforms-architecture/security-interlock/)

## FY26 Metrics

Application Security is rebuilding our operational business health metrics in FY26. These metrics are in addition to Key Risk Indicators, project-level metrics, or sub-team specific metrics. For many of these, metrics instrumentation and reporting mechanisms are still forthcoming. As the team matures, these metrics will evolve and be shared on this page.

## Useful resources for AppSec engineers

### PTO

Team members that are taking PTO for 5 days or more must both discuss time off with their manager prior to scheduling to ensure visibility and adequate team operational coverage [**and** create a PTO coverage issue](https://gitlab.com/gitlab-com/gl-security/product-security/appsec/appsec-team/-/issues/new?issuable_template=pto_coverage) to organize their coverage during their time off. The PTO coverage issue should:

- List any potential requests that could come to the team while on PTO
- The team member taking PTO should organize their work accordingly and ensure the PTO coverage issue contains the context required to handle the work
- Assign primary and secondary responsible team members

AppSec team members should add any important information related to the work they are covering for the person on PTO and AppSec manager(s) should add any important announcement to see upon their return.

### Roles & Responsibilities

Please see the [Application Security Job Family page](/job-description-library/security/application-security).

### Helpful Quicklinks

- [The AppSec private group that contains other private subgroups and projects](https://gitlab.com/gitlab-com/gl-security/product-security/appsec)
- [The `appsec-lab` group on Staging. This has an Ultimate license.](https://staging.gitlab.com/appsec-lab)
- [Bug Bounty Council search](https://gitlab.com/gitlab-com/gl-security/product-security/appsec/bug-bounty-reviewers/bug-bounty-council/-/issues)
- [Bug Bounty Council archive (before November 2025)](https://gitlab.com/gitlab-com/gl-security/security-department-meta/-/issues?scope=all&state=opened&label_name[]=Bug+Bounty+Council)
- [Upcoming patch release](https://gitlab.com/gitlab-org/gitlab/-/issues?sort=created_date&state=opened&label_name%5B%5D=upcoming+security+release)
- [GitLab Project Security dashboard](https://gitlab.com/gitlab-org/gitlab/-/security/dashboard/?project_id=278964&scope=dismissed&page=1&days=90)
- [Security issue board that tracks ongoing issues (hackerone and others)](https://gitlab.com/groups/gitlab-org/-/boards/1216545?label_name[]=security)
- [The latest releases](https://gitlab.com/gitlab-org/gitlab/-/tags)
- [Overview of a project member permissions](https://gitlab.com/help/user/permissions)
- [The DevOps stages and their different groups](/handbook/product/categories/). This page contains information on the development teams, their areas of focus, and their team members.
- [The product features listed by groups that own them](/handbook/product/categories/features/)
- [List of merged security issues in `gitlab-org`](https://gitlab.com/groups/gitlab-org/-/merge_requests?scope=all&state=merged&label_name[]=security&milestone_title=%23upcoming). **Note:** It can include results from the security mirror `gitlab-org/security/`.
- [Application Security KPIs & Other Metrics Dashboard (internal)](https://10az.online.tableau.com/#/site/gitlab/views/appsectest2rawdata/AppSec-ApplicationandContainerVulnerabilityDashboard?:iid=4), including Embedded KPIs which can be filtered by section, stage, or group.

The list above is not exhaustive and is subject to be modified as our processes keep evolving.

## Key resources

- [Application Security Reviews](/handbook/security/product-security/security-platforms-architecture/application-security/appsec-reviews/)
- [Root Cause Analysis for Critical Vulnerabilities](/handbook/security/root-cause-analysis)
- [Application Security Engineer Runbooks index](runbooks)

## Backlog reviews

If a backlog review is necessary, follow the process defined in the [Vulnerability Management Procedure](/handbook/security/product-security/security-platforms-architecture/application-security/vulnerability-management/).

## GitLab Secure Tools coverage

As part of our [dogfooding effort](/handbook/product/product-processes/dogfooding-for-r-d/),
the [Application Security Tools](https://docs.gitlab.com/ee/user/application_security/) are set up on many different GitLab projects (see our [policies](/handbook/security/product-security/security-platforms-architecture/application-security/inventory/#policies)).
This list is too dynamic to be included in this page, and is now maintained in the [GitLab AppSec Inventory](/handbook/security/product-security/security-platforms-architecture/application-security/inventory/).

Projects without the expected configurations can be found in the [inventory violations list](https://gitlab.com/gitlab-com/gl-security/product-security/inventory/-/issues) (internal link).

## GitLab Inventory

Learn more about the [GitLab AppSec Inventory](/handbook/security/product-security/security-platforms-architecture/application-security/inventory/).

## Responding to customer scan review requests

The Vulnerability Management team now handles customer scan review requests. Refer to the [Customer Scan Review process](/handbook/security/product-security/vulnerability-management/customer-scan-review-requests/) for details.

## Reproducible Vulnerabilities

Learn how to identify or remediate security issues using real examples with GitLab's [Reproducible Vulnerabilities](/handbook/security/product-security/security-platforms-architecture/application-security/reproducible-vulnerabilities/).

## Reproducible Builds

Learn how GitLab is implementing [Reproducible Builds](/handbook/security/product-security/security-platforms-architecture/application-security/reproducible-builds/) for our build processes.

## Application Security Automation and Monitoring

Review the [automation and monitoring initiatives](/handbook/security/product-security/security-platforms-architecture/application-security/application-security-automation-monitoring/) used by the Application Security team.

## Content Review and Updates

This charter will be reviewed quarterly to ensure alignment with company and divisional priorities, the GitLab Security product roadmap, and relevant business and operational changes. Updates may occur more frequently as business operations evolve.

*Next scheduled review: June 30, 2025*
