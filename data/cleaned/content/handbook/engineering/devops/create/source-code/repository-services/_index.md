---
title: "Create:Repository Services Team"
description: The permanent Source Code team for the repository side of GitLab, building an access layer on the Gitaly team's primitives.
---

## What we do

Repository Services is the backend team for the repository side of Source Code. One part of the mission is settled: build an access layer on the Gitaly team's primitives that the product and agents can use. The full mission statement is still being defined and will be published here. The team starts with a keep-the-lights-on (KTLO) and support focus.

Current initiatives:

- SSH certificates
- Rate limiting
- Branch Rules (parked, still owned by this team)

## What we expect to own

The split of the Source Code surface between the four teams is still being agreed with the Source Code Triage, Source Code Investigation and Hardening and Modernization teams. The features below are the ones expected to move to Repository Services; the list will be updated once the backlog move is done.

- Repository mirroring (push, pull and bidirectional)
- Git LFS
- Protected branches and Branch Rules (Branch Rules is parked, but stays with this team)
- Push rules
- Code Owners (shared with Create:Code Review)
- Commit and tag signing: GPG, SSH and X.509 or S/MIME signatures, web-based commit signing, and rejecting unsigned commits

## What we do not own

- **The rest of Source Code.** The Source Code Triage and Source Code Investigation teams own the Source Code features outside the list above, until the split is agreed.
- **Systemic security and frontend modernization.** The temporary [Source Code Hardening and Modernization team](/handbook/engineering/devops/create/source-code/hardening-and-modernization/) owns this work and hands the results over to the feature teams.
- **Gitaly itself.** The [Gitaly team](/handbook/engineering/infrastructure-platforms/tenant-scale/gitaly/) owns Gitaly. We build on its primitives.

## Team members

{{< team-by-manager-role role="Manager, Engineering(.*)Create:Repository Services" team="Create:Repository Services" >}}

One EMEA Backend Engineer position is open.

## Stable counterparts

{{< engineering/stable-counterparts manager-role="Manager, Engineering(.*)Create:Repository Services" role="(Product Manager|Product Designer)(.*)Create:Source Code(,|$)|Director of Engineering(.*), Plan$" >}}

Technical writer: Brendan Lynch (shared with the other Source Code teams).

## How we work

- **Planning.** A planning issue is generated monthly in [gitlab-org/create-stage](https://gitlab.com/gitlab-org/create-stage/-/issues) with the title `Repository Services <MILESTONE> Planning`, starting with 19.6. We plan on the boards listed below.
- **Retrospectives.** [async-retrospectives](https://gitlab.com/gitlab-org/async-retrospectives) generates our retrospectives into [gl-retrospectives/create-stage/source-code](https://gitlab.com/gl-retrospectives/create-stage/source-code), shared with the other Source Code teams. A dedicated project may follow.
- **Gitaly sync.** A recurring sync with the Gitaly team, because we build on Gitaly's primitives. How requirements are carried back to Gitaly is still being agreed and will be documented here.
- **Feature category and error budget.** Not assigned yet. Source Code's single feature category, `source_code_management`, stays with Source Code Investigation until it is split. The split, and the error budget that comes with it, are tracked in the [setup issue](https://gitlab.com/gitlab-org/create-stage/-/work_items/13314).

## Boards

All boards filter on the `group::repository services` label.

- [SCM Planning Board - Multiple milestones](https://gitlab.com/groups/gitlab-org/-/boards/7577682?label_name%5B%5D=group%3A%3Arepository%20services)
- [Create:Source Code - scm-backlog](https://gitlab.com/groups/gitlab-org/-/boards/7657028?label_name%5B%5D=group%3A%3Arepository%20services&label_name%5B%5D=scm-backlog)
- [SCM Milestone Planning](https://gitlab.com/groups/gitlab-org/-/boards/7658776?label_name%5B%5D=group%3A%3Arepository%20services)
- [SCM BE Planning Board](https://gitlab.com/groups/gitlab-org/-/boards/7577683?label_name%5B%5D=group%3A%3Arepository%20services&label_name%5B%5D=backend)
- [SCM Next 1-3 Milestones](https://gitlab.com/groups/gitlab-org/-/boards/7153926?label_name%5B%5D=group%3A%3Arepository%20services&label_name%5B%5D=backend&milestone_title=Next%201-3%20releases)
- [SCM UX Planning Board](https://gitlab.com/groups/gitlab-org/-/boards/5092292?label_name%5B%5D=group%3A%3Arepository%20services)
- [Create: Source Code Infradev](https://gitlab.com/gitlab-org/gitlab/-/boards/706619?label_name%5B%5D=group%3A%3Arepository%20services)
- [Work items](https://gitlab.com/groups/gitlab-org/-/work_items?label_name%5B%5D=group%3A%3Arepository%20services&label_name%5B%5D=devops%3A%3Acreate)

## Links

- [Tracking issue](https://gitlab.com/gitlab-org/create-stage/-/work_items/13314) (confidential)
- [Parent epic](https://gitlab.com/groups/gitlab-org/-/work_items/23672)
- [Create:Source Code teams](/handbook/engineering/devops/create/source-code/)
- [Gitaly team](/handbook/engineering/infrastructure-platforms/tenant-scale/gitaly/)
- Slack: `#g_create_repository-services` (not created yet)
