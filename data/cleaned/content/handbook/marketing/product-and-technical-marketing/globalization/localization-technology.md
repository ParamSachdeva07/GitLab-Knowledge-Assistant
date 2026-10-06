---
title: "Localization Engineering and Technology Management at GitLab"
description: "Comprehensive overview of GitLab's localization engineering processes, technology ecosystem, workflows, and AI-powered translation infrastructure enabling global content delivery."
---

This page covers GitLab's localization engineering processes and the technology stack that delivers GitLab's product, documentation, and marketing content in multiple languages.

## Mission and vision

[Localization technology at GitLab - mission and vision](https://gitlab.com/gitlab-com/localization/localization-team/-/issues/453)

## Localization technology stack - Overview

The Globalization team manages a sophisticated technology ecosystem designed to automate and enhance translation workflows across GitLab's global content. Our technology stack consists of purpose-built custom solutions, commercial Language Technology Platforms (LTPs), and emerging AI-powered services that collectively enable localization of GitLab's product UI, marketing content, and product documentation. The Globalization team owns this infrastructure and drives its direction and priorities. Engineering work is delivered by a localization engineer embedded in the [Digital Experience (DEX)](/handbook/marketing/digital-experience/) team.

## What we localize

1. **Product documentation** (docs.gitlab.com): localized through an internationalization layer and connected tooling, including the Argo orchestration platform, Phrase TMS, and AI-powered translation systems. For full architecture details, see [GitLab Product Documentation Localization](/handbook/marketing/product-and-technical-marketing/globalization/tech-docs-localization/).
2. **Marketing website** (about.gitlab.com): continuous localization across 6 languages.
3. **Product UI**: community-driven translation through [Crowdin](https://docs.gitlab.com/development/i18n/), using [GitLab <-> Crowdin sync](https://gitlab.com/gitlab-org/frontend/crowdin-translation-sync/-/blob/main/README.md) integration, supported by [GitLab String Search](https://gitlab.com/gitlab-com/localization/gitlab-string-search) and [Crowdin Automation](https://gitlab.com/gitlab-com/localization/crowdin-automation).

## Localization technology stack - Components

See more details and visuals in the [Localization management technology stack at GitLab](https://gitlab.com/gitlab-com/localization/localization-team/-/issues/452) issue.

### AI-powered translation

- [Tech Docs AI-powered translation](https://gitlab.com/gitlab-com/localization/tech-docs-ai-powered-translation) - Google Cloud Vertex AI with LLMs processing GitLab product documentation, using advanced NLP, chained prompt systems, multiple glossaries and style guide injection, and file transformations and validations
- [GitLab Duo Agent Translation Platform](https://gitlab.com/gitlab-com/localization/gitlab-duo-agent-translation-platform) project with configurations and specifications for the custom [GitLab Translation Agent](https://gitlab.com/explore/ai-catalog/agents/532/)
- [CI Translation Components](https://gitlab.com/gitlab-com/localization/ci-translation-components) - GitLab CI components for translation workflows, providing reusable jobs to detect source content changes and trigger translation agents from CI/CD pipelines
- Emerging AI tools - standalone projects in Claude in the early stages of prototype

### Content management system integrations

- [Decap CMS integration](https://gitlab.com/groups/gitlab-com/localization/-/epics/83) - Marketing website content workflow automation through GitLab repositories
- Legacy integrations: [Contentful](https://gitlab.com/groups/gitlab-com/localization/-/epics/27)

### Integrations with Language Technology Platforms

- [Phrase TMS integration](https://gitlab.com/groups/gitlab-com/localization/-/epics/95) - for automated product documentation translation via Argos Multilingual, with AI enhancement capabilities
- [Crowdin integration](/handbook/business-technology/tech-stack/#crowdincom) - for community-driven product UI translation
- [TranslationOS integration](https://gitlab.com/groups/gitlab-com/localization/-/epics/92) - for semi-automated translation workflow for marketing content, via Translated

### Orchestration platform

[Argo](https://gitlab.com/groups/gitlab-com/localization/-/epics/35) - Localization Request Management system serving as the central orchestration hub, consisting of the following specialized services:

- Argo web client (UI) - Argo web UI used by localization program managers, stakeholders and vendors
- Argo web services - backend/API orchestration engine  
- Argo-Phrase integration - service for GitLab product docs localization workflow
- Argo-TOS integration - service for marketing localization workflow
- Argo-GitLab integration - service handling webhooks
- Argo GitLab agent - service for preprocessing GitLab product docs markdown files
- Database & reporting - business analytics and tracking, available within Argo UI

### GitLab integration services

- [Argo GitLab Integration](https://gitlab.com/gitlab-com/localization/argo-gitlab-integration) - [GitLab Translation Service](/handbook/engineering/architecture/design-documents/gitlab_translation_service/) that bridges GitLab projects with translation management systems through webhook automation and Translation MR delivery
- [Argo GitLab Agent](https://gitlab.com/gitlab-com/localization/argo-gitlab-agent) - specialized service for GitLab markdown preprocessing and other content processing tasks

### Supporting tools and services

- [GitLab String Search](https://gitlab.com/gitlab-com/localization/gitlab-string-search) - web interface for searching GitLab's translatable source code strings. The website is used by wider community translators on Crowdin. For details, see this [implementation epic](https://gitlab.com/gitlab-com/localization/localization-team/-/issues/342)
- [Crowdin Automation](https://gitlab.com/gitlab-com/localization/crowdin-automation) - automation scripts for adding context to strings on Crowdin, tracking translator contributions, analyzing comments in Crowdin
- [Kalcium Quickterm](https://gitlab.com/groups/gitlab-com/localization/-/epics/51) - terminology management system

## Vendor engineering partnerships

- [Spartan Software](https://gitlab.com/groups/gitlab-com/localization/-/work_items/60): Argo orchestration platform development and maintenance.
- [Argos Multilingual](https://gitlab.com/groups/gitlab-com/localization/-/work_items/60): AI translation pipelines and projects, linguistic services, translation management system configuration, and Crowdin engineering.

## Central content repository

All localization workflows converge through GitLab as the single source of truth for content management and translations. This GitLab-centric approach ensures:

- Version control for all source and translated content
- Unified delivery mechanism through Translation MRs
- Consistent quality gates and approval workflows
- Integrated CI/CD pipelines for content publishing

## Review workflow

Merge request reviews for localization infrastructure align with the GitLab [Code Review Guidelines](https://docs.gitlab.com/development/code_review/).

Infrastructure and [Translation MRs](https://gitlab.com/gitlab-com/localization/argo-gitlab-integration/-/blob/main/doc/en-US/merge_requests.md?ref_type=heads#translation-mr) are reviewed by the localization engineer in the [Digital Experience (DEX)](/handbook/marketing/digital-experience/) team, with other DEX engineers reviewing as needed. Translation MRs are created by [@gitlab-argo-bot](https://gitlab.com/gitlab-argo-bot) when translations are complete in Argo for the Marketing website and GitLab product documentation.

Localization engineering also helps review MRs authored in Decap CMS by the Localization Content Managers who own and maintain the [Blog](https://about.gitlab.com/blog/) in multiple languages. Blog update MRs from Decap are typically content-only changes that help with deployment agility and can use lightweight review processes. Content Managers may request a review from the localization engineer or another DEX engineer for complex changes, code, or troubleshooting.

## Communication channels

- `#localization-engineering`: localization engineering working channel
- `#localization-alerts`: automated failure reports for fork sync pipelines and Translation MR notifications
- `#spartan-software`: direct communication with Spartan Software engineering team
- `#argos_multilingual`: direct communication with Argos Multilingual engineering team
