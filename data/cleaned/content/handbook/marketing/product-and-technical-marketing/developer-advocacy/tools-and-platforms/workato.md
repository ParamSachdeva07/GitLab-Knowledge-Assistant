---
linkTitle: "Workato"
description: "Workato automations used by Developer Advocacy and how to request workflow changes."
title: "Developer Advocacy tools: Workato"
---

Developer Advocacy team uses [Workato](/handbook/marketing/marketing-operations/workato/) to automate workflows between tools and platforms.

## Workato maintainers

Updated or new workflows need to be requested from the [Enterprise Technology team maintaining Workato](https://internal.gitlab.com/handbook/eta/administrative/organizational-structure/enterprise-applications-integrations/workato-playbook/).

## Current workflows

| Type | Workflow | Description | Involved Tools |
| --- | --- | --- | --- |
| Blog-to-Forum | Post new Blogs to the GitLab forum | GitLab blog post is posted as [a new forum topic](#gitlab-blog-forum-bot) | GitLab Blog RSS feed, Discourse |
| Forum-to-Slack | New forum topics in the GitLab Duo category | Reads Discourse forum RSS feed `https://forum.gitlab.com/c/gitlab-duo.rss` and posts to `#gitlab-duo-forum-posts` channel. | Discourse forum, Slack |
| Blog-to-Slack | New blog posts - GitLab | Reads GitLab blog RSS feed and posts to `#developer-advocacy-updates` channel. | GitLab Blog, Slack |
| Blog-to-Slack | New blog posts - GitHub | Reads GitHub blog RSS feed and posts to `#developer-advocacy-updates` and competitive Slack channels. | GitHub Blog, Slack |
| Blog-to-Slack | New blog posts - CNCF | Reads CNCF blog RSS feed and posts to `#developer-advocacy-updates` channel. | CNCF Blog, Slack |

### gitlab-blog Forum Bot

The [`gitlab-blog`](https://forum.gitlab.com/u/gitlab-blog/summary) user is used to automatically post new [GitLab blog posts](https://about.gitlab.com/blog/) as a new topic to the [Community](https://forum.gitlab.com/c/community/39) category.  This process is controlled through Workato which reads the blog RSS feed at `https://about.gitlab.com/atom.xml` and posts a new topic using the admin API key and `gitlab-blog` user for each new entry there.

The `gitlab-blog` credentials and admin API key are stored in the 1Password Marketing vault. Admins can directly edit the user in Discourse without login.

## History

Zapier was migrated to Workato in 2025, content in this [internal issue](https://gitlab.com/gitlab-com/business-technology/enterprise-apps/integrations/integrations-work/-/work_items/829).
