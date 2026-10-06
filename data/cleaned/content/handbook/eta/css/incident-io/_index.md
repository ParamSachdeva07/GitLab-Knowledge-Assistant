---
title: 'Incident.io'
description: 'Documentation on Incident.io'
---

{{% alert title="Technical Details" color="primary" %}}

- Deployment type: `Ad-hoc`

{{% /alert %}}

## Understanding Incident.io

### What is Incident.io

As per the description on Incident.io's [homepage](https://incident.io/):

> incident.io is an all-in-one incident management platform unifying on-call scheduling, real-time incident response, and integrated status pages – helping teams resolve issues faster and reduce downtime.

### How we manage items in Incident.io

We currently manage all Incident.io items within Incident.io itself.

### Accessing the Customer Support Systems status page

To access our status page:

1. Navigate to the status page at https://statuspage.incident.io/cust-support-ops/main
1. Enter your work email
   - Note this does require the use of a gitlab.com email address for authentication
1. Check your email inbox
   - Subject should be `Log in to Customer Support Operations`
1. Click the `Log in to Customer Support Operations status page` button

## Customer Support Systems setup

### Components catalog

<sup>Source: [Customer Support Operations components](https://app.incident.io/gitlab/catalog/01JXZ8QTFEYF84RP0V80MG1VAP)</sup>

These reflect the items that can have incidents or maintenances on them. Think of it as the items within a status page itself.

Due to the extensive list of items contained in this, please see the source link above.

### Groups catalog

<sup>Source: [Customer Support Operations groups](https://app.incident.io/gitlab/catalog/01JXZ8X7HVN23T3773PGXB5NNR)</sup>

These are items that group together components.

We currently only utilize one group:

- `Main`

### Status page

<sup>Source: [Customer Support Operations Status](https://app.incident.io/gitlab/status-pages/01JXZ9CT4V8HHVJYJDP7XY7B4T/overview/now)</sup>

This is our actual status page. It uses the [group](#groups-catalog) (and the [components](#components-catalog) within said group).

- Basic settings
  - Basic settings
    - Page title: `Customer Support Operations`
    - Base URL: https://statuspage.incident.io/cust-support-ops
  - Customization
    - Support URL: none
    - Google Analytics tag: none
    - Privacy policy: none
    - Terms of service: none
- Customer pages
  - Customer pages
    - [Customer Support Operations for Main](https://statuspage.incident.io/cust-support-ops/main)
  - Disabled sub-pages: none
- Page setup
  - Theming
    - Dark mode
    - Date view: Calendar
- Components
  - Component uptimes: Coloured bars and uptime percentage
- Custom domain
  - Custom domain: none

## Administrator tasks

{{% alert title="Warning" color="warning" %}}

- All tasks should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).
- All tasks are tailored specifically to the Customer Support Systems team and do not reflect how other teams may perform their administrator tasks

{{% /alert %}}

### Managing component catalogs

#### Creating a component catalog

As we manage all Incident.io items within Incident.io itself, you will need to create the component catalog in the system itself. To create a component catalog:

1. Login to Incident.io (via Okta)
1. Go to [Catalog](https://app.incident.io/gitlab/catalog)
1. Click [Add a custom type](https://app.incident.io/gitlab/catalog/create)
1. Enter a `Name`
1. Enter a `Description`
1. Under `Categories` click `+ Services`
1. Ensure `Are entries of this type ranked?` checkbox is checked
1. Ensure `Reference entries by name` checkbox is checked
1. Click `Save` at bottom-right

#### Editing a component catalog

As we manage all Incident.io items within Incident.io itself, you will need to edit the component catalog in the system itself. To edit a component catalog:

1. Login to Incident.io (via Okta)
1. Go to [Catalog](https://app.incident.io/gitlab/catalog)
1. Click the component catalog to edit
1. Click `Edit type` at the top-right of the page
1. Make the needed changes
1. Click `Save` at bottom-right

#### Adding a component to a component catalog

As we manage all Incident.io items within Incident.io itself, you will need to add the component to the component catalog in the system itself. To to add the component to the component catalog:

1. Login to Incident.io (via Okta)
1. Go to [Catalog](https://app.incident.io/gitlab/catalog)
1. Click the component catalog to add a component to
1. Click `Create entry` at the top-right of the page
1. Enter the `Name` of the new component
1. Click `Create` at bottom-right

#### Deleting a component catalog

As we manage all Incident.io items within Incident.io itself, you will need to delete the component catalog in the system itself. To delete a component catalog:

1. Login to Incident.io (via Okta)
1. Go to [Catalog](https://app.incident.io/gitlab/catalog)
1. Click [Add a custom type](https://app.incident.io/gitlab/catalog/create)
1. Click the component catalog to delete
1. Click `Delete type` at the top-right of the page
1. Type the name of the component catalog you are deleting in the text box of the popup modal
1. Click `Continue` at bottom-right of the popup modal

### Managing group catalogs

#### Creating a group catalog

This is the same process as [Creating a component catalog](#creating-a-component-catalog).

#### Editing a group catalog

This is the same process as [Editing a component catalog](#editing-a-component-catalog).

#### Adding a group to a group catalog

As we manage all Incident.io items within Incident.io itself, you will need to add the group to the group catalog in the system itself. To to add the group to the group catalog:

1. Login to Incident.io (via Okta)
1. Go to [Catalog](https://app.incident.io/gitlab/catalog)
1. Click the component catalog to add a group to
1. Click `Create entry` at the top-right of the page
1. Enter the `Name` of the new component
1. Populate the list of components for the group in the `Components` area
1. Enter an `Email domain` of `gitlab.com`
1. Click `Create` at bottom-right

#### Adding a component to a group catalog

This is done by [Editing a group](#editing-a-group).

#### Deleting a group catalog

This is the same process as [Deleting a component catalog](#deleting-a-component-catalog).

### Managing groups

#### Creating a group

This is done by [Adding a group to a group catalog](#adding-a-group-to-a-group-catalog).

#### Editing a group

As we manage all Incident.io items within Incident.io itself, you will need to edit the group in the system itself. To edit the group:

1. Login to Incident.io (via Okta)
1. Go to [Catalog](https://app.incident.io/gitlab/catalog)
1. Click the catalog the group is within
1. Locate the group to edit in question and click on it
1. Click the pencil icon in the top-right of the right-hand sidebar
1. Make your changes
1. Click `Save` on the bottom-right of the right-hand sidebar

#### Deleting a group

As we manage all Incident.io items within Incident.io itself, you will need to delete the group in the system itself. To delete a group:

1. Login to Incident.io (via Okta)
1. Go to [Catalog](https://app.incident.io/gitlab/catalog)
1. Click the catalog the group is within
1. Locate the group to edit in question and click on it
1. Click the trashcan icon in the top-right of the right-hand sidebar
1. Click the `Confirm` button to confirm the deletion

### Managing components

{{% alert title="Warning" color="warning" %}}

- All components we use should align with the item in [Customer Support Systems Criticality](/handbook/eta/css/criticalities/#customer-support-systems-system-criticality).

{{% /alert %}}

#### Creating a component

This is done by [Adding a component to a component catalog](#adding-a-component-to-a-component-catalog).

#### Editing a component

As we manage all Incident.io items within Incident.io itself, you will need to edit the component in the system itself. To edit the component:

1. Login to Incident.io (via Okta)
1. Go to [Catalog](https://app.incident.io/gitlab/catalog)
1. Click the catalog the component is within
1. Locate the component to edit in question and click on it
1. Click the pencil icon in the top-right of the right-hand sidebar
1. Make your changes
1. Click `Save` on the bottom-right of the right-hand sidebar

#### Deleting a component

As we manage all Incident.io items within Incident.io itself, you will need to delete the component in the system itself. To delete the component:

1. Login to Incident.io (via Okta)
1. Go to [Catalog](https://app.incident.io/gitlab/catalog)
1. Click the catalog the component is within
1. Locate the component to edit in question and click on it
1. Click the trashcan icon in the top-right of the right-hand sidebar
1. Click the `Confirm` button to confirm the deletion

### Managing status pages

#### Creating a status page

As we manage all Incident.io items within Incident.io itself, you will need to create the status page in the system itself. To create the status page:

1. Login to Incident.io (via Okta)
1. Go to [Status pages](https://app.incident.io/gitlab/status-pages)
1. Click [Create customer page](https://app.incident.io/gitlab/status-pages/customer/create)
1. Enter a `Page title`
1. Enter `Status page URL` (if you want to change the auto-generated one)
1. Under `Customer pages`
   - Click `Use an existing catalog type`
   - Set `Which catalog type defines the customers you'd like to create?` to the group catalog you wish to use
   - Set `Which catalog attribute represents your components?` to `Components`
   - Set `Which catalog attribute represents allowed email domains?` to `Email domains`
1. Under `Pages`
   - Set the `Page name`
   - Set the `URL`
1. Under `Page setup`
   - Set `Theming` to `Dark mode`
   - Select a `Company logo` (if desired)
   - Select a `Favicon` (if desired)
1. Click `Create status page` at the bottom-right of the page

#### Editing a status page

As we manage all Incident.io items within Incident.io itself, you will need to edit the status page in the system itself. To edit the status page:

1. Login to Incident.io (via Okta)
1. Go to [Status pages](https://app.incident.io/gitlab/status-pages)
1. Click the name of the status page to edit
1. Click the `Settings` tab
1. Make the changes needed for the section you need to change (and click `Save` to implement the changes)

#### Adding a component to a status page

This is done by [Adding a component to a group catalog](#adding-a-component-to-a-group-catalog).

#### Deleting a status page

As we manage all Incident.io items within Incident.io itself, you will need to delete the status page in the system itself. To delete the status page:

1. Login to Incident.io (via Okta)
1. Go to [Status pages](https://app.incident.io/gitlab/status-pages)
1. Click the name of the status page to edit
1. Click the `Settings` tab
1. Scroll to the bottom of the page and click `Delete status page`
1. Type the name of your status page
1. Click `Delete status page`

### Managing incidents

#### Creating an incident

To create an incident:

1. Login to Incident.io (via Okta)
1. Navigate to [Status pages](https://app.incident.io/gitlab/status-pages)
1. Click on the status page you want to make an incident on
1. Click `Publish incident` at the top-right
1. Fill out a meaningful `Name`
1. Set the `Status` of the incident
   - Investigating: Report an incident
     - This is normally what you would use as the starting point
   - Identified: Problem has been determined and a fix is being made
   - Monitoring: Fix is implemented and we are monitoring the situation
   - Resolved: Everything is good to go
1. Set a meaningful `Message` for the incident
   - You should include a link to your incident issue here
1. Set the level of impact on `Affected components` (the value needed depends on the impact of the incident)
   - No impact: The incident does not impact this component
   - Degraded performance: The component is working but at lower than standard performance levels
   - Partial outage: Significant parts of the component are not working
   - Full outage: The component is hard down
1. Click `Review incident`
1. Review all information for accuracy
1. Click `Publish incident`

#### Updating an incident

To update an incident:

1. Login to Incident.io (via Okta)
1. Navigate to [Status pages](https://app.incident.io/gitlab/status-pages)
1. Click on the status page the incident is on
1. Click on the incident in question
1. Click the top-right status bar (says what the current status is)
1. Select the new `Status`
   - Identified: Problem has been determined and a fix is being made
   - Monitoring: Fix is implemented and we are monitoring the situation
   - Resolved: Everything is good to go
1. Enter a meaningful message
1. Click `Review update`
1. Review all information for accuracy
1. Click `Publish update`

### Managing maintenance

#### Creating a maintenance event

To create a maintenance event:

1. Login to Incident.io (via Okta)
1. Navigate to [Status pages](https://app.incident.io/gitlab/status-pages)
1. Click on the status page you want to make an incident on
1. Click on `Maintenance`
1. Click `Schedule maintenance` at the top-right of the page
1. Fill out a meaningful `Name`
1. Ensure `Automatically update status` is checked
1. Set the `Impact window` (keep in mind it is using local time)
1. Set a meaningful `Message`
1. Set the level of impact on `Affected components`
   - No impact: The maintenance does not impact this component
   - Under maintenance: The maintenance does impact this component
1. Click `Review`
1. Review all information for accuracy
1. Click `Publish maintenance`

#### Updating a maintenance event

To update a maintenance event:

1. Login to Incident.io (via Okta)
1. Navigate to [Status pages](https://app.incident.io/gitlab/status-pages)
1. Click on the status page you want to make an incident on
1. Click on `Maintenance`
1. Click the maintenance in question
1. Click the top-right status bar (says what the current status is)
1. Select the new `Status`
1. Enter a meaningful message
1. Click `Review update`
1. Review all information for accuracy
1. Click `Publish update`
