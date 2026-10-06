---
title: 'Tags'
description: 'Documentation on Zendesk tags'
---

This guide covers how to create and use Zendesk tags at GitLab.

{{% alert title="Technical Details" color="primary" %}}

- Deployment type: `Ad-hoc`
  - **Note:** Tags are currently managed manually in Zendesk

{{% /alert %}}

## Understanding tags

### What are tags

As per [Zendesk](https://support.zendesk.com/hc/en-us/articles/4408888664474-About-tags):

> Tags are words, or combinations of words, you can use to add more context to tickets and topics. You can apply tags to tickets, users, and organizations.

At its core, Zendesk relies on tags pretty heavily. As such, it is best to fully understand the tags used and how they correlate to what Zendesk does to the ticket.

### What are our tags

As there are many, many tags, and new ones get added frequently, we maintain it via the [Zendesk Tags Google sheet](https://docs.google.com/spreadsheets/d/1VUaXLcE3L--uBhKi2VrNk8wzaslkydF5AMTMsJMiQpU/edit?usp=sharing) (internal access only).

For more information on how the Google sheet is populated, please see [below](#tag-list-generator).

## How to use tags

{{% alert title="Warning" color="warning" %}}

- As tags have considerable power in Zendesk, you should avoid adding/removing tags from tickets unless you are 100% sure of the impact it could have. Given the variety of use tags allow, it could be as small as causing data consistency issues or as large as a ticket being purged from the system.

{{% /alert %}}

### Naming conventions

While Zendesk does not have an enforced naming convention for tags (outside of requiring the use of alphanumeric characters, hyphens, and underscores), we at GitLab try to follow these concepts for naming tags:

- Keep it simple
- Make the meaning of the tag clear
- Try to have the name also detail where it stems from (for Zendesk items)
- Use snake_case (ex: `support_category_geo`)

### Creating a tag

Creating a tag is done simply by using the tag itself on a Zendesk ticket, organization, or user.

To do so, navigate to the item in question (ticket, organization, or user), click on the `Tags` box, and type your tag (remember no spaces exist in tags). Once you have typed out your new tag, hit the spacebar to "submit" the tag. Once you update the object in question, the tag will exist moving forward.

Keep in mind to update the object in question:

- You have to submit the change on a ticket
- You have to click outside of the `Tags` box for organizations
- You have to click outside of the `Tags` box for users

### Adding an existing tag to an object

To add an existing tag to an object, navigate to the object, click on the `Tags` box, and start typing your tag. Zendesk will show existing tags that match what you are typing in a drop-down. Once you see the tag you wish to use, click on it.

Once you update the object in question, the tag will then be added to said object.

### Removing a tag from an object

To remove an existing tag from an object, navigate to the object, locate the `Tags` box, and click the `x` symbol to the right of the tag you wish to remove.

Once you update the object in question, the tag will then be removed from said object.

## Tag list generator

This covers the projects that populate the [Zendesk Tags Google sheet](https://docs.google.com/spreadsheets/d/1VUaXLcE3L--uBhKi2VrNk8wzaslkydF5AMTMsJMiQpU/edit?usp=sharing) (internal access only). It only covers tags from Zendesk items and those we manually set as external tags (custom tags added by agents are not present).

{{% alert title="Technical Details" color="primary" %}}

- Deployment type: `Standard`
- Projects:
  - [Zendesk Global](https://gitlab.com/gitlab-support-readiness/zendesk-global/tickets/tag-list-generator)
  - [Zendesk US Government](https://gitlab.com/gitlab-support-readiness/zendesk-us-government/tickets/tag-list-generator)

{{% /alert %}}

### How it works

When the script runs, it begins by gathering all Zendesk automations, macros, organization fields, ticket fields, triggers, and user fields from the Zendesk instance it is populating the sheet for. With those, it reviews each item to locate the use of tags and stores said tags to an array (via a hash object pointing to where it came from).

The script then reads the `data/external_tags.yaml` file to load tags not contained in standard Zendesk items (such as items from the agent sync, ticket processors, etc.) and adds them to the array of tags.

With this list in hand, the script removes all content from the relevant Google sheet (in case there are less items on the current run than a previous run). Once cleared, the script then adds all tag data to the Google sheet.

### Requesting a manual tag be added

To request manually made tags be added to the Google sheet, please create a [Feature Request issue](https://gitlab.com/gitlab-com/eta/css/issue-tracker/-/issues/new?description_template=Feature) (as it will require manual intervention by the Customer Support Systems team).

### How to add new tags to it

{{% alert title="Note" color="primary" %}}

- This action requires `Developer` level access to the project in question.
- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).

{{% /alert %}}

Given the way it works, the only time you would need add tags to the process would be if they were external tags. That being the case, you would add a new entry to the `data/external_tags.yaml` file (via a MR), using the format:

```yaml
- tag: 'Tag name to add'
  source: 'Source of tag'
```

After a peer reviews and approves your MR, you can merge the MR. When the next deployment occurs, it will be synced to Zendesk.

### How to remove tags from it

{{% alert title="Note" color="primary" %}}

- All sections in this section require `Administrator` level access to Zendesk.

{{% /alert %}}

The only tags that can be removed from it would be external tags (as the rest stem from Zendesk items and would be automatically removed if said item using the tag was removed). Being those are managed via the `data/external_tags.yaml` file, you will need to create a MR to remove the entry in question.

After a peer reviews and approves your MR, you can merge the MR. When the next deployment occurs, it will be synced to Zendesk.

### Performing an exception deployment

To perform an exception deployment for the tag list generator, navigate to the tag list generator project in question, go to the scheduled pipelines page, and click the play button for the sync item. This will trigger a sync job for the tag list generator.

## Common issues and troubleshooting

### Not seeing a tag listed in the sheet after a merge

As the tag list generator follows the `Standard` deployment type, they would only be deployed during a normal deployment cycle (or when an exception deployment has been done).
