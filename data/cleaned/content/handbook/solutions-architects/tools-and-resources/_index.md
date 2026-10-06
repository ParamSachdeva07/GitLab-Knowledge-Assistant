---
title: Tools and Resources
description: "Reference index of tools, platforms, and resources used by Solutions Architects"
---

## Tools and Resources

This page is a grouped reference index of tools, platforms, and resources used by Solutions Architects. For end-to-end engagement guides, see [SA Engagement Playbooks](/handbook/solutions-architects/playbooks/). For mandatory process steps, see [SA Processes](/handbook/solutions-architects/processes/).

### Demo and Presentation Tools

GitLab Solutions Architects conduct hands-on workshops as interactive events for GitLab prospects and customers to learn the GitLab product and DevSecOps capabilities. Workshops may be executed as marketing events or run independently for specific customers. Detail information is provided on the [Hands-on Workshops](/handbook/solutions-architects/tools-and-resources/workshop/) page.

### Customer Engagement and Recording

When Support is required during the pre-sales cycle, for example during a POV exercise or while pursuing a potential new deal with a customer, Solutions Architects should first log in to Zendesk. Next, they should use the [Zendesk Internal Request Form](https://gitlab-internal.zendesk.com/hc/en-us/requests/new?ticket_form_id=22783651259548) and select "Request assistance from support" under "What is this request concerning?".

For all other situations with existing customers, Solutions Architects should advise the customer to open a support ticket themselves.

If a ticket later becomes a priority, the assigned Support Engineer can escalate it to the responsible backend engineering team through a [GitLab Request for Help](https://gitlab.com/gitlab-com/request-for-help/) (RFH) issue. In exceptional circumstances such as a blocker that could prevent closing business, Solutions Architects may raise an RFH issue directly. If doing so, please ensure you carefully follow the documented process in the [RFH README](https://gitlab.com/gitlab-com/request-for-help/-/blob/main/README.md) and, when closing the issue, apply the correct [closure label](https://gitlab.com/gitlab-com/request-for-help/-/blob/main/README.md#applying-the-correct-closure-labels) to align with reporting requirements.

### Data Seeding and Demo Environments

When SAs discover bugs or customer-blocking issues during DAP trials, POVs, or customer deployments, use the [DAP Rapid field reporting process](/handbook/solutions-architects/tools-and-resources/dap-issue-reporting/) to route them to engineering with appropriate severity and tracking labels. SAs can file bugs directly — no Zendesk ticket required.

### SaaS Trials for Existing Customers

Paid customers must set up a new namespace on SaaS when trialing Ultimate.  There are two primary reasons for this:

1. Some paid features are not available in a trial, so a customer might lose functionality they had been using if a trial license is applied
2. GitLab does not have an appropriate mechanism for applying and reverting a trial license on SaaS without the namespace potentially being reverted to free when the trial expires ([see issue](https://gitlab.com/gitlab-org/gitlab/-/issues/12186))

Both situations put customer production GitLab usage at risk if a trial is applied to the SaaS namespace.

Instead, a customer should create a new namespace and trial there.  We have put together some [trial guidelines](/handbook/solutions-architects/tools-and-resources/trial-guidelines/) in order to make the process as seamless as possible for customers.

### Learning Platforms

As a Solutions Architect, it is important to be continuously learning more about our product and related industry topics. The [education and enablement handbook page](/handbook/customer-experience/education-enablement/) provides a dashboard of aggregated resources that we encourage you to use to get up to speed.

### Product Releases

Solutions Architects have to keep up the pace of the GitLab monthly product releases to position feature sets and capabilities for the prospect and customer needs while demonstrating the market leading position.

Following links provide product release information to assist in technical discussions and technical evaluation.

- [Upcoming Releases](https://about.gitlab.com/upcoming-releases/)
- [Previous Releases](https://gitlab.com/gitlab-org/gitlab/-/releases)
- [Releases Blog](https://about.gitlab.com/releases/categories/releases/)
- Compare two releases with the [What is New Since? Release Feature Overview Tool](https://gitlab-com.gitlab.io/cs-tools/gitlab-cs-tools/what-is-new-since/?)

### Customer Facing Meeting Tools

Solutions Architects frequently interact with customers for demos, presentations or Q&A. These calls should enable the customer to clearly experience the value of GitLab without distraction or interruption. The below list of tools was compiled by the GitLab SA team as commonly used solutions. Note, this list does not represent a requirement to use any of these products or an endorsement for these products.

- [Muzzle](https://muzzleapp.com/) to mute all notifications prior to beginning a call
- [Tab Resize Chrome plugin](https://chrome.google.com/webstore/detail/tab-resize-split-screen-l/bkpenclhmiealbebdopglffmfdiilejc?hl=en-US) to break tabs into split-screen viewing
- [Screenbrush](https://screenbrush.imagestudiopro.com/) to draw on the screen
- [Toby](https://www.gettoby.com/) or [Tabs Outliner](https://chrome.google.com/webstore/detail/tabs-outliner/eggkanocgddhmamlbiijnphhppkpkmkl) to launch many preset tabs at once
- [Station](https://getstation.com/) to group pages by application in a smart dock
- [MouseBeam](https://geeky.gent/tag/mousebeam/) enables the mouse cursor to use multiple screens like a circle
- [Rectangle](https://rectangleapp.com/) to quickly move and resize windows in macOS using keyboard shortcuts or snap areas
- [Dark Reader](https://darkreader.org/) enables browser dark mode to better fit room lighting
- [Postman](https://www.postman.com/) for API interaction
- [VSCodium](https://vscodium.com/) open-source IDE preferred by some SAs for demos and development
- [Visual Studio Code](https://code.visualstudio.com/) lightweight IDE text editor

#### Related macOS tips

- [Switch between full screen applications](https://www.intego.com/mac-security-blog/how-to-enter-and-exit-full-screen-mode-in-macos/) using the trackpad, Command keys or other options
- Use the [Zoom Accessibility Features](https://www.imore.com/how-use-zoom-mac) to zoom in on targeted screen locations
- [Work in multiple spaces on a single monitor](https://support.apple.com/en-gb/guide/mac-help/mh14112/mac) to keep multiple app windows or browser tabs open in fullscreen mode
  - Enables switching between windows or tabs with trackpad gestures, keeping display screen clean and uncluttered

### Useful Customer Facing Presentations

No two presentations are the same and we often find ourselves mixing and matching content tailored to our Customer's journey. All field and customer facing collateral is hosted on

- [HighSpot](https://gitlab.highspot.com/) (for field teams)
- [Solution Pages](https://about.gitlab.com/solutions/) (for web users)

### O'Reilly Learning Platform

More information can be found on the [Customer Success Education & Enablement page](/handbook/customer-experience/education-enablement/).

### LinkedIn Learning Platform

LinkedIn Learning is another platform with various resources to help SA's during their onboarding journeys.

### Getting started as an associate SA

Here are courses that will facilitate the onboarding process of associate SAs and help them in getting up to speed with the technical concepts required for the role:

**Free for GitLab members**

- The learning path [Become a DevOps Engineer](https://www.linkedin.com/learning/paths/getting-started-with-devops), particularly the following sections:
  - [DevOps Foundations](https://www.linkedin.com/learning/devops-foundations-23454205)
  - [Learning Docker](https://www.linkedin.com/learning/learning-docker-17236240)
  - [DevOps Foundations - CI/CD](https://www.linkedin.com/learning/devops-foundations-continuous-delivery-continuous-integration-14449917)

- [Docker for the Absolute Beginner - Hands-On](https://learning.oreilly.com/videos/docker-for-the/9781788991315/)

**Paid**
Paid courses can be expensed as part of the [Growth and Development benefits](/handbook/people-group/learning-and-development/growth-and-development/)

- IBM course on Coursera: [Information Technology (IT) and Cloud Fundamentals Specialization](https://www.coursera.org/specializations/it-cloud-fundamentals)
Especially the module [Introduction to Cloud Computing](https://www.coursera.org/learn/introduction-to-cloud?specialization=it-cloud-fundamentals)

### Data Seeding (Demo Data)

The [GitLab Data Seeder](https://docs.gitlab.com/ee/development/data_seeder.html) is a tool that Solutions Architects can use to showcase to customers "what good data looks like" in GitLab.
The data that is generated is customizable, time-relative, and can be used on-demand to generate data to demonstrate.

The Demo Data can be showcased on any self-managed instance including Docker, GDK, and customer environments.

### Diagramming Tools

Being able to diagram as-is and to-be workflows and architectures is a key tactic for Solutions Architects to communicate key benefits of a GitLab DevSecOps transformation.  GitLab has made FigJam available for SAs to use and we have [Solutions Architecture Workspace](https://www.figma.com/files/972612628770206748/workspace/1338898741676176280/directory/teams?fuid=1339310988336517144) available for storing our diagrams.
