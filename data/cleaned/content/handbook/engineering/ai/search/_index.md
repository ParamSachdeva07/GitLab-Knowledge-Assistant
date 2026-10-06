---
title: Global Search Group
description: "The Global Search team is focused on bringing world class search functionality to GitLab.com and self-managed instances."
---

## Vision

The Global Search Group focuses on bringing world class search functionality to GitLab.com and self-managed instances.

This page covers processes and information specific to the Global Search group. See also the [Global Search](https://about.gitlab.com/direction/global-search/) and [Code Search](https://about.gitlab.com/direction/global-search/code-search/) direction pages.

## Mission

The group is responsible for improving and expanding upon our current global search implementations using Elasticsearch, PostgreSQL, Zoekt, and Gitaly. Areas of responsibility will include global search functionality, UI, ingestion mechanisms, optimal indexing, administrative tools, and installation mechanisms for self-managed installations.

Additionally, we build and maintain critical AI context infrastructure, principally **GitLab Zoekt** — GitLab's scalable exact code search service and file-based database system, with flexible architecture supporting various AI context use cases beyond traditional search. It's built on top of open-source code search engine Zoekt.

These systems will be fundamental to providing high-quality context for AI features via Retrieval Augmented Generation work, which includes:

- Identifying and preparing new useful data for our AI-powered features in collaboration with feature teams and the AI Framework team
- Storing vector embeddings of epics, issues, MRs, source code, and more
- Providing retrieval APIs for those vector embeddings, metadata filtering, and ensuring permissions are enforced
- Enabling fast, precise code search and context retrieval essential for AI context

This team doesn't own custom searches for specific features, such as the "filter bar" on issues which is part of the [Issue Tracking](https://about.gitlab.com/direction/plan/project_management/team_planning/) category owned by the [Project Management group](/handbook/product/categories/#project-management-group).

## Team Members

The following team members are permanent members of the Global Search Group. John Mason is the group's acting Engineering Manager.

<!--
This list is maintained by hand. `group-by-slugs` matches each argument exactly against the
`slug` field in team.yml, and a slug that no longer matches is skipped silently -- the page
builds green with that person simply missing. Re-check the slugs whenever membership changes.

Slugs come from the file names under data/team_members/person in
https://gitlab.com/gitlab-com/www-gitlab-com

The same roster is also listed by hand on
content/handbook/engineering/data-engineering/analytics/platform-insights.md -- update both.
-->

{{< group-by-slugs john-mason rkumar555 siddharthdungarwal >}}

## Stable Counterparts

The following members of other functional teams are our stable counterparts:

| **Name**                                                 | **Role** |
| ---------------------------------------------------------| ------------------------------------------------------------------------------- |
| [Ashraf Khamis](/handbook/company/team#ashrafkhamis)     | [Senior Technical Writer](/job-description-library/product/technical-writer/) |
| [Cleveland Bledsoe Jr](/handbook/company/team#cleveland) | [Senior Support Engineer](/job-description-library/engineering/support-engineer/) |
| [Brenda Nyaringita](/handbook/company/team#bnyaringita)  | [Support Engineer(EMEA)](/job-description-library/engineering/support-engineer/) |

## Shared Responsibilities

The Global Search team shares responsibilities with the AI Framework team in the area of ![Retrieval Augmented Generation](/images/handbook/engineering/ai/search/rag_ownership_framwework.png) (RAG). Specifically, we will collaborate in the data preparation stage and information retrieval stage of the RAG process.

## AI Context Infrastructure and Advanced Search data stores

![Global Search data stores and interfaces diagram](/images/global_search_interfaces.png)

The Global Search team maintains several key systems that power both traditional search and AI context capabilities:

### Core Infrastructure Components

- **Elasticsearch**: Powers Advanced Search functionality with full-text search, aggregations, and vector similarity search capabilities
- **GitLab Zoekt**: GitLab's scalable file-based database system providing exact code search with enterprise-scale performance (48+ TiB indexed on GitLab.com). Beyond code search, Zoekt's flexible architecture serves as a foundation for various AI context use cases

These systems work together to provide comprehensive search and AI context capabilities, from traditional keyword search to sophisticated vector similarity matching for AI features.

### Infrastructure ownership and DRIs

Service ownership is declared in the [runbooks service catalog](https://gitlab.com/gitlab-com/runbooks/-/blob/master/services/service-catalog.yml), which is the machine-readable source of truth used to route alerts and error budgets. The Global Search Engineering Manager is the DRI for both services the team owns, and delegates day-to-day operational work to the team.

| System | Service catalog entry | DRI | SRE guide | Alerts |
| --- | --- | --- | --- | --- |
| Elasticsearch (Advanced Search) | `search`, owner `global_search` | Global Search Engineering Manager | [runbooks.gitlab.com/search](https://runbooks.gitlab.com/search/), [runbooks.gitlab.com/elastic](https://runbooks.gitlab.com/elastic/) | [`Service::Elasticsearch`](https://alerts.gitlab.net/#/alerts?filter=%7Btype%3D%22search%22%2C%20tier%3D%22inf%22%7D) |
| GitLab Zoekt (Exact Code Search) | `zoekt`, owner `global_search` | Global Search Engineering Manager | [runbooks.gitlab.com/zoekt](https://runbooks.gitlab.com/zoekt/) | [`Service::Zoekt`](https://alerts.gitlab.net/#/alerts?filter=%7Btype%3D%22zoekt%22%2C%20tier%3D%22inf%22%7D) |

Alerts for both services page `#g_global_search_alerts`, and weekly error budget reports go to `#g_global_search`. Both channels are configured on the `global_search` team entry in [`services/teams.yml`](https://gitlab.com/gitlab-com/runbooks/-/blob/master/services/teams.yml).

#### Elasticsearch cluster maintenance

The production and staging Advanced Search clusters run on Elastic Cloud. Cluster configuration, index lifecycle management policies, watchers, index and component templates, and API keys are managed as code in the [`elastic-cloud`](https://gitlab.com/gitlab-com/gl-infra/observability/elastic-cloud) repository and applied by Atlantis on merge to `main`. Do not make these changes through the Kibana UI — they are reverted by the next Terraform apply.

The [Elastic runbook](https://runbooks.gitlab.com/elastic/) carries the operational procedures, including the version upgrade checklist, cluster health verification, disk space saturation handling, and disaster recovery for lost Advanced Search updates.

#### Active Context and semantic code search

The **ActiveContext** abstraction layer and the vector stores behind semantic code search are owned by the [Semantic Code Search team in AI Core Infra](/handbook/engineering/ai/ai-core-infra/semantic-code-search/), not by Global Search. Its operational documentation lives in the [Active Context runbook](https://runbooks.gitlab.com/ai-active-context/), which covers the embeddings pipeline, vector store management, and codebase indexing. Global Search remains the owner of the Elasticsearch cluster that ActiveContext may use as a backing store, so incidents can require both teams.

### Advanced Search as an Enabling Framework

Beyond powering GitLab's global search functionality, Advanced Search serves as a critical framework that enables other teams across GitLab to overcome the inherent limitations of PostgreSQL for complex search and analytics use cases. Teams leverage Advanced Search infrastructure to:

- **Scale beyond PostgreSQL constraints**: Handle large-scale text search, aggregations, and analytics that would be prohibitively expensive or slow in PostgreSQL
- **Enable sophisticated filtering**: Support complex multi-field queries, faceted search, and advanced filtering capabilities
- **Power analytics and insights**: Generate aggregations, statistics, and insights from large datasets without impacting primary database performance
- **Support AI and ML workflows**: Provide vector similarity search, embeddings storage, and retrieval capabilities essential for AI features

This framework approach allows feature teams to focus on their domain expertise while leveraging battle-tested, scalable search infrastructure maintained by the Global Search team.

### A note on basic search

Basic search utilizes Postgres for text searching and Gitaly for code searching. Both functionalities are significantly limited compared to with Advanced search.

## Current state of Advanced Search scopes

There are many data types and search scopes already available via the Advanced Search interfaces. Below is a table that outlines the various available data types and the status of various functional elements, such as permissions, cross-group searching, and embeddings.

| Data type / scope | Privacy / Permissions | Cross-namespace / cross-group searching | Keyword search | Similarity search & Embeddings | Metadata filtering |
|-------------------|-----------------------|-----------------------------------------|----------------|--------------------------------|--------------------|
| **Code** | Yes | Yes | Yes | In progress | Group, Project, Include/exclude archived, include/exclude forks, Language, Filename, Path, Extension |
| **Issues** | Yes | Yes | Yes | Yes | Group, Project, Status, Confidentiality, Labels, Include/exclude archived |
| **Merge requests** | Yes | Yes | Yes | No | Group, Project, Status, Include/exclude archived |
| **Epics** | Yes | Yes | Yes | No | Group, Project |
| **Comments** | Yes | Yes | Yes | No | Group, Project, Include/exclude archived |
| **Users** | Yes | Yes | Yes | No | Group, Project |
| **Commits** | Yes | Yes | Yes | No | Include/exclude archived |
| **Milestones** | Yes | Yes | Yes | No | Group, Project, Include/exclude archived |
| **Project** | Yes | Yes | Yes | No | Group |
| **Wiki** | Yes | Yes | Yes | No | Group, Project |

## Meetings

Whenever possible, we prefer to communicate asynchronously using issues, merge requests, and Slack. However, face-to-face meetings are useful for establishing a personal connection and addressing items that would be more efficiently discussed synchronously, such as blockers.

- The Global Search Group meets weekly on Tuesdays at 14:00 UTC.
- The Global Search Group also has an Open Discussion Hour on Thursdays at 12:30 UTC

## Work

We follow the general workflow and principles defined in [Product Development Flow](/handbook/product-development/how-we-work/product-development-flow/) and [Engineering Workflow](/handbook/engineering/workflow/). To bring an issue to our attention, please create an issue in the relevant project. Add the `~"group::global search"` label and any other suitable labels. If it is an urgent issue, please reach out to the Product Manager or Engineering Manager listed in the [Stable Counterparts](/handbook/engineering/ai/search/#stable-counterparts) section above.

Below are a few guidelines the team follows in the day-to-day work.

- We use asynchronous communication with each other and with other GitLab teams via GitLab, Slack, Google Docs, etc.
- We have weekly team meetings, 1-on-1 meetings, and virtual happy hours via Zoom to discuss various topics and create team bonding.
- We encourage all backend engineers in our team to have their changes reviewed by someone else in our group. It's great for knowledge sharing.
- We organize our tasks under Epics and Issues. The Product Manager and Engineering Manager go through the backlog at the planning phase of each release and put issues into the next one or two milestones. The issues on the [milestone board](https://gitlab.com/groups/gitlab-org/-/boards/1339901?label_name[]=group%3A%3Aglobal%20search) are sorted based on priority. The higher priority issues are placed on the top.
- We apply the Deliverable label to the issues that we intend to close in a milestone before the milestone starts. Issues added during a milestone should not have the Deliverable label applied. We review these issues in the middle of the milestone, usually the first week of each month. We will remove the Deliverable label from the issues that are not likely to make it into the release.
- We apply the Stretch label to the issues that we intend to start during a milestone but are not committing to closing.
- We work with the UX team for features that need their design input by labeling the issues with a UX workflow label and adding the corresponding UX team counterpart as the assignee. We use `workflow::problem validation` and `workflow::solution` validation for user research and `workflow::design` for UI design and prototyping. Once the design is finished, `workflow::ready for development` label will be added as an indicator that development can start. For minor UX/UI changes, we contact our UX counterpart or the Product Design Manager to request a review for fast iterations.
- We work with the [Developer Experience](/handbook/engineering/infrastructure-platforms/developer-experience/) team for issues that require input from a testing perspective by creating an [RFH](/handbook/engineering/infrastructure-platforms/developer-experience/#request-for-help-process).
- We work with the Technical Writing team for issues that need documentation change by labeling the issues with <code>documentation</code> and adding our counterpart in the Technical Writing team as assignee. Our technical writer helps us update the corresponding document. The documentation change normally happens together with the code change.
- We work with our stable counterpart in the Security team for issues that need input from a security perspective. We suggest using team planning issues, for example, [this one](https://gitlab.com/gitlab-org/search-team/team-tasks/-/issues/17), for communication.
- We work with the Support Engineering team by collaborating on issues directly. We invite our counterpart in the Support Engineering team to our team meeting every month to have direct communication.
- When team members are ready for their next tasks, they will pick an issue from the milestone board and become the issue owner by assigning the issue to themselves. Team members should prioritize issues with the Deliverable label. The issue owner will be responsible for finding the solution to the issue. They can propose a solution by opening a Merge Request. They can also break down the issue into smaller sub-issues if it makes sense to take an iterative approach.
- Before going out of office for an extended time, assign items still in review to the Engineering Manager. The Engineering Manager can reassign as needed.
- Whenever a team member reviews an author's work that is out of office for an extended time, they are welcome to complete the changes requested if they deem themselves comfortable with the remainder of the work.
- We review and prioritize bugs every week. It is common for bugs to represent the problem without identifying the impact. Because the Product Management and QA share the responsibility of assessing every bug for priority, severity, and details. Severity uses an approximation of the Risk Matrix to identify potential risk and frequency. Priority is based on total impact over time. Occasionally, something of a lower priority/ severity will be added to a milestone when it relates to work currently scheduled.
    1. Review all new bugs for content, priority, severity, and milestones
    1. Review any bugs missing priority or severity
    1. Prioritize bugs for the current milestone. 10% of scheduled work should be focused on bugs
    1. Schedule bugs for future milestones based on capacity, severity, priority, and relationship to any scheduled work

### Breaking changes process

Before a major milestone starts, we prepare an epic with all the breaking change issues linked. As usual, we work to get approvals but keep the MR in draft to prevent it from merging before the major milestone. If an MR is independent, we can have the `master` as a target branch. If not, we can have a sequence of MRs with target branches set to each other. As soon as the first one merges, the next will automatically target `master`.

Every MR that was created before the breaking change milestone should have this or a similar warning in the description: `:warning: This MR must be kept as a draft and cannot be merged until **DATE** :warning:`

### Bugfix backport process

We review the bugfix merge requests every week. To facilitate this process, we have created scoped labels: `backport::required`, `backport::skip`, and `backport::complete`.

- The `backport::skip` label will be added to merge requests if no backport is needed.
- The `backport::required` label will be added to the merge requests that need to be backported to a previous release in the initial review. The DRI will follow the [patch release process](/handbook/engineering/releases/patch-releases#patch-release-overview) to backport the fix to a previous release. Once the backport is done, the `backport::complete` label will be added to indicate the whole process is complete.

### Advanced Global Search Rollout on GitLab.com

The team has been actively working on enabling Elasticsearch powered Advanced Search on GitLab.com. [Based on our analysis](https://gitlab.com/groups/gitlab-org/-/epics/1736), we set our first target to roll this feature out for all the paid groups on GitLab.com. You can find more details about the timeline and progress in the links below.

- [Plan of Advanced. Search Rollout on GitLab.com](https://gitlab.com/groups/gitlab-com/-/epics/649)
- [Steps and Enhancements of Advanced Search Rollout on GitLab.com](/handbook/engineering/ai/search/es-rollout-timeline/)

### Severity Labels for Search Issues (`~advanced search`, `~global search`)

| Type of Operation | `~severity::1` - Blocker | `~severity::2` - Critical | `~severity::3` - Major  | `~severity::4` - Low |
| ------------------|--------------------------|---------------------------|-------------------------|----------------------|
| Recall Record, Global | Above 10 seconds to timing out | Between 7 and 10 seconds | Between 4 and 7 seconds | Between 2 and 4 seconds |
| Time until inserted record is recallable | Above 15 minutes | Between 15 and 10 minutes | Between 10 and 5 minutes | Between 3 and 5 minutes|

The two types of operations we detail severity metrics for above are:

- Recall Record, Global: This is the time it takes to recall a record using a globally scoped search of GitLab.com. Records could be entities such as projects, users, groups, etc.
- Time until inserted record is recallable: This is the elapsed time between adding a new record and having that new record be recallable via a search. This process depends on many underlying technologies such as the [Go indexer](https://gitlab.com/gitlab-org/gitlab-elasticsearch-indexer), [Sidekiq queues](https://docs.gitlab.com/ee/development/advanced_search.html#how-does-it-work), and the Elasticsearch database.

### Weighting for Search Issues

We use the Fibonacci rating system to assign weights to Search issues. Below are a few guidelines when setting issue weight:

- Issues that include `~backend` and `~frontend` work should have the weights added for a total weight representative of the work effort.
- Spike issues are assigned a weight to help timebox the effort.
- Bugs will not be given a weight.
- Any issue weighted over 5 should be broken down into smaller iterative steps if the issue does not contain `~backend` and `~frontend` work.

| Weight | Description |
|--------|--------|
| 0      | No effort or trivial effort (example: Documentation typo or Feature Flag Rollout) |
| 1      | Low effort (No Database migrations or Advanced Search migrations) |
| 2      | Low-Medium effort |
| 3      | Medium effort |
| 5      | High effort |

### MR reviews

We have the following guidelines for doing reviews on Global Search Team MRs:

- The MR author is responsible for deciding if the initial or maintainer reviews should be done by a Global Search Team member and can indicate that in a comment or by assigning the reviewers.
- Draft status indicates that the MR is not ready to be merged, but the author could decide to assign a reviewer while in draft mode. Unless a review is urgent, the author should wait for the pipeline to pass before assigning a reviewer.
- We use [Conventional Comments](https://conventionalcomments.org/) to communicate effectively in review comments.
- The merge request author resolves only the threads they feel they have fully addressed and all discussions have been closed, anything else is resolved by the reviewer. When a merge request has many threads, it is helpful for the reviewer to go back to open threads to pick up where the previous discussions were left off.

#### Reviewer and maintainer types

Beyond the usual backend and frontend maintainer roles, the team owns two shared components with their own maintainer groups. Both are enforced through [`.gitlab/CODEOWNERS`](https://gitlab.com/gitlab-org/gitlab/-/blob/master/.gitlab/CODEOWNERS) in `gitlab-org/gitlab`, so an MR touching the paths below requires approval from that group whoever the author is.

| Maintainer group | CODEOWNERS section | Covers |
| --- | --- | --- |
| [`@gitlab-org/search-team/maintainers/advanced-framework`](https://gitlab.com/groups/gitlab-org/search-team/maintainers/advanced-framework) | `[Advanced Search Framework]` (required) and `[Advanced Search Framework - Entity Implementations]` (optional) | Core framework abstractions under `ee/lib/search/elastic/` and `ee/lib/elastic/`, the bulk indexer, client, query builder and DSL, Elastic concerns, services and workers, plus `doc/development/advanced_search.md`. New entity implementations — query builders, types, references, record preloading — fall into the optional section. |
| [`@gitlab-org/search-team/maintainers/advanced-migrations`](https://gitlab.com/groups/gitlab-org/search-team/maintainers/advanced-migrations) | `[Advanced Search Migration]` (required for `ee/elastic/migrate/` and `ee/elastic/docs/`, optional for the specs) | Advanced search migrations. These are required rather than optional because an incorrect migration affects availability, in the same way a database migration does. |

The distinction between the required and optional CODEOWNERS sections matters: a change to a core framework abstraction blocks on a framework maintainer, while a new entity implementation only requests one. See the [advanced search migration review guidelines](https://docs.gitlab.com/development/search/advanced_search_migration_review/) before reviewing in the migrations group.

### Automation

The team relies on several automations. Each one's process is documented in the repository it runs from; the links below are the entry points, not a duplicate of the process.

#### Marking advanced search migrations obsolete

Migrations older than one milestone before the last required stop are marked obsolete automatically. Two [GitLab Housekeeper](https://gitlab.com/gitlab-org/gitlab/-/blob/master/gems/gitlab-housekeeper/README.md) keeps do the work, both living in `gitlab-org/gitlab`:

1. [`Keeps::MarkOldAdvancedSearchMigrationsAsObsolete`](https://gitlab.com/gitlab-org/gitlab/-/blob/master/keeps/mark_old_advanced_search_migrations_as_obsolete.rb) — prepends `Search::Elastic::MigrationObsolete`, swaps the spec for the deprecated-migration shared example, updates the dictionary file, and assigns a Global Search backend engineer.
2. [`Keeps::DeleteObsoleteAdvancedSearchMigrations`](https://gitlab.com/gitlab-org/gitlab/-/blob/master/keeps/delete_obsolete_advanced_search_migrations.rb) — deletes all but the most recent obsolete migration.

**Where the pipeline lives:** the marking keep runs monthly from the [`engineering-productivity/team` scheduled pipelines](https://gitlab.com/gitlab-org/quality/engineering-productivity/team/-/pipeline_schedules), in the `automatic-mark-search-migrations-obsolete` job defined in that project's [`.gitlab-ci.yml`](https://gitlab.com/gitlab-org/quality/engineering-productivity/team/-/blob/main/.gitlab-ci.yml). The schedule sets `AUTO_MARK_OBSOLETE_SEARCH_MIGRATIONS`, which is what gates the job and its failure alert to `#g_global_search_alerts`. The removal keep is run manually.

The MR assignee still has manual steps to complete — checking `marked_obsolete_by_url`, clearing `.rubocop_todo/` references, removing `migration_has_finished?` backwards-compatibility branches, and backing up deleted migrations to the [migration graveyard](https://gitlab.com/gitlab-org/search-team/migration-graveyard). These are listed in the [advanced search migration style guide](https://docs.gitlab.com/development/search/advanced_search_migration_styleguide/#cleaning-up-advanced-search-migrations).

#### Indexer releases

Both indexers release themselves weekly from a scheduled pipeline and document the process in-repo:

1. **Elasticsearch indexer**: [`doc/process.md`](https://gitlab.com/gitlab-org/gitlab-elasticsearch-indexer/-/blob/main/doc/process.md) in `gitlab-org/gitlab-elasticsearch-indexer`. A weekly schedule with `SCHEDULE_TYPE=weekly_release` runs `release_create_mr`, which uses `git-cliff` to decide whether conventional commits warrant a bump, opens the release MR, and tags on merge. `renovate-gitlab-bot` then opens the MR bumping `GITLAB_ELASTICSEARCH_INDEXER_VERSION` in `gitlab-org/gitlab`. That doc also lists the current maintainers and the trainee maintainer process.
2. **Zoekt indexer**: [`DEPLOYMENT_PROCESS.md`](https://gitlab.com/gitlab-org/gitlab-zoekt-indexer/-/blob/main/DEPLOYMENT_PROCESS.md) in `gitlab-org/gitlab-zoekt-indexer`, covering both the indexer and the Zoekt webserver. Tagging is automated the same way (`release_create_mr` on a weekly schedule), but propagating a release is a manual chain across the CI image, CNG, the [`gitlab-zoekt` chart](https://gitlab.com/gitlab-org/cloud-native/charts/gitlab-zoekt) and the main GitLab chart. Follow the steps in that file rather than reproducing them here.

### Oncall escalation coverage

As the Global Search Team requires special domain knowledge, such as
Elasticsearch, we borrow team members with this domain knowledge from other
groups to cover the on-call escalation when we are understaffing, especially
during the holiday seasons. In general, we will follow
the [Tier 2 On-Call Program](/handbook/engineering/infrastructure-platforms/incident-management/on-call/tier-2/)
for escalations requiring domain expertise. The Elasticsearch domain experts,
identified by domain_expertise on their profile, may be contacted when SRE and
Tier 2 on-call engineers cannot resolve the production incidents. We don't
expect the domain experts to work outside their normal working hours. In case of
emergency, we will follow the rules and best practices outlined in
our [Incident Management](/handbook/engineering/infrastructure-platforms/incident-management/)
handbook. To assist team members in catching up on the latest development status
and resolving potential incidents, we have created
a [Global Search Incident Management document](https://gitlab.com/gitlab-org/search-team/training-materials/-/tree/main/2021-12-14-production-incident-management)
as a reference.

#### Onboard domain experts from other groups to cover production incident escalation

When onboarding domain experts from other groups to help cover production incident escalation, we may consider the following actions:

- Suggest the team member add `elasticsearch` as their `domain_expertise` in their team member profile
- Add the team member to the Slack group global-search-team which can be used by SREs and other on-call engineers to contact in case of emergency
- Create the access request for the team member to grant them access permissions to Elasticsearch cluster
- Schedule [walk-through sessions](https://youtu.be/dK-G-pLVRfE) with the team member to go over the latest architecture and development status

#### Offboard domain experts from production incident escalation coverage

- Remove the team member from the Slack group global-search-team
- Revoke the team member's access permission of Elasticsearch cluster

### Common Links

- [Global Search Team Milestone Board](https://gitlab.com/groups/gitlab-org/-/boards/1339901?label_name[]=group%3A%3Aglobal%20search)
- [Global Search Team Workflow Board](https://gitlab.com/groups/gitlab-org/-/boards/4440461?not[label_name][]=UX%20Paper%20Cuts&label_name[]=group%3A%3Aglobal%20search&milestone_title=Started)
- [Global Search Team Epics](https://gitlab.com/groups/gitlab-org/-/epics?scope=all&utf8=%E2%9C%93&state=opened&label_name[]=group%3A%3Aglobal%20search)
- Global Search team slack channel (internal) [#g_global_search](https://gitlab.slack.com/app_redirect?channel=g_global_search)
- [Global Search Roadmap](https://gitlab.com/groups/gitlab-org/-/roadmap?state=all&sort=start_date_asc&layout=MONTHS&timeframe_range_type=CURRENT_YEAR&label_name%5B%5D=group%3A%3Aglobal+search&label_name%5B%5D=Roadmap&progress=COUNT&show_progress=true&show_milestones=false&milestones_type=ALL)
- [Bug Review Board](https://gitlab.com/groups/gitlab-org/-/boards/2118530?label_name[]=type::bug&label_name[]=group%3A%3Aglobal%20search)

### JTBD

We utilize the [Jobs to be Done](/handbook/product/ux/jobs-to-be-done/) (JTBD) framework to better understand our customers' and users' needs. You can view the current list of our JTBD [here](/handbook/engineering/ai/search/jtbd/#jobs-to-be-done).

### Performance Testing

We are exploring [Rally](https://esrally.readthedocs.io/en/stable/) for performance testing the Elasticsearch cluster. Workload data is determined using Kibana and stored in a [Google Sheet](https://docs.google.com/spreadsheets/d/1K_MteuTEX0spu0jOiRt9BqDLZXywUhQ9NUw7PbU8odw/edit?usp=sharing) (internal)

## Resources

### Documentations

#### Search and Advanced Search

- [GitLab Elasticsearch Integration](https://docs.gitlab.com/ee/integration/advanced_search/elasticsearch.html)
- [GitLab Advanced Search Development Guidelines](https://docs.gitlab.com/ee/development/advanced_search.html)
- [GDK Elasticsearch Setup Instructions](https://gitlab.com/gitlab-org/gitlab-development-kit/-/blob/main/doc/howto/elasticsearch.md)

#### AI Context Infrastructure

- [Zoekt Design Document](/handbook/engineering/architecture/design-documents/code_search_with_zoekt/) - Comprehensive architecture and implementation details
- [GDK Zoekt Setup Instructions](https://gitlab.com/gitlab-org/gitlab-development-kit/-/blob/main/doc/howto/zoekt.md)
- [Semantic Code Search](/handbook/engineering/ai/ai-core-infra/semantic-code-search/) - AI Core Infra team page covering the ActiveContext framework and RAG for code

### Blog Posts

- [Lessons from our journey to enable global code search with Elasticsearch on GitLab.com](https://about.gitlab.com/blog/2019/03/20/enabling-global-search-elasticsearch-gitlab-com/)
- [Update: The challenge of enabling Elasticsearch on GitLab.com](https://about.gitlab.com/blog/2019/07/16/elasticsearch-update/)
- [Update: Elasticsearch lessons learnt for Advanced Global Search 2020-04-28](https://about.gitlab.com/blog/2020/04/28/elasticsearch-update/)
- [How the Search Team at GitLab Implemented a Risk Map to Direct Automated Testing Efforts](https://about.gitlab.com/blog/2020/09/03/risk-mapping/)
- [GitLab's data migration process for Advanced Search](https://about.gitlab.com/blog/2021/06/01/advanced-search-data-migrations/)

### Product Demos

- [GitLab search with Custom Search Engines](https://www.youtube.com/watch?v=YESlLDxHH4o)
- [Use the GitLab search bar to navigate](https://www.youtube.com/watch?v=OE9b0Qc6KaI)
- [Search suggestions for recently viewed issues and merge requests](https://www.youtube.com/watch?v=_5s4ZjnDZPo)
- [How to search for epics in GitLab](https://www.youtube.com/watch?v=bu6kaBqcYFc)
- [Elasticsearch Migrating Issues To Separate Index Technical Overview](https://youtu.be/1znFvPH_wjU)
