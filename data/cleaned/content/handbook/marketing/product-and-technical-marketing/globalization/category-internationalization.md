---
title: "Internationalization (i18n) at GitLab"
description: Technical foundation and community-driven efforts to make GitLab accessible to users worldwide across different languages and regions.
---

## Internationalization (i18n) at GitLab

[The Globalization team owns GitLab's product internationalization category](https://gitlab.com/gitlab-com/Product/-/issues/14118), which transferred from the Import and Integrate group in 2025 (reference: [Product sections, stages, groups, and categories](/handbook/product/categories/)). This brings together the technical infrastructure for i18n with GitLab's broader localization strategy.

### What is internationalization category

Internationalization provides the technical foundation that enables localization. Among other things, it involves separating text from code through externalization, handling pluralization rules across languages, supporting various character encodings, managing date and time formatting and i18n nuances of timeago, adherence to standards around UI text message composition and localizability, and building and maintaining infrastructure for translation management. The Globalization team bridges technical implementation with market needs and translation community requirements.

### Current state

GitLab's internationalization has reached viable maturity. Most user-facing strings are externalized and available for translation through Crowdin. Many languages have substantial translation coverage - see percentage on https://crowdin.com/project/gitlab-ee. However, technical opportunities for impovemnet remain: string externalization that remains incomplete across the codebase, pluralization systems need improvements, and the larger backlog under [Internationalization strategy](https://gitlab.com/groups/gitlab-org/-/epics/2722) needs continuous refinement, that's owned by the Globalization team.

### Evolution of translation management

Previously, translation management required extensive manual intervention. The original process involved waiting for the merge requests to be created, manually triggering pipelines for validation, individually disapproving problematic translations in Crowdin, and manually merging approved translations. This manual workflow could take hours and required deep knowledge of Crowdin's interface and GitLab's validation systems.

Now, our sophisticated [crowdin-translation-sync](https://gitlab.com/gitlab-org/frontend/crowdin-translation-sync) system automates the entire workflow through multiple integrated pipelines. The system handles source uploads to Crowdin, downloads approved translations, runs comprehensive quality assurance, syntax validation and content linting, automatically resolves common translation errors, and creates well-managed merge requests with proper labels and reviewers. What previously required hours of manual work now completes in 3-5 minutes through this automation system, though final review and approval of merge requests still requires manual oversight.

### Opportunities for improvement and investment

- i18n backlog refinement and i18n issue resolution
- Enhancing the translation process with context, including using AI
- Issue management and resolution in Crowdin ('issue' means translator's questions and reported mistranslations)
- Wider community engagement
- Glossary managemenet on Crowdin
- Crowdin automation enhancements and maintenance
- Faster translation updates
- Impprove translation quality
- [Upgrade to Crowdin Enterprise](https://gitlab.com/gitlab-com/localization/localization-team/-/issues/258) in the long term

### Wider community contributions

Wider community can contribute through string externalization, translation work via Crowdin, proofreading, and technical i18n improvements.

- **String externalization**: identify and externalize hardcoded strings using GitLab's internationalization framework
- **Translation**: submit translations and vote on suggestions through Crowdin
- **Proofreading**: review translations before acceptance (we actively recruit proofreaders for all languages)
- **Technical improvements**: contribute to issues labeled "Seeking community contributions"

See [Translate GitLab to your language](https://docs.gitlab.com/development/i18n/) and [Internationalization for GitLab](https://docs.gitlab.com/development/i18n/externalization/).
