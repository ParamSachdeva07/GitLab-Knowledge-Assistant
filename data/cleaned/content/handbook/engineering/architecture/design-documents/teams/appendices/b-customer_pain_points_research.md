---
owning-stage: "~devops::tenant_scale"
title: 'Appendix B: Customer Pain Points and Research Findings'
description: 'Customer interviews, support analysis, and the measurements that substantiate the need for a separate Teams entity.'
status: accepted
creation-date: "2026-01-19"
authors: [ "@lohrc", "@rymai" ]
---

This appendix summarizes the customer research behind the [Teams blueprint](../_index.md), drawn from enterprise customer interviews, support ticket analysis, internal employee interviews, and existing feature requests. It is background: no decisions are made here. For the problem statement these findings substantiate, see [Appendix A](a-dual_purpose_group_problem.md).

## Pain Point Categories

**Permission management and inheritance.** Inheritance is confusing and hard to predict. The recurring scenario is a project manager who needs epic and issue visibility at the group level, where granting Guest propagates to every project below and exposes repositories they should not see. Customers cannot exclude inherited members from specific projects, cannot grant planning visibility without code access, and cannot assign a group of users directly to an environment or a protected branch without first assigning it at the project level — a gap they work around with role naming conventions that do not scale across thousands of projects. For companies whose business depends on proprietary software, accidental exposure through inheritance is described as potentially catastrophic.

**Organizational structure limitations.** Users report confusion about the distinction between projects and groups from their first day, and check URLs to work out where they are. Feature parity differences between the two levels lead some to describe the experience as two separate platforms. Customers who reorganize every 6 to 12 months face repeated restructuring because the hierarchy conflates organizational structure with project organization, and matrix organizations, multiple reporting lines, and temporary project teams have no representation at all.

**Enterprise scale management.** One representative deployment has 12,000 users, 180,000 projects, and 25,000 groups, with thousands of top-level groups created without consistent naming or hierarchy. Features designed around hierarchical reporting become unusable when the structure does not match the product's assumptions: these customers cannot answer "show me all Java projects in my area" and have built external tools for compliance scanning and cross-project reporting. Teams of 15 or more administrators manage permissions, compliance reporting, and user lifecycle manually, without adequate bulk operations.

**Audit and compliance gaps.** Administrators report difficulty tracking who has access to what, with ex-employees appearing in project member lists despite access being disabled higher in the hierarchy. Over-provisioning is common: release managers who only need to trigger deployments are granted developer access because no deployment-specific role exists. There is no centralized permission reporting for audits, no automated periodic access review, and terminated-employee cleanup is manual across every project.

**Member management fragmentation.** The members overview cannot clearly show all members and their sources, users from shared groups do not appear in project member lists at all, and administrators cannot determine why a user holds a particular role. Max-role calculation is unexplained, so nobody can tell whether a role came from inheritance, a direct invite, or a share, while the "Select a role" UI suggests a choice where the result is calculated. Member-heavy pages return 500 errors past roughly 1,500 members.

**Data recovery and deletion concerns.** Deletion is described as too easy relative to its consequences, and recovery windows as too short for enterprise change management, where an unintended deletion may not surface until the next reporting cycle. The effect on access is indirect but significant: customers afraid of losing data are reluctant to restructure access at all, which entrenches whatever over-provisioned structure they already have.

## Patterns Across the Research

**Work, code, and people are organized differently.** People sit in hierarchical org structures with matrix-like team membership that changes at every reorganization. Work is process-oriented and flow-based — epics to stories to tasks do not map onto groups to projects. Code is organic, less hierarchical except for permissions, and repositories are owned by teams in ways that do not match project structure. One hierarchy is being asked to serve all three.

**The empty groups signal.** Around **15% of groups contain no projects at all** and exist purely for member management. A narrower measurement points the same way from the other end: roughly **35% of all group shares** in the `gitlab-org` hierarchy are clean-replacement cases, where the shared-with group is a pure member bag. That second figure is what makes assisted conversion worth building ([ADR-007](../decisions/007-parity_before_migration.md)).

**Security is the primary driver.** Code exposure risk is existential for software companies, security concerns are the main barrier to SaaS migration for some customers, and regulated industries require governance controls the current model cannot enforce.

**Products outlast teams.** Customers note that products and product groups are more stable than team structures, making them better anchors for hierarchy. Tying user management to the same hierarchy forces a choice between optimizing for people or for code.

## Related Documents

- [Teams blueprint](../_index.md)
- [Appendix A: The Dual-Purpose Group Problem](a-dual_purpose_group_problem.md)
- [Appendix C: Industry and Competitive Context](c-industry_and_competitive_context.md)
