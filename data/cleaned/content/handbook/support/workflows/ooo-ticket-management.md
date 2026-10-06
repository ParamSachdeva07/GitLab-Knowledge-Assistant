---
title: OOO Ticket Management
category: Handling tickets
description: How to manage assigned tickets when going on scheduled PTO
---

## Overview

These workflows discuss how support engineers can asynchronously manage and summarize on-going assigned tickets within Zendesk before they go on PTO.

### Using the OOO Ticket Summary macro

As part of this workflow, the Support Engineer going on leave will leave notes on currently Open, Pending and On-Hold tickets with a macro. This macro will provide a summary of the ticket and add the Support Engineer to the ticket's CC list. It is recommended to follow this workflow for all high-priority tickets or when taking three or more days of PTO. Pending tickets do not need to be manually unassigned as the OOO macros enable automatic unassignment when customers respond.

### Ticket Prioritization Workflow

### Before Going on PTO

- Optional: You may choose to document your tickets by making a list or taking a screenshot, including the description and ID numbers. This can serve as a helpful backup reference.
- Understand Automation: A ticket will automatically be unassigned and placed onto the Global Queue when the assignee has used the OOO macros and is marked as unavailable in the Out of Office app, and the customer responds to the ticket.

#### For Severity 2 and Above Tickets

When planning PTO with high-priority tickets in your queue:

1. Find an appropriate assignee through the following progression:
   - Check for colleagues on the same shift.
   - Check regional support channels if no one is available on your shift.
   - If no assignee can be found, escalate to your manager.
1. Conduct a warm handover with the new assignee:
   - Schedule a pairing session or have a detailed Slack discussion.
   - Walk through the ticket details, customer context, and current status.
   - Apply the `General::OOO Ticket Summary` macro using the below Flow Chart Workflow.
   - The new Assignee takes assignment of the ticket.

#### For Severity 3 and Below Tickets

For lower-priority tickets:

1. Inform customers of your upcoming absence.
2. Set your ticket to Pending status.
3. Apply the `General::OOO Ticket Summary` macro to all tickets.

#### For solved tickets

Solved tickets can reopen if the customer replies. We need to apply the OOO macro to them as well.

1. In Zendesk click on your profile icon on the top right and then "View profile"
2. Under "status: solved" select the tickets by adding a checkbox
3. Click on the black "Edit X ticket(s)" button on the top right
4. Apply "OOO Solved" macro

This ensures those tickets are properly unassigned and returned to the queue if a customer responds while you are away.

### Workflow

Go to the My Assigned Tickets view in Zendesk. For each ticket you wish to summarize because you anticipate on-going work will be required, do the following:

1. Use the `General::OOO Ticket Summary` macro.
2. Fill in the sections of the internal note with details for your peers. It is important that you summarize:
   - What is the problem to be solved?
   - Action Taken?
   - Next Steps Needed? Alternatively, clarify if you are uncertain what the next steps are.
   - Blockers?
   - Return Date.
3. Feel free to also ask regional peers if they can pickup tickets in other forms of communication, such as Slack, but Zendesk should remain as the single source of truth for tickets that need attention from other team members.

#### Ticket Handover Process

When taking over a ticket from a colleague who is on PTO:

1. Review unassigned tickets for your region from the Global Support Ticket View.
1. Assign the ticket by clicking `take it`. It is important that you also perform an update (such as adding an internal note or sending a customer update) to document your work.
1. Set the Zendesk field `Handover Status` to `Handover Completed`.
1. After the return date specified in the macro, you can liaise with the original engineer to hand the ticket back. If needed, schedule a knowledge transfer session with the returning engineer.

#### Returning from PTO Process

1. Optional: Review the status of the tickets assigned to you before your PTO. You can coordinate with the new owner if it makes sense to reclaim ownership. This could be beneficial if you have an established rapport with the customer, possess strong technical expertise on the issue, or had previously agreed to continue the investigation upon your return.
1. Apply the `General::Return from OOO` macro on all of your active tickets. This is important to ensure the automatic unassignment behaviour is turned off now that you are back.

Tip: you can use the [Zendesk bulk edit functionality](https://support.zendesk.com/hc/en-us/articles/4408886890906-Managing-tickets-in-bulk) to apply the macro to multiple tickets at once. Please exercise caution when using this functionality.

**Important notes on the macros:**

1. If you **do not** run the OOO macro when going on PTO, tickets will **not** be automatically unassigned when customers respond.
1. If you **do not** run the Return from OOO macro when returning, tickets **will** continue to be automatically unassigned when customers respond.

#### PTO FlowChart

```mermaid
flowchart TD
    Start[Engineer Planning PTO] --> DocumentTickets[Document Ticket List/Screenshot]
    DocumentTickets --> TicketPriority{Check Priority?}

    TicketPriority -->|Sev 2 and Above| HighPriority[High Priority Process]
    TicketPriority -->|Sev 3 and Below| NormalPriority[Normal Priority Process]

    HighPriority --> NotifyManager[Notify Manager 2+ Days Before]
    NotifyManager --> FindAssignee[Find Assignee]

    FindAssignee --> SameShift[Check Same Shift]
    SameShift --> OtherRegions[Check Regional Channels]
    OtherRegions -->|Found| WarmHandover[Conduct Warm Handover]
    OtherRegions -->|Not Found| EscalateManager[Escalate to Manager]

    WarmHandover --> PairingSession[Pairing Session/Slack Discussion]
    PairingSession --> ApplyMacro[Apply OOO Ticket Summary Macro]

    NormalPriority --> InformCustomer[Inform Customers of Absence]
    InformCustomer --> SetPending[Set to Pending Status]
    SetPending --> ApplyMacro[Apply OOO Ticket Summary Macro]


    subgraph MacroDetails [OOO Ticket Summary]
        ApplyMacro --> Summary[Add Ticket Summary]
        Summary --> AutoUnassign["Note: Ticket will auto-unassign<br/>if customer responds while you are OOO"]
        AutoUnassign --> DocumentDetails[Document:
        - Problem Description
        - Action Taken
        - Next Steps Needed
        - Blockers
        - Return Date]
    end

    DocumentDetails --> |Return from PTO| ReviewPrePtoTickets[Review your tickets assigned to you before PTO]
    ReviewPrePtoTickets --> ApplyReturnPtoMacro[Apply the General::Return from OOO macro]
```
