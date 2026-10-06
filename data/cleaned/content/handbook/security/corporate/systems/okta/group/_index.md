---
title: Okta Groups
---

## Overview

Okta groups are collections of users that serve multiple purposes across GitLab's identity and access management infrastructure. Groups enable efficient access management, targeting for communications, and organizational reporting by logically organizing users based on attributes, roles, or business needs.

## Purpose of Groups

Groups in Okta serve several key functions:

* **Access Management:** Grant users access to applications and resources based on group membership
* **Communication:** Target announcements, calendar invites, and emails to specific populations
* **Reporting:** Identify and analyze user populations for compliance, auditing, and business intelligence
* **Automation:** Power workflows and integrations across GitLab's technology stack
* **Organizational Structure:** Reflect GitLab's divisions, departments, and teams for easy identification

## Group Capabilities

### Application Assignment

Groups can be assigned directly to applications in Okta to grant access:

* When a user joins the group, they automatically receive access to assigned applications
* When a user leaves the group, their access is automatically revoked
* Simplifies access management by managing groups instead of individual users

### Push Groups (Syncing to External Services)

Okta groups can be "pushed" to downstream applications where native Okta integration is limited or unavailable

**Supported Push Targets:**

* Google Workspace: Push groups become Google Groups with email addresses
* Slack: Push groups become Slack user groups and can be assigned to channels upon joining

Note: gitlab.com is currently not supported for syncing user groups from Okta

**How Push Groups Work:**

1. An application-specific push group is created
2. A group rule is created in Okta to populate members of one or more attributes
3. The push group is assigned to the application in Okta as a "push group"
4. Okta creates and maintains a corresponding group in the target application
5. Membership changes in Okta automatically sync to the external application within minutes

## What kind of group do I need?

**Managed Groups (mostly used by members of the CorpSec team)**

Use when you need a group that represents an organizational unit or combination of Workday attributes. Membership is fully automated and updates within 1 hour of Workday changes. No manual additions are allowed.

Examples:

* All members of the Security division
* All Engineering managers in the United States

Learn more: [Managed Okta Groups](/handbook/security/corporate/systems/okta/group/managed)

**Hybrid Groups (App assignment or App Push Groups with Manual Additions)**

Use when you need a communication group (Google or Slack) where most of the members are defined by attributes, but you need flexibility for manual exceptions.

Examples:

* Security division Slack group + executive assistant
* Engineering managers Google Group + 3 cross-functional Product managers

Learn more: [Hybrid Okta Groups](/handbook/security/corporate/systems/okta/group/hybrid)

**Manual Groups**

Use when membership cannot be defined by Workday attributes, or the group is temporary/project-based. All members can be individually added by creating an access request.

Examples:

* Application admin groups (ex: Figma Admins)
* Push groups to sync assorted membership into an application, that can't be collected by attributes (ex: Cat owners)

Learn more: [Manual Okta Groups](/handbook/security/corporate/systems/okta/group/manual)
