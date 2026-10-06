---
title: "GitLab CI/CD - Hands-On Lab: Working with CI/CD Components"
description: "This Hands-On Guide demonstrates how to add CI/CD components to a pipeline"
---

> Estimated time to complete: 15 minutes

## Preface

As Tanuki Enterprises scaled from one project to dozens, your team discovered they were copying and pasting the same CI/CD configurations across every repository. The problems multiplied quickly:

- **Configuration Drift**: Each project has slightly different versions of the same jobs, making it impossible to maintain consistency
- **Maintenance Nightmare**: When a security update requires changing a configuration, teams must manually update dozens of .gitlab-ci.yml files
- **No Standardization**: New projects reinvent the wheel, with each developer writing their own version of common tasks
- **Knowledge Silos**: Best practices from one team don't propagate to others because there's no central way to share CI/CD patterns
- **Wasted Effort**: Developers spend hours configuring pipelines instead of focusing on application code

## Objectives

In this lab, you'll learn to create reusable CI/CD components that can be shared across projects and teams. You'll build a component catalog that allows Tanuki Enterprises to standardize their pipeline configurations, maintain them centrally, and version them just like application code.

## Task A. Creating a Component

Let's create a component to use in our GitLab project.

1. Navigate to your **My Test Group** by clicking it in the breadcrumb at the top of the page.

1. From your **My Test Group** in GitLab, click the **New project** button.

1. Click the **Create blank project** tile.

1. Name your project `Tanuki App Component`.

1. Leave all other values as their default, and click the **Create project** button and wait for GitLab to redirect you to the new project's main page.

      Now, we need to set up the configuration for the component.

1. In the repository of your Tanuki App Component project, click the **+** button, then click the **New Directory** option.

1. For the directory name, type in **templates**. Make sure that it is in lower case.

1. Click the **Commit changes** button, and commit it to the main branch.

1. Ensure you are now in the new templates directory. Click on the **+** button, then click the **New file** button.

1. Type in **sample-template.yml** as the file name.

1. In the body of the file, copy the following text to create your sample component:

      ```yaml
      spec:
        inputs:
          stage:
            default: test
      ---
      component-job:
        script: echo "The Tanuki Component is live"
        stage: $[[ inputs.stage ]]
      ```

      Here, we are creating a component with an input called *stage*. The stage input has a default value of 'test', which we will override in our other project.

1. Click **Commit changes**, and then click **Commit changes** in the pop-up screen.

      Now we have a component file, but in order for the component to be accessible by other projects, we need to publish the component. Note that since the project is private, it will only be accessible by you.

## Task B. Publishing the Component

1. On the left-hand toolbar, select **Settings > General**.

1. All components require a project description. Write in your project description section, "This component is a Tanuki App Component, and is meant for demonstration purposes only."

1. Click **Save changes** to save your description.

1. Expand **Visibility, project features, permissions**.

1. Turn on the CI/CD Catalog project toggle. Click **Save changes**.

      This will now make the project a CI/CD Catalog project. Any templates in the *templates* directory will now be available to any project, provided we make a release. Next we will use a component to make a release on our new custom component.

1. In the repository of your Tanuki App Component project, click the **+** button, then click the **New File** option.

1. Title the file `.gitlab-ci.yml`.

1. In the `.gitlab-ci.yml` file, add the following code snippet.

      ```yaml
      stages:
        - release

      release component:
        stage: release
        image: registry.gitlab.com/gitlab-org/release-cli:latest
        script:
          - echo "Releasing the latest version of our component."
        release:
          tag_name: '1.0.$CI_PIPELINE_IID'
          description: 'The latest component release.'
        rules:
          - if: $CI_COMMIT_REF_NAME == $CI_DEFAULT_BRANCH
      ```

      This code looks similar to our release job we made in a similar lab, but there is one key difference - component releases require a release format in semantic versioning (Major.Minor.Patch). We use the Patch version to differentiate between each commit.

1. Click **Commit changes**, and then click **Commit changes** in the pop-up screen.

1. Wait for the pipeline to complete.

1. To verify that the release has successfully completed, navigate to **Deploy > Releases** to see the released version of your component.

## Task C. Adding the Created Component to our Project

1. Navigate to your CI/CD Catalog by clicking on the search bar, and then clicking the **Explore** option.

1. Click on the **CI/CD Catalog** option on the left.

1. Click on the **Tanuki App Component** component. This component will be only visible to you.

1. Copy the `include` statement in the component. It should look similar to this:

      ```yaml

      include:
        - component: $CI_SERVER_FQDN/training-users/session-0a9ee9b9/iuhrhhmd/example-component/sample-template@v0.4.0

      ```

1. Navigate to your Tanuki App project by clicking on the Tanuki logo in the top left corner of the page, then click on **Projects**. Click on your Tanuki App project (the one that is not the component project).

1. Select **Build > Pipeline Editor**.

1. At the top of your file, below the image, add in the custom component we created earlier.

      The top of the `.gitlab-ci.yml` file should look like this:

      ```yaml
      workflow:
        rules:
          - if: $CI_COMMIT_TAG
            when: never
          - when: always

      default:
        image: golang

      include:
        - component: $CI_SERVER_FQDN/training-users/session-0a9ee9b9/iuhrhhmd/example-component/sample-template@v0.4.0
      ```

1. Select **Commit changes**.

1. After committing your changes, navigate to the pipeline created for your commit. You will now see a new job named *component-job*. This job is the custom job we have imported using the `include` keyword.

1. Let's try overriding the stage to instead run in the build stage by adding the following to the `.gitlab-ci.yml` file:

      ```yaml
        include:
          - component: $CI_SERVER_FQDN/training-users/session-0a9ee9b9/iu6t0rjr/example-component/sample-template@v0.36.0
            inputs:
              stage: build
      ```

1. Select **Commit changes**, and watch as your *component-job* now runs in the build stage.

## Postface

Due to you implementing CI/CD components, Tanuki Enterprises transformed their pipeline infrastructure from fragmented to standardized. Your team can now create a central component catalog where reusable pipeline configurations are published, versioned, and shared across all projects. When a security update or best practice change is needed, they now update a single component and bump the version—projects automatically receive the improvements by updating their component reference. The `inputs` feature allows your team to customize components for their specific needs while maintaining the core standardized logic, striking the perfect balance between flexibility and consistency. This approach reduced pipeline configuration time for new projects by 80%, ensured consistent security and quality standards across all repositories, and freed your team to focus on building features rather than maintaining CI/CD boilerplate.

## Lab Guide Complete

You have completed this lab exercise. You can view the other [lab guides for this course](/handbook/customer-experience/professional-services-engineering/education-services/ilt-labs/gitlabcicdhandson).

## Suggestions?

If you wish to make a change to this lab, please submit your changes through a Merge Request.
