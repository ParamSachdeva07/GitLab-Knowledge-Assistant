---
title: On-Call Processes and Policies - Tier 1
---

Tier 1 Rotations refer to on-call rotations that respond to pages from automated systems.

## Active Tier 1 Rotations

### SRE EOC GitLab.com

- Rotation Leader: Sarah Walker
- Coverage: 24x7
- Schedule: [schedule](https://app.incident.io/gitlab/on-call/schedules/01K5YWAGZ7YCQGAG7ATQ9XQWHW)
- Slack: [#eoc-general](https://gitlab.enterprise.slack.com/archives/C07G9CP5XRR)

#### Responsibilities

In addition to incident management responsibilities, the EOC also is responsible for time sensitive interrupt work required to support the production environment that is not owned by another team. This includes:

1. Reviewing and handling certain change requests (CRs). This includes:
    1. Reviewing CRs to ensure they do not conflict with any ongoing incidents or investigations
    1. Executing the CR directly if the author does not have the required permissions to make the change themselves (such as admin-level changes)
    1. Support during C1 CRs, such as database upgrades, that may occur on weekends
1. Handling incident related teleport access requests
1. Approving an exception for running ChatOps commands when they fail their safety checks
1. Investigating and fixing buggy/flapping alerts
1. Removing alerts that are no longer relevant
1. Collecting production information when requested
1. Responding to `@sre-oncall` Slack mentions
1. Assisting Release Managers with deployment problems

### GitLab Dedicated Platform

- Rotation Leader: Florbela Viegas
- Coverage: 24x7
- Schedule: [schedule](https://gitlab.pagerduty.com/schedules#PE57MNA)

### GitLab Dedicated PubSec

- Rotation Leader: Florbela Viegas
- Coverage: 24x7
- Schedule: [schedule](https://gitlab.pagerduty.com/schedules#PRP4EC1)

### Incident Managers (aka IMOC)

- Rotation Leader: Devin Sylva
- Coverage: 24x7
- Schedule: [schedule](https://app.incident.io/gitlab/on-call/schedules/01K77XZFD7X7E3W8T6GDVMKAFF)

## Tier-1 for Service teams (STEOC)

Service teams are paged for alerts for their owned service reducing MTTR and ensuring code ownership.

The teams are paged for alerts explicitly configured to page and carry the `Service` label that the team owns. EOC is part of the escalation chain as the first fallback for missed pages.
 
### Responsibilities 

Service teams on Tier-1 rotations are responsible for:

1. Responding to pages for alerts configured to page their owned service
2. Investigating and resolving incidents related to their owned services
3. Escalating to EOC or other Tier 2 and Tier 1 teams when the issue is outside the scope of their service or requires additional support
4. Updating alert configurations to reduce noise and improve signal quality
5. Documenting findings and resolutions in the post incident review
6. Participating in [post-incident reviews](/handbook/engineering/infrastructure-platforms/incident-review/) & creating corrective actions to improve processes and prevent recurrence

Service teams on an active Tier-1 rotation: 

#### Runners Platform

- Rotation Leader: Kam Kyrala
- Coverage: 24x5
- Schedule: [Runners Platform on-call schedule](https://app.incident.io/gitlab/on-call/schedules/01K7HNBCW9EN2MMS4SHAJ5B2WF)

#### Further details

- Incident manager rotation is staffed by certain [team members in the Engineering Group](/handbook/engineering/infrastructure-platforms/incident-management/incident-manager-onboarding/).
- More information regarding the Incident Manager role, including shift schedules, responsibilities can be found in the [Incident Manager on-boarding page](/handbook/engineering/infrastructure-platforms/incident-management/incident-manager-onboarding/).
