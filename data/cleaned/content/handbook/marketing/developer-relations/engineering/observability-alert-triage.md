---
title: "Observability alert triage"
description: "How to investigate and close a contributor platform Observability alert"
---

When the [GitLab Observability](https://gitlab.com/groups/gitlab-org/developer-relations/contributor-success/-/observability/setup) alert system fires,
an issue is automatically created in the [contributors-gitlab-com tracker](https://gitlab.com/gitlab-org/developer-relations/contributor-success/contributors-gitlab-com/-/issues)
and the team is pinged through the service desk. Follow these steps to follow up on those alerts.

## 1. Open the alert issue

The issue title looks like:

```text
[FIRING:1] <rule-id> (Error log entry ... error error)
```

Open the issue. The description contains:

- `ruleSource`: a direct link to the alert rule in the observability UI.
- `related_logs`: a pre-filtered log explorer link scoped to the time the alert fired.
- `description`: the threshold that was crossed (for example, "observed value: 1, threshold: 0").

> It is known that both the format and available info is not ideal to quickly see the reason **why** there is an alert.
> This is a known issue tracked in [the `gitlab_o11y` project](https://gitlab.com/gitlab-org/embody-team/experimental-observability/gitlab_o11y/-/work_items/48).

## 2. Open the logs

Use the `related_logs` link from the issue description. It opens the
[group logs explorer](https://gitlab.com/groups/gitlab-org/developer-relations/contributor-success/-/observability/logs/logs-explorer)
with the correct filters already applied.

## 3. Read the error

Expand the log entries. Identify:

- The error message and stack trace.
- Whether the error is isolated (one or two occurrences) or sustained.
- Whether it points to a known cause (for example, a transient DB connection drop, an expired token,
  a downstream API failure).

## 4. Document your finding in the issue

Add a comment to the alert issue. Keep it short:

- What the error was.
- Whether it appears transient or recurring.
- Any relevant log excerpt.

Example from [contributors-gitlab-com#552](https://gitlab.com/gitlab-org/developer-relations/contributor-success/contributors-gitlab-com/-/issues/552):

> cause was what looks like a temporary db connection issue
>
> ```text
> PG::ConnectionBad: connection to server at "127.0.0.1", port 5432 failed:
> FATAL: Cloud SQL IAM service account authentication failed
> ```
>
> didn't recur, so closing

{{< alert type="warning" >}}
**Alert issues are confidential (created through the service desk)**

Keep all sensitive details, including raw log output, stack traces, and internal infrastructure data, inside this confidential issue. Do not copy them verbatim into public issues or MRs. See [Act on the finding](#5-act-on-the-finding) for sanitization rules.
{{< /alert >}}

## 5. Act on the finding

Choose one of the following paths based on what you found.

### Transient, no action needed

The error did not recur and has no impact. Close the alert issue with a short comment
explaining the cause.

### Needs a fix, low urgency

Create a public issue to track the fix. Include only a sanitized description:

- Describe the class of error (for example, "IAM authentication failure") without raw log output,
  user identifiers, or stack traces that could leak internal infrastructure details.
- Link the public issue back to the confidential alert issue for traceability.
- Apply the standard labels: `~"Contributor Success"` and the appropriate `~type::` and
  `~workflow::` labels.
- Link the public issue to the
  [observability umbrella work item #308](https://gitlab.com/gitlab-org/developer-relations/contributor-success/contributors-gitlab-com/-/work_items/308)
  if it is related to a recurring pattern.
- Close the alert issue, referencing the new public issue.

### Needs a fix, high urgency

Open an MR directly. Apply the same sanitization rules to the MR description: no raw log
output or sensitive data. Link the MR back to the confidential alert issue in a comment on
the alert issue, not in the MR description itself.

### Unclear or needs a second opinion

Leave the alert issue open, add your findings as a comment, and ping someone from the team.

## Data sanitization rules

Alert issues are confidential. Any downstream artifact (public issue, MR, work item comment)
must not contain:

- Raw log output with stack traces or internal hostnames.
- User identifiers, email addresses, or account IDs from log entries.
- Internal service account names or IAM role names.
- Connection strings or environment-specific configuration values.

Describe the problem in terms of behavior and impact, not raw infrastructure detail.
