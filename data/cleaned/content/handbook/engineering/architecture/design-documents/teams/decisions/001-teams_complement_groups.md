---
owning-stage: "~devops::tenant_scale"
title: 'ADR-001: Teams Complement Groups'
description: 'Teams are an additive layer over groups rather than a restructuring of them, keeping the decision a two-way door. Group sharing is sunset over the long term in favour of Team grants.'
status: accepted
creation-date: "2026-01-19"
authors: [ "@lohrc", "@rymai" ]
---

## Context

Groups serve two purposes at once: they organize projects into a namespace hierarchy, and they organize people and control their access. That dual purpose is the root of the problems in [Appendix A](../appendices/a-dual_purpose_group_problem.md).

Two ways to resolve it were considered seriously: restructure GitLab's hierarchy so that access, settings, aggregation, and relationships each become their own system, or add a complementary layer and leave groups alone. Every other decision in this series depends on the answer.

## Options Considered

| Option | Why it was rejected or chosen |
| --- | --- |
| Enhance the current group model | Lowest cost, but leaves the dual purpose in place. Sharing inconsistencies and the absence of a people-only entity are properties of the model, not of its implementation |
| Restructure into a flat hierarchy | Cleanest separation, and a one-way door. It would rewrite most permission-related code, break existing integrations, remove the group boundaries customers use for compliance, and reduce namespace cardinality |
| **Teams as a complementary layer** | **Chosen.** A two-way door that builds on the existing architecture, keeps integrations working, and delivers value before the full vision is settled |

## Decision

**Teams are an additive layer over groups rather than a restructuring of them.**

Organizations remain the customer isolation boundary, groups remain where work lives, and Teams describe who does the work. Groups keep their hierarchy, their cascading settings, and their project organization; Teams add a way to grant a set of people access to a part of that hierarchy.

Because Teams are additive, group-based and Team-based user management coexist, and no customer is forced to migrate on GitLab's schedule. Coexistence is how Teams arrive rather than where this ends: the long-term intent is to deprecate, sunset, and eventually remove **group sharing** as an access mechanism, with Team grants replacing it. Group membership itself stays, because a group's own members are how its projects are reached. Teams are gated by a `teams` organization flag advancing through the [Organizations release process](https://docs.gitlab.com/development/organizations/release_process/), so the additive layer arrives one audience at a time rather than all at once.

## Consequences

### Positive

- The decision can be revised. Team ownership, nesting, or deeper restructuring can be added later; none of them could be extracted from a restructured model without a migration
- Existing integrations, automations, and API contracts keep working
- Customer value arrives incrementally instead of after a multi-year rewrite

### Negative

- Two ways to manage users means two things to document, support, and maintain. The sunset bounds that cost rather than leaving it open-ended, but it also commits GitLab to the removal work and not only to the addition
- The dual purpose of groups is mitigated, not eliminated: a group can still be used as a member bag, and nothing prevents it
- **The sunset needs a migration program, not a deprecation notice.** Some customers will not move on their own, and removing group sharing requires the group-as-principal parity in [ADR-007](007-parity_before_migration.md) to be complete rather than partial, because a group referenced as a principal cannot be converted at all until its feature accepts a Team

## Related Documents

- [Teams blueprint](../_index.md)
- [Appendix A: The Dual-Purpose Group Problem](../appendices/a-dual_purpose_group_problem.md)
- [Appendix C: Industry and Competitive Context](../appendices/c-industry_and_competitive_context.md)
- [ADR-003: A Team Is a Principal, Not a Container](003-a_team_is_a_principal_not_a_container.md)
