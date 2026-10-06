---
title: "GitLab Navigation"
description: "Navigation refers to elements that aid users in moving around GitLab, which includes organization and wayfinding clues."
---

## Ownership

The below RACI table outlines the collaboration between the [Growth: Engagement](/handbook/product/categories/#engagement-group) and [Foundations: Design System](/handbook/product/categories/#design-system-group) teams in building our product's wayfinding experience. While the Engagement team serves as the ultimate owner of navigation decisions and user flow optimization, the Design System team takes primary responsibility for creating the structural foundation that enables these experiences - including component frameworks, layout templates, responsive design patterns, and consistency standards. The Design System team builds the scaffolding and reusable systems, while the Engagement team determines how users navigate through and interact with these structures to achieve business objectives.

### Key

- **R** = Responsible (does the work)
- **A** = Accountable (final decision maker)
- **C** = Consulted (provides input)
- **I** = Informed (kept in the loop)

### RACI table

| Task/Role | Engagement Team | Design System Team | Notes & Examples |
|-----------|-------------|-------------------|------------------|
| **Define structural framework and templates** | C | R/A | Container structures, grid systems, page templates. *Example: Creating slots for navigation chrome* |
| **Establish component relationships and hierarchy** | C | R/A | How components nest, visual hierarchy guidelines. *Example: Panel structure, borders, padding* |
| **Create layout patterns and responsive design** | C | R/A | Grid systems, breakpoints, layout templates. *Example: Main page template with defined regions* |
| **Define navigation architecture and user flows** | R/A | C | Menu structures, information architecture, user pathways. *Example: How users move between features* |
| **Determine content placement and prominence** | R/A | I | What goes where, CTA's within defined templates, feature discovery. *Example: What content fills the navigation slots* |
| **Optimize conversion paths and user experience** | R/A | I | Funnel optimization, feature positioning. *Example: AI panel placement, trial widget positioning* |
| **Extend existing layout framework** | R/A | C | Adding new regions or modifying templates. *Example: Adding bottom toolbar, changing panel count from 3 to 4* |
| **Maintain design system consistency** | C | R/A | Ensuring reusability and portability across teams. *Example: Panel components usable by other teams* |
| **Establish design principles and guidelines** | C | R/A | High-level design standards and best practices. *Example: Visual hierarchy rules, color modes* |
| **Make application-specific navigation decisions** | R/A | C | Product-specific navigation choices within framework. *Example: Logo placement* |
| **Implement component functionality** | R/C | R/C | Technical implementation of layout components. *Example: Resizable panels, responsive behavior* |
| **Collaborate on cross-functional changes** | R/C | R/C | Changes requiring both structural and content considerations. *Example: Right-to-left language support* |

### Collaboration principles

1. **Templates without Content**: Design System defines structural templates and regions; Growth defines content within those regions
1. **Guidelines over Requirements**: Design System provides flexible principles rather than rigid rules
1. **Extensible Framework**: Growth can extend the system and contribute patterns back to Design System
1. **Consultation First**: Teams consult each other before major changes, even in primary ownership areas
1. **Disagree and Commit**: Accountable party makes final decisions when alignment isn't reached

### Escalation process

- **Layout vs. Navigation conflicts**: Escalate to both team leads
- **Feature vs. System prioritization**: Escalate to product leadership
- **Emerging ownership questions**: Address in regular sync meetings before they become blockers

## Requesting a navigation change

> Note: a [Code Owners approval rule](https://docs.gitlab.com/user/project/codeowners/) is in place to prevent unapproved changes to the navigation. If you have not followed this process, your Merge Request will be blocked.

### What is navigation?

Navigation refers to elements that aid users in moving around GitLab, which includes their organization and wayfinding clues. The navigation experience directly impacts the usability and discoverability of our features. This document describes how we can collectively evolve the navigation while still [meeting our goals](https://about.gitlab.com/direction/foundations/personal_productivity/#navigation).

### Why do we need to be careful when changing the navigation?

In the past, teams added items to highlight new features. However, this created an overwhelming navigation structure that makes it challenging for users to find what they need. Our [quarterly GitLab SUS survey](https://gitlab.com/groups/gitlab-org/-/epics/1455) continues to highlight these recurring themes:

- The navigation is complex or confusing
- The navigation is difficult to learn
- The navigation is not intuitive

### What kind of navigation changes require approval?

While GitLab's UX allows users to navigate across the product in different ways, the focus of the approval process is on the left-side navigation. This area serves both as navigation and as a feature discovery point for users. As the navigation evolves, it's crucial that we maintain a balance between a focus on core workflows and feature visibility.

To help maintain this balance, we ask for everyone to use this process when proposing changes to the left-side navigation:

- First, second, and third-level navigation additions
- Renaming a navigation item
- Removing a navigation item
- Changing the sort order of navigation items
- Changing navigation functionality or features
- Launching an [Experiment](https://docs.gitlab.com/policy/development_stages_support/#experiment) or [Beta](https://docs.gitlab.com/policy/development_stages_support/) feature
- Changing the viewership of a navigation item (e.g. moving from disabled by default to enabled by default)

### When to change the navigation

We only make new additions to the GitLab navigation structure through a deliberate process that is intended to optimize user workflows. This [video](https://www.nngroup.com/videos/number-items-navigation-menu/) summarizes the main factors that are important to consider as we iterate on our navigation. In the past, teams added items to highlight new features. However, it becomes impossible to accommodate every new feature, as this creates an overwhelming navigation structure that makes it too difficult for users to find what they need to complete their tasks.

Therefore, we **do not add new items** to:

- Improve discoverability of new features. Instead, look for other opportunities to [highlight the functionality](https://design.gitlab.com/usability/feature-discovery/) throughout the product.
- Optimize for the potential future. We should be forward thinking without over optimizing. As features are developed and added, we can look into what changes may need to occur to support a growing feature.

### How do I evaluate navigation changes?

There are two main questions we need to answer for navigation changes:

1. Does this navigation proposal facilitate one of our [primary JTBDs](https://gitlab.com/gitlab-com/www-gitlab-com/-/blob/master/data/jtbd.yml?ref_type=heads)? Which job?
1. How does this change improve the workflow for users attempting to complete that job?

There are many different types of [Problem Validation research](/handbook/upstream-studios/experience-research/problem-validation-and-methods/) that could be done to learn about areas of opportunity for our navigation. The specific type of research performed should be based on the research questions and goals of the study. The following research methods and frameworks are some examples of ways research can be used to justify a new addition to the existing GitLab navigation:

1. [Contextual inquiry](https://www.nngroup.com/articles/contextual-inquiry/): This method involves observing and interviewing users as they perform tasks related to their role to understand the "why" and the "how" behind them.
   - **Example**: Users may demonstrate how they navigate through multiple menus and pages in GitLab to find their dashboards. This insight would reveal the need for a single page in GitLab to find all dashboards.
1. [Jobs to be Done (JTBD)](/handbook/product/ux/jobs-to-be-done/): This framework is a type of [foundational research](/handbook/upstream-studios/experience-research/foundational-research/) meant to learn the job(s) that customers want to accomplish within their roles. Jobs allow us to define the circumstances, goals, and outcomes of customers' work.
   - **Example**: By interviewing users, we learn that have a main job of tracking metrics to show the health of their application, so they can identify when the application is failing. This insight would suggest a gap we could fill in GitLab by adding a page for displaying application metrics.
1. [Diary study](/handbook/upstream-studios/experience-research/diary-studies/): This method is used to gain feedback from users over a period of time, so we can uncover changes that occur over days, weeks, or months.
   - **Example**: When gathering feedback about how users engage with a major change to GitLab's navigation bar, we observe that GitLab admins continuously struggle from one month to the next with locating the admin area to adjust settings. This insight would suggest we need to surface the admin area in the user interface since it is not easy to find over time.

Questions to ask to learn whether a change to the navigation is needed:

1. What are the main tasks associated with your current role?
1. Why are those tasks important? What would happen if you could not complete those tasks?
1. Show me how you perform a specific task using your existing tools.
1. What, if anything, would you improve about the process of completing that task?

After there is insight into a problem with the navigation, the Product team DRI should work with Product Design and UX Research to evaluate the ideal solution through a subsequent [solution validation](/handbook/upstream-studios/experience-research/evaluating-navigation/#our-approach-to-evaluating-navigation-changes) study.

### How to propose a navigation change

> If your primary goal is to improve discoverability of your feature, please start by looking for other opportunities to [highlight the functionality](https://design.gitlab.com/usability/feature-discovery/) throughout the product.

1. Before opening an issue, review the [elements and patterns for navigation in Pajamas](https://design.gitlab.com/usability/navigation-sidebar/).
1. Review the [list of navigation changes](/handbook/product/ux/navigation/#what-is-navigation) and what they are to make sure your change qualifies.
1. The Product Manager for [Growth: Engagement](/handbook/product/categories/#engagement-group) is the [DRI](/handbook/people-group/directly-responsible-individuals/#what-is-a-directly-responsible-individual) for navigation changes. Reach out to them to determine whether your proposal needs [full validation](#full-validation-path) or [limited validation](#limited-validation-path).
1. You can initiate the review for this process by using the [Navigation Proposal](https://gitlab.com/gitlab-org/gitlab/-/issues/new?issuable_template=Navigation%20Proposals) issue template.
1. Designers on [Growth: Engagement](/handbook/product/categories/#engagement-group) will assist the DRI by reviewing the proposal and providing input. The typical turnaround time from the [Growth: Engagement](/handbook/product/categories/#engagement-group) team will be 1 milestone. After providing feedback, it is the responsibility of the DRI to move the proposal forward and seek additional feedback as needed.
1. When you have approval and are ready to start implementation, then follow the [GitLab Docs on adding items to the navigation](https://docs.gitlab.com/development/navigation_sidebar/#adding-page-specific-vue-content).

#### Full validation path

This path is suitable for navigation changes that affect a majority of GitLab users or that introduce new design patterns. Some examples of changes that may need full validation are:

- Launching a Beta or Generally available feature
- Changes to navigation structure or functionality
- Removing an existing navigation item
- Renaming an existing navigation item

The [Growth: Engagement](/handbook/product/categories/#engagement-group) PM is the DRI for determining if your proposal should follow the full validation path. On this path, we require the following steps be completed and documented as part of the navigation proposal issue.

| Step | Requirement |
| --- | --- |
| Business case | All proposals must include a business case that identifies the underlying problem and goals of changing the navigation. |
| Problem validation | Problem validation research is required to discover and verify the areas of opportunity for our navigation. |
| UX review | A UX review has been conducted with the design DRIs for the related stage group. |
| Counterpart support | The proposal is supported by product, design, and research counterparts for the related stage group. |
| Solution validation | Solution validation research is conducted to evaluate a navigation change against other potential solutions. |

#### Limited validation path

This path is suitable for navigation changes that affect a minority of users or that follow pre-existing design patterns. Some examples of changes that may need limited validation are:

- Experimental features available behind a feature flag
- New 3rd party integrations that follow the pattern of existing integrations
- Changes that bring consistency where there is already inconsistency

The [Growth: Engagement](/handbook/product/categories/#engagement-group) PM is the DRI for determining if your proposal can follow the limited validation path. On this path, we require the following steps be completed and documented as part of the navigation proposal issue.

| Step | Requirement |
| --- | --- |
| Business case | All proposals must include a business case that identifies the underlying problem and goals of changing the navigation. |
| Problem validation | User research is not required to identify the area of opportunity for our navigation. |
| UX review | A UX review has been conducted with the design DRIs for the related stage group. |
| Counterpart support | The proposal is supported by product and design counterparts for the related stage group. |
| Solution validation | Proposals need to describe or visualize alternative solution(s) that surface changes at other points of the user journey. Then critically assess how well the proposed and alternative solutions address the problems and goals outlined in the business case. |

### Reconciliation process

The navigation proposal process attempts to balance a focus on core workflows and feature visibility, which means sometimes proposal authors may disagree with the [Growth: Engagement](/handbook/product/categories/#engagement-group) team decision. If you feel like we've struck the wrong balance, add a comment to the proposal and:

1. Summarize why the proposal was rejected and your perspective on why this decision is incorrect
1. Mention your manager and the [Growth: Engagement](/handbook/product/categories/#engagement-group) PM manager
1. Request their input on the decision
