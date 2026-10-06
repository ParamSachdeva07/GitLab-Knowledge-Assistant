---
stage: enablement
group: Tenant Scale
title: 'Cells: Term Agreements'
toc_hide: true
---

{{% alert %}}
This document is a work-in-progress and represents a very early state of the
Cells design. Significant aspects are not documented, though we expect to add
them in the future. This is one possible architecture for Cells, and we intend to
contrast this with alternatives before deciding which approach to implement.
This documentation will be kept even if we decide not to implement this so that
we can document the reasons for not choosing this approach.
{{% /alert %}}

Term agreements will be cell-local. As a result, users migrated to another cell will be prompted to re-accept the terms and conditions.

## 1. Definition

GitLab allows administrators to require all users to accept [terms of service](https://gitlab.com/-/users/terms) before they can use the instance. Acceptance is recorded as a term agreement associated with the user.

## 2. Data flow

Term agreements are stored per-cell. When a user accepts terms on a given cell, that acceptance is only recorded locally on that cell. There is no cluster-wide record of term acceptance.

## 3. Proposal

### 3.1. Cell-local term agreements

Term agreements will remain cell-local. When a user is migrated to a new cell, their term agreement from the source cell is not transferred. The user will be prompted to re-accept terms on the destination cell before they can proceed.

This approach is consistent with keeping user-facing compliance actions scoped to the cell the user is currently operating on. See [issue #595225](https://gitlab.com/gitlab-org/gitlab/-/work_items/595225#note_3390346693) for the decision rationale.

## 4. Evaluation

We choose Cell-local term agreements.

### 4.1. Pros

- No cross-cell synchronization of term agreement state is required.
- Term acceptance remains auditable and enforceable per-cell.

### 4.2. Cons

- Users migrated to another cell must re-accept terms, which may be unexpected.
