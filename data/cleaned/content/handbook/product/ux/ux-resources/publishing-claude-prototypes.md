---
title: "Publishing Claude prototypes to GitLab Pages"
description: "How to deploy interactive Claude prototypes as live websites using GitLab Pages for sharing and usability testing."
---

GitLab team members are experimenting with Claude for prototyping and have been impressed by what it can produce. Interactive charts, sortable tables, filtering, popovers, even a simulated GitLab Duo Chat panel. But once the prototype is ready, it raises the question: how do you actually share it with someone? With Figma and Figma Make, you can generate a shareable link and send it to stakeholders. With Claude, the prototype lives inside the Claude interface with no easy way to send someone a URL.

A few of us ran into this same problem, and [GitLab Pages](https://docs.gitlab.com/user/project/pages/) turned out to be a [boring solution](/handbook/values/#boring-solutions). This guide walks through how to deploy a Claude prototype as a live website that anyone can access.

## Why GitLab Pages

Claude generates fully interactive components, but they live inside the Claude interface as an [artifact](https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them) and can't be shared directly. Even prototypes built with Claude Code need somewhere to be hosted. GitLab Pages lets you host static websites from a GitLab repository, and since a Claude prototype is just HTML, CSS, and JavaScript, it deploys without needing a backend or database.

It also means you're [dogfooding](/handbook/product/product-processes/dogfooding-for-r-d/) GitLab's own tools, and keeping prototypes in GitLab makes it easier for the whole team to collaborate, fork, and iterate on each other's work.

Once it's live, you can share the prototype with anyone through a link, use it for unmoderated usability testing without scheduling calls, keep every iteration version-controlled in Git, and update the site just by committing a change. Updates are usually live within two minutes.

## Starter template

If you'd rather skip the manual setup, there's a ready-made template you can fork:

**[gitlab.com/diegocapetown/claude-pages-template](https://gitlab.com/diegocapetown/claude-pages-template)**

Fork it, replace the contents of `src/main.jsx` with your Claude-generated code, commit, and your prototype will be live within minutes. The `.gitlab-ci.yml` is already configured.

> **Note:** This template is set up for React-based prototypes, which is what Claude generates by default. If your prototype uses a different structure, follow the manual setup steps below instead.

The step-by-step guide below explains how everything works if you'd prefer to understand what's happening under the hood.

## Step-by-step setup

### Before you begin

These steps assume that you have already built your prototype in Claude.

### Create your GitLab project

You will need a project per prototype. You can manage multiple prototypes under one project but that is out of scope for this tutorial.

1. Create a new **blank project** on GitLab.com under your personal namespace.
   1. Set the visibility to **Public** if you want anyone to access the site without logging in.

### Add your prototype file

This step copies the Claude prototype to a file in GitLab

1. Click **New file** to add a new file to the repository
1. Name the file `index.html`
1. Insert the code of the prototype into file contents
    1. Go to your Claude prototype
    1. Click **Copy code** button
    1. Go to the file editor in GitLab and paste the code
    1. Click **Commit changes** to save the file

### Add the CI/CD configuration

This step will ensure that your file will be deployed to GitLab Pages.

1. Create a `.gitlab-ci.yml` file at the root of the project:

```yaml
pages:
  stage: deploy
  script:
    - echo "Deploying to GitLab Pages"
    - mkdir public                      # GitLab Pages deploys files under the /public folder
    - cp index.html public/             # copies the prototype file to the public folder
  artifacts:
    paths:
      - public
  rules:
    - if: $CI_COMMIT_BRANCH == "main"
```

### Deploy

1. Commit both files. The pipeline runs automatically and your site will be live within a couple of minutes at `https://<your-username>.gitlab.io/<project-name>`.
2. Go to **Settings → General → Pages** and set access to **Everyone**. "Everyone With Access" sounds like it means _everyone_, but on GitLab.com it actually means _everyone with a GitLab account_. For fully public access with no login required, you need the explicit Everyone setting. See [GitLab Pages access control](https://docs.gitlab.com/user/project/pages/getting_started/pages_ui/) for more details. This is the step that's easy to miss.

## Tips

**Test at full browser width.** Claude artifacts render in a constrained iframe. When your prototype goes live on Pages at full width, the layout may behave differently. Worth checking both sizes.

**Updating is fast.** Edit the file in GitLab, commit, and the pipeline redeploys automatically. Usually live within two minutes.

**Forking existing prototypes.** If a colleague has built a prototype that works for your use case, you can fork their project and adapt it rather than starting from scratch.

## Examples from the Product Design team

- **Group CI/CD Analytics Dashboard** - [Repository](https://gitlab.com/diegocapetown/group-ci-cd-analytics-dashboard-prototype) / [Live site](https://diegocapetown.gitlab.io/group-ci-cd-analytics-dashboard-prototype)
- **Nav Gem** - [Repository](https://gitlab.com/gitlab-org/foundations/nav-gem) / [Live site](https://nav-gem-a6866e.gitlab.io/#/onboarding)
- **Component Health** - [Repository](https://gitlab.com/jeldergl/component-health) / [Live site](https://jeldergl.gitlab.io/component-health/#/)
- **Accessibility Cache** - [Repository](https://gitlab.com/jeldergl/accessibility-cache) / [Live site](https://jeldergl.gitlab.io/accessibility-cache/)
- **Claude Test Prototype** - [Live site](https://claude-test-prototype-77c38b.gitlab.io/)

If you've published a prototype to GitLab Pages, feel free to add it to this list by submitting an MR.

## Related resources

- [Sharing files and prototypes (Figma)](https://design.gitlab.com/get-started/uik-sharing/) - for sharing Figma-based prototypes
- [GitLab Pages documentation](https://docs.gitlab.com/ee/user/project/pages/) - full documentation on GitLab Pages
- [AI usage](/handbook/upstream-studios/how-we-work/ai-usage/) - guidelines for using AI tools in the UX department
