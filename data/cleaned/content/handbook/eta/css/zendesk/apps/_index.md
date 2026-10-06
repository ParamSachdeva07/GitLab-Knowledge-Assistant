---
title: 'Apps'
description: 'Documentation on Zendesk apps'
---

This guide covers information and management of Zendesk apps at GitLab.

For a list of currently used apps:

- [Zendesk Global](./global/)
- [Zendesk US Government](./us-government/)

Developers should review the [Development documentation](./development/).

Administrators should review the [Administrator tasks](#administrator-tasks) section.

{{% alert title="Technical Details" color="primary" %}}

- Deployment type: `Standard`
- Groups sync repos are in:
  - [Zendesk Global](https://gitlab.com/gitlab-support-readiness/zendesk-global/apps)
  - [Zendesk US Government](https://gitlab.com/gitlab-support-readiness/zendesk-us-government/apps)

{{% /alert %}}

## Understanding Zendesk apps

### What is a Zendesk App

A Zendesk App is an application (written in HTML/CSS/JS) that runs in a location of Zendesk. What it does and how it does it varies greatly from application to application. Applications can be run in a great many places, but the traditional locations are:

- Ticket sidebar
- User sidebar
- Organization sidebar
- Navbar
- Background

You can see more resources on application locations via the [Zendesk Developer Manifest Reference documentation](https://developer.zendesk.com/documentation/apps/app-developer-guide/manifest/#location).

Zendesk applications tend to come from one of two areas:

- [Zendesk Marketplace](https://www.zendesk.com/apps/)
- Developed in-house

### How we manage apps

While Zendesk offers a full way to manage apps via the UI, we turn to a more version controlled methodology. This allows for a set review process, the ability to perform rollbacks as needed, etc.

That being the case, we utilize sync repos and managed content repos.

## Administrator tasks

### Versioning

For Zendesk app version, you use the following style:

`Major.Minor`

This follows [Semantic Versioning](https://www.geeksforgeeks.org/software-engineering/introduction-semantic-versioning/) (without the `Patch` number). As such, you should combine the normal `Minor` and `Patch` definitions into one.

As a general rule:

- Minor version changes (increment Minor number):
  - Bug fixes and corrections
  - Small UI improvements
  - Performance optimizations
  - Minor feature additions
- Major version changes (increment Major, reset Minor to 0):
  - Breaking changes to functionality
  - Major redesigns or rewrites
  - Significant new features
  - Changes requiring new permissions

As an example:

- doing small changes on app version `2.9` would make the new version `2.10`
- doing large changes on app version `2.9` would make the new version `3.0`

### Installing an app

{{% alert title="Info" color="info" %}}

- This covers installing the app in Zendesk.
  - If you need to create the app project, please see [project setup](/handbook/eta/css/gitlab/project-setup)
  - If you need to develop the app, please see [App development](./development/)
- If installing an app from the Zendesk marketplace, please see directions on that app's page.

{{% /alert %}}
{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).

{{% /alert %}}

To install an app in Zendesk, you first must package your app. To do this, run the following command (via CLI) within the project repo:

```bash
zip -r data/application.zip assets manifest.json translations
```

You will then use `data/application.zip` to upload (and install) the app in Zendesk by doing the following:

1. Navigate to the admin dashboard for the Zendesk instance
   - [Zendesk Global (production)](https://gitlab.zendesk.com/admin/home)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/home)
   - [Zendesk US Government (production)](https://gitlab-federal-support.zendesk.com/admin/home)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/home)
1. Go to `Apps and integrations > Apps > Zendesk Support apps`
   - [Zendesk Global](https://gitlab.zendesk.com/admin/apps-integrations/apps/support-apps)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/apps-integrations/apps/support-apps)
   - [Zendesk US Government](https://gitlab-federal-support.zendesk.com/admin/apps-integrations/apps/support-apps)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/apps-integrations/apps/support-apps)
1. Click `Upload private app` in the top-right of the page
1. Enter the app's name (as it is detailed in the app's `manifest.json` file)
1. Click `Choose File` and select the `data/application.zip` file made previously
1. Click `Upload`

From there, you will be taken to the app's page (after install), where you can set the restrictions, parameters, etc.

### Updating an app

{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).
- Make sure you follow our [Versioning](#versioning) information

{{% /alert %}}

Updating already installed apps is considerably easier since a corresponding sync repo controls it. To update an app, you will need to create a MR in the sync repo for the app. The exact changes being made will depend on the request itself.

After a peer reviews and approves your MR, you can merge the MR. When the next deployment occurs, it will be synced to Zendesk.

#### Force updating an installed app in the sandbox

If you need to force update an app in the sandbox (especially during development), run the command `./bin/sync_sandbox force` when within the project repo (via CLI).

### Deactivating an app

{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).
- If deactivating an app, you will need to disable the scheduled pipelines that control its sync mechanism

{{% /alert %}}

To deactivate an app:

1. Navigate to the admin dashboard for the Zendesk instance
   - [Zendesk Global (production)](https://gitlab.zendesk.com/admin/home)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/home)
   - [Zendesk US Government (production)](https://gitlab-federal-support.zendesk.com/admin/home)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/home)
1. Go to `Apps and integrations > Apps > Zendesk Support apps`
   - [Zendesk Global](https://gitlab.zendesk.com/admin/apps-integrations/apps/support-apps)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/apps-integrations/apps/support-apps)
   - [Zendesk US Government](https://gitlab-federal-support.zendesk.com/admin/apps-integrations/apps/support-apps)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/apps-integrations/apps/support-apps)
1. Hover over the app in question and click the down arrow
1. Click the slider under the `Enabled` option

### Uninstalling an app

{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).
- You should only ever uninstall a deactivated app

{{% /alert %}}

To uninstall an app:

1. Navigate to the admin dashboard for the Zendesk instance
   - [Zendesk Global (production)](https://gitlab.zendesk.com/admin/home)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/home)
   - [Zendesk US Government (production)](https://gitlab-federal-support.zendesk.com/admin/home)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/home)
1. Go to `Apps and integrations > Apps > Zendesk Support apps`
   - [Zendesk Global](https://gitlab.zendesk.com/admin/apps-integrations/apps/support-apps)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/apps-integrations/apps/support-apps)
   - [Zendesk US Government](https://gitlab-federal-support.zendesk.com/admin/apps-integrations/apps/support-apps)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/apps-integrations/apps/support-apps)
1. Hover over the app in question and click the down arrow
1. Click `Uninstall`

### Performing an exception deployment

To perform an exception deployment for an app, navigate to the app project in question, go to the scheduled pipelines page, and click the play button for the sync item. This will trigger a sync job for the app.

## Common issues and troubleshooting

### Not seeing app changes after a merge

As apps follow the `Standard` deployment type, they would only be deployed during a normal deployment cycle (or when an exception deployment has been done).
