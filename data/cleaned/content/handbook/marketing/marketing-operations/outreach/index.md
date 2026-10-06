---
title: "Outreach"
---

### Outreach

Outreach is our sales outbound engagement platform which helps Sales and Sales Dev team members efficiently and effectively engage prospects and customers to drive more pipeline and increase deal closure.

## Support

Outreach is a tool co-owned by the Marketing Operations and Sales Operations teams.
If you require further assistance outside of the contents of this handbook page and Highspot page, please reach out in the appropriate Slack channels based on your role:

- Marketing or Sales Development requests, please contact #mktgops on Slack.
- Sales requests, please contact #sales-tools-support on Slack.

## Access

Outreach access is dependent on your role. Below is a list of roles that will receive access automatically during onboarding.

### Role-Based Entitlement

- Sales Development
- Business Development Representatives
- Managers, SDR or BDR
- Account Executives
- Regional Directors
- SMB Advocates
- SMB Managers
- Renewals Managers
- Managers, Renewals Managers

Once you have access please take the following steps:

- Download and install the Outreach Chrome extension.
- Connect your calendar and email.
- Connect your LinkedIn Sales Navigator account (if applicable)

## Outreach Sequence Creation and Best Practices

### Best Practices

#### Sequence Naming Convention

**All Sales Dev Team Members must use this naming convention in their Sequences**

PLease take note of the following naming convention. Your sequences should be easy to distinguish using the following format:

**Department, Inbound or Outbound, High Touch or Low Touch, Region, Description/Motion, Language**

- **Department**
  - Sales
  - SD
  - RM
  - All Field
- **Inbound or Outbound**
  - IB
  - OB
- **High Touch or Low Touch**
  - HT
  - LT
- **Region**
  - Global
  - AMER
  - APJ
  - EMEA
  - PubSec
- **Team**
  - EAST
  - SEUR
  - META
  - LATAM
- **Description/Motion**
  - Trial
  - Contact Request
  - Overage
  - Google Cloud Follow Up
  - GitHub Takeout
- **Language**
  - ESP
  - FR
  - GER
  - JP
  - KOR
  - PT

**Examples:**

- SD IB LT EMEA Content GER
- SD OB HT Global CE User
- Sales Global PIpeGen Day #PGDay

#### Sequence Settings to Check

- Make sure email tracking is enabled on all email steps
- Interval Type = Schedule Days
- Make sure the sequence has all tags and is part of a collection
- Throttle Settings = "Max active prospects per user = 1000" and "Max adds per user every 24 hours = 75"

#### Tags

- Outreach tags are labels you can add to sequences or prospects. They help you quickly categorize and search for the information you need. Due to reporting needs please do not create your own tags and instead reach out to Sales Ops or Sales Dev Ops to create the tag.

**Tag Categories and Examples (Not Exhaustive)**

- Team/Group
  - SD
  - AE  
  - RNWL
  - SMB
- Inbound or Outbound
  - IB
  - OB
- High Touch vs Low Touch
  - HT
  - LT
- Geo
  - AMER
  - EMEA
  - APJ
- Team Specific
  - East
  - NEUR
  - DACH
- Sequence Type
  - Competitor
  - GitHub
  - Jenkins
  - Atlassian
  - Closed Lost
  - Event
  - Free to Paid
- Language
  - ESP
  - FR
  - KOR
  - JP
  - GER

#### High touch Vs Low touch

- A high touch sequence is a sequence that contains multiple forms of communication (Phone, LinkedIn, and Email) and are usually over two weeks long with at least ten steps. High Touch sequences should be the standard
- Low Touch sequences are usually four or less automated email steps. These sequences should only be used when a phone number cannot be found or for certain situations like event invites

#### Outreach Variables

- Outreach variables are placeholders that automatically pull in details about a prospect or sender, so emails feel personalized at scale. The only exception is for personalized variables which you can see an example of below

**Examples of variables**

