---
title: "Workflows for working with community contributions"
description: All processes the Co-Create & Community Engineering team work with
---

## Workflows

## How we plan work

The team uses the [Contributor Success Kanban board](https://gitlab.com/groups/gitlab-org/-/boards/7745119?label_name[]=Contributor%20Success).
Issues must:

- Be created in the `gitlab-org` group
- Have the `Contributor Success` label
- Have at least 1 `workflow` label from the list below

We use `priority` labels to designate focus areas per quarter.

### Workflow labels

- `workflow::validation backlog`: Issues start in our backlog so the team can validate for effort vs. impact against our KPIs, OKRs and team strategies.
- `workflow::refinement`: These issues are validated and refined through planning and team discussion before they are marked as ready. Issues should have an Implementation Plan section before moving to the next workflow stage.
- `workflow::ready for development`: These issues are ready to be picked up, have an Implementation Plan section and a `priority` label.
- `workflow::in dev`: Issues actively being worked on this quarter.
- `workflow::blocked`: Issues currently blocked. The description must note the blocker and include a link to issues that would unblock.
- `workflow::complete`: Issues that are resolved after implementation. These should be highlighted in reports back to the team and Developer Relations department before being closed.

### Priority labels

- `priority::1` (highest priority): Issues critical to the current quarter's KPIs and OKRs, or urgent bugs blocking work for contributors.
- `priority::2`: Issues aligned with current quarter's goals but without urgent due dates.
- `priority::3`: Issues that support long-term objectives without impact on current quarter goals.
- `priority::4` (lowest priority): Issues that bring incremental value but can wait for additional capacity.

### How to pick issues

Team members should select issues from `workflow::ready for development` based on `priority` label.
While the team focuses on `priority::1` and `priority::2` issues for the current quarter, sometimes it makes sense to pick up a lower-priority task between larger projects.
We are guided by GitLab's values on [efficiency](/handbook/values/#efficiency) and [iteration](/handbook/values/#iteration) to act as [managers of one](/handbook/values/#managers-of-one) when choosing tasks.

### Retrospective

Every quarter we hold an asynchronous retrospective [(example)](https://gitlab.com/gitlab-org/developer-relations/contributor-success/team-task/-/issues/665) using GitLab issues.

Questions asked are:

- What should we start?
- What should we stop?
- What should we continue?

The team DRI is responsible for creating an issue in the team tracker
[`gitlab-org/developer-relations/contributor-success/team-task`](https://gitlab.com/gitlab-org/developer-relations/contributor-success/team-task/-/issues)
so that it can be easily retrieved in the future.

The team DRI is responsible for digesting the feedback and selecting one issue, after votes, to take into the new quarter.

### Stand-up

The purpose of this stand-up is to collaborate between team members. This is a team-specific
meeting to check in on blockers, progress and ways to think differently and iterate towards our goals.

- Agenda: <https://docs.google.com/document/d/1chIzCdg1CNRrRRuYR7c7OW_BF1mBxKFTJoXyP2HLt4E/edit#heading=h.o6qzal1u0b7i>

## Real-time Communications

A GitLab contributor room is available on [Discord](https://discord.gg/gitlab) for people interested in contributing to GitLab. This is open to everyone to join and is a good place for community members to network and help each other.

## Issues

### Contributor links

To make it clear and easy for everyone to contribute, a [triage-ops processor](https://gitlab.com/gitlab-org/quality/triage-ops/-/blob/master/triage/processor/issue_summary.rb)
adds contributor links to issues to enable customers/community members to label, close and assign themselves.

Not a GitLab Team member, new here or looking to get started with contributing features, bug fixes, translations or more to GitLab?
Start your onboarding via the [Contributor platform](https://contributors.gitlab.com/).

GitLab team members can suppress the contributor links by adding the `suppress-contributor-links` label.

### Labeling issues for community contributors

See guidance on [seeking wider community contributions](/handbook/marketing/developer-relations/engineering/community-contributors-workflows/#seeking-wider-community-contributions) and the [criteria for `quick win` issues](/handbook/marketing/developer-relations/engineering/community-contributors-workflows/#criteria-for-quick-win-issues).

### Community issues workflow manual process

See the [partial issue triage checklist](/handbook/product-development/how-we-work/issue-triage/#partial-triage-checklist).

## Merge Requests

Wider community merge requests are MRs opened by a person that's not present on <https://about.gitlab.com/company/team/> (excluding any bot, service account users or individual contractors).

### Labels

- The `Community contribution` label is automatically applied by the [GitLab Bot](https://gitlab.com/gitlab-bot) to MRs submitted by wider community members.
  - You can see the list of MRs in [`gitLab-org` list of merge requests](https://gitlab.com/groups/gitlab-org/-/merge_requests?label_name[]=Community+contribution).
- [Learn more about the cadence and conditions for this automation](/handbook/engineering/infrastructure-platforms/developer-experience/triage-operations/#label-community-contributions).
- The `1st contribution` label is added to first-time contributions. Every time a contributor is opening a merge request under the `gitlab-org` namespace for the first time, the label `1st contribution` is automatically applied to the merge request.
  - You can see the list of MRs in [`gitlab-org` list of merge requests](https://gitlab.com/groups/gitlab-org/-/merge_requests?label_name%5B%5D=1st+contribution).
  - [First-time contributors](/handbook/marketing/developer-relations/engineering/community-contributors-workflows#first-time-contributors) are also awarded a gift as our way to say thanks.

### Triage reports

See [Community-related triage reports](/handbook/engineering/infrastructure-platforms/developer-experience/triage-operations/#community-related-triage-reports).

### Scheduled workflow automation

See [Community-related scheduled workflow automation](/handbook/engineering/infrastructure-platforms/developer-experience/triage-operations/#community-related-scheduled-workflow-automation).

### Reactive workflow automation

See [Community-related reactive workflow automation](/handbook/engineering/infrastructure-platforms/developer-experience/triage-operations/#community-related-reactive-workflow-automation).

## Merge request coaches

[Merge request coaches](/job-description-library/expert/merge-request-coach/) are available to help contributors with their MRs. This includes:

- Identifying reviewers for the MR.
- Answering questions from contributors.
- Educating contributors on the [contribution acceptance criteria](https://docs.gitlab.com/ee/development/contributing/merge_request_workflow#contribution-acceptance-criteria).
- Or completing the MR if the contributor is unresponsive or unable to complete.
  - In that case, the `coach will finish` label will be added to the MR and the coach will either directly push new commits to the MR, or re-create a new MR with the original changes.
  - Contributors can mention the coaches in their MRs by typing `@gitlab-org/coaches`.

The list of current merge request coaches can be found in the [team page](/handbook/company/team/) by selecting `Merge Request
Coach` in the department filter.

There is also the [`#mr-coaching`](https://gitlab.slack.com/archives/C2T9APP9C) channel in GitLab Slack if GitLab team
members have any questions related to community contributions.

More information on merge request coaches (including how to become a merge request coach) can be found in the
[MR coach lifecycle page](/handbook/marketing/developer-relations/engineering/merge-request-coach-lifecycle).

## Contributing to the GitLab Enterprise Edition (EE)

### For community contributors

To contribute to any of the paid features in [GitLab Enterprise Edition](https://gitlab.com/gitlab-org/gitlab/-/tree/master/ee), community contributors will need to add a license to their GDK. If they don't already have a license, they can get a [free trial for 30 days](https://about.gitlab.com/free-trial/) (choose the Self-Managed option). If they cannot complete their work in 30 days, a new EE license for 90 days for a limited number of users (100) can be issued.

Renewal of this license:

- In the event of active contributions in the previous license cycle, this license can be renewed for a further year.
- If there have been no active contributions in the previous license cycle, a 90 day renewal can be granted.

Contributors will need to create an request in this project to request their license: [Wider Community Contributor License Request](https://gitlab.com/gitlab-org/developer-relations/contributor-success/team-task/-/issues/new?issuable_template=contributor_ee_license_request).

### Processing Enterprise Edition (EE) License Requests

To be completed by a GitLab team member:

#### Prerequisites

- Access to Zendesk support portal, requested via [Zendesk Global Light Agent form](/handbook/support/internal-support/#requesting-a-zendesk-light-agent-account).

#### Process

- Login to Zendesk through Okta
- Access the [GitLab L&R Internal Requests form](https://gitlab-internal.zendesk.com/hc/en-us/requests/new?ticket_form_id=22783840298780)
- Choose from **Other** > **Wider community license** from the subsequent dropdown list
- Fill out the required fields provided in the request issue
  - Contact information: Use the requesting contributor's information
- Other required fields:
  - True-up: 0
  - Priority of request: Low
  - License type: Ultimate (unless otherwise specified)
  - Expiration date:
    - 90 days for new contributors
    - 1 year for renewals
  - Use Nick's email as approving manager if it is a 1 year renewal
- In "What is the reason for the license being issued?" specify `Wider community contributor EE license request` and add a link to the license request issue
- Add a public comment to the request issue indicating the request has been submitted
- The support form, when submitted, gives the user a link to the pipeline that "creates" the request in Zendesk. Save the link to this pipeline in an internal comment in case there are any issues that need investigating later

The Support team will respond following [this workflow](/handbook/support/license-and-renewals/workflows/self-managed/creating-wider-community-license) within 24 hours.

{{% alert title="Note" color="primary" %}}
(GitLab team members) You can find a video of this by searching Google Drive [here](https://drive.google.com/drive/u/0/search?q=Wider_EE_Developer_License_Renewal.mov)
{{% /alert %}}

#### Close

After license is provisioned:

- Add a public comment on the issue with confirmation that the license request has been provisioned
- Add a confidential comment with a screenshot of the "Private Note" included in the email sent to you by support
- Close the issue

## DCO and CLA Guidance

All external contributions to GitLab are subject to the [GitLab DCO or CLA](https://about.gitlab.com/community/contribute/dco-cla/), depending
on where the contribution is made and on whose behalf.

Instructions for corporate contributors to enter into an overarching Corporate CLA covering all contributions made on
their behalf are set out on the [DCO-CLA page](https://about.gitlab.com/community/contribute/dco-cla/#need-a-corporate-cla-covering-all-contributors-on-behalf-of-your-organization).

### Corporate CLA Contributor Management

Contributor success has been assisting the Legal and Corporate Affairs team with the creation and maintenance of a namespace under which GitLab can maintain lists of users associated with Corporate CLAs.

This group can be found here: https://gitlab.com/gitlab-corporate-cla

#### Adding a new group

Subgroups under `gitlab-corporate-cla` are managed declaratively via OpenTofu in the [`gitlab-corporate-cla/config`](https://gitlab.com/gitlab-corporate-cla/config) project. All standard group settings (visibility, description, project/subgroup creation levels, wiki disabled, mentions disabled, share-with-group lock, etc.) are applied automatically by the pipeline.

1. Open a merge request against [`gitlab-corporate-cla/config`](https://gitlab.com/gitlab-corporate-cla/config) that adds an entry to [`groups.yaml`](https://gitlab.com/gitlab-corporate-cla/config/-/blob/main/groups.yaml):

    ```yaml
    - name: Acme Corp
      path: acme-corp
    ```

    1. `name` — the organization's legal name (used as the group display name and in the standard description).
    1. `path` — the URL-safe slug for the subgroup (lowercase, hyphens for spaces).
    1. `description` — *(optional)* override for the standard `"Approved contributors for {name} under the GitLab Corporate CLA"` template. Use when the organization needs additional context in the description.

1. The MR pipeline runs `tofu plan` and posts the diff. Review and merge once the plan shows the expected single new group.
1. The `main` branch pipeline runs `tofu apply` and creates the subgroup. Drift detection runs on a schedule against `main` as a safety net.
1. Perform the post-apply manual steps (these settings are not yet supported by the [GitLab Terraform provider](https://registry.terraform.io/providers/gitlabhq/gitlab/latest/docs/resources/group) and must be configured by hand):
    1. In the new subgroup's **Settings > General > Permissions and group features**, set:
        1. **Customer relations is enabled** — disable
        1. **GitLab Duo availability** — `Always off`
    1. Add the user account of the Organization's designated user manager(s) to the group as `Owner` (under **Group information > Members**).
    1. Remove your user account as a direct member of the subgroup (under **Members**, filter for `Membership = Direct`, click the 'kebab menu', select 'Leave Group').

## Educational materials

1. [Gitpod with GDK - Introduction (video)](https://www.youtube.com/watch?v=OzgGP5tT4bo)
1. [Gitpod with GDK - Setup (video)](https://www.youtube.com/watch?v=6VNm36wdXnI)

## GitLab Notable Contributor Selection Process

See [GitLab Notable Contributor Selection Process](/handbook/marketing/developer-relations/engineering/notable-contributor-process).

## Contributor Thanks messages

The Contributor Success team has been regularly thanking wider community members for active participation in merge requests.
This takes the form of a weekly thanks message in:

- The `#thanks` channel in discord.
- The `community` area of the forum.

Thanking wider community members for having MRs merged, as well as participating in other's MRs that were merged.

These messages are generated with the help of a [script](https://gitlab.com/gitlab-org/developer-relations/contributor-success/toolbox).
The script runs on a Monday morning.

Tracking issue:

- [Wider Community message](https://gitlab.com/gitlab-org/developer-relations/contributor-success/team-task/-/issues/186)

### Manual execution

In the event you need to generate the message(s) manually, you will need to follow these prerequisite steps:

1. Check out the latest `main` branch of the toolbox project: `git clone git@gitlab.com:gitlab-org/developer-relations/contributor-success/toolbox.git`
1. Change directory to the checked out project: `cd toolbox`
1. Install the required gems: `bundle install`

1. Execute the script following the 'wider' example [here](https://gitlab.com/gitlab-org/developer-relations/contributor-success/toolbox/#community-mr-participants)
1. Make sure to check the duration for which you want to run the report.
1. Paste the resulting message into `#thanks` in discord.
1. Double check the message that was pasted - to ensure the users/names all look 'right'.
1. Send the message and join in the celebrations!
1. Record the PI numbers from the message in the [tracking issue](https://gitlab.com/gitlab-org/developer-relations/contributor-success/team-task/-/issues/186) if necessary.
1. Update the assignee of the tracking issue and due date.

## Organizing and promoting events

### Event planning

- Draft an agenda before the meeting, including (make sure the document is open to anyone with the link)
  - Roll call, introductions
  - Various topics
  - Open floor for the community to bring topics
- Include instructions on how to join
  - Link to zoom (or any other video platform)
- Add the event to the [Developer Advocacy team calendar](/handbook/marketing/product-and-technical-marketing/developer-advocacy/#calendar). If you are not a GitLab Team Member, ask a member of the [Developer Relations](/handbook/marketing/developer-relations/) team to add the event to the calendar.
- Follow the instructions below for social support or open a request at the [Code Contributor's planning repo](https://gitlab.com/gitlab-com/marketing/community-relations/contributor-program/general/issues/new?issuable_template=event-support-request).

### Social

- Draft a short action-oriented copy like: "Join the upcoming GitLab hackathon (link) on the N."
- Share the message on the following channels at least 2 weeks before, 1 week, and a day before the event:
  - Twitter: use your account but mention `@gitlab` (note: never share a Zoom link on Twitter)
  - [GitLab Community Discord](https://discord.gg/gitlab)

### Event platforms

- Ask [John Coghlan](https://gitlab.com/johncoghlan) for adding the event on [meetup.com](https://www.meetup.com/gitlab-virtual-meetups/).
- Add the event on [GitLab Events page](https://about.gitlab.com/events/).

### Hackathons

There will be a quarterly [Hackathon](https://about.gitlab.com/community/hackathon/) for GitLab community members to come together to work on merge requests, participate in tutorial sessions, and support each other on the [GitLab Discord](https://discord.gg/gitlab).  Agenda, logistics, materials, recordings, and other information for Hackathons will be available on the [GitLab Community Hackathon](https://about.gitlab.com/community/hackathon/) page.

The event planning will be done following the [Hackathon issue template](https://gitlab.com/gitlab-org/developer-relations/contributor-success/team-task/-/issues/new?description_template=hackathon).

### Virtual hackathons/hackathon-in-a-box

We also encourage wider community members to organize events to encourage and support new contributors to GitLab. This could be done as a part of in-person or virtual GitLab meetups.

If wider community members are interested in including a hackathon as a part of a meetup, ask them to include this information when they open a [meetup issue](https://gitlab.com/gitlab-com/marketing/community-relations/evangelist-program/general/issues/new?issuable_template=meetup-organizer). Contributor Success team members will get in touch with the organizer and provide the necessary resources to support the event.

Some of the available resources can be found in the [hackathon-in-a-box folder](https://drive.google.com/drive/u/0/folders/1YWb16NAguXq9T5kORhNcXOk3JwdaS4NF), [GDK tutorials playlist](https://www.youtube.com/playlist?list=PL05JrBw4t0KofEeWa9EXUOS8kJHOjIH_W), etc. The program manager should also work with the organizer to create a list of issues that are good for first-time/inexperienced contributors and share the list with participants prior to the event. There should also be coordination with the organizer on GitLab merchandise that can be distributed to anyone who creates a Merge Request during the event.

### Community office hours

To facilitate communication between the wider community and GitLab team members, product teams may host community office hours. The purpose of these office hours is to gather wider community feedback on product/development, discuss wider community contributions, review MR backlog, and other topics. Office hour related issues or MRs will have the label `Office Hours` as you can see in [these examples](https://gitlab.com/groups/gitlab-org/-/issues?scope=all&utf8=%E2%9C%93&state=all&label_name[]=Office%20Hours).

Calls will be open to everyone and recordings will be posted after the call. See examples of past office hours from [this playlist](https://www.youtube.com/playlist?list=PL05JrBw4t0KrXZEInAfyddFlalvwaxL-I). To make it easier for the community to find the videos, each stage should create their own office hours playlist and link to it from their handbook page.

All the community office hour calls should be added to the [Developer Advocacy calendar](/handbook/marketing/product-and-technical-marketing/developer-advocacy/#calendar) and [meetup.com group](https://www.meetup.com/gitlab-virtual-meetups/).

#### Security reminder for office hours recordings

Before publishing any office hours recording, ensure that no credentials or secrets are visible or audible in the video. This includes, but is not limited to:

- GitLab personal access tokens (PATs)
- Project access tokens
- Group access tokens
- OAuth tokens or client secrets
- SSH keys
- API keys or webhook secrets
- Passwords or passphrase

If a credential is accidentally exposed during a session, it must be revoked and rotated immediately — do not rely solely on editing the video due to the nature of live streamed videos.

For team members who upload recordings directly (rather than publishing a converted live stream), GitLab's internal [video scanner](https://internal.gitlab.com/handbook/security/product_security/token-leaks/video_scanner/) is available to help detect token leaks before the video goes public. Using this tool is optional but strongly encouraged as an extra layer of protection.

Please refer to GitLab's [YouTube uses and access](/handbook/marketing/marketing-operations/youtube/) for more information on how to best use YouTube for publishing and managing recordings.

#### How to organize a community office hour call

**Preparation**

- Once you have a finalized date and time, add it to:
  - the [meetup.com group](https://www.meetup.com/gitlab-virtual-meetups/) (meetup.com account available at your GitLab's 1Password vault)
  - the [developer advocacy calendar](/handbook/marketing/product-and-technical-marketing/developer-advocacy/#calendar)
- Update [the office hour running notes doc](https://docs.google.com/document/d/18ddf5d5xASImrYnAG9P8VJXe0I63SBXy7ufDBBNB5H4/edit#) with the Zoom URL and call details
- Announce it [on Discord](https://discord.gg/gitlab)
- Tweet about it, [tagging GitLab](https://twitter.com/gitlab)
- The day before the call, post reminders on Discord

**Running the call**

- Ask for everyone's permission to live stream the call. Then press the Live Stream on YouTube button in Zoom to begin streaming.
- Enable close captioning in zoom for accessibility.
- Once the call starts, do a round of introductions asking the question: "what brought you to this call". This will help you adjust the call to the community's needs and, answer any questions/meet their expectations.
- Keep detailed meeting minutes

**After the call**

- Add the youtube video to the "office hour calls" playlist
- Post a recap and the video recording on Discord

#### Community challenge

To encourage contribution to priority issues on an on-going basis (and not just during Hackathons), we will maintain a list of up to 5 priority issues for each [product stage](/handbook/product/categories/) and prizes will be given to wider community members who have MRs merged for these issues. These issues will have the label [`Community challenge`](https://gitlab.com/groups/gitlab-org/-/issues?label_name%5B%5D=Community+challenge) and more details such as prizes, assignment of these issues, etc.

## Supporting the Wider Community Contributors

### Unblocking wider community contributions

The Contributor Success team helps unblock wider community contributors and move contributions forward. Sometimes other teams at GitLab do not have the capacity to support community contributions, but this should not stop the community from contributing.

These 10 GitLab values support efforts to unblock the wider community and push forward:

1. [Do it yourself](/handbook/values/#do-it-yourself)
1. [Short toes](/handbook/values/#short-toes)
1. [Collaboration is not consensus](/handbook/values/#collaboration-is-not-consensus)
1. [Bias for action](/handbook/values/#operate-with-a-bias-for-action)
1. [Disagree, commit, and disagree](/handbook/values/#disagree-and-commit)
1. [Escalate to unblock](/handbook/values/#escalate-to-unblock)
1. [Cleanup over sign-up](/handbook/values/#cleanup-over-sign-off)
1. [Minimal valuable change](/handbook/values/#minimal-valuable-change-mvc)
1. [Everything is in draft](/handbook/values/#everything-is-in-draft)
1. [Make two-way door decisions](/handbook/values/#make-two-way-door-decisions)

### Seeking wider community contributions

GitLab team members seeking help can reach out to the wider community for contributions. It is suggested to start with smaller `quick win` issues that have a clear implementation plan before moving on to bigger project requests.

- Add a `quick win` label to the issue by following the [criteria for `quick win` issues](#criteria-for-quick-win-issues).
- Share the issue on the GitLab Community Discord in the [#contribute channel](https://discord.com/channels/778180511088640070/997442331202564176).
- If a community contributor expresses interest, assign them to the issue.
- Follow up with the community contributor to see if they need help.

### Criteria for `quick win` issues

GitLab guides the wider community to search for issues with the `quick win` label when looking to contribute.
These issues are intended to be straightforward for community contributors and quick enough to complete while still learning the contribution process.
This follows [GitLab's mission](/handbook/company/mission/#mission) to enable everyone to contribute and to support our first-time contributors onboarding with the community.

AI triage assesses every new team-authored issue and applies the `quick win` label when the issue:

- Have a clear, self-contained implementation plan (or be straightforward enough that one could easily be written)
- Be deliverable quickly and easily by a wider community contributor
- Not require deep knowledge of the codebase

Team members can also apply the label directly, and AI will assess whether it agrees.
If AI does not believe the issue qualifies as a `quick win`, it will ping the team member who added the label
(it will not remove the label).

[GitLab Bot](https://gitlab.com/gitlab-bot) removes the label when it has been applied for over a year or when the issue becomes blocked.

### Criteria for `quick win::first-time contributor` issues

During the onboarding process, new contributors are linked to `quick win::first-time contributor` issues. These issues are intended to help new contributors learn the process of contributing by using our easiest and most straight forward issues. When creating a `quick win::first-time contributor` issue, it is recommended to add a support contact.
Each contributor may complete only one `quick win::first-time contributor issue`. After completing their first, contributors should move on to other issues. There is no limit on regular `quick win` issues. 

- The issue description must include an implementation plan as a second or third level heading with guidance
to help contributors get started.
For example `## Implementation`, `### Implementation`, `## Implementation plan` and `### Implementation guide` are all acceptable.
This section can be very brief or offer possible actions to resolve the issue.
- It's recommended to include at least 1 GitLab team member or experienced community contributor (e.g., "Support contact: @username") tagged in the `Implementation plan` section

### First-time contributors

Every time a contributor is opening a merge request to a GitLab namespace for the first time, the label "~1st contribution" is automatically applied to the merge request.

### Working with the Core Team

More information on the [Core Team](https://about.gitlab.com/community/core-team/) is available in the [Core Team handbook page](/handbook/marketing/developer-relations/engineering/core-team/).

### GitLab Duo for Contributors

To support our mission to enable everyone to contribute, we offer complimentary GitLab Duo Enterprise
licenses across the GitLab community forks for all our wider community contributors.
[GitLab Duo](https://about.gitlab.com/gitlab-duo/) features Code Suggestions, Chat, Root Cause Analysis
and more AI-powered features to help boost efficiency and effectiveness by reducing the time required
to write and understand code and pipelines.
Community contributors receive GitLab Duo once approved for [requesting access to the community forks](https://gitlab.com/groups/gitlab-community/community-members/-/group_members/request_access).

### Highlighting high-value contributions with product bonuses

This is an experiment that we run in FY25Q4 (November 2024 - January 2025).

To highlight high-value contribution directions, the contributor success team might set up a dedicated budget that product managers (PM) can give out to contributors in their area in a given timeframe. The overall budget is shared equally across user-facing product stages where PMs can apply labels (`community-bonus::100`. `community-bonus::200`, `community-bonus::300`. `community-bonus::500`) to show how much value they give to the specific issue/epic. The bonus is accounted for when the issue is closed or in case of an epic, the contributor success team can give out part of the bonus for specific issues as discussed by the respective PM. PMs are expected to stay within their budgets when selecting issues.

Bonuses can be granted after the contribution too.

A bonus in this context is not a monetary grant. These bonus points can only be used to make purchases in the [contributor store](https://gitlab-contributor.brilliantmade.com/).

#### Process

Once an issue with a community bonus label is closed, it appears on [a triage report](https://gitlab.com/gitlab-org/developer-relations/contributor-success/team-task/-/issues/960). A Co-Create & Community Engineering team member will:

##### Verify the contribution

- Visit the issue and check it is assigned to a wider community contributor.
- Check the linked merge requests were authored by a wider community contributor.
- If the above is clear, proceed to [award the bonus points](#award-the-bonus-points).
- If the above is not true, remove the `community-bonus::` scoped label.
- If there is any uncertainty, ping the relevant team on the issue to confirm.

##### Award the bonus points

- Go to https://contributors.gitlab.com/users/[GitLab username]
- Scroll down to **Bonus Points**
- Click **Add points**
  - Use the issue link as the reason
  - Enter the number of bonus points
  - Select `Community bonus` as the activity type
  - Select **Add points**
- Verify that the points you awarded are displayed in the **Bonus Points** section
- On GitLab, add the `community-bonus-awarded` label to the issue

### For contributors who don't own a credit card

For contributors who don't own a credit card and need to be manually verified,
ask them to register and raise a [support request](https://support.gitlab.com/hc/en-us/requests/new)
using the **Gitlab.com user accounts and login issues** reason.

### For contributors who run out of compute minutes or other CI/CD resources

Wider community members may run out of monthly compute minutes, or run into other [GitLab CI/CD limits](https://docs.gitlab.com/ee/user/gitlab_com/index#gitlab-cicd) if they are working from a personal fork.

The solution is to work from the [GitLab community forks](https://gitlab.com/gitlab-community/meta#about).

### Contacting contributors

To be respectful to the contributor's privacy, we will only use contact data that is publicly available to reach out to them.

Here are some ways to reach out to contributors:

- You can mention them in an issue using their GitLab username.
- In private through our communication platform (Discord, Slack, etc.).
- A user might have e-mail on their GitLab profile. Sometimes users have the same username in other platforms (e.g. GitHub), and might have more information on their profiles there.
- Their e-mail address is stored in their git commits, unless they choose to use a [private commit e-mail](https://docs.gitlab.com/ee/user/profile/index#private-commit-email).

Once you've found out the best way to contact them, you can choose to use a mention, e-mail, or Discord.

### Contributor blog post series

Goal is to publish a regular blog post featuring contributors from the community.  The format will be a [casual Q&A with a community member](https://about.gitlab.com/blog/2018/08/08/contributor-post-vitaliy/) and will be posted on the [GitLab blog page](https://about.gitlab.com/blog/).

When developing a blog post, follow the [blog guidelines](/handbook/marketing/blog/).

## Contributor outreach campaigns

Outreach campaigns help us reconnect with past contributors to GitLab who have stopped
or users who have expressed interest in contributing but have not started.
When reaching out, we plant trees in the [GitLab forest](https://tree-nation.com/profile/gitlab)
in their name to recognize their past and/or potential future contributions.

### Outreach goals

The Contributor Success team experimented with different criteria and messages to create a repeatable
outreach campaign with three goals:

1. Maximize community members opening new merge requests
1. Minimize time commitment from Contributor Success to run the campaign
1. Prevent outreach campaigns from being a nuisance or appearing like marketing spam

### Candidate criteria for return contributors

- 0 opened merge requests in the last 3 months
- Must have merged 2 or more merge requests in the last 12 months
- Has not previously been contacted in an outreach campaign

### Candidate criteria for new contributors

- Requested and received access to the community forks at least 1 month ago
- No merged merge requests in their history
- Has not previously been contacted in an outreach campaign

### Tracking Results

Outreach campaign results are tracked in the [Outreach resuts spreadsheet](https://docs.google.com/spreadsheets/d/1oAkJsYoeRmcYevacWb_PK339C1F-wi-cfy4p7F7BlSg/edit?usp=sharing)
and reported in the [Report on all outreach campaigns issue](https://gitlab.com/gitlab-org/developer-relations/contributor-success/team-task/-/issues/517).

#### Results for return contributor campaigns

| Outreach campaign    | Criteria         | Total outreach users | Returned users | User return rate | Merged MR | Opened MR | Closed MR |
|----------------------|------------------|----------------------|----------------|------------------|-----------|-----------|-----------|
| December 2023        | 6 months idle    | 49                   | 7              | 14.29%           | 11        | 0         | 2         |
| January 2024         | 3 months idle    | 124                  | 12             | 9.68%            | 15        | 2         | 2         |
| April 2024           | 3 months idle    | 40                   | 5              | 12.50%           | 12        | 1         | 1         |

#### Results for new contributor campaigns

| Outreach campaign    | Criteria         | Total outreach users | Returned users | User return rate | Merged MR | Opened MR | Closed MR |
|----------------------|------------------|----------------------|----------------|------------------|-----------|-----------|-----------|
| April 2024           | 0 contributions  | 274                  | 6              | 2.19%            | 4         | 2         | 1         |

#### Observations on results

- To date, the return contributor campaigns has been a success with an average user return rate of 11%, 24 returned contributors, and 38 merged merge requests.
- The April experiment with a new contributor campaign was less successful with a 2% contribution rate.
  - This campaign did not have a time restriction on how long ago users requested community forks access and likely many users had lost interest in getting started.
  - It is expected that return contributors would be more successful than new contributors in opening a merge request.
- In addition to opened and merged merge request results, we observed user engagement in the issues, onboarding task completion, and apreciation of the tree planting.
- Many contributors will not have the availability to make a merge request within 1 month of the outreach to appear in these results. The campaign might be a positive reminder of the opportunity to contribute at a later time.

### Outreach campaign scheduling

Outreach campaigns are targeted to run every 3 months but should coincide with an announcement that might entice contributors.
For example, announcing an upcoming hackathon or a new contributing feature like GDK-in-a-box.

### Outreach campaign workflow

#### Review candidate pool

The Contributor Success team reviews the candidate pool to remove:

- Any known GitLab team members with either a GitLab account or a personal account
- Longstanding contributors who have lapsed but should be contacted separately outside of the campaign (e.g. Core members, former MVPs, GitLab Heroes, etc.)
- Any known community members who have had code of conduct violations, expressed they do not want to be contacted,
or expressed they do not want to contribute to GitLab

#### Create issues and plant trees

- Use the temporary branch [`temp-outreach-path` in the reward engine project](https://gitlab.com/gitlab-org/developer-relations/contributor-success/reward-engine/-/tree/temp-outreach-patch?ref_type=heads)
- Paste candidate usernames into the `recipients` variable in [the `RewardIssuer` module](https://gitlab.com/gitlab-org/developer-relations/contributor-success/reward-engine/-/blob/temp-outreach-patch/lib/reward_issuer/gitlab.rb?ref_type=heads)
- Run `bundle exec bin/reward_engine`
- Use a personal access token so the outreach message comes from a real team member instead of a bot

#### Responding and closing outreach issues

- Answer any questions or acknowledge feedback in the outreach issues
- Close outreach issues after 2 month period with a closing message encouraging the contributor to reopen the issue and reach out if they would like support

### Potential iterations

- Reduce the manual review step with automation by checking candidates against role criteria or list of candidates to exclude
- Thank users who contribute after the outreach campaign in their respective issues which might give opportunity for them to share why they came back

## Recognition for contributors

### Appreciation for highlighted contributions

From time to time, a wider community member will submit a particularly outstanding contribution. Any GitLab team member or the wider community can follow the process to [nominate them as a Notable Contributor](https://contributors.gitlab.com/docs/notable-contributors).

### Top Annual Contributors

In order to recognize regular contributors, the list of top contributors for each calendar year will be published in the [Top Annual Contributors page](https://about.gitlab.com/community/top-annual-contributors/). There will be three categories of top contributors:

- SuperStar: more than 75 MRs merged
- Star: between 11 and 75 MRs merged
- Enthusiast: between 5 and 10 MRs merged

Customized GitLab merchandise will be created for these contributors and will be available on Printfection. For GitLab team members, you can follow the steps below to get the awards to the wider community members.

1. Login to Printfection using the credentials in 1Password.
1. Under `Campaigns`, go to `Giveaways` and create a new `GIVEAWAY CAMPAIGN` (you may need to [create a new `Kit`](/handbook/marketing/brand-experience/merchandise-handling/) under the `Merchandise` tab if you want to include more than one item).
1. Add the item/kit to the campaign.
1. Generate Giveaway links for each contributors.
1. Include the Giveaway link in the individual email to the Top Annual Contributors.

## Contributor lifecycle segments

In an effort to understand, support, and empower the GitLab code contributor community, we have come up with the following lifecycle segments.

These lifecycle segments are assigned on an individual user level.

| Contributor Experience level | MRs merged |
| ------ | ------ |
| Level 0 | 0 MRs |
| Level 1 | 1 - 3 MRs |
| Level 2 | 4 - 25 MRs |
| Level 3 | 26 - 75 MRs |
| Level 4 | 75+ MRs |

| Contributor Status | MRs merged | Timeframe |
| ------ | ------ | ------ |
| Casual contributor | < 10 MRs | Last 6 months |
| Regular contributor | 10+ MRs | Last 6 months |
| Leading contributor | 20+ MRs | last 6 months |
| [Core](https://about.gitlab.com/community/core-team/) | Election based | All time |

Segmenting our contributor community will allow us to understand better how contributors "move" across this funnel and how we can better support them through their journey.

The goal is to increase code contributors across all segments (except the inactive ones), by identifying ways to support and reward our contributors.

## Contributor metrics

Note: this is currently a working list of all locations where we can currently gather contributor metrics. It is not *yet* the final set of metrics we will be using to monitor the success of the contributor program with.

### Tableau dashboards

Internally, GitLab uses [Tableau](/handbook/enterprise-data/platform/tableau/) for tracking down the performance of various KPIs. Below you can find a list of community-related dashboards.

| Dashboard | Description |
| --- | --- |
| [Wider Community Dashboard](https://10az.online.tableau.com/#/site/gitlab/views/WiderCommunityPIsPart1/WiderCommunityPIsDashboardPart1) | Metrics associated to contributors (people) and organizations |
| [MRARR Dashboard](https://10az.online.tableau.com/#/site/gitlab/views/MRARRDashboard_17055242209630/MRARRDashboard) | Metrics associated to contributing organizations who are also a customer of GitLab |

### GitLab.com

You can also directly query data from `Merge Requests` pages for projects (e.g. CE, EE, Omnibus, Shell, etc.) on gitlab.com and apply appropriate filters for milestone, labels, etc. Some of the examples are listed in the metrics table below.

### Number of Contributors

In the past we often mentioned 2,000+ contributors in the GitLab community (GitLab team members + wider community) as you can see in [this example](https://about.gitlab.com/blog/2018/08/13/join-the-gitlab-community/). However, this only included contributors to CE and EE projects based on the old [https://contributors.gitlab.com](https://web.archive.org/web/20190619012814/https://contributors.gitlab.com/) page.

If you include other GitLab projects, the total number of contributors is much larger.

- Total code contributors: includes GitLab team members and wider community contributors (since 2015)
- Wider community code contributors: includes wider community contributors only (since 2015)
- These figures count contributors who have opened at least one merge request, regardless of whether the merge request has been merged, closed or is still open.

- The number of wider community code contributors with a successful contributions (whose Merge Requests have been merged), can be found by looking at the Wider Community Dashboard.
- See [our top misused terms page](/handbook/communication/top-misused-terms/) for a refresher on the definition of wider community members.

When people ask about the number of contributors at GitLab, it's best to clarify if they're asking about total code contributors or wider community code contributors. In most cases, people tend to be more interested in the wider community number.

It's also important to mention that there are other ways the community contributes to GitLab other than code, as listed in our [Contribute to GitLab guide](https://about.gitlab.com/community/contribute/). Contributions like Translations, Evangelism, support on our Forum, and opened issues are not included in the metrics above.

### Monitored projects

We monitor and recognize contributions across a variety of projects on the [`gitlab-org` group](https://gitlab.com/groups/gitlab-org), not only [the GitLab project](https://gitlab.com/gitlab-org/gitlab).

As a general rule, a project will be set up for monitoring wider community contributions if it uses the `gitlab-org` group milestones and the `Community contribution` label.

See the exhaustive list of [monitored `gitlab-org` group projects](https://gitlab.com/Bitergia/c/gitlab/sources/blob/master/projects.json).

Are you interested in contributing to GitLab? Check out the available [contribution opportunities here](https://about.gitlab.com/community/contribute/).
