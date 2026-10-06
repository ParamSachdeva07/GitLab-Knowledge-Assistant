---
title: Translation MR Review Workflow
description: Defines the assignee and reviewer roles, draft status, and review process for translation merge requests across Tech Docs and Marketing Site workflows.
---

This page defines the assignee and reviewer roles, draft status, and review process for translation merge requests.

For general guidance, refer to the [GitLab Code Review Guidelines](https://docs.gitlab.com/development/code_review/) and the [Engineering Workflow: Code Review](/handbook/engineering/workflow/code-review/).

## Tech Docs (Upstream)

Translation MRs for Tech Docs go through two rounds of review: one on `gitlab-com` (the fork) and another on `gitlab-org` (upstream). On the forks, the process is flexible with no strict approval rules. Upstream, the following structure applies.

### Assignee

1. **Fixes conflicts.** If you can't fix the conflicts, pass over to someone else. By looking at the commit history of each file in `main`, you can see what target changes are causing the conflict. Those could be caused by:
   - Us changing translations on production
   - TW making a change to shortcodes, linting, etc.
2. **Fixes any pipeline issues.**
3. **Rebases if needed.**
4. **Checks the review app** (Duo is great at producing a list of URLs; [example](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/229940#note_3218543601)).
5. **Removes the MR from Draft mode.** This will trigger the first review by GitLab Duo.
6. **Handles GitLab Duo review feedback.** If the Duo review brought up any translation errors that require our [language content maintainers](https://gitlab.com/gitlab-com/localization/maintainers) to review, the assignee pings and adds them as a reviewer. Note: They will not be able to approve the MR after adding a commit.
7. **Hands off for review** to a [Tech Docs maintainer](https://gitlab.com/gitlab-com/localization/maintainers/tech-docs).

### Reviewer

1. Reviews changes.
2. Verifies build pipeline.
3. Merges on approval.

## Marketing Site

For the marketing site, approval rules like "Prevent approvals by users who add commits" are not enforced in `gitlab-com`, so reviewers can add commits and still approve/merge. Translation MRs now open in Draft mode by default.

### Assignee

1. **Fixes conflicts.** By looking at the commit history of each file in `main`, you can see what target changes are causing the conflict. Those could be caused by:
   - Us changing translations on production
   - DEX team making updates, like changing schemas or adding new components ([example](https://gitlab.com/gitlab-com/marketing/digital-experience/about-gitlab-com/-/merge_requests/4027/diffs))
2. **Fixes any lint issues breaking the pipeline.**
3. **Rebases if needed.**
4. **Checks the review app** for all impacted pages to QA visually.
5. **Removes the MR from Draft mode.** This will trigger the first review by GitLab Duo.
6. **Addresses GitLab Duo's review comments** directly where possible.
7. **Hands off for review.** The idea here is that if the MR is handed over for review, it is ready to merge. It can be merged once a single approval is acquired.

### Reviewer

1. Reviews translations.
2. Applies changes to translations when needed.
3. Merges on approval. If reviewers don't merge, the assignee merges ASAP.
