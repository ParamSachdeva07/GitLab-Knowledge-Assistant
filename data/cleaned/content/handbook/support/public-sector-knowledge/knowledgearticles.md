---
title: Public Sector Knowledge Base
description: GitLab Public Sector Knowledge Base
---

The Knowledge Base is a searchable repository of Solutions to customer problems, designed to help users quickly find answers to their questions without having to contact support.

![Knowledge Management](/images/support/assets/usg_kb.jpg)

**Knowledge base articles can be found here**

- [US Public Sector support knowledge base](https://federal-support.gitlab.com/hc/en-us/sections/29015014994068-Knowledge-Base)
- [Global support knowledge base](https://support.gitlab.com/hc/en-us/sections/15215649512604-Knowledge-Base)

 **Benefits**:

- Deflects ticket creation.
- Resolves user problems faster.
- Creates consistent, standard answers.
- Creates an environment of trust.
- Gives Support more time to focus on harder issues or improvements.

## Principles

- **Turn it into a habit.** If the issue is worth solving, it is worth saving.
  - Start a knowledge article every time you solve a problem for a customer, a team member or yourself.

- **Accelerate knowledge capture.** Our tools and processes should enhance the speed at which we add knowledge to the Knowledge Base.
  - Capture Knowledge in the moment when the context is clearest and we are able to access customer feedback.
  - Provide feedback as soon as possible if you find a better way to do something.

- **Capture customer context.** Prioritize capturing the right knowledge, in the context of the customer.
  - Focus on documenting the errors and issue as described by the customer for improved findability from other users.
  - Include clear steps and context when documenting solutions. When in doubt, ask, [would Josh Darnit be able to do it?](https://www.youtube.com/watch?v=cDA3_5982h8)

- **Always be iterating.** The Knowledge Base is as much for us as for our customers. We review and update knowledge as we use and reuse it.
  - Reuse is Review: We improve the quality of our knowledge by always iterating.

## How Knowledge Articles differ from GitLab docs

The Knowledge Base and our product documentation are both key elements of GitLab's digital support experience that serve different needs.
See [examples and learn more here](../knowledge-base/docs-vs-kb/)

### Docs

Docs answer: "How does this work?"

- Offers comprehensive information about Product features, architecture and Usage.
- Provides an overview of the current version of our products.
- Often more technical and detailed
- Updated less frequently (New Feature releases)
- Primarily created for engineers, advanced users, Product details

### Knowledge Articles

Knowledge Articles answer: "How do I fix this?"

- Solves problems encountered while using our products.
- Provides solutions to common issues and questions
- Typically task oriented and includes videos, screenshots
- Updated frequently based on new issues, new workarounds, new troubleshooting and feedback
- Primarily created for customer self-service

## Why you should create a knowledge article

Knowledge articles help users to do tasks, get answers to questions and fix issues they may encounter while using our products.

Did you know that Knowledge can be **INTERNAL** or **EXTERNAL**?!  Knowledge articles arent just for Customers. They are for Internal users as well. Within a knowledge base we offer internal only knowledge that assists our internal team members.

We use *types* of knowledge to efficiently provide the information for our end users. This includes:

- How-To
- Break/Fix
- FAQ (Question and answer)
- Troubleshooting
- Process

## When to create a knowledge article

In short, you should create an article when someone will benefit from the information.

Some questions to consider:

- Will it help customers find information quickly?
- Does it answer a common question / issue?
- Does it document a repeatable way to do something?
- Would this information help a customer get what they need without Support intervention?
- Is this information that may need frequent updates?
- Is this a new issue (with or without a solution) that may cause an influx of support tickets?

## What can be / should be part of a Knowledge Article?

- Overview
- Workarounds, Root Cause, Issue
- Videos (Link to video)
- Screenshots (Be careful to not add screenshots of Personal Identifiable information)
- References (be careful of internal links if the article is external)

### What Training is Available for Knowledge Articles in ZenDesk?

A list of available training can be found in [Knowledge Base Training Resources](../knowledge-base/knowledge-base-training).

## Implementation

We now use a [Sync Repo](https://gitlab.com/gitlab-com/support/articles) to create, modify, and  publish knowledge base articles.

Want to see how to create a knowledge article in the Sync repo? Check out our [LevelUp video](https://levelup.edcast.com/insights/creating-an-knowledge-article-in-the-sync-repo-mp)

**Here's what you need to know**

- We are still aligned with Zendesk. THe sync repo will 'sync' knowledge articles with Zendesk to present to customers.
- The Create article button in Zendesk will still be present, however it will direct you to the sync repo (a note will be displayed).
- The knowledge articles will still be present on the knowledge base of our Support Portal.
- Support Engineers will still be able to link knowledge articles and/or documentation to a support ticket by using the search feature.

**What's NOT changing**

- Zendesk remains our tool for support tickets
- Customers see no difference
- Internal article visibility stays the same (look for the 🔒 icon for internal-only content)
- How you view articles is unchanged

- **TL;DR**: Same reading experience, new writing process.

## How to create a knowledge article in the Sync Repo  

The following process is creating a knowledge article using a WebIDE and Knowledge article template. A [video](https://drive.google.com/file/d/1oxcPg4IA3yRDAshab31yO8Yf24XqmvY8/view?usp=sharing) has been created to Guide you as a visual.

1. Go to the Sync Repo Project [Articles](https://gitlab.com/gitlab-com/support/articles)
2. Open a WebIDE (use the period on your keyboard to open the WebIDE)
3. Drop down the arrow next to the Knowledge Articles (Right side) and choose the Templates folder.
4. Drop the arrow next to the Templates folder and choose one (Breakfix, FAQ, How-To, Process).
5. COPY the entire File Information
6. Go to one of the SECTIONS under Knowledge Articles (Administrative, CI_CD Pipeline, Errors, how To, Kubernetes, Licensing and subscription, Migrations, Other articles, performance, Security, Upgrades, Troubleshooting) . **Note**: If you do not see a section that needs to be added we have a way to do that!  See the Section details here: https://handbook.gitlab.com/handbook/security/customer-support-operations/zendesk/knowledge-center/sections/#current-sections-in-use
7. Right Click on the Name and choose “FILE”
8. Name the File (Your Article Title) and add .md after the title: Example - TitleOfYourKnowledgeArticle.md
9. Paste the template details you copied into the right side panel.
10. Enter the body (details) of the knowledge articles (remove or add information as needed).
11. Save, Commit and Create the Merge Request (MR)

Update the Top Metadata Fields FIRST:

- **Title**: Change the TITLE (to the title of your knowledge article)
- **Previous Title** (should match the Title)
- **Category**- Knowledge Articles (Leave as is)
- **Section** - Add the section that the article should be in (Administrative, CI/CD Pipeline, Errors, How To, Kubernetes, Licensing and Subscription, Migrations, Other articles, Performance, Security, Upgrades, Troubleshooting).  
- **Author** (will be you)
- **Tags** - Add version specific details.  Example '17.10'
- **Labels** - Specifics to reporting, Product detials. Example 'Runner', 'Duo'
- **Instances** - the article will be shown in both Global and Gov knowledgebase. If the article is to only go to Gov, remove the Global. If the article is to only go to Global remove the Gov line.
- **Public** - is set to TRUE. This indicates the article is PUBLIC VISIBLE. If the article is to be INTERNAL ONLY set to FALSE.
- **convert_markdown** - If the article is in HTML and you convert it to markdown, you must change `convert_markdown` to `true`. If the article is going to stay in HTML format, leave the `convert_markdown` to `false`.

**Note**: The Workflow will then be started - MR Created, Reviewers must review,  article will be approved and added to the Sync Repo and then visible on our Knowledge base.

## Other ways to Create Knowledge Articles

**Option 1- External Template Request**

1. Go to the [Folder and choose a template](https://drive.google.com/drive/folders/1hpHAB51x49bRS1tfUqxiQ56UnlITtFHR)
2. Create the article using the template and Save the document.
3. Use the Knowledge Slack Channel [#spt_knowledge-base](https://gitlab.enterprise.slack.com/archives/C07QDCG4AGH) to request the article to be created. Please tag {{< member-by-name "Kirsty Allen" >}} .
4. Your Article will be created in the sync repo and assigned to a Reviewer & then Published.
5. Roles and Permissions remain. The same "Reviewers" today will have access to Approve an MR to publish an article.

**Option 2.-Template Support Team Meta**

1. Use the **template** under [Support Team Meta](https://gitlab.com/gitlab-com/support/support-team-meta/-/issues) . The Template is named `knowledge-base-article-request`. Make sure to tag {{< member-by-name "Kirsty Allen" >}}
2. Your Article will be created in the sync repo and assigned to a Reviewer & then Published. You will be notified of Publication.

**Option 3. -Template in Articles Repo**

1. Use the **template** under [Articles](https://gitlab.com/gitlab-com/support/articles/-/work_items). The Template is named `knowledge-base-article-request`. Make sure to tag {{< member-by-name "Kirsty Allen" >}}
2. Your Article will be created in the sync repo and assigned to a Reviewer & then Published. You will be notified of Publication.

**Option 4-Create through Slack**

To create a NEW issue to Knowledge use the following Command in Slack

- /gitlab gitlab-com/support/articles issue new  

To UPDATE an existing issue in Slack, use this command in Slack

- /gitlab gitlab-com/support/articles issue comment  Work item number (shift + Enter) Add the comment

### Roles and Permissions

There are three roles: Support Engineer, Knowledge Champions and Knowledge Admins.

- **Knowledge Contributors**: Create, update and use KB articles in tickets.
- **Technical Reviewers**: Will review an article for technical accuracy before it's published.
- **Knowledge Champions (Coaches)**: Create, Modify, Review, publish, as well as Mentor Junior Members (knowledge), identify opportunities for knowledge.
- **Knowledge Admins**:  Ensure processes are followed, assist with archive, restore.

Please see the  [Knowledge Roles Permissions, and Responsibilities](/handbook/support/knowledge-base/knowledge-roles/) page for more information.

### Getting Help

Questions can be asked in the dedicated [#spt_knowledge-base](https://gitlab.enterprise.slack.com/archives/C07QDCG4AGH) Slack channel.

For any issues with permissions, please use the knowledge dedicated Slack channel:  [#spt_knowledge-base](https://gitlab.enterprise.slack.com/archives/C07QDCG4AGH) - and  tag  or open an [Issue](https://gitlab.com/gitlab-com/support/support-team-meta) and tag {{< member-by-name "Kirsty Allen" >}}.
