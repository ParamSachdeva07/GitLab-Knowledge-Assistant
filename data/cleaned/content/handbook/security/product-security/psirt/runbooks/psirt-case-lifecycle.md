---
title: "PSIRT Case Lifecycle"
description: Description of how PSIRT will manage cases
---
Last updated: December 3, 2025

## About the PSIRT Case Lifecycle

PSIRT Analysts and Engineers work together to investigate reports of security vulnerabilities within GitLab products, services, and infrastructure. For all valid reports, PSIRT works with Engineering to consult on remediation and with Delivery to inform our customers about essential security updates.

The PSIRT investigates reports from the following sources:

- HackerOne
- Customer
- VAT
- Public/News
- Security Tooling with demonstrable exploitation
- Internal Security Research

PSIRT raises an incident when a critical vulnerability is being actively exploited or is publicly known. See the [Unified Incident Severity Matrix](/handbook/engineering/infrastructure-platforms/incident-management/#severities) once it's in the handbook for details of how the PSIRT works within the GitLab incident process. Otherwise, reports are investigated, filed, and remediated within established SLAs.

## PSIRT Case Investigation

PSIRT cases have six stages. The first two stages, triage and assessment, are completed within PSIRT while the last four stages involve cross-functional work with multiple teams in Engineering and Delivery.

**Note:** The PSIRT triage process does not correspond to the Triage stage of a HackerOne case.

| Stage | Triage | Assessment | Remediation | Validation | Release | Post-release |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| **Who** | Security Analyst (SA) | Security Engineer (SE) | SA & SE | Security Engineer (SE) | SA & SE | Security Analyst (SA)  |
| **What** |  Initial review of a case to determine whether it requires a full assessment.  | Full validation and assessment for each platform, including impact, reproduction steps, CWE, CVSS, impacted versions, severity | SE:  Consultation on issue with Engineering and additional variant hunting  SA: Monitoring of caseload SLAs & any Heightened Watch criteria | Review of fix to determine sufficiency | Release of fix and notification to customers in a security release blog post  | Completion of monthly/quarterly reporting If critical, completion of retro and executive reporting. |
| **Possible Outcomes** | Not valid Full assessment by PSIRT engineer Full assessment by PSIRT engineer with Heightened Watch Handover to SIRT Handover to Vulnerability Management  | Not valid File defect for Engineering File defect for Engineering with Heightened Watch Joint PSIRT/SIRT Incident  | Variants discovered and issue filed Mitigations and workarounds discovered  No additional information discovered Escalate Heightened Watch to Joint PSIRT/SIRT incident | No fix: Risk accepted by Engineering Approve MR for fix RejectMR for fix  | N/A |  |
| **HackerOne case state** | New <br/> Pending Program Review | Pending Program Review | Triaged | Triaged | Triaged | Closed |

### SLO

We have the following SLO to triage, assess, and complete post-release reporting on vulnerabilities:

| | Critical/High | Medium | Low |
| :---- | :---- | :---- | :---- |
| Triage | 5 days | 5 days | 5 days |
| Assessment | 10 days from triage handoff | 20 days from triage handoff | 20 days from triage handoff |
| Post-Release | 15 days from release | 30 days from release | 30 days from release |

## PSIRT Triage Workflow

The PSIRT Triage workflow ensures accurate initial assessment and proper routing of vulnerabilities through the system based on their severity and characteristics.

The following workflow applies to all reports within the scope of PSIRT but may include steps that are only applicable to [HackerOne reports](/handbook/security/product-security/psirt/runbooks/hackerone-process/).

1. Monitor for new reports in [HackerOne](https://hackerone.com/bugs?organization_inbox_handle=gitlab_inbox&assigned_to_group_ids%5B%5D=108264&text_query=&end_date=&reported_to_team=&sort_direction=descending&sort_type=latest_activity&start_date=), email, and Slack.
2. Acknowledge Receipt
   - Confirm receipt of the vulnerability report to the finder
3. Completeness Check
   - Assess the report to determine if there are sufficient details to proceed
   - If incomplete: Ask the finder for additional details before continuing
4. Check for handoff
   - Handoff to Vulnerability Management
     1. If the report is of a published CVE that is not critical and has no GitLab specific POC, check the Known Exploited Vulnerabilities list
     2. If not on [KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog): Hand off to Vulnerability Management
   - Handoff to SecOps:
     1. If the report is of a published CVE that is critical and on the KEV list, trigger Heightened Watch
     2. If the report is within the SecOps scope, hand off to SecOps
5. For remaining reports, open a GitLab issue using the Import procedure in Slack
6. Validate the report
   - Review the report to determine if there is a potential vulnerability
   - If invalid: Inform the issue reporter and update the report as required, then disengage
   - If the report is potentially valid, classify the severity level (Critical, High, Medium, Low and complete the Triage Assessment section of the issue.
7. Assign to Security Engineer
8. (HackerOne) Monitor report for additional details or requests for updates

## PSIRT Assessment Workflow

The assessment phase is primarily a technical evaluation period where PSIRT Engineers conduct deep analysis while maintaining coordination with other teams as needed for incident response or specialized expertise.

### PSIRT Engineer Tasks

1. Once assigned, complete technical vulnerability analysis
   - Vulnerability Reproduction: Confirm and reproduce the reported vulnerability
   - Platform and Version Identification: Determine all affected platforms and versions
   - Exploitability Research: Assess how easily the vulnerability can be exploited
   - Severity Assessment: Evaluate the technical severity level
   - Impact Analysis: Conduct STRIDE methodology assessment to understand security impact
   - CVSS Scoring: Calculate the Common Vulnerability Scoring System score
   - CWE Classification: Assign appropriate [Common Weakness Enumeration](/handbook/engineering/development/sec/security-factory/products/metrics/) category
2. Record all findings and technical details in the PSIRT investigation issue
   - If GitLab is not impacted, identify reason and assign to Security Analyst for followup to finder
   - If GitLab is impacted, complete assessment and file issue for Engineering remediation; ping Security Analyst to pay bounty and move HackerOne report to Triaged
3. IOC Analysis: If the issue is critical, determine if Indicators of Compromise can be identified
   - If Indicators of Compromise can be identified, open a joint PSIRT/SIRT investigation for SIRT to look for IOC exploitation markers.
   - If exploitation is indicated, open SIRT incident
   - Otherwise, implement Heightened Watch

### PSIRT Analyst Tasks

1. Complete Bounty and Administrative Tasks
   - If GitLab is not impacted, follow up with finder
   - If GitLab is impacted:
     - For HackerOne reports pay appropriate bounty and move issue to Triaged state in HackerOne
     - For other reports, follow up with finder
   - If Heightened Watch, monitor for escalation to Incident

## PSIRT Remediation Workflow

### PSIRT Engineer Tasks

1. In parallel with Remediation:
   - Variant Hunting: Search for related vulnerabilities or attack vectors
   - Mitigation Identification: Identify potential mitigations and workarounds

### Handling Breaking Changes

When evaluating a solution that risks a breaking change, the PSIRT engineer should verify and assist:

- Is this solution secure by default?
- Per the [breaking change template](https://gitlab.com/gitlab-com/Product/-/blob/main/.gitlab/issue_templates/Breaking-Change-Exception.md?ref_type=heads), PSIRT could assist in the following areas:
  - In the _Executive Summary_ section: PSIRT is the natural owner of confirming whether a breaking change qualifies under the "_significant security risk - Severity 1 or 2_" criterion. The team should validate the severity rating and confirm the security justification.
  - In the _"Can we get the same outcome without a breaking change?"_ section: PSIRT can provide input on whether alternative fixes exist that avoid breaking changes, or confirm that the breaking approach is the only viable remediation.
  - In the _"When do you want to make the breaking change?"_ section: PSIRT should weigh in on timing, especially when vulnerability SLAs or FedRAMP remediation deadlines constrain the timeline.
  - In the _Customer Communication_ section: PSIRT should review customer-facing copy to ensure it doesn't over-disclose vulnerability details while still explaining why the breaking change is necessary. There's also the question of coordinating with the security release blog post vs. the general breaking change comms.
  - In the _Deprecation issue linkage_ section: The template says to create a public deprecation issue after VP approval. For security-motivated changes, PSIRT should review what goes into that public issue to avoid premature disclosure.

## PSIRT Validation Workflow

The verification phase serves as a quality gate to ensure vulnerabilities are properly resolved before moving to the release process. The remediation and verification phases work in a loop \- if the fix is determined to be insufficient during validation, the process returns to engineering remediation for additional work until the fix is deemed complete and sufficient.

### PSIRT Engineer Tasks

1. [Validate Fix](/handbook/security/product-security/psirt/runbooks/verifying-security-fixes/) in MR Review
   - If fix is inadequate, reject MR
   - If fix is inadequate, approve MR and confirm affected platforms, versions, severity, CWE and CVSS score

## PSIRT Release Workflow

Patch releases are a shared engineer and analyst responsibility.
Refer to the [General process for the product security incident response team in patch releases](/handbook/security/product-security/psirt/runbooks/security-engineer/) for general information and [PSIRT Patch Release Duties](https://internal.gitlab.com/handbook/security/product_security/psirt/runbooks/security_release/) for specific steps.

## PSIRT Post-Release Workflow

The post-release tasks are shared between engineers and analysts.

### PSIRT Engineer Tasks

1. Verify that the release has been completed successfully.
2. Create and/or contribute to the Release Retro issue

### PSIRT Analyst Tasks

1. If the issue is critical, schedule a retrospective and prepare executive reporting. Work in conjunction with SIRT if the issue was a joint SIRT/PSIRT responsibility.
2. Create and/or contribute to the [Release Retro issue](https://gitlab.com/gitlab-com/gl-security/product-security/appsec/appsec-team/-/issues/new?description_template=release_retro)
3. Add to the Monthly Business Report (TBD)
4. Ensure that the HackerOne report is closed.
