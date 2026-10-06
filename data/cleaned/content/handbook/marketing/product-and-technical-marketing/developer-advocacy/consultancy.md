---
linkTitle: "Consulting"
title: "Consultancy workflows for Developer Advocates"
description: "Learn about the Developer Advocacy team's consultancy workflows and requests."
---

Teams and divisions can request consultancy in areas where [Developer Advocates are Subject Matter Experts (SME)](/handbook/marketing/product-and-technical-marketing/developer-advocacy/#team-members-and-focus-areas), or can help with their experience or connection network.

## Organization

Consultancy requests are labelled using the [`DA-Consulting::` scoped labels](/handbook/marketing/product-and-technical-marketing/developer-advocacy/workflow/#consulting-labels), with the [`DA-Type::Consulting` label as pre-filtered list](https://gitlab.com/gitlab-com/marketing/developer-relations/developer-advocacy/developer-advocacy-meta/-/issues/?sort=updated_desc&state=opened&label_name%5B%5D=DA-Type%3A%3AConsulting&first_page_size=20). Issues are grouped in a [yearly consultancy epic](https://gitlab.com/groups/gitlab-com/marketing/developer-relations/-/work_items?sort=created_date&state=opened&label_name%5B%5D=DA-Type%3A%3AConsulting&type%5B%5D=8&first_page_size=20).

### Request developer advocate consultancy

> **Important**: Verify that the request requires help from the Developer Advocacy team before requesting consultancy. In most cases, the Solution and Demo Architects teams are the first to ask for help.

Developer Advocates and requestors can use the [`consultancy-request` issue template](https://gitlab.com/gitlab-com/marketing/developer-relations/developer-advocacy/developer-advocacy-meta/-/issues/new?issuable_template=consultancy-request).

### Decision matrix

1. [ARR](https://internal.gitlab.com/handbook/sales/annual-recurring-revenue-arr/) (and influenced ARR for [SKUs](https://about.gitlab.com/pricing/))
1. Aligned with business objectives and marketing strategy (for example, a specific Vertical in the quarter).
1. Expertise and resources. If developer advocates cannot deliver on a specific programming language/framework, or do not have the resources to prepare for consultancy, we will deny the request and suggest alternative DRIs on the SA/CSM/Engineering teams.

## Consultancy areas

There is a wide variety of areas and topics that can be requested. It is important for Developer Advocates that requests align with their expertise and resources, and are not too broad, or without success exit criteria. All consultancy requests should be turned into opportunities to repurpose the learnings or created resources into more [content](/handbook/marketing/product-and-technical-marketing/developer-advocacy/content/).

Generally, all product areas, features and technology can be requested. The sections below document a few recent examples of requests and their results.

### GitLab Duo Agent Platform Adoption

Goal: Help customers adopt GitLab Duo Agent Platform.

Developer Advocates are encouraged to help with

- (Live) programming workshops, when fluent and confident in the requested language.
- GitLab UI and IDE setup and troubleshooting.
- Latest product updates and improvements.
- Best practice resources, demos, product tours, and use cases (see [content library](/handbook/marketing/product-and-technical-marketing/developer-advocacy/content/#content-library))
- Support field teams in Slack, [#sme-ai](https://gitlab.enterprise.slack.com/archives/C05GK6M7FBQ)

Cross-functional collaboration for customer workshops is required: [Solution Architects](/handbook/solutions-architects/) lead the [Proof of Value (PoV) workshops for GitLab Duo and AI](/handbook/solutions-architects/playbooks/pov/ai/). They get help building the workshop outline from the [SA Demo Architects](/handbook/solutions-architects/center-of-excellence/demo-architecture/) and [Customer Success Management team](/handbook/customer-experience/). Developer Advocates are encouraged to help with programming workshops, IDE setup and troubleshooting, and generally sharing best practices as a developer with customer's (engineering) teams.

Customer feedback can inspire bug reports, feature proposals, documentation updates, blog tutorials, demo stories and much more. Make sure to always listen and take notes during customer engagements.

Recent customer workshop examples are available in the [pre-filtered Duo Agent Platform consulting issues](https://gitlab.com/gitlab-com/marketing/developer-relations/developer-advocacy/developer-advocacy-meta/-/issues/?sort=updated_desc&state=all&label_name%5B%5D=DA-Type%3A%3AConsulting&search=dap&first_page_size=20) (internal).

{{% details summary="Archived results for Duo Enterprise" %}}

Customer adoption engagement examples are available in the [FY25Q2 OKR KR](https://gitlab.com/gitlab-com/gitlab-OKRs/-/work_items/8073), the [GitLab Duo (AI) Adoption FY25 (DevRel) epic](https://gitlab.com/groups/gitlab-com/marketing/developer-relations/-/epics/475) and [this pre-filtered issue list](https://gitlab.com/gitlab-com/marketing/developer-relations/developer-advocacy/developer-advocacy-meta/-/issues/?sort=updated_desc&state=all&label_name%5B%5D=DA-Type%3A%3AConsulting&search=duo&first_page_size=20).

- Customer workshops for GitLab Duo ([list in the content handbook](/handbook/marketing/product-and-technical-marketing/developer-advocacy/content/#workshops))
  - [GitLab Duo Use Case - Python workshop 2024-07-10](https://gitlab.com/gitlab-da/use-cases/ai/ai-workshops/gitlab-duo-use-case-python-2024-07-10)
  - [Build your own adventure with GitLab Duo - C++ observability tool with embedded hardware sensors](https://gitlab.com/gitlab-da/use-cases/ai/ai-workshops/gitlab-duo-workshop-build-your-own-adventure-cpp-2024-12-05)
- Blog: Best practice tutorials for customers and field teams ([AI/ML blog category](https://about.gitlab.com/blog/categories/ai-ml/)/)
- Documentation
  - Author and maintain the [GitLab Duo Use Case documentation](https://docs.gitlab.com/ee/user/gitlab_duo/use_cases.html) and linked resources:
    - [GitLab Duo Prompts library](https://gitlab.com/gitlab-da/use-cases/ai/ai-workflows/gitlab-duo-prompts)
    - [GitLab Duo Challenges](https://gitlab.com/gitlab-da/use-cases/ai/ai-workflows/gitlab-duo-challenges)
  - [Improve GitLab Duo Onboarding](https://gitlab.com/gitlab-org/gitlab/-/issues/467162)
- Continued [GitLab Duo Coffee Chats](/handbook/marketing/product-and-technical-marketing/developer-advocacy/projects/#gitlab-duo-coffee-chat) helping specific customer workflows (refactoring, code generation prompts, etc.).
- Product/Engineering: Feature proposals and bug reports ([FY25 epic](https://gitlab.com/groups/gitlab-com/marketing/developer-relations/-/epics/475#feature-proposals) (internal)).
  - Add `/fix` slash command for Duo Chat ([issue](https://gitlab.com/gitlab-org/gitlab/-/issues/443366)).

{{% /details %}}

SME DRI: @dnsmichi

### MLOps Adoption

Goal: Enable data scientists and [MLOps](https://about.gitlab.com/direction/modelops/mlops/) engineers to adopt DevSecOps practices and enjoy the benefits of automation, repeatable workflows, standardization, and automatic provisioning of infrastructure.

Recent customer workshop examples are available in [this pre-filtered issue list](https://gitlab.com/gitlab-com/marketing/developer-relations/developer-advocacy/developer-advocacy-meta/-/issues/?sort=updated_desc&state=all&label_name%5B%5D=DA-Type%3A%3AConsulting&search=mlops&first_page_size=20) (internal).

SME DRI: @waarias
