---
title: Globalization
description: Learn more about the Globalization team's vision and processes.
---

## Introduction

The Globalization team collaborates with the Marketing, Sales, Product and Engineering [divisions](/handbook/company/structure/#organizational-structure), as well as external partners (vendors) and the wider community of translators, to enable GitLab's global reach and user experience across key pillars: Marketing (about.gitlab.com), Editorial (blogs), Product, Documentation, and Enablement (support, customer success, etc.).

The team's key initiatives include increasing our non-English blog publishing cadence and performance, localizing the marketing website pages, enabling the localization of docs.gitlab.com, launching the terminology management system, deploying cutting-edge Generative AI and machine translation solutions, expanding into customer-facing programs such as localization of Support content and training & certification materials, and supporting all of the above by the localization technology platform and tooling.

Our ability to support regional teams with localized product documentation, marketing content, and customer success materials directly impacts GitLab's ability to grow in global markets.

## Localization Technology Management

The Globalization team is managing the diverse technology stack consisting of several purpose-built solutions, as well as commercial Language Technology Platforms (LTPs) for managing the localization of GitLab product UI, marketing website and GitLab product documentation:

- [GitLab Translation Agent](https://gitlab.com/explore/ai-catalog/agents/532) is our GitLab Duo Chat powered AI translation assistant that is optimized for GitLab's internal localization workflow. GitLab Translation Agent uses the [GitLab Duo Agent Translation Platform](https://gitlab.com/gitlab-com/localization/gitlab-duo-agent-translation-platform) to produce translations for GitLab marketing content, such as website pages and blogs in German, French, Italian, Japanese, Portuguese (Brazilian), and Spanish. The translation output is reviewed and edited by GitLab's localization Content Managers before publication.
- The [Localization Request Management system](https://gitlab.com/groups/gitlab-com/localization/-/epics/35) and its suite of integrations and microservices, aka Argo
- The [GitLab Translation Service](/handbook/engineering/architecture/design-documents/gitlab_translation_service/) aka [Argo GitLab Integration](https://gitlab.com/gitlab-com/localization/argo-gitlab-integration)
- Argo integrations and automations between LTPs (language technology platforms), such as [TranslationOS](https://gitlab.com/groups/gitlab-com/localization/-/epics/92) and [Phrase TMS](https://gitlab.com/groups/gitlab-com/localization/-/epics/95), and GitLab projects and systems, such as [Decap CMS](https://gitlab.com/groups/gitlab-com/localization/-/epics/83)
- Purpose-built custom AI-powered solutions for machine translation and localization-adjacent tasks for GitLab product documentation. See project [Tech Docs AI-powered translation](https://gitlab.com/gitlab-com/localization/tech-docs-ai-powered-translation)
- Purpose-built custom solutions for context-enhanced localization of GitLab product UI, using [Crowdin](/handbook/business-technology/tech-stack/#crowdincom). See project [GitLab String Search](https://gitlab.com/gitlab-com/localization/gitlab-string-search), epic [Implement and launch the string search context-enhancement solution as Pages website](https://gitlab.com/gitlab-com/localization/localization-team/-/issues/342), project [Crowdin Automation](https://gitlab.com/gitlab-com/localization/crowdin-automation), and project [crowdin-translation-sync](https://gitlab.com/gitlab-org/frontend/crowdin-translation-sync)
- [Argo GitLab Agent](https://gitlab.com/gitlab-com/localization/argo-gitlab-agent), a purpose-built service as a  component of the Argo ecosystem for specialized localization-related tasks, such as file pre- / post-processing, etc.
- Terminology management system - [Kalcium Quickterm](https://gitlab.com/groups/gitlab-com/localization/-/epics/51)

## Localization Program Management

### Contact us

The Globalization team manages general localization-related, language-specific and partner-spacfic Slack channels:

- `#localization`: Central channel for translation and localization questions, requests, and collaboration with the Globalization team.
- `#tech-docs-localization`: Channel for quick communication and interactions between, mainly, the Globalization team and the Technical Writing team.
- `#blog-localization-content`: Channel for communication around our international blogs
- `#translated-team`: For communication with our language services provider, [Translated](https://gitlab.com/groups/gitlab-com/localization/-/epics/11).
- `#spartan-software`: For communication with our technology partner, [Spartan Software](https://gitlab.com/gitlab-com/localization/localization-team/-/issues/41).
- `#oban-international`: For communication with our copywriting and digital marketing agency, [Oban International](https://obaninternational.com/).
- `#crowdin_gitlab`: For communication with our technology provider for product UI text localization, [Crowdin](https://crowdin.com/).
- `#argos_multilingual`: For communication with [Argos Multilingual](https://gitlab.com/gitlab-com/localization/localization-team/-/issues/60), our language services, solutions and technology provider for product and technical documentation.
- `#terminology`: For communication with our terminology consultant, vendors (Translated and Argos Multilingual) and the technology provider of the terminology management system, [Kaleidoscope](https://kaleidoscope.at/en/).

Channels for collaboration between GitLab stakeholders and Globalization team on language-specific initiatives:

- `#japan_localization_gitlab`
- `#french-localization`
- `#german-localization`
- `#italian-localization`
- `#portuguese-brazil-localization`
- `#spanish-localization`

### Labels

#### Localization request status labels

| Label | Purpose |
| ------ | ------------ |
| `L10n-status::triage` | To triage localization requests or initiatives |
| `L10n-status::New Request` | To indicate a new localization request |
| `L10n-status:in progress` | To indicate that a localization request is in progress |
| `L10n-status:Completed` | To indicate that a localization request is completed |
| `L10n-status:LQA` | To indicate that a localization request is under localization quality assurance (LQA) |
| `L10n-status-blocked`| To indicate that the localization request is blocked |
| `L10n:: business owner review` | To indicate that the requesting team/person is reviewing the translations. Also used when an [Internal Reviews](#internal-reviews) is happening |
| `L10n::backlog`| For tracking issues in our backlog |

#### Labels for our main localization pillars

| Label | Purpose |
| ------ | ------------ |
| `L10n-mktg` | for work on marketing localization |
| `L10n-infrastructure`| for work on our localization infrastructure and technology |
| `L10n-training` | related to learning everything about localization at GitLab |
| `L10n-partners` | for tracking work vendor related |
| `L10n-docs`| for tracking work related to the localization of GitLab documentation |
| `L10n-product`| for tracking work related to the localization GitLab product UI |
| `L10n-terminology-mngmnt` | Work related to terminology management processes, terminology management system implementation, glossary work on Crowdin for product translations, etc. |

#### Locale labels

| Label | Purpose |
| ------ | ------------ |
| `fr-FR` | tracking content and localization work in French |
| `de-DE`| tracking content and localization work in German |
| `es-International`| tracking content and localization work in Spanish|
| `ja-JP` | tracking content and localization work in Japanese|
| `pt-BR` | tracking content and localization work in Brazilian Portuguese|
| `it-IT` | tracking content and localization work in Italian|

#### Translation Engine labels

| Label | Purpose |
| ------ | ------------ |
| `translation::gdatp` | Translation MR generated by [GDATP](https://gitlab.com/gitlab-com/localization/gitlab-duo-agent-translation-platform).  |
| `translation::aiqt` | MRs where content came from AI Quick Translator (Claude-based project)  |
| `translation::argo-phrase` | MRs created from the Argo → Phrase TMS → Argos Multilingual pipeline (continuous / vendor-managed flow). |
| `translation::argo-matecat` | MRs created from the Argo → TranslationOS → Matecat pipeline. |
| `translation::inhouse-linguist` | MRs where translation was done manually by GitLab staff linguists or Content Managers, with no machine engine in the loop. |
| `translation::external-vendor` | MRs where translation was delivered manually by a vendor linguist outside Argo automation (one-off requests, direct files, etc.). |

## How to submit translation requests to the Globalization team

**Primary method**
Submit an issue through our [Localization Issue Tracker](https://gitlab.com/gitlab-com/localization/issue-tracker/-/issues/new?issuable_template=localization-request) when your content is ready for localization or review.

Note: While you can contact the Translated or Argos Multilingual team directly via Slack in `#translated-team` or `#argos_multilingual`, we prefer submission through the Issue Tracker.

**Additional support**
For general localization questions:

- Join our `#localization` Slack channel
- Add the L10n-attention label to issues, epics, or merge requests
- Here you can view the status of current localization requests: [Issue Tracker Board](https://gitlab.com/gitlab-com/localization/issue-tracker/-/boards/7726880)

### When to engage with us

We recommend connecting with the Globalization team early in your planning, especially for global initiatives affecting users across all regions that have a specific timeline. While we can't begin translations until content is finalized and approved, early collaboration during planning and design will ensure success.

### Internal reviews

We are managing the internal review process by working with language leads and contractors, so that our in-market GitLab teams can focus on their normal duties. Please note, however, that we may need to engage the internal review team from time to time, as our new teams ramp up and build the context they need to successfully localize our content in a way that aligns to GitLab and local expectations.

Our internal reviewers are volunteer GitLab employees. We completely appreciate that this task is on top of your day job and will continue to respect that. Both translation and reviews are conducted in Translated tooling; processes for review are currently a work in progress.

## Localization of GitLab product documentation site (docs.gitlab.com)

We are working on localizing GitLab product documentation. To learn more, go to the [Localization of GitLab Product Documentation](tech-docs-localization.md) Handbook page, see the [Docs Site Localization project](https://gitlab.com/gitlab-com/localization/docs-site-localization) and follow the [Localization of GitLab Product Documentation epic](https://gitlab.com/groups/gitlab-com/localization/-/epics/14).

## Marketing Localization

GitLab marketing website is being continuously localized and maintained in 6 languages. GitLab's international blog is available in Japanese, French and German, with a dedicated content manager. To learn more, go to the [Marketing Localization](marketing-localization.md) Handbook page.
