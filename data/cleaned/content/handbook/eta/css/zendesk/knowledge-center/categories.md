---
title: 'Categories'
description: 'Documentation on Zendesk categories'
---

This guide covers how to create, edit, and manage Zendesk categories at GitLab. Administrators should review the [Administrator tasks](#administrator-tasks) section.

{{% alert title="Technical Details" color="primary" %}}

- Deployment type: `Standard`
- Sync repos
  - [Zendesk Global](https://gitlab.com/gitlab-support-readiness/zendesk-global/help-center-categories)
  - [Zendesk US Government](https://gitlab.com/gitlab-support-readiness/zendesk-us-government/help-center-categories)
- `CustSuppOps Zendesk Test Suite Generator` enabled

{{% /alert %}}

## Understanding categories

### What are categories

As per [Zendesk](https://support.zendesk.com/hc/en-us/articles/4408845897370-Organizing-knowledge-base-content-in-categories-and-sections#topic_hjs_tl4_kk):

> Categories are the top-level organizing containers of the help center. Categories contain sections. The help center must have at least one category. If you have only one category in your help center, then the category itself is hidden to end users, and they see only the sections in your help center.

The knowledge center uses a three-level structure:

- **Categories** (top level) - Organize major topic areas, documented on this page
- **Sections** (middle level) - Subdivide categories into related groups, documented on [sections page](/handbook/eta/css/zendesk/knowledge-center/sections)
- **Articles** (content level) - Individual help articles, documented on [articles page](/handbook/eta/css/zendesk/knowledge-center/articles)

### How we manage categories

While Zendesk offers a full way to manage categories via the UI, we turn to a more version controlled methodology. This allows for a set review process, the ability to perform rollbacks as needed, etc.

That being the case, we utilize sync repos.

## Current categories in use

- Zendesk Global
  - [About GitLab Support](https://support.gitlab.com/hc/en-us/categories/19831379587100-About-GitLab-Support)
  - [Knowledge articles](https://support.gitlab.com/hc/en-us/categories/360002276159-Knowledge-Articles)
- Zendesk US Government
  - [About GitLab Support](https://federal-support.gitlab.com/hc/en-us/categories/37060125978004-About-GitLab-Support)
  - [Knowledge articles](https://support.gitlab.com/hc/en-us/categories/360002276159-Knowledge-Articles)

## Creating a category as a non-admin

For the creation of a category, please create a [Feature Request issue](https://gitlab.com/gitlab-com/eta/css/issue-tracker/-/issues/new?description_template=Feature) (as it will require manual intervention by the Customer Support Systems team).

## Editing a category as a non-admin

For the modification of a category, please create a [Feature Request issue](https://gitlab.com/gitlab-com/eta/css/issue-tracker/-/issues/new?description_template=Feature) (as it will require manual intervention by the Customer Support Systems team).

## Deleting a category as a non-admin

To request the deactivation of a category, please create a [Feature Request issue](https://gitlab.com/gitlab-com/eta/css/issue-tracker/-/issues/new?description_template=Feature) (as it will require manual intervention by the Customer Support Systems team).

## Administrator tasks

{{% alert title="Note" color="primary" %}}

- All sections in this section require `Administrator` level access to Zendesk.

{{% /alert %}}

### Viewing categories in Zendesk

To see the current categories in Zendesk:

1. Navigate to the knowledge center dashboard for the Zendesk instance
   - For the primary brand:
     - [Zendesk Global (production)](https://gitlab.zendesk.com/knowledge/lists/default/1/1?brand_id=3252896)
     - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/knowledge/lists/default/1/1?brand_id=12510498177436)
     - [Zendesk US Government (production)](https://gitlab-federal-support.zendesk.com/knowledge/lists/default/1/1?brand_id=360002482351)
     - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/knowledge/lists/default/1/1?brand_id=360003799392)
   - For the internal brand:
     - [Zendesk Global (production)](https://gitlab.zendesk.com/knowledge/lists/default/1/1?brand_id=22781249167132)
     - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/knowledge/lists/default/1/1?brand_id=22687153149724)
     - [Zendesk US Government (production)](https://gitlab-federal-support.zendesk.com/knowledge/lists/default/1/1?brand_id=41824350085780)
     - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/knowledge/lists/default/1/1?brand_id=41389709130900)
1. Click the `Arrange content` icon on the left side
   - For the primary brand:
     - [Zendesk Global (production)](https://gitlab.zendesk.com/knowledge/arrange/?brand_id=3252896)
     - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/knowledge/arrange/?brand_id=12510498177436)
     - [Zendesk US Government (production)](https://gitlab-federal-support.zendesk.com/knowledge/arrange/?brand_id=360002482351)
     - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/knowledge/arrange/?brand_id=360003799392)
   - For the internal brand:
     - [Zendesk Global (production)](https://gitlab.zendesk.com/knowledge/lists/arrange/?brand_id=22781249167132)
     - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/knowledge/lists/arrange/?brand_id=22687153149724)
     - [Zendesk US Government (production)](https://gitlab-federal-support.zendesk.com/knowledge/lists/arrange/?brand_id=41824350085780)
     - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/knowledge/lists/arrange/?brand_id=41389709130900)

### Creating a category

{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).
- **SEO Impact:** Categories affect URL structure, search indexing, and article discoverability. Changing category names or structure can break existing links and impact search engine rankings.
- Exercise caution if you make changes to categories.

{{% /alert %}}

For the creation of a category, you will need to create a MR in the sync repo. The exact changes being made will depend on the request itself. A starting template you can use would be:

```yaml
---
name: 'Your category name here'
previous_name: 'Your category name here'
description: 'Your description here'
locale: 'en-us' # This should always be used
position: 0 # Integer representing category display order
source_locale: 'en-us' # This should always be used
```

After a peer reviews and approves your MR, you can merge the MR. When the next deployment occurs, it will be synced to Zendesk.

### Editing a category

{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).
- **SEO Impact:** Categories affect URL structure, search indexing, and article discoverability. Changing category names or structure can break existing links and impact search engine rankings.
- Exercise caution if you make changes to categories.

{{% /alert %}}

To edit a category, you will need to create a MR in the sync repo. The exact changes being made will depend on the request itself.

After a peer reviews and approves your MR, you can merge the MR. When the next deployment occurs, it will be synced to Zendesk.

#### Changing the name of a category

If you need to change the name of a category, copy the current value into the `previous_name` attribute and then change the `name` attribute. This allows the sync to still locate the category in question to update.

### Deleting a category

{{% alert title="Danger" color="danger" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).
- When you delete a category, all the sections contained in the category are also deleted, and all the articles (including any translations) contained in the sections are archived.
- Exercise extreme caution in doing this.

{{% /alert %}}

As the sync repos do not perform deletions, you will have to do 2 actions to delete a category.

First, you must delete the corresponding file from the sync repo. After a peer reviews and approves your MR, you can merge the MR.

After that is done, you then must delete it from Zendesk itself.

To delete a category from Zendesk:

1. [Navigate to the category list](#viewing-categories-in-zendesk)
1. Click the three vertical dots to the right of the category you wish to delete
1. Click the `Edit category`
1. Click `Delete category` on the left-hand side
1. Click `OK` to confirm the change

### Performing an exception deployment

To perform an exception deployment for categories, navigate to the categories sync project in question, go to the scheduled pipelines page, and click the play button for the sync item. This will trigger a sync job for the categories.

## Common issues and troubleshooting

### Not seeing category changes after a merge

As categories follow the `Standard` deployment type, they would only be deployed during a normal deployment cycle (or when an exception deployment has been done)
