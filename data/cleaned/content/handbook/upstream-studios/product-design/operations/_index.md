---
title: Product Design Operations
description: >-
  "Operational guidance for Product Designers and Product Design Managers including issue management, team operations, and administrative processes."
---

Product Design is part of [Upstream Studios](/handbook/upstream-studios/), GitLab's full-stack experience organization. As strategic partners positioned upstream, we're involved in planning from the start and use these operational practices to ensure design is integrated throughout the product development process.

For design processes, collaboration practices, and craft guidance, see [Product Designer Workflow](/handbook/upstream-studios/product-design/workflow/).

## Issue management

### Triaging UX issues

Every Product Designer is empowered to triage issues labeled with `~UX`, `~Deferred UX`, and `~UI polish`. If you are not the one triaging, you should be included for feedback by the responsible PM and EM. Use [Priority labels](/handbook/product-development/how-we-work/issue-triage/#priority) to suggest when the issue should be resolved and [Severity labels](/handbook/product-development/how-we-work/issue-triage/#severity) to indicate its user impact. Always coordinate with your PM and EMs on the assigned labels.

### Scheduling issues in a milestone

Strategic partnership means being involved in planning from the start. All issues labeled [`Deliverable`](https://gitlab.com/groups/gitlab-org/-/issues?scope=all&utf8=%E2%9C%93&state=opened&label_name%5B%5D=UX&label_name%5B%5D=Deliverable) that require UX will be assigned to a Product Designer by the kickoff. Issues labeled [`Stretch`](https://gitlab.com/groups/gitlab-org/-/issues?scope=all&utf8=%E2%9C%93&state=opened&label_name%5B%5D=Stretch&label_name%5B%5D=UX) may or may not be assigned by the kickoff. Learn more about how we use Workflow labels in the [GitLab Docs](https://docs.gitlab.com/development/labels/#release-scoping-labels).

### Communicating scheduled UX issues to the stage group

Consider adding a `User Experience` section to your team's planning issues ([example 1](https://gitlab.com/gitlab-org/ci-cd/release-group/release/-/issues/53#user-experience-roller_coaster), [example 2](https://gitlab.com/gitlab-org/ci-cd/release-group/release/-/issues/59#research-sleuth_or_spy)). This section can include active design items for the milestone, such as research projects, Deferred UX, UI polish, or Pajamas components. Learn more about [planning and capacity](/handbook/upstream-studios/product-design/workflow/capacity-management/) for Product Designers.

Including design problems in the planning issue makes design efforts visible and encourages cross-functional collaboration during `workflow::problem validation`, `workflow::design` and `workflow::solution validation`.

**Key benefits:**

- Advocating for UX within the stage group by making it part of monthly planning discussions
- Using the planning issue with the Product Manager during milestone kickoff
- Communicating current design and research efforts regularly to customers and counterparts
- Sharing the Product Designer's capacity with the team
- Encouraging early collaboration with counterparts during the design phase

## Workflow labels

Product Designers use workflow labels to track where issues are in the development lifecycle. These labels help us maintain our strategic positioning by showing when we're involved in validation, design, and implementation phases.

**Product Development Flow labels:**

Issues move between these labels as needed. Not all labels apply to every issue:

- `workflow::validation backlog`
- `workflow::problem validation`
- `workflow::design`
- `workflow::solution validation`
- `workflow::planning breakdown`
- `workflow::scheduling`
- `workflow::ready for development`

Learn more about workflow labels in the [Product Development Flow](/handbook/product-development/how-we-work/product-development-flow/).

**When to apply specific labels:**

- **`workflow::planning breakdown`**: Solution needs to be broken into smaller issues for implementation. Stay involved by walking PM and Engineering through the proposed solution
- **`workflow::scheduling`**: Solution needs to be scheduled by PM and/or EM. Mention the [responsible product manager](/handbook/product/categories/#devops-stages) and communicate with the assigned engineer
- **`workflow::ready for development`**: Issue is meant for implementation in the current milestone and engineer(s) are comfortable with the solution

**Handling premature moves to Build phase:**

As design DRIs, we hold the line on quality. Sometimes a Product Manager might request moving an issue to the Build phase before it meets UX standards. In such cases, create follow-on issues and/or apply the `Deferred UX` label to indicate that the product doesn't meet UX requirements and will need immediate iteration.

## Delivering your solution

### Update the issue description

Once your work is complete and feedback is addressed, update the issue description (the SSOT) with a "Solution" section. This should be the reference point for what should be done and how.

### Include your design

Add your design to the "Solution" section. For small designs, a mockup may suffice. For more detailed changes, include a link to the Figma file.

### Use the design handoff checklist

Follow the [design handoff checklist](https://docs.gitlab.com/development/contributing/design/#handoff) to ensure all design specifications are documented and engineers are set up for success.

### Leverage collaboration tools

Utilize Figma's collaboration tools to gather feedback from your team and navigate discussions.

### Consider new UX paradigms carefully

When proposing new patterns or paradigms:

- Evaluate if the new pattern will be inconsistent with other areas
- Determine if other areas need updating to maintain consistency
- Assess if the new pattern significantly improves the user experience
- If changes are necessary, follow the [component lifecycle documentation](https://design.gitlab.com/get-started/lifecycle/)

## Follow through

### Scope down features

- Encourage engineers to break features into multiple merge requests for easier, more efficient reviews
- Consider the UX impact of merging partial changes. Use feature branches or flags if partial changes negatively affect the UX to ensure the full scope ships together

### Communicate end goals

When breaking solutions into smaller parts, ensure the entire team understands the end design goal to align development efforts.

### Maintain the SSOT

**Keep issue descriptions updated:**

- Update the issue description (the SSOT) with all agreed-upon elements, including images or links to design work
- Remove or archive outdated content to keep the SSOT clear
- For obvious changes, update the SSOT directly [without waiting for consensus](/handbook/values/#collaboration), using your judgment

**Stay engaged:**

- Subscribe to and regularly review issues in your product area
- Actively contribute to planning meetings to ensure proper prioritization
- Stay assigned and subscribed to active issues
- Follow related MRs and address any additional UX issues that arise

## Follow-up after design is finalized

### For changes affecting Pajamas

For changes that affect the [design system](https://design.gitlab.com/):

- **New UI component**: [Create a UX Pattern issue](https://gitlab.com/gitlab-org/gitlab-design/issues/new?issuable_template=UX%20Pattern) in GitLab Design and follow the checklist
- **Documentation updates**: Create an issue and/or MR in the [Design System](https://gitlab.com/gitlab-org/gitlab-services/design.gitlab.com)
- **Application updates**: Create issues to update affected areas of the application
- **Socializing changes**: Inform the team of changes through Slack channels, such as `#upstream-studios`

### After changes go live

**Gather feedback:**

- Listen for feedback from social media, Slack, forums, and internal/external sources
- Create an issue to track and address the feedback

By following these operational practices, you ensure effective communication, collaboration, and continuous improvement aligned with Upstream Studios' commitment to strategic partnership and quality delivery.

## Manager operations

### Team member updates

Whenever you need to update the area of the product a team member is supporting, such as on the Product Categories page, you'll generally need to update or review the following pages and projects. For all updates, confirm that the name matches the name used on the team page.

**Section-level updates:**

1. Go to the [www-gitlab-com project](https://gitlab.com/gitlab-com/www-gitlab-com) > Repository > Files
2. Select the `data` directory
3. Scroll down and click on the `sections.yml` file
4. Select the editor type of your choice
5. Locate the person you need to update, make the change, commit/create an MR, and follow the MR process from there

**Group-level updates:**

1. Go to the [www-gitlab-com project](https://gitlab.com/gitlab-com/www-gitlab-com) > Repository > Files
2. Select the `data` directory
3. Scroll down and click on the `stages.yml` file
4. Select the editor type of your choice
5. Locate the person you need to update, make the change, commit/create an MR, and follow the MR process from there

**Update team member (such as to remove/add from UX MR Reviewer Roulette):**

1. Go to the www-gitlab-com project > Repository > Files - Documentation
2. Navigate to the `data/team_members/person/product` directory
3. Locate the correct alphabet letter folder according to the team member's first initial in their first name
4. Click on their `.yml` file
5. Select the editor type of your choice
6. To remove from the UX MR Reviewer Roulette bot:
   - Delete the `gitlab: reviewer UX` line under the `projects:` section
   - Commit/create an MR, and follow the MR process from there
7. To add to the UX MR Reviewer Roulette bot:
   - Revert the original MR where the team member was removed or find their `.yml` file again following the above steps
   - Add back the `gitlab: reviewer UX` line under the `projects:` section
   - Commit/create an MR, and follow the MR process from there

**Triage reports:**

In the [triage-ops project](https://gitlab.com/gitlab-org/quality/triage-ops), open an MR to add or remove team members from receiving triage reports. The file to edit is `group_definition.yml`.

**Retrospectives:**

In the [GitLab team retrospective group](https://gitlab.com/gl-retrospectives), find the team members section and group, and add and remove team members there. This step is required so that confidential issues can be seen by team members.

Also, open an MR to add or remove team members in the `team.yml` file in [async-retrospectives](https://gitlab.com/gitlab-com/gl-retrospectives/async-retrospectives).

### Growth & Development

When working with your team members on any Growth & Development requests, refer to the [Growth and Development Benefit guidelines](/handbook/people-group/learning-and-development/growth-and-development/).

## Talent assessment

In Product Design and Design System, we utilize [performance factor worksheets](https://drive.google.com/drive/folders/1KgmIt7Umm0XH2-74jMBpOl67Yko1t2uK) (**🔒 internal only**) to facilitate talent assessment and growth conversations between managers and their direct reports. These worksheets are available in Google Sheets format and include tabs for mid-year and year-end reviews, as well as a tab to list achievements, strengths, and opportunities throughout the year.

It is strongly encouraged for each team member to have their own worksheet created at the start of the fiscal year so it can be used as a tool throughout the entire year.

Performance factor worksheets can be utilized to help efficiently complete the year-end company [talent assessment program within Workday](/handbook/people-group/talent-assessment/).
