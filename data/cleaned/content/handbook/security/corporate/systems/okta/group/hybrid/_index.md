---
title: Hybrid Okta Groups
---

## Overview

Hybrid groups combine the best of both worlds: **automated membership** based on Workday attributes with the ability to **manually add exceptions** through access requests. These groups are usually intended to be pushed to other GitLab services like Google, Slack, etc. in order to sync members and automate groups.

**Use hybrid groups when**

* Most members of the group can be automatically added by Workday attributes
* A small number of exceptions need to be included (For example: executive assistants supporting a division, cross-functional partners)

**Hybrid groups use a combination of**

* Okta Group Rules - Automatically populates core membership based on attributes
* Manual Additions via access request - Allows approved exceptions to be added

### Example

**Group:** push.google.dept.brand_design - A mailing list that includes all members of the “Brand Design” department

**Google Group:** dept.brand_design@gitlab.com

**Automated members:** All employees where Department = Brand Design

**Manual additions:** Executive Business Administrator (EBA) supporting the Marketing Division (parent of Brand Design), and a member of the Campaigns Department doing a career experience for 6 months (performing both roles simultaneously)

## Membership Lifecycle

**Automated members:** Added/removed automatically when Workday data changes (within 1 hour)

**Manual members:** Team members can use an access request issue to be manually added to a group

**Both types:** Users are automatically removed when they leave GitLab

## Naming Convention

Hybrid groups are almost always application push groups and will generally follow the same pattern as other app groups:

**Pattern:** push.{application}.{attribute}.{value}.{secondary_value}.{tertiary_value}

### Examples

* **push.google.div.security** - Security division Google Group with manual additions enabled

* **push.slack.dept.engineering** - Engineering department Slack group with manual additions enabled
  * The Slack Group will simply be named dept.engineering

* **push.google.dept.brand_design.manager** - Brand Design managers in Google with manual additions enabled
  * The Google Group will be named Brand Design Dept Managers and the email address will be dept.brand_design.manager@gitlab.com

Note: You may come across some situations where a group can not be named according to our conventions.
An example may be where the application supports group attribute mappings, and requires the Okta Groups to be in a certain format.
Push Groups can often be renamed in the downstream application to align with the needs of that service while maintaining the correct convention in Okta.
An Okta Group may be `push.google.div.security` in Google, but can be configured to show up in Google Workspace as `Security Division Employees`
