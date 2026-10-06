---
title: "Contributor Stats Banner"
description: "Contributor Stats Banner"
---

Add a dynamic stats banner to your GitLab profile README, personal website, or anywhere else you can embed an SVG.
See the below example:

[![Lee's Contributor Stats](https://contributors.gitlab.com/users/leetickett-gitlab/banner.svg)](https://contributors.gitlab.com/users/leetickett-gitlab)

## How to use

Add the following line to your README or any markdown file, replacing `USERNAME` with your GitLab username:

```markdown
[![GitLab Contributor Stats](https://contributors.gitlab.com/users/USERNAME/banner.svg)](https://contributors.gitlab.com/users/USERNAME)
```

For example, if your GitLab username is `awesome-tanuki`, you would use:

```markdown
[![GitLab Contributor Stats](https://contributors.gitlab.com/users/awesome-tanuki/banner.svg)](https://contributors.gitlab.com/users/awesome-tanuki)
```

If you haven't set up a profile README yet, follow these docs to learn [how to add a README to your GitLab profile](https://docs.gitlab.com/user/profile/#add-details-to-your-profile-with-a-readme).

## How it works

The banner dynamically displays your contributor stats from the [GitLab Contributor Platform](https://contributors.gitlab.com).
Your stats update automatically each time the banner is loaded.

### Contributor levels

The banner displays your current contributor level, which corresponds to your level on the Contributor Platform.

Learn more about [how levels and points are calculated](https://contributors.gitlab.com/docs/user-guide) on the Contributor Platform.

## Who can use this

- **Community members**: Your banner will display your contributor level and stats based on your activity on the Contributor Platform.
- **GitLab team members**: You can also use the banner! Your banner will display your stats and indicate that you're a team member rather than show a level.
