---
title: Threat Intelligence Team
---

## Engaging Threat Intelligence

For urgent security requests, [engage the security team](/handbook/security/security-operations/sirt/engaging-security-on-call/) using the Slack command `/security`.

For all other matters, Threat Intelligence can be contacted by:

- Tagging `@threat-intelligence` in the Slack channel `#security_discuss` for general discussions.
- Tagging `@threat-intelligence` in the Slack channel `#security_help` for general requests.
- Following the [RFI process](#requests-for-information-rfi) for formal, well-defined requests.

## Our Vision

Empower GitLab to make informed, intelligence-driven decisions that keep our company and customers secure, while setting a new standard for transparency and collaboration across the industry.

## Our Mission Statement

Our mission is to provide actionable intelligence that empowers GitLab to make informed, proactive decisions about security.

We monitor the threat landscape with a focus on identifying the most relevant risks to GitLab. We analyze these risks, track the associated threat actors, and build relationships with industry peers. These connections give us access to timely, unique insights that are not otherwise available. We focus on extracting the information most relevant to our organization, allowing us to deliver clear, concise reports that recommend immediate actions.

By staying vigilant and sharing targeted intelligence, we strive to help GitLab anticipate challenges, move swiftly, and protect our customers and our platform.

## The Team

The Threat Intelligence team consists of one dedicated engineer, reporting to a Senior Manager within Security Operations.

## Services We Provide

### Security Operations Support

The Threat Intelligence engineer works closely with SIRT and other security teams, providing specialized expertise that overlays day-to-day security operations. This includes supporting active investigations and incidents through threat hunting, malware analysis, log analysis, and threat actor attribution. Much of this work is driven by team discussions in Slack, open cases, and active incidents rather than formal requests.

Supporting S1 incidents will always take priority over all other work.

### Threat Intelligence Reports

Reports are delivered on an ad-hoc basis in response to rapidly emerging threats, focusing on a specific threat actor, campaign, or vulnerability. They help GitLab make quick decisions to protect our customers and our organization. For themes that require ongoing attention, rolling summaries may be produced as needed.

All reports are written in GitLab.com, enabling collaboration and direct linking to recommendations. They consistently:

- Include linked issues with clearly defined next steps to address each topic covered
- Answer the following questions for each threat addressed:
  - How is this relevant to GitLab?
  - How well is GitLab prepared to deal with this threat today?
  - What steps is GitLab taking to better handle this threat?

Recommendations are often time-sensitive and critical, and are leveraged for activities like:

- Rapid iterations to security controls and detection capabilities
- Threat hunting
- Security communications
- Purple Team Flash Operations

Reports use the [Flash Report template](https://gitlab.com/gitlab-com/gl-security/security-operations/threat-intelligence-public/resources/threat-intelligence-templates/-/blob/main/.gitlab/issue_templates/flash_report.md?ref_type=heads).

### Requests For Information (RFI)

RFIs allow GitLab team members to request our help in analyzing threats and making intelligence-informed decisions. Team Members can [open an issue in our tracker using the RFI template](https://gitlab.com/gitlab-com/gl-security/security-operations/threat-intelligence/threat-intelligence-issue-tracker/-/issues/new).

Some examples where an RFI can provide value:

- Investigating active security incidents and exposure to third-party breaches
- Decisions on product security features and functionality
- Helping draft threat-informed communications about GitLab security decisions
- Third-party vendor and product evaluations

Requests for Information use [this template](https://gitlab.com/gitlab-com/gl-security/security-operations/threat-intelligence-public/resources/threat-intelligence-templates/-/blob/main/.gitlab/issue_templates/rfi.md?ref_type=heads).

## How We Measure Success

We track the following metrics using GitLab.com issues and custom labels.

### Current Metrics

- Adoption Rate: Measures the extent to which our intelligence-driven recommendations are accepted and implemented.
- RFI Satisfaction: Measures whether RFIs provide actionable information that answers the requestor's needs.

### Metric Labels

**Recommendation Classification Labels:**

- Detections & Alerts (`TIRec::Detection`)
- Security Controls (`TIRec::Control`)
- Processes and Procedures (`TIRec::Process`)
- Purple Team Operations (`TIRec::PurpleTeamOp`)

**Recommendation Outcome Labels:**

- Fully adopted and closed (`RecOutcome::Adopted`)
- Partially adopted and closed (`RecOutcome::PartiallyAdopted`)
- Not adopted and closed (`RecOutcome::NotAdopted`)

**RFI Satisfaction Labels:**

- RFI provided actionable information (`TIRFI::Satisfied`)
- RFI partially provided actionable information (`TIRFI::PartiallySatisfied`)
- RFI did not provide actionable information (`TIRFI::NotSatisfied`)

## Additional Resources

- [Threat Intelligence Templates](https://gitlab.com/gitlab-com/gl-security/security-operations/threat-intelligence-public/resources/threat-intelligence-templates): Public template repository for reports, RFIs, etc.
- [Annual Threat Intelligence Reports](https://gitlab.com/gitlab-com/gl-security/security-operations/threat-intelligence/threat-intelligence-resources/awesome-annual-security-reports): Internal mirror of publicly-available annual threat intelligence reports - team members can subscribe for updates.
