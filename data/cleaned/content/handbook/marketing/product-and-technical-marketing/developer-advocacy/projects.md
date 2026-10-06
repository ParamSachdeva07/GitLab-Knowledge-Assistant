---
description: "How Developer Advocacy organizes and maintains demo environments, tutorials, research, and automation projects."
title: "Projects"
---

## Introduction

We maintain our projects in the public [gitlab-da group](https://gitlab.com/gitlab-da). This group has access to an Ultimate subscription.

The group organizes use cases, demo environments, workshops, tutorials, maintained projects, playground research, and more learning resources.

## Organisation Structure

All projects are organized in sub-groups on the top level. No projects are allowed on the top-level namespace `gitlab.com/gitlab-da`.

| Group        | DRI | Description  |
|--------------|-----|--------------|
| [demo-environments](https://gitlab.com/gitlab-da) | all | Team maintained long-term demo environments |
| [conferences](https://gitlab.com/gitlab-da/conferences) | all / @fjdiaz | Group for public demos for team members at [conferences, events, meetups, etc.](/handbook/marketing/product-and-technical-marketing/developer-advocacy/events/#event-booth-training)  |
| [playground](https://gitlab.com/gitlab-da/playground) | all | Test projects, simple demo cases, code snippets, etc. without support. Please move them into the corresponding use-cases or demo-environment groups when linking from a blog post. |
| [use-cases](https://gitlab.com/gitlab-da/use-cases) | all | Use cases for specific topics for product demos, talks, thought leadership, research |
| [projects](https://gitlab.com/gitlab-da/projects) | all | Production projects maintained by the team. For blog projects and demos, use the specific `use-cases` groups. |
| [tutorials](https://gitlab.com/gitlab-da/tutorials) | all | Tutorials and workshops. |

### Access

Access is limited to [team members in the `gitlab-da` group](https://gitlab.com/groups/gitlab-da/-/group_members). Adding/removing members [requires an issue](https://gitlab.com/gitlab-com/marketing/developer-relations/developer-advocacy/developer-advocacy-meta/-/issues) to document the change.

Allowed exceptions are workshop sub-groups that invite external users into their workshop projects temporarily. All temporarily added users [**must** use a membership expiration date of 7 days](https://docs.gitlab.com/ee/user/project/members/#add-users-to-a-project).

### Add a new project or group

1. Define the scope of your project, and add it into one of the top-level groups.
1. When unsure, create the project in the [playground](https://gitlab.com/gitlab-da/playground) group first, and transfer it to its production location later in the project settings.

**Do not create new top-level groups without first proposing the change in an issue/MR.**

#### README

Always add a `README.md` file that explains the purpose of the project/group (copy the text into `Settings > General > Description`), and links all resources (issues, direction pages, blog posts, etc.). GitLab supports [Group READMEs](https://docs.gitlab.com/ee/user/group/manage#add-group-readme) next to project READMEs.

Optional but recommended: Add a project/group avatar image that illustrates the topic. Refer to Brand's [guidance on sourcing creative assets](/handbook/marketing/brand-experience/brand-creative/#sourcing-creative-assets) when selecting an image. Tip: You can [resize images](/handbook/tools-and-tips/#resizing-images).

Also apply other best practices such as `.gitignore`, `AGENTS.md` and CI/CD configuration when applicable by default.

#### Group: Demo environments

Long-term maintained demo environments, with different audiences and DRIs noted in their description.
If necessary, add a handbook page or `demo.md` file explaining the demo setup, and help other team members spin up the demo environment, too.

#### Group: Use Cases

1. Blog posts or thought leadership research usually describe a use case or specific topic. Review the existing [use-cases](https://gitlab.com/gitlab-da/use-cases), add a new project or sub-group.
1. If your use case is new, create a new subgroup, add a description, and update the handbook organization structure. Add yourself as DRI to the table.

#### Group: Tutorials and Workshops

[Tutorials](https://gitlab.com/gitlab-da/tutorials) provide helpful content to learn specific topics and have a DRI assigned to maintain the projects. Tutorials are referenced in blog posts, webinars, etc.

When unsure where to start, create a new tutorial sub group first, and later decide to migrate the content to a workshop for example.

#### Group: Projects

The [projects](https://gitlab.com/gitlab-da/projects) group contains all projects that are used in production. They require extended documentation in the team handbook, since the team depends on the functionality for workflows and efficiency. We also maintain microsites that are served with GitLab Pages and custom domains.

### Remove a project/group

Our demo projects are referenced in blog posts and other public content. Archiving these projects is recommended to signal their deprecation to users, including a README note if possible.

## Project Resources

Some projects require access to Kubernetes clusters, self-managed CI/CD Runners, cloud VMs, domains, etc. The team has access to Google Cloud or AWS cloud resources that allow hosting these types of external infrastructure dependencies for GitLab.com SaaS demos. Learn more in the [Cloud Resources handbook](/handbook/marketing/product-and-technical-marketing/developer-advocacy/tools-and-platforms/cloud-resources).

### Best Practices

1. Document the project setup in its README file (or a in a `docs/` structure in the Git repository).
1. Always add [security scanning](https://docs.gitlab.com/ee/user/application_security/) as default, unless it competes with the demo cases.
1. A GitLab app requires OAuth setup from an account. Use a group shared account (for example, `demo-tanuki`) so everyone can maintain and update the app.

### Development Environments

See [Development Environments for Developer Advocates](/handbook/marketing/product-and-technical-marketing/developer-advocacy/dev-environments/).

## Product Adoption Initiatives

### LinkedIn Lives in Collaboration with the Social team

GitLab hosts a monthly LinkedIn Live broadcast, generally on the fourth Thursday of every month, to highlight our monthly release, and share product updates and thought leadership. Each broadcast features GitLab team members and special guests to discuss the latest in AI-powered software development. This is a collaborative project between [Developer Advocacy](/handbook/marketing/product-and-technical-marketing/developer-advocacy/) and the [Social Media](/handbook/marketing/corporate-communications/social-marketing/) teams.

Episodes generally run for 30 minutes and feature 4-5 panelists and a moderator to discuss a predetermined topic or product update. In certain instances, the conversations are pre-recorded.

| Episode Title                                                                 | Views   | Month   |
|-------------------------------------------------------------------------------|---------|---------|
| [GitLab 16.11](https://www.linkedin.com/events/7191139444916146176/) | 5.6K    | 2024/04 |
| [GitLab 17.0](https://www.linkedin.com/feed/update/urn:li:activity:7198692684436250626) | 6.8K    | 2024/05 |
| [GitLab 17 Release event recap](https://www.linkedin.com/video/live/urn:li:ugcPost:7212131667262492673/) | 7.3K    | 2024/06 |
| [Harnessing AI: GitLab’s Insights & Innovations](https://www.linkedin.com/events/7219699059933020163) | 6.3K    | 2024/07 |

#### Information for Panelists

**Before the Broadcast/Recording**

- You will be added to a temporary Slack channel with the social media team and other panelists to discuss the agenda, logistics, and promotion.
- You will be asked to be available for a 30-minute walkthrough before the recording/broadcast to do a tech check, walk through the talking points, and meet the other panelists.
- You will be added as a speaker to the LinkedIn event page so your network is notified that you will be going live on LinkedIn.
- Please help us promote the event by sharing any LinkedIn posts promoting the event with your network.

**During the Broadcast/Recording**

- Please confirm you have a strong wifi signal and are in a well-lit area that is free from distractions.
  - Ideally, use a virtual background.
- If you have GitLab swag, please wear it!
- Use a headset as your microphone.

**After the Broadcast**

- Please engage with people who commented on the broadcast.
- Please re-share the event video with your network.

## Archived Projects

### Community newsletter

- Goal: Share developer-focused content, keep community members informed about upcoming events, and promote contributions within the community. The target audience for this newsletter is aspiring and existing GitLab contributors in our community. This newsletter will not be used to drive or generate leads.
- Duration: 2022-2024
- [Organization epic](https://gitlab.com/groups/gitlab-com/-/work_items/1821)
- Maintainer: @sugaroverflow
- Archive:
  - [FY23 Newsletter Epic.](https://gitlab.com/groups/gitlab-com/-/epics/1915)
  - All other past newsletter issues can be found using the [label `Da-Type-Content::newsletter`](https://gitlab.com/gitlab-com/marketing/developer-relations/developer-advocacy/developer-advocacy-meta/-/issues/?sort=updated_desc&state=closed&label_name%5B%5D=DA-Type-Content::newsletter&first_page_size=20) and searching for closed issues.
  - [Newsletter issue PDFs (internal)](https://drive.google.com/drive/folders/1w086j7mTDRCUEtINm2AVivkxfctMQT2J)

### GitLab Duo Coffee Chat

Live learning session with AI-powered workflows throughout the DevSecOps lifecycle, with the help of GitLab Duo. We discuss, explore, research, learn, debug, create product feedback and feature ideas, and discover new features and workflows. Learn more in the [FY25 Developer Relations epic](https://gitlab.com/groups/gitlab-com/marketing/developer-relations/-/epics/475) (internal).

Goal: The coffee chats help our customers learn how to use GitLab Duo and adopt best practices – by example, making mistakes, trying different routes, and achieving better results and DevSecOps efficiency.

Maintainer: [Michael Friedrich, @dnsmichi](https://gitlab.com/dnsmichi)

- [YouTube playlist](https://www.youtube.com/playlist?list=PL05JrBw4t0Kp5uj_JgQiSvHw1jQu0mSVZ)
- [GitLab group with projects](https://gitlab.com/gitlab-da/use-cases/ai/gitlab-duo-coffee-chat)
- [GitLab Duo](https://about.gitlab.com/gitlab-duo-agent-platform/)
- [Talk: Efficient DevSecOps Workflows with a little help from AI](https://docs.google.com/presentation/d/e/2PACX-1vQAS87EMBRc4FPtBs_pVMSYs-Pna6ZxV7KF9-z6iGzhNrtr8XD2cnm5nN4jT75U52sbtvfSo23nnkTI/pub?start=false&loop=false&delayms=3000&slide=id.g28d14e7db45_0_3) - [content epic](https://gitlab.com/groups/gitlab-com/marketing/developer-relations/-/epics/402)
- [Organization issue](https://gitlab.com/gitlab-com/marketing/developer-relations/developer-advocacy/developer-advocacy-meta/-/issues/375)
- [Slide templates and resources](https://docs.google.com/presentation/d/1FBOxe43l4qY8KastAWjblphOLiktNtPjHgFNmNYf0Uw/edit#slide=id.g2a6734f20af_0_0) for recording video editing.

The recordings are also linked from the [GitLab Duo Use Cases documentation](https://docs.gitlab.com/ee/user/gitlab_duo/use_cases.html).

#### Process

1. Define the scope of the session (for example, 30 minutes writing an application, or exploring a new programming language like COBOL). Duo Challenges require staying in the IDE or GitLab UI context only.
1. Invite guests to collaborate (optional)
1. Start the Zoom recording, give a short introduction about the goal of the session. When alone, you can also use OBS to record the session.
1. Start the session, ask Duo Chat how to get started, follow-up with Code Suggestions, etc.
1. When finished/stopping because time, breath and provide a recap summary of what we learned today.
1. Export the video.
1. Take a screenshot from the session (or IDE) that highlights the learning. Add the screenshot to the [slide placeholder](https://docs.google.com/presentation/d/1FBOxe43l4qY8KastAWjblphOLiktNtPjHgFNmNYf0Uw/edit#slide=id.g2b429ab8253_0_23), edit the text with the session details, and again create a slides screenshot. This will serve as a video introduction in Premiere Pro.

Video editing in Adobe Premiere Pro:

1. Create a new project in Adobe Premiere Pro.
1. Import the recording and intro/outro image assets.
1. Drag the video into a new sequence.
1. Add the intro screenshot into the first 3-5 seconds. Right-click > Scale to fit frame size.
1. Use the razor icon to cut the video after the intro sequence. Select the first part and delete the sequence.
1. Add an ending screenshot to the last 3-5 seconds. Right-click > Scale to fit the frame size.
1. Use the razor icon to cut the video before the ending sequence, and remove any silence parts. Select the last part and delete the sequence.
1. Export the raw video: `File > Export > Media`.

Video upload:

1. Log into [GitLab Unfiltered account on YouTube](https://www.youtube.com/@GitLabUnfiltered/) and upload the video file.
1. Edit the title of the session: `GitLab Duo Coffee Chat: Challenge - Explain and Refactor COBOL programs` or similar.
1. Edit the video description with 2-3 sentences of what to expect. Add all docs/blog URLs as `Resources` entry.
1. Open the video preview in a new window and scroll over the sections. Note the timestamps, and write down a TOC into the video description. The table of content helps viewers to navigate quickly.
1. Add to `Playlist` - `GitLab Duo Coffee Chat`
1. Add tags: `gitlab`, `gitlab-duo`, `ai`, `development`, etc.
1. Publish the video.

Distribution

1. Add the video to the [GitLab Use Case documentation](https://docs.gitlab.com/ee/user/gitlab_duo/use_cases.html), Highspot, blog posts, social posts, etc.

### CI/CD Components Catalog

Collaborate with product and engineering to help seed the CI/CD component catalog through CI/CD template migration for [GitLab-maintained components](https://gitlab.com/components). Help maintain and review contributions from community competition and hackathons. Repurpose the learnings into content and story-telling ([content epic](https://gitlab.com/groups/gitlab-com/marketing/developer-relations/-/epics/399)). Learn more in the [FY25 Developer Relations epic](https://gitlab.com/groups/gitlab-com/marketing/developer-relations/-/epics/466) (internal).

This initiative is part of the [CI Adoption WG](/handbook/company/working-groups/customer-use-case-adoption/) and contributions by Developer Relations ([epic](https://gitlab.com/groups/gitlab-com/marketing/developer-relations/-/epics/317)).

Goal: Help customers with CI/CD components for DevSecOps Efficiency. Learn best practices and share them in blog posts, tutorials, workshops.

Maintainers: [Michael Friedrich, @dnsmichi](https://about.gitlab.com/company/team/#dnsmichi), [Itzik Gan Baruch, @iganbaruch](https://about.gitlab.com/company/team/#iganbaruch)

### Developer Relations Bot

Maintainer: TBD. Ask [Michael Friedrich](https://gitlab.com/dnsmichi) meanwhile.

This bot aims to automate the team tasks such as:

- Create [release evangelism](/handbook/marketing/product-and-technical-marketing/developer-advocacy/social-media/#release-evangelism) issues for team members.
- Triage issues following the [Developer Advocacy workflows](/handbook/marketing/product-and-technical-marketing/developer-advocacy/workflow/).
- Generate an issue letter (created, closed, open CFPs) on every Monday.

Project: [DevRel Bot](https://gitlab.com/gitlab-da/projects/devrel-bot)
