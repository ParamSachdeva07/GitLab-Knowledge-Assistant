---
title: 'Sections'
description: 'Documentation on Zendesk sections'
---

This guide covers how to create, edit, and manage Zendesk sections at GitLab. Administrators should review the [Administrator tasks](#administrator-tasks) section.

{{% alert title="Technical Details" color="primary" %}}

- Deployment type: `Standard`
- Sync repos
  - [Zendesk Global](https://gitlab.com/gitlab-support-readiness/zendesk-global/sections)
  - [Zendesk US Government](https://gitlab.com/gitlab-support-readiness/zendesk-us-government/sections)
- `CustSuppOps Zendesk Test Suite Generator` enabled

{{% /alert %}}

## Understanding sections

### What are sections

As per [Zendesk](https://support.zendesk.com/hc/en-us/articles/4408845897370-Organizing-knowledge-base-content-in-categories-and-sections#topic_ysj_wtt_zz):

> Sections contain related articles.

Essentially, they are items used to subdivide categories into related groups.

The knowledge center uses a three-level structure:

- **Categories** (top level) - Organize major topic areas, documented on [categories page](/handbook/eta/css/zendesk/knowledge-center/categories)
- **Sections** (middle level) - Subdivide categories into related groups, documented on this page
- **Articles** (content level) - Individual help articles, documented on [articles page](/handbook/eta/css/zendesk/knowledge-center/articles)

### How we manage sections

We currently manage all sections within Zendesk itself.

**Note:** Section management via sync repos (similar to categories) is planned for future implementation in FY27.

## Current sections in use

- Zendesk Global
  - Under the [About GitLab Support](https://support.gitlab.com/hc/en-us/categories/19831379587100-About-GitLab-Support) category:
    - [Support Pages](https://support.gitlab.com/hc/en-us/sections/360004459140)
  - Under the [Knowledge articles](https://support.gitlab.com/hc/en-us/categories/360002276159-Knowledge-Articles) category:
    - [Administrative](https://support.gitlab.com/hc/en-us/sections/19926471791772-Administrative)
    - [Agile Planning](https://support.gitlab.com/hc/en-us/sections/25409845632540-Agile-Planning)
    - [AI](https://support.gitlab.com/hc/en-us/sections/25409833616540-AI)
    - [CI/CD Pipeline & Runner](https://support.gitlab.com/hc/en-us/sections/19926474845852-CI-CD-Pipeline-Runner)
    - [CoreDevOps](https://support.gitlab.com/hc/en-us/sections/25409846247964-CoreDevOps)
    - [Errors](https://support.gitlab.com/hc/en-us/sections/19926502520220-Errors)
    - [How-To](https://support.gitlab.com/hc/en-us/sections/19926486239772-How-To)
    - [Infrastructure](https://support.gitlab.com/hc/en-us/sections/25409833204508-Infrastructure)
    - [Kubernetes](https://support.gitlab.com/hc/en-us/sections/19926440992668-Kubernetes)
    - [Licensing & Subscription](https://support.gitlab.com/hc/en-us/sections/19926470769820-Licensing-Subscription)
    - [Migrations](https://support.gitlab.com/hc/en-us/sections/19926477110044-Migrations)
    - [Observability](https://support.gitlab.com/hc/en-us/sections/25409828080540-Observability)
    - [Performance](https://support.gitlab.com/hc/en-us/sections/19926476335644-Performance)
    - [R&D RPM](https://support.gitlab.com/hc/en-us/sections/25192479183388-R-D-TPM)
    - [Security](https://support.gitlab.com/hc/en-us/sections/19926473238940-Security)
    - [Security and Compliance](https://support.gitlab.com/hc/en-us/sections/25409832587932-Security-and-Compliance)
    - [Troubleshooting](https://support.gitlab.com/hc/en-us/sections/19926475879196-Troubleshooting)
    - [Upgrades](https://support.gitlab.com/hc/en-us/sections/19926489354268-Upgrades)
    - [Other Articles](https://support.gitlab.com/hc/en-us/sections/15215649512604-Other-Articles)
    - [Templates](https://support.gitlab.com/hc/en-us/sections/20197250020508-Templates)
- Zendesk US Government
  - Under the [About GitLab Support](https://federal-support.gitlab.com/hc/en-us/categories/37060125978004-About-GitLab-Support)
    - [Support Pages](https://federal-support.gitlab.com/hc/en-us/sections/10593044624020)
  - Under the [Knowledge articles](https://support.gitlab.com/hc/en-us/categories/360002276159-Knowledge-Articles)
    - [Administrative](https://federal-support.gitlab.com/hc/en-us/sections/37233537790740-Administrative)
    - [Agile Planning](https://federal-support.gitlab.com/hc/en-us/sections/46141240478612-Agile-Planning)
    - [AI](https://federal-support.gitlab.com/hc/en-us/sections/46141244316564-AI)
    - [CI/CD Pipeline & Runner](https://federal-support.gitlab.com/hc/en-us/sections/37233605456788-CI-CD-Pipeline-Runner)
    - [CoreDevOps](https://federal-support.gitlab.com/hc/en-us/sections/46141281147668-CoreDevOps)
    - [Errors](https://federal-support.gitlab.com/hc/en-us/sections/37233604397460-Errors)
    - [How-To](https://federal-support.gitlab.com/hc/en-us/sections/37233538834324-How-To)
    - [Infrastructure](https://federal-support.gitlab.com/hc/en-us/sections/46141282089236-Infrastructure)
    - [Kubernetes](https://federal-support.gitlab.com/hc/en-us/sections/37233537044372-Kubernetes)
    - [Licensing & Subscription](https://federal-support.gitlab.com/hc/en-us/sections/37233526841364-Licensing-Subscription)
    - [Migrations](https://federal-support.gitlab.com/hc/en-us/sections/37233603216404-Migrations)
    - [Observability](https://federal-support.gitlab.com/hc/en-us/sections/46141255714068-Observability)
    - [Performance](https://federal-support.gitlab.com/hc/en-us/sections/37233547873812-Performance)
    - [R&D RPM](https://federal-support.gitlab.com/hc/en-us/sections/45829936967700-R-D-TPM)
    - [Security](https://federal-support.gitlab.com/hc/en-us/sections/37233602184980-Security)
    - [Security and Compliance](https://federal-support.gitlab.com/hc/en-us/sections/46141257746452-Security-and-Compliance)
    - [Troubleshooting](https://federal-support.gitlab.com/hc/en-us/sections/37233516064532-Troubleshooting)
    - [Upgrades](https://federal-support.gitlab.com/hc/en-us/sections/37233572862356-Upgrades)
    - [Other Articles](https://federal-support.gitlab.com/hc/en-us/sections/29015014994068-Other-Articles)
    - [Templates](https://federal-support.gitlab.com/hc/en-us/sections/37233549693332-Templates)

## Creating a section as a non-admin

For the creation of a section, please create a [Feature Request issue](https://gitlab.com/gitlab-com/eta/css/issue-tracker/-/issues/new?description_template=Feature) (as it will require manual intervention by the Customer Support Systems team).

## Editing a section as a non-admin

For the modification of a section, please create a [Feature Request issue](https://gitlab.com/gitlab-com/eta/css/issue-tracker/-/issues/new?description_template=Feature) (as it will require manual intervention by the Customer Support Systems team).

## Deleting a section as a non-admin

To request the deactivation of a section, please create a [Feature Request issue](https://gitlab.com/gitlab-com/eta/css/issue-tracker/-/issues/new?description_template=Feature) (as it will require manual intervention by the Customer Support Systems team).

## Administrator tasks

{{% alert title="Note" color="primary" %}}

- All sections in this section require `Administrator` level access to Zendesk.

{{% /alert %}}

### Viewing sections in Zendesk

To see the current sections in Zendesk:

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
1. Click the name of the category the sections are within

### Creating a section

{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).
- **SEO Impact:** Sections affect URL structure, search indexing, and article discoverability. Changing section names or structure can break existing links and impact search engine rankings.
- Exercise caution if you make changes to sections.

{{% /alert %}}

For the creation of a section, you will need to create a MR in the sync repo. The exact changes being made will depend on the request itself. A starting template you can use would be:

```yaml
---
---
name: 'Your section name here'
previous_name: 'Your section name here'
description: 'Your description here'
locale: 'en-us' # This should always be used
position: 0 # Integer representing section display order
```

After a peer reviews and approves your MR, you can merge the MR. When the next deployment occurs, it will be synced to Zendesk.

### Editing a section

{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).
- **SEO Impact:** Sections affect URL structure, search indexing, and article discoverability. Changing section names or structure can break existing links and impact search engine rankings.
- Exercise caution if you make changes to sections.

{{% /alert %}}

To edit a section, you will need to create a MR in the sync repo. The exact changes being made will depend on the request itself.

After a peer reviews and approves your MR, you can merge the MR. When the next deployment occurs, it will be synced to Zendesk.

#### Changing the name of a section

If you need to change the name of a section, copy the current value into the `previous_name` attribute and then change the `name` attribute. This allows the sync to still locate the section in question to update.

### Moving sections to a new location

{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).
- **SEO Impact:** Sections affect URL structure, search indexing, and article discoverability. Changing section location or structure can break existing links and impact search engine rankings.
- Exercise caution if you make changes to sections.

{{% /alert %}}

To move a section to a new caregory, you will need to create a MR in the sync repo. The change is simply moving the file from its current folder (i.e. the current category) to the new folder (i.e. its new category).

After a peer reviews and approves your MR, you can merge the MR. When the next deployment occurs, it will be synced to Zendesk.

### Deleting a section

{{% alert title="Danger" color="danger" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).
- When you delete a section, all the articles contained in the section (including any translations) are archived.
- Exercise extreme caution in doing this.

{{% /alert %}}

As the sync repos do not perform deletions, you will have to do 2 actions to delete a section.

First, you must delete the corresponding file from the sync repo. After a peer reviews and approves your MR, you can merge the MR.

After that is done, you then must delete it from Zendesk itself.

To delete a section from Zendesk:

1. [Navigate to the sections view](#viewing-sections-in-zendesk)
1. Click the three vertical dots to the right of the section in question
1. Click `Edit section`
1. Click `Delete section` at the left-side of the page
1. Click `OK` to confirm the change

### Performing an exception deployment

To perform an exception deployment for sections, navigate to the sections sync project in question, go to the scheduled pipelines page, and click the play button for the sync item. This will trigger a sync job for the sections.

## Common issues and troubleshooting

### Not seeing section changes after a merge

As sections follow the `Standard` deployment type, they would only be deployed during a normal deployment cycle (or when an exception deployment has been done)
