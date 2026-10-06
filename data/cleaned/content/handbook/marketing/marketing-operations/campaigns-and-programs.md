---
title: "Campaigns and Programs"
description: "Campaigns are used to track efforts of marketing tactics"
---

## Campaigns

Campaigns are used to track efforts of marketing tactics - field events, webcasts, content downloads. The campaign types align with how marketing tracks spend and align the way records are tracked across three of our core systems (Marketo, Salesforce and Bizible) for consistent tracking. Leveraging campaign aligns our efforts across Marketing, Sales and Finance.

Marketing Ops partners with the Field Marketing and Corporate Events teams to provide Marketo program set-up and configuration, providing these teams with an internal partner to provide advise on the best technical set-up to reach their goals and streamlining more complex program requirements. Visit the [Marketo Program/Campaign Support page](/handbook/marketing/marketing-operations/campaign-operations/) for additional details.

In the tables below, "Valid for List Import" indicates if this particular status can be used in a [self-service list import](/handbook/marketing/marketing-operations/automated-list-import/). In very rare cases, there are special considerations for an event that require a consultation with MOps and those are flagged in the table.

### Campaign Cost Tracking

For information on how Marketing tracks campaign costs, please visit [this page](/handbook/marketing/marketing-team-processes/#how-marketing-tracks-campaign-expenses).

### Campaign Type & Progression Status

A record can only progress **one-way** through a set of event statuses. A record _cannot_ move backward though the statuses.

i.e. Record is put into `Registered` cannot be moved backwards to `Waitlisted`

#### Conference

Any event that we have paid to sponsor, have a booth/presence and are sending representatives from GitLab (example: AWS re:Invent, DevOps Enterprise Summit). This also includes any virtual event that we sponsor and/or participate in that we do not own the registration but will generate a list of attendees, engagement.

In a virtual conference, GitLab will pay a sponsorship fee to receive a virtual booth and sometimes a speaking session slot or panel presence. Presence of a virtual booth is a requirement due to success criteria. [Read more](/handbook/marketing/virtual-events/external-virtual-events/#virtual-conferences).

For list loads greater than 5,000 `attendees`, Mktgops will need to confer with the `Field Marketing Director` on legitimacy of labeling the program members as `success` as doing so affects `Bizible Touchpoints`. Follow [directions here](/handbook/marketing/marketing-operations/campaigns-and-programs/#instructions-how-to-update-conferences-with-more-than-5000-attendees) on how to do this (MktgOps only).

**Bizible:** This is tracked as an _offline_ channel, because we do not host a registration page, and receive a list of booth visitors post-event. Touchpoints for offline channels are created through our AMM (formerly known as Bizible) campaign sync rules that can be found in this [spreadsheet](https://docs.google.com/spreadsheets/d/1xR2Q7YKskfNaxclnfGOkK8Vi739zdKypQ6GgF9MLG58/edit#gid=92970564).

| Member Status | Definition | Success | Valid for list import |
| ------------- | ---------- | ------- | ------- |
| No Action | default starting position for all records |  | No |
| Sales Invited | Invitation/Information about event sent by Sales/SDR |  | No |
| Sales Nominated | Sales indicated record to receive triggered event email sent by Marketing |  | No |
| Marketing Invited | Marketing geo-targeted email |  | No |
| Waitlisted| Holding state if registration is full will be moved to Registered if space opens| | No |
| Registered | Registered for event|| No (ask MOps for special conditions) |
| No Show | Registered but no verification of attendance, presumed no show | | Yes |
| Meeting Requested | Meeting set to occur at conference |  | No (ask MOps for special conditions) |
| Meeting No Show | Scheduled meeting at conference was cancelled or not attended |  | Yes |
| Meeting Attended | Scheduled meeting at conference was attended | Yes | Yes |
| Attended| Attended the event, did not engage at booth OR attended expo floor speaking session | Yes | Yes |
| Visited Booth | Stopped by booth for any reason (most common conference status) | Yes | Yes |
| Follow Up Requested | Requested to be followed up with by sales post event | Yes | Yes |
| Attended On-Demand | Watched/consumed conference materials post-event on-demand | Yes| Yes |

#### Content Syndication

White Paper or other content offer that is hosted by a third party.

**Bizible:** This is tracked as an _offline_ channel. Touchpoints for offline channels are created through our AMM (formerly known as Bizible) campaign sync rules that can be found in this [spreadsheet](https://docs.google.com/spreadsheets/d/1xR2Q7YKskfNaxclnfGOkK8Vi739zdKypQ6GgF9MLG58/edit#gid=92970564).

| Member Status | Definition | Success | Valid for list import |
| ------------- | ---------- | ------- | ------- |
| No Action | default starting position for all records |  | No |
| Downloaded | Downloaded content | Yes | Yes |

#### Direct Mail (Brilliant Optimized)

This is when a package or piece of mail is sent out. Current procedure requires use of Brilliant Gifts and Qualified. To utilize shipping program statuses and alerts, a Marketing team member must send an order form email out to the recipient via the Brilliant interface and change program statuses manually in either Marketo or SFDC. If the recipient is given the option to select their gift, use `Send a Gift -> Campaign or Quick Send` inside of Brilliant. If the gift is chosen by the Marketing or Sales team, utilize `Send a Gift -> Surprise Send`. The `Meeting Booked` status is updated via Qualified and `Meeting Attended` must be updated manually by Sales or Marketing after a successful meeting. `Meeting No Show` is to be updated by Sales/Sales Dev via a Qualified automated email. 

Brilliant can now sync shipping statuses over to Marketo and SFDC via program status updates but they will only work with [Direct_Mail_eGift_Global - Brilliant connected](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/PG28387A1) and all Brilliant webhook calls **must** be made with the primary smart campaign: [Send to Brilliant webhook (do not alter)](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/SC77009A1ZN19). Only this program and smart campaign can successfully call Brilliant. Note: there are a few statuses used by Brilliant within the program type that we do not necessarily use but those help track shipping statuses

**Bizible:** This is tracked as an _offline_ channel. Touchpoints for offline channels are created through our AMM (formerly known as Bizible) campaign sync rules that can be found in this [spreadsheet](https://docs.google.com/spreadsheets/d/1xR2Q7YKskfNaxclnfGOkK8Vi739zdKypQ6GgF9MLG58/edit#gid=92970564).

| Member Status | Definition | Success | Triggers gift webhook?|
| ------------- | ---------- | ------- | ------------ |
| No Action | Default starting position for all records |  |  |
| **Created** | | | |
| Nominated | Leads are added to the program with this status indicating they will receive a meeting invite |  |  |
| Invite Sent | Indicating an email invite for a meeting has been sent |  |  |
| Clicked | Not currently utilized within the program type | | |
| **Gift Requested** | | | |
| Claimed | Recipient filled out the gift request form | | |
| **Pending** | | | |
| In Fulfillment | The gift has been ordered in Brilliant  | | |
| Partially Shipped <br> Externally Shipped <br> Shipped | The gift has been shipped and program status automatically changed by Brilliant to inform Sales | | |
| Out for Delivery <br> Partially Delivered <br> Delivered | The gift has been delivered and program status automatically changed by Brilliant to inform Sales | | |
| Meeting Booked | Recipient of meeting invite has scheduled a meeting via Qualified | Yes | |
| Meeting Attended | Recipient was not labeled as a No Show to the scheduled meeting | Yes | Yes |
|Cancelled | Person has cancelled prior to the scheduled meeting  | | |
| No Show | Sales Dev has indicated via Qualified automated email the meeting did not occur  | | |

#### Email Send

This program type is used in conjunction with Marketo email programs. This program type is available to sync into SFDC, but should only be synced into SFDC if the email send in question has significant business impact that needs associated opportunity tracking. Please keep in mind that some email addresses will block Marketo's tracking, so these cannot be 100% accurate.

**Bizible:** This is technically tracked as neither an _online_ or _offline_ channel. Touchpoints are technically not created by the program type itself, but rather the action of an email recipient clicking an in-email link and visiting a Touchpoint enabled website.

| Member Status | Definition | Success |
| ------------- | ---------- | ------- |
| No Action | Default starting position for all records |  |
| Member | Added to program. If still in this status after the email send, it can be assumed they were blocked from being sent the email |  |
| Email Bounced | Marketo's email tracking detected the recipient email address bounced   |  |
| Email Delivered | Marketo's email tracking detected the recipient email address received the email sent |  |
| Email Opened | Marketo's email tracking detected the recipient opened the email |  |
| Clicked In-Email Link | Marketo's email tracking detected the recipient opened a link found in the email | Yes |
| Replied to Email | Likely to be unused step as we do not prompt for email replies |  |
| Unsubscribed | Marketo's email tracking detected the recipient unsubscribed from further communications via the in-email preferences link |  |

#### Executive Roundtables

This is used for campaigns that can either be organised through a 3rd party vendor or GitLab, covering both in-person and virtual roundtables. It is a gathering of high level CxO attendees run as an open discussion between the moderator/host, GitLab expert and delegates. There usually aren't any presentations, but instead a discussion where anyone can chime in to speak. The host would prepare questions to lead discussion topics and go around the room asking delegates questions to answer. [Read More](/handbook/marketing/virtual-events/external-virtual-events/#overview).

Program type is included on the smart campaign meant to clear `dietary restriction` related fields. 7 days after an event's program statuses are recorded, the fields are cleared automatically.

**Bizible:** This is tracked as an _offline_ channel. Touchpoints for offline channels are created through our AMM (formerly known as Bizible) campaign sync rules that can be found in this [spreadsheet](https://docs.google.com/spreadsheets/d/1xR2Q7YKskfNaxclnfGOkK8Vi739zdKypQ6GgF9MLG58/edit#gid=92970564).

| Member Status | Definition | Success | Valid for list import |
| ------------- | ---------- | ------- | ------- |
| No Action | default starting position for all records |  | No |
| Sales Nominated | Sales indicated record to receive triggered event email sent by Marketing |  | No |
| Waitlisted | Holding state if registration is full will be moved to `Registered` if space opens |  | No |
| Registered | Registered for the event |  | No (ask MOps for special conditions) |
| Cancelled | Registered, but cancelled ahead of the event | | No |
| No Show | Registered, but did not attend the event |  | Yes |
| Attended | Attended the Event | Yes | Yes |
| Follow Up Requested | Requested follow up during the event | Yes | Yes |

#### Gated Content

White Paper or other content offer.

**Bizible:** This is tracked as an _online_ channel.

| Member Status | Definition | Success |
| ------------- | ---------- | ------- |
| No Action | default starting position for all records |  |
| Downloaded | Downloaded content | Yes |

#### Inbound - offline

**Bizible:** This is tracked as an _offline_ channel because touchpoints cannot be applied directly via online means, e.g. Qualified and PQL handraises. Touchpoints for offline channels are created through our AMM (formerly known as Bizible) campaign sync rules that can be found in this [spreadsheet](https://docs.google.com/spreadsheets/d/1xR2Q7YKskfNaxclnfGOkK8Vi739zdKypQ6GgF9MLG58/edit#gid=92970564).

| Member Status | Definition | Success |
| ------------- | ---------- | ------- |
| No Action | default starting position for all records |  |
| Requested Support | Took a handraise action to request support from the GitLab team ||
| Requested Contact | Filled out Contact, Professional Services, Demo or Pricing Request | Yes |

#### Inbound Request

Any type of inbound request that requires follow up.

**Bizible:** This is tracked as an _online_ channel.

| Member Status | Definition | Success |
| ------------- | ---------- | ------- |
| No Action | default starting position for all records, does not score |  |
| Requested Support | Took a handraise action to request support from the GitLab team, does not score ||
|Waitlisted|Submitted a request to purchase a future SKU||
|Non Profit or Start Up| Submitted a request for the non-profit or start-up programs, does not score||
|Beta - No Score|Submitted a request for a beta program, does not score||
|Beta - Score|Submitted a request for a beta program, auto-MQLs| Yes|
| Requested Contact - Medium | Filled out a request for Educational Services or some other low profile program, scores +50   |Yes |
| Requested Contact - High | Filled out Contact, Professional Services, Demo or Pricing Request, auto-MQLs | Yes |

#### Live Event

This event type functions similarly to `Owned Event` with the caveat it is only used with the in-person event platform, Accelevents. It will include more statuses as Accelevents grows its product. This is an event that we have created, own registration and arrange speaker/venue (example: GitLab Commit or Meetups). Also considered in this grouping would be 3rd party auxiliary events that are added on to a conference sponsorship (i.e a happy hour or VIP dinner at a conference).

**Bizible:** This is tracked as an _online_ and as an _offline_ channel because we manage the registration process through our website. Whenever someone registers, a TP will be created based on that online activity while another  TP is added based on the campaign sync rules, for the campaign members with success statuses.

| Member Status | Definition | Success | Valid for list import |
| ------------- | ---------- | ------- | ------- |
| Invited | Invitation/Information about event sent by Sales/SDR |  | No |
|Pending|A holding status for approvals||No|
| Waitlisted | Holding state if registration is full will be moved to `Registered` if space opens |  | No |
| Denied | User was not approved for event | | No |
| Approved | User was approved for event but unlikely this will be used over Registered| | No |
| Registered | Registered for event |  | Yes |
| No Show | Registered but did not attend event |  | Yes |
| Attended | Attended event live | Yes | Yes |
| Canceled| Individual canceled their registration pre-event| | No |
| Refunded | Individual was refunded their event related payment pre-event| |  No |

#### Operational

This is used for non-traditional list uploads in which we are looking to a) avoid scoring the uploaded leads b) avoid tradition nurture emails c) fulfill some other various operational related task. e.g., educational conference list uploads.

**Bizible:** This is tracked as an _online_ channel because we participated in an event, where applicable.

| Member Status | Definition | Success | Valid for list import |
| ------------- | ---------- | ------- | ------- |
| Member | default starting position for all records |  | MOps only |
| Registered | Registered (presumably did not attend) |  | MOps only |
| Attended | Attended live event |  Yes | MOps only |
| Attended Virtually | Attended an event virtually. Attendance can be live or post-event | Yes | MOps only |

#### Owned Event

This is an event that we have created, own registration and arrange speaker/venue (example: GitLab Commit or Meetups). Also considered in this grouping would be 3rd party auxiliary events that are added on to a conference sponsorship (i.e a happy hour or VIP dinner at a conference).

**Bizible:** This is tracked as an _online_ and as an _offline_ channel because we manage the registration process through our website. Whenever someone registers, a TP will be created based on that online activity while another  TP is added based on the campaign sync rules, for the campaign members with success statuses.

Program type is included on the smart campaign meant to clear `dietary restriction` related fields. 7 days after an event's program statuses are recorded, the fields are cleared automatically.

| Member Status | Definition | Success | Valid for list import |
| ------------- | ---------- | ------- | ------- |
| No Action | default starting position for all records |  | No |
| Subscribed to Updates | Subcribed to GitLab event updates via form fill |  | No |
| Sales Invited | Invitation/Information about event sent by Sales/SDR |  | No |
| Sales Nominated | Sales indicated record to receive triggered event email sent by Marketing |  | No |
| Marketing Invited | Marketing geo-targeted email |  | No |
| Declined Invitation | Event invitation declined by recipient | | No |
| Waitlisted | Holding state for limited attendance events, moved to `Registered` if space opens, `Declined` if not |  | No |
| Declined | Status for space not available | | No |
| Registered | Registered for event |  | No (ask MOps for special conditions) |
| Cancelled | Registered, but cancelled ahead of the event |  | No |
| No Show | Registered but did not attend event |  | Yes |
| Attended | Attended event live| Yes | Yes |
| Attended On-demand| Watched/consumed the presentation materials post-event on-demand| Yes | Yes |
| Follow Up Requested | Requested additional details about GitLab to be sent post event | Yes | Yes |

#### Paid Social

**Bizible:** This program is designated to house leads and programs brought in by social related campaigns (e.g. LinkedIn campaigns) and is tracked as an _offline_ channel. Touchpoints for offline channels are created through our AMM (formerly known as Bizible) campaign sync rules that can be found in this [spreadsheet](https://docs.google.com/spreadsheets/d/1xR2Q7YKskfNaxclnfGOkK8Vi739zdKypQ6GgF9MLG58/edit#gid=92970564).

| Member Status | Definition | Success |
| ------------- | ---------- | ------- |
| No Action | default starting position for all records |  |
| Responded | Took an action related to social campaigns, like a form fill  | Yes |

#### Partner - MDF

This is for an activity that our Channel Partner is executing utilizing MDF Funds. We track membership, but the partner, not GitLab follows up with these leads. See more details [here](/handbook/marketing/marketing-operations/campaigns-and-programs/#partner---mdf).

**Bizible:** This is tracked as an _offline_ channel. Touchpoints for offline channels are created through our AMM (formerly known as Bizible) campaign sync rules that can be found in this [spreadsheet](https://docs.google.com/spreadsheets/d/1xR2Q7YKskfNaxclnfGOkK8Vi739zdKypQ6GgF9MLG58/edit#gid=92970564).

| Member Status | Definition | Success | Valid for list upload |
| ------------- | ---------- | ------- | ------- |
| Member | default starting position for all records |  | Yes |
| Sales Nominated | status for when leads have been sales nominated for the program |  | No |
| Responded | Attended event or campaign |Yes| Yes |

#### Prospecting

This program type is specific to non-event related list uploads, such as partner lists or data upload centric lists.

**Bizible:** This is not tracked on Bizible.

| Member Status | Definition | Success | Valid for list uploads |
| ------------- | ---------- | ------- | ----- |
| No Action | default starting position for all records |  | MOps only |
| Uploaded | Status lead is normally transitioned to upon successful upload |  | MOps only |
| Do Not Use (Responded) | Not to be used. Included because Marketo requires a `success` step  | Yes  | No |
| Member | Indicative of a special member status for this program type. Meaning of "special" is dependent on use case |  | MOps only |

#### Speaking Session

This campaign type can be part of a larger Field/Conference/Owned event but we track engagement interactions independently from the larger event to measure impact. It is something we can drive registration. It is for tracking attendance at our speaking engagements.

**Bizible:** This is tracked as an _offline_ channel. Touchpoints for offline channels are created through our AMM (formerly known as Bizible) campaign sync rules that can be found in this [spreadsheet](https://docs.google.com/spreadsheets/d/1xR2Q7YKskfNaxclnfGOkK8Vi739zdKypQ6GgF9MLG58/edit#gid=92970564).

| Member Status | Definition | Success | Valid for list upload |
| ------------- | ---------- | ------- | ------- |
| No Action | default starting position for all records |  | No |
| Sales Invited | Invitation/Information about event sent by Sales/SDR |  | No |
| Sales Nominated | Sales indicated record to receive triggered event email sent by Marketing |  | No |
| Marketing Invited | Marketing geo-targeted email |  | No |
| Registered | Registered or indicated attendance at the session |  | No (ask MOps for special conditions) |
| No Show | Registered but did not attend event |  | Yes |
| Attended | Attended speaking session event | Yes | Yes |
| Follow Up Requested | Had conversation with speaker or requested to be followed up with by sales post event | Yes | Yes |

#### Sponsored Webcast

This is webcast hosted on an external partner/vendor platform. The status of `Attended On-demand` accounts for GitLab hosted On-Demand and non-GitLab hosted On-demand webcasts. [Read more](/handbook/marketing/virtual-events/external-virtual-events/#overview).

**Bizible:** This is tracked as an _offline_ channel for both types of touchpoints (TPs) mentioned below.

For Sponsored Webcasts we're creating TPs in two ways:

1. **Registration TPs**, which mimic the TPs created for Owned Events through the online registration method (bizible script on our LPs). However, because for Sponsored Webcasts, we don't own the LP registration, this method is unavailable. Instead, we're replicating these TPs through the Marketo Program membership method.

The Maketo Program membership rule creates a "Registration TP" for all program members housed in Marketo programs that sit in a Marketo folder with the folder's name containing "Sponsored Webcasts". As long as this naming convention is followed, these TPs will be created automatically. The Touchpoint Date for these touchpoints is the `Program Membership Date`.

1. **Responded Status TPs**, which are created based on the [AMM Channel/Sub-Channel Rules for Offline Touchpoints](https://docs.google.com/spreadsheets/d/1xR2Q7YKskfNaxclnfGOkK8Vi739zdKypQ6GgF9MLG58/edit?gid=92970564#gid=92970564)(Rule on row 19) for responded status campaign members only. The TP Date for these TPs is the `Member First Associated Date` in the associated SFDC Campaign. Please see below the campaign statuses for the Sponsored Webcasts campaign type:

| Member Status | Definition | Success | Valid for list upload |
| ------------- | ---------- | ------- | ------- |
| No Action | default starting position for all records |  | No |
| Sales Nominated | Used by marketing for invitee tracking | | No |
| Registered | Registered for webcast |  | No |
| No Show| Registered but did not attend event |  | Yes |
| Attended | Attended event | Yes | Yes |
| Follow Up Requested | Requested to be followed up with from GitLab | Yes | Yes |
| Attended On-demand | Watched/consumed the presentation materials post-event on-demand | Yes | Yes |

#### Survey

A survey that we or a 3rd party sends out. Tracks respondents and new leads we receive.

**Bizible:** This is tracked as an _offline_ Bizible channel. Touchpoints for offline channels are created through our AMM (formerly known as Bizible) campaign sync rules that can be found in this [spreadsheet](https://docs.google.com/spreadsheets/d/1xR2Q7YKskfNaxclnfGOkK8Vi739zdKypQ6GgF9MLG58/edit#gid=92970564).

| Member Status | Definition | Success | Valid for list upload |
| ------------- | ---------- | ------- | ------- |
| Member | default starting position for all records |  | No |
| Sales Nominated | Sales indicated record to receive triggered event email sent by Marketing |  | No |
| Invited | Was invited, but did not participate in survey |  | Yes |
| Filled-out Survey | Filled out survey | Yes | Yes |
| Follow Up Requested | Filled out survey and requested to be contacted by sales | Yes | Yes |

#### Trial

Track cohort of Trials for each product line (Self-managed or SaaS) to see their influence.

**Bizible:** In-product self-managed and SaaS trials are tracked as an **offline** Bizible touchpoint. The self-managed trial utilizing a Marketo form is an **online** Bizible touchpoint.

| Member Status | Definition | Success |
| ------------- | ---------- | ------- |
| No Action | default starting position for all records |  |
| Signed Up | Signed up for Trial | Yes |

#### User Signal

Track cohort of User Gems identified leads that have previously been a "GitLab Champion", indicating a former GitLab user capable of championing GitLab at their current company.

_Bizible:_ As intended, this campaign type will not create Bizible Touchpoints. 

| Member Status | Definition | Success |
| ------------- | ---------- | ------- |
| Member | default starting position for all records |  |
| User Signal > Signal Detected | Signals have been detected via tracking tools circling around this person's former "GitLab champion" status | Yes |

#### Vendor Arranged Meetings

Used for campaigns where a third party vendor is organizing one-to-one meetings with prospect or customer accounts. This does not organize meetings set internally by GitLab team members. An example would be a "speed dating" style meeting setup where a vendor organized meetings with prospects of interest to GitLab. [Read more](/handbook/marketing/virtual-events/external-virtual-events/#overview).

**Bizible:** This is tracked as an _offline_ Bizible channel. Touchpoints for offline channels are created through our AMM (formerly known as Bizible) campaign sync rules that can be found in this [spreadsheet](https://docs.google.com/spreadsheets/d/1xR2Q7YKskfNaxclnfGOkK8Vi739zdKypQ6GgF9MLG58/edit#gid=92970564).

Program type is included on the smart campaign meant to clear `dietary restriction` related fields. 7 days after an event's program statuses are recorded, the fields are cleared automatically.

| Member Status | Definition | Success | Valid for list upload |
| ------------- | ---------- | ------- | ------ |
| No Action | default starting position for all records |  | No |
| Registered | Registered for the event |  | No |
| No Show | Registered, but did not attend the event |  | Yes |
| Attended | Attended the Event | Yes | Yes |
| Follow Up Requested | Had conversation with speaker or requested additional details to be sent post event | Yes | Yes |

#### Webcast

Any webcast that is hosted and held by GitLab. There are a few different groups that run webcasts. Go their specific pages to see additional details on setup.

- [Campaign webcasts](/handbook/marketing/virtual-events/webcasts/#campaign-webcasts)
- [Field Marketing webcasts](/handbook/marketing/growth-marketing/regional-marketing/field-marketing-owned-virtual-events/#webcasts-1)
- [Goldcast webcasts](/handbook/marketing/marketing-operations/goldcast)

**Bizible:** This is tracked as an _online_ Bizible channel as well as an _offline_ channel. We own the registration process so whenever a person registers to a webcast, a TP will be created based on the Bizible snippet that lives on our landing pages, while another TP is created for campaign members with success/responded statuses.

| Member Status | Definition | Success | Valid for list upload |
| ------------- | ---------- | ------- | ------- |
| No Action | default starting position for all records |  | No |
| Sales Invited | Invitation/Information about event sent by Sales/SDR |  | No |
| Sales Nominated | Sales indicated record to receive triggered event email sent by Marketing |  | No |
| Marketing Invited | Marketing geo-targeted email |  | No |
| Registered | Registered through online form |  | No (ask MOps for special conditions) |
| No Show | Registered, but did not attend live webcast |  | Yes |
| Attended | Attended the live webcast | Yes | Yes |
| Follow Up Requested | Requested to be followed up with by sales post event | Yes | Yes |
| Attended On-demand | Watched the recorded webcast | Yes | Yes |

#### Workshop

An in-person or virtual workshop where the attendees are guided through an agenda of real life use cases within GitLab.

For logistical setup and more information, go [here](/handbook/marketing/growth-marketing/regional-marketing/field-marketing-owned-virtual-events/#virtual-workshops-1).
**Bizible:** This is tracked as an _offline_ Bizible channel. Touchpoints for offline channels are created through our AMM (formerly known as Bizible) campaign sync rules that can be found in this [spreadsheet](https://docs.google.com/spreadsheets/d/1xR2Q7YKskfNaxclnfGOkK8Vi739zdKypQ6GgF9MLG58/edit#gid=92970564).

Program type is included on the smart campaign meant to clear `dietary restriction` related fields. 7 days after an event's program statuses are recorded, the fields are cleared automatically.

| Member Status | Definition | Success | Valid for list upload |
| ------------- | ---------- | ------- | ------- |
| No Action | default starting position for all records |  | No |
| Sales Invited | Invitation/Information about event sent by Sales/SDR |  | No |
| Sales Nominated | Sales indicated record to receive triggered event email sent by Marketing |  | No |
| Marketing Invited | Marketing geo-targeted email |  | No |
| Waitlisted | Holding state if registration is full will be moved to Registered if space opens |  | No |
| Registered | Registered or indicated attendance at the session |  | No (ask MOps for special conditions) |
| Cancelled | Registered, but cancelled ahead of the event |  | No |
| No Show | Registered, but did not attend event |  | Yes |
| Attended | Attended workshop event | Yes | Yes |
| Follow Up Requested | Requested additional details about GitLab to be sent post event | Yes | Yes |

## SFDC Campaign Instructions

SFDC campaigns have a general set of required fields. This section describes the fields and when you need to populate them. You will do this step after you sync the campaign from Marketo (or when you set-up Content Syndication/Linked In campaigns). Instructions are contained in this section so any changes to required fields are centrally located and instructions do not become out of date.

### Updating SFDC fields

- Now go to Salesforce.com and check the [All Campaigns by create date](https://gitlab.lightning.force.com/lightning/o/Campaign/list?filterName=00B4M000004oVF9) view. Sort by create date and your campaign should appear at the top. You may also search for your campaign tag in the search box. Select the campaign.
  - If your event is being managed through Accelevents, you must update the name of the SFDC Campaign. This step only applies to Accelevents managed events because all other campaign types will have the correct naming format. Click the "Edit campaign name" icon next to the campaign name and update the name to reflect our naming convention: YYYYMMDD_OwnedEventName_RegionOrCity. Do not change the name in Marketo, only SFDC.
  - Change the `Campaign owner` to your name
  - Confirm that the `Active` box is checked
  - Status should be updated according to the [chart in this section](/handbook/marketing/marketing-operations/campaigns-and-programs/#important-notes). Typically you will use "In Progress"
  - Confirm that start date and end date populated correctly (this is automated).
  - Update the `Is this an in person event` dropdown, based on `in-person` vs `virtual` type
  - Update `Budget Holder` -  Do keep in mind that the `Budget Holder` field should be updated **only if**:
    - The campaign results in offline Bizible touchpoints based on campaign type (i.e. content syndication, sponsored webcast, etc.) - **NOTE:** an offline Bizible touchpoint happens when we gather a lead offline and in order for the system to have this name you must go through a [list upload process](/handbook/marketing/marketing-operations/list-import/)
  - Update `Is a Channel Partner involved?` - You can leave this blank if "No"
    - If yes, add the `Channel Partner Name`
  - Update `Is an Alliance Partner involved?` - You can leave this blank if "No"
    - If yes, add the `Alliance Partner Name`
  - Update `Will there be MDF Funding` - You can leave this blank if "No"
    - If yes, lookup the `MDF Request` in this field: [Detailed instructions](/handbook/marketing/growth-marketing/partner-and-industry-marketing/mdf-operations-process/#step-3-add-mdf-request-on-the-salesforce-campaign)
  - Update `Integrated Campaign` if applicable
  - Update `GTM Motion` if applicable
  - If there will be `Sales Dev Invite Support` - check this box. Otherwise leave blank
  - If there will be `Sales Dev Onsite Support` - check this box. Otherwise leave blank
  - Update `Is Hyperscaler involved?` to Yes if a hyperscaler is involved.
    - If yes, add the hyperscaler partner name after the date in your campaign name. Example using Executive Roundtable: YYYYMMDD_HyperscalerPartner_ExecutiveRoundtable_Topic_Region_EventType. For more info, [see](/handbook/marketing/marketing-operations/campaigns-and-programs/#partner-campaign-setup)
    - If yes, enter the hyperscaler partner name in the `Hyperscaler` field
    - If yes, select the type of Hyperscaler Funding using `Will there be Hyperscaler Funding?`, options are `MDF` or `Credits`
      - then, update the `Hyperscaler Fund Requested Amount`
  - Update the event epic
  - Update the description (if any)
  - Enter the `Form submission page` if you know it. Otherwise, it will need to be added after the landing page is created (if applicable)
  - Update `Budgeted Cost` - If cost is $0 list `1` in the `Budgeted Cost` field. - NOTE there needs to be at least a 1 value here for ROI calculations, otherwise, when you divide the pipeline by `0` you will always get `0` as the pipe2spend calculation.
  - Update `Region` and `Sub-region`, if these are local or targeted to a specific region
  - For all SFDC campaign types run by Corporate Events or Field Marketing, please check the `High Priority` check box on the campaign level.
    - Details on our [pilot](https://gitlab.com/gitlab-com/marketing/marketing-operations/-/issues/6905) we ran with the business development team which led us to add this!

    **OR:**

    - There were GitLab Dollars spent on the campaign (Field, Digital, Corporate, Community etc.) - can be left blank in the cases when we have campaigns that do not utilize budget; - **NOTE:** By updating the budget holder, we do **NOT** run the risk of double counting touchpoints, however, do keep in mind that since the field is not always filled out, it shouldn't be used for measuring each team's performance.
- Click "Save"
- Add the Marketo program link and SFDC campaign link to the epic.

#### Instructions for SFDC campaign creation when utilizing Allocadia

Using an integration from Allocadia > Marketo > SFDC, the information you've provided in Allocadia will push to your SFDC campaign.

**Please Note:** You must NOT edit the SFDC campaign until the Allocadia connector has completed the sync. This is normally done near-real time, but if the data does not push immediately, be aware it can take minutes to hours to do so. You'll know the Allocadia connect has completed its work when you see the SFDC campaign owner change from Marketo Integration to the name of the person running the camapign, as well as well as when all details are populated from Allocadia to SFDC. If you edit the campaign before the connector pushes the data over, it will break the build and you will manually have to edit all of the fields listed. For additional Allocadia details [go here](/handbook/enterprise-data/marketing-analytics/allocadia/#salesforcecom-sfdc).

- Go to alesforce.com and check the [All Campaigns by create date](https://gitlab.my.salesforce.com/701?fcf=00B4M000004oVF9) view. Sort by create date and your campaign should appear at the top. You may also search for your campaign tag in the search box. Select the campaign.
- Confirm that start date and end date populated correctly (this is automated)
- Add `Budgeted Cost`
  - `Budgeted Cost` in SFDC pulls from your `plan` number, not your `forecast` number from Allocadia. If you do not have a plan number in Allocadia, `Budgeted Cost` will remain blank in SFDC. If you do have a plan amount in Allocadia, that amount will pull through to SFDC in the nightly sync.
  - If the cost of the tactic is $0 (example - virtual workshop) list `1` in the `Budgeted Cost` field. There needs to be at least a 1 value here for ROI calculations, otherwise, when you divide the pipeline by `0` you will always get `0` as the pipe2spend calculation.

### Parent/Child Campaigns Setup

For some tactics, there are mutiple campaigns that occur as a part of a single initiative. Some examples of these could be a conference with speaking session or ancillary event, content syndication, or hybrid events (where in-person and virtual leads will be tracked separately). When this happens, a `parent` campaign should be created in SFDC and have each `child` campaign represent the individual tactics.

Two important aspects that need to be avoided when it comes when creating/editing parent campaigns are the following:

1. Do not add any campaign members to the parent campaign as we want to minimize the risk of creating duplicate bizible touchpoints for the same activity.
1. When creating a parent campaign, it should always be named with `_PARENT` at the end of the campaign name. This is so we do not double-report on campaigns.
1. Parent campaigns shouldn't have values in the `Actual Cost in Campaign` field, while in the `Budgeted Cost in Campaign` field, do not put more than $1 value. The true Budgeted Cost & Actual Cost are to be updated only on the child campaigns and not on parent campaigns, as we should not be running any ROI on the parent campaigns.
1. If you are an Allocadia user, you will not include the sub-category ID in the parent campaign. You will only use an Allocadia ID when creating the child campaigns. Since we do not have the same parent/child relationship structure available in Marketo, you will create a folder that will house all of the shared tactics together.

#### Create a Parent SFDC Campaign

- Create your first child campaign using the [below instructions](/handbook/marketing/marketing-operations/campaigns-and-programs/#steps-to-setup-marketo-programs-and-salesforce-campaigns)
- When finished, go to the top right of the campaign and click `Clone`
- Edit the campaign name to include _PARENT at the end (example: 20250409_GoogleCloudNext_PARENT)
- Confirm the `Active` box is checked
- Remove the Allocadia Sub-Category ID
- Adjust the `Budgeting Cost in Campaign` to $1
- Click `Save`

#### How to associate a child campaign to a parent campaign in SFDC

- Log in to SFDC and search for your child campaign
- Once in the campaign, click the edit button next to the `Parent Campaign` field
- Copy and paste the parent campaign name (example: 20250409_GoogleCloudNext_PARENT) into the field or start typing the parent campaign name and click `Save`
- Continue to do the same for any additional child campaigns
- You can view your campaign hierarchy in the right-hand panel (clicking `View All` will provide a full hierarchical view)

#### Allocadia IDs and Parent/Child Campaigns

If you are an Allocadia user and you are using our Allocadia > Marketo > SFDC sync, please note that you will NOT utilize the Allocadia sub-category ID in any of your individual child campaigns. Each campaign will have its own line item ID for that particular campaign, which all roll up to the parent campaign. Examples below.

**AWS Summit London - PARENT (No Allocadia ID)**

- AWS Summit Conference/Booth - Individual Line Item ID
- AWS Summit Speaking Session - Individual Line Item ID
- AWS Summit Executive Meetings - Individual Line Item ID

**An example of a Parent/Child SFDC hierarchy can be found [here](https://gitlab.lightning.force.com/one/one.app#eyJjb21wb25lbnREZWYiOiJzZmE6aGllcmFyY2h5RnVsbFZpZXciLCJhdHRyaWJ1dGVzIjp7InJlY29yZElkIjoiNzAxUEwwMDAwMFVqMGs5WUFCIiwic09iamVjdE5hbWUiOiJDYW1wYWlnbiIsInRyZWVEaXJlY3Rpb24iOiJjdXJyZW50VG9Eb3duIiwibGF5b3V0VHlwZSI6IlJFTEFURURfTElTVCIsImxheW91dE92ZXJyaWRlIjoiQ2hpbGRDYW1wYWlnbnMifSwic3RhdGUiOnt9fQ%3D%3D).**

#### Create a Parent Marketo Program (aka folder)

- Log in to Marketo
- Go to the correct event type folder based on fiscal year and quarter (example - FY26 - Q1 Conference)
- Right click the folder and select `New Campaign Folder`
- Add the campaign name as the `Campaign Folder Name` (example - 20250409_GoogleCloudNext)
- Hit `Save`
- All Marketo programs for your event can be nested under this main folder
  - To move any existing Marketo programs to your folder you can simply drag and drop the programs, or right click the programs and select `Move` and direct to the folder you created.

An example of a Marketo program folder with nested programs can be found [here](https://engage-ab.marketo.com/?munchkinId=194-VVC-221#/classic/MF25757A1).

### Important Notes

1. The `Active` checkbox must be checked on the SFDC campaign for Marketo to be able to "see" the campaign. This will happen automatically if you follow the process below, but if there is a time you cannot find a SFDC campaign in Marketo, check to make sure that box is checked in SFDC. Additionally, if this box is unchecked, Marketo cannot send leads or update campaign member status for that SFDC campaign.
1. If you are creating a parent campaign, please make sure that the campaign name of a parent campaign reflects the fact that it's a parent, by adding `_Parent` at the end of the Campaign Name. In the event of a mishap, when a parent campaign was setup by mistake to house responded campaign members,  adding `_Parent` at the end of the campaign name, makes sure that it gets seen by our campaign sync rules that [control the generation of touchpoints for offline campaigns](https://docs.google.com/spreadsheets/d/1xR2Q7YKskfNaxclnfGOkK8Vi739zdKypQ6GgF9MLG58/edit#gid=92970564) and does not create double touchpoints for campaign members that may be housed in both the parent and child campaigns.
1. If you are creating a campaign that relies on offline touchpoint generation, please make sure to double check that the campaign type is selected appropriately and that the campaign name does not contain words like `test`, `DONTUSE`, `template`, `parent`, because based on the [campaign sync rules that govern the creation of offline touchpoints](https://docs.google.com/spreadsheets/d/1xR2Q7YKskfNaxclnfGOkK8Vi739zdKypQ6GgF9MLG58/edit#gid=92970564), these campaigns will not have touchpoints created for them.
1. We have a trigger in SFDC that stamps the start date, end date, reporting date, and fiscal quarter by taking the first 8 characters of the name of the campaign (if they are numbers) and converting that into a date (example: 20210505 == 5/5/2021, so YYYYMMDD). So, campaigns starting with a number must contain a valid date, otherwise you will receive an error.
1. Campaign statuses other than `Aborted` are automatically set by SFDC workflow based on Start and End Dates.

|Status|Definition|When does it update?|
|------|--------|--------|
|Planned|The campaign is expected and has been set up, but the start date hasn't happened yet (could also be where its pulled back to if an event is postponed)|Prior to the Campaign Start date - upon Creation|
|In Progress|The campaign has begun |On Start date|
|Aborted|Campaign has been suspended, cancelled, aborted|Manually when campaign is aborted|
|Completed|The campaign took place and has ended|After the Campaign End Date|

## Marketo Program and Salesforce Campaign set-up

The Marketo programs for the corresponding campaign types have been prebuilt to include all the possible necessary smart campaigns, email programs, reminder emails and tokens that are to be leveraged in the building of the program.

For **LinkedIn Social Ads** follow the instructions documented in [the LinkedIn section](/handbook/marketing/marketing-operations/campaigns-and-programs/#steps-to-setup-linkedin-lead-gen-form)

For **virtual events**, there are additional set up details on this [page](/handbook/marketing/virtual-events).

For **live events using Accelevents**, please follow the Marketo set-up instructions here.

For all other campaign types, follows steps below. All steps are required.

## Steps to Setup Marketo programs and Salesforce Campaigns

### Step 1: Clone the Marketo program indicated below

Be advised that some templates are being used for both `in-person` and `virtual events`. These templates have been marked as `Hybrid template`. For these templates, the naming convention is slightly different in that additional campaign information appears in the name. When naming the program, `EventType` is replaced with either `Virtual`, `In-Person`, or `Hybrid` (if an event will be both in-person and virtual).

If this is to set up a program that involves a channel partner, you must also follow the directions on that [setup page](/handbook/marketing/growth-marketing/partner-and-industry-marketing/#joint-gitlab-and-partner-campaigns). You will still clone the program from the list below to get started.

#### How to Clone the Marketo program

- Click on the appropriate template for your tactic below (you must be logged into Marketo to proceed)
- Right click on the template in Marketo and select `Clone`
- In the `Clone To` field, select `A campaign folder`
- In the `Name` field, input the campaign name (this should be the campaign name previously created in Allocadia - example: 20220704_BestEventEver)  - The date should be the START date of your campaign.
- In the `Folder` field, select the appropriate folder based on your campaign type. Most folders are also organized by fiscal year and quarter.
- In the `Description` field, paste your epic URL
- Click `Create`

#### Partner Campaign Setup

There are currently several types of partner campaigns including Channel MDF campaigns, Joint GitLab/Partner, campaigns, Hyperscaler Campaigns, and Hyperscaler Funded Campaigns.

##### Channel MDF Campaign

Channel MDF is when GitLab covers 50% of a partner initiated campaign managed by the Partner Marketing team. All leads generated belong to the Channel Partner and are under Partner Queue ownership. Channel MDF has its dedicated Marketo template, go to [this page](/handbook/marketing/growth-marketing/partner-and-industry-marketing/mdf-operations-process/) for campaign setup instructions.

#### Joint GitLab/Partner Campaign

Joint GitLab/Partner campaigns when GitLab Field Marketing team fully funds and manages the marketing campaign. Leads that are partner sourced will be routed to the channel partner however, if the BDRs/SDRs are actively working the lead then it remains in get lab ownership. If a partner receives a lead but doesn't formally accept it within 30 days (by updating their share status), our system automatically recalls that lead, marks it as "Recycled," and brings it back into GitLab's nurture program. Follow the campaign setup instruction for each campaign type below. For more information about Joint/Partner campaign go [here](/handbook/marketing/growth-marketing/partner-and-industry-marketing/#joint-gitlab-and-partner-campaigns) - ensure these steps are completed.

##### Hyperscaler Campaigns

Hyperscaler Campaigns are strategic marketing initiatives conducted in partnership with our Hyperscaler allies. These marketing activities including Executive Roundtables, Vendor-Arranged Meetings, Conferences, Owned events and more.

For campaign setup, utilize the Marketo templates available in [Hybrid](/handbook/marketing/marketing-operations/campaigns-and-programs/#hybrid-marketo-templates) and [Other Tactic](/handbook/marketing/marketing-operations/campaigns-and-programs/#other-tactic-marketo-templates) section below.

Example using Executive Roundtable: `YYYYMMDD_HyperscalerPartner_ExecutiveRoundtable_Topic_Region_EventType`

- When you manage a Hyperscaler Campaign without Funds:
  - Add the Hyperscaler Partner name after the date: `YYYYMMDD_AWS_ExecutiveRoundtable_Topic_Region_EventType`.
- When you manage a Hyperscaler Campaign with MDF from the Hyperscaler Partner:
  - Add the Hyperscaler Partner name after the date, and "MDF": `YYYYMMDD_AWS _MDF_ExecutiveRoundtable_Topic_Region_EventType`.
- When you manage a Hyperscaler Campaign with Credits from the Hyperscaler Partner:
  - Add the Hyperscaler Partner name after the date and "CR" for Credits: `YYYYMMDD_GCP _CR_ExecutiveRoundtable_Topic_Region_EventType`.

Special Instructions for Content Syndication Teams: Update the Asset Name in the Marketo token of the Content Syndication Folder to include the Hyperscaler Name

Please add a Hyperscaler Campaign, funded by Hyperscaler, to the Hyperscaler Funded Campaign folder in Marketo.

**Important Lead Ownership Note:** All leads generated through Hyperscaler campaigns remain under GitLab's excl
usive ownership. These contacts enter our standard nurturing process, accumulating lead score according to engagement metrics. Upon reaching MQL status, they're automatically assigned to the appropriate BDR/SDR team for personalized follow-up.

##### Hybrid Marketo Templates

- Executive Roundtables - `Hybrid template`: [YYYYMMDD_ExecutiveRoundtable_Topic_Region_EventType_template](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/ME6028A1)
- Speaking Session - `Hybrid template`: [YYYYMMDD_SpeakingSession_EventType_Template](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/ME5092A1)
- Vendor Arranged Meetings (1:1 meetings) - `Hybrid template`: [YYYYMMDD_ArrangedMeetingsVendorName_Region_EventType_template](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/PG5698A1)
- GitLab Hosted Workshops - `Hybrid template`:
[For virtual workshops, please follow directions in the virtual workshop set-up section.](/handbook/marketing/growth-marketing/regional-marketing/field-marketing-owned-virtual-events/#virtual-workshop-logistical-set-up) In-person workshops utilize a similar setup, but do not involve the Zoom requirements. If you have a workshop to set up that is not one of the workshops listed below, you can still utilize any of these templates for backend setup and then use a [copy doc](https://docs.google.com/document/d/1j43mf7Lsq2AXoNwiygGAr_laiFzmokNCfMHi7KNLjuA/edit#heading=h.tl82wncgutxu) to indicate all copy adjustments that are required (you will also update the baseline Marketo tokens during the setup process).
  - Project Management: [YYYYMMDD_Workshop_ProjectManagement_EventType](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/ME6536A1)
  - Security: [YYYYMMDD_Workshop_SecurityWorkshop_EventType](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/ME6521A1)
  - CI Workshop: [YYYYMMDD_Workshop_CI_EventType](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/ME6807A1)
  - GitLab Duo Agent Platform Workshop: [YYYYMMDD_Workshop_DuoAgent_EventType](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/ME16197A1)
  - GitHub GitLab Migration: [YYYYMMDD_Workshop_GitHubGitLab_EventType](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/ME13738A1)
  - GitLab Basics: [YYYYMMDD_Workshop_GitLabBasics_EventType](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/ME17530A1)
  - GitLab Platform Engineering Workshop: [YYYYMMDD_Workshop_PlatformEngineering_EventType](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/ME22364A1)

##### Other Tactic Marketo Templates

- Conference - `Virtual`: [YYYYMMDD_YYYYMMDD_Vendor_VirtualConfName1 (Virtual Conference Template)](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/ME7624A1)
- Conference - `In person`: [skip to specific setup details here](/handbook/marketing/marketing-operations/campaigns-and-programs/#steps-to-setup-in-person-conferences)
- Conference - Meetings (FM led) `In person`: [skip to specific setup details here](/handbook/marketing/marketing-operations/campaigns-and-programs/#steps-to-setup-in-person-conference-meetings)
- Content Syndicaton: [skip to specific setup details here](/handbook/marketing/marketing-operations/campaigns-and-programs/#steps-to-setup-content-syndication-in-marketo-and-sfdc)
  - Note, if you are managing a hyperscaler campaign, update the Asset Name in the Marketo token of the Content Syndication Folder to include the Hyperscaler Name.
- Direct Mail: [FY00_Q0_Brilliant Gifts Direct Mail TEMPLATE](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/PG24060A1)
- Gated Content: [YYYY_Type_Content_Template](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/PG5111A1)
- Integrated Campaign: [FY20IntegratedCampaign_Template](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/PG4924A1)
- Surveys - For templates and setup instructions for surveys, skip to specific setup details [here](/handbook/marketing/marketing-operations/campaigns-and-programs/#steps-to-setup-surveys-in-marketo-and-sfdc).
- Owned Event - `Hybrid`: [YYYYMMDD_OwnedEvent_EventType_Template](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/ME4722A1)

##### Webcasts Marketo Templates

- Zoom GitLab Hosted Webcast: [YYYYMMDD_WebcastTopic_Region](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/ME5512A1)
- Sponsored Webcast: [YYYYMMDD_ExternalWebcastVendorName_Topic_Region](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/PG5523A1)

### Step 2: Sync to Salesforce

- At the program main screen in Marketo, where it says `Salesforce Sync` "not set", click on "not set"
  - Click "Create New." The program will automatically populate the campaign tag, so you do not need to edit anything.
  - If you are a user of Allocadia, you will need to add the Allocadia sub-category ID to the `Description` field.
  - Click "Save"

### Step 3: Update Marketo tokens

- Complete the information for each token. Instructions for what to enter for each token are included in the template.
  - Note that it is important that all tokens are completed as the "Interesting Moments" Smart Campaigns pushes information to Salesforce based on the tokens. Depending on the campaign, some auto-responders and emails rely on tokens as well.
  - Note that the token for `Event Location` should be filled in with the `City` for `In-Person` events and `Virtually` for `virtual events`.
  - You do not need to update the following tokens upon setup:
    - `{{my.email header image url}}` - This is optional. You will need this if you had custom images created.
    - `{{my.ondemandurl}}` - This will be entered AFTER the event date. It is the link to the recorded webcast. You will need to come back after the event and update this token.
- Update the utm_campaign field following the process outlined [here](/handbook/marketing/utm-strategy/#the-new-utm_campaign-structure).
- If your program qualifies for Action Streams (currently only available for Security), please update the {{my.Action Stream}} token with the relevant type [here](/handbook/marketing/lifecycle-marketing/email-processes-requests/#action-streams). [Video instructions](https://drive.google.com/file/d/1hBuYcScoJGVo8VUhKbiwToSE1g4Kr8Tl/view?usp=sharing) - note the instructions are different for Conferences and our outlined in the Conference instructions below.

### Step 4: Activate Marketo smart campaign(s)

- Action Stream tagging for programs: The following is relevant for all campaign types, except Content Syndication and LinkedIn Lead Gen forms. Those are handled differently. For webcasts, workshops, events, and gated content, please follow these instructions to properly route leads to Action Streams.
  - Add the [relevant stream type](/handbook/marketing/lifecycle-marketing/email-processes-requests/#action-streams) to the {{my.Action Stream}} token
  - In the `Processing` flow, select "Execute Campaign" from the right side panel and drag it into the flow. This should go near the bottom of the flow, before any "Remove from Flow" steps.
  - Complete the `Execute Campaign` flow step: Executed Campaign: *Air Traffic Control Automation.Action Stream tagging (programs), Use Parent Campaign Token Context: True  
- If this is a `Gated Content` campaign, follow the detailed set-up instructions on the [content in campaigns page](/handbook/marketing/demand-generation/campaigns/content-in-campaigns/#steps-gated-landing-pages).
- If this is a `Vendor Arranged Meeting`:
  - Click the `Smart Campaigns` folder
  - Select the `01 Interesting Moments` smart campaign
    - The correct program should automatically apply when cloned, so _you don't need to do anything here._ However, you can confirm that the campaign
- If this is `Speaking Session` follow the below activation instructions:
  - Click the `Smart Campaigns` folder
  - Select the `01a Registration Flow` smart campaign
    - The correct program should automatically apply when cloned, so _you don't need to do anything here._ However, you can confirm that the campaign tag appears on in the Smart List and Flow. If the name of the template appears anywhere, replace it with the campaign tag.
  - Click to the `Schedule` tab and click `Activate`
  - Select the `04 Interesting Moments` smart campaign
    - The correct program should automatically apply when cloned, so _you don't need to do anything here._ However, you can confirm that the campaign tag appears on in the Smart List and Flow. If the name of the template appears anywhere, replace it with the campaign tag.
  - Click to the `Schedule` tab and click `Activate`
  - (NO ACTION) If a list is used to import registrants/attendants, the `03 - Processing - No Shows / Attendees` smart campaign will be run after the list is uploaded.
  - For `Speaking Session` also select the `02-Interesting Moments` smart campaign, click to the `Schedule` tab and click `Activate`
- If this is an `Executive Roundtable`
  - Click on the `Campaigns` folder
  - Click on `Interesting Moments`, click to the `Schedule` tab and click `Activate`
  - If you are creating a Marketo landing page for this event, click on `01 Registration Flow`, click to the `Schedule` tab and click `Activate`. If you are doing a list upload, this step is not necessary.
- If this is `Workshop` follow the below activation instructions:
  - Click the `Smart Campaigns` folder
  - Select the `00 Interesting Moment` smart campaign, navigate to the Schedule tab and select `Activate`
  - Select the `01a Registration Flow` smart campaign
  - The correct program should automatically apply when cloned, so _you don't need to do anything here._ However, you can confirm that the campaign tag appears on in the Smart List and Flow. If the name of the template appears anywhere, replace it with the campaign tag.
  - Click to the `Schedule` tab and click `Activate`
- If this is an `Owned Event` follow the below activation instructions:
  - Click the `Campaigns` folder
  - If you have a Marketo registration page for this event, select the `01b - Registration` smart campaign
  - The correct program should automatically apply when cloned, so _you don't need to do anything here._ However, you can confirm that the campaign tag appears on in the Smart List and Flow. If the name of the template appears anywhere, replace it with the campaign tag.
  - Click to the `Schedule` tab and click `Activate`
  - Select the `02a - Interesting Moments` smart campaign
  - The correct program should automatically apply when cloned, so _you don't need to do anything here._ However, you can confirm that the campaign tag appears on in the Smart List and Flow. If the name of the template appears anywhere, replace it with the campaign tag.
  - Click to the `Schedule` tab and click `Activate`
  - LIST UPLOAD ONLY: If you do not have a registration page and responses will be uploaded via a list load, MOps will activate the `02b - Manual Upload Processing` campaign if necessary.
- For all other campaign types, follow the below activation instructions:
  - Click the "Smart Campaigns" folder
  - Select the `Interesting Moments` smart campaign.
  - The correct program should automatically apply when cloned, so _you don't need to do anything here._ However, you can confirm that the campaign tag appears on in the Smart List and Flow. If the name of the template appears anywhere, replace it with the campaign tag.
  - Click to the "Schedule" tab and click `Activate`.
  - Select the `01 Processing` smart campaign. (Does not apply to Virtual Conference or External Webcast)
  - The correct program should automatically apply when cloned, so _you don't need to do anything here._ However, you can confirm that the campaign tag appears on in the Smart List and Flow. If the name of the template appears anywhere, replace it with the campaign tag.
  - Click to the "Schedule" tab and click `Activate`.

- If you do not see an `Interesting Moments` campaign, check to see if that step is in `01 Processing` or `Viewed on Demand` campaigns.
- For `Speaking Sessions` with pre-registration, find the `Pre-Registration` folder, and activate the `01 - Form Fill` step after populating the smart list with the correct form and landing page.

### Step 5: Setting Landing Page / Smart Campaign Expiration (Asset Expiration)

As of early 2022, Adobe has introduced a new feature to Marketo called `asset expiration`, which can be read about in Marketo's documentation [here](https://experienceleague.adobe.com/docs/marketo/using/product-docs/core-marketo-concepts/programs/working-with-programs/local-asset-expiration.html?lang=en#:~:text=Right%2Dclick%20on%20your%20desired,Choose%20an%20expiration%20date). This applies to smart campaigns and landing pages. For GitLab's use case, we have enabled this feature for the following role permissions: `Field Marketing User`, `Marketing Program Managers` and `Marketing User`. If you do not have these permissions would like this feature enabled, please submit an `access request`.

#### Asset Expiration Use Cases

All programs have different necessities so it will be important to determine how `asset expiration` should be utilized for various program types. Guidance can be supplied by MktgOps, if needed, but utilize this method for the majority of cases:

- `Conference`, `Direct Mail`, `Executive Roundtable`, `Owned Event`, `Speaking Session`, `Sponsored Webcast` (if no on-demand component), `Survey`, `Vendor Arranged Meeting`, `Workshop`: For one-time programs that are completely done after a specific date and will not use an `Attended On-Demand` member status over time, set the expiration of assets at 4 weeks after the event and at the end of the day, so at 23:55 PST. For example, if a `conference` or `executive roundtable` program type occurs on the April 3, schedule asset expiration for end day on May 1.
- `Content syndication` or Campaigns where the end of the campaign is difficult to pinpoint: there are 2 different options to consider:
  - Set up expiration **12 weeks after the estimated campaign end**, again at the end of the day. This is useful for campaigns where a third-party is handling lead collection for us and we are manually uploading lead lists. This also supplies a buffer in the event the SLA is not met on schedule and the campaign runs longer than anticipated.
  - **Do not use asset expiration at all**. We often have content syndication focused programs that go on indefinitely so expiration does not make sense to utilize in this case. Assets can be discontinued in the future.
- `Gated Content`: It is not recommended to use asset expiration as these remain in use for long periods of time.
- `Webcast`: It is not recommended to use asset expiration as these typically have an on-demand component.

#### Setting Asset Expiration On A Program

- Right click the Marketo program to open the program menu and select `Set local asset expiration`. Please note, this will not work without the correct permissions.
- A menu with all expiration capable assets will be shown as a segmented list. Example assets that can appear are `landing pages`, `active trigger campaigns` and `Reocurring batch campaigns`.
- Use the asset checkboxes to select all assets you wish to set an expiration for and select `set expiration` when ready. Assets that should be expired are `landing pages`, `active trigger campaigns` and `Reocurring batch campaigns`. Set your date and time and then submit.
  - Prioritize setting expirations on  `smart campaigns`.
  - Be mindful of which smart campaigns are set to expire and when because such an event will disable program `registation` and `on-demand` flows.
- To remove expirations at a later date, right click on the program to return to the capable assets and submit changes.

### Step 6 Setting up optional self-service cancellation

*This option is only available on specific program templates: the Owned Event template and the Executive Roundtable template. Workshop templates may be added at a later time._ When a person fills out the cancellation form, their status in the program is updated to cancelled and an alert is sent to the event owner listed in the tokens. If the person cancels using a different email address, they will be added to the campaign as cancelled and the event owner will need to update the original registration to cancelled.

- Self-service cancellation should always be utilized for Field Marketing's Owned Event and Executive Roundtable programs.
- Included in the mentioned templates are 2 landing pages and 2 email templates - in the `Self Service Cancellation Assets` folder. To provide a self-service option for recipients to cancel their reservation, these landing pages and email templates will need to be updated.
- Grab the URL of the `Cancel Page` landing page and place it in the token called `my.cancellation page`. **If this is not done, the link included in the registration confirmation email will be broken**.
- Activate the `01 Cancellation Flow` smart campaign
- For the `Send Alert` step, determine the preferred internal GitLab email address that will receive the cancellation alert. This flow step alert notifies stakeholders of cancellations. If only one email should be notified, fill in the {{my.event owner email address}} token in the program tokens with the appropriate email. If more than one email should be notified, change the token as previously described - then within the `3 - Send Alert` flow step, add each additional email to the `To Other Emails` field after the token, with each email separated by a comma
- Activate asset expirations for 2-3 days after the event is over for all live cancellation assets

### Step 7: Update the Salesforce campaign

Refer to instructions [above](/handbook/marketing/marketing-operations/campaigns-and-programs/#step-5-update-the-salesforce-campaign).

### Step 8: Update the Salesforce campaign - Using Allocadia

Please refer to the instructions [above](/handbook/marketing/marketing-operations/campaigns-and-programs/#instructions-for-sfdc-campaign-creation-when-utilizing-allocadia).

#### Training Videos for Setting up SFDC Campaign - Using Allocadia

- [Instructional Video](https://youtu.be/1681EBw5344)
- [Sync Results Video](https://youtu.be/PocOPnJY4w0)

### Waitlist processing - Owned Event, Workshop, Webcasts

If you need to change an event from registration to waitlist, or you want to start off with a waitlist, use these instructions.

- Confirm that the email copy you would like to use is set-up in the `Confirm - Waitlist` email. This email uses tokens and should be set for you, but you can customize as necessary.
- Confirm that the `{{my.event owner email address}}` is completed in the tokens section. The Waitlist program will send an alert to this email address so you know each time someone is added to the waiting list based on this token.
- Deactivate the `01b Registration` Smart Campaign
- Activate the `01a Waitlist` Smart Campaign
- Activate the `01c Waitlist to Registered` Smart Campaign
- If you would like to send notification to a registrant if they are unable to be accommodated at an event, activate the `01d Waitlist to Declined` Smart Campaign. If no notification is required, you can still use the `Declined` status and no notification will be sent. You must provide email copy to use this option.
You have now activated the waiting list processing. If you need to reactivate Registration, you will deactivate the Waitlist campaigns, and reactivate `01b Registration`.

### Moving from Waitlist - Owned Event, Workshop, Webcasts

Use these instructions to move people from the waiting list to Registered or Declined.

Waitlist > Registered

- Click on the Marketo program (the name of the campaign)
- Click on `Members`
- Change the filter to `Waitlisted`
- Click on the person/people you would like to move to Registered. They will highlight when they are selected.
- Click on `Change Status`
- Select `Registered`

Once you click `Registered`, the status will change and the `01c Waitlist to Registered` Smart Campaign will send the Registration Confirmation email.

Waitlist > Declined

- Click on the Marketo program (the name of the campaign)
- Click on `Members`
- Change the filter to `Waitlisted`
- Click on the person/people you would like to move to Registered. They will highlight when they are selected.
- Click on `Change Status`
- Select `Declined`

Once you click `Declined`, the status will change and if activated, the `01d Waitlist to Declined` Smart Campaign will send the notification email. Note that you must provide email copy if you would like a notification to be sent.

### Post Event Processing for Waitlisted Members - Owned Event, Workshop, Webcasts

In the situations where you have an event that had the waitlist feature turned on and you had hit capacity, follow these steps to process waitlisted leads. After you've processed the No Show + Attended leads you will need to process the Waitlisted leads since they technically are neither `Attended` or `No Show`. The important thing here is that we don't want them receiving follow-up emails for No Show or Attended. Please follow these steps to ensure no emails are sent and interesting moments and behavior scores are updated.

- Click on the Marketo program (the name of the campaign)
- Navigate to the `Campaigns Folder`
- Navigate to the `01c Waitlist to Registered` campaign.
- Navigate to "Schedule" and click `Deactivate`
- Navigate to the `01d Waitlist to Declined` campaign.
- Navigate to "Schedule" and click `Deactivate`. Only do this if the campiagn is currently active. If the button says `Activate`, do nothing here.
- Navigate back to the `Member list` for the event.
- Filter Status to `waitlisted` or click on the person/people you would like to move to Registered. They will highlight when they are selected.
- Click on `Change Status`
- Select `Registered`
Once you click `Registered`, the status will change and the `Interesting Moments` & `behavior score` will be updated and NO Registration Confirmation email will be sent. After this is complete and they are moved to a registered stats, we can still send them a follow up email, based on the registered status. You will need to complete a no show, attended, and registered (all separate copy) email issues.

### Setting up a controller Marketo program for a muti-day event

This is an optional feature for anyone looking to run an event on multiple days while using the same form and landing page for all included days - but with each day having its own Marketo programs/SFDC campaigns. Note this streamlined workflow exists on only 2 templates at the moment but work similarly on both templates: [YYYYMMDD_EventName_Webcast_On24_template](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/ME12620A1) and [YYYYMMDD_WebcastTopic_Region](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/ME5512A1). If there is demand, this can be requested for other program templates via an issue.

- First, determine the number of days needed for your event. If the event requires anything different than 3 days, complete as much setup as possible following the below directions and then ping MktgOps on your current issue so we can finish the setup. The intention here is to allow for use of a tokenized global form rather than individual forms for each program. The form is `FORM 1419: Webcast_MultipleTimeSlots`. If your event requires a different number of days, MktgOps needs to clone `1419` and change the number of days allotted in the dropdown
- Clone the program template you will need for as many days as your multi-day event will require - then clone one more and name the extra program as your `controller` program - with a name that somewhat alludes to your child programs. Keep all of your programs near each other and within the same Q1/2/3 or Q4 folder, if possible. Be sure to list the programs in play in the issue if you require finishing touches by MktgOps
- In the `controller` program, add `FORM 1419: Webcast_MultipleTimeSlots` to the Marketo landing page. `FORM 1419` is tokenkized with these local program tokens: `Date 1`, `Date 2`, `Date 3`, `Date 1 Option`, `Date 2 Option` and `Date 3 Option`. Fill in the `Date` tokens with the time, date and timezone **exactly** as they should appear on the dropdown menu on the landing page. The dropdown will appear on the landing page for users to select, so formatting is important. Fill in the `Option` tokens with a keyword relating to your individual multi-day events. e.g. `Day 1 = Aug 23 7:00` and `Day 2 = Sept 1 5:00` so `Day 1 Option = August` and `Day 2 Option = September`. There cannot be overlapping information on the `Option` tokens as they are part of some `contains` logic in the processing smart campaign
- Speaking of that, still in the `controller` program, move on to the smart campaign `01 Registration Flow (Multi-timeslot)`. The rest of this setup continues to be similar as a regular program set up. Click on `Flow` and scroll down to `step 3`. Change `Option 1`, `Option 2` and `Option 3` to match the keywords from the `Date 1/2/3 Option` tokens. This will add leads to static lists for safe keeping. It will also help monitor for errors. If your events only span 2 days, remove `Option 3` and if there are more than 3 days MktgOps will handle adding more days as this requires more logic and tokens
- On `Flow Step 4`, again change the `Option 1/2/3` to match your token keywords. In the `Requested Campaign` field, find the `registration` smart campaigns from your `child` programs and plug them in here. Be careful to select the correct smart campaigns here. Their names will start with the name of the child campaign but they will all have the same or similar smart campaign name of `01a Registration Flow - Form fill`
  - Note, the registration processing smart campaigns in the children programs **need to be activated** in order to appear as a `request campaign` option in the `controller` program's `Multi-timeslot` smart campaign
- Note there is an alert that will be set to an email of your choosing if there is something arry with the registration flow
- On the controller campaign there is nothing left to set up. Activate the appropriate processing smart campaigns on your child programs (busy as usual), including all needed processings, such as `Interesting moments`, `Attended` flows, `Follow up Requested`, etc. Remember to sync the child campaigns to sfdc, but there is no need to sync the `controller` program to sfdc as it does not house program members with relevant program statuses

### Setting up assets for Late/In-person Registration

This is an _optional_ feature only available for the `Owned Event` program template. Utilize this feature if a team wants flexibility to `register` unregistered attendees that have appeared `in-person` to an `owned event` but the normal registration process through the landing page form has been prevously closed down. **The teams in charge of the event should agree on whether to use this feature _before_ the event and setup should be done prior to when the event starts**. This allows the landing page/form to be manually added as a bookmark on `check-in` devices, such as on GitLab owned `tablets` and `laptops`.

- Locate the `Late Registration Assets` sub-folder found in the `Assets` folder. This only exists in the `YYYYMMDD_OwnedEvent_EventType_Template` template
- Request in the MktgOps Slack channel that someone with the needed permissions to approve Marketo program assets activate the `Late Registration page` and `Late Thank you page` landing pages. These are by default `not` approved in the program template. Be sure to check beforehand for anything that needs to be changed, such as the included `form` on the landing page.
  - It's highly suggested to change the landing page URL to something short and easier to type before approving the landing page, e.g. `https://page.gitlab.com/EventNameLateReg.html`
- Take the `Late Registration page` URL and place it in the program `token` named {{my.late registration page}}, leaving out the `https://`. This allows there to be a circular pattern on the registration `Thank you` page. The `Thank you` page displays a return link to the `late registration page` for the next registrant to utilize
- Activate the `01 Late Registration` smart campaign to activate the flow
- Right click on the program to set up the asset expiration dates for **all** `late registration` assets. These are not meant to be left on and should be set to expire the day after the event ends or when it is estimated no more regsitrants will be accepted
- Share the `late registration page` URL with the appropriate team participating in the upcoming event so the page can be added to check-in devices, such as GitLab owned `tablets` and `laptops`, where it can be accessed on the event floor with ease

## Steps to Setup in-person Conferences

### Step 1: Clone this program

- [Clone this program](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/ME12196A1)
- Use format `YYYYMMDD_Hyperscaler(if applicable)_Conference_EventType`
- Note that if you are using Jifflenow for setting Executive Meetings or Booth Demos/Meetings, you will need a Marketo program and SFDC campaign for each type. They are all `Conference` campaign types, so you can create the first one following these instructions (including filling out the tokens), then clone that program. That will make it so you don't need to complete all of the tokens each time (you will need to make minor modifications, but they are quicker this way). You will sync each program to SFDC to create the SFDC campaign as described below.

### Step 2: Sync to Salesforce

- At the program main screen in Marketo, where it says `Salesforce Sync` with "not set", click on "not set"
  - Click "Create New." The program will automatically populate the campaign tag, so you do not need to edit anything.
  - If you are a user of Allocadia, you will need to add the Allocadia ID sub-category ID to the `Description` field.
  - Click "Save"

### Step 3: Update Marketo tokens

- Update all tokens as they feed the email and interesting moments
  - You do not need to update `Request` tokens if there are no meetings being set up for the conference
  - If you are scheduling in person meetings, be sure to update the `reply email` token. This is used in the confirmation email. You need to add the correct email address for cancellations or special accomodations, and update the subject to something descriptive. Keep the `%20` between each word in the subject so the subject populates correctly.
  - If your program qualifies for Action Streams (currently only available for Security), please update the {{my.Action Stream}} token with the relevant type [here](/handbook/marketing/lifecycle-marketing/email-processes-requests/#action-streams).

### Step 4: Activate Marketo smart campaign

- `00 Send Sales-Driven Invite` (optional) can be turned on and scheduled to send on a reoccurring basis if sales and XDRs are going to be inviting people to the conference. This is not required on all campaigns and should be activated after building the Sales-Driven email. After scheduling, Sales can add someone to the campaign in SFDC and that person will be automatically sent an email invite. There is a separate email for sales invites listed in the `email` folder
- `01 Manual upload processing` this will be activated by MOps if a manual upload is required. If you upload using the self-service process, this is not required.
- `02 Add as Marketing Invited` should only be used if XDRs are planning to follow up and drive attendance to the event. This should be scheduled AFTER the first email invite is scheduled to send. It will update everyone who had the email invite sent to them as `Marketing Invited`. They will be updated in the campaign and visible in SFDC. **Do not use this unless there is planned event drivers**
- `03 Interesting Moments` Activate this campaign. This should be turned on before any lists are uploaded.
- `04 Action stream processing` If your conference covers a relevant [Action Stream topic](/handbook/marketing/lifecycle-marketing/email-processes-requests/#action-streams), be sure you added the Action Stream to the tokens, then activate this campaign.

### Step 4a. Meeting Request Processing

These steps are not yet configured. If you are planning to do this for your next event, please create an issue with the Marketing Operations team.

### Step 4b. Set-up Asset Expiration

- Right click the Marketo program to open the program menu and select `Set local asset expiration`. Please note, this will not work without the correct permissions.
- A menu with all expiration capable assets will be shown as a segmented list. Example assets that can appear are `landing pages`, `active trigger campaigns` and `Reocurring batch campaigns`.
- Use the asset checkboxes to select all assets you wish to set an expiration for and select `set expiration` when ready. Assets that should be expired are `landing pages`, `active trigger campaigns` and `Reocurring batch campaigns`. Set your date and time and then submit.
  - Prioritize setting expirations on  `smart campaigns`.
  - Be mindful of which smart campaigns are set to expire and when because such an event will disable program registation flows.
- To remove expirations at a later date, right click on the program to return to the capable assets and submit changes.

### Step 5: Update the Salesforce campaign

Refer to instructions [above](/handbook/marketing/marketing-operations/campaigns-and-programs/#step-5-update-the-salesforce-campaign).

- Add the Marketo program link and SFDC campaign link to the epic.
- If the program is being ran by Digital Marketing, add the SFDC campaign under the parent campaign `Demand Gen Pulishers/Sponsorships`

If utilizing Allocadia, please refer to the instructions [above](/handbook/marketing/marketing-operations/campaigns-and-programs/#instructions-for-sfdc-campaign-creation-when-utilizing-allocadia).

## Steps to Setup in-person Conference Meetings

The instructions below are designed for meetings led by Field Marketing at large conferences.

### Step 1: Clone this program

- [Clone this program](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/ME17801A1)
- Use format `YYYYMMDD_Hyperscaler(if applicable)_Conference_ExecutiveMeetings`
- Note that if you are using Jifflenow for setting Executive Meetings or Booth Demos/Meetings, you will need a Marketo program and SFDC campaign for each type.

### Step 2: Sync to Salesforce

- At the program main screen in Marketo, where it says `Salesforce Sync` with "not set", click on "not set"
  - Click "Create New." The program will automatically populate the campaign tag, so you do not need to edit anything.
  - If you are a user of Allocadia, you will need to add the Allocadia ID sub-category ID to the `Description` field.
  - Click "Save"

### Step 3: Update Marketo tokens

- Update all tokens as they feed the email and interesting moments. Don't skip the epic token because it is included in the internal alert.
  - Be sure to update the `reply email` token. This is used in the confirmation email. You need to add the correct email address for cancellations or special accomodations, and update the subject to something descriptive. Keep the `%20` between each word in the subject so the subject populates correctly.
  - If your program qualifies for Action Streams (currently only available for Security), please update the {{my.Action Stream}} token with the relevant type [here](/handbook/marketing/lifecycle-marketing/email-processes-requests/#action-streams).

### Step 4: Activate Marketo smart campaign

- `00 Send Sales-Driven Invite` (optional) can be turned on and scheduled to send on a reoccurring basis if sales and XDRs are going to be inviting people to the conference. This is not required and the email needs to be updated before scheduling. After scheduling, Sales can add someone to the campaign in SFDC and that person will be automatically sent an email invite. There is a separate email for sales invites listed in the `email` folder
- `01 Manual upload processing` this will be activated by MOps if a manual upload is required. If you upload using the self-service process, this is not required.
- `02 Add as Marketing Invited` should only be used if XDRs are planning to follow up and drive attendance to the event. This should be scheduled AFTER the first email invite is scheduled to send. It will update everyone who had the email invite sent to them as `Marketing Invited`. They will be updated in the campaign and visible in SFDC. **Do not use this unless there is planned event drivers**
- `03 Interesting Moments` Activate this campaign. This should be turned on before any lists are uploaded.
- `01a Meeting Request Processing` Activate this campaign if you have a landing page. Do not activate it if you are only uploading leads.
- `04 Action stream processing` If your conference covers a relevant [Action Stream topic](/handbook/marketing/lifecycle-marketing/email-processes-requests/#action-streams), be sure you added the Action Stream to the tokens, then activate this campaign.

### Step 4b. Set-up Asset Expiration

- Right click the Marketo program to open the program menu and select `Set local asset expiration`. Please note, this will not work without the correct permissions.
- A menu with all expiration capable assets will be shown as a segmented list. Example assets that can appear are `landing pages`, `active trigger campaigns` and `Reocurring batch campaigns`.
- Use the asset checkboxes to select all assets you wish to set an expiration for and select `set expiration` when ready. Assets that should be expired are `landing pages`, `active trigger campaigns` and `Reocurring batch campaigns`. Set your date and time and then submit.
  - Prioritize setting expirations on  `smart campaigns`.
  - Be mindful of which smart campaigns are set to expire and when because such an event will disable program registation flows.
- To remove expirations at a later date, right click on the program to return to the capable assets and submit changes.

### Step 5: Update the Salesforce campaign

Refer to instructions [above](/handbook/marketing/marketing-operations/campaigns-and-programs/#step-5-update-the-salesforce-campaign).

If utilizing Allocadia, please refer to the instructions [above](/handbook/marketing/marketing-operations/campaigns-and-programs/#instructions-for-sfdc-campaign-creation-when-utilizing-allocadia).

## Steps to Setup Content Syndication in Marketo and SFDC

### Step 1: Clone this program

[Clone this program](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/PG5149A1).

- Use format `YYYY_Vendor_NameofAsset`
- If the content syndication is part of a package with an external vendor, promoting several assets or webcasts, keep all of the Marketo programs together in a folder for easy access as part of a single vendor program.

### Step 2: Sync to Salesforce

- At the program main screen in Marketo, where it says `Salesforce Sync` with "not set", click on "not set"
  - Click "Create New." The program will automatically populate the campaign tag, so you do not need to edit anything.
  - If you are a user of Allocadia, you will need to add the Allocadia ID sub-category ID to the `Description` field.
  - Click "Save"

### Step 3: Update Marketo tokens

- Change the `Content Title` to be the title as it appears in the Content Syndication program
  - If you have multiple assets, you can add additional tokens by dragging the text token into the main window and naming it (for example Content Title2)
- Change the `Content Type` to be the type of content
  - The only available options are `Whitepaper`, `eBook`, `Report`, `Video`, or `General`
  - If you add a Content Type value other than the above, the record will hit an error when syncing to Salesforce because these are the only currently available picklist items for `Initial Source`

### Step 4: Activate Marketo smart campaign

- `02 Interesting Moments` If you have multiple assets, you can create different interesting moments to indicate which asset was downloaded. To do this, click on Flow. In step 1 (Interesting Moment), click Add Choice. Choice 1 will appear. Select If `Last Event Notes` contains [name of asset]. Then, Type: Milestone, Description: Enter the Interesting Moment that you would like to appear. You can do this for as many assets as you have. Activate this campaign. This should be turned on before any lists are uploaded.
- Click to the "Schedule" tab and click `Activate`. It should be set that a person can only run through the flow once.
  - IMPORTANT: When you do your list upload, you must use the exact same wording in the `Last Event Notes` field so the automation will trigger. For example, you can say `Downloaded Guide to Software Supply Chain Security` in the Last Events Notes field. In Marketo, you can use `software supply chain` in the choice and the correct Description will trigger. Do not use the same string of words in your choices. You can see an example of the Interesting Moments set-up in the flow of [program](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/SC21549C3ZN19). Disregard the rest of the processing as our process has changed.
- `01 Manual upload processing` - this will be activated by MOps if it is required. It will only be used on a manual upload and is not necessary if you use the self-service upload process.
  - When the leads are loaded to the campaign, the leads will immediately have an interesting moment, +15 score, and initial source, person source and person status update as needed.
- If your assets are for Finserv or PubSec, you need to add the SFDC campaigns to nurture processing to make sure people go into the current nurture program.
  - For Finserv: Update the Smart Lists for [00d - Add to Finserv nurture](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/SC62869A1ZN19) and [Vertical check](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/SC64233B2ZN19)
  - For PubSec: Update the Smart Lists for [Nurture - PubSec check](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/SC64118A1ZN19), [00 - Add to PUBSEC](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/SC24342A1ZN19), and [PubSec - Action Stream check](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/SC64194A1ZN19)

### Step 4a: Set-up Asset Expiration

- `Content syndication` or Campaigns where the end of the campaign is difficult to pinpoint: there are 2 different options to consider:
  - Set up expiration **12 weeks after the estimated campaign end**, again at the end of the day. This is useful for campaigns where a third-party is handling lead collection for us and we are manually uploading lead lists. This also supplies a buffer in the event the SLA is not met on schedule and the campaign runs longer than anticipated.
  - **Do not use asset expiration at all**. We often have content syndication focused programs that go on indefinitely so expiration does not make sense to utilize in this case. Assets can be discontinued in the future.

#### Setting Asset Expiration On A Program

- Right click the Marketo program to open the program menu and select `Set local asset expiration`. Please note, this will not work without the correct permissions.
- A menu with all expiration capable assets will be shown as a segmented list. Example assets that can appear are `landing pages`, `active trigger campaigns` and `Reocurring batch campaigns`.
- Use the asset checkboxes to select all assets you wish to set an expiration for and select `set expiration` when ready. Assets that should be expired are `active trigger campaigns` and `Reocurring batch campaigns`. Set your date and time and then submit.
  - Prioritize setting expirations on  `smart campaigns`.
  - Be mindful of which smart campaigns are set to expire and when because such an event will disable program registation flows.
- To remove expirations at a later date, right click on the program to return to the capable assets and submit changes.

### Step 5: Update the Salesforce campaign

Refer to instructions [above](/handbook/marketing/marketing-operations/campaigns-and-programs/#step-5-update-the-salesforce-campaign).

- Add the Marketo program link and SFDC campaign link to the epic.
- If the program is being ran by Digital Marketing, add the SFDC campaign under the parent campaign `Demand Gen Pulishers/Sponsorships`

If utilizing Allocadia, please refer to the instructions [above](/handbook/marketing/marketing-operations/campaigns-and-programs/#instructions-for-sfdc-campaign-creation-when-utilizing-allocadia).

## Steps to Setup Surveys in Marketo and SFDC

**Please Note: Once you have created your survey program, please ping Marketing Ops in the `#mktops` Slack channel and link your program for review. Each survey is unique and may require tweaks to the setup.**

### Step 1: Clone program template

- [General survey template](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/PG6402A1)
- Use format `YYYY_MM_SurveyName`

### Step 2: Sync to Salesforce

- At the program main screen in Marketo, where it says `Salesforce Sync` with "not set", click on "not set"
  - Click "Create New." The program will automatically populate the campaign tag, so you do not need to edit anything.
  - If you are a user of Allocadia, you will need to add the Allocadia ID sub-category ID to the `Description` field.
  - Click "Save"

### Step 3: Create issue for lead upload

- If the survey requires a manual upload via a list upload, focus attention on updating the `01 Processing` batch smart campaign. For manual list uploads, the batch will be activated manually by MktgOps during the upload process.
- If the survey requires a Zapier automation, consult MktgOps [via issue](https://gitlab.com/gitlab-com/marketing/marketing-operations/-/blob/master/.gitlab/issue_templates/zapier_connection_request.md) on building out the automation, MktgOps will also be the ones to activate the `01 processing` campaign

### Step 4: Update the Salesforce campaign

- Refer to instructions [above](/handbook/marketing/marketing-operations/campaigns-and-programs/#updating-sfdc-fields).
- Add the Marketo program link and SFDC campaign link to the epic.

If utilizing Allocadia, please refer to the instructions [above](/handbook/marketing/marketing-operations/campaigns-and-programs/#instructions-for-sfdc-campaign-creation-when-utilizing-allocadia).

### Step 5: Troubleshooting

1. Look at the `Results` tab of the smart campaign, if there are errors, you will clearly see them there.
1. If the lead is not pushing to SFDC? Make sure that the `Person Source` is not `SurveyName`
1. If existing leads are not being pulled into the program, it is likely the `SurveyName` field is capturing the wrong name.
1. If net-new leads are not being pulled into the program, it is likely the `Person Source` SurveyName was not updated correctly.

## Steps to Setup Direct Mail Campaigns

Note that Direct Mail campaigns require the use of Qualified, Marketo and Brilliant Gifts. Brilliant Gifts, our merch vendor, needs to set up a Preferred Gift campaign on their end, which can take up to a month and requires contacting their support. The current Qualified tech owner will be required to set up the Qualified meeting booking link. Refer to the [tech stack](https://gitlab.com/gitlab-com/www-gitlab-com/-/blob/master/data/tech_stack.yml) for the appropriate contacts. The Marketo template has been set up in a way to be easily cloned, so move slowly and carefully during set up

### Step 1: Create the Marketo program and Salesforce campaign

- Clone the [#TEMPLATE - FY00_Q0_Brilliant Gifts Direct Mail TEMPLATE](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/PG24060A1) into the appropriate folder and rename the program. If the intention is to run in ONE region, clone once. If the intention is to run in multiple regions and there's desire for tracking each region individually, clone enough programs for all regions (e.g. AMER, APJ, EMEA) and place in their own `FYXX_QX` folder under the primary [Brilliant Gifts program's folder](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/PG28387A1). Keep the naming convention similar for the regional/child programs but add a region tag at the end of the program name (e.g. `FY00_Q0_Campaign_AMER`). 
- Sync ALL programs to SFDC
- Note a few aspects of the template: The [01 - Processing](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/SC63769A1ZN19) smart campaign only fires on certain program statuses and [ONLY IF THE LEAD APPEARS IN THE TARGET LIST](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/SL53588098A1LA1). The target list can be swapped, if needed, but the processing smart campaign MUST be updated. In the flow, only the `Meeting Attended` status will send a lead to the primary Brilliant program's static list. A new static list will need to be created under the [primary Brilliant program](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/PG28387A1) under the appropriate `FYXX_QX` folder and added to flow step 6 for each cloned program. Flow step 4 will add the lead to the primary Brilliant program under `Invite Sent` status, but the static list will be used for longterm tracking and cleaning within the primary program
- Note: The primary Brilliant connected program appears as this campaign in SFDC: [Direct_Mail_eGift_Global - Brilliant connected](https://gitlab.lightning.force.com/lightning/r/Campaign/701Qq00001Pkt5sIAB/view). Program/Campaign statuses relating to shipping info can be observed on either the Marketo program or the SFDC campaign 

### Step 2: Set up the Marketo programs

- Fill out the required program tokens. A token unique to this program type is the `my.qualifiedlink` token, which appears in the `Sales Nominated Invite` email. The Qualified link will be shared by the Qualified technical owner when it is ready (more on that below)
- The program receives `Meeting Booked` and `Meeting Attended` inputs from Qualified and the Processing smart campaign calls the webhook to Brilliant to send the gift redemption email (only if the program status is `Meeting Attended`) 
- Activate `03 Change to No Show` on the single or parent program to register `no show` activities * Feature is experimental at the moment

### Step 3: Target lists and loading nominated leads

The program template contains a target list smart list asset. It is recommended to consult with MktgOps for this stage.

- To plan the target list(s), use `Target List NEW`. If there is another smart list being used for the target list, update where needed in the processing smart campaign(s)
- It is recommended to add all of the target list to the cloned program under the status `Nominated`

### Step 4: Emailing target list

While the smart campaign `02 Send Sales Nominated Invite` exists in the template, it's possible other methods of outreach will be used. `02a Sales Nominated Invite Sent` exists as a method of changing the program status on leads already emailed. Plug in the correct email asset that was sent to change the program status using this smart campaign - or request a report and MktgOps will assist with processing the report

### Step 5: Brilliant Set Up

This step will require communication to the Brilliant support team and can take up to over a month to fulfill. Reach out to the Brilliant tech owner, who will email (with the requester CC'd) our Brilliant contact. From there, the Brilliant team will ask a series of questions to the requester regarding the intended campaign and discuss set up. A few items that will be decided upon:

- Do we require a new Preferred Gift campaign?
- Is the Brilliant storefront established and adequate for this campaign's needs?
- What backend assets in Brilliant need to be updated? e.g., branded gift redemption emails

The Brilliant team also needs to verify the Marketo program and webhook are reaching their backend

Note: MktgOps will need to verify the webhook is working by utilizing [Call to Brilliant TEST](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/SC76999A1ZN19) found in the main program. There are two smart campaigns involved because a smart campaign requesting a webhook needs to be a trigger based smart campaign, not a batch smart campaign. The TEST smart campaign links to the only smart campaign capable of calling to Brilliant's webhook: [Send to Brilliant webhook do not alter](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/SC77009A1ZN19)

### Step 6: Qualified-powered meeting booking set up

This next step will require the help of the Qualified tech owner. Supply them with the SFDC campaign being used for the campaign (the cloned one, not the primary Brilliant program). From there, a Qualified link will be created and shared by the tech owner to the requester. The link will be used during prospect outreach as the method needed for nominated prospects to book a meeting with Sales Dev

- Qualified will change program status to `Meeting Booked` when a prospect books a meeting
- A reminder email will be sent about the meeting 1 hour before the time
- Once a meeting has occurred, Qualified will send a confirmation email to Sales Dev team member to confirm if the meeting happened or was missed
- An experimental automation is watching for if Qualified updates the meeting acitivty with `not attended` to mark as `no show`

### Step 7: Campaign completion

At the end of the campaign, request the Qualified logic be taken down. Updates to Brilliant storefronts and preferred campaigns TBD, but each new campaign will require checking in with Brilliant to update e-gift value and the confirmation email

## Steps to Setup LinkedIn Lead Gen Form

We have listeners set up in Marketo listening certain parameters. Please check the `Marketo Listener` column below to see if a program is already set up in Marketo. If it is, you do not need to create a new listener, you only need to add the content to the program. Otherwise, please follow the process outlined below to ensure leads are being captured.

**Active or in progress campaigns**

| Campaign                                 | Campaign Parameter for Tracking |Marketo Listener?|
|------------------------------------------|---------------------------------|-----------------|
| Digital Retargeting                     | fy27_rtg                          |[Yes](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/PG16666A1) |
| Digital Retargeting                         | fy26_rtg_global               |[Yes](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/PG16666A1)|
| ABM - DevSecOps                    | abmkey_devsecops                       | [Yes](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/PG16770A1) |
| ABM - DevOps GTM                    | abmkey_devopsgtm                     |[Yes](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/PG16770A1)  |
| ABM - DevSecOps Plat                              | abmkey_devsecopsplat   |[Yes](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/PG16770A1)|
| Digital Contact Us                       | fy27_rtg_2026_scaled_contactsales_amer |[Yes](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/PG26750A1)|
| Digital Contact Us Free to Paid       | fy27_rtg_2026_scaled_f2pcontactsales_amer  |[Yes](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/PG26851A1)|

**Deactivated or old campaigns, no longer in use** These listeners are no longer active and would need to be set-up prior to running a LinkedIn campaign for them.

| Campaign                                 | Campaign Parameter for Tracking |Marketo Listener?|
|------------------------------------------|---------------------------------|-----------------|
| Version Control & Collaboration Use Case | vccusecase                      |  |
| Simplify DevOps                          | simplifydevops                  |  |
| Jenkins                                  | cicdcmp2                        |      |
| Increase Operational Efficiencies           | operationalefficiences          ||
| Deliver Better Products Faster           | betterproductsfaster            ||
| Reduce Security and Compliance Risk       | reducesecurityrisk              ||
| CI Build & Test Auto                       | cicdcmp3                        ||
| OctoCat                                   | octocat                         ||
| DevSecOps Use Case                       | devsecopsusecase                | |
| AWS                                       | awspartner                      ||
| GitOps Use Case                          | iacgitops                       | |
| DevOps GTM                               | devopsgtm                        | |
| AutoSD                                    | autosd                          | |
| DevSecOps Platform                        | devsecopsplat                   | |
| Security & Compliance                     | seccomp                         | |
| CI Use Case                               | singleappci                     | |
| PubSec - DevOps GTM only                  | amer-pubsec                     | |

If this form is in a different language, make sure that the LinkedIn Form has that exact language in the form name (as spelled below). We currently support:

- Japanese
- Italian
- French
- Spanish
- Korean
- German
- Portuguese

When someone fills out these forms, they will be automatically added to the [Language Segmentation](/handbook/marketing/marketing-operations/marketo/#segmentations) allowing them to receive messages in their local language.

### Create LinkedIn Lead Gen Form in LinkedIn (digital marketing)

- Clone the form template according to the region your campaign is located (AMER, EMEA/APAC). The reason for the different forms is compliance related, so please be sure to use the correct template for the region. If you are setting up all three regions, you will need to use both templates.
  - Ensure the 'form name' includes the utm_campaign exactly as it appears in the table above
  - Form name should also include the utm_content exactly as listed in the issue
  - Form names in AMER forms also need to include `amer` in the form name
  - Example of correct format
    - _Ex.devopsgtm_amer_guide-to-devops_feb2023_
    - NOTE: If there is a segment specific version, add the segment inside the content name for better tracking. _devopsgtm_amer_guide-to-smb-devops_feb2023..._
- Fill out 'offer headline' and 'offer details'
- Update 'confirmation message' and `landing page URL`
  - The template has the homepage as a standard landing page URL, but if there is a more appropriate page, update the URL and keep the UTMs the same
- Update hidden field for `utm_campaign` and `utm_content`
  - This is very important to have the correct campaign naming to ensure the lead data is passed to Marketo
- Save Form
- Navigate to the campaign that will be using the new form and edit
- In `form details` select `download` as the call-to-action and select your new form
  - Note: If your new asset is launching in multiple regions, confirm you're adding the correct form to the correct regional campaign

### Step 1: Create Salesforce Campaign

[clone this program](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/PG8361A1)

- Use format `YYYY_Region_Social_[Name]_[parameter]_LinkedIn Lead Gen`
- Campaign parameter must be one of the [GTM campaign parameters](/handbook/marketing/utm-strategy/#the-new-utm_campaign-structure) (usually used as utm_campaign - ex. `devopsgtm` or `autosd`). The Salesforce campaign name must include the campaign parameter for the responses to roll up to the correct campaign on the Sisense dashboards.
- If an asset has multiple forms running across multiple regions, you'll need to create a separate SFDC campaign for each region.
Example: fy27_rtg_2025_eBook_CostFragmentedDevSecOpsAI_apac and fy27_rtg_2025_eBook_CostFragmentedDevSecOpsAI_amer forms promote the same asset — create one SFDC campaign for APAC and one for AMER.

_e.g.: 2020_Social_AutomatedSoftwareDelivery_autoSD_LinkedIn Lead Gen_

- Add `Parent Campaign` of `2020_Social_LinkedIn_Lead Gen`
- Refer to instructions [above](/handbook/marketing/marketing-operations/campaigns-and-programs/#step-5-update-the-salesforce-campaign).
- Update budget holder
- Update GTM Motion
- Add the SFDC campaign link to the epic or issue.

### Step 3: Auto-responder email

- If you're activating multiple assets, you will need to clone the autoresponder email and update all of the tokens in the email to match the additional tokens you added to the program for each asset.

### Step 4: Update the Marketo Program

- For adding Digital LinkedIn Lead Gen forms, go to the [Digital Paid Social Marketo Program](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/PG16666A1). For ABM LinkedIn Lead Gen forms, go to the [ABM Paid Social Marketo Program](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/PG16770A1).

- Create local program tokens. These programs are set-up to process multiple LI lead gen forms. You'll add new tokens for the asset you're activating.

**Smart List**

- Confirm the `01 Filled Out Form - Autoresponder` campaign smart list filter with `contains` and the prefix
  - `Fills out LinkedIn Lead Gen Form`, `Lead Gen Form Name contains [parameter]`
  - Available parameters are [listed above](/handbook/marketing/marketing-operations/campaigns-and-programs/#steps-to-setup-linkedin-lead-gen-form), or create new if not listed.
- `Filled out LinkedIn Lead Gen Form` filter - Make sure that other programs are excluded if your new campaign will use a similar LinkedIn Lead Gen form name. Common exclusions are `amer-pubsec`, `contactsales` and `abmkey`as these flow through separate campaigns. This is not a full list of all exclusions required as this will be based on what you are setting up. You can review existing LI Lead Gen programs for examples of exclusions.
- Other programs are looking for the parameters [listed above](/handbook/marketing/marketing-operations/campaigns-and-programs/#steps-to-setup-linkedin-lead-gen-form). If your LI Lead Gen form contains any of these, you will need to exclude your campaign from the existing program processing (for example, if your LI Lead Gen Form contains `devsecopsusecase`, you will need to exclude your LI Lead Gen form name from processing through the others that use `devsecopsusecase`). Please see the testing section below as this provides instructions to make sure you captured exclusions properly. Note that the ABM Team runs LinkedIn campaigns using `abmkey` and the campaign parameters above, so `abmkey` must always be excluded.
**Flow**
- No change to `1 - Remove from Flow` - If you remove this temporarily to test, be sure to add it back in before going live. `Remove from Flow`: Choice 1: If Email Address contains @gitlab.com. Campaign: this campaign. Default Choice: Campaign is Do nothing
- `2 - Send Email` - This step will vary. In general, you will set Choice 1: If Filled out LinkedIn Lead Gen Form contains [content name from form] then, Email [select appropriate email autoresponder]. There are multiple choices here, one for each asset. Even if you only have one asset in this step, best practice is to set up a choice with the default of Do Nothing. This is another backup in case the automation fails and will make sure that people don't receive an autoresponder email for another asset because the content name won't be found. You can view an example with multiple assets [here](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/SC21615C3ZN19). If multiple LinkedIn Lead Gen forms promote the same asset, add each form to the same choice by clicking the plus sign.
- No change to `3 - Change Program Status` - This is automatically in the template. Program: [Marketo program name] - New Status Paid Social > Responded
- `4 - Interesting Moment` Set this up the same way as the Send Email logic, except you will change the description to match the asset. In general, you will set Choice 1: If Filled out LinkedIn Lead Gen Form contains [content name from form] then, Type Milestone, Description: Filled out LinkedIn form to view asset: [asset name]. Default choice should be generic: "Filled out LinkedIn form to view [GTM name] asset."
  - If you set up additional tokens for each asset, you can use the tokens to populate the Interesting Moments
- `5 - Add to SFDC Campaign` - Set this up the same way as the Send Email logic, except you will set the Campaign dropdown field to the SFDC campaign you created for the LinkedIn Lead Gen form, with Status = Responded. Repeat this step for each form you're activating.
- No changes to steps 6, 7, and 8.
- Step 9: `Execute campaign` - This processes Action Stream tagging. No action required on this step. This should be: Executed Campaign: Action Stream tagging: (LinkedIn) Check Asset
- No changes to step 10.
- Turn on / Activate the triggered campaign in the `schedule` tab of the smart campaign
- All LinkedIn programs with your form prefix will now flow through this campaign
- If your new form promotes an asset that [qualifies for an action stream](/handbook/marketing/lifecycle-marketing/email-processes-requests/#action-streams), click on the [Action Stream tagging: (LinkedIn) Check Asset](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/SC58851A1ZN19) program. Otherwise, skip this step.
- Smart List: Add the name of the LinkedIn Lead Gen form in filter 1.
- Flow: Add the name of the LinkedIn Lead Gen form in filter 1.
- If your assets are for Finserv or PubSec, you need to add the SFDC campaigns to nurture processing to make sure people go into the current nurture program.
  - For Finserv: Update the Smart Lists for [00d - Add to Finserv nurture](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/SC62869A1ZN19) and [Vertical check](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/SC64233B2ZN19)
  - For PubSec: Update the Smart Lists for [Nurture - PubSec check](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/SC64118A1ZN19), [00 - Add to PUBSEC](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/SC24342A1ZN19), and [PubSec - Action Stream check](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/SC64194A1ZN19)

### Step 6: Test your LinkedIn Lead Gen Set-up

- Have Digital Marketing send a test record through the form. You can request this in the issue using the following text, updating the indicated sections:   `The Marketo program has been set-up for [name of asset] in [segment/region if applicable - you will not always need to provide this]. The automation will trigger based on [gtm code] and [content name]. Please submit a test record.`
- After the test lead is submitted, open the test record in the Marketo database. Go to the `Activity History` and confirm:
   1. The form that was submitted. You will pay attention to the gtm name and the content name. Make sure this is the form you wanted to test. If confirmed, move to step 2.
   1. Confirm the correct autoresponder for the requested asset deployed (digital)
   1. Confirm that no other autoresponders were sent (campaigns)
   1. Confirm that the correct Interesting Moment was triggered (campaigns)
   1. Confirm that the test record was added to the SFDC campaign (this may take a few minutes) (campaigns)
   1. Confirm that the test record was not sent any other emails or added to other programs as a result of this test (campaigns)

### Step 7: Update this Handbook page

- Update this [handbook page with the parameter](/handbook/marketing/marketing-operations/campaigns-and-programs/#steps-to-setup-linkedin-lead-gen-form) with a `yes` and a link to the parameter and campaign you have set up.

## Test your Marketo program setup

1. Submit a test registration on the webpage for this campaign. If you need to create a new test record (instead of using your existing email address), you can add a `+` after your username: for example `jdoe+testuser@gitlab.com`. When you run your test, pay attention to if the flow has a "Remove from flow" for GitLab email addresses. If this is the case, you need to either delete that flow step or test with another email address.
1. After the test lead is submitted, go to the Marketo database by clicking `Database` in the Marketo navigation. Then click on `Default` on the left side menu.
1. Search for the email address you used for your test record and open the test record in the Marketo database. Go to the Activity History and confirm:
     1. The form was submitted
     1. The record was added to the correct program with a successful status (should not be No Action)
     1. Confirm the correct autoresponder for the requested asset deployed
     1. Confirm that no other autoresponders were sent
     1. Confirm that the correct Interesting Moment was triggered
     1. Confirm that the test record was added to the SFDC campaign (this may take a few minutes)
     1. Confirm that the test record was not sent any other emails (except double opt-in email for Germany if applicable) or added to other programs as a result of this test

### LinkedIn Lead Gen Contact Us Set-up

- LinkedIn Lead Gen Contact Us forms process through the [Request - Digital Contact Us](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/PG26750A1) for non-Free to Paid Campaigns. Free to Paid LinkedIn Lead Gen Contact us forms process through [Request - Digital Contact Us Free to Paid](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/PG26851A1).
**Smart List**
- Add the LinkedIn Lead Gen form name to the `01 - Filled-out form` Smart List `Fills Out LinkedIn Lead Gen Form` trigger.
**Flow - non-Free to Paid form only**
- `6 - Interesting Moment` Add the LinkedIn Lead Gen form as an option to Choice 1. Skip this step if you're setting up a Free to Paid LinkedIn Lead Gen contact us form.
**Alert**
- Add the LinkedIn Lead Gen form name to the [Request - Contact](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/PG2466A1) `02 Alert for Contact Us` Smart List `Fills Out LinkedIn Lead Gen Form` trigger.

## Test your LinkedIn Lead Gen Contact Us Set-up

- Have Digital Marketing send a test record through the form. You can request this in the issue using the following text, updating the indicated sections:  `Marketo Contact Us processing has been set-up for form [form name]. Please submit a test record using a non-GitLab email address and non-GitLab company name.`
- After the test lead is submitted, open the test record in the Marketo database. Go to the `Activity History` and confirm:
      1. The form that was submitted. You will pay attention to the gtm name and the content name. Make sure this is the form you wanted to test. If confirmed, move to step 2.
      1. Confirm the correct autoresponder deployed (digital)
      1. Confirm that no other autoresponders were sent (campaigns)
      1. Confirm that the correct Interesting Moment was triggered (campaigns)
      1. Confirm that the test record was added to the SFDC campaign (this may take a few minutes) (campaigns)
      1. Confirm that the test record was not sent any other emails or added to other programs as a result of this test (campaigns)
      1. Confirm that any comments collected on the lead gen form were captured on the webform field
      1. Confirm that MQL was triggered
      1. Confirm that the Sales Alert was sent

### Adding LinkedIn Lead Gen forms to drive event registration

LinkedIn Lead Gen forms can be used to drive event registration without adding a new Marketo program.

1) Follow the instructions above to create the LI Lead Gen form. There are a couple of changes you must make to be sure the responses only flow through the event registration processing and not the standard LI form processing.
2) For ABM LI Lead Gen forms, use the naming convention: `abmkey_region_gtm` for driving event registration. The standard (non-event) format is `abmkey_gtm_region`. By changing the order of `region` and `gtm`, you will not need to add exclusions to the main LI Lead Gen form processing.
3) For Digital Marketing forms, do not use the `gtm` in the form name. Use a unique name that represents the event.
4) In Marketo, go to the Marketo program for the event you are promoting.
5) For most events, we recommend setting up a waitlist for responses from LinkedIn. This allows the event DRI to approve registrations. If a waitlist processing campaign is already activated in the program, you can skip to step 6.
     a) ONLY DO THIS IF THE WAITLIST PROCESSING IS NOT ACTIVE: If only the `Registration` processing campaign is active, you will need to activate the waitlist for LI responses. Click on `Waitlist` and **remove** the "Filled out form" trigger. Now, complete the task in step 6 and activate the `Waitlist` campaign. You must also activate the "Waitlist to Registered" campaign.
6) Add a trigger for "Fills out LinkedIn Lead Gen Form". Lead Gen Form Name: `contains` (enter Lead Gen form name you created in step 1 here). If you have multiple forms for this event, you can click the green plus sign in the box after `contains` and add multiple forms.
7) If your form is only targeting AMER responses, click on the "Flow" steps and at the bottom, add "Change Data Value". Add Choice. If LinkedIn Lead Gen Form name `contains` (name(s) of LI lead gen form). Attribute: Opt-in, New value: True
8) Test your updates. Details for what to look for can be found in the [Test your Marketo program setup](/handbook/marketing/marketing-operations/campaigns-and-programs/#test-your-marketo-program-setup) - Note that when a person is added to the waitlist, they will not get an autoresponder, but you will see them added to the program.
9) If you have any questions or just want your set-up checked over, please reach out to Marketing Ops before pushing your campaign live.

## Steps to set-up Marketo programs for Accelevents

1. Create your event in Accelevents using the instructions on the [Accelevents handbook page](/handbook/marketing/marketing-operations/accelevents/).
1. Submit a test registration through Accelevents. This will create the program in Marketo. DO NOT CHANGE THE NAME OF THE PROGRAM IN MARKETO, this will break the sync.
1. All Accelevents programs are created in the [Program_Events folder](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/MF29385A1). Locate your program (it will be named with the URL you used when you set-up the landing page) and click on it.
1. On the Summary page of the program, select `Salesforce Campaign Sync` and select "Create New". This will create a salesforce.com campaign. You will come back to this later to update it.
1. Complete the following Marketo tokens. Instructions for what to enter for each token are included in the program.
     - All tokens that contain the word "event" (example: {{my.event name}}). It is important that all event details related tokens are completed as the “Interesting Moments” Smart Campaigns pushes information to Salesforce based on the tokens. Depending on the campaign, some auto-responders and emails rely on tokens as well. The token for Event Location should be filled in with the City for In-Person events and Virtually for virtual events.
     - {{my.epic link}} - this can be a link to a GitLab epic or Asana project
     - {{my.landingpageURL}}
     - {{my.utm}} - Fill in the utm_campaign value (leave the rest of the utms as-is). You can use the [UTM Generator](/handbook/marketing/utm-strategy/#how-to-create-utms) to create the campaign UTM.
     - {{my.reply email}}
     - If your program qualifies for Action Streams (currently only available for Security), please update the {{my.Action Stream}} token with the relevant type here.
1. Clone processing campaigns and emails into your program.
     - Click on the [template](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/ME24226A1) and expand the drop-down.
     - Select the appropriate processing campaign, right click, select Clone. In the popup, select: Clone to: Programs, Program: Select the program that Accelevents created (where you added the tokens above), Name: 01 Processing. Click Clone.
     - Select Invitation Email, right click, select Clone. In the popup, Clone to: Different program, Name: Invite Email 1, Program: Select the program that Accelevents created (where you added the tokens above). Click Create.
     - Select Target List, right click, select Clone Smart List. In the popup, Clone to Marketing Activities, Program: Select the program that Accelevents created (where you added the tokens above), Name: Target List. Click Clone.
1. Go back to your new program that was created by Accelevents.
1. Click on 01 Processing
1. Under Smart List, change the program name to the name of your Marketo program in both filters. This must match exactly (you can select it from the dropdown).
1. Under Flow, Change the Acquisition program NEW VALUE to the name of your Marketo program.
1. Under Schedule, click `Activate`. If you have any questions on this program set-up, please contact MOps to review.
1. Follow the instructions under the [SFDC Campaign section](/handbook/marketing/marketing-operations/campaigns-and-programs/#sfdc-campaign-instructions) to complete your set-up.

## Raffles

Raffles can be associated with many different campaign types and have various ways to enter. You must complete the [legal requirements](/handbook/legal/marketing-collaboration/#engaging-legal-for-approval) before launching your raffle.

In general, the [YYYYMMDD_SurveyName](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/PG6402A1) Marketo program and Survey Campaign type will be used for raffles. Due to the potential set-up complexities for raffles, Marketing Ops will need to be involved even if you use the instructions below. Use these instructions to create the program and to engage Marketing Ops for additional set-up or review.

### For a Raffle Update Smart Lists, Flows and Tokens

- Clone the [YYYYMMDD_SurveyName](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/PG6402A1)
- Name the program using the following syntax: `YYYYMMDD_NameofProgram_Raffle`. You will likely have another campaign type associated as well (for example, a Conference) and this program should be housed in the folder for that event. This is a similar process to creating a speaking session associated to a conference.
- Sync to SFDC at the program main screen in Marketo, where it says Salesforce Sync with "not set", click on "not set", Click "Create New." The program will automatically populate the campaign tag, so you do not need to edit anything except click `Save`.
  - If you are a user of Allocadia, you will need to add the Allocadia raffle line item ID to the `Description` field. Click `Save`.
- [Update the SFDC campaign](/handbook/marketing/marketing-operations/campaigns-and-programs/#step-4-update-the-salesforce-campaign) and associate it to the [parent campaign](/handbook/marketing/marketing-operations/campaigns-and-programs/#parentchild-campaigns-setup) where applicable.
  - If you are a user of Allocadia, please see instructions [here](/handbook/marketing/marketing-operations/campaigns-and-programs/#step-8-update-the-salesforce-campaign---using-allocadia).
- Go back to the Marketo program and complete the tokens. Update the {{my.Survey Name}} token with the word "Default" - do not use another entry on this token.
- If you are using a landing page: Update your [Registration page](/handbook/marketing/demand-generation/campaigns/landing-pages/#general-marketo-landing-page-creation-instructions), thank you page, and registration confirmation email.
- If you are using a landing page: Click into the `01a Registration Flow` and change the Smart List to "Form Name is any" and "Web page is" should already be populated with the registration page for this program. The Flow should already be populated for you, but update Step 5 - Interesting Moment to read: "Filled out form to enter raffle {{my.Survey Title}}" in the `Description` field of Step 5. Go to `Schedule` and click "Activate".
- Responders to the form will be added to the program and SFDC campaign as `Filled out Survey` and will be scored according to the `Survey - Low` entry in the [scoring model](/handbook/marketing/marketing-operations/marketo/#behavior-scoring).
- Due to the potential set-up complexities for raffles, Marketing Ops will need to be involved. You can add the `MktgOps::00:Triage` and `MktgOps-Support` labels to your `Marketo LP and Automation` issue for assistance with set-up.
- If you are not using a landing page, MarketingOps will help you determine the correct processing for this campaign.

## Updating Member Statuses for Owned Events from Marketo Programs

Once an `Owned Event` (that included a GitLab-run landing page where we collected leads) is complete, DRIs are able to update the member statuses directly from Marketo, versus submitting a [lead list upload](/handbook/marketing/marketing-operations/automated-list-import/). **NOTE:** This is **ONLY** for status changes. If you have notes to add to leads, you will need to submit a [lead list upload](/handbook/marketing/marketing-operations/automated-list-import/).

1. Log into Marketo and click into the appropriate program for your campaign
1. Click on the `Members` tab at the top of the page
1. Click on the line item for the member that requires a status change
1. Select `Change Status` at the top of the screen
1. Select the appropriate status in the drop down (`Attended`, `Follow up Requested`, `No Show`, etc.)
1. Marketo will take a few moments to adjust the status and then the status will be updated

## Removing Registrations from Marketo Programs

Once a landing page has been set up for a campaign, it is good practice to have multiple people test the registration to make sure everything is integrated and running properly. As a result, there are often various test registrations in the Marketo program. To remove these test registrations, follow the below instructions.

1. Log into Marketo and click into the appropriate program for your campaign
1. Click on the `Members` tab at the top of the page
1. Click on the line item for the member you wish to remove and make sure that line item is highlighted
1. Select `Change Status` at the top of the screen
1. Select `Not in Program` in the drop down
1. Marketo will take a few moments to adjust the status and then the name will be removed from the `Members` list

### Removing SPAM from Marketo Programs and Zoom

On occassion, SPAM bots attack our webcast registration. Follow these steps to remove from Marketo and SFDC. You must open an issue with Mops to complete. Please include the marketo program link in your issue request and the dates of the event. The SPAM registrants will not be removed from zoom, and will need to be manually removed. However, it is OK to leave them in the zoom campaign, because it will not affect your campaign numbers.

1. Find the program in marketo
1. Isolate the SPAM and add them to a newly created static list.
1. Remove the SPAM from the program, by `Select All` in the static list. Then right clicking then Marketing > Change Program Status. Choose the Campaign and update the status to `Not in Program` This will also remove them from Salesforce.com campaign
1. Go to your static list. Highlight all and `Delete Person`
1. Agree to popup, and also remove from SFDC.

After program ends, double check your Marketo program for SPAM, as people that registered (but were excluded from registration filters) would be added to program as `No Action` becuase the form is a part of that program. Re-run the steps above to fully remove them from any campaingn stats.

## Canceling an Email send

There are cases where an email is set to send, but you need to cancel it. There are a few ways to do this based on the type of program.

### Smart Campaign - Scheduled Send

1. You can cancel specific runs by going into the smart campaign > schedule and clicking the red `x` next to the date and time of send.
1. To cancel the entire run, go into the smart campaign > schedule > campaign actions > `Abort Campaign` .
   - You can still reschedule the send after you abort it

Marketo documentation:

- [Stopping campaign runs](https://experienceleague.adobe.com/docs/marketo/using/product-docs/core-marketo-concepts/smart-campaigns/using-smart-campaigns/cancel-a-scheduled-batch-campaign-run.html?lang=en)
- [Aborting campaign](https://experienceleague.adobe.com/docs/marketo/using/product-docs/core-marketo-concepts/smart-campaigns/using-smart-campaigns/abort-a-smart-campaign.html?lang=en)

### Smart Campaign - Triggered Send

1. If the campaign is running on a triggered basis, you should go into the smart campaign > schedule and click the `deactivate` button. This will stop any lead from qualifying from the campaign again.
1. If the campaign is running through multiple flow steps, in order to halt the leads from continuing in the flow, you must go into the smart campaign > schedule > campaign actions > `Abort Campaign`. This will stop leads from continuing in the flow, and stop any further emails from being sent out.

Marketo Documentation:

- [Deactivating a smart campaign](https://experienceleague.adobe.com/docs/marketo/using/product-docs/core-marketo-concepts/smart-campaigns/using-smart-campaigns/deactivate-a-trigger-smart-campaign-schedule-tab.html?lang=en)
- [Aborting a smart campaign](https://experienceleague.adobe.com/docs/marketo/using/product-docs/core-marketo-concepts/smart-campaigns/using-smart-campaigns/abort-a-smart-campaign.html?lang=en)

### Email Batch Campaign

This program type has a mailbox icon.

1. If a campaign is scheduled, but hasn't sent yet. Click into the main program (mailbox) and view the control panel. You'll see 4 boxes. In the bottom right box, click `unapprove` and the email will not go out. When you are ready to reschedule, update date and time, and click `approve` in the bottom right box. All boxes will have a green checkmark signaling it is ready for send.
1. If a campaign is actively sending and you want to stop it, click into the main program (mailbox) and in the bottom right box click `Abort Program`. This will stop the sending of emails, but will not recall any email that was already sent. You will see how many you send in the `dashboard` view. Once an email program is aborted, you cannot reschedule it again.

You can view screenshots and further documentation from Marketo here:

- [Aborting an email program](https://experienceleague.adobe.com/docs/marketo/using/product-docs/email-marketing/email-programs/email-program-actions/abort-email-program.html?lang=en)
- [Unapproving an email program](https://experienceleague.adobe.com/docs/marketo/using/product-docs/email-marketing/email-programs/email-program-actions/approve-unapprove-an-email-program.html?lang=en)

### Instructions: How to update Conferences with more than 5,000 attendees

For conferences list loads with more than 5,000 attendees, consider not marking them as `success`. If the acting `Field Marketing Director` agrees to avoid marking these members as `success`, these are the steps to avoid that from happening. **This can only be done by a member of the MktgOps team!**

1. Open Marketo, Navigate to Admin>Tags>Channel>Conference
1. Uncheck `Success` box for `Attended` and save
1. Load the list in with the attended members
1. Once the list is done processing and campaign members are added, go back into Admin>Tags>Channel>Conference, and recheck the `Success` box for `Attended`

## Instructions: How to collect Dietary Restrictions on event registration and view responses

1. For an owned event (Field Marketing), add `FORM 4286: Owned event with Dietary Restriction` to the LP. Note that we do have other forms that collect this data, for example DevSecOps World Tour forms. Check with MOps if you aren't sure which form to use for your use.
1. Update Smart Campaign to look for `FORM 4286` in the Registration Processing SC.
1. Create a smartlist to look for the responses from the form. From the program, click "New", then "New local asset", then "Smart List". Name the smart list "Dietary Requirements". Add the filters `Member of Program` (Program name) & `Dietary Restriction Details` (is not empty).
1. Next, you need to [create a custom view](https://experienceleague.adobe.com/en/docs/marketo/using/product-docs/core-marketo-concepts/smart-lists-and-static-lists/using-smart-lists/create-and-change-views-for-lists-and-smart-list) in Marketo to see the details. Once you create the view, you will always have it available for selection the dropdown.
1. Click on the `Dietary Requirements` smart list you created, then go to the People tab.
1. Click where it says `View: Default`
1. Select Create View
1. Name the view Dietary Restrictions and under hidden columns, select `Dietary Restriction Detail` and `Dietary Restrictions: Other`
1. Click Create
1. Note that you can follow the same steps above if you need to view Physical Accommodation requests in a Marketo report. The fields for this are `Physical Assistance Needs` and `Physical Assistance Detail`.

The view you created will be saved for future use, so any time you need to see this specific view in the future, you will click View: Default and select "Dietary Restrictions" from your dropdown (the list is unique to you, so you will have different options than other people). Due to privacy requirements, we are not pushing this information to SFDC, but you can see it in Marketo up until seven days after the event. The dietary restriction fields will automatically be cleared 7 days after the lead list is loaded.

## Steps to Set up Sales Play Salesforce Campaign

1. Go to Campaigns tab

   1. If you aren’t seeing the Campaigns, select the + to see all tabs, and click on Campaigns

2. Click on the New button to create a new campaign. Using this framework, name the campaign: `FYXX_QX_Sales Play_NameofSalesPlay`
  
   1. Example: FY25_Q1_Sales Play_Dedicated & Compliance Play

3. Check `Active`
4. Type = `Prospecting`
5. Type Detail = `Acceleration`
6. Select the apprioprate `GTM Motion`
7. Update the `Description`
8. Add any related issue(s) or epic(s) in `Event Epic`
9. Update the `Status` appropriately
10. Add `Start Date` and `End Date`
11. Update `Region` and `Sub-region`
12. Update `Budgeted Cost` in Campaign (required field)
