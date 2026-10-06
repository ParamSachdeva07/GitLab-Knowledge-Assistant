---
title: "GitLab Compliance - Hands-On Lab: Compliance Reports"
description: "This Hands-On Guide walks you through viewing various compliance reports in your project."
---

> Estimated time to complete: 15 minutes

## Objectives

This lab will outline how to access the various compliance reports, including audit reports and SBOM reports.

## Task A. Viewing Compliance Reports and Permissions

1. Navigate to your project.

1. In the left sidebar, select **Secure > Compliance center**.

1. Review the contents of the report.

1. To view user permissions, navigate to **Manage > Members**.

1. Review the different users and roles in this section. Note that your user is the owner of the project, allowing you to view all details of all reports.

1. In the top right, you will see different options for adding users to your project. Explore each option and the different roles available in each option.

## Task B. Viewing an SBOM Report

As a part of our compliance labs, we have been running a dependency scanner. This scanner produces an SBOM report when it runs. To view the SBOM report:

1. In the left sidebar, select **Build > Pipelines**.

1. Select the most recently passed pipeline.

1. Select the `dependency-scanning` job.

1. In the right sidebar, select **Browse** under **Job artifacts**.

1. Review the reports shown here. You can download these reports to view them in more detail.

## Lab Guide Complete

You have completed this lab exercise. You can view the other [lab guides for this course](/handbook/customer-experience/professional-services-engineering/education-services/ilt-labs/gitlabcompliancehandson).

## Suggestions?

If you wish to make a change to this lab, please submit your changes through a Merge Request.
