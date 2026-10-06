---
title: "Qualified"
description: "Qualified facilitates instant sales conversations with visitors on the GitLab marketing website"
---


## Overview

Qualified allows Sales Development Reps to have live conversations with visitors on the about.gitlab.com site. Reps can see which accounts are viewing the site, their propensity to buy and choose to engage in a conversation or wait for the visitor to reach out through the automated chat bot.

### SDR Use Case

SDRs (inbound reps) will be routed chats of visitors who have requested to chat with a human while having a conversation with our AI Rep. These leads are first order available and not associated with an "Actively Working" account. They will route via round robin pools based on the account or visitor's geography. Once a chat is routed the rep will qualify the lead and determine if a meeting needs to be booked for a discovery call. SDRs can create and update the Salesfoce lead record with information gathered during the chat. Reps can also send their calendar to the visitor to book a meeting directly from the Qualified platform.

### BDR Use Case

BDRs (outbound reps) will be routed conversations from visitors who request to chat with a human while speaking with our AI Rep associated with "Actively Working" accounts they are assigned to. BDRs will also have the ability to initiate a conversation with a site visitor from an "Actively Working" account. Once a chat is routed the rep will qualify the lead and determine if a meeting needs to be booked for a discovery call. BDRs can create and update the Salesfoce lead record with information gathered during the chat. Reps can also send their calendar to the visitor to book a meeting directly from the Qualified platform. 

### Experiences

Experiences are what the site visitor sees when they are browsing the site. It appears as a chat box in the bottom right corner of the web page. Visitors can choose to engage with the experience to help them navigate the site, book a meeting with a sales development rep or choose "Just Browsing" and close the experience.

We now offer experiences in English, French, German, and Japanese. Experiences in these languages match the language of the site being viewed. For example, the French epxeriences show on pages that contain /fr-fr.

Have questions about the experiences on the website? Please reach out to us in the #mktgops Slack channel.

