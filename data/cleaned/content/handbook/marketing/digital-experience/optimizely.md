---
title: "Digital Experience Optimization Program"
description: "The Digital Experience Optimization Program is a cross-functional initiative designed to systematically improve digital performance through disciplined, data-informed experimentation across [about.gitlab.com](http://about.gitlab.com). The program establishes a consistent operating model for identifying high-impact opportunities, forming clear hypotheses, executing tests effectively, and translating results into actionable business decisions. This program ensures experimentation decisions are grounded in measurable business impact, resource efficiency, and statistical rigor—enabling us to scale growth with confidence rather than intuition.
"
---

## Our Tools

- **Optimizely**: An experimentation platform that enables teams to test changes in live digital experiences across  [about.gitlab.com](http://about.gitlab.com), measure their impact with statistical rigor, and make confident optimization decisions based on real user behaviour. The tool allows for team members with all levels of technical ability to implement experiments through no-code-required editors.
- **Figma**: A design platform that enables teams to visually ideate and mockup experiments before proceeding with experiment implementation.
- **ContentSquare**: An analytics platform that enables self-serve data analysis (e.g engagement metrics, heat maps, session replays, surveys) on experiment opportunity locations or flows.
- **Google Analytics**: An analytics platform that is used in combination with test result performance for trial registration metrics since Optimizely is not currently implemented on gitlab.com.
- **[Tableau Digital Experience Dashboard](https://10az.online.tableau.com/t/gitlab/views/DigitalExperience_17485613133410/Overview)**: An analytics platform that is used to self-serve page traffic data and average page conversion rates.

## Our Methodologies

### Step 1: Opportunity Model

To identify high impact areas for experimentation, use an opportunity model which helps us understand the possible impact any area can have.

| Framework | Example | Importance |
|---|---|---|
| Opportunity location | DevSecOps free trial page | Clearly defined location/flow |
| Primary conversion type | High value trials | Directly impacts OKR |
| Traffic volume | 1m unique visitors in FY26 | Represents impact scale |
| Conversion rate | 0.9% Avg. CVR in FY26 | Represents baseline metric |
| Estimated impact | (1m x 0.009) x 0.10 | Represents possible impact |
| Business efficiency | Cost per lead: $100 | Improves spend efficiency |

**Opportunity statement example**: *“If we improve the DevSecOps Free Trial page’s high value free trial conversion rate by 10%, it may result in an additional 900 high value trials over a full fiscal year for the same cost per lead—or—effectively generating the same volume of leads for $100k less.”*

### Step 2: Hypothesis Statement

We develop hypotheses in order to effectively establish the problem, how the problem could be solved, and how we’ll know when it’s solved.

| Framework | Example | Importance |
|---|---|---|
| What problem are we solving | Data has shown users are struggling to find the primary conversion point on the DevSecOps free trial page. | Identify/validate problem |
| What could solve the problem | Simplifying the path to conversion, removing unnecessary links and simplifying supporting content, could result in users understanding where to proceed next. | Identify possible solution |
| What is the expected result | Increased high value trial conversion volume. | Establish success metric |

**Opportunity statement example**: *“We believe by simplifying the path to conversion on the DevSecOps Free Trial Page, removing unnecessary links and simplifying supporting content, it could result in a higher volume of free trial CTA click-throughs, and ultimately, a higher volume of high value free trial conversions”*

### Step 3: Experiment Execution

This section outlines different test types and statistical rigor expectations. The test you’re executing will either be a statistical significant test or a directional (“do-no-harm”) test. If the duration to statistical significance is under 3 weeks, it is considered a statistically significant test-type. Tests projected to require extended durations to reach statistical significance may be categorized as directional (“do-no-harm”) tests, where learning velocity is prioritized over definitive proof.

We use our [Duration Estimate Calculator](https://docs.google.com/spreadsheets/d/1WWL40CEV8ZIi8uBSorbGg-uZWUty8tx2/edit?gid=1465277230#gid=1465277230) to determine test durations.

**Test type: Statistical significance test**
The test results reach 80-95% confidence and we can make a definitive decision on which variant to proceed with. We can project the annual impact of the winning variant if implemented:

| Change type | Change example | MDE* | Daily page views | Annual avg CVR | 80% Stat Sig | 95% Stat Sig |
|---|---|---|---|---|---|---|
| Minor change | A CTA button label | 10% | 3000 | 2% | 2-3 weeks | 4-5 weeks |
| Moderate change | Moving a form to a new location | 20% | 3000 | 2% | 1 week | 1-2 weeks |
| Major change | Completely new page layout | 20%+ | 3000 | 2% | <1 week | <1-2 weeks |

**Duration and confidence statement example**: *“Testing the new variant layout against the control layout on the Free Trial DevSecOps page will take 1-2 weeks to reach between 80-95% statistical significance.”*

---

**MDE (Minimum Detectable Effect) is determined by the magnitude of changes being tested. Minor refinements (button colors, copy tweaks) are 10% MDE, moderate changes (form field changes, CTA repositioning) use 20% MDE, and major redesigns (new layouts, template changes) use 20%+ MDE.*

---

**Test type: Directional test (“Do-no-harm”)**
The test runs for 2-3 weeks, and once that has completed the test will conclude. We use the results to make a directional decision on how to proceed:

| Change type | Change example | MDE* | Daily page views | Annual avg CVR | 80% Stat Sig | 95% Stat Sig |
|---|---|---|---|---|---|---|
| Minor change | A CTA button label | 10% | 600 | 2% | 3+ weeks | 3+ weeks |
| Moderate change | Moving a form to a new location | 20% | 600 | 2% | 3+ weeks | 3+ weeks |
| Major change | Completely new page layout | 20%+ | 600 | 2% | 3+ weeks | 3+ weeks |

**Duration and confidence statement example**: *"The test to change the label on the primary CTA on the Why GitLab page will run for 2-3 weeks, then we’ll make a directional decision based on the results.”*

### Step 4: Decision Framework for Results

Experiments will present a variety of result types. We use this decision model to determine our action once we have our final test results.

| Result type | Result percentage | Action |
|---|---|---|
| Statistical significance test | The variant increased conversion by 1%+. | Implement the variant. |
| Statistical significance test | The variant decreased conversion by -1%+. | Don't implement the variant. |
| Directional test | The variant increased conversion by 10%+. | Cross-reference Google Analytics data. If consistent, implement the variant. |
| Directional test | The variant increased conversion by 1-10%. | Cross-reference Google Analytics data. If consistent, implement the variant and continue monitoring results. |
| Directional test | The variant decreased conversion by -1%+. | Don't implement the variant. |

**Results decision statement example**: *“The variant in the DevSecOps Free Trial Page test increased high value trial conversion by +10%, so we will proceed with implementing the variant.”*

## How to run a test

### Step 1: Ideation

Anyone at GitLab can contribute an experiment idea.

1. [Create an issue using the "experiment" issue template](https://gitlab.com/gitlab-com/marketing/digital-experience/about-gitlab-com/-/issues/new?description_template=experiment) and complete the hypothesis section.

2. The issue will be automatically assigned to the DEx Design Manager and Marketing Analyst to complete the remaining sections and experiment setup.

   - **UX Designers**: Responsible for initial experiment setup and variation design using the visual editor.
   - **DEx Engineers**: Handle experiments requiring advanced configurations beyond the visual editor's capabilities. This may require using their [utilities](https://docs.developers.optimizely.com/web-experimentation/reference/utilities)
   - **Marketing Analysts**: Manage audience targeting, traffic allocation, roll-out strategy, and success metrics definition.

3. **Localization Considerations**: When determining if separate experiments are needed for localized paths:
   - **Text-based variants**: Consult the Localization team to verify if translated text maintains the intended message. If the meaning differs significantly, create separate experiments for localized pages.
   - **Non-text variants**: Experiment only on the default English page.

### Step 2: Prioritization

The [DEx Experimentation Roadmap Google Sheet](https://docs.google.com/spreadsheets/d/1WWL40CEV8ZIi8uBSorbGg-uZWUty8tx2/edit?gid=1692352114#gid=1692352114) contains planned experiments and priority scoring.

### Step 3: Design Experiment

1. The DEx Designer will create mockups in Figma, which require review and approval by the Design Manager.

2. The Marketing Analyst will define:

   - Audience targeting
   - Traffic allocation
   - Roll-out strategy
   - Success metrics
   - Estimated duration

### Step 4: Optimizely Configuration

#### Experiment Setup

**Naming Convention**: `[Page Path] - [Experiment Name]`

Examples:

- Home - Hero Trial CTA
- /pricing/premium/ - Anchor Links Blue vs Green
- /why-gitlab/ - Sticky CTA vs Fixed

**Description**: Include your hypothesis, design changes, and a link to the GitLab issue.

**Target By (Page)**:

1. Search for existing pages under "Saved Pages" first
2. If the page doesn't exist, click "Create New Page"
3. Use the page path as the Name (excluding the Home page)

Examples:

- Home
- /pricing/
- /sales/
- /solutions/supply-chain/

**Variation Naming Convention**:

- Control: [element name] (e.g., "Control: Get Started")
- Variant: [element name] (e.g., "Variant: Free Trial")

#### Audience Targeting

> "Targeted experiments can generate 41% higher impact on specific audiences than general experiences"

Optimizely offers multiple targeting options:

- **Standard attributes**: Device type, location, browser
- **Behavioral targeting**: Based on web browsing behaviors
- **Third-party integrations**: Google Analytics and 6Sense audiences, including Sales Segments (SMB, MM, ENT)

#### Traffic Allocation

Default to 100% unless the experiment is considered high risk; in such cases, gradually roll out to 100%.

#### Traffic Distribution

- **High-traffic pages**: Use manual 50/50 traffic split
- **Low-traffic pages**: Consider "Stats Accelerator" distribution mode, which allocates more traffic to the currently winning variant to reach statistical significance faster
- **General rule**: Traffic distribution should always be an even split

#### Metrics

**Before creating new metrics**: Verify if the event already exists to avoid duplication.

**Metric Types**:

- **Click Event Metric**: For click-based metrics
- **Page View Metric**: Based on page hits (e.g., confirmation page)
- **Custom Event Metric**: For all other events (requires Google Tag Manager integration)

**Naming Convention**: `[Metric Type] - [Page/Area Name] - [Element Name]`

Examples:

- Click - Home - Free Trial
- Custom - /sales/ - Form
- Click - Navigation Menu - Platform

### Step 5: QA and Publishing

**QA Checklist**:

- Designer: Verify desktop and mobile layouts
- Designer: Verify visual requirements are met based on mockups
- Analyst: Verify tracking for all variants
- Analyst: Confirm metrics are tracking correctly on Optimizely and Google Analytics

**Approval Process**: All experiments require approval from the Design Manager, Engineering Manager, Director of DEx, or Marketing Analyst before launching to production.

**Launch Times**: Tuesday through Thursday are often preferred for launches, avoiding Monday (when user behavior can be irregular after the weekend) and Friday (to avoid weekend monitoring issues). And early in the day (morning hours of targeted audience) gives us time to monitor for issues and make adjustments if needed.

**Note**: If an experiment needs to be edited after its published, you must create a new experiment, otherwise the data can be skewed.

### Step 6: Analysis and Next Steps

Once the experiment reaches statistical significance (ideally 95% confidence), the Marketing Analyst will provide final results and declare a winner in the issue.

**Optional**: Share results in the #digital-experience-team Slack channel.

**Next steps based on results**:

- **If the variant wins**: The Designer will:

  - Roll out the variant to 100% of traffic
  - Create a new Engineering issue to implement the winning design permanently
  - Turn off the experiment after the permanent implementation goes live

- **If the control wins or data is inconclusive**: The Designer will turn off the experiment.

### Step 7: Announcement

Once the experiment launches, announce it in the #digital-experience-team Slack channel for team visibility. The Designer will update the  issue with next steps based on results.
