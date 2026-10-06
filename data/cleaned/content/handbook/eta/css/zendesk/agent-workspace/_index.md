---
title: 'Agent Workspace'
description: 'Documentation on the Zendesk Agent Workspace'
---

The Zendesk Agent Workspace is the primary interface agents use to receive, manage, and respond to tickets. This page covers the key features and components available within the workspace and references relevant GitLab or Zendesk documentation where applicable.

## Ticket Tabs

Agents can have multiple tickets open simultaneously, each accessible via a tab at the top of the workspace. See [Using ticket tabs to manage conversations](https://support.zendesk.com/hc/en-us/articles/4408844108826-Using-ticket-tabs-to-manage-conversations).

## Ticket Summaries

Ticket Summaries generate an AI recap of a ticket's comments (including internal notes if enabled) in a banner you can refresh, collapse/expand, hide/show, or regenerate for a new language. See [Summarizing ticket comments using generative AI](https://support.zendesk.com/hc/en-us/articles/8037649972634-Summarizing-ticket-comments-using-generative-AI).

## Ticket Metadata

The left-hand panel of a ticket contains the core metadata fields used to classify and route the ticket.

### Brand

The Zendesk brand the ticket was submitted to. See [Multibrand resources](https://support.zendesk.com/hc/en-us/articles/4408833921306-Multibrand-resources).

#### Requester

The end-user who submitted the ticket. See [Changing the ticket requester](https://support.zendesk.com/hc/en-us/articles/4408886900506-Updating-ticket-requesters-and-organizations#topic_jwd_bnr_wt).

#### Assignee

The agent and the associated group currently responsible for the ticket.

#### CC List

Additional agents or end-users copied on ticket updates.

#### Ticket Form

The form used to capture structured information from the requester. For more information on how ticket forms are managed, see [Customer Support Systems documentation on ticket forms](../tickets/forms/).

#### Tags

Labels automatically or manually applied to tickets for routing, reporting, and automation. For more information on how we use and manage tags, see [Customer Support Systems documentation on tags](../tags/).

#### Ticket Type

Classifies the ticket as Question, Incident, Problem, or Task. See [About ticket types](https://support.zendesk.com/hc/en-us/articles/4408886739098-About-ticket-fields#:~:text=your%20business%20rules.-,Type,-There%20are%20four).

### Custom Ticket Fields

Additional fields designed to capture information specific to GitLab's needs. These are used in routing, automation and reporting. For more information on how ticket forms are managed, see [Customer Support Systems documentation on fields](../tickets/fields/).

## Macros

The **Apply macro** button allows agents to apply a pre-configured set of actions to a ticket in a single click, such as adding a comment, setting fields, or changing ticket status. For more information on how macros are used and managed, see [Customer Support Systems documentation on macros](../macros/).

## Comment History

The conversation thread displays comments in chronological order — oldest at the top, newest at the bottom.

## Comment Editor

The comment editor is used to compose and send public replies or internal notes. It allows agents to format text and add attachments.

### Public and Internal Comments

Agents can toggle between **Public reply** (visible to the requester) and **Internal note** (visible only to agents). See [Adding comments to tickets](https://support.zendesk.com/hc/en-us/articles/4408828489370-Adding-comments-to-tickets).

### Draft Mode

This ensures a confirmation window is shown to agents submitting public comment updates before the comment is sent publicly on the ticket. See [Writing drafts of public replies in tickets](https://support.zendesk.com/hc/en-us/articles/5627101293722-Writing-drafts-of-public-replies-in-tickets).

### Text Formatting

The editor supports rich text formatting including bold, italic, lists, headings, and code blocks. See [Adding formatting to ticket comments](https://support.zendesk.com/hc/en-us/articles/4408828489370-Adding-comments-to-tickets#topic_djd_2jx_4y). In addition to rich text formatting, markdown commands are also supported. See [Formatting text with Markdown](https://support.zendesk.com/hc/en-us/articles/4408846544922).

### Emojis

Agents can insert emojis into comments using the emoji picker in the comment editor toolbar.

### Attachments

Files can be attached to both public replies and internal notes directly from the comment editor. See [Adding attachments to ticket comments](https://support.zendesk.com/hc/en-us/articles/4408835822618-Adding-attachments-to-ticket-comments).

### Hyperlinks

Text within comments can be formatted as clickable hyperlinks using the comment editor toolbar.

### Enhance Writing

Enhance Writing lets you expand, simplify, adjust the tone (friendlier or more formal), match your own voice, or apply a custom prompt to your ticket comments. See [Enhancing ticket comments using generative AI](https://support.zendesk.com/hc/en-us/articles/5608712782362-Enhancing-ticket-comments-using-generative-AI).

### Glean Integration

The comment editor integrates with [Glean](/handbook/eta/ai/tools/glean/) and displays a dedicated Glean button in the toolbar. It allows agents to draft responses to customers using generative AI.

## Search

The search icon in the top navigation bar opens a global search interface allowing agents to find tickets, users, and organisations across Zendesk. See [Using Zendesk Support advanced search](https://support.zendesk.com/hc/en-us/articles/4408835086106-Using-Zendesk-Support-advanced-search).

## Profile Menu

The profile menu in the top navigation bar provides access to the agent's profile, notification settings, and the ability to set their online status.

## Customer Context Panel

The context panel on the right side of a ticket surfaces information about the requester, including their profile, recent tickets, and interaction history. See [Using the context panel](https://support.zendesk.com/hc/en-us/articles/4408836526362-Using-the-context-panel).

## Knowledge Panel

The Knowledge panel allows agents to search the GitLab Help Centre, link articles to tickets, and quote content directly into replies. See [Using help center content in your tickets without leaving Agent Workspace](https://support.zendesk.com/hc/en-us/articles/5581313653530-Using-help-center-content-in-your-tickets-without-leaving-Agent-Workspace).

## Apps

Zendesk apps extend agent functionality and appear in the context panel. For information on which apps are available and how they are configured, see the [GitLab Support Systems documentation on Zendesk apps](../apps/).

### Pinning Apps

Agents can pin frequently used apps to the context panel so they are easily accessible, instead of scrolling through the entire list of currently installed apps. See [Managing personal app shortcuts](https://support.zendesk.com/hc/en-us/articles/6066877041690-Managing-personal-app-shortcuts).

## Submitting Tickets

### Submit Button

The **Submit as** button at the bottom of the ticket allows agents to save the ticket in a specific status. See [Updating a ticket and changing its status](https://support.zendesk.com/hc/en-us/articles/4408832151834-Updating-and-solving-tickets#id_xsq_5f5_st).

### Post-Submit Navigation Options

Agents can set the default behaviour of a ticket once it has been submitted. The options are as follows:

- **Stay on ticket** — Remain on the current ticket after submission.
- **Next ticket in view** — Move to the next ticket in the current view.
- **Close ticket** — Close the ticket tab and return to the previous screen.

See [Working with tickets in a view](https://support.zendesk.com/hc/en-us/articles/4408829483930-Accessing-your-views-of-tickets).

## Translating Tickets

### Overview
 
Zendesk provides AI-powered ticket translations within the Agent Workspace, allowing agents to communicate with end users who speak a different language. When activated, both incoming messages (from the customer) and outgoing messages (from the agent) are automatically translated using Amazon Nova Micro in real time.
 
### How Translation Works
 
#### What the Agent Sees
 
When a language difference is detected, a translation banner appears at the top of the ticket informing the agent of the customer's detected language. The agent can then:
 
- **Click "Translate"** — incoming messages are translated to the agent's language, and outgoing messages are translated to the customer's language.
- **Dismiss the banner** — decline translation for now (can be re-enabled later via the ticket Options menu).
- **Correct the detected language** — use the dropdown in the banner to select the correct language if detection was wrong.

Once translation is active on a ticket:
 
- Translated tickets will provide an indication that the ticket is currently being translated.
- Agents can click "Show original" on any customer message to see the untranslated text.
- Agents can click "Show translation" on their own messages to see what was sent to the customer.
- The agent's translation preference persists when the ticket is closed and reopened — they don't need to re-enable it.
- Translations on the current ticket can be stopped by clicking the "Stop" button in the translation banner.

#### What the Customer Sees
 
Customers are not notified when an agent enables translation. Agent messages will automatically appear in the customer's detected language, whether viewed via email or the Support Portal.
 
### Translating an Outbound Message Before Sending
 
When composing an outgoing message, agents can click the **Translate** button in the composer to generate the translation before sending it to the customer. This cannot be easily reverted, so if modifications needs to be made to a message, it will need to be written from scratch.

For more information, see [Translating conversations in tickets](https://support.zendesk.com/hc/en-us/articles/6327770807450-Translating-conversations-in-tickets).

## Additional Resources

- [About the Zendesk Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408821259930-About-the-Zendesk-Agent-Workspace)
- [Documentation resources for the Zendesk Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408827107226-Documentation-resources-for-the-Zendesk-Agent-Workspace)
