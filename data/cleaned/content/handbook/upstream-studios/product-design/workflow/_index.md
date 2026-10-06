---
title: Product Designer Workflow
description: "Comprehensive guide to design processes, collaboration practices, and craft for Product Designers who work as strategic partners positioned upstream in the product development process."
---

Product Designers work within [Product Design](/handbook/upstream-studios/product-design/), part of [Upstream Studios](/handbook/upstream-studios/). We operate as strategic partners positioned upstream, collaborating in trios with Product Management and Engineering throughout the product development process.

For operational details like issue triaging, labeling, and scheduling, see [Product Design Operations](/handbook/upstream-studios/product-design/operations/).

## Product design process

Product Designers follow a strategic, iterative process that emphasizes early collaboration, user-centered thinking, and continuous validation. As strategic partners, we're involved from the start—shaping direction, not just executing on decisions already made.

### Define the opportunity

Start by collaborating with your PM to validate the who/what/why:

- Validate **who** you're designing for, **what** you're designing, and **why** you're designing it
- Help your PM articulate this as a [job to be done (JTBD)](/handbook/product/ux/jobs-to-be-done/): understanding the job users are trying to accomplish and the context around it
- If asked to implement a non-evidence-based "how," encourage the PM to refocus on the who/what/why to collaboratively determine the best how
- Assist your PM in defining [MVC](/handbook/product/product-principles/#the-minimal-valuable-change-mvc) success criteria, prioritizing MVC "must-haves" and non-MVC "should-haves" and "could-haves"

Note that these criteria may change based on new insights from the iterative design process and customer feedback.

### Before you design

#### Generate ideas

Strategic partners don't just respond to requests—we proactively explore, experiment, and push thinking forward. Upstream Studios values staying curious and questioning assumptions, which means actively seeking out problems worth solving.

As a Product Designer, lead and facilitate idea generation within your teams. While it's important to address known UX problems and work on product roadmaps with PMs, remember that there are also undiscovered issues worth exploring.

**Activities and resources to inspire creativity:**

- **Host workshops**: Organize synchronous (e.g., [ThinkBig!](/handbook/product/ux/thinkbig/)) or asynchronous workshops to brainstorm ideas
- **Engage with counterparts**: Reach out to [sales](/handbook/sales/), [customer success](/handbook/customer-experience/), or [marketing](/handbook/marketing/brand-experience/brand-creative/) counterparts for fresh perspectives
- **Conduct problem validation research**: Collaborate with PMs and UX Researchers to prioritize a round of [problem validation research](/handbook/upstream-studios/experience-research/problem-validation-and-methods/)
- **Join customer calls**: Participate in customer calls with PMs to hear firsthand how users describe their challenges and workflows
- **Discover unknown pain points**:
  - Use [Dovetail](/handbook/product/ux/dovetail/) to analyze data and access the research repository
  - Use [Gong](https://www.gong.io/) to search sales call recordings for insights
  - Explore [Zendesk](https://gitlab.zendesk.com/agent/) to identify existing problems
  - Review the [community forum](https://forum.gitlab.com/)

#### Understand the space

- **Review existing research**: Investigate the UXR Library. If no relevant research exists, contact the Experience Research team in Slack (`#experience_research`).
- **Conduct competitive analysis**: Analyze competitors to understand terminology, functionality, and UX conventions. Adhere to industry standards unless there is a strategic reason for deviation
- **Create user flows and journey maps**: Develop flows or journey maps to ensure comprehensive understanding of the workflow

#### Investigate possible dependencies

Platform thinking, one of our core strategic approaches, means assessing how your work impacts the broader product experience, not just your assigned area. Strong designer-to-designer connections enable this strategic perspective.

- **Collaborate with peers**: Proactively reach out to other Product Designers to gather background information and understand how your work interacts with other product areas
- **Identify and involve the DRI**: Determine the [Directly Responsible Individual (DRI)](/handbook/people-group/directly-responsible-individuals/) for the product area and involve them from the start. If unsure, consult the [Product Categories page](/handbook/product/categories/)
- **Review product kickoff**: Check the [Product Kickoff Review](https://about.gitlab.com/direction/kickoff/) to see what's planned in other stages

### Ideate and iterate

Great design starts with vision. Before breaking work into iterations, establish a clear picture of where you're headed, a north star that guides every decision. Without vision, iteration becomes aimless refinement toward local maxima rather than deliberate progress toward transformative outcomes.

Once you have a compelling vision, iteration becomes your delivery strategy. Break the vision into the smallest changes that move users meaningfully closer to that future state. Each release should validate assumptions, generate learning, and inform refinement of both the solution and the vision itself.

**Building and communicating vision:**

- **Define the north star**: Collaborate with your PM and engineering partners to articulate the end-state experience. What does success look like for users? What problems disappear entirely?
- **Use strategic artifacts**: Journey maps, storyboards, and design visions help align the trio and communicate direction to stakeholders. Keep fidelity low when the solution scope is large
- **Treat vision as living**: The design vision isn't permanent, it evolves as you ship and learn. Each iteration informs the next version of your north star

**Delivering through iteration:**

- **Start low-fidelity, increase with confidence**: Begin with the simplest artifact that communicates your idea. Increase fidelity as the solution solidifies and implementation approaches
- **Partner early with your PM**: Shape problem definition and success criteria together from Interlock planning forward. Strategic partners are involved at the start, not brought in after decisions are made
- **Collaborate with engineering**: Involve engineers early for technical feasibility and their design perspective. The best solutions emerge from diverse viewpoints challenging each other
- **Use design critiques**: Participate in critiques with other Product Designers for objective feedback and fresh approaches
- **Partner with Technical Writers**: For substantial UI text changes, collaborate with your group's Technical Writer
- **Involve your Product Design Manager**: For significant UX changes, include your PDM for broader context and strategic alignment
- **Design with data, judge with experience**: Validate high-risk directions with users through [UX research](/handbook/upstream-studios/experience-research/solution-validation-and-methods/). For lower-risk work, gather feedback post-release. Experience-based intuition can inform judgment calls, but that's the exception, not the rule
- **Use the [design and UI changes checklist](https://docs.gitlab.com/development/contributing/design/#checklist)**: Ensure readability, appearance, and functionality before shipping

**On breaking things down:**

> "Breaking things down creates psychological safety for me as a designer." - GitLab Product Designer

### Refine MVC

To maintain focus and avoid scope creep:

- **Prioritize must-haves**: Work with your PM and developers to identify "must-have" versus elements that can be deferred. Document non-MVC concepts in new issues, linking them to the original
- **High confidence, low risk changes**: If developers need to start before validation is complete, focus on high confidence, low risk changes
- **Plan ahead**: PMs and Product Designers should work together to [get 1-2 months ahead](/handbook/product-development/how-we-work/product-development-flow/#validation-track), ensuring the Build track always has well-validated opportunities ready
- **Manage large features**: Features should be buildable within 1-2 milestones. If too large, work with your PM and Engineering team to split into smaller, manageable segments

For inspiration, watch our Product Designers discuss [iteration at GitLab](https://youtu.be/0lhjzU-QZ2w).

### Present an MVC solution

**Propose one solution:**

As design DRIs with design judgment authority, we propose a single validated solution rather than multiple options. Suggesting alternatives can lead to design-by-committee and undermine the strong point of view we bring as strategic partners. If you must propose multiple solutions, clearly explain your reasoning.

**Share context and goals asynchronously:**

- Provide all necessary context in your issue to ensure your audience understands your proposal and knows how to assist
- Clarify who the solution is for, what it will enable them to do, whether you need feedback, assistance, or approval, and ping the people you want it from
- Highlight changes since the last review to facilitate understanding
- Use [collapsed content sections](https://handbook.gitlab.com/docs/markdown-guide/#collapse) to include supportive information without distracting from the main point

**Request feedback from your Product Design Manager:**

`@mention` your Product Design Manager for feedback. They can provide strategic alignment, ensure quality, and maintain functional consistency across the product.

**Focus on the customer and problem:**

Frame design discussions around the customer and the problem being solved, not the UI or functionality. Begin with the current state, explain how it fails to meet user needs, and present the proposed solution from the user's perspective.

**Anticipate and address questions:**

- Anticipate potential questions and address them in your proposal comments
- Explain your rationale to reduce feedback loops and unnecessary discussions
- Structure your proposal with [headings framed as questions](https://gitlab.com/gitlab-org/gitlab/-/issues/118442#note_276666054) to provide clarity and focus

**Follow design file guidelines:**

**Keep the SSOT updated:**

Ensure the Single Source of Truth is updated with all agreed-upon elements, including images or links to design work.

## Design reviews

Upstream Studios emphasizes that strategic partners have strong internal connections first, strong external partnerships second. Design reviews build the designer-to-designer relationships that enable strategic thinking and platform-wide collaboration.

Sharing work and gathering feedback can happen at any stage of the design process, often through mocks and open discussions in issues. Design Reviews are dedicated sessions for Product Designers to give and receive specific feedback.

**Benefits of design reviews:**

- Discovering what others are working on
- Identifying overlapping work
- Surfacing opportunities for group collaboration
- Encouraging the practice of sharing work
- Building the designer-to-designer relationships that enable strategic thinking

We prioritize [asynchronous](/handbook/values/#bias-towards-asynchronous-communication) design reviews to allow broader participation. Here's how to conduct an asynchronous review:

1. **Identify key issues**: Choose an issue with many open questions or one you're most excited to work on
2. **Select the best format**: Share your work using an issue, text blurb, screenshots, Figma file, or a short video walkthrough
3. **Provide context**: Share the customer problem, constraints, and specific feedback needs. Clearly state what feedback you want and where to provide it
4. **Post for feedback**: Share your work in the [`#ux-coworking`](https://gitlab.slack.com/app_redirect?channel=ux_coworking) Slack channel and relevant group channels, providing links to the item and the feedback location
5. **Record videos**: If recording a video, use Zoom and upload it to the [GitLab Unfiltered](https://www.youtube.com/channel/UCMtZ0sc1HHNtGGWZFDRTh5A) YouTube channel. Set the visibility to "Public" unless confidential and add it to the "UX" playlist
6. **Comment with references**: Comment on your feature issue with a link to the video and related references ([example](https://gitlab.com/gitlab-org/gitlab/-/issues/217355#note_435285696)), such as issues, epics, and Figma files. Add these links to the video description
7. **Capture feedback in issues**: Open an issue dedicated to capturing feedback ([example](https://gitlab.com/gitlab-org/gitlab/-/issues/241511)), attaching all necessary references and information needed for review
8. **Include a due date of when to receive feedback by**: When you share your work, tell the audience the date by which you need feedback. We recommend using **2 business days** when asking for design feedback from stage group stakeholders, to shorten the design feedback cycle, similar to the expected turnaround for MR reviews.

**Examples:**

- [Add a new list iteration - feedback request](https://gitlab.com/gitlab-org/gitlab/-/issues/284610)
- [Swimlane boards loading states - Skeleton loaders feedback request](https://gitlab.com/gitlab-org/gitlab/-/issues/277240)
- [Right issuable sidebar patterns feedback request](https://gitlab.com/gitlab-org/gitlab/-/issues/270117)
- [Geo: Maintenance mode design](https://gitlab.com/gitlab-org/gitlab/-/issues/201757)

### Who to include in design reviews

Determining who to include in a design review can be challenging. Here are some guidelines:

- **Stage group**: Your Product Manager, Engineering Manager, Frontend Engineers, and Product Design Manager should always have opportunities to review and provide feedback. Include them in the issue for ongoing collaboration
- **Designers**: Engage peer designers within your Section at any phase of the design process
- **Cross-stage counterparts**: If your work impacts other Stages, include those counterparts
- **Broad impact**: For changes to [navigation](/handbook/product/ux/navigation/), global headers/footers, or Pajamas patterns, request a UX Department review in the `#ux_coworking` Slack channel or mention `@gitlab-com/gitlab-ux/designers` in GitLab
- **Other departments**: If your work involves other departments (e.g., Customer Success, Sales, Marketing), invite them to provide feedback, especially when deviating from brand guidelines

If unsure who to include, consult your Product Design Manager for guidance.

## Design critiques

Upstream Studios values elevating craft and defaulting to collaboration. Design critiques embody both principles by creating space for productive conflict that makes the work stronger.

Design critiques are dedicated sessions where Product Designers exchange rigorous, constructive feedback to elevate work quality—challenging assumptions and examining the underlying rationales for design decisions beyond standard design reviews.

**Benefits:**

- Pushing designs to excellence through specific, actionable feedback that increases overall quality and value for customers
- Building a culture where constructive challenge is valued and expected
- Accelerating professional growth and design craft through deeper discussions
- Addressing issues and inconsistency earlier in the design process
- Alignment with the design system, other product areas, and UX paradigms
- Ensuring user-centered thinking remains at the forefront

We prioritize a balanced approach to design critiques that practices benevolent, [radical candor](https://www.radicalcandor.com/blog/what-is-radical-candor/) and cares personally, but challenges directly. Here's how to conduct an effective critique:

1. **Prepare the work**: Select designs that would benefit from rigorous feedback, whether early concepts or refined work
2. **Structure the critique session**:
   - Provide thorough context: Share the customer problem, constraints, design decisions made, and areas where you specifically need critique. Be clear which aspects you want challenged (5 minutes)
   - Begin by presenting work without excessive explanation (10 minutes)
   - Allow participants to ask clarifying questions and provide critique (bulk of the session)
   - Summarize key takeaways and next steps (5-10 minutes)
3. **Participate effectively**:
   - Be curious by asking questions like "have you…," "how does this…," and "why is this…" to understand the design decisions
   - Provide specific and detailed comments that encourage, challenge, and unblock the presenter
   - Connect feedback to user needs and business goals instead of personal preference
4. **Receive critique productively**:
   - Listen openly before responding
   - Take detailed notes and ask clarifying questions when needed
   - Thank participants for specific, challenging feedback
5. **Document and follow up**:
   - Capture key critique points in the relevant issue or epic
   - Share how the critique influenced your design decisions in subsequent iterations
   - Acknowledge team members whose critique led to meaningful improvements

### Setting the right mindset

To ensure critique sessions maintain both psychological safety and honest feedback, facilitators are strongly encouraged to reference the code of conduct and verbalize the mantra before beginning.

#### Code of conduct

During our critique sessions, we commit to:

1. Focus on the design work, not the designer
2. Communicate with respect and avoid offensive language or behavior
3. Challenge directly while showing we care personally
4. Provide specific, actionable feedback and reasoning rather than vague comments
5. Practice genuine curiosity to understand design decisions before critiquing them
6. Remain open to different perspectives and approaches
7. Receive critique openly and be willing to let go of unsuccessful elements
8. Engage in candid conversation and spirited debate with passion for our craft

## Design principles and approaches

### Sophisticated simplicity

We aim for **sophisticated simplicity**, balancing three principles to create optimal user experiences:

1. **Structure** - Organize and arrange content and concepts into meaningful groups and patterns
2. **Discovery** - Ensure users can interact and explore in ways that promote learning and proficiency while minimizing mistakes
3. **Capability** - Provide features and functions that enable users to complete tasks and automate processes

Balancing these principles is crucial:

- **Structure + discovery without capability**: Simple experience suitable for static content but lacking functional richness
- **Discovery + capability without structure**: Robust and intriguing experience that is difficult to master due to lack of guiding structure
- **Structure + capability without discovery**: Sophisticated complexity—functionality is abundant, but users struggle with learning and understanding

Achieving sophisticated simplicity reduces friction for accessing basic functionality, provides quick access to powerful features, and helps users become proficient in completing tasks.

**Consider these questions when designing:**

- Is the content hierarchy and flow clear?
- Are similar items grouped, and are the groups clearly defined?
- Does this content or functionality need to be visible all the time and for everyone?
- Is this content or functionality necessary in this context? Is it both helpful *and* essential?
- Does discovery help users avoid mistakes or recover from mistakes easily?
- Does the structure support discovery and the use of advanced capabilities?
- Is this feature or capability needed or used, or what would happen if it were removed?
- Is everything "in reach," or are users left wandering?

### Designing with modes

Design must work in all generally available modes, which currently includes light and dark mode. Keep these considerations in mind as you design:

- Light mode is the most used mode preference in the product, the default for Pajamas UI Kit design assets, and the default for [usability tests](/handbook/upstream-studios/experience-research/usability-testing/#steps-for-conducting-a-usability-test)
- The [design system](https://design.gitlab.com) provides design tokens and components that work in supported modes
- Take extra care when mode is a primary factor in customer outcomes
- Use analytics data to determine which mode should be your primary design focus

**Dark mode design principles:**

Dark mode design must align with these principles:

- **Forward elements are lighter, receding ones are darker**: This mimics natural light behavior. In dark mode, brighter elements create depth, ensuring important content stands out without relying heavily on borders or shadows
- **Reduced color saturation**: In a dark UI, color naturally stands out more. Instead of flooding backgrounds with color, use color selectively to draw attention where needed
- **Dimmed, not inverted**: Dark mode should feel like dimming the lights rather than completely inverting the interface. Carefully decide which elements to darken and which to brighten to maintain content clarity

For design tokens and mode-specific components, see the [Pajamas Design System](https://design.gitlab.com).

### Additional design guidance

- **AI design**: Follow the [AI design guide](/handbook/upstream-studios/product-design/workflow/ai-design/) for designing AI-powered features
- **Design modes**: See [Figma and design tools](/handbook/upstream-studios/product-design/workflow/figma/) for guidance on designing for light and dark modes
- **Design principles**: Review the complete [design principles in Pajamas](https://design.gitlab.com/get-started/principles/)

## Partnering with Technical Writers

Technical Writing is a core discipline within Upstream Studios alongside Product Design. Our words shape the product experience, and collaboration between designers and writers strengthens the complete stack we deliver.

When adding or changing UI text, it's essential to collaborate with your group's Technical Writer. This collaboration should begin during the Product [Design phase](/handbook/product-development/how-we-work/product-development-flow/#validation-phase-4-design).

UI text includes button or menu labels, error messages, log files, user-assistance microcopy, notification emails, and any other text visible in the UI. Changes to UI text can significantly impact documentation steps.

**To ensure a smooth process:**

- **Label the issue and MR**: Apply the [UI text](https://gitlab.com/gitlab-org/gitlab/-/issues?label_name%5B%5D=UI+text) and `documentation` labels
- **Request a review**: Message the [Technical Writer for the group](/handbook/marketing/product-and-technical-marketing/technical-writing/#assignments) in the design issue to request a review. Specify files or lines to review and how to preview or understand the context
- **Collaborate on finalizing text**: Work closely with the Technical Writer to finalize the UI text, ensuring it's usable and accurate
- **Incorporate feedback from other departments**: When other departments provide input on UI copy, ask for goals rather than specific text to avoid extensive revisions and design-by-committee

### Collaborating on in-product reference information

Sometimes the designer, PM, and technical writer agree to display additional [in-product reference information](https://design.gitlab.com/usability/contextual-help/) in a [drawer component](https://design.gitlab.com/components/drawer/). The reference information should align with the existing documentation for the feature.

1. **Draft copy**: The designer drafts the content for the drawer, identifying necessary information for user goals. This draft should be as close as possible to the final version
2. **Mark draft status**: Indicate that the drawer content is not final, using a text watermark like "waiting on documentation," "draft," or "placeholder," or a pin in the Figma file
3. **Follow design to development process**:
   - Developers create the drawer and documentation as part of feature code MR
   - The Technical Writer reviews the documentation and drawer content
   - Once the documentation is published, the drawer is populated with the content

## Partnering with UX Researchers

UX Research is a core discipline within Upstream Studios alongside Product Design. Research informs design and drives what we build, ensuring every experience is grounded in user understanding.

UX Researchers collaborate with Product Managers and Product Designers to ensure research projects are targeted and provide valuable insights.

- **Contact your UX Researcher**: Reach out to your [UX Researcher](/handbook/upstream-studios/experience-research/how-uxr-team-operates/) to conduct or guide research
- **Document findings**: Ensure research findings are documented according to established processes

## Socializing your work

Sharing design work allows Product Designers to mentor, engage, and inspire peers inside and outside GitLab. It widens your perspective and helps you understand the broader impact of design decisions on the product.

**Internal socialization:**

- **Slack**: Share insights and updates
- **Unfiltered YouTube**: Provide updates and gather feedback
- **[Upstream Forum](/handbook/product/ux/upstream-forum/)**: Open pathways for collaboration with teams addressing similar objectives and JTBDs

**External socialization:**

- **[Blog posts](/handbook/marketing/blog/)**: Write about your design decisions and processes
- **[Speaking at events/conferences](/handbook/marketing/corporate-communications/speaking-resources/)**: Share your work and insights

These activities not only inspire other designers but also increase visibility for Upstream Studios, enhancing transparency and attracting potential applicants.
