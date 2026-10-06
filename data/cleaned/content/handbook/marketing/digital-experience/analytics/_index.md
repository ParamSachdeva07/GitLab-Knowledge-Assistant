---
title: "Analytics"
description: >-
  What the Digital Experience team owns for analytics on the marketing site,
  what stays with other teams, and how to route requests.
---

This page describes how the Digital Experience team supports analytics on the marketing site. It covers what we own, what stays with other teams, and where to send requests.

## What we own

We are co-DRI for Google Analytics (GA4) and Google Tag Manager (GTM) on the marketing site, alongside the Marketing Analytics team.

**Properties we own analytics for:**

- [about.gitlab.com](https://gitlab.com/gitlab-com/marketing/digital-experience/about-gitlab-com)
- [GitLab Blog](https://gitlab.com/gitlab-com/marketing/digital-experience/gitlab-blog)
- [Navigation](https://gitlab.com/gitlab-com/marketing/digital-experience/navigation)
- [Slippers Design System](https://gitlab.com/gitlab-com/marketing/digital-experience/slippers-ui)
- [Buyer Experience (deprecated)](https://gitlab.com/gitlab-com/marketing/digital-experience/buyer-experience)

**What we handle for these properties:**

- GTM container changes for marketing-site requests
- GA4 event tagging and `dataLayer` implementation on the marketing site
- OneTrust quarterly cookie scans across marketing-site domains
- Pixel and third-party script implementation in GTM, after Legal vetting

## What stays with other teams

**Marketing Analytics** owns the measurement framework, dashboards, attribution modeling, and Snowflake data exports. They define what the data means and how it is reported. See the [Marketing Analytics GA4 handbook page](/handbook/enterprise-data/marketing-analytics/google-analytics-4/) for their scope.

**Marketing Operations** owns Marketo and Adobe Measure (Bizible). These feed into the analytics pipeline but are configured outside Digital Experience.

**Other GitLab properties** — `api.gitlab.com`, `customers.gitlab.com`, `docs.gitlab.com`, `university.gitlab.com`, and `ir.gitlab.com` — are owned by their respective product or engineering teams. Analytics requests for these properties should go to the property owner first. Digital Experience may consult on implementation when invited, but does not take ownership by default.

## Request routing

For analytics requests on the marketing site (about.gitlab.com, the Blog, Navigation, Slippers):

1. [Open an issue in the Digital Experience project](https://gitlab.com/gitlab-com/marketing/digital-experience/about-gitlab-com/-/issues/new) using the standard request template.
2. Include the property, the event or data you need, and any deadline.

For requests on other GitLab properties (`api.gitlab.com`, `docs.gitlab.com`, etc.), contact the team that owns that property first. They can loop in Digital Experience if implementation support is needed.

For questions about dashboards, attribution, or marketing metrics, reach out to the [Marketing Analytics team](/handbook/enterprise-data/marketing-analytics/).

## See also

- [Digital Experience team handbook](/handbook/marketing/digital-experience/)
- [GTM Configuration Guide](https://internal.gitlab.com/handbook/marketing/digital-experience/google-tag-manager-configuration-guide/) (internal) — how to configure GTM tags, triggers, and variables
- [OneTrust](/handbook/marketing/digital-experience/onetrust/) — cookie consent and compliance
- [Data Dictionary](/handbook/marketing/digital-experience/engineering/data-dictionary/) — `data-ga-name` and `data-ga-location` attribute conventions for the marketing site
- [Marketing Analytics GA4 handbook](/handbook/enterprise-data/marketing-analytics/google-analytics-4/) — measurement framework and reporting
- [GTM handbook](/handbook/enterprise-data/marketing-analytics/google-tag-manager/) — supported third-party platforms and the co-DRI list
