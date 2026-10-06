---
title: "Design and run your own cross-functional workshop"
description: "This page is for anyone at GitLab who wants to run a sync workshop to adopt a holistic perspective for the challenge at hand. This guide covers three types of workshops (Problem Framing, Journey Mapping, Ideation), the core questions each answers, and the end-to-end process of designing and running a workshop (including a Claude Skill)"
---

## **Design and run your own cross-functional workshop**

This page is for anyone at GitLab who wants to run a sync workshop to adopt a holistic perspective for the challenge at hand. This guide covers three types of workshops (Problem Framing, Journey Mapping, Ideation), the core questions each answers, and the end-to-end process of designing and running a workshop (including a Claude Skill)
The Claude Skill called as design-workshop can be found in the [Product Design folder in the GitLab AI Marketplace, internal only](https://gitlab.com/gitlab-com/marketplace/-/tree/main/product/ux/product-design?ref_type=heads).

**Run a workshop when a group needs to think together to produce something. Skip it when you already know what needs to be done.** A workshop usually needs follow up, so don't expect one session to solve everything. Workshops can range from an hour to multi-day events such as a [Design Sprint](/handbook/product/ux/design-sprint/). This guide helps design 60 to 90 minute sessions, conducted using Zoom, using a FigJam board as a shared canvas. This guide also advocates for breakout groups of 2-3 where needed to ensure everyone can contribute. While it is expected for people to read upfront, it is best to design a session as if no one did.

## **What type of workshop do you need?**

|  | Use it when | What you walk out with | Watch out for |
| :---- | :---- | :---- | :---- |
| **Problem Framing** | The problem is fuzzy or people are jumping to solutions when the core problem isn't defined yet | Shared problem + knowns vs unknowns | Drifting into solving |
| **Journey Mapping** | The experience crosses stages and you need a group of people to see the picture together | Mapped journey + top moments to act on | Mapping everything with no lens |
| **Ideation** | The problem is agreed upon and you need to explore different concept directions | Ranked shortlist + one next step each | Anchoring on the first idea |

Sessions can also blend depending on previous work done. GitLab's UX Researchers have also mapped out several workshops centered on research (retrospectives, research planning, aligning on recommendations, etc) that may be of interest. You can read about these [on this handbook page](/handbook/upstream-studios/experience-research/how-to-conduct-ux-research-workshops/).

### **What you go in with, what you walk out with for each workshop type:**

Each workshop type has prerequisites for it to be successful. Below are prerequisites (what you go in with) and the questions you can expect answers to (which also help you determine the workshop agenda):

#### **Problem Framing/Discovery**

You go in with:

* A gist of problems or a problem statement for the room to react to.
* The people who hold the context, present in the session.
* No need for a solution yet.

You walk out with answers to questions such as:

* What are all the problems in this space?
* What do we know (and how)? What are the biggest unknowns that we need to figure out?
* What are our risky assumptions and how might we validate them?
* What is the core problem statement?

#### **Journey Mapping/Blueprinting**

You go in with:

* An understanding of why you are mapping a journey and what decisions will be made based on this.
* An experience that is defined enough, with end-to-end stages and key user steps. Avoid going in with a blank canvas as that can be done upfront and async.
* People who know the real experience (or research standing in for them).

You walk out with answers to questions such as:

* What are our knowledge gaps?
* Where does this journey break? Who else do we need?
* Which moments matter most, and why those?
* What is invisible here: the backstage work, the roles, the handoffs?

#### **Ideation/Co-creation**

You go in with the problem already understood and agreed upon, plus the known constraints. This is the strongest prerequisite. If the problem is not agreed upon, you are not ready to ideate.

You walk out with answers to questions such as:

* How might we solve this? (generate wide, on your own first)
* Which ideas cluster, and which are worth keeping?
* What are the top picks and why?
* How might we break this idea and create a storyboard or a user flow?

## **The shape of a workshop**

Every session has a similar arc where the engine is one or more diverge-converge cycles. This rhythm makes a session produce something rather than just discuss until time runs out.

* **Diverge** means the group generates options in parallel, wide and messy, before narrowing anything. Individual sticky-writing, breakout brainstorms, walking a journey and marking moments are activities that fall in this category.
* **Converge** means the group takes what came out of diverge and narrows it, by ranking, clustering, or picking, instead of just producing a pile of ideas.

This rhythm matters because a room that only diverges ends with a wall of stickies and no decision, and a room that only converges skips straight to the first idea anyone said out loud. Alternating the two is what makes a session produce something rather than just discussions until time runs out.

Note for facilitators: Don't hesitate to push people through to the next steps when they are spending too much time in one area. Inform the group that you have a plan to get through, will move them along as needed, and can put issues/topics in the parking lot for a later moment.

**Frame:** goal, why we need this workshop, agenda, parking lot. Include any upfront reading here.

**Warm up:** Only include if it is really needed to get people into a certain mindset. Keep it concise, and make sure it produces raw material the next block uses.

**Load context:** someone introduces the flow, pitch or research. Keep it short.

**Cycle 1, on the problem**

* **Diverge:** Breakout groups generate in parallel, embracing some silent individual time and discussion.
* **Converge:** Everything comes into one space and gets ranked or clustered.

**Cycle 2, on the solution (not every workshop needs this second cycle)**

* **Diverge again:** Groups build on the converged output. This is where solutions happen.
* **Converge again:** Compare the built work and agree on a next step. Keep it light, a share, or a react and pick. Don't skip it and don't collapse into "Close", else the session ends without a clear direction.

**Close:** takeaway, feedback on the session, next steps.

## **How to set up a workshop: the work before, during, and after a workshop**

This section describes the stages of setting up and running a workshop. We also have a Claude Skill that can help you run through all the stages. More on that in the next section.

### **Stage 0: Intake, decide the type, and the basics**

* Pin down the real challenges behind the topic, then pick the type: Problem Framing, Journey Mapping, Ideation, or a blend.
* Check if you have the prerequisites covered for the workshop type.

### **Stage 1: Write a workshop brief**

* As the facilitator, you might not always be the workshop sponsor or a decision maker. A one-page brief ensures you are aligned with your stakeholders.
* [Here is the template for a Workshop Brief](https://docs.google.com/document/d/1wt4NIJoCxJm20LRw-SnaSbJ7HbcGSXboa2tUDqMZ0o4/edit?usp=drive_link) that you can create as a Google doc or paste into a GitLab issue. You can continue to use this for the next stage where you break the agenda down into activities. This will help in Stage 3 to create a FigJam board in a matter of minutes.
* Share it with people whose time you want, plus whoever signs off on that time. It is a comprehension check and a gate: get a yes before you build.

### **Stage 2: Design the activities for the agenda (aka Run of Show)**

* Follow the shape of a workshop as described above to create an agenda and activities for it. Here are links to external libraries of workshop activities from [NN/group](https://www.nngroup.com/articles/workshop-activities/) and [SessionLab](https://www.sessionlab.com/library/design) respectively.
* Ensure every activity has a purpose. The output of one block feeds the next, or lands as action items before the topic changes. If you cannot say in one line why you need an activity, cut it.
* Timings in fives (such as 5, 10 minutes) help cover any extra discussions.
  * Rough proportions: frame and context 15 to 20%, diverge blocks the largest share at 20 to 25 minutes each, converge and share 10 to 15 minutes, close 10 to 15%.
* **Decide how groups work.** Default 2 to 3 per breakout group to ensure richer contribution. Assign quiet individual time before group time to ensure everyone can contribute.
* **Write the board the way you would say it out loud.** Prompts are questions people can answer ("What breaks trust and interest?", not "Identify friction points in the trust experience"). Facilitator notes read as speech ("Suggest 5 minutes on your own first, then discuss", not "Participants will engage in individual ideation"). Converge points have a Key Questions box where you need one to push past the obvious answer.
* **Close:** Ask everyone for one takeaway each, feedback on the session (can do async too), and follow-up actions/questions.

### **Stage 3: Build the workshop board with Figma AI**

If you prefer to run the workshop in a Google doc, then follow [GitLab's meeting guidelines](/handbook/company/culture/all-remote/live-doc-meetings/).

* Paste the Run of Show in FigJam's AI panel.
* Let Figma AI lay out the FigJam board, then check it against your tone of voice and preferred activity layout.

### **Stage 4: Facilitating the workshop**

* Ask someone to keep the time for you if you don't want to multitask.
* You can ask the workshop sponsor/decision maker to kick off and close the workshop so that they can set the context and next steps.
* Read [the ultimate guide to facilitation](https://facilitator.com/blog/the-ultimate-guide-to-facilitation) for more tips on how to facilitate a session.

### **Stage 5: Follow up**

* Write a concise summary for someone who was not present during the workshop and include it in the workshop board if possible.
* Pull out what the room produced, the top moments or concepts, and the open questions. Create and share action items and artifacts.
* A workshop that never gets followed up quietly becomes a nice afternoon that changed nothing.

## **How to use Design-Workshop Claude Skill**

Use the Design-Workshop Claude Skill to help you run through all the stages of setting up a workshop. The Skill can be found in the [Product Design folder in GitLab AI Marketplace](https://gitlab.com/gitlab-com/marketplace/-/tree/main/product/ux/product-design?ref_type=heads) or [Design-Workshop Claude Skill in Google Drive](https://drive.google.com/file/d/1VM_HiqUV5wl44cVL8qEPfjoQPmM9YrMK/view).
The Skill can also be used if you already have an agenda/FigJam board. This Skill walks you through the stages above one at a time, producing a concrete output at each step, so you don't have to build a brief, agenda, or board from scratch. The Skill stops after each stage and waits for your edits before moving to the next.

**What you give it:** You don't need to write a brief or prep any material first. Just tell it what you're planning to workshop and answer its questions as it asks them. If you already have a FigJam board or a brief, give that as input.

**What it gives you back, one stage at a time:**

| Stage | Output from the Skill |
| :---- | :---- |
| Intake, decide the type, and the basics | A shortlist of what's known and what's still needed, plus the workshop type (Problem Framing, Journey Mapping, or Ideation) |
| Write a workshop brief |  A one-page brief to send to whoever's time you need |
| Design the activities for the agenda (aka Run of Show) | A run of show with timings and facilitator notes |
|  Build the workshop board with Figma AI | A text prompt you paste into FigJam's AI panel to build the board |
| Facilitating the workshop | Live tips for running the session, asked for on the day |
| Follow up | A write-up pulled from the board, for people who weren't there |

### **Want help?**

If you have a session coming up and want a second pair of eyes on the frame, the activities or the board, send a message to Bindu Upadhyay or ask in the #experience-research Slack channel. Happy to review what you have or help you design from scratch.
