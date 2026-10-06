---
title: 'Themes'
description: 'Documentation on Zendesk themes'
---

This guide covers how to create, edit, and manage Zendesk themes at GitLab. Administrators should review the [Administrator tasks](#administrator-tasks) section.

{{% alert title="Technical Details" color="primary" %}}

- Deployment type: `Standard`
- Sync repos
  - [Zendesk Global](https://gitlab.com/gitlab-support-readiness/zendesk-global/theme)
  - [Zendesk US Government](https://gitlab.com/gitlab-support-readiness/zendesk-us-government/theme)

{{% /alert %}}
{{% alert title="Danger" color="danger" %}}

- Never directly modify themes in the Zendesk UI in any instance (sandbox or production). You will severely break the entire setup if you do (and it is not easy to fix).
- This is a very customer facing item. Exercise caution in making changes and ensure you thoroughly review a preview of the changes in the sandbox.
- We are looking to revamp and change how we work with themes in FY27. See [gitlab-com/gl-security/corp/cust-support-ops/issue-tracker#752](https://gitlab.com/gitlab-com/gl-security/corp/cust-support-ops/issue-tracker/-/issues/752) and [gitlab-com/gl-security/corp/cust-support-ops/issue-tracker#727](https://gitlab.com/gitlab-com/gl-security/corp/cust-support-ops/issue-tracker/-/issues/727) for more information.

{{% /alert %}}

## Understanding themes

### What are themes

A theme is a set of files that determine what your support portal looks like.

### How we manage themes

While Zendesk offers a full way to manage themes via the UI, we turn to a more version controlled methodology. This allows for a set review process, the ability to perform rollbacks as needed, etc.

That being the case, we utilize sync repos.

## Creating a theme as a non-admin

For the creation of a theme, please create a [Feature Request issue](https://gitlab.com/gitlab-com/eta/css/issue-tracker/-/issues/new?description_template=Feature) (as it will require manual intervention by the Customer Support Systems team).

## Editing a theme as a non-admin

For the modification of a theme, please create a [Feature Request issue](https://gitlab.com/gitlab-com/eta/css/issue-tracker/-/issues/new?description_template=Feature) (as it will require manual intervention by the Customer Support Systems team).

## Changing the live theme as a non-admin

To change the live theme, please create a [Feature Request issue](https://gitlab.com/gitlab-com/eta/css/issue-tracker/-/issues/new?description_template=Feature) (as it will require manual intervention by the Customer Support Systems team).

## Deleting a theme as a non-admin

To request the deletion of a theme, please create a [Feature Request issue](https://gitlab.com/gitlab-com/eta/css/issue-tracker/-/issues/new?description_template=Feature) (as it will require manual intervention by the Customer Support Systems team).

## Administrator tasks

{{% alert title="Note" color="primary" %}}

- All sections in this section require `Administrator` level access to Zendesk.

{{% /alert %}}

### Viewing themes in Zendesk

To view the themes in Zendesk:

1. [Access the knowledge center](../knowledge-center/#accessing-the-knowledge-center)
1. Click the `Customize design` icon on the left side:
   - For the primary brand:
     - [Zendesk Global (production)](https://gitlab.zendesk.com/theming/workbench)
     - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/theming/workbench)
     - [Zendesk US Government (production)](https://gitlab-federal-support.zendesk.com/theming/workbench)
     - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/theming/workbench)
   - For the internal brand:
     - [Zendesk Global (production)](https://gitlab-internal.zendesk.com/theming/workbench)
     - [Zendesk Global (sandbox)](https://gitlab1707170878-internal.zendesk.com/theming/workbench)
     - [Zendesk US Government (production)](https://gitlab-federal-internal.zendesk.com/theming/workbench)
     - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082-internal.zendesk.com/theming/workbench)

### Creating a theme

{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).
- This can dramatically impact the usability and appearance of what our customers see when they use the support portal. Exercise caution in proceeding.

{{% /alert %}}

This is a very complex process to integrate into our systems. As such, please have a Fullstack Engineer for the Customer Support Systems team assist you in this. It is a very manual process.

### Editing a theme

{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).
- This can dramatically impact the usability and appearance of what our customers see when they use the support portal. Exercise caution in proceeding.
- It is _vital_ you follow the [Versioning information](#versioning-information). Not doing so can cause things to break severely.

{{% /alert %}}

To edit a theme, you will need to create a MR in the sync repo. The exact changes being made will depend on the request itself, but make sure to use our [Versioning information](#versioning-information) in your changes.

Once the MR is created, a preview link will be generated in the MR comments. This link allows you to preview theme changes before merging. If you push new commits to your MR, a new preview link will be generated.

After a peer reviews and approves your MR, you can merge the MR.

Once merged, any preview themes generated (for preview links) will be deleted via automation from the system. Once that completes, it will fully merge into the default branch.

When the next deployment occurs, it will be synced to Zendesk.

#### Versioning information

{{% alert title="Quick versioning guide" color="primary" %}}

- First digit: Always matches `api_version` (currently 4)
- Second digit: Increment when creating new MR
- Third digit: Start at 0, increment for each commit to same MR

{{% /alert %}}

It is vital for the theme that we use the correct versioning style. The version itself stems from the `data/theme/manifest.json` file's `version` attribute. It uses 3 digits separated by a period. When making changes, keep the meaning of these digits in mind:

- The first digit: should always match the `api_version` attribute
- The second digit: when creating a new MR, you should take the previous value and add 1 to it
- The third digit:
  - when creating a new MR, it should be `0` (see [Example 1](#example-1))
  - If you push new changes to the MR after creation, you should add 1 to it (see [Example 2](#example-2))

##### Example 1

You need to perform changes to the theme, so you develop them and then create a new MR. The `data/theme/manifest.json` file had the following in it before you made any changes:

```plaintext
{
  "name": "GitLab Zendesk Global Theme",
  "author": "Jason Colyer",
  "version": "4.0.39",
  "api_version": 4,
  "default_locale": "en-us",
```

Since you are creating a new MR, the new value should look like this:

```plaintext
{
  "name": "GitLab Zendesk Global Theme",
  "author": "Jason Colyer",
  "version": "4.1.0",
  "api_version": 4,
  "default_locale": "en-us",
```

If, after creation, you needed to push new changes to the MR, the new value should look like this:

```plaintext
{
  "name": "GitLab Zendesk Global Theme",
  "author": "Jason Colyer",
  "version": "4.1.1",
  "api_version": 4,
  "default_locale": "en-us",
```

##### Example 2

You are working with a peer on an existing MR for theme changes. After your development, you decide to push changes to the existing MR. The `data/theme/manifest.json` file had the following in it before you made any changes:

```plaintext
{
  "name": "GitLab Zendesk US Government Theme",
  "author": "Jason Colyer",
  "version": "4.10.9",
  "api_version": 4,
  "default_locale": "en-us",
```

Since the MR already existed and you are pushing new changes, the new value should look like this:

```plaintext
{
  "name": "GitLab Zendesk US Government Theme",
  "author": "Jason Colyer",
  "version": "4.10.10",
  "api_version": 4,
  "default_locale": "en-us",
```

### Changing the live theme

{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).
- This can dramatically impact the usability and appearance of what our customers see when they use the support portal. Exercise caution in proceeding.

{{% /alert %}}

This is a very complex process to integrate into our systems. As such, please have a Fullstack Engineer for the Customer Support Systems team assist you in this. It is a very manual process.

### Deleting a theme

{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).
- This can dramatically impact the usability and appearance of what our customers see when they use the support portal. Exercise caution in proceeding.
- You cannot delete the current live theme.

{{% /alert %}}

If deleting a non-live theme, you may proceed as normal. To do this:

1. [Navigate the themes listing](#viewing-themes-in-zendesk)
1. Locate the theme in question and click the three vertical dots to the right side of it
1. Click `Delete`
1. Click `Delete theme` to confirm the deletion

### Performing an exception deployment

To perform an exception deployment for themes, navigate to the themes sync project in question, go to the scheduled pipelines page, and click the play button for the sync item. This will trigger a sync job for the themes.

## Common issues and troubleshooting

### Not seeing theme changes after a merge

As themes follow the `Standard` deployment type, they would only be deployed during a normal deployment cycle (or when an exception deployment has been done)
