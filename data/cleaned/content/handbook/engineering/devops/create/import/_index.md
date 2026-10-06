---
title: Import Group
description: The Import Group facilitates migrations.
---

## About

The Import group is a part of the [Create Stage](/handbook/engineering/devops/create/).
The group supports the product by migrating between GitLab instances and from other providers.

This page covers processes and information specific to the Import group. See also the
[group direction page](https://about.gitlab.com/direction/create/import/) and the
[features we support per category](/handbook/product/categories/#import-group).

## How to reach us

To get in touch with the Import group, it's best to create an
issue in the [GitLab project](https://gitlab.com/gitlab-org/gitlab) and add the
`~"group::import"` label, along with any other [appropriate labels](#issue-labels). Then,
feel free to ping the relevant Product Manager and/or Engineering Manager.

For more urgent items, feel free to use the Slack Channel (internal): [`#g_import`](https://gitlab.slack.com/archives/g_import).

## Team Members

The following people are permanent members of the group:

{{< engineering/stable-counterparts role="Dedicated:Import" >}}

## Work

A week before each milestone, the Engineering Manager creates a
[planning issue](https://gitlab.com/gitlab-org/gitlab/-/work_items?sort=closed_at_desc&state=opened&label_name%5B%5D=Planning%20Issue&label_name%5B%5D=group%3A%3Aimport&first_page_size=100)
with the priorities for the team. The team members are notified, and proceed to update the issue
with their commitments for the milestone.

### Issue Development Workflow

We use the standard GitLab [engineering workflow](/handbook/engineering/workflow/).

### Issue Boards

The work for the Import group can be tracked in the following locations:

- [Import Current Milestone](https://gitlab.com/groups/gitlab-org/-/boards/1459244?milestone_title=Upcoming&milestone_title=Started&label_name%5B%5D=group%3A%3Aimport&group_by=epic) (manually adjust the milestone filter to the current milestone)
- [Planning issues](https://gitlab.com/gitlab-org/gitlab/-/work_items?sort=closed_at_desc&state=opened&label_name%5B%5D=Planning%20Issue&label_name%5B%5D=group%3A%3Aimport&first_page_size=100)
- [Planning issue epics](https://gitlab.com/groups/gitlab-org/-/work_items?sort=created_date&state=opened&label_name%5B%5D=Planning%20Issue&label_name%5B%5D=group%3A%3Aimport&type%5B%5D=epic&first_page_size=100)

### Issue Labels

To increase discoverability, apply the correct labels to issues.

All issues should have:

- `~"group::import"` (the bot will apply stage and section labels accordingly)
- One or more of the category labels:
  - `~"Category:Importers"` (FIXME: at the moment the bot forces all issues to have this category)
  - `~"Category:Webhooks"`
- A [type label](/handbook/product/groups/product-analysis/engineering/metrics/#work-type-classification)
- A [workflow label](/handbook/engineering/workflow/#updating-workflow-labels-throughout-development)
- `~"backend"` or `~"frontend"`, if appropriate

For issues related to importers, also apply an `Importer:` label. For example: `~"Importer:GitHub"` or `~"Importer:Direct Transfer"`.

### Backlog Refinement

Engineers typically refine the issues they plan to work on. However, anyone may refine an issue to
make it ready for development, especially if a community contributor might pick it up.

When an issue is part of an Epic, the DRI may refine it or delegate refinement to an engineer
assigned to that Epic. Regardless of who refines the issue, aim to complete refinement before the
milestone begins.

At the latest, refinement should start when the Engineering Manager shares the planning issue for
the next milestone, which happens a week before the end of the current milestone.

#### Identifying Issues for Refinement

The Engineering Manager schedules issues, which are then included in the milestone planning issue.

Based on each engineer's allocation for the milestone, identify issues that are not in `Ready for
Development` status. These typically have `Refinement` or `Planning breakdown` status, but may have any
[Product Development Flow](/handbook/product-development/how-we-work/product-development-flow/)
status.

Issues that are `Ready for Development` but were refined many months ago should be refined again
with a focus on changes in the codebase, product or architecture direction.

#### Refining Issues

Follow the Create stage [Cross-Team Planning and Refinement](/handbook/engineering/devops/create/#cross-team-planning-and-refinement) guidelines, specifically the [Refinement](/handbook/engineering/devops/create/#refinement) and [Implementation Plan](/handbook/engineering/devops/create/#implementation-plan) sections.

For the Import group, an issue is considered refined when it meets those guidelines plus the following Import-specific requirements:

- Weight (optional for `type::bugs`)
- Peer review by another engineer (optional for weight 1 issues); to show it's been reviewed, the reviewer can leave a comment or move the issue to `Ready for development`
- `Ready for development` status

**Bug readiness**

Bugs do not need to be perfectly understood before we work on them, and hence don't need a weight.

The effort to fully understand a bug is often most of the effort of fixing it. Consequently,
proposed solutions in bug issues may be considered **suggestions** made on an imperfect
understanding of the defect.

Try to include at least:

- Steps to reproduce
- Current behavior
- Expected correct behavior

The
[Bug template](https://gitlab.com/gitlab-org/gitlab/-/blob/master/.gitlab/issue_templates/Bug.md?ref_type=heads)
includes these fields.

### Requesting help

If you are not part of the Support organization, we recommend reaching out to them first, as they have greater availability and can assist with most common issues. There's a dedicated Slack channel [#spt_pod_import](https://gitlab.enterprise.slack.com/archives/C052K0Z1F8T) you can join, follow and ask questions in. However, there are times when in-depth technical knowledge is needed to resolve a customer issue, requiring the involvement of an engineer from the team.

Before requesting help from the Engineering team, please first review the [GitLab documentation](https://docs.gitlab.com/) for the topic of your interest and the additional resources listed below:

- [Importer Runbook](https://gitlab.com/gitlab-org/foundations/import-and-integrate/team/-/blob/main/importers/runbook.md?ref_type=heads)
- [GitLab Log Analysis Tool](https://gitlab.com/gitlab-org/foundations/import-and-integrate/gitlab-logs-analysis)
- [Jira playlist](https://www.youtube.com/playlist?list=PL05JrBw4t0Koazgli_PmMQCER2pVH7vUT)

If you cannot find the answer to your question in the resources listed above, please open a [Request for Help (RFH) issue](https://gitlab.com/gitlab-com/request-for-help/-/issues/new?issuable_template=SupportRequestTemplate-Import) and use the `SupportRequestTemplate-Import` template. Please ensure that you provide all the required information before reaching out to the team; otherwise, we will be unable to proceed with your request. New issues will be prioritized according to our internal triage process. Please note that we can only support requests for issues affecting the current and the two most recent minor GitLab versions (N-2). We cannot offer a fix for older versions. This is aligned with our [maintenance policy for backports](https://docs.gitlab.com/ee/policy/maintenance.html#patch-releases).

### Milestone Doctors

Each milestone, two backend engineers in the team are assigned the role of Milestone Doctor, one as Primary and the other as Secondary. The assignments are in the [Milestone Doctor rotation schedule](https://gitlab.com/groups/gitlab-org/-/work_items/21520#milestone-doctor---rotation-schedule). Engineers can freely trade upcoming shifts and update the schedule.

The Secondary doctor steps in when the Primary is OOO or over capacity, assuming the same responsibilities. Otherwise, they work on tasks planned for the milestone. The Primary doctor should let the Secondary know when they're OOO or facing capacity issues.

The milestone capacity for the primary Doctor is 100% assigned to the role responsibilities. If there are none left, the engineer should work on `~type::maintenance` or `~type::bug` issues, and consider increasing their code review capacity.

The current doctors can be tagged with `@gitlab-com/create-team/import/reaction-rotation`.

#### Responsibilities

- Engage with Support and PS on new [RFH issues](https://gitlab.com/gitlab-com/request-for-help/-/issues/?sort=popularity&state=opened&label_name%5B%5D=Help%20group%3A%3Aimport&first_page_size=100)
- Follow-up on long-lasting open issues
- Assist the Support team on customer calls
- Maintain team runbook documentation on how Milestone Doctors have successfully diagnosed problems
- Respond to questions in our team Slack channel [`#g_import`](https://gitlab.enterprise.slack.com/archives/C04RDL3MEH5)
- Update our [FAQ](https://gitlab.com/gitlab-org/foundations/import-and-integrate/team/-/blob/main/importers/faq.md?ref_type=heads) with any learnings from the shift
- Review [importer dependencies](#importer-dependencies), and create issues for required changes
  due to 3rd-party API changes.
- Monitor [`#import_exceptions`](https://gitlab.enterprise.slack.com/archives/C061EPC0RST) and the [Direct Transfer Kibana Dashboard](https://log.gprd.gitlab.net/app/dashboards#/view/f2640580-a8bd-11ed-85ed-e7557b0a598c) for errors; triage, escalate, and create follow-up issues as needed.
- Review the [error budget](#error-budgets) once per milestone, investigate regressions, and write follow-up issues for any findings.
- Update [membership of `@gitlab-com/create-team/import/reaction-rotation`](https://gitlab.com/groups/gitlab-com/create-team/import/reaction-rotation/-/group_members?with_inherited_permissions=exclude) at the end of the milestone.

##### Importer dependencies

Once per milestone, review each importer's dependency changelogs for upcoming breaking changes and
API deprecations. Use [GitLab Duo Chat](https://docs.gitlab.com/user/gitlab_duo_chat/) to assess
impact, and create an issue with the relevant `~"Importer:"` label for any change that requires an
update.

After the review, leave a comment in the planning issue with a summary and links to any issues
created; tag the EM for attention.

<details>
<summary>Suggested prompt</summary>

Replace `[START_DATE]` with the last date when the dependencies where checked.

```text
You are helping an engineer on the GitLab Import team perform a periodic review of third-party API dependencies. Our importers integrate with external services and we need to check their changelogs for any breaking changes, deprecations, or required migrations announced since [START_DATE].

Review the following changelog pages and identify any changes that could break or require updates to our importers:

**GitHub importer**
- Source: https://gitlab.com/gitlab-org/gitlab/-/tree/master/lib/gitlab/github_import
- Changelogs: https://docs.github.com/en/rest/about-the-rest-api/breaking-changes, https://github.blog/changelog/, https://github.com/octokit/octokit.rb/releases

**Bitbucket Cloud importer**
- Source: https://gitlab.com/gitlab-org/gitlab/-/tree/master/lib/bitbucket, https://gitlab.com/gitlab-org/gitlab/-/tree/master/lib/gitlab/bitbucket_import
- Changelogs: https://developer.atlassian.com/cloud/bitbucket/changelog/

**Bitbucket Server importer**
- Source: https://gitlab.com/gitlab-org/gitlab/-/tree/master/lib/bitbucket_server, https://gitlab.com/gitlab-org/gitlab/-/tree/master/lib/gitlab/bitbucket_server_import
- Changelogs: https://developer.atlassian.com/server/bitbucket/changelog/

**Gitea importer**
- Source: https://gitlab.com/gitlab-org/gitlab/-/blob/master/app/controllers/import/gitea_controller.rb (uses GitHub import client)
- Changelogs: https://github.com/go-gitea/gitea/blob/main/CHANGELOG.md, https://blog.gitea.com

**Jira importer**
- Source: https://gitlab.com/gitlab-org/gitlab/-/tree/master/lib/gitlab/jira_import
- Changelogs: https://developer.atlassian.com/cloud/jira/platform/changelog/, https://github.com/sumoheavy/jira-ruby/releases

**FogBugz importer**
- Source: https://gitlab.com/gitlab-org/gitlab/-/tree/master/lib/gitlab/fogbugz_import
- Changelogs: https://support.fogbugz.com/section/3113-articles

For each change you find, check the corresponding GitLab implementation to verify whether the change affects us.

Then, for each importer, list:
1. The name of the importer
2. Whether changes are required
3. A summary of the required change (for changes that do not affect us, simply provide a link to
   the announcement)
4. The due date or enforcement date

If no actionable changes are found, confirm that and note the date range you checked.
```

</details>

### Working with Security

The group has an existing [threat model](https://gitlab.com/gitlab-com/gl-security/product-security/appsec/threat-models/-/blob/master/gitlab-org/gitlab/GitLab%20Migration.md) to assist in identifying issues that may have security implications, but there are other considerations.

An [Application Security Review](/handbook/security/product-security/security-platforms-architecture/application-security/appsec-reviews/) should be requested when the issue or MR might have security implications. These include, but aren't limited to, issues or MRs which:

- falls under the threat model
- handles binary files (downloading, decompressing, extracting, moving, deleting)
- modifies or uses file manipulation services
- uses methods from Import/Export `CommandLineUtil`

### Longer lived feature flags

This is a supplement to GitLab's common [development guidance](https://docs.gitlab.com/ee/development/feature_flags/)
for use of feature flags. It applies to all flag types besides the [`ops` type](https://docs.gitlab.com/ee/development/feature_flags/#ops-type).

Changes to Import features often happen in high-traffic code paths and have
led to outages on GitLab.com in the past. Outages are often to do with resource contention that can
be difficult to see ahead of time in code review or in QA testing.

- Large imports can trigger thousands of workers.
- Integrations and webhooks are executed millions of times a day.
- Contention problems sometimes do not surface immediately, and only when large customers trigger the new code path.

For this reason we should prefer to keep feature flags in the codebase for a longer period of time than normal.
During this time the flag is enabled by default but can still be disabled quickly in the event of an incident.

In the past, we were able to quickly mitigate several incidents by disabling the feature:

- [2023-09-21: Group import allows impersonation of users in CI pipelines](https://gitlab.com/gitlab-sirt/shared-incidents/incident_4304/-/issues/1)
- [2023-10-30: GitLab.com is down](https://gitlab.com/gitlab-com/gl-infra/production/-/issues/17054)
- [2024-01-30: Sidekiq Apdex SLO](https://gitlab.com/gitlab-com/gl-infra/production/-/issues/17504)

For changes within importers, integrations or webhooks we should prefer to:

1. Roll out the flag with `/chatops` as normal.
1. QA the changes using large data to proactively flush out any problems at scale.
   For importers, see [our runbook](https://gitlab.com/gitlab-org/manage/import-and-integrate/team/-/blob/main/importers/runbook.md)
   for tips.
1. When you come to release the feature, change the feature flag to be `default_enabled: true`
   rather than to remove it. This is the
   [optional release the feature with the flag](https://gitlab.com/gitlab-org/gitlab/-/blob/e730c474ed80143ebae33df90900b342020ad7c0/.gitlab/issue_templates/Feature%20Flag%20Roll%20Out.md?plain=1#L83)
   step on the flag rollout issue.
1. At this point the feature is considered released within the milestone, and can be
   announced in the release post as it will ship to self-managed customers.
1. **Wait between 1-3 weeks** where the flag exists in the codebase but remains enabled by default.
   Use the longer period for changes in areas of more contention, or if you feel it may take
   longer to detect problems for any reason.
1. After that period, remove the feature flag to complete the flag rollout process.

### During a release

- When an issue is introduced into a release after Kickoff, an equal amount of weight must be removed to account for the unplanned work.
- Development should not begin on an issue before it's been estimated and given a weight.
- By the 15th, engineering merge requests should be merged. In other words, we assume code merged after the 15th will not be in the release. That allows time for the release to be finalized, and any associated [release posts](https://docs.gitlab.com/development/documentation/release_notes/) to be merged by the 17th. (This is an [experiment starting with 13.11](https://gitlab.com/gitlab-org/manage/general-discussion/-/issues/17330).)

### Release posts

For issues which need to be announced in more detail, a release post can be automatically created using the issue.
When working on an issue, either in planning, or during design and development, you can use the
[release notes writer agent](https://gitlab.com/components/agents-and-flows/release-notes-writer)
to have the release post created and notify all the relevant people.

If you do not want an issue to have a release post, make sure that the issue does not have a
release notes section or do not use a `release post item::` label.

### Proof-of-concept MRs

We strongly believe in [Iteration](/handbook/values/#iteration) and delivering value in small increments. Iteration can be hard, especially when you lack product context or are working on a particularly risky/complex part of the codebase. If you are struggling to estimate an issue or determine whether it is feasible, it may be appropriate to first create a proof-of-concept MR. The goal of a proof-of-concept MR is to remove any major assumptions during planning and provide early feedback, therefore reducing risk from any future implementation.

- Create an MR, prefixed with `PoC:`.
- Explain what problem the PoC MR is trying to solve for in the MR description.
- Timebox it. Can you determine feasibility or a plan in less than 2-3 days?
- Identify a reviewer to provide feedback at the end of this period.
- Close the MR. Provide a summary in the original issue on what you learned from the PoC, including product and performance implications.
  - State whether you are able to move forwards with implementation or not.
  - Please do not close the issue.

The need for a proof-of-concept MR may signal that parts of our codebase or product have become overly complex. It's always worth discussing the MR as part of the retrospective so we can discuss how to avoid this step in the future.

### Retrospectives

We have 1 regularly scheduled "Per Milestone" retrospective, and can have ad-hoc "Per Project" retrospectives.

#### Per Milestone

The Import group conducts [milestone retrospectives in GitLab issues](https://gitlab.com/gl-retrospectives/manage-stage/import/-/work_items). These include the engineers, UX, PM, and
all stable counterparts who have worked with that team during the milestone.

Participation by our team members is highly encouraged for every milestone.

These are confidential during the initial discussion, then made public in time
for each month's [GitLab retrospective](/handbook/engineering/careers/management/group-retrospectives/). For more information, see [group retrospectives](/handbook/engineering/careers/management/group-retrospectives/).

#### Per Project

If a particular issue, feature, or other sort of project turns into a
particularly useful learning experience, we may hold a synchronous or
asynchronous retrospective to learn from it. If you feel like something you're
working on deserves a retrospective:

1. [Create an issue](https://gitlab.com/gitlab-org/manage/import-and-integrate/discussions/-/issues) explaining why you want to have a retrospective and indicate whether this should be synchronous or asynchronous.
1. Include your EM and anyone else who should be involved (PM, counterparts, etc).
1. Coordinate a synchronous meeting if applicable.

All feedback from the retrospective should ultimately end up in the issue for reference purposes.

### Tech Leads

Our group works with tech leads to help organize work on different topics and identify DRIs for them.

#### Characteristics of a Tech Lead

A tech lead is:

- an individual contributor with additional responsibilities. Every engineer regardless of their seniority is qualified to be a tech lead.
- a temporary role that is tied to a specific topic/project. We allow the team to have multiple tech leads at the same time for different topics/projects.
- **not** a manager.
- **not** an additional seniority level.

The Tech Lead role provides growth opportunity for engineers who are interested in adopting leadership skills.

#### Responsibilities of a Tech Lead

Tech leads wear many hats. Their responsibilities may differ from project to project but may include:

- Technical Vision and Architecture - Defining and evolving the overall technical architecture for a given project
- Technical Guidance - Providing technical guidance and mentoring to other developers on the team
- Planning and Prioritizing Work - Organizing the work by breaking down bigger tasks into smaller actionable items
- Tracking Progress -  Tracking progress on commitments and reporting status updates
- Risk Management - Identifying, assessing and managing technical risks that may impact deliverables
- Coordination - Overseeing the work of others and helping remove blockers
- Technical documentation - Maintaining documentation of the technical architecture and code structure for other developers

#### Current Tech Leads

Below is an overview of topics that are overseen by a tech lead:

| Topic | Tech Lead | Topic Link | Notes |
| ------ | ------ | ------ | ------ |
| Direct Transfer - User contribution mapping | Rodrigo Tomonari | [Epic](https://gitlab.com/groups/gitlab-org/-/epics/12378) | - |
| Improve the efficiency of developer contributions to the importers | James Nutt | [OKR](https://gitlab.com/gitlab-com/gitlab-OKRs/-/work_items/6658) | - |
| Congregate | tbd | https://gitlab.com/gitlab-org/gitlab/-/issues/428657 | |
| GitHub Actions | tbd | https://gitlab.com/gitlab-org/manage/general-discussion/-/issues/17652 | |
|  | | |  |

## Merge request roulette reviews

When areas of the Import codebase are changed, the [reviewer roulette](https://docs.gitlab.com/ee/development/code_review.html#reviewer-roulette)
will recommend that the merge request is reviewed by an Import team member. This will only happen when the merge request is
authored by people outside of the Import team. See [this example](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/74338#note_731247058) of how the review recommendation looks.

The [reasoning](https://gitlab.com/gitlab-org/gitlab/-/issues/343486) behind these special recommendations
is that other groups have some ownership of certain integrations or webhooks. Reviewing
changes made by non-team members allows us to act as owners of foundational code and maintain
a better quality of the Import codebase.

### How roulette matches work

File paths of changes in a merge request are matched against a
[list of regular expressions](https://gitlab.com/gitlab-org/gitlab/-/blob/240d4c37c955878c224718e47f4d527bea250299/tooling/danger/project_helper.rb#L42-62).
The roulette uses these hash values to recommend reviewer groups. For example, `:import_integrate_be` and
`:import_and_integrate_fe` will recommend Import backend and frontend reviews respectively. As the regex matches
are [first match wins](https://gitlab.com/gitlab-org/gitlab/-/blob/54e182410219d1c77c5c6b2b7c88a6639f622cc6/tooling/danger/project_helper.rb#L18)
and not cumulative, any other relevant reviewer groups like `:backend` or `:frontend` must also be included
in each hash value.

The regex list should be updated to match integrations or webhooks code whenever needed. The list matches our
commonly namespaced files, so new code in existing namespaces will always match.

To see which files in the GitLab repository produce a match, paste the following in a Rails console:

```ruby
require Rails.root.join('tooling/danger/project_helper.rb')

ALL_FILES = Dir.glob('**/*');

def category_regexs(category)
  matching_categories = Tooling::Danger::ProjectHelper::CATEGORIES.select do |regexs, categories|
    next if regexs.is_a?(Array)

    Array.wrap(categories).include?(category)
  end

  regexes = matching_categories.map(&:first)
  Regexp.union(*regexes)
end

def print_files(category)
  regex = category_regexs(category)

  puts ALL_FILES.grep(regex).reject { |path| File.directory?(path) }.sort
end

puts "Backend:\n"
print_files(:import_integrate_be)

puts "Frontend:\n"
print_files(:import_integrate_fe)
```

## Monitoring

This is a collection of links for monitoring our features.

### Grafana dashboards

- [Import group dashboard](https://dashboards.gitlab.net/d/stage-groups-import/stage-groups-import-group-dashboard?orgId=1) which contain:
  - Links to various Kibana logs, filtered to our feature categories
  - Our [error budget](#error-budgets) spend attribution
- [Worker queues](https://dashboards.gitlab.net/d/sidekiq-queue-detail/sidekiq-queue-detail?orgId=1&var-PROMETHEUS_DS=Global&var-environment=gprd&var-stage=main&var-queue=jira_connect:jira_connect_sync_branch) where you can switch queues with the `queue` dropdown

### Sentry errors

- [Matching "IntegrationsController"](https://new-sentry.gitlab.net/organizations/gitlab/issues/?project=3&query=is%3Aunresolved+IntegrationsController&referrer=issue-list&statsPeriod=14d)
- [Matching "Integrations"](https://new-sentry.gitlab.net/organizations/gitlab/issues/?project=3&query=is%3Aunresolved+Integrations&referrer=issue-list&statsPeriod=14d)
- [Matching "Jira"](https://new-sentry.gitlab.net/organizations/gitlab/issues/?project=3&query=is%3Aunresolved+Jira&referrer=issue-list&statsPeriod=14d)

### Kibana dashboards

See a [list of all Import Kibana dashboards](https://log.gprd.gitlab.net/app/dashboards#/list?s=tag:(group::import)&sort=title&sortdir=asc).

Importer dashboards:

- [Project Import/Export](https://log.gprd.gitlab.net/app/dashboards#/view/03a11c50-ba46-11ec-b73f-692cc1ae8214)
- [GitHub Import - Overview](https://log.gprd.gitlab.net/app/dashboards#/view/62965d10-9c0e-11ed-9f43-e3784d7fe3ca)
- [GitHub Import - Project import debug](https://log.gprd.gitlab.net/app/dashboards#/view/be0fb6d0-9c24-11ed-85ed-e7557b0a598c)
- [GitLab Direct Transfer](https://log.gprd.gitlab.net/app/dashboards#/view/f2640580-a8bd-11ed-85ed-e7557b0a598c)
- [User contributions mapping](https://log.gprd.gitlab.net/app/dashboards#/view/f9c66d73-50a1-43e2-89ab-56b71645df33)

API/Webhooks dashboards:

- [REST and GraphQL API](https://log.gprd.gitlab.net/app/dashboards#/view/ee792100-cfc7-11ec-afaf-2bca15dfbf33)
- [Webhooks](https://log.gprd.gitlab.net/app/dashboards#/view/deec2320-3914-11ed-b86b-d963a1a6788e)

### Kibana logs

GitLab for Jira Cloud app workers:

- [`JiraConnect::SyncMergeRequestWorker`](https://log.gprd.gitlab.net/goto/309f97d4a5c3e918e2c07754fefc94ee) errors.
- [`JiraConnect::SyncBranchWorker`](https://log.gprd.gitlab.net/goto/96364e957898896c4dc7e9ee5534b6de) errors.
- [`JiraConnect::SyncProjectWorker`](https://log.gprd.gitlab.net/goto/5f0e03847ddc1b074d6346199c8bc4d2) errors.
- [All JiraConnect sync worker](https://log.gprd.gitlab.net/goto/39348f2d169e6929c41dba2d6fb063ee) timeout errors.

### Error budgets

GitLab uses [error budgets](/handbook/engineering/error-budgets/) to measure the availability and performance of our features.
Each engineering group has its own budget spend. The current 28-day spend for the Import team
shows in this [Grafana dashboard](https://dashboards.gitlab.net/d/stage-groups-import/stage-groups-import-group-dashboard?orgId=1).

Error budget spend happens when either of the following exceeds a certain threshold:

- Error rate of an endpoint or worker
- Apdex (latency) of an endpoint

#### Determine the highest-impact fixes

To determine the highest-priority problems in our [Grafana dashboard](https://dashboards.gitlab.net/d/stage-groups-import_and_integrate/stage-groups-import-and-integrate-group-dashboard?orgId=1):

1. Go to the **Error budget** panel.
1. Expand **Budget spend attribution**. The **Budget failures** panel is ordered by top failures.
1. In **Failure log links**, click the corresponding links.

Fixing the top offenders will have the biggest impact on the budget spend.

#### Further resources

Learn more about error budgets with these resources:

- [Error budgets and how they are calculated](/handbook/engineering/error-budgets/)
- [What Apdex is and how it works](https://docs.gitlab.com/ee/development/application_slis/rails_request.html)
- [Error budget in Grafana dashboards](https://docs.gitlab.com/ee/development/stage_group_observability/index.html#error-budget)
- [Feature categorization](https://docs.gitlab.com/ee/development/feature_categorization/): our code is attributed to us by `feature_category: :integrations`, `feature_category: :importers`, and `feature_category: :webhooks`

## Usage data dashboards

You can view data for feature usage in Tableau.

- [Centralized Product Usage Metrics Dashboard](https://10az.online.tableau.com/#/site/gitlab/views/DRAFTCentralizedGMAUDashboard/MetricReporting?:iid=1) can be used to observe any chosen metric. To see data for e.g. Microsoft Teams integration, on the left in `Select Metric Level` choose `PI`, in the `Select Metrics to view` first uncheck `All` and then search for `microsoft` and check metrics for Microsoft Teams integration you're interested in, see [example](https://10az.online.tableau.com/t/gitlab/views/DRAFTCentralizedGMAUDashboard/MetricReporting/8c7d8afd-ffc7-4198-b11a-6099df2b8611/3170c5bb-4509-4b3d-8362-470e49286d42). You can choose timeframe and `Dimention Paremeter`, e.g deployment type. Another example is data for [GitHub importer](https://10az.online.tableau.com/t/gitlab/views/DRAFTCentralizedGMAUDashboard/MetricReporting/57ab6fbb-7d64-4ab9-ac36-dfcfbd891c69/1e04a888-66de-44c8-b722-1c31e214b8db) or [webhooks usage by deployment](https://10az.online.tableau.com/t/gitlab/views/DRAFTCentralizedGMAUDashboard/MetricReporting/ef4c4285-1a54-4769-86d7-60331b44a10a/0fa98245-8e1c-4db1-82f3-2591e310aa3d)
- [Integrations Usage Dashboard](https://10az.online.tableau.com/#/site/gitlab/views/ManageIntegrationsUsage/ServicePingResults?:iid=1) shows all usage of integrations. You can filter in or out (keep only or exclude) any specific integration on the right hand side.
- [Importer Usage Dashboard](https://10az.online.tableau.com/#/site/gitlab/workbooks/2214374/views). This is still work in progress.
- [User Contribution Mapping Usage Dashboard](https://10az.online.tableau.com/#/site/gitlab/workbooks/3238494/views) shows data on placeholder users created during imports.

## Links and resources {#links}

{{% include "includes/engineering/foundations/shared-links.md" %}}

- [Milestone retrospectives](https://gitlab.com/gl-retrospectives/manage-stage/import/-/work_items)
- Our Slack channels
  - Create:Import [#g_import](https://gitlab.slack.com/archives/C04RDL3MEH5)
  - Daily standups [#g_import_daily](https://gitlab.slack.com/archives/C04UYQV7716)
- Issue boards
  - [Current milestone board](https://gitlab.com/groups/gitlab-org/-/boards/1459244?milestone_title=Upcoming&label_name[]=group%3A%3Aimport%20and%20integrate)
- Contribution guides
  - [Principles of importer design](https://docs.gitlab.com/ee/development/import/principles_of_importer_design/)
  - [Contributing to Direct Transfer](https://docs.gitlab.com/ee/development/bulk_imports/contributing/)
    - [Feedback issue](https://gitlab.com/gitlab-org/gitlab/-/issues/456468)
- Onboarding videos (GitLab Unfiltered Youtube)
  - [Direct Transfer](https://www.youtube.com/watch?v=vVQ6Ex9fSl8) (formerly known as GitLab Migration)
  - [Introduction to GitHub Importer](https://www.youtube.com/watch?v=TxHopzXop5s)
  - [File based GitLab Import/Export](https://www.youtube.com/watch?v=A4kdpnbhmcw)
  - [Remote S3 Import Example](https://www.youtube.com/watch?v=I85SXNmiS_k)
