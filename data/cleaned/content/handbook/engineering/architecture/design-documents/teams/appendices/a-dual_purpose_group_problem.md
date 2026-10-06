---
owning-stage: "~devops::tenant_scale"
title: 'Appendix A: The Dual-Purpose Group Problem'
description: 'Background on the dual-purpose nature of GitLab groups and how Teams relate to existing systems.'
status: accepted
creation-date: "2026-07-28"
authors: [ "@lohrc", "@rymai" ]
---

This appendix explains the problem the [Teams blueprint](../_index.md) exists to solve, and how Teams relate to the systems already in place. It is background: no decisions are made here.

## Groups Do Two Jobs

Groups serve two purposes that create inherent tension: they are a hierarchical structure for managing code, issues, and CI/CD resources, and they are the mechanism for organizing people and controlling their access to those resources.

Nothing distinguishes the two uses. The same entity, with the same settings, hierarchy, and sharing mechanics, models "the Platform department" and "the place the API gateway lives". Customers who need those two structures to differ — and large customers almost always do, because reporting lines and repository layout evolve independently — can only express it by creating groups that exist to hold people, and sharing them into the groups that hold work.

Three consequences follow, and they are what customers report. Detailed evidence for all three is in [Appendix B](b-customer_pain_points_research.md).

**Permission management complexity.** Nearly every customer interview mentioned inheritance producing unexpected access levels when users hold different roles at different hierarchy levels. GitLab's roles already provide fine-grained control through over 40 specific [custom permissions](https://docs.gitlab.com/user/custom_roles/abilities/); the complexity comes from how those interact with the dual purpose of groups, not from the permissions themselves.

**Inconsistent sharing behavior.** Sharing a group with another group shares only its direct members, while sharing a group with a project includes both direct and inherited members. Two operations that read as the same action produce different populations.

**Cognitive load.** Users expect permissions to be explicit and visible. Invisible inheritance violates that expectation, and people work around what they cannot predict.

## Why Organizations Do Not Resolve It

The [Organization](../../organization/_index.md) framework provides customer isolation and administrative boundaries. It is a prerequisite for Teams rather than an alternative to them.

It does not resolve the dual purpose of groups. Organizations contain groups, and those groups still face the same challenges: no way to separate user management from project organization, and administrative overhead for cross-functional collaboration. The two layers answer different questions. Organizations provide **customer isolation**; Teams provide the **who does the work** layer inside a customer's boundary.

## How Teams Relate to Existing Systems

**Roles** define what users can do; **Teams** define which users should have access. Teams do not replace, wrap, or reinterpret roles — a Team grant carries an existing role, and it resolves the way any other member's role resolves ([ADR-004](../decisions/004-team_membership_is_an_ordinary_membership.md)).

**Organizations** are the boundary Teams operate inside, never crossing customer isolation ([ADR-002](../decisions/002-teams_are_organization_scoped.md)).

**Groups and projects** continue to provide namespace management, settings inheritance, and project organization. Projects remain the fundamental unit of work, reachable through both the group hierarchy and Team access ([ADR-001](../decisions/001-teams_complement_groups.md), [ADR-003](../decisions/003-a_team_is_a_principal_not_a_container.md)).

## Related Documents

- [Teams blueprint](../_index.md)
- [Appendix B: Customer Pain Points and Research Findings](b-customer_pain_points_research.md)
- [Appendix C: Industry and Competitive Context](c-industry_and_competitive_context.md)
- [Organization blueprint](../../organization/_index.md)
