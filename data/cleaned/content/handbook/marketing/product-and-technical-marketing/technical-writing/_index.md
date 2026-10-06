---
title: "Technical Writing"
description: "The GitLab Technical Writing team collaborates with developers, product managers, and the community to develop product documentation."
---


Good documentation meets the evolving needs of GitLab customers, users, and administrators. It educates readers about features and best practices. It enables people to efficiently configure, use, and troubleshoot GitLab. The Technical Writing team manages the [docs.gitlab.com](https://docs.gitlab.com) site and its content, processes, and tooling.

The [documentation roadmap](https://gitlab.com/groups/gitlab-org/-/epics/17363) drives our efforts to improve both the content and [documentation website](https://docs.gitlab.com/). For example, we know that people have trouble finding information on docs.gitlab.com. We have roadmap items and OKRs to replatform the docs site, provide better task-based information, and make content easier to find. These larger projects, completed in addition to feature documentation, provide continual, iterative improvement to the user experience of our documentation.

Anyone can contribute to the documentation. Follow our [GitLab documentation guidelines](https://docs.gitlab.com/development/documentation/).

## About Us

For more information about the team size and team members, see [Meet Our Team](/handbook/company/team/?departmentOrDivision=Technical+Writing), filtered by Technical Writing. The roles in our team include:

- [Technical Writers](/job-description-library/product/technical-writer/) at Intermediate, Senior, and Staff levels.
- [Technical Writing Managers](/job-description-library/product/technical-writing-manager/).
- [Fullstack Engineers, Technical Writing](/job-description-library/product/ux-fullstack-engineer/).
- A [Technical Writing Director](/job-description-library/product/technical-writing-manager/#director-technical-writing).

## Contact Us

You can contact us through the various Slack channels or the dedicated GitLab
group aliases. `@gl-docsteam` is a large group. For MR reviews, check the docs page metadata
and assign or at mention the [designated Technical Writer](#assignments-to-devops-stages-and-groups) directly.

### Slack channels

The team manages general documentation-related and team-specific Slack channels:

- `#docs`: Questions and general discussion about GitLab documentation, and requests by GitLab team members for doc and UI text reviews.
- `#docs-engineering`: Discussion about the Docs website and other engineering projects.
- `#docs-processes`: Discussion about documentation processes.
- `#docs-tooling`: Discussion about documentation tooling.
- `#docs-site-changes-hugo`: Automated messages from the [`docs-gitlab-com`](https://gitlab.com/gitlab-org/technical-writing/docs-gitlab-com) project.
- `#tw-team`: Technical Writing team chat.
- `#tw-social`: Technical Writing team social chat.

### GitLab group aliases

Some team members are part of specific groups. To contact all the members of
those groups in a GitLab issue or MR, use the following aliases:

| Alias                                                          | GitLab group                                                                                                                                                                                            | Description |
|:---------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------|
| `@gl-docsteam`                                                 | [gl-docsteam](https://gitlab.com/groups/gl-docsteam/-/group_members)                                                                                                                                    | Entire Technical Writing team (leadership, writers, engineers) |
| `@gitlab-org/tw-leadership`                                    | [gitlab-org/tw-leadership](https://gitlab.com/groups/gitlab-org/tw-leadership/-/group_members?with_inherited_permissions=exclude)                                                                       | Leadership (Managers, Staff Technical Writers, Staff Engineers) |
| `@gitlab-org/technical-writing/tw-docops`                      | [gitlab-org/technical-writing/tw-docops](https://gitlab.com/groups/gitlab-org/technical-writing/tw-docops/-/group_members?with_inherited_permissions=exclude)                                           | [DocOps](#docops-group) |
| `@gitlab-org/technical-writing/tw-eng`                      | [gitlab-org/technical-writing/tw-eng](https://gitlab.com/groups/gitlab-org/technical-writing/tw-eng/-/group_members?with_inherited_permissions=exclude)                                           | Engineers |
| `@gitlab-org/maintainers/gitlab-development-kit/documentation` | [gitlab-org/maintainers/gitlab-development-kit/documentation](https://gitlab.com/groups/gitlab-org/maintainers/gitlab-development-kit/documentation/-/group_members?with_inherited_permissions=exclude) | Technical Writers who review [GDK](https://gitlab.com/gitlab-org/gitlab-development-kit) documentation |

## Learn GitLab tech writing fundamentals

If you're interested in updating or creating GitLab documentation,
see [GitLab Technical Writing Fundamentals](https://university.gitlab.com/courses/gitlab-technical-writing-fundamentals).
This course is aimed at both GitLab team members and community contributors and includes:

- Guidelines for technical writing
- GitLab style conventions
- Information about internal testing
- Instructions for content types

This course is **not required** to contribute to docs.gitlab.com. Everybody can contribute!

For suggestions and feedback, see the [feedback issue](https://gitlab.com/gitlab-org/technical-writing/team-tasks/-/issues/445).

## Documentation

GitLab documentation is crafted to help users, administrators, and decision-makers
learn about GitLab features and to optimally implement and use GitLab to meet
their [DevOps needs](https://about.gitlab.com/stages-devops-lifecycle/).

The documentation is an essential part of the product. Its source is developed
and stored with the product in its respective paths in the
[GitLab repositories](https://docs.gitlab.com/development/documentation/site_architecture/#architecture).
It's published at [docs.gitlab.com](https://docs.gitlab.com) (offering multiple
versions of all product documentation) and at the `/help/` path on each GitLab
instance's domain, with content for that instance's version.

The documentation is the [single source of truth](https://docs.gitlab.com/development/documentation/styleguide/#documentation-is-the-single-source-of-truth-ssot)
for all product information.
We follow a [docs-first methodology](https://docs.gitlab.com/development/documentation/styleguide/#docs-first-methodology)
with the goal of creating documentation that is complete, accurate, and easy to use.
The documentation should be easy to browse or search for the information you need, and
it should be easy to contribute to the documentation itself.

To get started contributing to the documentation, see
[Contribute to the GitLab documentation](https://docs.gitlab.com/development/documentation/).
For standards and guidelines, see [the style guide](https://docs.gitlab.com/development/documentation/styleguide/)
and [word list](https://docs.gitlab.com/development/documentation/styleguide/word_list/).

## Responsibilities

Team members are [assigned](#assignments) to specific DevOps stage groups. The Technical Writing team is broadly responsible for both developing documentation content and UI text, and helping others while they develop content:

- Maintaining documentation for many engineering projects.
- Occasionally developing new content to meet the needs of the community.
- Reviewing and collaborating on documentation plans, reviewing doc merge requests or recently merged docs, and ensuring that content meets style and language standards.
- Reorganizing, revamping, and authoring improved documentation to ensure completeness and a smooth user experience.
- Collaborating with Product Designers on UI text, such as microcopy, links from the UI to documentation, error messages, and UI element labels.
- Acting as Technical Writing Lead for the monthly [release notes](https://docs.gitlab.com/development/documentation/release_notes/).

### Prioritization

When evaluating work to meet our stakeholders' needs, we prioritize in the following order:

1. Feature work (including documenting new features, and providing guidance on UI text)
1. OKR-related work
1. Docs improvements and backlog issues (including stage lead work, docs technical debt, and topic type implementation)
1. All other tasks (including DocOps tasks)

### Processes

The team is responsible for developing and maintaining efficient processes, including:

- Ensuring that processes are in place and being followed to keep the GitLab docs up to date.
- Following and optimizing documentation workflows with Product and Engineering and Technical Writing team workflows.
- Triaging doc-related issues.
- Refining the [Documentation Style Guide](https://docs.gitlab.com/development/documentation/styleguide/) and continuously improving content about GitLab documentation and its contribution process.
- Making it easier for anyone to contribute to the documentation while efficiently handling community contributions to docs.

#### Style Guide

The [Documentation Style Guide](https://docs.gitlab.com/development/documentation/styleguide/)
provides language and style guidance for the product documentation and release notes.

Any Technical Writer (or other contributor) can make suggestions for
documentation style updates or additions by creating an issue or merge request with the
`~tw-style` label, and then assigning the issue or MR to the Style Guide DRI. GitLab team members can also use the `#docs` Slack channel.

Use the following searches to track completed style-related issues:

- [GitLab project style issues](https://gitlab.com/gitlab-org/gitlab/-/issues?scope=all&utf8=%E2%9C%93&state=opened&label_name[]=tw-style)
- [GitLab project style MRs](https://gitlab.com/gitlab-org/gitlab/-/merge_requests?scope=all&utf8=%E2%9C%93&state=opened&label_name[]=tw-style)
- [Technical Writing project style issues](https://gitlab.com/gitlab-org/technical-writing/team-tasks/-/issues?scope=all&utf8=%E2%9C%93&state=opened&label_name[]=tw-style)

#### Translation and internationalization

Everyone can contribute to the translation of GitLab from English into other languages.
To learn more about translation and internationalization at GitLab, see
[internationalization](/handbook/marketing/product-and-technical-marketing/globalization/category-internationalization/).
For a step-by-step guide to translation contributions, see [translating GitLab](https://docs.gitlab.com/development/i18n/translation/).

The [docs.gitlab.com](https://docs.gitlab.com/) site is available in English and Japanese.
To learn more about the localization process, see
[product documentation localization](/handbook/marketing/product-and-technical-marketing/globalization/tech-docs-localization/).

## Assignments

Technical Writers (TWs) collaborate with [their assigned groups](#assignments-to-devops-stages-and-groups). TWs can also be assigned [other work](#assignments-to-other-projects-and-subjects).

Some content on docs.gitlab.com is [not reviewed by TWs](#content-not-reviewed-by-tws).

<a id="designated-technical-writers"></a>

### Assignments to DevOps Stages and Groups

The designated Technical Writer is the go-to person for their assigned
[groups](/handbook/product/categories/). They collaborate with
other team members to plan new documentation, edit existing documentation,
review any proposed changes to documentation, suggest changes to UI microcopy,
and generally partner with subject matter experts (SMEs) in
all situations where documentation is required.

{{% product/tech-writing %}}

<!--
  To update the table above:

  - For tech writer's name per stage, change https://gitlab.com/gitlab-com/www-gitlab-com/-/blob/master/data/stages.yml and https://gitlab.com/gitlab-com/content-sites/handbook/-/blob/main/layouts/_shortcodes/product/tech-writing.html
  - To turn off a stage, set tw: false in https://gitlab.com/gitlab-com/www-gitlab-com/-/blob/master/data/stages.yml

Reference: https://gitlab.com/gitlab-com/www-gitlab-com/merge_requests/24952
-->

{{% alert title="Note" color="primary" %}}
**If you were directed here from a documentation page's metadata:**

- The metadata doesn't indicate developer ownership, but is meant to direct you to an appropriate Technical Writer.
- If you are part of a development group and would like to add metadata to documentation pages, create an issue in [the TW team tasks project](https://gitlab.com/gitlab-org/technical-writing/team-tasks/) for discussion. Additional discussion is in [issue 547](https://gitlab.com/gitlab-org/technical-writing/team-tasks/-/issues/547).
- If the stage is listed as `none`, see if [there is a DRI](#assignments-to-other-projects-and-subjects) or use [roulette](https://gitlab-org.gitlab.io/gitlab-roulette/?sortKey=stats.avg30&order=-1&hourFormat24=true&visible=maintainer%7Cdocs).
{{% /alert %}}

Technical Writers are encouraged to review and improve documentation of other
stages but they aren't required to. When contributing to docs they don't own,
they must respect the assigned TW's ownership and request their review
and approval when adding significant changes to their docs.

When a Technical Writer [is on PTO](#technical-writer-pto), the whole team acts as their backup.

<!-- vale handbook.Spelling = NO -->

### Section leads

Technical Writing Managers are assigned to key [sections](/handbook/product/categories/).
The designated Manager is the go-to person for their assigned sections. They represent technical
writing in the leadership group, and act as the point of contact for the team.

{{% product/tech-writing-sections %}}

These sections represent:

| Area                                             | Assigned Manager |
|:-------------------------------------------------|:--------------------|
| AI, Core DevOps  | {{< member-by-name "Sarah Watt" >}} |
| Analytics & Monetization, Platforms, Security | {{< member-by-name "Robert Landry" >}} |

### Stage leads

Some Technical Writers are assigned as **stage leads** for a given [DevOps stage](/handbook/product/categories/#devops-stages).

| Stage            | Assigned stage lead |
|:-----------------|:--------------------|
| Verify           | {{< member-by-name "Lysanne Pinto" >}} |
| Create           | {{< member-by-name "Brendan Lynch" >}} |
| Plan             | TBD (on hold) |
| Application Security Testing | TBD (on hold) |

Stage leads might work across an entire stage, or a subset of groups in the stage.
They support other Technical Writers assigned to groups in the stage.

Stage leads:

- Assume the same [responsibilities](#responsibilities) as Technical Writers, but with a more targeted focus on proactively creating and improving documentation for their assigned stage.
- Spend approximately 70% of their time on issues and merge request reviews authored by developers for [new features and enhancements](https://docs.gitlab.com/development/documentation/workflow/#documentation-for-a-product-change) for their assigned groups.
- Spend the remainder of their time:
  - Creating and refining content to address documentation needs and gaps for their assigned **stage**
    (for example, writing tutorials and use case-based content, restructuring existing content, and working on the information architecture).
  - Supporting other writers in the stage to contribute to documentation improvements.
- Complete a quarterly planning issue to outline the content gaps and improvements that they aim to address over three milestones
  (for example, [FY25Q3 Stage lead planning issue: Secure](https://gitlab.com/gitlab-org/technical-writing/team-tasks/-/issues/1067)). The [planning issue](https://gitlab.com/gitlab-org/technical-writing/team-tasks/-/blob/main/.gitlab/issue_templates/tw_stage_lead.md) is automatically created and assigned to all Technical Writers in the stage on the 20th of the last month before the start of the quarter.
- Apply the relevant `tw-lead` [label](https://gitlab.com/groups/gitlab-org/-/labels?utf8=%E2%9C%93&subscribed=&search=tw-lead) to documentation improvement MRs that they drive or provide input on. This label allows us to track the improvements that come out of the stage lead process as one of our performance indicators (PIs). [Tableau chart](https://10az.online.tableau.com/#/site/gitlab/views/DRAFT-UXKPIs/TechnicalWritingMRsbyTWLeadStage?:iid=1) accessible to GitLab team members only.
- Collaborate with other stage leads on documentation improvements.

Over time, and with fewer groups assigned per stage lead, an aspirational goal is for stage leads to spend 70% of their time on proactive work rather than 30%.

For [documentation improvements](https://docs.gitlab.com/development/documentation/workflow/#documentation-feedback-and-improvements), stage leads are responsible for creating an
issue board to track ongoing and planned documentation enhancements and additions.

### DocOps group

[DocOps](https://www.writethedocs.org/guide/doc-ops/) is like DevOps, but for documentation. It's an
approach to help streamline the creation, management, and deployment of documentation.

Some Technical Writers are members of the [DocOps group](https://gitlab.com/gitlab-org/technical-writing/tw-docops),
which is responsible for:

- Maintaining content quality through testing and linting in CI/CD pipelines and locally.
- Assisting [Docs Engineers](/job-description-library/product/ux-fullstack-engineer/) with operations tasks when asked, or when
  those engineers are not online. For example, helping with Pages configuration, deployments, scheduled pipelines, and
  review apps.
- Updating dependencies for linting tools, and rolling those updates out in upstream documentation projects.
- Monitoring the [TW: DocOps issue board](https://gitlab.com/groups/gitlab-org/-/boards/9427118?label_name%5B%5D=tw-testing).

The DocOps group is not responsible for the documentation website's code, infrastructure, or build scripts.
DocOps tasks are [prioritized](#prioritization) below feature work and OKR-related work.

Participation in the DocOps group is based on team requirements. To express interest in joining, speak to your manager.

#### Documentation testing

The DocOps group develops and maintains toolkits to test GitLab's documentation (and other technical content) for
problems. These toolkits include (but aren't limited to):

- Content and formatting: markdownlint, Vale, yamllint
- Link validity: Lychee
- File permissions and naming: `lint-doc.sh`

To suggest changes to our linting rules or tooling:

1. Create an issue or merge request with the
   [`~tw-testing`](https://gitlab.com/gitlab-org/gitlab/-/issues?label_name[]=tw-testing) label.
1. Mention [@gitlab-org/technical-writing/tw-docops](https://gitlab.com/gitlab-org/technical-writing/tw-docops) on the issue or MR.

The DocOps group balances this work against other [technical writing priorities](#prioritization).

### Assignments to other projects and subjects

For collaboration in other projects and subjects:

| Subject                                                                              | Assigned Technical Writer |
|:--------------------------------------------------------------------------------     |:--------------------------|
| The documentation site                                                               | {{< member-by-name "Sarah Watt" >}}, {{< member-by-name "Robert Landry" >}} |
| The documentation site backend (code, automation)                                    | {{< member-by-name "Hiru Fernando" >}} |
| The documentation's information architecture (content restructuring and major changes to left nav) | {{< member-by-name "Fiona Neill" >}} |
| [GitLab Design System ("Pajamas")](https://design.gitlab.com/) information under [`content`](https://gitlab.com/gitlab-org/gitlab-services/design.gitlab.com/-/tree/main/contents/content) | {{< member-by-name "Fiona Neill" >}} |
| [Style Guide](#style-guide)                                                          | {{< member-by-name "Fiona Neill" >}} |
| [Documentation testing](#documentation-testing) (DocOps/Vale/markdownlint)           | {{< member-by-name "Sarah Watt" >}} |
| [GitLab Development Kit (GDK)](https://gitlab.com/gitlab-org/gitlab-development-kit) | {{< member-by-name "Ashraf Khamis" >}}, {{< member-by-name "Evan Read" >}}, {{< member-by-name "Lorena Ciutacu" >}}, {{< member-by-name "Marcel Amirault" >}} |

### Content not reviewed by TWs

Technical Writers do not review content in:

- The `doc/development` directory. Any Maintainer can merge docs in the `doc/development` directory.
  The only exception is `/doc/development/documentation`, where the writers maintain guidelines.
- The `doc/solutions` directory. This information is created, reviewed, merged, and maintained by Solutions Architects.

### Stable counterparts

The Technical Writing team gets assistance with the `docs-gitlab-com` project from stable counterparts outside the team.

| Subject          | Person |
|:-----------------|:-------|
| Backend reviews  | TBD |
| Frontend reviews | [Paul Gascou-Vaillancourt](https://gitlab.com/pgascouvaillancourt) |
| Support          | [Mike Lockhart](https://gitlab.com/mlockhart) |

<!-- vale handbook.Spelling = YES -->

## Docs site stats and analytics

The technical writing team tracks documentation performance across three key areas: satisfaction, findability, and usefulness. We use a combination of metrics, including user surveys, Google Analytics, user feedback, content audits, and site availability.

We track statistics in the six primary projects: GitLab, Omnibus, Charts, Operator, Runner, and CLI:

- There are over 3,100 documentation pages and 4,400,000 words in the documentation projects.
- Since May 2020, the page count has increased by over 165%, and the word count by over 270%.
- The largest share of pages (30%) and words (30%) are in the **Use GitLab** section of the left navigation.

GitLab team members can view additional documentation metrics on the [doc metrics page](https://internal.gitlab.com/handbook/marketing/product-and-technical-marketing/technical-writing/metrics-kpis/)
and the docs.gitlab.com [LookerStudio dashboard](https://lookerstudio.google.com/reporting/d6af7a2b-2aaa-4f30-8742-811e62777c93/page/IeVBD). For dashboard instructions, see [Google Analytics](https://internal.gitlab.com/handbook/marketing/product-and-technical-marketing/technical-writing/google-analytics/).

## Technical Writer PTO

When Technical Writers take [paid time off](/handbook/people-group/time-off-and-absence/time-off-types/), the rest of the team provides coverage for them.
These team members may require additional context for requests. Requests are incorporated into the list of stage/group and
feature priorities for *their* primary groups.

Options for groups to get help when an assigned Technical Writer is on PTO are:

- [Reviewer Roulette](https://gitlab-org.gitlab.io/gitlab-roulette/?sortKey=stats.avg7&order=-1&visible=maintainer%7Cdocs).
  A rouletted Technical Writer can be pinged or assigned to an issue or merge request.
- A request in the [`#docs`](https://gitlab.slack.com/archives/C16HYA2P5) channel in Slack, where it will be picked
  up by an available volunteer Technical Writer.
- For help with a specific, time-sensitive, in-progress piece of work, a pre-arranged Technical Writer. The Technical
  Writer can be pinged on issues or merge requests and begin participating.

If taking extended PTO (one week or more), Technical Writers and Managers should use the Technical Writer
[coverage issue](https://gitlab.com/gitlab-org/technical-writing/team-tasks/-/blob/main/.gitlab/issue_templates/TW_Coverage.md).
This issue can describe exactly who is providing coverage, for what, and by what means.

### Taking PTO

When taking PTO, Technical Writers:

1. Ensure their [out-of-office messaging](/handbook/people-group/time-off-and-absence/time-off-types/) reflects the available mechanisms for coverage.
   It's important to keep GitLab.com statuses up to date to ensure:

   - [Reviewer Roulette](https://gitlab-org.gitlab.io/gitlab-roulette/?sortKey=stats.avg7&order=-1&visible=maintainer%7Cdocs) can make accurate suggestions.
   - The TW team can easily see the PTO status of all team members when checking the Roulette dashboard.
1. Send a message in the group Slack channels indicating where to find the available mechanisms. For example:

   ```text
   I'm off for the holidays (202y-mm-dd - 202y-mm-dd). For help with documentation while I'm away, see
   https://handbook.gitlab.com/handbook/marketing/product-and-technical-marketing/technical-writing/#technical-writer-pto for ways to get help.
   For urgent _named time-sensitive task_ matters, ping _named TW_.
   ```

### Merge request queue checks

Before a Technical Writer goes on PTO, the writer or their manager should determine who will check the writer's MR queue.
The assigned person should check the queue at least once a day, using one of the following:

- The [GitLab Review Workload Dashboard](https://gitlab-org.gitlab.io/gitlab-roulette/?sortKey=stats.avg30&mode=show&order=-1&hourFormat24=true&visible=maintainer%7Cdocs).
- The **Merge requests** page for the [`gitlab` project](https://gitlab.com/gitlab-org/gitlab/-/merge_requests), filtered by **Reviewer**.
- The [merge request queue](https://gitlab.com/gitlab-org/technical-writing/team-tasks/-/blob/main/.gitlab/issue_templates/TW_Coverage.md?plain=1#L17) section in the coverage issue.

The assigned writer does not need to do the work. When they check the queue, they can:

- Assign the MRs to themselves for review.
- Use Roulette to find other TWs to review.

## Regularly scheduled tasks

Along with Technical Writers' normally assigned work, there are recurring tasks
that need to be completed each month:

- **Release notes and documentation release:** The assigned Technical Writer [reviews the content](https://docs.gitlab.com/development/documentation/release_notes/#review-a-feature-release-note) of the release notes. At the end of the milestone, the writer [publishes the release notes](https://docs.gitlab.com/development/documentation/release_notes/#publish-release-notes) and [creates the monthly release for the docs site](https://gitlab.com/gitlab-org/technical-writing/docs-gitlab-com/-/blob/main/doc/releases.md).

- **Docs project maintenance tasks:** The assigned Technical Writer completes maintenance tasks for the documentation site and its content. This involves [creating a new issue using the `tw-monthly-tasks` template](https://gitlab.com/gitlab-org/technical-writing/team-tasks/-/issues/new?issue[title]=Docs%20project%20maintenance%20tasks%2C%20Month%20YYYY&issuable_template=tw-monthly-tasks) in the `technical-writing` project to track maintenance work. If additional work beyond what's described in the maintenance issue is required, the Technical Writer creates merge requests and additional issues as needed.

### Schedule

<!-- vale handbook.Spelling = NO -->

| Version | Month | Release notes and documentation release | Maintenance tasks |
|---------|-------|----------------------------------------|-------------------|
| 19.9 | February 2027 | TBD | {{< member-by-name "Evan Read" >}} |
| 19.8 | January 2027 | {{< member-by-name "Evan Read" >}} | {{< member-by-name "Marcel Amirault" >}} |
| 19.7 | December 2026 | {{< member-by-name "Marcel Amirault" >}} | {{< member-by-name "Isaac Durham" >}} |
| 19.6 | November 2026 | {{< member-by-name "Ashraf Khamis" >}} | {{< member-by-name "Lorena Ciutacu" >}} |
| 19.5 | October 2026 | {{< member-by-name "Isaac Durham" >}} | {{< member-by-name "Zach Painter" >}} |
| 19.4 | September 2026 | {{< member-by-name "Lorena Ciutacu" >}} | {{< member-by-name "Roshni Sarangadharan" >}} |
| 19.3 | August 2026 | {{< member-by-name "Zach Painter" >}} | {{< member-by-name "Fiona Neill" >}} |

<!-- vale handbook.Spelling = YES -->

### Previous schedule

<!-- vale handbook.Spelling = NO -->

| Version | Month | Release post check | Monthly doc release | Maintenance tasks |
|---------|-------|------------------------------|---------------------|-------------------|
| 19.2 | July 2026 | {{< member-by-name "Roshni Sarangadharan" >}} | {{< member-by-name "Fiona Neill" >}} | {{< member-by-name "Achilleas Pipinellis" >}} |
| 19.1 | June 2026 | {{< member-by-name "Isaac Durham" >}} | {{< member-by-name "Achilleas Pipinellis" >}} | {{< member-by-name "Jon Glassman" >}} |
| 19.0 | May 2026 | {{< member-by-name "Achilleas Pipinellis" >}} | {{< member-by-name "Brendan Lynch" >}} | {{< member-by-name "Uma Chandran" >}} |
| 18.11| April 2026 | {{< member-by-name "Jon Glassman" >}} | {{< member-by-name "Uma Chandran" >}} | {{< member-by-name "Ryan Lehmann" >}} |
| 18.10| March 2026 | {{< member-by-name "Uma Chandran" >}} | {{< member-by-name "Russell Dickenson" >}} | {{< member-by-name "Brendan Lynch" >}} |
| 18.9 | February 2026 | {{< member-by-name "Ryan Lehmann" >}} | {{< member-by-name "Kati Paizee" >}} | {{< member-by-name "Evan Read" >}} |
| 18.8 | January 2026 | {{< member-by-name "Brendan Lynch" >}} | {{< member-by-name "Evan Read" >}} | {{< member-by-name "Marcel Amirault" >}} |
| 18.7 | December 2025 | {{< member-by-name "Evan Read" >}} | {{< member-by-name "Marcel Amirault" >}} | {{< member-by-name "Ashraf Khamis" >}} |
| 18.6 | November 2025 | {{< member-by-name "Marcel Amirault" >}} | {{< member-by-name "Ashraf Khamis" >}} | {{< member-by-name "Zach Painter" >}} |
| 18.5 | October 2025 | {{< member-by-name "Ashraf Khamis" >}} | {{< member-by-name "Zach Painter" >}} | {{< member-by-name "Lysanne Pinto" >}} |
| 18.4 | September 2025 | {{< member-by-name "Zach Painter" >}} | {{< member-by-name "Lysanne Pinto" >}} | {{< member-by-name "Isaac Durham" >}} |
| 18.3 | August 2025 | {{< member-by-name "Russell Dickenson" >}} | {{< member-by-name "Isaac Durham" >}} | {{< member-by-name "Lorena Ciutacu" >}} |

<!-- vale handbook.Spelling = YES -->

## Reviews

Technical Writers are assigned to review merge requests that contain documentation changes authored by GitLab team members and community contributors. The reviews are assigned by subject matter according to the [Technical Writer assignments](#assignments) to [stage groups](/handbook/product/categories/#devops-stages) or other specialties.

### Levels of edit

The Technical Writers use the following levels of edit:

**Light**

- Ensure the pipeline passes and no obvious grammar, spelling, or punctuation errors exist.

**Medium**

- Ensure the pipeline passes and no grammar, spelling, or punctuation errors exist.
- Ensure the content is clear, discoverable, navigable, and written with the user's perspective in mind.
- Ensure the content meets the guidelines in the [Documentation Style Guide](https://docs.gitlab.com/development/documentation/styleguide/).

**Heavy**

- Ensure the pipeline passes and no grammar, spelling, or punctuation errors exist.
- Ensure the content is clear, discoverable, navigable, and written with the user's perspective in mind.
- Ensure the content meets the guidelines in the [Documentation Style Guide](https://docs.gitlab.com/development/documentation/styleguide/).
- Ensure the content conforms to the defined [topic types](https://docs.gitlab.com/development/documentation/topic_types/).
- Ensure the content fits well into the larger documentation set.
- For UI text, ensure the content meets the standards defined in the [Pajamas Design System](https://design.gitlab.com/) and the [Technical Writer Word List](https://docs.gitlab.com/development/documentation/styleguide/word_list/).

#### How the writers apply the levels of edit

To balance quality, speed, and resource constraints, the Technical Writers apply different levels of edit to different documentation.

These guidelines are meant to provide general guidance. They aren't set in stone, and they can be overridden on a case-by-case basis.

These items **do not receive** an edit unless it's specifically requested (and if requested, they receive a **light** edit):

- In the GitLab repository, the Contribution guidelines (in the `/development` directory).
- In the GitLab repository, the `doc/solutions` directory. This information is owned by Solutions Architects.

These items receive a **light** edit:

- Documentation outside of the five main GitLab repositories (GitLab, Charts, Operator, Omnibus, and Runner).
- Deprecations and removals.
- Merge requests authored by other Technical Writers, unless the MR is part of an OKR, or the author requests a more in-depth edit.

These items receive a **medium** edit:

- Day-to-day product documentation requests:
  - New feature work (from [stage groups](/handbook/product/categories/#devops-stages))
  - Improvements
  - Bug fixes
  - Community contributions
- Release notes

These items receive a **heavy** edit:

- Topic type restructuring efforts (["CTRT"](https://docs.gitlab.com/development/documentation/topic_types/))
- OKR work
- UI text

In all cases, the Technical Writer confirms that an authoritative source has checked the documentation for technical accuracy.
The Technical Writer can serve as that authoritative source if they have the required knowledge or
can efficiently perform the necessary verification.

### Review workflow

To balance [velocity](/handbook/engineering/development/principles/#velocity) and quality, the Technical Writers use this workflow:

- When a Technical Writer opens a merge request, another Technical Writer must review and merge.
  - The Technical Writer should not approve or merge their own MR. Instead, they should [request a review](#selecting-a-reviewer) from a peer with Maintainer access. The reviewer merges the MR after the final approval.
    - This requirement aligns with the GitLab [Code Review Guidelines](https://docs.gitlab.com/development/code_review/) and satisfies the GitLab [Change Management Policy](/handbook/security/security-and-technology-policies/change-management-policy/).
- When anyone else (like a developer, community member, or Support team member) opens a merge request:
  - If the MR contains only documentation changes, the Technical Writer:
    - Reviews the content and offers suggestions.
    - Does not directly make large changes (by applying suggestions or pushing commits) to the author's branch unless they have explicit approval in the MR to do so.
      Pushing to a branch can cause hard-to-resolve merge conflicts, and content can be accidentally overwritten.
    - Can use suggestions or commits to make changes themselves only if the writer has agreement from the author to make changes directly to the author's branch.
      In these cases, the author must always review the Technical Writer's changes before the writer merges, to help ensure accuracy.
    - Can apply small suggestions using the **Apply suggestion** feature if an MR is nearly ready to merge.
      Writers can fix things like missing punctuation, typos, and pipeline failures without additional review.
    - Approves and merges the documentation MR when it is ready.
  - If the MR is primarily a code change that also contains a documentation update, the Technical Writer:
    - Offers suggestions for any documentation, UI text, and error message changes, but should not apply any suggestion themselves.
      Making any changes to a code MR can cause pipelines to fail, as code and specs often need to be updated by the engineer to match technical writing suggestions.
    - Approves the MR if the documentation changes are ready to merge.
    - Does not merge code MRs. The MR must be merged by an engineer who also reviews the code change.
  - If the MR is primarily a documentation change, but also has a small code change to update a link to match the change, the Technical Writer:
    - Reviews the content using the same workflow as a documentation-only MR.
    - Can merge *only* if the MR has all [required approvals](#merge-rights).

For more information about review turnaround times, see [Review-response SLO](/handbook/engineering/workflow/code-review/#review-response-slo).

#### Triaging automated group mentions

When a bot or a community contributor mentions either `@gl-docsteam` or several Technical Writers based on CODEOWNERS, TWs should volunteer to:

1. Scan the MR and either volunteer to review it or determine which TW should review it, following the guidelines in [Selecting a reviewer](#selecting-a-reviewer).
1. Then, if the MR:
   - Seems ready for review, assign the selected TW as a reviewer.
   - Doesn't seem ready for review, leave a comment for the contributor asking them to mention the selected TW when they're ready.
1. Edit the bot's comment and format the team mention as code. For example: ``Hi `@gl-docsteam`! Please review this documentation merge request.`` This removes other TWs from the MR's participants list, and they will no longer receive notifications for it. The to-do notification will be updated to show the username in backticks, so team members working from their to-do list will have a visible hint that the MR has been addressed.

### Selecting a reviewer

In most cases, Technical Writers should use the [GitLab Review Workload Dashboard](https://gitlab-org.gitlab.io/gitlab-roulette/?sortKey=stats.avg7&order=-1&hourFormat24=true&visible=maintainer%7Cdocs) to identify someone for a technical writing review. Be sure the page's filter is set to show only Technical Writers and sort by **Assign events last 7 days**.

To get an available Technical Writer, select **Spin the wheel!** on the Dashboard page. In the specific cases where the selected Technical Writer already has a lot of assigned reviews or has recently been very busy, you can select **Spin the wheel!** again to get a different writer.

If you have content that needs a specific assignee, or if you have a merge request for a page that has a DRI (such as the Documentation Style Guide), you can specifically assign the review to that person.

### Determining Technical Writer availability

There are occasions when Technical Writers may be too busy for general team merge request reviews, and need to focus on their groups or other priorities. In those cases, Technical Writers can update their GitLab status by selecting the **Busy** checkbox and adding the 🔴 (`:red_circle:`) emoji, which prevents their name from appearing in the reviewer roulette.

For example, Technical Writers on release duty for a milestone should add the busy indicator to their status for the week preceding the [release date](/handbook/engineering/releases/), to focus on release notes and other requirements.

In all other cases, while Technical Writers can add (and remove) the busy indicator from their profiles, we ask that the busy indicator be in place for no longer than two days at a time, and be employed no more than once every two weeks. (Using the busy indicator during releases doesn't count toward this limit.) If you need more time not participating in the review roulette, be sure to talk to your manager so they can help (which may include additional use of the busy indicator).

## Merge rights

The Technical Writing team is given merge rights (through [Maintainer access](/handbook/engineering/workflow/code-review/#how-to-become-a-project-maintainer))
to GitLab projects as part of their role. Not all developers get Maintainer access, so Technical Writers must use this privilege responsibly.

As Maintainers, Technical Writers must limit what they merge to:

- Documentation, typically in Markdown-formatted files.
- UI text, error messages, and link-related updates in code files, with the approvals of appropriate engineers.
  You can skip engineer approval and ask a member of the [TW leadership team](https://gitlab.com/groups/gitlab-org/tw-leadership/-/group_members?with_inherited_permissions=exclude)
  or the [TW DocOps team](https://gitlab.com/groups/gitlab-org/technical-writing/tw-docops/-/group_members?with_inherited_permissions=exclude) to approve code changes when:
  - The only code changes in a documentation MR are link fixes to match changes to documentation files or anchor names, and
  - The pipeline completed successfully.
- Documentation-related tooling and configuration such as linters, and changes
  to the [`docs-gitlab-com`](https://gitlab.com/gitlab-org/technical-writing/docs-gitlab-com) project. Engineers
  are available for code review and merges.

In addition, Technical Writers must:

- Never merge an MR with a failed pipeline.
- Ensure that MRs are complete before merging, with appropriate labels and milestones.
- Ensure that the DRI has reviewed and approved the MR.

## Onboarding Technical Writers

While the Technical Writer is onboarding, they will be assigned to
shadow groups and then start contributing as trainees. Veteran Technical Writers will coach them through the process.

For more information about onboarding phases and tasks, see the [Technical Writer onboarding template](https://gitlab.com/gitlab-org/technical-writing/team-tasks/-/blob/main/.gitlab/issue_templates/tw_onboarding.md).

## Standups

We have set up [Geekbot](https://app.geekbot.com/dashboard/home) for our twice-weekly
standups (at 10:00 AM, Tuesday and Thursday, in your local time zone) and a random weekly question
(run on Wednesdays at 12:00 PM).

All members can edit and manage the standups.

To add a new member to the daily standup:

1. Visit the [Geekbot dashboard](https://app.geekbot.com/dashboard/home) and
   sign in using your Slack account when asked.
1. Select the [Tues/Thurs ping](https://app.geekbot.com/dashboard/standup/42533/manage?members)
   standup and search for the member by name in the **Add participants** area.
1. Give the newly added member Manage access and select **Save** in the upper
   right corner.

To add a new member to the Weekly Wednesday Question standup:

1. Visit the [Geekbot dashboard](https://app.geekbot.com/dashboard/home) and
   sign in using your Slack account when asked.
1. Select the [Weekly Wednesday Question](https://app.geekbot.com/dashboard/standup/28408/manage?members)
   standup and search for the member by name in the **Add participants** area.
1. Give the newly added member Manage access and select **Save** in the upper
   right corner.

As a member of the Technical Writing team, you're encouraged to add your
question to the list of random Wednesday questions! To do so:

1. Visit the [Weekly Wednesday Questions](https://app.geekbot.com/dashboard/standup/28408/manage?questions).
1. Under the **Questions** section, you can see a "This is a random set of questions"
   question. Hover over the two arrows on the right, and select **Edit**.
1. Scroll to the bottom and select **Add question**.
1. Select **Save questions**.

## Community contribution opportunities

We welcome [improvements to content](https://docs.gitlab.com/development/contributing/)
as well as to the development of our
documentation website, at https://docs.gitlab.com.

For more information about community contributions, see:

- [List of available issues](https://gitlab.com/gitlab-org/gitlab/-/issues/?sort=created_date&state=opened&label_name%5B%5D=documentation&label_name%5B%5D=docs-only&label_name%5B%5D=Seeking%20community%20contributions)
- [GitLab Docs repository](https://gitlab.com/gitlab-org/technical-writing/docs-gitlab-com)

## Make an urgent content update on docs.gitlab.com

The documentation website is refreshed every hour. On rare occasions, we might have to publish documentation
updates a little faster. If you need an urgent update, follow the steps to [manually deploy the docs site](https://docs.gitlab.com/development/documentation/site_architecture/deployment_process/#manually-deploy-to-production).

## Report a docs website problem or infrastructure issue

Report website bugs or feature requests in the [issue list for the GitLab Docs project](https://gitlab.com/gitlab-org/technical-writing/docs-gitlab-com/-/issues).

For outages or website availability issues, see [Docs site infrastructure](https://gitlab.com/gitlab-org/technical-writing/docs-gitlab-com/-/blob/main/doc/infrastructure.md).

## Related topics

- [Documentation workflow](https://docs.gitlab.com/development/documentation/workflow/)
- [Set up your local environment](https://docs.gitlab.com/development/documentation/authoring_environment/)
- [Documentation site architecture](https://docs.gitlab.com/development/documentation/site_architecture/)
