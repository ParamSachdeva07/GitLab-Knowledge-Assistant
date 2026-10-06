---
title: 'Analytics dashboards'
description: 'Documentation on Zendesk analytics dashboards'
---

{{% alert title="Note" color="info" %}}

- All actions detailed on this page require at least light agent access to Zendesk analytics
- Analytics refreshes hourly which means Analytics based data is not always real time depending on query.

{{% /alert %}}

## Tips to create effective dashboards

1. Define your objectives: Clearly outline the goals and objectives of your custom dashboard. Determine the specific metrics and KPIs (Key Performance Indicators) you want to track. For example, you may want to monitor ticket volume, average resolution time, or customer satisfaction scores.
1. Identify relevant data and datasets: Determine the data sources and datasets you need to connect to your custom dashboard.
1. Select appropriate visualizations: Choose the most appropriate chart types and visualizations that effectively represent your data. Consider the nature of your metrics and the story you want to convey. Line charts, bar charts, and pie charts are commonly used, but explore other options based on your requirements.
1. Create queries: Use the Zendesk Analytics Query Builder to create queries that fetch the data for your metrics. Apply filters, groupings, and calculations to generate the desired insights. Leverage the query functionality to analyze data from different angles and create multiple queries for different metrics.
1. Design an intuitive layout: Organize your charts and visualizations in a logical and intuitive manner on the dashboard. Group related metrics together and arrange them in a way that allows for easy comparison and understanding. Consider using sections, columns, and color schemes to enhance clarity.
1. Leverage dashboard interactivity: Take advantage of interactive features to enhance user experience and exploration. Add drill-through links that allow you to navigate to more detailed reports or data. Utilize filters that enable users to dynamically modify the data displayed on the dashboard.
1. Apply contextual filters: Contextual filters allow you to refine the data displayed on your dashboard based on specific criteria, such as time frames, regions, or agent performance. This helps you focus on the relevant data and gain deeper insights.
1. Regularly review and refine: Continuously review and refine your custom dashboard based on evolving business needs and feedback. Keep track of emerging trends, identify anomalies, and adjust your metrics and visualizations accordingly. Regularly revisit your objectives to ensure alignment with your dashboard content.
1. Keep your custom dashboard focused and concise. Include only the most relevant metrics to avoid clutter and information overload.
1. Use color coding and visual cues to highlight important insights or trends. This helps users quickly identify critical information.
1. Leverage text and annotations to provide context and explanations for the metrics displayed on your dashboard. This ensures clarity and understanding for dashboard users.
1. Regularly share and collaborate on your custom dashboard with relevant stakeholders. Encourage feedback and use it to improve the dashboard’s effectiveness.
1. Consider setting up scheduled reports to automatically distribute the dashboard to stakeholders. This ensures timely access to updated insights without the need for manual sharing.

Remember, the key to creating an effective custom dashboard lies in aligning it with your business objectives, selecting relevant metrics, and presenting the data in a visually appealing and easily understandable manner. Regularly review and update your custom dashboard to ensure its continued relevance and usefulness.

## Seeing a list of reports

To see a list of dashboards, you would navigate to the [dashboard library page](https://gitlab.zendesk.com/explore/studio#/dashboards).

## Creating a dashboard

{{% alert title="Note" color="info" %}}

- This requires write access to Zendesk analytics
- Dashboards can be very complex to create and edit. See [Zendesk documentation](https://support.zendesk.com/hc/en-us/articles/4408831595418-Creating-Explore-dashboards) for more in-depth information.

{{% /alert %}}

To create a dashboard:

1. Navigate to the [dashboard library page](https://gitlab.zendesk.com/explore/studio#/dashboards)
1. Click `Create dashboard` on the top-right of the page
1. Select a starter template to use
1. Click `Select` at the bottom-right of the popup
1. Fill out all information for the dashboard (this will vary based off what you are making a report for)
1. Click the `Publish changes` link at the top-right of the page

## Editing a dashboard

{{% alert title="Note" color="info" %}}

- This requires either `Administrator` permissions or ownership of the dashboard in question
- Dashboards can be very complex to create and edit. See [Zendesk documentation](https://support.zendesk.com/hc/en-us/articles/4408831595418-Creating-Explore-dashboards) for more in-depth information.

{{% /alert %}}

To edit a dashboard:

1. Navigate to the [dashboard library page](https://gitlab.zendesk.com/explore/studio#/dashboards)
1. Locate the dashboard you wish to edit and click its name
1. Click `Edit` at the top of the page
1. Make the changes you wish to make
1. Click the down carrot to the right of `Shared` at the top-right of the page
1. Click `Publish`

## Cloning a dashboard

{{% alert title="Note" color="info" %}}

- This requires write access to Zendesk analytics

{{% /alert %}}

To clone a dashboard:

1. Navigate to the [dashboard library page](https://gitlab.zendesk.com/explore/studio#/dashboards)
1. Locate the dashboard you wish to clone and click the three vertical dots to the right of it
1. Click `Clone`
1. Enter the new name for the dashboard
1. Click the checkbox if you wish to also clone the reports (optional)
1. Click the checkbox if you wish to also clone the datasets (optional)
1. Click `Clone`

## Sharing a dashboard

To share a dashboard:

1. Navigate to the [dashboard library page](https://gitlab.zendesk.com/explore/studio#/dashboards)
1. Locate the dashboard you wish to share and click the three vertical dots to the right of it
1. Click `Share`
1. Click the checkboxes to the left of the group(s) or person(s) you wish to share it with
1. Click `Update`

## Deleting a dashboard

{{% alert title="Danger" color="danger" %}}

- This action is permanent and cannot be undone

{{% /alert %}}
{{% alert title="Note" color="info" %}}

- This requires either `Administrator` permissions or ownership of the dashboard in question

{{% /alert %}}

To delete a dashboard:

1. Navigate to the [dashboard library page](https://gitlab.zendesk.com/explore/studio#/dashboards)
1. Locate the dashboard you wish to delete and click the three vertical dots to the right of it
1. Click `Delete`
1. Click `Yes, delete` to confirm the deletion

## Common issues and troubleshooting

This is a living section that will have items added to it as needed.