To request a new experience please use [this issue template](https://gitlab.com/gitlab-com/marketing/marketing-operations/-/issues/new#) in the Marketing Operations project.

### Routing

Routing rules are set up in Qualified to send a visitor to the most appropiate rep to handle the conversation.

- A visitor that is existing in our CRM and being Actively Sequenced, they will be routed to the sequencing rep.
- A visitor that is identified as being associated to a US PubSec account will be routed to the BDR Assigned on that account. If no BDR Assigned is present on the account they will be round robined to the PubSec team.
- A visitor that is identified to be associated with an Actively Working account will be routed to the BDR Assigned on that account. If the rep is not available, the visitor will be routed to the inbound SDR team based on Geo to further qualify the lead. Once routed to an SDR, ownership of the lead will be determined by our standard [Rules of Engagement](/handbook/sales/sales-development/).
- A visitor who interacts with one of our non-English experiences will be routed to the team member or members who speak the appropriate language.
- A visitor that is not being sequenced, not PubSec, and not part of an Actively Working account will be routed to the appropriate Geo based SDR round robin pool.

If you feel you have been routed a conversation or visitor in error please post a link to the lead/conversation in the #mktgops Slack channel.

### Signals

Signals data is a collection of custom fields added to the Account object, reports, and dashboard components in Salesforce to showcase Signals data for your organization. The Signals Account 360 is a robust account profile that presents an account's engagement with your campaigns and their likely purchase intent over time. Sales reps and executives alike can view the Signals Account 360 to identify which accounts and opportunities are most likely to close.

### Integrations

Qualified is currently integrated with SalesForce, Outreach, and 6sense. Information on each integration is below.

#### Salesforce

The Qualified/Salesforce integration allows reps to create and update lead records from the Qualified platform and update contact records. Because Qualified is integrated with Salesforce reps can easily see information from the SFDC record directly in the Qualified platfrom while chatting. It also allows for the ability to map any field from the lead/contact record to Qualified to give reps pertinent information.

#### 6sense

Qualified offers an integration with 6sense to help you pull in firmographic information about the website visitors from the start. Using 6sense's reverse IP lookup, you can quickly see where the visitor is coming from, their company information, segments they belong to, and insights for their product lines.

#### Zoom

The Zoom integration is active for all Qualified users. Reps can now connect their Zoom account to auto-generate a unique meeting link for every meeting booked through Qualified, so there's no need to manually paste in Zoom links.

How to connect:

1. Go to your Calendar settings in Qualified

2. Under Meeting details, click Connect with Zoom

3. Once connected, you'll see your Zoom email listed as Active and Qualified will generate a unique link for each meeting automatically

#### Marketo

While Qualfied can create/edit person records, leads are typically created in SFDC first. Marketo utilizes triggers from SFDC activity or campaign membership for Interesting Moments and scoring for Qualified actions.

Qualified also has an integration to view a program in Marketo, within Qualified. We have hundreds of programs, so to reduce visibility, we created a program tag type `UsedWithQualified` = `True` to surface the program to Marketo. You can do this in Marketo's individual program settings under `setup`. This tag is not required, so despite having a `false` value, you can simply not use it if you do not want to surface the program to Qualified.

#### Slack

Qualified is integrated through Slack by adding the Qualified app in a user's Slack instance. The integration allows for notifications to be sent through Slack regarding conversations, meetings booked or meetings offered but not booked. We have enabled a feature for reps to recieve AI notifications when a meeting is booked on their calendar. These notifications have the following information:

- Meeting details — type, duration, time, lead info
- Lead summary — background, engagement signals, and intent indicators
- Account summary — company details, tech stack, current stage, and activity history

### Performance Measurement

The Rep Performance Dashboard helps you understand the metrics that mean the most to your success including:

- Visitor sessions routed to reps for pouncing (proactive engagement)
- Successful pounce conversations
- Visitor sessions where a visitor waited for a rep to join the chat
- When reps were available throughout the day
- Visitor sessions that waited for a chat and had a successful conversation with a rep
- Visitor sessions that waited for a chat and had no conversation
- Total rep availability

### Qualified AI SDR

Qualified has an AI offering that they call "Piper". We have chosen to name our AI SDR "Dev". Dev has the ability to have conversations with website visitors, freeing up human rep bandwidth to focus on more outbound prospecting. This gives us the ability to provide a better visitor experience on the website by easily answering visitor questions, qualifiying visitors and booking meetings with human reps 24/7.

Dev is enabled to greet visitors on our website. Visitors have an open text box to be able to ask Dev anything they want about GitLab. Dev will continue the conversation and look for behavior that will trigger one if it's goals. Those goals are to Book a Meeting, Route to a Rep, or provide Support related information.

All aspects of how Dev behaves is controlled in the "AI Studio" on the admin side of Qualified. The "Content" section is where the GitLab AI Rep has indexed the GitLab marketing site, GitLab documentation, and other GitLab resources to be able to converse with and answer visitor questions live. The goals of the AI Rep are to either connect the visitor to a human rep (if one becomes available) or to book a meeting with a human rep.

We have set certain rules of engagement for the AI Rep to follow which include:

1. Never discussing special pricing or promotions
2. Always directing visitors looking for support to https://about.gitlab.com/support/
3. Never direct visitors to the demo or contact us page (we want these visitors to meet with a human)
4. Always make GitLab the better choice when making comparisons

The "Scorecard" and "Inbox" sections of the AI Studio is where we have control over how the GitLab AI Rep will answer specific questions. Here is where we can insert our own commonly asked questions and see how AI will respond. We can accept AI's response, tweak it, or tell it exactly what we want to certain questions. As visitors ask question they will appear in the "Inbox" we can move the most common ones to the "Scorecard" to rate.

#### AI Rep Rollback Plan

If there is a need to turn off the GitLab AI Rep, we have build the experiences in a way to easily switch off AI and switch on a traditional experience.

In the Qualified admin settings, navigate to `Experiences` and select `Automatic`. Beginning at experiences 48 and 49 you will start to see duplicate experience titles with one having `AI` added to the end. For example `[EN] Page - Solutions - Moble` and `[EN] Page - Solutions - Mobile - AI`. If the  GitLab AI Rep needs to be turned off you will need to go down the experience list, switch off each experience that ends in `AI` and switch on the corresponding expereince without `AI`.

### Qualified AI Email

Beginning in FY26 Q1 we will be testing Qualified's AI email functionality. Our test includes two use cases.

1. Visitors to the GitLab marketing site who are offered to book a meeting through the Qualified chat and who fail to book that meeting. AI will follow up via email to attempt to re-capture that meeting booking on behalf of the Sales Development rep whose calendar was shown. These leads and contacts will MQL as usual since they have shown enough intent to either explicitly request a meeting or trigger an AI goal to offer a meeting. Once AI reaches out via email the record will move to Accepeted status and on to either Recycle or Qualifiying depending on the outcome of the email campaign.
2. Leads and contacts added to specific content syndication campaigns. These will be earlier in the funnel prospects in an attempt to raise interest earlier and more quickly. The status of these recods in Salesforce will not be updated. Rather we will indicate that these leads are being reached out to by AI with a checkbox on the record. Once the AI email campaign is over, the box will uncheck and the record will continue it's normal lifecycle. The record will need to be routed to a Sales Development rep and if there is a response they will be able to respond back via email and dispostion the lead appropriately.

### Qualified AI Email Rollback Plan

Just like the AI chat rollback plan, in the Settings section of Qualified an Admin will be able to select Email Campaigns in the AI section of the left navigation bar. You will see the various campaigns that are running and the Admin can switch off the campaign by clicking into the campaign and in the top right corner selecting Off.

#### AI Rep Support

Have questions about the GitLab AI Rep on the website? Please reach out to us in the #mktgops Slack channel. We also have an external Slack channel with our Qualified support team. If you are not already in that channel, please ask a Marketing Ops team member to be added if you need access to our Qualified team.

To request a new feature or change please use [this issue template](https://gitlab.com/gitlab-com/marketing/marketing-operations/-/issues/new#) in the Marketing Operations project.

## Other Qualified Features

### Qualified Offers

Qualified Offers (also referred to as AI Offers) is a lead generation and content distribution tool within the Qualified PipelineAI platform. It automatically surfaces relevant marketing promotions, content assets, and calls-to-action to website visitors based on their buyer signals, account profile, and engagement context. The feature is designed to streamline lead capture and increase conversion rates by presenting personalized offers at the right moment in the buyer journey.

#### Core Offers Functionality

Automated Content Delivery

- Dynamically presents marketing offers to website visitors based on their characteristics, behavior, and intent signals
- Integrates with Piper the AI SDR to automatically serve relevant content during conversations
- Adapts offer selection based on buying stage, account attributes, and real-time visitor behavior

Offer Builder

- Point-and-click interface for creating and designing offers without development resources
- Multiple placement options: notification banners, sidebar pop-ups, and modal overlays
- Customizable styling, copy, and CTAs (buttons, links, or embedded forms)
- Preview functionality to review offers on target landing pages before activation

Lead Capture & Enrichment

- Embedded single-field forms within offers for frictionless lead collection
- Automatic data enrichment (company, title, location, etc.)
- Direct push to connected platforms including Salesforce, Marketo

Custom Triggers

- Exit intent detection to retain departing visitors
- Content gating for premium assets
- Time-on-page or scroll-depth triggers
- Custom conditions based on audience segments and visitor attributes

Analytics & Reporting

- Performance dashboards tracking impressions, click-throughs, and conversions
- Offer-level metrics to identify top-performing content
- Integration with broader Qualified analytics for holistic pipeline visibility

### Primary Use Cases

**Event & Webinar Promotion**
Drive registrations for sponsored events, webinars, and virtual sessions by targeting high-intent visitors or specific account segments with relevant event offers.

**Content Distribution & Nurture**
Promote gated content assets (whitepapers, case studies, guides) to visitors based on their industry, role, or demonstrated interests. Move prospects through the funnel by serving stage-appropriate content.

**Account-Based Marketing (ABM)**
Create tailored offer experiences for target accounts, presenting customized content, demos, or trial offers to key stakeholders within priority organizations.

**Exit Intent Engagement**
Capture visitors showing exit behavior by presenting compelling last-chance offers, keeping them engaged and providing one more conversion opportunity before they leave.

**Trial & Demo Promotion**
Accelerate pipeline generation by promoting product trials or demo bookings to qualified visitors, with immediate scheduling options integrated into the offer flow.

**Lead Re-engagement**
Target returning visitors who haven't yet converted with personalized follow-up content or alternative CTAs based on their previous site interactions.

### Best Practices

- Define clear audience segments to ensure offer relevance. Too many filters can greatly limit visibility.
- Align offer content with visitor intent signals and account attributes
- Monitor performance analytics regularly and iterate based on conversion data
- Coordinate offer strategy with broader demand generation campaigns

### Smart Forms

Using smart forms with Qualified allows your existing lead capture form to qualify leads on-the-fly and route your most qualified visitors to your sales reps in real-time.

Traditional lead forms often come with the expectation that visitors coming to your website will have to wait hours or days to talk to your sales team. Smart forms allow you to alert your reps in real-time to those hot prospects on your site ready to talk with sales, or book a meeting with your sales team for a later time.

To request a new smart form please use [this issue template](https://gitlab.com/gitlab-com/marketing/marketing-operations/-/issues/new#) in the Marketing Operations project.

### Smart Buttons

The Smart Button changes CTAs from a static one-size-fits-all form to a bespoke buying experience. When visitors meet your ideal customer profile, trigger a real-time sales conversation with your sales team to open the door to a dynamic two-way conversation. This gets buyer questions answered in real-time and helps your sales teams instantly capture more pipeline.

To request a new smart button please use [this issue template](https://gitlab.com/gitlab-com/marketing/marketing-operations/-/issues/new#) in the Marketing Operations project.

### Resources

- [Qualified University](https://www.qualified.com/university)
- [Sales Rep Setup Guide](https://www.qualified.com/university-guides/sales-rep-setup-guide)
- [Best Practices for Sales Reps](https://www.qualified.com/university-categories/sales-reps)
- [Best Practices for Sales Managers](https://www.qualified.com/university-categories/sales-managers)
