---
title: Security Policies - How we prioritize our current work?
---

## How do we prioritize our current work?

Please refer to the flowchart provided below to understand the process we follow when determining the next task to work on after completing all assigned tasks.

<div class="x-scrollable">
<div style="width: 1800px;">

```mermaid
flowchart TD
    AA{Is there anything on the board<br/>that is currently assigned to you<br/>and you are not blocked?} -->|Yes| A{Take a look at assigned issues according to their states:}
    AA -->|No| BA{Is there anything on<br/>the board you can work on?}
    A -->|workflow::verification| B(Verify the issue,<br/>provide results as a comment<br/>and close it.)
    A -->|workflow::in review| C{All MRs for the issue are merged<br/>, and the change is already deployed?}
    C -->|Yes| D(Verify the issue,<br/>provide results as a comment<br/>and unassign yourself.<br/>Close it when you are not an author of the change,<br/>otherwise once you are unassigned<br/>the bot will select the next person to verify it.)
    C -->|No| E(Wait for review and address comments<br/>in your MRs if there are any.)
    A -->|workflow::in dev / workflow::ready for development| I(Make sure it is in the `workflow::in dev` state.<br/>Review the issue for clarity,<br/>create your implementation plan as part of delivering the MR,<br/>and work on it until you have an MR ready.<br/>Then move it to `workflow::in review`.<br/>If the issue is complex, ask a team member to review your plan.)
    BA -->|Yes| BB(Take a look at unassigned issues on the board<br/>according to this order:<br/>- workflow::verification,<br/>- workflow::ready for development.<br/><br/>When you see another team member is assigned to the issue<br/>and you would like to reduce their load and help them,<br/>reach out to them asking how you can help.)
    BA -->|No| BC(Go to Priorities page.)
    BC --> BD{Are you a DRI for one of the Epics?}
    BD -->|Yes| BE(Start with a spike/PoC to validate the approach,<br/>then prepare implementation issues.)
    BD -->|No| BF(Take a look at the board<br/>for future milestone for issues in<br/>`workflow::ready for development` state<br/>and start working on them.)
```

</div>
</div>
