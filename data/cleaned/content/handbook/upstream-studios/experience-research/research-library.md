---
title: GitLab Research Library
description: Your central hub for UX research insights, findings, and knowledge discovery.
---

The GitLab Research Library is an intelligent research repository that helps team members discover, organize, and leverage UX research insights across GitLab's product areas.

The Library is located at [uxr-library.com](https://uxr-library.com) (internal link). Below is a brief overview of what the site contains and what it can do.

The repository for the site is [here](https://gitlab.com/gitlab-com/ux/ux-research-library/ux-research-library), and a readme for contributing code to the library is [here](https://gitlab.com/gitlab-com/ux/ux-research-library/ux-research-library/-/blob/production/CONTRIBUTE.md?ref_type=heads) .

## Navigation

### Overview

The Library homepage displays quick-action shortcuts, the 6 most recent research entries, featured research themes, and top investment areas. This landing page also shows high-level stats: total research entries, recent additions, contributors, and unique tags.

### Search & Browse

The main way to find research. Enter keywords to search across titles, descriptions, findings, and recommendations. Use the filter panel to narrow by investment area, research method, job performer, participant tier, business size, platform, and date range. Results show taxonomy badges, descriptions, and key metadata.

### Research Agent

An AI-powered conversational interface. Ask natural-language questions about your research library — for example, *"What do we know about CI/CD usability?"* or *"What pain points do enterprise users mention?"* The agent synthesizes findings across multiple internal UX research entries and can also surface related customer verbatim from Dovetail, Zendesk tickets, and Gong call summaries. Responses include citations linking back to the source material. Conversations auto-save and can be resumed from the history dropdown.

**Note:** All customer verbatim surfaced through the Research Agent is sourced from consented research sessions (and whatever we class zendesk and gong as) and anonymised prior to display — if you have questions about the underlying data or its provenance, reach out to the Experience Research Team.

### Insights Explorer

Displays AI-generated clusters of atomic insights (findings, recommendations, research questions) grouped by theme across all research entries. Useful for spotting recurring patterns and cross-study themes without reading individual entries.

- **Grid view**: Clusters grouped by category with counts and breakdowns
- **All view**: Flat list of all clusters, sortable by size, recency, or theme
- **Search view**: Filter clusters by keyword to find relevant themes quickly

Each cluster shows how many findings, recommendations, and questions it contains, plus counts of related Dovetail quotes, Zendesk tickets, and Gong calls.

### Hypothesis Validator

Tests a research hypothesis against existing evidence from four sources: insights from internal research reports, Dovetail customer quotes, Gong calls and Zendesk support tickets.

Enter a hypothesis (10–500 characters), and the tool returns:

- A **validation score** (0–100) based on the ratio of supporting to contradicting evidence
- An **evidence breakdown** showing supporting, contradicting, and neutral items by source
- **Thematic groupings** of the most relevant evidence
- An **AI-generated summary** with synthesis, confidence assessment, and identified gaps
- Validation history so you can return to previous runs

### Add Research

Add new research entries to the library, either by importing from a URL or filling in the form manually. In general, members of Experience Research, Product Design and Product Management will be the main authors and are responsible for adding completed research to the library. 

Other team members with valid, high-quality research reports are encouraged to add their research as well. Reach out to the #gitlab-research-library Slack channel if you would like assistance determining if your research should be added or not (and if you need help adding it). 

**Import from URL** (recommended): Paste a GitLab work item or Google Drive document link. AI reads the content and automatically extracts research questions, findings, recommendations, tags, product taxonomy, GitLab tier, platform, business size, and relevant verticals. Review the pre-filled form before saving.

**Note:** You will need to enter a valid GitLab [Personal Access Token (PAT)](https://docs.gitlab.com/user/profile/personal_access_tokens/) in order to import directly from GitLab. You will also need to authenticate with Google Drive before import from Drive will work. 

**Supported sources**: GitLab work items, Google Docs, Google Sheets, Google Slides.

**Manual entry**: Fill in the form directly if you don't have a URL to import from.

### Analytics

A research library health dashboard. Shows:

- **Overview stats**: Total entries, recent additions, contributors, unique tags, findings, recommendations, and questions
- **Insight stats**: Dovetail quotes, Zendesk ticket links, Gong call summaries, and cluster counts
- **Monthly activity chart**: Research added over the past 6 months
- **Research by investment area**: Coverage breakdown across product areas
- **Top contributors, stage groups, and tags**: Ranked lists with relative usage bars

## Authentication

Sign in with your GitLab Okta account. All pages require authentication.

*Questions or feedback? Reach out to the UX Research team via #gitlab_research_library on Slack, comment on the [feedback issue](https://gitlab.com/gitlab-org/ux-research/-/work_items/3698)*
