---
title: Product Category Field
description: "How to use the Product Category field and ZenDuo prompt to categorize support tickets"
category: Closing tickets
---

## Overview

This document provides information about the custom Zendesk field "Product Category", and how to populate it.  This is an expected part of the Closing phase of ticket handling.

## What is the Product Category field?

The Product Category field is a multi-select field in Zendesk that helps us identify which GitLab product areas are at the heart of each support ticket. This field is required to be populated before setting any ticket to **Solved**. This data is highly beneficial for providing customer insights to our product and development teams.

The data collected through this field enables:

- Analytics on which GitLab features generate the most support volume
- Trend identification for product team feedback
- Improved knowledge management and documentation prioritization

The options in the field have been populated from the [categories.yaml](https://gitlab.com/gitlab-com/www-gitlab-com/blob/master/data/categories.yml) file for actively developed categories, along with `maintained` categories listed in the [stages.yaml](https://gitlab.com/gitlab-com/www-gitlab-com/blob/master/data/stages.yml) file.

## Using the Product Category field

### When to populate the field

The Product Category field needs to be populated as part of the ticket closure process, though it can be updated at any time prior to the ticket closing. Setting the ticket to "Solved" will often be the most appropriate time to set this, as we tend to gain information during the course of solving a ticket that helps us better understand what was the primary cause of the problem the customer experienced.

### How to populate the field

You can populate the Product Category field in two ways:

1. **Manual selection**: If you clearly know which category applies to the ticket, select the appropriate options directly from the multi-select field. More than one category can apply to a single ticket.

2. **Glean agent assistance**: Use the "Zendesk Product Category" [agent](#using-the-glean-zendesk-product-category-agent) to help identify the most relevant categories based on the ticket content.

3. **Engineering Directory tool assistance**: If you know the feature/s the ticket is related to, you can use the [Engineering Directory](https://gitlab-com.gitlab.io/support/toolbox/engineering-directory/) to identify which category that feature belongs to.

## Using the Glean "Zendesk Product Category" agent

### What is the Glean Product Category agent?

The Glean "Zendesk Product Category" agent is a specialized prompt designed to analyze ticket content and suggest appropriate Product Category selections. This prompt was developed through extensive iteration to provide consistent and helpful categorization suggestions. As an LLM tool, it won't always get it right, but generally it gets us close enough to be helpful. You can see the full details of the agent by going to Glean, choosing `Agents` from the left menu bar, search for `Zendesk Product Category` and then click `View agent setup` in the popup box for the agent.

### How to use the Glean agent

To use the Product Category agent:

1. Navigate to the ticket you want to categorize
2. Open the Glean app from Zendesk
3. Select the "Zendesk Product Category" from the home screen of the app
4. Click on `Run agent`
5. Use the suggestions to populate the Product Category field. (This is a manual step for now.)

The suggestions are expected to be reported in the following format, where the %age is an indicator of confidence in the category being relevant to the cause of the ticket.  It will not return any suggestions that are below 76% confidence.

```markdown
Pipeline Composition | 92% | Pipeline failed during merge request
Compliance Management | 78% | Branch protection rules not enforced
```

### Expected behavior and limitations

- The agent analyzes the entire ticket conversation to identify relevant product areas
- Results are generally consistent, but may occasionally provide unhelpful suggestions
- Manual review of suggestions is always recommended before field completion
- The agent is generally good at only suggesting valid items - however the process to update the available options in the field is currently manual, and sometimes lags behind product changes. Please ping `Jane G` in Slack if you are experiencing this.

### When the agent doesn't work well

If you find the agent consistently providing unhelpful results for certain types of tickets, please provide feedback through the [feedback issue](https://gitlab.com/gitlab-com/support/support-team-meta/-/issues/7020). This helps improve the agent's effectiveness over time.

## Troubleshooting

### Common issues

- **Glean suggests irrelevant categories**: Manual review and selection is always recommended. Use your judgment to select the most appropriate categories. Provide feedback in the feedback issue as the prompt may need tweaking. You can also use the Chat feature (`Ask anything`) in the Glean app and add a follow up prompt of "those categories are not in the filtered-categories.yml file"

### Getting help

If you encounter issues with the Product Category field or Glean agent:

- Provide feedback ([feedback issue](https://gitlab.com/gitlab-com/support/support-team-meta/-/issues/7020)) on prompt effectiveness to help improve future iterations

### References

- [Roadmap issue](https://gitlab.com/gitlab-com/support/support-team-meta/-/issues/6859) where this was introduced
