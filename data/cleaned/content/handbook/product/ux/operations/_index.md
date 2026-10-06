---
title: UX Operations
description: >-
  Operational guidance for UX team members including headcount planning, procurement, labels, and team processes.
---

This page contains operational information for working in the UX department at GitLab.

## Headcount planning

UX team members work with stable counterparts across Product Management and Engineering, with alignment models varying by discipline and work type.

### Product Design

Product Designers primarily work in one of two models:

- **Stage group alignment:** Designers aligned to stage groups partner with a dedicated PM and Engineering team on specific product areas
- **Project-based work:** Designers work on cross-cutting platform initiatives (Design System, navigation, strategic projects) that span multiple groups or operate independently

Planning ratios for stage-aligned roles:

- 1:1 Product Designers to PM
- 1 Product Designer per 1-3 Frontend engineers; 2 per 4-5 Frontend engineers

### UX Research

UX Researchers support multiple groups within a section:

- 1:5 ratio of UX Researchers to Product Managers
- Approximately 1:35 ratio of UX Researchers to Engineers

### Technical Writing

Technical Writers each support multiple stage groups:

- 1:3 ratio of Technical Writers to stage groups
- Approximately 1:21 ratio of Technical Writers to Engineers

### Design System

The Design System team operates independently, building platform-wide infrastructure that serves all Product Designers, Engineers, and Technical Writers. This team is not aligned to specific stage groups or PMs.

### Management

Manager support is appropriate for each function:

- Approximately 1:5 ratio of Managers to direct reports for UX Research and Product Design
- Approximately 1:7 ratio of Managers to direct reports for Technical Writing

## Procurement requests

