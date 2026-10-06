---
title: Managed Okta Groups
---

## Overview

Managed, rule-based, attribute-based, dynamic, or automated groups are those created using Okta Group Rules, that definitively include all members of a certain attribute. They can be used for reporting purposes, or for using in iPaaS tools like Okta workflows to sync with other services.
Aside from the “Employee Type” attribute, all managed groups will be exclusively populated with employees unless mentioned otherwise
**Critical Rule: There should NEVER be any members that are manually added to these groups.**

## Ownership

The CorpSec Identity team will be responsible for creating and maintaining all new and existing managed groups, for each of the attributes that we support (see Supported Attributes section below) {LINK}.

These groups will be adjusted whenever departments are added/removed/changed, company entity names are changed, or whenever we hire employees in a new country.

If you are in need of a managed group that encompasses multiple attributes, crosses multiple departments or more, please create a CorpSec issue {LINK} and let us know what groups you need to automate, and why.

## Naming Convention

All managed groups will follow the pattern: {attribute}.{attributeValue}.

Examples:

* dept.engineering
* div.security
* country.us
* mgmt_level.manager

### Alternatives considered

* sot.* (source of truth)
* auto.* (automated)
* dyn.* (dynamic)

We've chosen this solution because of a few reasons

* **Community standards** - Most other organizations don't seem to utilize a prefix for attribute-based groups and rules.
* **Length of group and rule names** - By not adding a prefix, we are less likely to bump up against length limitations like Okta Group Rules' name limits being 55 characters.

## Supported Attributes

The following attributes from Workday are available for managed group creation:

| Attribute | Attribute Shortname | Example Value | Example Group Name |
|-----------|---------------------|---------------|-------------------|
| Division | div | Security, Engineering, Sales | div.security |
| Department | dept | Accounting Operations, Communications, Corporate Security | dept.accounting_operations |
| Country Code | country | NL, US, CA | country.nl |
| Workday Management Level | mgmt_level | Director, Manager, Individual Contributor | mgmt_level.individual_contributor |
| Workday Company | company | GitLab Canada Corp., GitLab Inc, GitLab Federal, LLC | company.gitlab_canada_corp |
| User Type | user_type | Employee, Contractor, Professional Services Partners | user_type.employee |

## Use Cases

Here are some examples where these groups may be valuable:

* Reporting: Quickly identify all members of a specific department or division
* Compliance audits: Generate lists of employees by country or company entity
* Communication: Target announcements to specific organizational units
* Automation: Use as source groups for Okta Workflows or other iPaaS integrations
* Application provisioning: Feed into push groups for Google, Slack, and other applications

## Multi-Attribute Groups

Managed groups can also combine multiple attributes for more specific targeting.
We recommend this order for consistency:

1. Division
2. Department
3. Management Level
4. Workday Company
5. Country Code
6. Employee Type (**Default Scope**: All groups are Employee-only by default unless the group name explicitly includes another employee type. ex: user_type.contingent_worker)

Examples:

* **division.security.manager.us** - All managers in the security division, in the USA
* **department.engineering.individual_contributor** - All individual contributors in Engineering

## Character Limit Constraint

Okta Group Rule names have a 50-character limit.
Google Groups have a 73-character limit. Keep combined attribute groups concise to ensure compatibility with downstream applications.

## Membership Updates

Membership in managed groups is automatically updated based on Workday data:

* Workday changes sync to Okta within 1 hour
* No manual intervention required
* Changes propagate automatically to all downstream push groups
* If a request comes in to manually add somebody to one of these managed groups, please partner with the People Ops team to update their information in Workday. Otherwise, we are not manually assigning team members to these managed groups
