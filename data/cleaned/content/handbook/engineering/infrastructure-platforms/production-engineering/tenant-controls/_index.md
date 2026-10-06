---
title: "Tenant Controls Team"
description: "The Tenant Controls team owns application rate limiting on GitLab.com: our mission, ownership, and the boards and labels we track work on."
---

Within Production Engineering, the Tenant Controls team owns application-level rate limiting on
GitLab.com: the framework that defines, counts and observes every application rate limit, and the
migration of the existing implementations onto it. For the limits themselves, see
[Rate Limiting](/handbook/engineering/infrastructure-platforms/rate-limiting/), which is the source
of truth for operators.

## Mission

Our mission is to give GitLab.com a single way to define, configure and observe every application
rate limit, so that limits can be reasoned about during an incident and changed without a deploy.

## Ownership and Responsibilities

The team's scope is set by the
[Unified Rate Limiting Architecture](/handbook/engineering/architecture/design-documents/unified_rate_limiting/)
and delivered as the workstreams listed under [Boards](#boards):

1. **Unified SDK:** [labkit](https://gitlab.com/gitlab-org/labkit) as the shared rate limiting SDK,
   and conformance of callers to it.
1. **Application unification:** routing the existing implementations, `Rack::Attack` and
   `ApplicationRateLimiter`, through that SDK without breaking changes.
1. **Externalized configuration:** moving limit configuration out of the application and the
   database into a config file that labkit loads.
1. **Dynamic rule service:** an external service that returns rules per request, which is what
   makes per-customer and per-tier limits possible.
1. **Tier-aware throttles:** limits that vary by plan rather than applying one number to everyone.
1. **Operational ownership:** the rate limiting framework in production, including its
   observability, dry-run and bypass behavior.

Setting the value of an individual limit is a change-managed operation shared with operators, not
something this team owns unilaterally; see
[Rate Limiting](/handbook/engineering/infrastructure-platforms/rate-limiting/).

## Getting Assistance

- **Slack:** [#g_tenant-controls](https://gitlab.slack.com/archives/C0ATYKN2NTG)
- **Rate limit settings for a user or group:** use the
  [request template](https://gitlab.com/gitlab-com/gl-infra/production-engineering/-/issues/new?issuable_template=request-rate-limiting).
- **Bypass requests:** follow the
  [Rate Limit Bypass Policy](/handbook/engineering/infrastructure-platforms/rate-limiting/bypass-policy/).

## Common Links

|                        |                                                                                                                   |
|------------------------|-------------------------------------------------------------------------------------------------------------------|
| **Workflow**           | [Infrastructure Platforms Project Management](/handbook/engineering/infrastructure-platforms/project-management/) |
| **Program**            | [Rate Limiting on GitLab.com — Program Index](https://gitlab.com/groups/gitlab-com/gl-infra/-/epics/2112)         |
| **Canonical design**   | [Unified Rate Limiting Architecture](/handbook/engineering/architecture/design-documents/unified_rate_limiting/)  |
| **Issue tracker**      | [production-engineering](https://gitlab.com/gitlab-com/gl-infra/production-engineering/-/issues)                  |
| **Team Slack Channel** | [#g_tenant-controls](https://gitlab.slack.com/archives/C0ATYKN2NTG)                                                                                              |
| **Operator docs**      | [Rate Limiting handbook section](/handbook/engineering/infrastructure-platforms/rate-limiting/), [rate limiting runbook](https://gitlab.com/gitlab-com/runbooks/-/blob/master/docs/rate-limiting/README.md) |

## Team Members

The following people are members of the Tenant Controls team:

<!-- Listed manually: these members carry no Tenant Controls team_tag upstream, so team-by-manager-slug cannot select them. -->

| Name | Role |
|------|------|
| [Bob Van Landuyt](https://gitlab.com/reprazent) | Architect |
| [Hercules Lemke Merscher](https://gitlab.com/hmerscher) | Backend Engineer |
| [Ashwin S](https://gitlab.com/ashs2) | Backend Engineer |
| [Hardik Gala](https://gitlab.com/hardikgala) | Backend Engineer |
| [Sankalp Das](https://gitlab.com/sankalp_gl) | Backend Engineer |
| [Nidhey Indurkar](https://gitlab.com/nindurkar) | Backend Engineer |

## How work is tracked

The team plans and tracks its work as epics and issues in the `gitlab-com/gl-infra` group.
Every board listed below is driven entirely by labels, and GitLab does not propagate labels
from an epic to its child issues, so the author applies them when the epic or issue is created.

The labels and boards are named after the work, `Rate Limiting`, rather than after the team, so
`team::Rate Limiting` is the Tenant Controls team's label.

Two principles keep the boards accurate:

**The epic defines the labels.** The `team::` and `rate-limits::` labels on an epic are the
labels its child issues are expected to carry. An issue created without them appears on no
board and is therefore missed in planning and status reviews.

**The epic board is the inventory.** The epics in scope are those carrying
`team::Rate Limiting`; no separate list is maintained. Applying the label brings an epic into
scope, and removing the label or closing the epic takes it out.

## Boards

One epic board, one team-level issue board, and one issue board per workstream.

| Board | Type | Scope label |
|---|---|---|
| [Rate Limiting Team - Epics](https://gitlab.com/groups/gitlab-com/gl-infra/-/epic_boards/3105698) | Epic board | `team::Rate Limiting` |
| [Rate Limiting Team - Delivery](https://gitlab.com/groups/gitlab-com/gl-infra/-/boards/11620253) | All team issues | `team::Rate Limiting` |
| [Tier-Aware Throttles](https://gitlab.com/groups/gitlab-com/gl-infra/-/boards/11580670) | Workstream | `rate-limits::tier-aware-throttles` |
| [Rack::Attack Removal](https://gitlab.com/groups/gitlab-com/gl-infra/-/boards/11620514) | Workstream | `rate-limits::rack-attack-removal` |
| [SDK Conformance](https://gitlab.com/groups/gitlab-com/gl-infra/-/boards/11590863) | Workstream | `rate-limits::sdk-conformance` |
| [Rails Unification](https://gitlab.com/groups/gitlab-com/gl-infra/-/boards/11624199) | Workstream | `rate-limits::rails-unification` |
| [Config Externalization](https://gitlab.com/groups/gitlab-com/gl-infra/-/boards/11624316) | Workstream | `rate-limits::config-externalization` |
| [Dynamic Rule Service](https://gitlab.com/groups/gitlab-com/gl-infra/-/boards/11625955) | Workstream | `rate-limits::dynamic-service` |
| [Opportunistic and KTLO](https://gitlab.com/groups/gitlab-com/gl-infra/-/boards/11625109) | Workstream | `rate-limits::ktlo` |

Because `rate-limits::` labels are scoped, an issue can carry only one of them. The workstream
boards are therefore a partition of the Delivery board: the workstream counts sum to the team
count. If they stop matching, an issue is missing a workstream label, usually because an epic
went on the board without one.

## Labels

These labels are defined at the `gitlab-com/gl-infra` group and are specific to this team. For
the labels every Infrastructure Platforms team uses, such as `workflow-infra::`, `group::`,
`section::` and `infra-category::`, see
[Infrastructure Platforms Project Management](/handbook/engineering/infrastructure-platforms/project-management/).

| Label | Meaning |
|---|---|
| `team::Rate Limiting` | Owned by this team. Puts an epic on the epic board and an issue on the Delivery board. |
| `rate-limits::<workstream>` | Which workstream the work belongs to. Scoped, so exactly one per issue. |
| `initiative::rate-limits` | Part of the wider rate limiting program, including work owned by other teams. |

### Naming a new workstream label

Format: `rate-limits::<workstream>`, where `<workstream>` is a kebab-case short name for the
workstream, such as `rate-limits::config-externalization`. The [Boards](#boards) table lists the
labels currently in use.

- Name the **outcome**, not the artifact. Use `config-externalization` rather than `yaml-file`,
  because formats change and outcomes usually do not.
- Keep it **short**: one to three words, close enough to the workstream's epic title and board
  name that the three can be matched at a glance.
- Use **US spelling**, so `-ization` rather than `-isation`, even where an epic title uses
  British spelling. Nobody should have to guess when filtering.
- **One workstream label per epic.** Two would break the partition, and because the labels are
  scoped GitLab silently replaces one with the other anyway.
- **Never invent a label on an issue.** If an epic carries no `rate-limits::` label, create the
  label and put it on the epic first.

## Adding a new workstream

Three steps, in order:

1. **Create the label** at `gitlab-com/gl-infra`: `rate-limits::<name>`, color `#5843AD`, with a
   description that links the epic.
1. **Put it on the epic**, together with `team::Rate Limiting`. That second label is what places
   the epic on the epic board.
1. **Carry both labels down** to the epic's child issues, and keep applying them to new issues
   as they are filed.

Then create an issue board scoped to the new label, if the workstream warrants one.

### Standing work that fits no workstream

Small improvements and keep-the-lights-on items that belong to no workstream go to the standing
quarterly epic under `rate-limits::ktlo`. If an item fits an existing workstream, file it there
instead. The standing epic is closed and rolled forward each quarter, so its contents get a
forced review rather than accumulating indefinitely.

## Known gaps

- **Cross-group children cannot carry these labels.** They are defined at `gitlab-com/gl-infra`,
  so applying one to an issue in another group, such as `gitlab-org/gitlab`, would create a stray
  project-level label there. Leave those issues unlabeled: they are still tracked in their epics,
  but they do not appear on the team's boards.
- **Child epics do not inherit either.** If an epic has child epics, label each child epic and put
  it on the board in its own right.