- {{first_name}} – Inserts the prospect’s first name.
- {{company}} – Inserts the prospect’s company name.
- {{!personalization}} – Lets the XDR add a custom note. Anything written after the “!” becomes the internal note ex. {{!Event Name}}
{{Personalize this based off recent account news}} {{!Your AEs Name}}.
- {{sender.first_name}} – Inserts the sender's name.
- {{sender.calendar_url}} - Inserts sender’s calendar link.

#### When not to create a sequence

- One time edits to current messaging
- Keep in mind that you can edit email steps while adding prospects to sequences.
- When the messaging can be incorporated in an A/B Test
- A/B Testing can be done on any sequence’s email step

#### Time Based Sequences (Events)

- If a hyper personalized sequence needs to be created for a one time event please put the date of the event in the title of the sequence so the Ops team will know when to archive it.

#### When to create a net new sequence

- Filling a gap in messaging we currently do not have
- A/B Test iteration won't suffice due to need for: Different step ordering, different timeframe, different channels to be used

### Sharing Policies

#### Collection Policies

- Sales Dev
  - Inbound Collections
    - All inbound MQLs should be actioned with sequences from the Inbound collections

#### Team Collection Policy

- Each Sales Dev Team has their own team collection where they can test messaging for their particular regions. Globally applicable versions of these sequences can be created for the Good Collection as well.

#### Testing and Good Collection

- When a new sequence request is globally applicable it will go to the “Testing Collection” instead of a team collection.

### Sales

#### AE to BDR Sharing

- If an AE wants to share a sequence with a BDR, they can share the sequence with the BDRs manager. BDR managers will have access to all of the globally approved sales collections as well as their regions collections. The BDR Manager then can follow the process below to have a clone of the sequence created.

### Sales Dev Sequence Creation Process

- Request – XDR Managers submit a new sequence request issue on behalf of their XDRs when messaging gaps can’t be filled with a simple A/B test.
- Manager Review – The XDR Manager checks the sequence setup (naming, tags, settings, tracking, applicability) and approves it.
- Director Approval & Activation – The Director double-checks, launches the sequence, and sets a 60-day review date.
- Performance Review – After 60 days, the Director, Ops, and/or the Manager review results to decide whether to keep, expand, or retire the sequence.

