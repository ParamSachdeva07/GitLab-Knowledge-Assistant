---
title: "Cognism"
description: "Cognism is sales intelligence software that provides contact or account data helping sales and marketing teams drive predictable pipeline"
---

## About Cognism

Cognism is sales intelligence software that provides contact or account data helping sales and marketing teams drive predictable pipeline

## Set Up

Once you receive your login and enter the Cognism platform you will need to download the Cognism Chrome extension. You can also find the link for the Cognism Chrome Extension by following this [link](https://help.cognism.com/hc/en-gb/articles/4403402216722-How-to-install-the-Cognism-Chrome-Extension).

## Connect your tools

Once you are logged in into your Cognism Web-App, start by connecting your tools (Salesforce & Outreach). This will allow you to export leads to both tools.

Even though this process is very straight forward, feel free to reference the [How to Integrate Cognism to Salesforce](https://help.cognism.com/hc/en-gb/articles/4407455139602-How-to-Integrate-Cognism-to-Salesforce-) and [How to Integrate Cognism to Outreach](https://help.cognism.com/hc/en-gb/articles/12127689794834-How-to-integrate-Cognism-to-Outreach) documentations if need be.

## Ways to access Cognism

Cognism is accessed through Okta and can be opened in either the Cognism web app or the Cognism Chrome extension. Both interfaces provide access to Cognism data. Cognism data is also written to Salesforce on lead records that meet the criteria for automatic enrichment and on records exported manually from the Chrome extension or web app.

## Who can use Cognism at GitLab?

Cognism licenses are primarily assigned to the BDR role in the Sales Development organization and the AE role in the Sales organization.

Temporary licenses may be granted to team members outside these roles if seats are available. These temporary licenses may be reassigned if they are needed for a new user in one of the primary roles.

If a licensed user does not login to Cognism for 2+ months their seat may be reassigned to new users.

Unlicensed team members can still view Cognism-enriched data on lead and contact records in Salesforce.

## Training

Both the Cognism Web App and the Cognism Chrome Extension are self explanatory and very user friendly, however, Cognism does provide additional videos that can be viewed to get familiar with the tool.

| Title | Duration | Summary |
| ------ | ------ | ------ |
| [Cognism Chrome Extension Intro](https://www.youtube.com/watch?v=D0kv7aF7Iho&ab_channel=Cognism)| 2:04 | A general overview of the Cognism Chrome Extension|
| [Cognism Chrome Extension Workflow](https://www.youtube.com/watch?v=GduWMj4nzx8&ab_channel=Cognism)| 1:13 | Cognism Chrome Extension Workflow Examples|
| [How to Use Cognism for Sales - Product Tour](https://www.youtube.com/watch?v=4YG5NhxbN-w) | 10:40 | Cognism Platform Product Tool|
| [How to Use Cognism for Marketing](https://www.youtube.com/watch?v=4YG5NhxbN-w) | 04:19 | How to use the Cognism platform to power-up your marketing engine |

## SFDC Field Mappings

With Cognism, we're only enriching Cognism custom fields so the mapping reflects this. You'll find these fields by looking for `[Cognism]` in their field label name. On the lead & contact layouts, you'll find the Cognism Section, right below the Zoominfo Section.

If you have concerns about field mapping or you notice that some of the fields do not get enriched as expected, do reach out to Marketing Operations.

## Do Not Call and Do Not Email Automation

If the proper criteria is set, Cognism can cause a lead/contact in SFDC to be labeled as `Do not email` and `Do not call`. Read more about the rules on the [sales development handbook page](/handbook/sales/sales-development/#do-not-call-and-do-not-email-automations).

## Outreach Integration

The Cognism Outreach integration is live and you may export contacts directly to Outreach. Any contacts you do export, will also be exported in SFDC.

There are some limitations in place:

- We do not allow for new accounts/account updates from Cognism into Outreach.
- Please do not upload any contact without an email address into Outreach- if you do, the prospect will not sync into SFDC and any activities you do on the prospect will not be recorded in SFDC.
- Any prospects created without email address will be found and deleted in the Outreach database management we will run monthly. To avoid uploading contacts with no email addresses, please use the Cognism filtering available.

## Use of Cognism Enhance feature to enrich lead list uploads without email

There are situations where list uploads, obtained from various events, do not have an email and, therfor, cannot be uploaded into our SFDC instance. To bypass this challenge, we use the [Cognism Enhance](https://help.cognism.com/hc/en-gb/articles/4404423963026-Using-Cognism-Enhance) feature.  It only needs certain data points (`First Name`, `Last Name`, `Company Name`) to be able to fill in the rest (`Email`).

If your lead list does not have is missing the email data point, feel free to open a Mops project with this issue template, fill in the needed details, and the missing data will be added for those leads that match to Cognism's database.

**NOTE:** All leads that have been enriched with email information, are, by default, opted out of email communication. These are not opted in and we can only reach out if we get the proper `express consent`.

## Cognism <> Workato Automated Enrichment

GitLab now uses Workato, rather than Openprise, to run automated Cognism enrichment for existing Salesforce lead and contact records. This integration does not create net-new leads or contacts; it only enriches records that already exist in Salesforce.

The current setup works in two steps. First, RingLead Mass Update identifies records that meet the approved enrichment criteria and sets the Enrich with Cognism checkbox. Once that field is set, Workato picks up the record, calls Cognism’s API, and writes the mapped Cognism data back to Salesforce.

The integration runs on an hourly basis in production. If a record was already enriched by Cognism in the last month, it is not re-enriched until a month has passed since the last Cognism enrichment.

As part of the enrichment, the process writes back Cognism custom fields and can also populate standard fields such as Phone and Email when those fields are blank. Lead ownership is not changed by this process.

The current enrichment cohorts are:

- **Working EMEA Trial**

1. Status is one of `MQL`, `Accepted`, or `Qualifying` *AND* Impartner Partner Account is `null` *AND* `[Cognism] Automatically Enriched` is `False` *AND* Account Demographics: Region is `EMEA` *AND* Currently in Trial is `True` *AND* `[Cognism] Automatically Enriched` relative date before `Last Month`.

- **Recently Engaged High-Score PQLs**

1. Last Interesting Moment Date equals `Last 60 Days` *AND* `[PQL] Product Qualified Lead` is `True` *AND* `[PTP] Score Value` is `4, 5` *AND* `[Cognism] Automatically Enriched` relative date before `Last Month` *AND* `Enrich with Cognism` is `False`.

- **Request Contact & ZoomInfo Exported Records with no Email/Phone**

1. Initial Source is `Request - Contact` *OR* `Zoominfo` *AND* Owner Name does not contain `Disq`, `Inel`, or `Jihu` *AND* (Phone is `blank` *OR* Email is `blank`) *AND* Demographic Score is greater than `59` *AND* Created Date is `This Fiscal Year` *OR* `Last Fiscal Year` *AND* `[Cognism] Automatically Enriched` relative date before `Last Month` *AND* `Enrich with Cognism` is `False`.

- **APJ Missing Number**

1. Account Demographics: Territory contains `APJ` *AND* Account Demographics: Territory does not contain `SMB` *AND* Account Demographics: Employee Count is greater than `101` *AND* Phone is `blank` *AND* Mobile is `blank` *AND* Created Date is `This Fiscal Year` *OR* `Last Fiscal Year` *AND* `[Cognism] Automatically Enriched` relative date before `Last Month` *AND* `Enrich with Cognism` is `False`.

- **EMEA SMB Growth Team**

1. Owner Name is one of `Arthur Gabor`, `Bastien Escudé`, `Ben Quilligan`, `Camilo Hernandez Murillo`, `Deepika Raj`, `Emma Szász`, `Hugo Barennes`, or `Kellie Lewis` *AND* `[Cognism] Automatically Enriched` relative date before `Last Month` *AND* `Enrich with Cognism` is `False`.

- Accepted Leads

1. Owner Profile contains `SDR` or `Sales Development` *AND* Initial Source is one of `AE Generated`, `Cognism`, `DiscoverOrg`, or `Email Request` *AND* Status is `Accepted` *AND* Created By is not `Marketo Integration` or `Outreach Integration` *AND* `[Cognism] Automatically Enriched` relative date before `Last Month` *AND* `Enrich with Cognism` is `False`.

If a team needs records enriched with Cognism data outside of the automated cohorts above, they should open a Marketing Operations issue in the Mops project and tag `@RobRosu` for review.

## Cognism Licensing Policy & Procedures

### Administration

Cognism is currently co-managed by the Marketing Operations and Revenue Technology teams.

Primary license ownership is reserved for the BDR role in the Sales Development organization and the AE role in the Sales Operations organization.

Temporary licenses may be assigned to team members outside these roles when seats are available. These temporary licenses may be reassigned if they are needed for a new user in one of the primary roles.

### Access & Help

BDRs and AEs should request Cognism access via Lumos during onboarding.

If a team member loses access or needs access restored, they should submit a new access request via Lumos.

For help with Cognism issues, ask in the #mktgops or #sales-tools-support Slack channels, or contact Cognism Support directly at help@cognism.com.

### Monthly License Review

Due to the limited number of available seats, licenses are reviewed monthly to ensure alignment with the licensing policy.

An active, non-admin license may be flagged for review if it does not meet the following criteria:

Integrated with Salesforce
More than 10 profiles viewed in the last 3 months

Marketing Operations will contact users in their org to confirm whether access is still needed. If the user does not need access, or does not respond, the license may be reassigned.

Unlicensed team members can still view Cognism-enriched data on lead and contact records in Salesforce.

### Detailed Process

1. Review Cognism user activity in the dashboard.
2. Identify users who do not meet the monthly review criteria.
3. Contact those users in Slack to confirm whether access is still needed.
4. Deactivate or reassign licenses that are no longer needed.
5. Create an issue in the Marketing Operations project to track deactivated users and apply the Mktg Tool Audit label.

### Pending Invites

Pending Cognim Invites have to be accepted in the time-span of a week because they block licenses from being assigned. If, after a week, the invite is still not accepted, it will be cancelled. Another invite can be sent out if requested through an [individual access request](/handbook/eta/corporate-it/end-user-services/access-requests/access-requests/)
