---
title: "How We Work"
description: "How we work, communicate, and run things day-to-day in AI Core Infra"
---

## Backlog Refinement

Every week the engineering team completes a backlog refinement process
to review upcoming issues. The goal of this effort is for all issues to have a
weight so we can more accurately plan each milestone using the estimated
capacity for the team and the estimated issue weights.

In addition to this backlog refinement process, engineers on the team can add
weights to any issues that are straight-forward and do not need backlog
refinement.

This process happens in three steps.

### Step 1: Identifying Issues for Refinement

The engineering manager picks issues to refine each week. We aim for 5 issues in total.
If you think an issue is a good candidate, just mention it in the issue itself

We try to keep refinements themed to avoid too much context switching. Good
places to look for candidates:

* [Infradev Issues](https://gitlab.com/groups/gitlab-org/-/work_items?sort=created_date&state=opened&label_name%5B%5D=group%3A%3Aai%20core%20infra&label_name%5B%5D=infradev&first_page_size=20)
* [Issues scheduled for the next milestone without weight](https://gitlab.com/groups/gitlab-org/-/work_items?sort=created_date&state=opened&label_name%5B%5D=group%3A%3Aai%20core%20infra&weight=None&milestone_title=Upcoming&first_page_size=100)
* [Security Issues](https://gitlab.com/groups/gitlab-org/-/issues?scope=all&state=opened&label_name[]=group%3A%3Aai%20core%20infra&label_name[]=security&weight=None)
* [Missed-SLO](https://gitlab.com/groups/gitlab-org/-/work_items?sort=created_date&state=opened&label_name%5B%5D=group%3A%3Aai%20core%20infra&label_name%5B%5D=SLO%3A%3AMissed&first_page_size=100)
* [Approaching-SLO](https://gitlab.com/groups/gitlab-org/-/work_items?sort=created_date&state=opened&label_name%5B%5D=group%3A%3Aai%20core%20infra&label_name%5B%5D=SLO%3A%3ANear%20Miss&first_page_size=100)
* Bugs
  * [Rails](https://gitlab.com/groups/gitlab-org/-/work_items?sort=created_date&state=opened&label_name%5B%5D=group%3A%3Aai%20core%20infra&label_name%5B%5D=type%3A%3Abug&weight=None&first_page_size=20)
  * [AIGW/DWS](https://gitlab.com/gitlab-org/modelops/applied-ml/code-suggestions/ai-assist/-/work_items?sort=created_date&state=opened&label_name%5B%5D=group%3A%3Aai%20core%20infra&label_name%5B%5D=type%3A%3Abug&weight=None&first_page_size=20)
  * [CEF](https://gitlab.com/groups/gitlab-org/modelops/ai-model-validation-and-research/ai-evaluation/-/work_items?sort=created_date&state=opened&label_name%5B%5D=group%3A%3Aai%20core%20infra&label_name%5B%5D=type%3A%3Abug&weight=None&first_page_size=20)
* Issues without weight
  * [Rails](https://gitlab.com/groups/gitlab-org/-/work_items?sort=created_date&state=opened&label_name%5B%5D=group%3A%3Aai%20core%20infra&weight=None&first_page_size=100)
  * [AIGW/DWS](https://gitlab.com/gitlab-org/modelops/applied-ml/code-suggestions/ai-assist/-/work_items?sort=created_date&state=opened&label_name%5B%5D=group%3A%3Aai%20core%20infra&weight=None&first_page_size=100)
  * [CEF](https://gitlab.com/groups/gitlab-org/modelops/ai-model-validation-and-research/ai-evaluation/-/work_items?sort=created_date&state=opened&label_name%5B%5D=group%3A%3Aai%20core%20infra&weight=None&first_page_size=100)

Once selected, the engineering manager applies the `ai-framework::ready for next refinement` label and uses
the [Refinement Bot](https://gitlab.com/gitlab-org/ai-powered/ai-framework/refinement-bot)
to generate a refinement issue with all the candidates bundled together.

### Step 2: Refining Issues

Over the week, each engineer on the team will look at the list of issues
selected for backlog refinement. [Current backlog refinement issues](https://gitlab.com/groups/gitlab-org/-/work_items?sort=created_date&state=opened&label_name%5B%5D=ai-framework%3A%3Aready%20for%20refinement&first_page_size=100).

For each issue, each team member will review the issues and provide the
following information:

* Estimated weight.
* How to break down the issue into different issues or merge requests.

Some considerations:

* Keep the conversation on the original issues.
* During this process, the issue description and labels should be updated as
more information is gathered.
* For efficiency, engineers can also skip the refinement of some issues
depending on the feedback that we already have, provided the issue still meets our definition of ready.
* Where the fix is clear and easy, we can assign the issue to
ourselves, give it a weight of 1 and push the fix.

An issue is more likely to be scheduled for development if it meets our definition of ready.

## Weighting and Estimation Process

### Weight Guidelines

Issues are weighted using the Fibonacci sequence (0, 1, 2, 3, 5, 8, 13+):

* **Weight 0:** Smallest issues (typos, minor formatting, simple code changes without tests)
* **Weight 1:** Simple issues with minimal uncertainty (good for new contributors)
* **Weight 2:** Straightforward issues requiring multiple code/test updates
* **Weight 3:** Larger issues with some complexity but manageable scope
* **Weight 5:** Should typically be broken down; acceptable for large manual updates with low risk
* **Weight 8/13+:** Placeholder weights indicating need for breakdown; too large or uncertain for immediate implementation

### Weight Update Process

Every issue assigned to the upcoming milestone needs to be weighed before applying the Deliverable label by Engineering Manager. Engineering Manager needs to check whether weight is assigned and, in case of the weight being equal or above 5, works on breaking issues down into smaller ones.

Engineering manager and Product Manager are responsible for asking to weight issues assigned for the upcoming milestone during weekly team meetings. They should ask engineers to read issue descriptions before the meeting so they are ready to weight them and ask questions if needed. They can split this process between more than one meeting.
