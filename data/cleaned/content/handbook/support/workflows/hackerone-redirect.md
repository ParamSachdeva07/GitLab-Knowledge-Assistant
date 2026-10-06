---
title: Redirecting bug bounty / vulnerability report disputes to HackerOne (reply template)
description: "When a requester contacts Support about a HackerOne bug bounty report, route them back to HackerOne; includes a copy/paste reply template."
category: Zendesk
---

When a requester contacts Support about a vulnerability report that is being handled in GitLab's bug bounty program (HackerOne) (for example: triage disagreements, reward disputes, or mediation requests), route the requester back to the HackerOne report thread rather than attempting a secondary review via Support.

## Reply template

```text
Hi <Person's Name>,

Thank you for reaching out and for your commitment to responsible disclosure. We appreciate security researchers like yourself who contribute to GitLab's bug bounties.

GitLab manages all vulnerability reports through our HackerOne bug bounty program, which is the appropriate channel for report submissions, triage decisions, and any disputes regarding those decisions.

If you filed a report through HackerOne at https://hackerone.com/gitlab then HackerOne will reply there. If you believe a triage decision was made in error, we encourage you to continue the conversation directly on your HackerOne report.

The HackerOne platform provides a mechanism to request mediation if you and the triage team are unable to reach an agreement.

Unfortunately, we are unable to provide secondary reviews or override triage decisions through our support channels, as this would bypass the structured process that ensures fair and consistent handling of all submissions.

We value your contribution and encourage you to continue working with us through HackerOne.
```

## Notes

- Avoid pasting sensitive report details into the Support ticket.
- If the ticket is not actually about a HackerOne / bug bounty submission, use the normal Support workflow instead.
