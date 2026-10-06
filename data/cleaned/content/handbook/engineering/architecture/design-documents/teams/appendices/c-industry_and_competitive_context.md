---
owning-stage: "~devops::tenant_scale"
title: 'Appendix C: Industry and Competitive Context'
description: 'Market and competitive evidence behind the Teams blueprint, and how other platforms solved the same problem.'
status: accepted
creation-date: "2026-07-28"
authors: [ "@lohrc", "@rymai" ]
---

This appendix collects the market and competitive evidence behind the [Teams blueprint](../_index.md). It is background: no decisions are made here. The decision this evidence informs is [ADR-001](../decisions/001-teams_complement_groups.md).

## Industry Context and Competitive Pressure

Access management inefficiencies cost US companies approximately $61 billion annually, with 94% of applications showing some form of broken access control. Broken access control is also [the #1 vulnerability in the OWASP Top 10](https://owasp.org/Top10/A01_2021-Broken_Access_Control/).

Major platforms have converged on four approaches to enterprise access management: team-based hierarchical models with explicit inheritance patterns, organizational structure separated from project management, project-level permission cascading that removes per-resource management overhead, and a clear split between permanent user organization and temporary access. GitLab's dual-purpose group model increasingly appears dated against these, which limits enterprise adoption and competitive positioning.

## Competitive Analysis Insights

Four patterns recur across the platforms studied. Each carries a challenge GitLab's design has to answer rather than inherit.

**Hierarchical team models** — parent-child teams with automatic permission inheritance, access control integrated into development workflows through code ownership, and fine-grained tokens with organization-level approval. The challenge is deep nesting complexity and its performance cost. GitLab's answer is flat Teams over the namespace hierarchy ([ADR-003](../decisions/003-a_team_is_a_principal_not_a_container.md)), taking the inheritance benefit from a hierarchy that already exists rather than from nesting Teams.

Named evidence for that choice, since the products differ more than "some nest and some do not" suggests:

| Product | Nests? | What the documentation says |
| --- | --- | --- |
| [GitHub teams](https://docs.github.com/en/organizations/organizing-members-into-teams/about-teams) | Yes | "Multiple levels of nested teams", and "child teams inherit the parent's access permissions". No documented depth limit |
| [Microsoft Entra ID security groups](https://learn.microsoft.com/en-us/entra/fundamentals/concept-learn-about-groups) | Yes, but access does not follow | "Groups can be members of other groups", yet "only members in the parent group have access to shared resources and applications". Microsoft 365 groups take users only |
| [Slack user groups](https://slack.com/help/articles/212906697-Create-user-groups) | No documented support | Membership is individual users; nothing in the documentation adds a group to a group |

The Entra row is the more instructive one. The largest directory product permits nesting and then declines to propagate resource access through it, which is the same conclusion this blueprint reaches by a different route: a nesting structure that does not confer access is organizational modeling, and one that does confer access is a second inheritance system competing with the namespace hierarchy.

**Enterprise-scale organizational integration** — multi-tier structures spanning thousands of organizational units, mapping for both structural and temporal workflows, and tight directory-service integration. The challenge is that this complexity overwhelms smaller teams and creates vendor dependencies.

**Cross-product permission consistency** — cascading project-level permissions, centralized administration across an integrated suite, and simplified role models. The challenge is maintaining consistency across diverse capabilities. GitLab's answer is to enforce through the existing membership system rather than beside it ([ADR-004](../decisions/004-team_membership_is_an_ordinary_membership.md)), so consistency is structural rather than maintained.

**Separation of permanent and temporary access** — permission boundaries defining maximum capability regardless of grants, and just-in-time access for sensitive operations. The challenge is implementation complexity and the learning curve. Grant expiry is in scope; just-in-time access and permission boundaries remain secondary goals.

## Industry Validation of the Hybrid Approach

Industry evolution since 2023 supports adding Teams as a complementary layer rather than restructuring: major platforms implemented Teams alongside their existing organizational structures rather than replacing them.

Cross-platform architectural constraints — hierarchy depth of 5 to 10 levels, 1,000 to 5,000 entities per container, 150 to 300 groups per token — are what three of the blueprint's four scale limits come from, each taken at the conservative end of its range rather than derived by a formula. Enterprise architects should design assuming practical thresholds arrive at 20% to 30% of documented hard limits, because the most impactful limits are undocumented degradation points rather than hard caps.

The fourth limit, **under 100 direct children per parent**, is a GitLab observation rather than a cross-platform one, and it is recorded here without a citation. It needs a source or it should be dropped from the blueprint's [Scale](../_index.md#scale) section.

## Source Material

Detailed competitive analysis, including specific platform implementations and feature comparisons, is in the [DevOps Access Control Research Report (internal)](https://drive.google.com/drive/folders/1WeMK7PYvFhGtWqYFY8VPMUOxUVfay3vr?ths=true).

## Related Documents

- [Teams blueprint](../_index.md)
- [Appendix A: The Dual-Purpose Group Problem](a-dual_purpose_group_problem.md)
- [Appendix B: Customer Pain Points and Research Findings](b-customer_pain_points_research.md)
- [ADR-001: Teams Complement Groups](../decisions/001-teams_complement_groups.md)