Full Process Details → [BDR Sequence Creation Request Issue Template](https://gitlab.com/gitlab-com/marketing/sales-development/-/blob/main/.gitlab/issue_templates/BDR_Sequence_Creation_Request.md?ref_type=heads)

## Signature

Sales Development will be set by Opensense. The integration is live so you will just need to sync your gmail for it to come through. If you need to make any changes in your signature, please do it through Opensense.

## Email Sending limits

We have set email sending limits to protect our organisation sending score. This score affects our placement within the inbox so it’s very important we don’t abuse these limits. If you need to send to a larger amount than these limits, please work with your field marketer who have tools that can send to larger amounts.

- 500 emails a day can be sent from within Outreach. This is the number of emails each User can send using Outreach in a single day.
- 1000 emails a day can be sent from within GitLab. Total number of email deliveries that can be sent by Outreach Users each day.
- 25 emails a day can be sent to one email domain. This is the total number of emails that can be sent to one email domain per days. We don’t limit to the following domain:

  - gmail.com
  - microsoft.com
  - Outlook.com

If you would like to add to this list, please contact Marketing Ops.

## Rulesets

Rulesets in Outreach apply to sequences and control the status of the prospect. If you or a prospect performs a certain action while active in a sequence, it will move the status of the prospect, which will sync back to SFDC. The purpose of this is to manage the lifecycle of a prospect better.

### Default Ruleset

- Once the first task of a sequence is completed, it will move the status to Accepted.
- If a prospect replies, then it will move the status to Qualifying.
- If a meeting is booked, then it will mark the sequence as finished and the status will be Qualifying.
- If the prospect opts out during the sequence, it will move the status to Disqualified.
- If the prospect does not reply during the sequence and reaches the end of the sequence, it will move the status to Recycle.
- If a user manually marks the prospect as finished within the sequence, we will move it to Recycle.
- If Outreach detects that the prospect is OOO, then it will pause the sequence for 1 week OR if the date of return is in the OOO notification, Outreach will pause until that date.

### Follow Up Ruleset

- Once the first task of a sequence is completed, it will move the status to Qualifying.
- If a prospect replies, then it will move the status to Qualifying.
- If a meeting is booked, then it will mark the sequence as finished and the status will be Qualifying.
- If the prospect opts out during the sequence, it will move the status to Disqualified.
- If the prospect does not reply during the sequence and reaches the end of the sequence, it will move the status to Recycle.
- If a user manually marks the prospect as finished within the sequence, we will move it to Recycle.
- If Outreach detects that the prospect is OOO, then it will pause the sequence for 1 week OR if the date of return is in the OOO notification, Outreach will pause until that date.

### Support Ruleset

- Once the first task of a sequence is completed, it will move the status to Ineligible.
- If the prospect opts out during the sequence, it will move the status to Disqualified.
- If the prospect does not reply during the sequence and reaches the end of the sequence, it will move the status to Ineligible.
- If a user manually marks the prospect as finished within the sequence, we will move it to Ineligible.
- If Outreach detects that the prospect is OOO, then it will pause the sequence for 1 week OR if the date of return is in the OOO notification, Outreach will pause until that date.

### Phone Numbers

Due to global phone number regulations, at this time, we can only purchase a local/mobile phone number where GitLab has an entity. Below are the countries that we can currently purchase for:

- US
- Canada
- United Kingdom
- Ireland
- Germany
- France
- Spain
- Netherlands
- Singapore
- Australia

We are also investigating countries where we can purchase toll free numbers we can outbound prospect with. More to come soon.

Reps can also upload their personal numbers to use if it’s preferred.

## EMEA & APJ XDRS

All xDRs will receive a number for each entity in the region they are covering. EG if you are in EMEA, you will receive a number for Germany, France, Spain, Netherlands, Ireland( coming soon).

## AMER XDRs

All XDRs will be able to leverage the local dial feature. Outreach will automatically assign you a number based on the area you are calling into to make it appear as though you are calling from that area.

## Call Dispositions

| Call Disposition Name | Description  | Signal | Sequence Status | Lead/Contact Status |
| ------ | ------ | -------| -------| -------|
| CC: Answered: Info Gathered: Create Stage 0 Opp    |Some qualification questioned were answered and a Stage 0 opp should be created| Positive signal| Ends Sequence | Qualifying |
| CC: Answered: Create follow up task |Needs follow up in order to gain qualification/no current use case/not the right time| Positive signal | Ends Sequence | Recycle |
| CC: Answered: Not Interested |Have stated on the call they are not interested| Negative signal | Ends Sequence | Recycle |
| CC: Answered: Personal Use |They are using GitLab for personal reasons| Negative signal | Ends Sequence | Recycle |
| CC: Answered: Asked for Call Back | Caught them at a bad moment and they asked for a call back OR they are still evaluating tool, call back in a few weeks. | Neutral signal | Sequence Continues | Accepted |
| CC: Answered: Create follow up task | Call was answered and the rep needs to manually decide how to action the lead going forward. | Positive Signal | Ends Sequence | Qualifying |
| CC: Answered: Using Competition |They are using competition. A generic task will be created giving you the option to move the lead to recycle or add them to a pre made Competition Objection Follow Up Sequence|Negative signal | Ends Sequence | Qualifying |
| Automated Switchboard |You reached the automated switchboard and there was no option forward |Neutral signal | Sequence Continues | Stays Accepted |
| Main Company Line - Can't Transfer Line |There's no way to contact your prospect through this company number | Neutral signal | Sequence Continues | Stays Accepted |
| IQM Set | You were able to schedule an IQM while on the phone call. Note that a trigger exists in SFDC to automatically change lead status to Qualifying when this option is selected| Positive signal | Ends Sequence | Qualifying |
| Correct Contact: Left Message |You were able to reach the voicemail for the correct contact and you left a message on their machine or with their Personal Assistant | Neutral signal | Sequence Continues | Stays Accepted |
| Correct Contact: Not Answered/Other |You were able to reach the correct contact through a company directory but it kept ringing. You reached the contacts voicemail but their voicemail was not set up so you could not leave a message|Neutral signal | Sequence Continues | Stays Accepted |
| Incorrect Contact: Answered |The wrong person answered the phone number that you had for this contact and it is the wrong persons phone number (They were not a personal assistant) A generic task will be created giving you the option to move the lead to recycle or add them to a pre made Referral Sequence. They didn’t take a message for the correct person or give helpful information |  Neutral signal | Ends Sequence | Stays Accepted |
| Incorrect Contact: Left Message |The wrong person answered the phone and it is the wrong persons phone number (They were not a personal assistant). They took a message for the correct person/gave you the correct number for the contact| Neutral signal | Ends Sequence | Stays Accepted |
| Incorrect Contact: Not Answered/Other |You got through to the voicemail but the voicemail was for someone other than the person who you were trying to contact. Or the person was not listed in the company directory and you were calling the companies main number |Neutral signal | Ends Sequence | Stays Accepted |
| Incorrect Contact: Answered: Gave Referral | It was the wrong person but they gave a referral to speak to. Please record in notes who the referral is. | Positive signal | Ends Sequence | Qualifying |
| Incorrect Contact: No Authority | The person who answered the phone number has no authority nor decision to move forward with a purchase.| Negative signal | Ends Sequence | Stays Accepted |
|Correct Contact: Discovery Call Set  | You were able to schedule a discovery call while on the phone call. Note that a trigger exists in SFDC to automatically change lead status to Qualifying when this option is selected | Positive Signal | Ends Sequence | Qualifying |

## Call Troubleshooting

- [Call Audio Troubleshooting](https://support.outreach.io/support/solutions/articles/159000426364)- If you are experiencing any issues with the call audio after the call is connected. Please follow the steps as outlined in the linked page.

- [Call Connection Troubleshooting](https://support.outreach.io/support/solutions/articles/159000425754-troubleshooting-outreach-voice-call-connection-issues) - If you are experiencing any issues with the call not connecting. Please follow the steps as outlined in the linked page.

## Inbound Calls

If you have been assigned a number, if a prospect calls you back, it will come through to you.

**For local presence (AMER) :**

Outreach will route inbound calls with local presence in the following order:

- If the incoming phone number matches a single Prospect, route the call to the last active user that called this number using the local Presence number the Prospect called.
- If the incoming phone number matches a single Prospect, route to the owner of the Prospect.
- If the phone number matches a single Prospect, route the last active user that called this number using ANY local presence phone number.
- If the phone number matches a call (to/outgoing or from/incoming), route to the user that was on that call.
- If the local number has never been used by Outreach (ex: the local number was recently purchased but never used), Outreach routes the call to the most recent active Outreach user.

## Requesting a New Phone Number in Outreach

**Overview**

If you believe your current Outreach phone number has been flagged as spam, you can request a replacement number by following the process below. All requests require evidence that your current number is marked as spam before a new number will be provisioned.

**Step 1: Confirm Your Number Is Marked as Spam**

Before submitting a request, you must verify and document that your number has been flagged. Acceptable forms of evidence include:

- A screenshot from a spam-checking tool such as [Should I Answer](https://www.shouldianswer.net/), or a similar number reputation service showing your number is flagged
- A screenshot or recording of a prospect's caller ID displaying "Spam," "Spam Likely," or "Scam Likely"

**Step 2: Submit a Request**

Once you have documented evidence, submit a request through the **#mktgops** Slack channel or open a Marketing Operations issue with the following information:

- Your current Outreach phone number
- Your Outreach username / email
- Your evidence (screenshot, as outlined above)
- Your preferred area code for the replacement number (if applicable)

**Step 3: Review and Provisioning**

Marketing Operations will review your request. If the evidence is sufficient, a new number will be provisioned and assigned to your Outreach profile. You will be notified via Slack or GitLab issue when the change is complete.

**Important Notes**

- Requests submitted without spam evidence will not be processed.
- To maintain number reputation, avoid high-volume cold calling patterns that can trigger carrier spam filters. Review best practices in the [Sales Development Outreach Playbook](/handbook/marketing/marketing-operations/outreach/#best-practices).
- Number replacement does not guarantee the new number will remain spam-free. Calling cadence and behavior are the primary factors in number reputation.

**Questions?** Reach out to Marketing Operations in **#mktgops**.

## Sync to/ From CRM Process

The sync from Outreach to SFDC and vice versa will happen every 10 mins automatically. If you need to force a sync, then there is an option to hit the little cloud on the side panel within outreach on prospect/accounts and force a push sync to CRM or a pull sync into Outreach.

## Available Integrations

- Highspot
- 6Sense
- Terminus
- Qualified
  - With Qualified for Outreach, sales reps have a modern tool in their toolkit to help them meet with their most valuable prospects. They no longer need to wait for an email reply to get a meeting on the books. Instead, sales reps can capitalize on that “magic moment” when a prospect arrives on your website from an email sequence to instantly start a conversation that’s consistent across channels. This results in more web conversions, more pipeline, and more closed/won business. Plus, it provides a seamless buying experience, helping you move from click to close faster than ever before. In short, sales teams use Outreach to prospect into target accounts and Qualified to close them.
  - Qualified Signals is an AI-based product that combines first and third-party website engagement, including Outreach email click-throughs, with Salesforce data to predict the buying intent of a B2B company’s target accounts. Qualified’s integration with Outreach surfaces Signals data within the Outreach platform, where outbound sales reps spend their day. This is beneficial because it gives sales reps quick access and clear direction on which accounts they should be prospecting into to generate more pipeline and crush their quota. From here, sales reps can quickly craft and send VIP buyers a personalized outbound Outreach email, driving them back to your site. This approach helps you accelerate your sales cycle and drive more pipeline, more efficiently.
- LISN
  - The Sales Navigator for Outreach integration provides an enhanced experience by interacting with the rich professional data in Sales Navigator, right where you’re selling. With Outreach for Sales Navigator, you’ll gain access to LinkedIn Sales Navigator intelligence tiles: Lead information and Account, while being able to execute LinkedIn Sales Navigator tasks directly from the Outreach Platform.
  - [How to add LinkedIn Sales Navigator to an Outreach Profile](https://support.outreach.io/hc/en-us/articles/115003566233-How-To-Add-LinkedIn-Sales-Navigator-to-an-Outreach-Profile)

## Triggers

Triggers in Outreach automate actions and workflows based on specific prospect/account/task conditions. The following triggers are active in Outreach

| Trigger Name | Description  |
| ------ | ------ |
| Add Timezone to Prospect | Adds timezone to a prospect located outside of North America. |
| Bad Data - Bad Phone Number/Bounced Email - Stop Sequence | Stops a prospect in sequence when a call is marked bad number and Bad Data Reason is Bounced Email. |
| Bad Data - Email Bounced/Bad Phone number - Disqualified | Marks prospect status as Disqualified when an email bounces and Bad Data Reason is Bad Phone Number. |
| Campaign - White Glove Sequence |Adds prospect to `SD IB HT Global EVT White Glove Task Step 1` when HP Reason is White Glove and HP is true and status is MQL. |
| Campaign- Uncheck High Priority | Removes HP check when HP is true and Actively Being Sequenced is true. |
| New Task - CC: Answered: Asked for Call Back | Creates a new task on the prospect when a call disposition is set to `CC: Answered: Asked for Call Back` |
| New Task - CC:Answered: Using Competition | Creates a new task on the prospect when a call disposition is set to `CC: Answered: Using Competition` |
| New Task - Incorrect Contact: Answered: Gave Referral | Creates a new task on the prospect when a call disposition is set to `Incorrect Contact: Gave Referral` |
| New Task - PTP Score Updated | Creates a new task on the prospect when a PTP Score is updated to 4 or 5 and the prospect is Actively Being Sequenced. |
| Operational - Attempting to Contact - Bounce - Bad Data | Sets Bad Data Reason as `Bounced Email` a mailing task is marked as Bounced. |
| Operational - Bad Data - Stop Sequences | Stops all sequences when a prospect is Actively Being Sequenced and status is Disqualified and Disqualified reason is Bad Data. |
| Operational - Ineligible - Support | Sets Ineligible Reason as `Support` when a prospect status is Ineligible and current sequence name contains `Support` or `Support/Technical Related` |
| Operational - LinkedIn/Task 1st Step- Accepted | Sets status as `Accepted` after a LinkedIn step is completed as a first step in a sequence. |
| Operational - Meeting Booked - Move to Qualifying | Sets status as `Qualifying` when a meeting is booked. |
| Operational - Not Interested - Unsubscribe - Disqualified | Sets Disqualified Reason as `Unsubscribe` when status is Disqualified and Disqualified Reason is blank and Date opted out is not blank. |  
| Operational - Recycle- Set No Response | Sets Recycle Reason to `No Response` when status is Recycle and Recycle Reason is empty. |
| Operational - Remove Status Reason when updated |Removes all status reasons when status is `MQL`, `Inquiry`, `Accepted`, `Raw`, `Qualifying`, or `Qualified` |
| Operational - Set qualifying stage when IQM set | Sets status to `Qualifying` when an IQM is booked. |
| Operational- Bad Phone Number - Bad Data Reason | Sets Bad Data Reason to `Bad Phone Number` when call disposition is Bad Phone Number |
| Set Disqualified Reason - Call Disposition: Incorrect Contact: Answered | Sets status to `Disqualified` when a call disposition is set to `Incorrect Contact: Answered` |
| Set Disqualified Reason - Call Disposition: Personal Use | Sets status to `Disqualified` and Reason to `Personal Use` when a call disposition is set to `CC: Answered: Personal Use` |
| Set Nurture Reason - Call Disposition: Competition | Sets status to `Recycle` and Recycle Reason to `Evaluating` when a call disposition is set to `CC: Answered: Using Competition` |
|Set Nurture Reason - Call Disposition: Not Interested | Sets status to `Recycle` and Recycle Reason to `No Interest` when a call disposition is set to `CC: Answered: Not Interested` |
| Set Nurture Reason - Call Disposition: Not Opp yet | Sets status to `Recycle` and Recycle Reason to `Evaluating` when a call disposition is set to `CC: Answered: Info Gathered: Not Opp yet` |
| Set Recycle Reason - Call Disposition: Gave referral |Sets status to `Recycle` and Recycle Reason to `Evaluating` when a call disposition is set to `CC: Incorrect Contact: Answered: Gave Referral` |
| Set to Qualifying - Call Disposition: Answered: Asked for Call Back | Sets status to `Qualifying` when a call disposition is set to `CC: Answered: Asked for Call Back` |

## Resources

### Call Coaching Best Practices

#### Permission and Selection Guidelines

**1. For Group/Public Sessions:**

- Team members must either self-nominate their calls OR provide explicit written permission before their call is shared
- Never surprise someone by playing their call in front of others
- Give the person at least 24-48 hours notice before the session
- Allow them to preview the specific segments that will be discussed
- Offer an opt-out option without requiring justification

**2. For One-on-One Sessions:**

- Manager and rep should jointly select calls to review
- Balance challenging calls with successful ones (aim for 2:1 ratio of wins to improvement areas)
- Frame difficult calls as learning opportunities, not failures

#### Feedback Delivery Standards

| **Do** | **Don't** |
|--------|-----------|
| Start with what went well—always identify specific strengths first | Use sarcasm or mocking language |
| Focus on behaviors and techniques, not personal attributes ("The question could have been more open-ended" vs. "You're not a good listener") | Compare team members to each other negatively |
| Provide specific, actionable alternatives ("Try asking X instead" or "Here's a framework for handling that objection") | Pile on multiple criticisms without breaks for discussion |
| Normalize mistakes as part of learning ("This is a tough objection we all struggle with") | Revisit the same calls repeatedly unless specifically requested |
| Ask the rep what they noticed first—self-assessment builds awareness | Share call snippets in Slack or other channels without explicit permission |

#### Session Structure Recommendations

**1. Group Sessions (30-45 minutes)**

| **Step** | **Description** |
|----------|-----------------|
| 1. Set ground rules | Set psychological safety ground rules at the start |
| 2. Review clips | Review 2-3 short clips (2-3 minutes each maximum) |
| 3. Apply framework | Use the "What went well / Even better if" framework |
| 4. Invite observations | Invite peer observations, not judgments ("I noticed..." vs. "They should have...") |
| 5. Close with action | End with key takeaways and role-play practice |

**2. One-on-One Sessions (Weekly/Bi-weekly)**

| **Step** | **Description** |
|----------|-----------------|
| 1. Review calls | Review 1-2 full calls or 3-4 key moments |
| 2. Rep-led assessment | Let the rep lead with their observations first |
| 3. Co-create plan | Co-create an action plan with 1-2 specific focus areas |
| 4. Follow-up | Schedule follow-up to track progress |

#### Protection Mechanisms

- Establish a "learning zone" culture where sharing struggles is encouraged
- Rotate whose calls are reviewed so no one feels targeted
- Never tie call reviews directly to performance improvement plans (PIPs) or disciplinary action
- If a call reveals a significant performance issue, address it privately first
- Document that feedback is confidential between participants unless the rep agrees to share
- Group call coaching sessions should be recorded

<br>

**If you notice these patterns, intervention is needed:**

| **Red Flag** |
|--------------|
| Team members actively avoiding having their calls reviewed |
| Defensive or withdrawn behavior during sessions |
| Decrease in call volume (avoiding being recorded) |
| Only the same "safe" calls being volunteered |

#### Call Recording Access & Commenting Policy

**Viewing Access**

All employees in the org can view recorded calls for self-learning and professional development purposes.

**Commenting Permissions**

| **Role** | **Permission Level** | **Guidelines** |
|----------|---------------------|----------------|
| Rep's direct manager | May comment | Must follow quality standards |
| Directors and VP within Sales Dev | May comment | Must follow quality standards |
| Sales Dev Enablement | May comment | Must follow quality standards |
| All other team members | View only | Can share feedback through rep's manager |

**Rationale**

While transparency in learning is valuable, unrestricted commenting can lead to:

- Inconsistent or conflicting feedback that confuses the rep
- Pile-on criticism from multiple sources
- Junior team members providing guidance beyond their expertise
- Comments becoming a forum for venting rather than coaching

**All Other Team Members**

- Can view calls to learn from peer examples
- If someone has valuable feedback on a call, they should:
  - Share it with the rep's manager
  - The manager evaluates and decides whether to add it as a comment (attributing the source if appropriate)
  - Or the manager facilitates a direct conversation between the team members if more appropriate

### Sales Development Spot Checking Call Views

The table below shows calls placed in the last 7 days, per Sales Development team, with views for positive outcomes and objections for spot-checking and coaching purposes.

| Team | Positive Outcomes | Objections |
|------|------------------|------------|
| BDR AMER COMM | [View Positive Calls](https://web.outreach.io/calls?smart_view=25376) | [View Objections](https://web.outreach.io/calls?smart_view=25388) |
| BDR AMER EAST-WEST | [View Positive Calls](https://web.outreach.io/calls?smart_view=25377) | [View Objections](https://web.outreach.io/calls?smart_view=25389) |
| BDR AMER FINS-LATAM | [View Positive Calls](https://web.outreach.io/calls?smart_view=25378) | [View Objections](https://web.outreach.io/calls?smart_view=25390) |
| BDR AMER PUBSEC | [View Positive Calls](https://web.outreach.io/calls?smart_view=25379) | [View Objections](https://web.outreach.io/calls?smart_view=25391) |
| BDR BASE TEAM | [View Positive Calls](https://web.outreach.io/calls?smart_view=25375) | [View Objections](https://web.outreach.io/calls?smart_view=25387) |
| BDR EMEA DACH | [View Positive Calls](https://web.outreach.io/calls?smart_view=25380) | [View Objections](https://web.outreach.io/calls?smart_view=25392) |
| BDR EMEA TELCO EGC | [View Positive Calls](https://web.outreach.io/calls?smart_view=25381) | [View Objections](https://web.outreach.io/calls?smart_view=25393) |
| BDR EMEA NEUR UKI | [View Positive Calls](https://web.outreach.io/calls?smart_view=25382) | [View Objections](https://web.outreach.io/calls?smart_view=25394) |
| BDR EMEA SEUR | [View Positive Calls](https://web.outreach.io/calls?smart_view=25383) | [View Objections](https://web.outreach.io/calls?smart_view=25395) |
| XDR APJ | [View Positive Calls](https://web.outreach.io/calls?smart_view=25384) | [View Objections](https://web.outreach.io/calls?smart_view=25396) |
| SDR AMER | [View Positive Calls](https://web.outreach.io/calls?smart_view=25385) | [View Objections](https://web.outreach.io/calls?smart_view=25398) |
| SDR EMEA | [View Positive Calls](https://web.outreach.io/calls?smart_view=25386) | [View Objections](https://web.outreach.io/calls?smart_view=25397) |

### Sales Development Kaia Playlists

The playlists below showcase calls that are showing great potential. We use our [Claude call rank prompt on our outbound prospecting project](/handbook/sales/sales-development/#claude-sales-dev-bdrsdr-user-guide) to sort through all calls that have more than 2' duration on Outreach, and then manually screen as a second step.

Please find the full list on [Outreach Kaia here](https://web.outreach.io/kaia/playlists/101), and a quick description of their ranking below.

| Category | Score | Description |
|----------|-------|-------------|
| **BENCHMARK PERFORMANCE** | 75-100 | Deep discovery, Purposeful use of our sales methodologies, differentiated AI positioning, consultative approach, and strong pipeline quality. Minor gaps only. |
| **GROWTH OPPORTUNITIES** | 50-74 | Surface-level discovery, generic positioning, single-threaded. Solid foundation with specific refinement needs. |
| **DEVELOPMENT FOCUS** | 0-49 | Skill-building opportunities. Elements like research, pattern interrupts, discovery or trap-setting questions and differentiatiors are present and can be improved upon. |

### Comment Quality Standards

**All authorized commenters must follow these guidelines:**

| **Standard** | **Description** |
|--------------|-----------------|
| **Constructive** | Focus on what can be improved and how |
| **Specific** | Reference exact timestamps and provide clear examples |
| **Balanced** | Note strengths as well as improvement areas |
| **Actionable** | Include alternative approaches or techniques |
| **Respectful** | Professional tone that assumes positive intent |

#### Comment Review

- Managers should review comments left by others on their direct reports' calls weekly
- Directors/Enablement should coordinate to avoid redundant or conflicting feedback on the same call
- If a comment violates the quality standards above, the rep's manager should flag it for removal

#### Violations

| **Instance** | **Action** |
|--------------|------------|
| First instance | Verbal coaching on the policy |
| Second instance | Written warning |
| Continued violations | Loss of commenting privileges and potential escalation |

## Outreach SFDC Reports Upload

There are a couple of prerequisites that are needed for successful uploads:

- The report format needs to be a Leads ,Contacts & Accounts or Opportunity with Contact roles format
- Please ensure Contact ID field is added to the report
- Run the report for either All Leads or All Accounts (rather than just My Leads or My Contacts).
- It needs to be saved in a PUBLIC FOLDER.
- Salesforce limits imports to 2000 records per import.
- Please make sure that their email address is included in this public report. Otherwise, we are at risk of duplicates/activity not logging back to SFDC.

You can read more information here: https://support.outreach.io/hc/en-us/articles/206297527-How-To-Import-Salesforce-Reports-into-Outreach-to-Bulk-Create-Prospects-and-Opportunities

Please note that CSV uploads is not enabled for our org and at present there are no plans to do so. Opportunity reports are also not enabled at this time
