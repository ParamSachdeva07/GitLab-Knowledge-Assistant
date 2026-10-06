---
title: "Spec Driven test scenarios"
description: "Testing scenarios and requirements for Spec-Driven Development features including the Agent plan widget."
status: ongoing
maturity: still defining
creation-date: "2026-04-21"
authors: [ "@vanessaotto" ]
owning-stage: "~devops::plan"
toc_hide: true
---

Read more about SDD in [Spec-Driven Development](_index.md).

## Summary

This page add testing scenarios and requirements that relate to Spec driven development features.

### Agent plan

#### Prerequisites

Before running any test scenarios, ensure the following conditions are met:

- **Feature Flag**
  - The `agent_plan` feature flag must be enabled for the user, group, or instance under test.
  - Verify via: Rails console (`Feature.enable(:agent_plan)`) or the GitLab Admin UI under `/admin/feature_flags`.
- **EE Mode**
  - The instance must be running in EE mode. The feature is not available in FOSS-only mode.
  - To confirm: do not start GDK with `FOSS_ONLY=1`. Starting with that flag should cause the widget to be absent - this is itself a test case (see Section 1).
- **User / Data Setup**
  - At least one project with each work item type available: Issue, Task, Incident, Epic.
  - At least one group with work items (Issues, Epics).
  - A user account with sufficient permissions to view work items in both project and group contexts.

#### Section 1 - Feature Flag & EE Gating

These tests confirm the feature is correctly guarded before any UI testing begins.

##### 1.1 - Feature is hidden when agent_plan flag is OFF

**Steps:**

1. Disable the `agent_plan` feature flag.
1. Navigate to any work item (e.g., a project Issue).
1. Observe the work item detail panel or full page.

**Expected:** The agent plan widget is not rendered. No empty placeholder or broken UI is visible.

##### 1.2 - Feature is hidden in FOSS-only mode

**Steps:**

1. Start GDK with `FOSS_ONLY=1 gdk start`.
1. Enable the `agent_plan` feature flag.
1. Navigate to any work item.

**Expected:** The agent plan widget is not rendered. The rest of the work item UI renders normally.

##### 1.3 - Feature is visible with flag ON in EE mode

**Steps:**

1. Ensure GDK is running without `FOSS_ONLY=1`.
1. Enable the `agent_plan` feature flag.
1. Navigate to any work item.

**Expected:** The agent plan widget is visible within the work item detail view.

#### Section 2 - Project Work Items

These tests cover the agent plan widget in a project context. Run each scenario for both the panel view and the full page (single-item view).

Views to test for each scenario:

- **Panel view** - work item opened as a side panel (e.g., from a board or list)
- **Full page** - work item opened directly at its own URL

##### 2.1 - Issue in a Project

**Steps:**

1. Navigate to a project.
1. Open an Issue in panel view. Verify the agent plan widget is present.
1. Open the same Issue (or another) at its full page URL. Verify the agent plan widget is present.

**Expected:** Agent plan widget renders correctly in both panel view and full page.

##### 2.2 - Task in a Project

Same steps as 2.1, using a Task work item type.

**Expected:** Agent plan widget renders in both views.

##### 2.3 - Incident in a Project

Same steps as 2.1, using an Incident work item type.

**Expected:** Agent plan widget renders in both views.

##### 2.4 - Epic in a Project

Same steps as 2.1, using an Epic work item type (if available at the project level).

**Expected:** Agent plan widget renders in both views.

##### 2.5 - Other / Additional Work Item Types

For any other work item types supported by the project (e.g., OKR, Key Result, Test Case), repeat the same panel + full page check.

**Expected:** Agent plan widget renders consistently regardless of work item type.

#### Section 3 - Group Work Items

These tests cover the agent plan widget in a group context.

**Note:** Group work items are accessible only in panel view unless the work item has a full standalone URL at the group level. Test accordingly.

##### 3.1 - Issue in a Group (Panel View)

**Steps:**

1. Navigate to a group's work items list.
1. Open an Issue in panel view.

**Expected:** Agent plan widget is visible in the panel.

##### 3.2 - Epic in a Group (Panel View)

**Steps:**

1. Navigate to a group's Epics list.
1. Open an Epic in panel view.

**Expected:** Agent plan widget is visible in the panel.

##### 3.3 - Epic in a Group (Full Page)

**Steps:**

1. Navigate to a group's Epics list.
1. Open an Epic at its full page URL.

**Expected:** Agent plan widget is visible on the full page.

#### Section 4 - Negative / Edge Cases

These tests protect against regressions and unexpected exposure of the feature.

##### 4.1 - Flag toggled OFF mid-session

**Steps:**

1. Enable the flag and navigate to a work item. Confirm the widget is visible.
1. Disable the flag.
1. Refresh the page.

**Expected:** The widget is no longer rendered after the flag is disabled and the page is refreshed.

##### 4.2 - User without sufficient permissions

**Steps:**

1. Log in as a user with Guest-level access to a project.
1. Navigate to a work item.

**Expected:** Verify expected behavior - either the widget is hidden, or it renders in a read-only state, depending on the intended permission model. Clarify with the team and document the expected state here.
