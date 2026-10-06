---
title: "Impartner"
description: "PRM and Partner Portal"
---

GitLab uses Impartner as our primary Partner Relationship Management (PRM) platform, partner portal and marketing center for Channel and Alliance Partners.

We use Impartner for MDF requests, lead sharing, deal registration to maximize the value of [GitLab partner program](/handbook/resellers/) for channel partners. Watch this video for step-by-step  instructions on where partners can view, accept, reject, assign and convert leads to deal registration.

## PRM MDF Approval/ Process

The Partner Marketing team offers Market Development Funds to support the **Channel Partner**'s marketing campaigns and events. Channel Partners submit the MDF request and claim to the Partner Portal, and they must be approved before being reimbursed.

This process is reflected in Iteration 2, [see flowchart](https://www.figma.com/board/5JXv8yRHDyXttWt669A67E/MDF-Process-Iterations?node-id=0-1&p=f&t=PhdMoT9RvpJz9VKz-0).

<iframe style="border: 1px solid rgba(0, 0, 0, 0.1);" width="800" height="450" src="https://embed.figma.com/board/5JXv8yRHDyXttWt669A67E/MDF-Process-Iterations?node-id=0-1&embed-host=share" allowfullscreen></iframe>

The emails to Partner and GitLab team members in the PRM Approval Process can be viewed in [this document](https://docs.google.com/document/d/1LfI-J77ag1CBRYUtjG5sQF-YuQFPnfT9ol0J26bmNjk/edit?usp=sharing).

### Change Management

1. The MDF request and claim will sync to Salesforce, however the attachments will not sync to Salesforce. That said, when we complete the POP task on the epic/issue, we will have to use Impartner as the SSOT. Please link the Impartner URL to the epic/issue.
2. There will be a new MDF dashboard, and Partner will be able to add a claim directly from the dashboard when the request is Approved.
3. There is a new required field on the Claim form asking for a Claim Title. We will need to provide guidance to Partner so they know how to name the Claim. Claim Titles need to be unique for each submission otherwise the workflows will fail.
4. Partners are asked to submit the lead list and proof of performance on the Claim, and Invoice when we receive a notification when the PO is created.

### Step 1 - MDF Request Submission

On the MDF Request Form, Partners are required to provide the following:

1. Activity Name
2. Type of Marketing Activity
3. In Person or Virtual Event
4. Description
5. Expected Start Date of Activity
6. Expected End Date of Activity
7. Total Cost of Activity (USD)
8. Target Number of Contacts
9. Estimated Pipeline Created (USD)
10. Partner Investment (Your Investment in USD)
11. Total Amount Required (From GitLab MDF Program in USD)
12. Vertical Industry Target Type
13. Segment Target Type

Once submitted, the Partner will receive a confirmation email indicating that their MDF request has been received.

### Step 2 - MDF Request Approval

The MDF Request Approval process will kick off as soon as the Partner submits the MDF Request.

The GitLab team member of the Activity Location will receive a notification requesting to accept or reject the MDF Request. This means if global Partner runs an event in AMER, the approval will be routed to the AMER CMM, and if they run an event in EMEA, the approval will be routed to EMEA CMM.

The GitLab team member must use the links below to review the MDF request submission, however, you can only approve or deny directly from the email notification.

Should you want to review all your requests, [see section](/handbook/marketing/marketing-operations/impartner/#prm-mdf-view).

Note that, when you have a planned PTO, Marketing Ops will need to add your manager as a secondary approver. Previously, you can do this in Salesforce, however, you'll need to create an issue request for support from MktgOps.

#### MDF Request Status

The MDF Request Status can be found in the MDF Request Details section.

- Open - when partner submits Request
- Approved - when Request is approved
- Closed - when Request and Claim are completed
- Denied - when Request is denied
- Canceled - when Request is canceled

### Step 3 - MDF Claim Submission

Once the MDF Event End Date has been reached, the Partner will receive reminder notification on the 2nd, 14th and 28th day since the End Date to submit their MDF Claim.

On the MDF Claim Form, Partners are required to provide the following:

1. Claim Title
1. Claim Amount
1. Paid Date
1. Proof of Performance attachment
1. Lead List attachment

Once submitted, the Partner will receive a confirmation email indicating that their MDF request has been received. If the Partner doesn't upload more than 2 attachments, the Partner will be notified to ensure they have provided all the necessary attachments.

### Step 4 - Check Attachments and Claim Approval

When the Partner has uploaded the Proof of Performance and Lead List attachments, the GitLab team member will be asked to check to ensure they are in-fact the right attachment.

- If they are missing an attachment, the GitLab team member is required to update the field, `Missing POP` (under the MDF Claim Details section) with the missing item. This will trigger an automated message to Partner will add the selected item to the Claim.
- If all attachments are received and looks good, the GitLab team member will update the `Approval Status` to `Denied` or `Approved` (under the Claim section).

#### MDF Claim Status

The MDF Claim Status you are to used is under the Claims section, called `Approval Status`.

- Open - when partner submits Claim
- Approved - when POP is approved
- Denied - when POP is denied

## Canceled MDF Request

When an MDF request has been cancelled, CMM will need to change the status on the MDF Request Details: `Status` => `Cancelled`. Partners will receive a notification informing them the Fund Request has been canceled. If Partners try to submit a Claim, it will automatically be rejected.

## PRM MDF View

To access your MDF request, go to PRM, and retrieve the `MDF` tab. If you do not see it, go to the `More` tab, there you'll be able to see the hidden tabs.

The preset filter will display all MDF requests that are Pending, Approved and Denied.

Should you wish to have a customized view, following the instructions below.

1. Go to the `Pending` tab
1. Select the three dots in a circle, and `Create From Current View`
1. Update the Name to "My Pending Requests"
1. Set Visibility: "Private - can only be seen by me"
1. In Manage Filters, Click on `+Add`

      1. Field: `Channel Marketing Manager - Name`
      1. Operator: `equals`
      1. Type: `Value`
      1. Value: Select your name

1. In Column Configuration, add any additional fields.
1. Save and repeat for the other statuses - Approved and Denied.

## MDF Dashboard Access

Partner needs to be granted access to the MDF dashboard. To do so, they must be an Authorized partner and MDF administrator.

To update the user to an MDF administrator:

1. Go to the user profile and select edit
1. In the Delegated Administrative Privileges section, check `MDF Administrator` under Administrative Privileges

## Lead-Sharing

### Channel Partner Lead Flow Overview

**Channel Partners** can work with the Partner Marketing team to create campaigns that will be shared to Prospects. The [campaign types](/handbook/marketing/growth-marketing/partner-and-industry-marketing/#types-of-partner-campaigns) include Partner sponsored, MDF funded and joint partner campaigns.

The flow starts from Marketo > Salesforce > Traction > Impartner.

The partner lead is:

1. Created in Marketo via list import or form submission
2. Synced SFDC via Salesforce Campaign Sync
3. Assigned to Partner Queue via Traction
4. Added to the Prospects in Partner Portal.

### Impartner Sync Requirements

The synchronization between Salesforce and Impartner operates through a newly created Salesforce object called "Prospects." This object serves as an intermediary layer that bridges the gap between Salesforce's lead/contact structure and Impartner's requirements. Since Impartner can only sync to one object type through Salesforce, the Prospects object was specifically designed as a placeholder to facilitate this data transfer.

The flow works as follows: leads are initially uploaded into Marketo from events and other sources, then sync to Salesforce as they always have. From Salesforce, the data now syncs to the new Prospects object, which then pushes the information to Impartner.

### Change Management: Vartopia to Impartner

1. Lead upload process into Marketo remain completely unchanged. The Marketo to Salesforce synchronization continues as before with no modifications required to templates or daily workflows.
2. The manual "Sync to Vartopia" checkbox is eliminated and replaced with automated sync based on [criteria](/handbook/marketing/marketing-operations/impartner/#partner-campaign-requirements).
3. MDF campaign leads are automatically [accepted](/handbook/marketing/marketing-operations/impartner/#mdf-campaign-auto-acceptance) upon entry to Impartner, removing the manual acceptance step.
4. Field names updated:
   1. Vartopia Partner Account → Impartner Partner Account
   2. Partner Prospect Status → Partner Lead Status
   3. Prospect Admin → Impartner Partner Contact.
5. A new Partner Sync Date field is added for verification
6. A new Prospects object in Salesforce serves as an intermediary for sync while teams continue using existing lead/contact records.
7. Partners now require "[Opportunity Admin](/handbook/marketing/marketing-operations/impartner/#prospects-and-deals-view-access)" permission (found in Delegated Administrator Privileges) to view all organizational leads and deal registrations. Without this permission, partners only see records assigned specifically to them.

### Requirement for Sync

1. `Impartner Partner Account` not equal to `NULL`
2. `Impartner Partner Account` associated with the partner requires a `Partner Contact` on the account
3. Partner Lead must have a:
   1. First Name
   2. Last Name
   3. Phone
   4. Email
   5. Address (Country)

When synced, `Partner Synced Date` will be populated with the time and date the partner lead was synced to Impartner. If an Impartner Partner Account in Salesforced, but the `Partner Synced Date` is missing, please notify Marketing Ops.

### MDF Campaign Auto-Acceptance

Market Development Fund campaigns receive enhanced treatment within the tracking system. MDF campaign leads are automatically accepted upon entry into Impartner, streamlining the partner experience and reducing administrative friction.

### Prospects and Deals View Access

Enable Partner to see all organizational leads and deal registrations in partner portal by updating partner user permissions to grant "Opportunity Admin" access

To update the user to an Opporrunity Administrator:

1. Go to the user profile and select edit
1. In the Delegated Administrative Privileges section, check `Opportunity Administrator` under Administrative Privileges

## Partner Campaign Tracking

This process tracks which marketing campaigns drive partner deal registrations and measures their effectiveness. We automatically link leads to their originating partner campaigns, so when partners submit deal registrations, the platform seamlessly pulls campaign attribution data from the Prospect record in Impartner without requiring additional partner effort.

When automated attribution isn't available, partners maintain control by manually selecting the specific marketing initiative that influenced their deal registration.

### Partner Campaign Requirements

1. `Channel Partner Name` must be an exact match to the Partner Account in Salesforce
2. Budget Holder = `chnl` or `ptnr`
3. Status != Aborted

### Deal Registration Change Request

In the scenario where the Marketing Campaign needs to be added, updated or removed, the marketing team will need to create an asana task by filling out this [form](https://form.asana.com/?k=1i4lL5h0RLzfTqNWBTH84Q&d=306855239930259) with the Request Type, `Partner DR Campaign Request`.

The following will be required in this change request:

1. Identify the DR(s) that need to be updated with proof of campaign member or touchpoint
2. Marketing Ops will verify DR(s)
3. Marketing Ops to add Marketing Campaign

Note, that only Campaign after September 27 (launch date) will be approved.

This is a [video](https://youtu.be/_t98rC1ug6A) recording should you need a visual capture of how to create the change request.

## Partner Recall

The first phase of the recall process is live in the “Prospects” module in the GitLab Partner Portal. The recall process is built to be able to pull back leads that are not being actioned.

Only partner leads acquired from fully paid initiatives generated by GitLab Inc. through joint campaigns are subject to recall. **We will not recall leads from Partner sponsored, and MDF funded campaigns.**
As part of the first of three phases, partner leads older than 30 days with a Partner Share Status = Pending implying the Channel Partner has not accepted nor rejected the lead, will be recalled.

In the final phase, GitLab Inc. will allow Channel Partners a period of 5 days, starting from the day the lead is assigned in the Prospect module, to accept the lead by updating the Partner Share Status. After accepting, Channel Partners will have a period of 10 days starting from the date the lead was accepted to revise the Partner Lead Status before the lead is re-routed back to GitLab Inc for follow up.

### Rules

1. At any time, a recalled lead participates in another partner campaign, they will not be reassigned to a partner.
2. At any time, a partner lead participates in multiple campaigns will be prioritized to the partner of the first campaign.
3. At any time, a lead participates in an MDF campaign, they will not and can not be recalled.
4. Actively working leads will not shared to partners which means their CRM Partner ID can not be updated or should be removed. The only exception to this rule are leads who participate in an MDF campaign.

## Field Glossary

### Lead/Contact Object

| Field Name               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Partner Contact| The Partner Contact serves as the designated lead manager responsible for managing and assigning prospects within their organization, and will receive all partner lead notifications. Each Impartner Partner Account is limited to one individual in this critical role.<br>This Salesforce field in the Impartner Partner Account is mandatory—if left blank, prospect records will not be routed to anyone, resulting in missed opportunities and unassigned leads.|
| Partner Share Status| The Partner Share status tracks the current stage of each partner lead within the lead sharing workflow:<br><br>1\. Pending: Awaits partner decision to accept or reject the prospect<br>2\. Accepted: Partner has committed to qualifying and working the prospect<br>3\. Rejected: Partner has declined to pursue the lead and will not work it.|
| Partner Lead Status | The Partner Lead Status identifies the status of the lead as the partner work it through the sales cycle.<br><br>1\. Qualifying: Indicates that lead is being worked<br>2\. Qualified: Partner has contacted the prospects and confirmed that there's a real sales opportunity<br>3\. Disqualified: Partner has determined the prospect isn't worth pursuing<br>4\. Converted to DR: Partner has turned the prospect into a deal registration.|
| Impartner Partner Acount | Impartner Partner Account is a lookup field based on the Account ID (18) in Salesforce. This field shows the partner account in which the lead is associated with via Vartopia.|
| Partner Shared Date| This time/date field tracks the date the prospect is shared to Partners|
| Partner Synced Date| This time/date field tracks the date the prospect has been synced to Impartner.|
| Partner Accepted Date| This time/date field tracks the date the prospect is accepted by Partners|
| Partner Recalled Date| This time/date field tracks the date the prospect is recalled from Partners|

## PRM - Salesforce Integration

The integration from PRM to Salesforce is customizable per object.

- Impartner `MDF Request` is mapped to SFDC `Funds Request`
- Impartner `MDF Claim` is mapped to SFDC `Funds Claim`
- Impartner `Prospects` is mapped to SFDC `Partner Prospects`
- Impartner `Deal Registration` is mapped to SFDC `Deal Registration`

### MDF Request and Claim Salesforce Sync

There is a two way sync between MDF Request and MDF Claim objects. The ID indicator between both sync is the Funds Request Number, also known as the MDF Number.
