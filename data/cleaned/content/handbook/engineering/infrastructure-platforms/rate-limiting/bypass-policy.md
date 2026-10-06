---
title: "Bypass Policy"
description: "This policy relates to the rate limits for GitLab.com, for Self-Managed and Dedicated please reach out to your administrator."
---

## Bypass Policy for GitLab.com

[Published rate limits](https://docs.gitlab.com/user/gitlab_com/#rate-limits-on-gitlabcom) apply to all customers and users with no exceptions. Rate limiting bypasses are not granted for any reason.

The reason for this strict policy is we want to help every customer as much as possible when they run into problems, but on GitLab.com, we have to prioritize the reliability and stability of the entire instance to protect all customers and users. Allowing even one customer to bypass rate limits creates a high risk situation where we have opened an avenue for a high severity production incident (such as GitLab.com being unavailable to all users) to occur. This is why bypasses are not granted under any circumstances.

If you are hitting rate limits, we recommend investigating the following mitigations:

- Identify why rate limits have started to be hit. ([Troubleshooting Guide](/handbook/engineering/infrastructure-platforms/rate-limiting/troubleshooting/))
- Stagger execution of automated pipelines.
- Implement exponential backoff and retry for failed authentication attempts.
- Review [GitLab's rate limit documentation](https://docs.gitlab.com/user/gitlab_com/#rate-limits-on-gitlabcom) to understand the specific limits in place.
  - Backoff strategies can be added based on the specific limits being hit.
