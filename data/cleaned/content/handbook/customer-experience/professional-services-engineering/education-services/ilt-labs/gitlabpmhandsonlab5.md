---
title: "GitLab Agile Portfolio Management - Hands-On Lab: Reporting & Portfolio Management"
description: "This Hands-On Guide walks you through creating and managing dashboards in GitLab."
---

> Estimated time to complete: 20 minutes

## Objectives

GitLab provides different analytics insights for instances, groups, and projects. In this lab, we will explore various dashboards one can use in your system, as well as how to create your own insights.

## Task A. Accessing Built-in Dashboards

GitLab offers several built-in dashboards at both the project and group level. Let's look at a few of them now.

1. Navigate to your project repository.

1. Click on **Analyze** in the left sidebar.

1. Explore the available dashboard options:
   - Value Stream Analytics - Shows the time it takes for code changes to move through your development lifecycle
   - CI/CD Analytics - Focuses on pipelines and jobs
   - Repository Analytics - Provides insights into repository activities like commits and merges
   - Insights - Allows for custom dashboards within your project or group.

  These are just some of the analytics available to you. More information on all of the GitLab-provided analytics can be found on our [Analyze GitLab Usage page](https://docs.gitlab.com/user/analytics/).

Now that we have some understanding on how dashboards look and function, let's create a dashboard for our project. To create a custom dashboard we will need to create our own `.gitlab/insights.yml` file, define its content, and save this configuration.

## Task B. Creating an Insights File

1. In your repository, click the **+** button, and click **New directory**.

1. Name the directory _.gitlab_, and commit on the main branch.

1. Inside the _.gitlab_ directory, click the **+** button, and click **New file**.

1. Title the file **insights.yml**.

1. Copy the content below into the file:

      ```yaml
      bugsCharts:
        title: "Insights for Awesome App"
        charts:
          - title: "Team Progress"
            description: "Tracking how many issues are being worked on by the development team over a month"
            type: bar
            query:
              data_source: issuables
              params:
                issuable_type: issue
                issuable_state: opened
                filter_labels:
                  - Dev
                group_by: month
                period_limit: 30
      ```

      This insight will help you track your work done by your team over a month.

1. Commit this change.

1. Review the resulting insight under the **Analyze > Insights** tab. If your dashboard is not displaying correctly, wait a few moments for it to refresh.

## Lab Guide Complete

You have completed this lab exercise. You can view the other [lab guides for this course](/handbook/customer-experience/professional-services-engineering/education-services/ilt-labs/gitlabpmhandson).

## Suggestions?

If you wish to make a change to this lab, please submit your changes through a Merge Request.