To request a new product/service, open an issue using the [UX procurement proposal issue template](https://gitlab.com/gitlab-com/Product/-/issues/new?related_item_id=undefined&type=ISSUE&description_template=UX-Procurement-Request). Your manager will work with UX Leadership to identify spending needs and partner with FP&A to secure budget before following the [vendor lifecycle](/handbook/finance/procurement/#vendor-lifecycle-management).

## UX labels

GitLab uses labels to categorize, prioritize, and track work. The following is a breakdown of the labels most directly related to the UX workflow. An overview of all the label types and uses can be found in the [contributing doc](https://gitlab.com/gitlab-org/gitlab-foss/blob/master/doc/development/contributing/issue_workflow.md).

- [**UX** label](https://gitlab.com/groups/gitlab-org/-/issues?scope=all&utf8=%E2%9C%93&state=opened&label_name[]=UX): Indicates that UX work is required on this issue. These issues can be new features, ideas for improvement or anything else where UX should contribute their expertise.
- [**Inclusion** label](https://gitlab.com/groups/gitlab-org/-/labels?utf8=✓&subscribed=&search=Inclusion): A change to GitLab that promotes inclusion as it relates to our [diversity](/handbook/values/#diversity-inclusion) value.
- [**Inclusive design** label](https://gitlab.com/groups/gitlab-org/-/labels?utf8=✓&subscribed=&search=Inclusive+design): Considering, exploring, and evaluating the different ways someone would access, interact with, or contribute to content that results in a more accessible experience.
- **Accessibility and scoped accessibility labels** are used to identify issues with accessibility impact. The scoped labels should be added after an accessibility audit has validated the impact and used in combination with [priority](/handbook/product-development/how-we-work/issue-triage/#priority) and [severity](/handbook/product-development/how-we-work/issue-triage/#severity) labels to [triage](/handbook/product-development/how-we-work/issue-triage/) an issue.
  - [**Accessibility** label](https://gitlab.com/groups/gitlab-org/-/labels?utf8=✓&subscribed=&search=%22Accessibility%22): Issues that contain actionable items that help create an accessible product experience.
  - [**Accessibility-audit** label](https://gitlab.com/groups/gitlab-org/-/labels?utf8=%E2%9C%93&subscribed=&search=%22Accessibility-audit%22): Issues related to auditing exisiting experiences in order to understand possible accessibility-related improvements.
  - [**Accessibility-ops** label](https://gitlab.com/groups/gitlab-org/-/labels?utf8=%E2%9C%93&subscribed=&search=%22Accessibility-ops%22): Issues related to building accessibility into our internal workflows.
  - `accessibility::critical`: Prevents some or all users from performing critical tasks with no possible workaround.
  - `accessibility::high`: Prevents some users from performing critical tasks. A workaround may exist, but not without creating frustration and inefficiency.
  - `accessibility::medium`: Prevents some users from performing non-critical tasks, or where the user experience is seriously degraded for users with certain assistive technologies.
  - `accessibility::low`: The user experience is degraded for users with certain disabilities or using certain assistive technologies, but users can still accomplish tasks.
- [**learnability** label](https://gitlab.com/gitlab-org/gitlab/-/issues/?label_name%5B%5D=learnability): Issues that address learnability problems by helping users quickly become familiar with GitLab features.
- **Scoped workflow labels** from the [Product Development Flow](/handbook/product-development/how-we-work/product-development-flow/#validation-phase-1-validation-backlog) should be used to indicate where an issue is in the development lifecycle. Issues can move between workflow labels as many times as necessary, and not all labels will be applicable to every issue. Issues that require UX would use one of these labels as defined in the Product Development Flow:
  - `workflow::validation backlog`
  - `workflow::problem validation`
  - `workflow::design`
  - `workflow::solution validation`
- **Pajamas component lifecycle labels** are scoped labels used for creating and updating [Pajamas](https://design.gitlab.com) components. Label usage guidelines can be found in the [Pajamas component lifecycle documentation](https://design.gitlab.com/get-started/lifecycle/).
- [**UX problem validation** label](https://gitlab.com/groups/gitlab-org/-/issues?scope=all&utf8=%E2%9C%93&state=opened&label_name[]=UX%20problem%20validation): Indicates that the issue requires UX work to validate that the problem is relevant to users. We use this label in addition to the Product Development Flow scoped labels, so that we can track validation efforts over time in our [UX Performance Indicators](/handbook/product/ux/performance-indicators/).
- [**UX solution validation** label](https://gitlab.com/groups/gitlab-org/-/issues?scope=all&utf8=%E2%9C%93&state=opened&label_name[]=UX%20solution%20validation): Indicates that the issue requires tasks to validate that the proposed solution is technically feasible and meets user needs. We use this label in addition to the Product Development Flow scoped labels, so that we can track validation efforts over time in our [UX Performance Indicators](/handbook/product/ux/performance-indicators/).
- [**UI polish** label](https://gitlab.com/groups/gitlab-org/-/issues?scope=all&state=opened&utf8=%E2%9C%93&label_name%5B%5D=UI+polish): Indicates the issue covers *only* visual improvement(s) to the existing user interface.
- [**Deferred UX** label](https://gitlab.com/groups/gitlab-org/-/labels?subscribed=&sort=relevance&search=deferred+ux): Deferred UX results from the intentional decision to deviate from the UX vision or MVC, which sacrifices the user experience. Deferred UX labeled issues are to be included in subsequent releases. Use this label to indicate that the UX released does not meet:
  - UX and Pajamas specifications
  - Usability standards
  - Feature viability standards

   This label is applied to any follow-up issues that address a UX gap. It does not apply to the issue or merge request that created the Deferred UX. For example, if the agreed MVC design solution is not fully realized due to release pressures or implementation oversight, that's considered Deferred UX.

   If the design is implemented correctly but unforeseen UX issues are identified, it is *not* considered Deferred UX.

   If in doubt about when to apply this label, use the following rule: If you can say "This UX problem did not originate from an issue or merge request," then it's just UX, not Deferred UX. In case your team makes the decision ship an MVC that contains Deferred UX, it is recommended to create an issue to track it as soon as the change has been released.

- [**Learn more about Deferred UX as a UX Department Performance Indicator**](/handbook/product/ux/performance-indicators/#deferred-ux).
- [**Seeking community contributions**](https://gitlab.com/groups/gitlab-org/-/issues?state=opened&label_name[]=Seeking+community+contributions&assignee_id=0&sort=weight)
- [**System Usability Scale (SUS)** labels](https://gitlab.com/gitlab-org/gitlab/-/labels?subscribed=&search=sus): Indicates that the issue is related to usability problems surfaced in one of our SUS research efforts. More specifically, issues related to SUS that are prioritized can be labeled with the corresponding Fiscal Year and Quarter. For example: `SUS::FY22 Q2 - Incomplete`.
[**Learn more about SUS score as a UX Department Performance Indicator**](/handbook/product/ux/performance-indicators/#perception-of-system-usability)
- [**Regression** label](https://gitlab.com/groups/gitlab-org/-/issues?scope=all&state=opened&utf8=%E2%9C%93&label_name%5B%5D=regression): Indicates a bug introduced in the latest release that broke correct behavior (see the [contribution guidelines](https://gitlab.com/gitlab-org/gitlab-ce/blob/master/CONTRIBUTING.md#regression-issues) for more info).
- [**UX scorecard** label](https://gitlab.com/groups/gitlab-org/-/issues?scope=all&utf8=%E2%9C%93&state=opened&label_name[]=UX%20scorecard): Indicates the primary issue or epic for the [UX Scorecard](/handbook/product/ux/ux-scorecards/). We use this label to help us easily find current work and track efforts over time.
- [**UX scorecard-rec** label](https://gitlab.com/groups/gitlab-org/-/issues?scope=all&utf8=%E2%9C%93&state=opened&label_name[]=UX%20scorecard-rec): Indicates this issue is a recommendation that was a result of a UX scorecard review. It's OK if the issue was created prior to the scorecard being done; it can still be pulled into the set of recommendations.
- [**cm-scorecard-rec** label](https://gitlab.com/groups/gitlab-org/-/issues?sort=created_date&state=opened&label_name[]=cm-scorecard-rec): Indicates this issue is a recommendation that was a result of a CM Scorecard.
- [Actionable Insights](/handbook/upstream-studios/experience-research/research-insights/#how-to-document-actionable-insights) document learnings from research that need to be acted on.
  - [Actionable Insight::Exploration needed](https://gitlab.com/groups/gitlab-org/-/issues/?sort=updated_desc&state=opened&label_name%5B%5D=Actionable%20Insight%3A%3AExploration%20needed): A research insight derived from a UX research study that requires further exploration.
  - [Actionable Insight::Product change](https://gitlab.com/groups/gitlab-org/-/issues/?sort=updated_desc&state=opened&label_name%5B%5D=Actionable%20Insight%3A%3AProduct%20change): A research insight derived from a UX research study and requires a change to the product experience.
- [Type labels](/handbook/product/groups/product-analysis/engineering/metrics/#work-type-classification): Used to track feature, maintenance, and bug issues and MRs. UX Leadership are active participants in influencing the prioritization of all three work types. See also who are the [DRIs for prioritization](/handbook/product/product-processes/cross-functional-prioritization/#prioritization-for-feature-maintenance-and-bugs).
- **Theme labels** can be created to group issues that solve a similar user experience problem but don't have a category. This can be especially useful for a user experience that spans the product. These issues still require a UX label.
- [**UX: Feature Discovery Improvement**](https://gitlab.com/groups/gitlab-org/-/issues?label_name%5B%5D=UX%3A++Feature+Discoverability+Improvement): Indicates issue may improve feature discoverability.
- [**UX: Onboarding Improvement**](https://gitlab.com/groups/gitlab-org/-/issues/?label_name%5B%5D=UX%3A%20Onboarding%20Improvement): Indicates issue is a potential onboarding improvement.

## Upstream Studios calendar

The [Upstream Studios Calendar](https://calendar.google.com/calendar/embed?src=gitlab.com_9psh26fha3e4mvhlrefusb619k%40group.calendar.google.com) (*internal only*) is the SSOT for our team meetings. You can find the details for Upstream Studios calls, Upstream Forum, and other team meetings here. These meetings are open to everyone in GitLab. Anyone in the Upstream Studios department can add events to the Google Calendar. Managers and above can make changes and manage sharing, while ICs can make changes to events.

## Retrospectives

To understand the specific challenges faced by the UX Department, we hold an async UX retrospective after every milestone. This retro is carried out through a new Issue created for the recent release in the [ux-retrospectives](https://gitlab.com/gl-retrospectives/ux-retrospectives/issues) project. The goal is to evaluate what went well, what didn't go well, and how we can improve.
