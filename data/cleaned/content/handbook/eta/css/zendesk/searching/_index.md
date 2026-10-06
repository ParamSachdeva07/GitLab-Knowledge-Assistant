---
title: 'Searching'
description: 'Documentation on searching within Zendesk'
---

This guide provides a reference for searching for items (tickets, users, organizations, etc.) within Zendesk.

## Search limitations

Note that while a search can say it has over 1000 results, only the first 1000 results (based on whichever sorting method you are using in the UI) can be accessed.

## Basic search

To perform a basic search, click the magnifying glass icon in the top-right of any page within Zendesk. This will reveal a textbox you can type your search into. Without using methods detailed in [Advanced searching](#advanced-searching), this will do a loose text match (also known as a fuzzy case-insensitive match) for the text you type to various items in Zendesk.

After typing your search query, hit the enter/return key on your keyboard.

This will bring up the search results page. The results from your search are separated into tabbed sections:

- Tickets
- Articles
- Users
- Organizations

If you wish to share these search results, the white `Copy link` button can be used to create a link that will replicate the search for you to share.

## Advanced searching

This covers searching for more specific information using the Zendesk search language. All results are still shown much like those within a [basic search](#basic-search). This is ideal to use when you need to refine your search beyond that of the loose text matching basic searches do.

### Using negation

You can search by negation by putting a minus sign in front of the search item. This will then do a "NOT" style search for it.

As an example, if you wanted to find items that do _not_ contain the tag `spam`, you would do `-tags:spam`.

### Searching by tag

To search for objects with a specific tag, you would simply use the syntax:

`tags:tag_name`

As an example, to locate objects using the tag `skip_2fa_automation`, you'd use:

`tags:skip_2fa_automation`

You can search for the negation of this by putting a minus in front of it:

`-tags:tag_name`

If you wanted to search for objects with multiple tags, you'd encapsulate them in double quotes:

`tags:"tag_name tag_name"`

As an example, if you wanted to find all objects that contains _both_ the tags `gold` and `sev1`, you'd do:

`tags:"gold sev1"`

### Comparison operators

The comparison operators are:

| Operator | Meaning                  |
|:--------:|--------------------------|
| `:`      | Equal to                 |
| `<`      | Less than                |
| `<=`     | Less than or equal to    |
| `>`      | Greater than             |
| `>=`     | Greater than or equal to |

### Searching by organization

You can search by organization using the format:

`organization:name_of_organization`

What this pulls up varies by object type:

- For tickets, it pulls up tickets owned by the organization
- For users, it pulls up users associated to the organization
- For organizations, it pulls up the organization

### Ticket only methods

### Searching by ID

To search by the ID, just put the ID value in the search box (by itself) and do the search. Doing so will open the ticket in your browser.

#### Searching by priority

To search by ticket priority, you would use the syntax:

`priority{operator}name`

The priority names (and order) are:

1. low
1. normal
1. high
1. urgent

These values are compared ordinally based on the order above

#### Searching by status

To search by ticket status, you would use the syntax:

`status{operator}name`

The status names (and order) are:

1. new
1. open
1. pending
1. hold
1. solved
1. closed

These values are compared ordinally based on the order above

#### Searching by dates

To search using dates, you will use the specific date object you want to search. For tickets:

| Object | What it ties to |
|--------|-----------------|
| `created` | The date the ticket was created |
| `updated` | The date of the most recent update on a ticket |
| `due_date` | The value of the due date ticket field for a ticket |
| `solved` | The date the ticket was solved (most recent one if moved to solved multiple times) |

You will use this in conjuction with [Comparison operators](#comparison-operators) to do a search, using the date format of `YYYY-MM-DD`.

As an example, to locate all tickets created after December 18, 2023, you would do `created>2023-12-18`

#### Searching by custom ticket field

To search by a custom ticket field, you use the format:

`custom_field_{id}:value`

where `{id}` is the ticket field ID. This one can be less intuitive as it requires knowing the ticket field ID. The best resource for this would be to talk to the Customer Support Systems team (via Slack) for assistance in locating the ticket field's ID value.

#### Searching by satisfaction rating

To locate tickets based on satisfaction rating, you would use the format:

`satisfaction:value`

The possible values are:

- bad - A bad rating without a comment
- badwithcomment - A bad rating with a comment
- good - A good rating without a comment
- goodwithcomment - A good rating with a comment
- offered - The survey has been sent but not responded to

#### Searching by submitter

To search by the submitter of a ticket, you use the format:

`submitter:search`

Where `search` can be:

- The email of the user
- The name of the user
- The ID of the user
- The term `me` (which searches for yourself)

#### Searching by requester

To search by the requester of a ticket, you use the format:

`requester:search`

Where `search` can be:

- The email of the user
- The name of the user
- The ID of the user
- The term `me` (which searches for yourself)

#### Searching by assignee

To search by the assignee of a ticket, you use the format:

`assignee:search`

Where `search` can be:

- The email of the agent
- The name of the agent
- The ID of the agent
- The term `me` (which searches for yourself)

### Organization only methods

#### Searching by custom organization field

To search by a custom organization field, you use the format:

`field_api_name{operator}query`

The common organization field API names are:

| Field                       | What it is for                                   | Zendesk Instance |
|-----------------------------|--------------------------------------------------|------------------|
| `account_owner` | The Account Manager for the org | Both |
| `aar` | The Annual recurring revenue (ARR) of the org | Global |
| `arr` | The Annual recurring revenue (ARR) of the org | US Government |
| `assigned_se` | The user ID of the Assigned Support Engineer for the org | Global |
| `technical_account_manager` | The Customer Success Manager for the org | Both |
| `support_level` | The highest support level of the org | Both |
| `health_score` | The Gainsight health score for the org | Both |
| `seats_decimal` | The highest number of licenses seats for the org | Global |
| `number_of_seats` | The highest number of licenses seats for the org | US Government |
| `salesforce_id` | The 18 character Salesforce account ID for the org | Both |
| `sfdc_short_id` | The 15 character Salesforce account ID for the org | Both |
| `solutions_architect` | The Solutions Architect for the org | US Government |

An example:

Searching for organizations with ARR less than 1000:

`aar<1000`

### User only methods

#### Searching by email

To locate a user by their email, use the format:

`email:email_address`

As an example, to find the user in Zendesk with the email `jcolyer@example.com`, you'd do `email:jcolyer@example.com`

#### Searching by custom user field

To search by a custom user field, you use the format:

`field_api_name:query`

The common user field API names are:

- `gitlab_username` - An agent's GitLab.com username
- `gitlab_user_id` - An agent's GitLab.com user ID

As an example, to find one where the GitLab.com username is jcolyer, you would do:

`gitlab_username:jcolyer`

### Combining advanced search items

You can combine multiple advanced search items to create a more refined search by separating them with a space.

As an example, you can find all tickets containing the tag `customer` that have a status of `new` by doing `tags:customer status:new`.

### Examples

#### Example 1

Task:

- the preferred region of support is AMER (a custom field using ID value `360018253094`)
- the support level of the organization is ultimate
- the satisfaction rating was bad (and had a comment)

`custom_field_360018253094:americas__usa tags:ultimate satisfaction:badwithcomment`

#### Example 2

Task:

- all ticket status except new, solved, and closed
- the assignee is Jason
- the SaaS Account problem type is Namesquatting (a custom field using ID value `360011793260`)

`-status:new -status:solved -status:closed assignee:Jason custom_field_360011793260:namesquatting_requests`

#### Example 3

Task:

- locate an organization in Zendesk based off the Salesforce ID

Salesforce accounts actually have two forms of their IDs, the standard 18 character value and the shortened 15 character value. Zendesk organizations have _both_ values within them, so you can use either to locate the account:

- Based off the 18 character ID value:
  `salesforce_id:ABCDEFGH0123456789`
- Based off the 15 character ID value:
  `sfdc_short_id:ABCDEFGH0123456`

You can also make use of a wildcard search by using an asterisk. So if you have the 15 character value, you could do this as well:

`salesforce_id:ABCDEFGH0123456*`

#### Example 4

Task:

- locate an L&R IR ticket based off the Salesforce ID of the account

As detailed in [Example 3](#example-3), there are two values one could have for a given Salesforce account. With L&R IRs, there is a custom field you can use to locate the Salesforce account it was filed for, but knowing if which of the two was used can be difficult. As such, it is best to use the 15 character value with a wildcard search. If you only have the 18 character value, drop the last 3 characters from the ID (so if it was `ABCDEFGH0123456789`, drop the last 3 to make it `ABCDEFGH0123456`). With that, you would do one of the following searches (depending on which Zendesk instance you are looking in):

- Zendesk Global:
  `custom_field_6978327875612:ABCDEFGH0123456*`
- Zendesk US Government:
  `custom_field_11717220820372:ABCDEFGH0123456*`

## Useful links

- [Zendesk search reference](https://support.zendesk.com/hc/en-us/articles/4408886879258-Zendesk-Support-search-reference)

## Common issues and troubleshooting

This is a living section that will have items added to it as needed.
