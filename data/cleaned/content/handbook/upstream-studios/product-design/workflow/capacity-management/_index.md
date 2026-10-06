---
title: Product Designer Priorities and Capacity Management
description: "Guidelines for Product Designers to prioritize work and manage capacity as strategic partners working in trios and on platform initiatives."
---

Product Designers work as [managers of one](/handbook/values/#managers-of-one), sequencing their own capacity across trio work, platform initiatives, and broader Upstream Studios responsibilities. This page provides guidance on prioritizing work and planning capacity.

For Product Designers working in [Product Design](/handbook/upstream-studios/product-design/), part of [Upstream Studios](/handbook/upstream-studios/).

## Planning and managing capacity

Product Designers are assigned to a group as an equal member of the trio. The following guidelines help you sequence work and protect capacity for both production work and the upstream judgment that's core to the role.

**Product Designers**

- Ensure cross-functional peers know about Upstream Studios assignments, such as platform initiatives, and what you'll need from them to succeed.
- When a request would crowd out research, exploration, or trio strategy work, raise it as a capacity trade-off with your manager directly.
- Account for time off (yours and others') during milestone planning.
- If you think you won't complete your committed work on time, tell your manager and your trio as soon as you know. Early notice keeps the trade-off conversation open.
- Optionally, use UX issue weights to better understand your capacity and facilitate conversations with your Product Manager.

**Product Design Managers**

- If requested, help Product Designers set a baseline capacity for group and platform-assigned work each milestone.
- Give production work clear time-to-complete (TTC) expectations and due dates. Give strategy work measurable goals and checkpoints, paced by what the team is learning.
- Resolve team questions, concerns, and blockers quickly.
- As AI absorbs more routine production work, redirect the freed capacity toward discovery and strategic work.
- Ensure cross-functional partners understand a designer's capacity includes discovery and strategic work alongside production work items, and are aware of potential dependencies.

### Priorities

The highest-leverage work happens before a line of code gets written: validating the problem, starting with the flow before jumping to a prototype, and setting success criteria early. When more than one thing wants the same hour, this is the order.

Must do:

- Committed trio work for the current milestone: issues assigned with labels `workflow::problem validation`, `workflow::solution validation`, or `workflow::design`, next-milestone planning, and sharing progress through Upstream Forum, Slack, and design critiques. This is what you've committed to; it comes first.
- Anything blocking someone else: peer feedback requests and merge request reviews, including community contributions, where automated coverage doesn't exist yet. Push for automated coverage in your domain so this shrinks over time.
- Exploration and vision work for large, holistic roadmap efforts, ahead of a specific solution being scoped. It's the easiest thing to cut because no one's waiting on it. That's exactly why it needs protecting.

Should do:

- Tasks that improve understanding of users and their workflows (e.g. [UX Scorecards](/handbook/product/ux/ux-scorecards/)).
- Issues in the current release milestone labeled `Stretch`, and Pajamas design system contributions (`pajamas::define`, `pajamas::design`, `pajamas::build`, or `pajamas::integrate`, and open [ToDo blocks in Pajamas](https://gitlab.com/search?group_id=5387503&project_id=4456656&scope=blobs&search=todo)). Fill remaining capacity here before reaching further out.

Nice to do:

- Future release or [Backlog](https://gitlab.com/groups/gitlab-org/-/issues?state=opened&milestone_title=Backlog&label_name%5B%5D=UX) milestone issues, community-labeled low-hanging fruit, popular issues with no milestones, and sharing your work externally. Pick these up when nothing above needs you.

#### Supporting Product Management

As strategic partners in trios, Product Designers provide insights into user needs and help identify both quick wins and larger strategic initiatives. This collaborative approach keeps design involved upstream, shaping planning discussions from the start.

### UX Issue Weights

Issue weights are optional but useful for planning. They help Product Designers understand their capacity, evaluate the impact of time off, facilitate trade-off discussions with Product Managers, and identify teams needing more UX support.

#### Using UX Issue Weighting

1. Review upcoming issues and break down the work
1. Assign an issue weight using the provided chart. Collaborate with the Product Manager for clarity if needed
1. Record your issue weight using your team's preferred method
    - List issues and weights in Google docs
    - Create a linked issue for the UX work and add a weight (close it after completion).
    - Use [design-weight labels](https://gitlab.com/gitlab-org/gitlab/-/labels?utf8=%E2%9C%93&subscribed=&search=design-weight)
1. Communicate your capacity and total issue weights when planning iterations or milestones
1. Review weights post-milestone to improve future planning accuracy

**Additional Notes:**

- Most UX issues, including research and Pajamas related issues can be weighted, if desired
- Consider visual reviews, meetings, and other non-weighted responsibilities when determining capacity
- Do not weight very small issues (less than 1)
- A weight of 8 or 13 indicates that the issue may be too large
- Add weights to unplanned work during a milestone and discuss trade-offs with the Product Manager

> Milestone Capacity Template:
>
> - **Total weights completed last milestone:** 10
> - **Average capacity (average of weights completed last 3 months):** 10
> - **Estimated capacity for current milestone:** 7 (use your average capacity and subtract planned time off)
> - **Total current weights:** 10

#### UX Weight Definitions

| Weight | Design Tasks | User Research Tasks |
| ------ | ------------ | ------------------- |
| 1 | Mostly small UI changes leading to small incremental UX improvements. No users’ workflow involved in these changes. Requirements are clear and there are no unanswered questions. <i>For example: A copy experiment or changing a button styling.</i> | Synthesizing previous research findings and generating recommendations based on them. |
| 2 | Simple UI or UX change where we understand all of the requirements but may need to find solutions to known questions/problems. These changes should blend in with an actual user workflow. <i>For example: [Simplify Sign in / Register process the in trial flow](https://gitlab.com/gitlab-org/growth/product/-/issues/1471)</i>. | Running a first click test or other type of unmoderated research study |
| 3 | A well-understood change but the scope of work is bigger. Several pages are involved and/or we're starting to design/redesign small flows or connect existing flows between each other. Designers may conduct extensive background research (previous issues, support tickets, review past user research, review analytics, etc). Some unknown questions may arise during the work. <i>For example: [Update the CustomersDot checkout page to allow subscription and billing information input](https://gitlab.com/gitlab-org/growth/team-tasks/-/issues/96), [Experiment with adding a contact sales option in app](https://gitlab.com/gitlab-org/gitlab/-/issues/197235)</i>. | A moderated, narrowly scoped research study with specific questions to answer, such as a usability review of a single page |
| 5 | A complex change where input from group members is needed as early as possible. Spans across multiple pages, and we're working on medium-sized flows that potentially connect with another area of the product There are significant open questions that need to be answered. The product designer may need to do some research on their own or in collaboration with a researcher, but this isn't always the case. Possible research activities might be to find and/or validate a Job To Be Done, conduct user testing or card-sorting, or do a survey. <i>For example: UX Scorecard, [How can we improve the dismiss action in upgrade moments](https://gitlab.com/gitlab-org/gitlab/-/issues/213344)</i>. | A research study evaluating the usability of an end-to-end flow or multiple related features, or a usability study with a minor exploratory component |
| 8 | Complicated changes introducing a new user flow that connects with other large flows and may require input from other designers, product managers, or engineers from the same or another stage group. This is the largest flow design/redesign that we would take on in a single milestone. This requires research where the designer may or may not be working with a researcher to plan and conduct exploratory interviews or user testing sessions. <i>For example: [Onboard new signs up through an onboarding issue board](https://gitlab.com/gitlab-org/growth/product/-/issues/107)</i>. | An exploratory study investigating broad-based behaviors related to a single stage, including one or more distinct user groups |
| 13 | Highly significant changes impacting multiple user flows, a large new feature, and/or a complete redesign. This issue could significantly impact product strategy and would require critical input from others (the wider GitLab community, e-group, customers), and there are many unknowns. This necessitates research where the designer could team up with a researcher and other designers to gather input data, plan and conduct exploratory interviews, lead user testing sessions… It's unlikely we would commit to complete this issue in a milestone, and the preference would be to further clarify requirements and/or break it into smaller issues planned in several milestones. <i>For example: [An improved free trial sign-up experience for GitLab.com SaaS users](https://gitlab.com/groups/gitlab-org/-/epics/377)</i>. | An exploratory study investigating broad-based behaviors across multiple stages and multiple types of users, potentially involving team members from the different stages. |
