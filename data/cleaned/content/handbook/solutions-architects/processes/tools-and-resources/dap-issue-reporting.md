---
title: DAP Rapid — Field Issue Reporting
description: How Solutions Architects report customer-blocking DAP issues to engineering
---

## Overview

**DAP Rapid** is the Duo Agent Platform program for handling Sev1 and Sev2 customer-blocking issues with clear SLOs, tracking, and escalation paths across 14 contributing engineering groups.

As a Solutions Architect, you can:

- **File bugs directly** in GitLab issues — no Zendesk ticket required
- **Propose severity labels** (engineering makes the final call)
- **Escalate critical issues** through RFH or incident.io

Use this process whenever you discover bugs or customer-blocking issues during DAP trials, POVs, or customer deployments.

## When to report

Report issues that block or significantly impair a customer's use of the Duo Agent Platform.

| Severity | Description | Examples |
|----------|-------------|----------|
| **Sev1 — Critical** | System down, major functionality broken, customer blocked | Agent cannot start, tool execution fails for all users, data loss |
| **Sev2 — Major** | Significant functionality impaired, workaround available | Specific tool fails intermittently, degraded performance, incorrect output with known workaround |

For Sev3/Sev4 issues (minor bugs, cosmetic problems), file a standard bug issue with the labels below — the DAP Rapid SLOs do not apply.

## How to report

Choose the channel based on severity and urgency:

```text
Customer-blocking issue discovered
    │
    ├─ Sev1 (system down, no workaround)
    │   └─ Raise incident through incident.io OR RFH
    │       → Escalation required if not resolved in 12h
    │
    ├─ Sev2 (impaired, workaround exists)
    │   └─ File bug in gitlab-org/gitlab OR raise RFH
    │       → Escalation if not resolved in 24h
    │
    └─ Sev3/4 (minor)
        └─ File bug in gitlab-org/gitlab with labels
```

### Channel 1: Direct bug filing (most common)

File an issue in [`gitlab-org/gitlab`](https://gitlab.com/gitlab-org/gitlab/-/issues/new) with the required labels listed below. This is the fastest path for field-discovered bugs.

### Channel 2: Request for Help (RFH)

Use [GitLab Request for Help](https://gitlab.com/gitlab-com/request-for-help/) when you need engineering to investigate a support-adjacent issue, or when the root cause is unclear. Follow the RFH README and apply the correct closure labels.

### Channel 3: incident.io (critical production incidents)

For Sev1 production incidents on GitLab.com, [declare an incident using incident.io](/handbook/engineering/infrastructure-platforms/incident-management/#reporting-an-incident) and ensure the "Affects Duo Agentic Platform (DAP)" field is set to YES.

## Required labels

When filing a bug issue in `gitlab-org/gitlab`, apply:

| Label | Purpose |
|-------|---------|
| `~"Duo Agent Platform GA Fast Follow"` | Routes the issue into DAP tracking |
| `~"type::bug"` | Bug identifier |
| `~"severity::1"` through `~"severity::4"` | Proposed severity (engineering makes final call) |
| `~"group::[team name]"` | Owning AI engineering group |

## Resolution SLOs by deployment type

These are internal targets (SLOs), not customer-facing SLAs. The primary goal is to **unblock customers within 24 hours** for all Sev1 and Sev2 issues.

| Deployment | Severity | Target unblock time | Fix/patch deployment |
|------------|----------|---------------------|----------------------|
| **GitLab.com (SaaS)** | Sev1 | 30 min – 12 hours | Immediate (deploy within ~6h of MR merge on business days) |
| | Sev2 | 4 – 24 hours | Target: 3 business days |
| **Self-Managed** | Sev1 | 30 min – 12 hours | Next [patch release](/handbook/engineering/releases/patch-releases/#patch-release-overview) (~2 weeks, 2nd/4th Wednesday) |
| | Sev2 | 4 – 24 hours | Next patch release |
| **Dedicated** | Sev1 | 30 min – 12 hours | Next patch release with [backporting](https://docs.gitlab.com/policy/maintenance/#backporting-to-older-releases) (2–4 weeks) |
| | Sev2 | 4 – 24 hours | Next patch release with backporting |

**Notes:**

- Configuration or setup issues should be unblocked within the target time without a code change.
- Code fixes requiring deployment follow the timelines above.
- For Self-Managed and Dedicated, communicate fix timeline to the customer within 12h (Sev1) or 24h (Sev2).
- Dedicated customers run one version behind; backporting is limited to the previous two minor versions.

## Tracking dashboards

| Tracker | Link | Owned by |
|---------|------|----------|
| Zendesk DAP issues | [Zendesk dashboard](https://gitlab.zendesk.com/explore/studio#/dashboards/65C06156A78CBD32904C3E92205D82AC4A6B49D51D5D149FF5D324C97ADAD8F6) | Support |
| incident.io DAP issues | [incident.io dashboard](https://app.incident.io/gitlab/incidents) | Engineering & Support |
| Bug tracker (GitLab issues) | [DAP Bug Tracker wiki](https://gitlab.com/groups/gitlab-org/ai-powered/-/wikis/home/Program-Duo-Agent-Platform/Program-Bug-Tracker) | AI EM & PM |
| RFH tracker | [DAP RFH Tracker wiki](https://gitlab.com/groups/gitlab-org/ai-powered/-/wikis/home/Program-Duo-Agent-Platform/Program-Bug-Tracker/DAP-RFH-Tracker) | Support Engineering |
| Reliability (Grafana) | [DWS log-based dashboard](https://dashboards.gitlab.net/d/3d9c7954-2669-4782-9206-b714c8a589fa/dws-log-based-dashboard) | Engineering |
| Latency (Snowflake) | [Language server metrics](https://app.snowflake.com/ys68254/gitlab/#/language-server-metrics-dd7LWVgnL) | Engineering |
| Tool call error rate | [Duo Workflow Service dashboard](https://dashboards.gitlab.net/d/duo-workflow-svc-main/duo-workflow-svc3a-overview) | Engineering |

## Slack channel

Use [`#f_duo-agent-platform`](https://gitlab.slack.com/archives/f_duo-agent-platform) as the consolidated channel for all DAP inquiries — questions, issue triage, and status updates.

Do **not** use `#building-on-duo-agent-platform`, `#usage-billing-help`, `#dap-customer-feedback`, or individual AI group channels for issue reporting. Redirect to `#f_duo-agent-platform`.

## Related resources

- [Zendesk Internal Request Form](https://gitlab-internal.zendesk.com/hc/en-us/requests/new?ticket_form_id=22783651259548) — Customer Support Internal Requests
- [RFH process](https://gitlab.com/gitlab-com/request-for-help/) — Request for Help from engineering
- [AI POV scope and acceptance](/handbook/solutions-architects/playbooks/pov/ai/) — running DAP customer trials
- [GitLab Support SLAs](https://support.gitlab.com/hc/en-us/articles/11626483177756-GitLab-Support) — official customer-facing SLAs
- [Incident escalation process](/handbook/engineering/infrastructure-platforms/incident-management/tier2-escalations/) — PagerDuty / incident.io escalation
