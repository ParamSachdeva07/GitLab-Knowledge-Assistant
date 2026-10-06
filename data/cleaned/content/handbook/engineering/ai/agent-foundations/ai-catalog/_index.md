---
title: AI Catalog Group
description: "The AI Catalog Group is focused on developing AI Catalog, a catalog of Agents, tools, and flows that can be created, curated, and shared across organizations, groups, and projects."
---

## Overview

The AI Catalog Group is focused on building the surface where GitLab users discover, evaluate, enable, and manage AI-powered objects - including agents, flows, MCP servers, and skills. We are responsible for the catalog experience across Explore, Group, and Project scopes, working across product, design, and engineering to define how AI objects are created, curated, surfaced, trusted, and put to work.

## Team members

{{% product/section-group-table "AI Catalog" %}}

## How to reach us

Depending on the context here are the most appropriate ways to reach out to the AI Catalog group:

* Slack Channel: `#g_ai_catalog`
* GitLab group `@gitlab-org/ai-powered/ai-catalog/engineering` (just engineers)

## What we're working on

TBD

## What we own

* The [GitLab for Slack app](https://docs.gitlab.com/user/project/integrations/gitlab_slack_application/)
  is owned by the External Agents feature team
  ([`#f_external-agents`](https://gitlab.enterprise.slack.com/archives/C0B4V7TJPG9))
  within this group. See the
  [release and manifest process](/handbook/engineering/ai/agent-foundations/ai-catalog/slack-app-release-process/).

## How we work

We're just getting started and will be defining how we work as we settle in to the new team.
Here are some links to get us started:

* [Root Epic](https://gitlab.com/groups/gitlab-org/-/epics/11111): For grouping all the work and setting out a roadmap
* [Issue board](https://gitlab.com/groups/gitlab-org/-/boards/11420787?label_name%5B%5D=group%3A%3Aai+catalog&milestone_title=Started#/): For all in-flight issues
* [Team tasks](https://gitlab.com/gitlab-org/ai-powered/ai-catalog/team-tasks/-/issues): For all non-product related team issues
* [Async updates](https://gitlab.com/gitlab-org/ai-powered/ai-catalog/team-tasks/-/issues/?label_name%5B%5D=async%20update)
* [Team Wiki](https://gitlab.com/gitlab-org/ai-powered/ai-catalog/team-tasks/-/wikis/home): For product decisions and useful information

### DRIs

When working on a large project, we'll split it into epics and issues.
The Directly Responsible Individual (DRI) for each epic serves as the single point of accountability for that domain.
The DRI doesn't necessarily do all the work, but owns the success of their epic.

DRI responsibilities:

1. Answer questions about epic status, scope, and technical decisions
2. Maintain accurate epic and issue descriptions
3. Monitor and [communicate delivery health status](#status-updates)
4. Curate the issue list. Include what's needed and remove what isn't
5. Coordinate with other DRIs when work spans multiple epics

### How we handle requests for help

When a customer is experiencing an issue with the catalog, our support team will
raise a [request for help](https://gitlab.com/gitlab-com/request-for-help).
If you wish to raise a request for help please read [this readme](https://gitlab.com/gitlab-com/request-for-help#please-read-the-following-before-submiting-a-request-for-help-to-the-gitlab-development-team-sections) for instructions on how and when to do so.

To handle requests for help in a timely manner without distracting the whole team, we nominate a goalkeeper for each milestone.
The goalkeeper is responsible for ensuring that incoming requests, questions, and issues are triaged and directed to the appropriate people or teams.

Each milestone, we assign a new goalkeeper and open a goalkeeping issue.

You can find more information in the [issue template](https://gitlab.com/gitlab-org/ai-powered/ai-catalog/team-tasks/-/blob/main/.gitlab/issue_templates/goalkeeper.md).

### Communication

The AI Catalog Team communicates based on the following guidelines:

* Always prefer async communication over sync meetings.
* Don't shy away from arranging a [sync call](/handbook/communication/#video-calls) when async is proving inefficient, however always record it to share with team members.
* By default communicate in the open.
* Prefer public channels (`#g_ai_catalog`) over private message for work-related Slack messaging.
* Use `#g_ai_catalog` to share progress, ideas, and demos across functional teams.
* When you finish a piece of work, record a short video or demo and share it in `#g_ai_catalog`.

### Frontend-Backend collaboration

We aim to foster high levels of collaboration between frontend and backend engineers to ensure
development velocity and code quality.

* **Schema-first development**: Before implementation begins, frontend and backend engineers collaborate
  to design a GraphQL API schema based on UI requirements, user experience needs, and performance considerations.
* **Parallel development processes**: Once the schema is agreed upon, the frontend can proceed
  using mock data, mock endpoints, or API stubs that match the agreed schema. The backend can
  focus on implementing the data model, business logic, and actual API schema.
* **Maintaining alignment**: We value great communication. When requirements or schema need to change, we communicate
  early through the relevant GitLab issue or in [`#g_ai_catalog`](https://gitlab.enterprise.slack.com/archives/C08T5J1KXKQ)
  so our frontend or backend counterparts stay informed of all changes and can provide feedback early to avoid late-stage blockers.

### AI stage collaboration

The AI Catalog relies on the
[Workflow Service](https://gitlab.com/gitlab-org/modelops/applied-ml/code-suggestions/ai-assist/-/tree/main/duo_workflow_service?ref_type=heads)
as a foundational backend service.
Most AI Catalog features require new capabilities to be developed within Workflow Service,
which means our engineers will need to contribute directly to that codebase in partnership with the
other teams within [Agent Foundations](../_index.md).

**Collaboration Requirements:**

* All Workflow Service contributions must be developed in close partnership with the Agent Foundations team
* Our implementations must align with their service architecture and vision
* We commit to supporting Workflow Service's broader goals and adhering to their technical standards

**Collaboration Process:**

* Reach out to relevant Agent Foundations contacts (listed below) during the planning phase
* Join their [`#g_duo-agent-platform`](https://gitlab.enterprise.slack.com/archives/C07035GQ0TB) channel
* Follow our [async communication preferences](#communication) by default, but schedule sync meetings
  when needed and ensure key outcomes are documented in GitLab issues

#### Primary Agent Foundations contacts

| Team Member | Expertise Area |
| --- | --- |
| [Mikołaj Wawrzyniak](https://gitlab.com/mikolaj_wawrzyniak) | Workflow Service architecture |
| [Frédéric Caplette](https://gitlab.com/f_caplette) | Client-side implementation |
| [Dylan Griffith](https://gitlab.com/DylanGriffith) | Workflow Executor architecture: remote execution environment and runner implementation |
| [Jessie Young](https://gitlab.com/jessieay) | Authorization and authentication |
| [Shekhar Patnaik](https://gitlab.com/shekharpatnaik)  / [Igor Drozdov](https://gitlab.com/igor.drozdov) | Duo Chat agent integration |
| [Sebastian Rehm](https://gitlab.com/bastirehm) | Engineering Manager, backup contact for any of the above |

### Planning cadence

We plan and align our work to GitLab's [product milestones](/handbook/product/product-processes/milestones/). Milestone planning happens during the week before the start of the next milestone.

Issue breakdown and [weighting](#weighting) must be completed during the planning week, before the
milestone starts. Issues and epics that have not been broken down and weighted cannot be committed
as `~Deliverable`.

If an issue or epic cannot be broken down within the planning time frame, add a `Spike` issue to the
milestone to cover the exploration and collaboration with Product and Design as part of the milestone
work. Update the epic and add further issues based on the outcome of the spike.

We plan holistically across `~"category:ai catalog creation"` and `~"category:ai catalog curation"`.
If one team needs more capacity, it can borrow from the other team.

### ~Deliverable and ~Stretch labels

Every issue assigned to a milestone is triaged and labeled either `~Deliverable` or `~Stretch`.
These labels apply to issues only. Epics should never be tagged `~Deliverable` or `~Stretch`
(see [Epics in a milestone](#epics-in-a-milestone)).

* `~Deliverable`: work the team has committed to complete within the milestone. These issues must have a [weight](#weighting).
* `~Stretch`: work that has been triaged but is not committed. Stretch issues are picked up once all
  `~Deliverable` issues are complete (see [Prioritization](#prioritization)).

The `~Deliverable` label serves multiple purposes:

* **Commitment signal**: Communicates to stakeholders and customers that we intend to complete this work in the milestone
* **Prioritization**: Helps team members identify which issues should be worked on first
* **Focus**: Clarifies which work is essential vs nice-to-have for the milestone

#### Who applies it and when

The Engineering Manager applies the `~Deliverable` and `~Stretch` labels during the planning process before the start of a milestone.
This decision is made in collaboration with the Product Manager based on:

* Team capacity for the milestone
* Issue estimates and complexity
* Strategic priorities and customer commitments

### Epics in a milestone

Epics are not tagged `~Deliverable` or `~Stretch`; those labels apply to issues only.

* An epic committed to the current milestone should only contain issues that are also committed to that milestone.
* If an epic is larger than a single milestone, it should be broken down into sub-epics (iteration 1, 2, etc.)
  so that each iteration fits within a milestone.

### Prioritization

Issues with the `~Deliverable` label take priority over other work in the milestone.
Team members should:

1. First, work on assigned `~Deliverable` issues in the current milestone
2. If all `~Deliverable` issues are complete or blocked, pick up `~Stretch` issues from the milestone
3. Consult with the Engineering Manager if priorities are unclear or if a `~Deliverable` issue needs to be deprioritized

**During the milestone:**

* If a `~Deliverable` issue becomes blocked or cannot be completed, communicate this early in `#g_ai_catalog` or the relevant issue
* The Engineering Manager may adjust `~Deliverable` and `~Stretch` labels during the milestone based on changing priorities or capacity

### Limiting work in progress

* Each functional team works on one delivery epic at a time, plus one epic in refinement or spike.
* The second epic, along with bugs and maintenance issues, is filler work for when the main epic is blocked.
* Rule of thumb: each team runs fewer workstreams than it has people.
* We limit the number of issues in `~"workflow::in dev"` to (number of people x 2) - 1. We cap issues
  in development, not open MRs. Example: a team of 3 engineers has at most 5 issues in development at
  a time.

### Weighting

Issues are weighted using the Fibonacci sequence (0, 1, 2, 3, 5, 8+):

* **Weight 1:** Simple issues with minimal uncertainty (good for new contributors)
* **Weight 2:** Straightforward issues requiring multiple code/test updates
* **Weight 3:** Larger issues with some complexity but manageable scope
* **Weight 5:** Should typically be broken down
* **Weight 8+:** Placeholder weights indicating need for breakdown; too large or uncertain for immediate implementation

During the planning week, each functional team reviews the weights on the issues proposed for the next
milestone together. Every issue in `~"workflow::in dev"` must have a weight.

When an issue is a big miss (for example, weighted 1 but took about 2 weeks), the assignee looks back
and asks what was missed: hidden complexity, unclear scope, a dependency, or being blocked on another
team. We bring these lessons to the next retrospective.

### Status updates

Everyone provides a weekly async status update on their `~Deliverable` and `~Stretch` issues and epics, by Friday or sooner if it makes more sense:

* Use [this template](https://gitlab.com/-/snippets/6052232) for the update comment.
  A manual Weekly Status comment posted in the last 6 days skips the AI-generated weekly summary.
* Updates are expected on issues that take 3 or more days of work. Issues completed within a day or
  two do not need an update.
* When an epic is the main `~Deliverable` and its child issues are all small (less than 3 days of work),
  post the weekly update on the epic itself.
* Keep the `workflow::` label and health status up to date, and make sure the assignee (DRI) is clear.
  If a health status rating does not match reality, update it manually.

### Before you go on PTO

* Anyone going on PTO for more than 3 business days creates an
  [engineering coverage issue](/handbook/engineering/#1-creating-an-engineering-coverage-issue).
* They leave a short handover note on each of their open MRs and issues.

### Our tech stack

* GraphQL [backend](https://docs.gitlab.com/development/api_graphql_styleguide/) and
  [frontend](https://docs.gitlab.com/development/fe_guide/graphql/). All new schema items must be
  [marked experimental](https://docs.gitlab.com/development/api_graphql_styleguide/#mark-schema-items-as-experiments)
  to let us making breaking changes when we need.
* GraphQL [subscriptions](https://docs.gitlab.com/development/fe_guide/graphql/#subscriptions) rather than polling.
* Read the [AI Catalog Backend Architecture](/handbook/engineering/architecture/design-documents/ai_catalog/) design document (authored February 2026).

## UX Principles

See our [UX principles](/handbook/engineering/ai/ai-catalog/ux-principles/) for the AI Catalog that guide every design and engineering decision.
It is intended as a reference point for anyone contributing to the catalog to align on intent before making tradeoffs.

## Team meetings

### AI Catalog: Group meeting

* **Time**: Every Tuesday, alternating weekly between 05:30 UTC and 15:00 UTC.
* **Purpose**: This meeting serves as a general sync meeting to bring up any current issues and blockers.
* **Agenda**: [Google Doc (internal only)](https://docs.google.com/document/d/19zrzqN37ZVwwEJ9iYhy4QBsUzVN0Hd1j1yn8J0v4dqE)
* **Recordings**: [Google Drive (internal only)](https://drive.google.com/drive/folders/1I9s96jg9knqOwDLabhn9100H-MsvG2ne)
