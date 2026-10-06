---
title: "UserGems"
description: "UserGems is a job changes tracking tool which captures and combines signals to help our teams identify the best buyers, have compelling reasons to reach out, and act on those insights with automation"
---

### Ways to access UserGems data

You can identify a lead created by UserGems by referencing its Initial Source.

UserGems creates leads with three slightly different Initial Sources based on the tracking motion or feature involved: Contact Tracking, Target Account Tracking, and Meeting Assistant. The three Initial Sources you'll see on UserGems-created leads are:

- UserGems Contact Tracking
- UserGems - New Hires & Promotions
- UserGems - Meeting Assistant — see the [UserGems Meeting Assistant](/handbook/marketing/marketing-operations/usergems/#usergems-meeting-assistant) section below for more information.

### UserGems Contact Tracking

UserGems helps GitLab track contacts from carefully selected cohorts and surface relevant job-change and relationship signals.

1. [CW Opp Associated Contacts (Large)](https://gitlab.lightning.force.com/lightning/r/Report/00OPL000006Rs2T2AS/view)
2. [CW Opp Associated Contacts (Mid-Market)](https://gitlab.lightning.force.com/lightning/r/Report/00OPL000006Rs8v2AC/view)
3. [CW Opp Associated Contacts (PubSec)](https://gitlab.lightning.force.com/lightning/r/Report/00OPL000006RsC92AK/view)
4. [CW Opp Contacts (SMB, by Titles)](https://gitlab.lightning.force.com/lightning/r/Report/00OPL000006ZDi62AG/view)
5. [Contacts associated with Open Opp (Large)](https://gitlab.lightning.force.com/lightning/r/Report/00OPL000006RsFN2A0/view)
6. [Contacts associated with Open Opp (Mid-Market)](https://gitlab.lightning.force.com/lightning/r/Report/00OPL000006RsGz2AK/view)
7. [Contacts associated with Open Opp (PubSec)](https://gitlab.lightning.force.com/lightning/r/Report/00OPL000006RsLp2AK/view)
8. [Paid Contacts w Admin Role](https://gitlab.lightning.force.com/lightning/_classic/%2F00OQq000003D7gHMAS)
9. [Contacts associated with Closed Lost Opportunities](https://gitlab.my.salesforce.com/00OPL000006MXuj2AG)

### UserGems Target Account Tracking

In a separate motion from contact tracking., UserGems also helps GitLab identify **New Hires & Promotions** at our tracked accounts.

The current list of target accounts are as follows:

1. [Actively Working Accounts](https://gitlab.my.salesforce.com/00OQq000005jJBhMAM)
2. [6Sense 6QA Accounts](https://gitlab.lightning.force.com/lightning/_classic/%2F00OQq000003Gf77MAC)
3. [SMB Accounts](https://gitlab.lightning.force.com/lightning/r/Report/00OPL00000CI2Np2AL/view)
4. [AMER COMM East MM Customers](https://gitlab.lightning.force.com/lightning/r/Report/00OQq000003FJILMA4/view)
5. [Domestic First Order Available](https://gitlab.lightning.force.com/lightning/r/Report/00OPL00000EtAcz2AF/view)
6. [Open Opp Accounts] - Automatically tracked cohort
7. [Revive Closed Lost Accounts] - Automatically tracked cohort

### What happens when UserGems detects a job change?

When job changes (or new hires/promotions into the target accounts) are detected for the contact cohorts tracked above, UserGems will:

- create a net new lead with the recent account/company info;
- mark the existing contact as No Longer at Company using the **UG - No Longer at Company** checkbox field;
- update the status to **Disqualified**
- set the **Disqualified Reasons** to **No Longer at Company**.

### UserGems Available Fields

Either through reporting or on the lead/contact/UserGems objects, you'll be able to reference a few fields that will be populated by UserGems. Some of the most important ones are:

- *[UG] Company Country*; - As the field name says, this represents the current company country;
- *[UG] Person Country*; - As the field name says, this represents the current person country;
- *[UG] Company State*; - As the field name says, this represents the current company state;
- *[UG] Person State*; - As the field name says, this represents the current person state;
- *[UG] Person LinkedIn URL*; - This is the current LinkedIn URL of the individual;
- *[UG] - Is Target Company*; - This checkbox will be checked if the account is found in the list of target accounts tracked by UG;
- *[UG] - No Longer At Company*; - This checkbox will be checked on the contact object if UserGems identifies a job change for the respective contact;
- *UG - Is Customer Company*; - This checkbox will be checked if the account is found on the list of customer accounts shared with UG;
- *UG - Job Started Date*; - This field will be updated on the lead record and will contain the job started date;
- *UG - Past Account*; - This field will be updated on the net new leads created by UG and will link to the account found on the associated contact;
- *UG - Past Contact*; - This field will be updated on the net new leads created by UG and will link to the previous contact for which the job change was identified;
- *UG - Past Title*; - This field will be updated on the net new leads created by UG with the title the contact had prior to the job change;

### UserGems Campaign Overview

| Campaign Name | Purpose | Use Case | Signals | Initial Source | Status |
|---------------|---------|----------|---------|----------------|--------|
| [FY27 UG Contact Tracking - Past Champions](https://gitlab.lightning.force.com/lightning/r/Campaign/701Qq00001J3p2YIAR/view) | Track GitLab champions who have changed companies | Immediate action when champions move to new accounts - leverage existing relationship | Past Champion | UserGems Contact Tracking | Active - Went Live on 9/21/2026 |
| [FY27 UG Contact Tracking - Re-Engagement](https://gitlab.lightning.force.com/lightning/r/Campaign/701Qq00001J3Y0AIAV/view) | Track attendees from PipeGenDays event | Follow up with engaged event attendees on discussions and next steps | N/A | UserGems | Inactive |
| [FY27 New Hires & Promotions](https://gitlab.lightning.force.com/lightning/r/701PL00000MTkJ0YAL/view) | Monitor job changes at tracked accounts | Engage new decision makers or elevated contacts at key accounts | New Hires, Promotions | UserGems - New Hires & Promotions | Inactive |

### UserGems Past Champions (Contact Tracking) Lead Handling Guidelines

#### Purpose

This document explains how SDRs/BDRs should work UserGems Past Champion leads from the time they enter the Past Champion motion through MQL processing, ownership assignment, Relevance AI enrichment, prioritization, and Outreach enrollment.

#### Audience

This guidance is for SDRs/BDRs who may receive or work UserGems Past Champion leads.

#### Scope

This document covers:

- how Past Champion leads enter the process
- how Past Champion leads become MQLs
- how standard MQL ownership assignment takes place
- when the Relevance AI fields are populated
- how SDRs/BDRs should use the Relevance AI fields
- Past Champion prioritization, follow-up, and Outreach enrollment

This document does not cover the following workflows:

- New Hires & Promotions
- Re-Engagement
- Revive Closed Lost
- Meeting Assistant
- Other UserGems motions

#### Relaunch Status

The Past Champions relaunch went live on September 21, 2026.

The relaunch uses the standard MQL process and the current Past Champion ownership process.

#### 1. How the Past Champion Flow Works

The process follows these steps:

1. UserGems identifies a tracked Past Champion and adds the lead to the approved Past Champion campaign.
2. Campaign membership identifies the Past Champion motion.
3. The lead is automatically moved into the MQL process.
4. Standard factor-based MQL ownership assignment takes place through the normal MQL routing process.
5. Once the lead has MQL status and a BDR or SDR assignment type, the Relevance AI workflow picks up the lead.
6. Relevance AI populates it's dedicated fields on the Salesforce lead record.
7. The assigned SDR/BDR reviews the lead, the Relevance fields, the account context, and the recommended next action.
8. The SDR/BDR manually adds the lead to the approved [Past Champion Outreach sequence](https://web.outreach.io/sequences/2513/overview) after completing the required checks.

#### 2. What Causes a Past Champion Lead to Enter the Process

Campaign membership is the primary Past Champion signal.

Supporting UserGems information includes:

- UserGems Contact Tracking as the Initial Source
- Created By as UserGems Integration
- Past Contact
- Past Account
- Past Title
- UserGems job-start information
- Current company, title, country, and LinkedIn information
- Interesting Moment and Last Interesting Moments (LIMs)

The supporting fields help SDRs/BDRs understand and work the lead. They do not replace the approved Past Champion campaign membership as the primary motion signal.

#### 3. How Past Champion Leads Become MQLs

Past Champion leads are automatically MQLed through the Past Champion process. SDRs/BDRs do not need to manually MQL these leads.

After the lead becomes MQL, it proceeds through the standard factor-based MQL ownership process. The final owner depends on the applicable Salesforce and account factors, which can include:

- matched account
- account status and customer status
- segment
- account coverage
- BDR or SDR availability
- preferred language and geographic information
- open opportunity context
- other standard MQL assignment rules

SDRs/BDRs should work the lead according to the owner and assignment shown on the Salesforce record. Do not assume that every Past Champion will be assigned to an SDR or BDR.

#### 4. How the Relevance AI Fields Are Populated

The Relevance AI workforce triggers when both conditions are true:

- Salesforce Lead Status = `MQL`
- Assignment Type = `BDR` or `SDR`

MQL status by itself is not sufficient. The lead must also have a BDR or SDR assignment type for the workforce to process it.

After the workforce processes the lead, it populates the following Salesforce fields:

| Field | What it contains | How SDRs/BDRs should use it |
| --- | --- | --- |
| `Relevance_Priority__c` | Priority tier and source bucket, such as `High \| UG Past Champions` | Use this to understand the recommended priority for the lead. |
| `Relevance_Summary__c` | Key triage signals and a concise summary | Read this first to understand why the lead is relevant and what signals matter. |
| `Relevance_Next_Action__c` | The single recommended next action | Use it as the starting point for the next step, then validate it against Salesforce and account context. |
| `Relevance_Research__c` | The full research and supporting detail block | Use it when you need deeper context for prioritization or personalization. |
| `Relevance_Last_Updated__c` | Timestamp showing when the Relevance fields were last updated | Use it to assess whether the output is current. |

Relevance fields are written to the Salesforce lead record. SDRs/BDRs should not expect them to populate before the lead reaches MQL and receives a BDR or SDR assignment type.

#### 5. What SDRs/BDRs Should Do When the Relevance Fields Are Populated

When the fields are available:

1. Review `Relevance_Priority__c` to understand the recommended priority.
2. Read `Relevance_Summary__c` to understand the key signals.
3. Review `Relevance_Research__c` for supporting detail.
4. Follow `Relevance_Next_Action__c` as the recommended starting point.
5. Validate the recommendation against the current Salesforce record, account, opportunity, and ownership context.
6. Use the relevant UserGems and LIMs context to personalize the first touch.
7. Manually add the person to the [approved Past Champion sequence](https://web.outreach.io/sequences/2513/overview) when the enrollment checks are complete.

Relevance AI provides a recommendation. The SDR/BDR remains responsible for reviewing the record and deciding whether the recommended action is appropriate.

#### 6. What to Check When the Relevance Fields Are Blank

If the Relevance fields are blank, check the following before treating it as a system failure:

- Is Lead Status set to `MQL`?
- Does the lead have Assignment Type = `BDR` or `SDR`?
- Is the lead assigned to a BDR or SDR rather than only an AE or another owner type?
- Was the lead disqualified, recycled, or otherwise moved out of MQL before the workforce could process it?
- Is the Relevance Last Updated field blank or stale?
- Are the UserGems campaign and lead fields populated as expected?

A lead that was MQL for only a short period or was disqualified before it received a BDR or SDR assignment may not be picked up by the workforce.

If the lead meets the trigger conditions and the fields remain blank, document the lead and escalate the issue to Marketing Operations and the Relevance AI support owners.

#### 7. How Ownership Assignment Works After MQL

The Past Champion process does not assign every lead directly to an SDR/BDR through UserGems.

The sequence is:

1. Past Champion campaign membership identifies the motion.
2. The lead becomes MQL.
3. Standard MQL ownership logic evaluates the lead.
4. The lead is assigned according to the applicable account, segment, language, coverage, and other MQL factors.
5. Relevance AI processes the lead only when the assignment type is BDR or SDR.

If the lead is assigned to an AE or does not have a BDR or SDR assignment type, the Relevance fields may not populate. Do not manually change ownership solely to force Relevance AI processing. Escalate ownership questions through the normal Marketing Operations or Sales Development process.

#### 8. Past Champion Prioritization

Use the following factors when deciding how quickly to act:

- strength and relevance of the prior GitLab relationship
- relevance of the current company or account
- recency of the UserGems job-change signal
- Relevance AI priority
- presence of relevant LIMs or account activity
- account coverage and open opportunity context

A recent Past Champion move to a strong-fit account should generally receive earlier attention than a lead with limited or stale context.

#### 9. Enqueue Past Champions in Outreach

Past Champions are not automatically added to an Outreach sequence as part of this process. SDRs/BDRs are responsible for manually adding eligible leads after reviewing the Salesforce record and confirming the ownership and sequence checks.

##### SDR/BDR Enrollment Process

1. Open the Salesforce lead record.
2. Confirm that the lead is a Past Champion and has the expected campaign membership.
3. Confirm the current owner and assignment type.
4. Review the Relevance Priority, Summary, Next Action, Research, and Last Updated fields.
5. Check for existing Outreach enrollment.
6. Do not create duplicate enrollment.
7. Select the approved Past Champion sequence:
   - Past Champion sequence: **[[SD IB HT GEM-E PAST CHAMPIONS - Sept26](https://web.outreach.io/sequences/2513/overview)]**
   - Language-specific sequence, if applicable: **[[SD IB HT GEM-E PAST CHAMPIONS LANGUAGES - Sept26](https://web.outreach.io/sequences/2514)]**
8. Add the person to the sequence manually.
9. Personalize the first touch using the prior GitLab relationship, current role, account context, and relevant LIMs.
10. Record the appropriate activity, disposition, or follow-up outcome.

##### Enrollment Guardrails

- Do not enroll a lead that is already active in an Outreach sequence.
- Do not use a sequence intended for New Hires & Promotions, Re-Engagement, or another UserGems motion.
- Do not enroll the lead before confirming the owner and account context.
- Do not treat the Relevance Next Action as a substitute for reviewing Salesforce.
- If the recommended next action conflicts with the current record, pause and resolve the conflict before outreach.

#### 10. Messaging Approach

Past Champion outreach should:

- acknowledge the prior GitLab relationship where appropriate
- connect the outreach to the person's current role or company
- use the Relevance Summary, Research, and LIMs to make the message specific
- avoid sounding overly automated or generic
- make the next step clear

Suggested message structure:

1. Reference the prior GitLab relationship.
2. Tie the message to the current role or company context.
3. Add a relevant account signal or LIM if useful.
4. Present a clear value statement.
5. Ask for a simple next step.

If UG AI-generated subject or body content is available in the sequence or on the record, treat it as draft content. Review and edit it before sending.

#### Source-of-Truth Statement

This document is the source of truth for how SDRs/BDRs should work UserGems Past Champion leads, including the MQL process, ownership assignment, Relevance AI field interpretation, prioritization, and Outreach enrollment.

### UserGems Meeting Assistant

UserGems Meeting Assistant is a separate stand alone feature of UG that syncs to SDRs/BDRs Google Calendars and captures & enriches the third party contact data present in their meetings. If this contact data meets all necessary criteria, it is added as a contact in our SFDC instance.

The necessary criteria that needs to be met for a contact to be created in SFDC is the following:

- associated account/company exists in our SFDC environment;
- associated account/company matches our set persona;
- contact has a LinkedIn profile;
- contact's email domain does not match the "free email providers";

Separately, if an open opportunity also exists for the contact's company, the contact will also be added as a contact role to that open opportunity.

We're starting to leverage Meeting Assistant as a pilot for a group of 6 reps on the 12th of December. With the plan to do a full roll-out to the whole Sales Development org in mid to late January 2025.

The tool is only processing the data of third-parties and data subject rights do not impute from that third-party contact to the Team Member. Even in the case where a team member uses a work calendar to schedule a meeting with friends, that contact will be omitted due to a personal domain exclusion.

### Dynamic Layouts

On both the lead & contact object, on the top right side, if this is a UserGems Lead or a UserGems Past Contact, you'll be able to reference, at a glance relevant information like: Current Lead Link, Past Contact Link, Current Account, Current Account Type, Current Title, Current Email along with many other fields that are relevant.
