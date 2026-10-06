---
title: "Visual Studio Code (VS Code)"
---

Website: <https://code.visualstudio.com/>

Best for: code editing, GitLab integration

Strengths:

- Extremely popular
- Vast number of extensions, including an [official GitLab extension](https://marketplace.visualstudio.com/items?itemName=gitlab.gitlab-workflow)
- Language server protocol (LSP) was designed for vscode

A powerful editor, suitable for all kinds of editing, with a shallow learning curve. The LSP system was
designed for vscode, so vscode has excellent support for this transformational technology.

## Setup and configuration

VS Code is free, which means there is significantly less setup required to get started than paid IDE products like [JetBrains](./jetbrains-ides) products.
There are, however, several VS Code extensions and some user/workspace settings that improve the developer experience of working on our source code, especially the GitLab monorepo.

### Extensions

#### Workflow

- The [GitLab](https://marketplace.visualstudio.com/items?itemName=gitlab.gitlab-workflow) extension mentioned above brings a lot of helpful information and functionality to VS Code for any git repo hosted in GitLab, including
  - GitLab Duo agentic chat in the editor
  - information on the most recently run pipeline for your current git branch
  - Access to your issues and MRs, including comments and workflow for MR changes
- The [GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens) extension is a convenient way to access links to specific commits or MRs in GitLab directly in your editor. Note however that in the GitLab monorepo project, this extension can degrade performance.

#### Language-specific

- The [Vue](https://marketplace.visualstudio.com/items?itemName=Vue.volar) extension is essential for syntax highlighting and IntelliSense in Vue files.
- The [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode) extension can be configured to format any file that matches our ESlint glob pattern on save, which will autofix fixable ESlint errors (for example, single/double quotes, trailing commas, spaces within double braces, etc).
- The [Ruby LSP](https://marketplace.visualstudio.com/items?itemName=Shopify.ruby-lsp) provides IntelliSense, autocomplete and Rubocop linting on save for Ruby files.
- The [Tailwind CSS IntelliSense](https://marketplace.visualstudio.com/items?itemName=bradlc.vscode-tailwindcss) extension will provide IntelliSense/autocomplete for the GitLab-specific Tailwind utility classes defined in Pajamas.

### User and workspace settings

- Due to the sheer size of the GitLab monorepo, you may find it convenient to set `"typescript.tsserver.maxTsServerMemory"` value to 8192 in your User or Workspace settings.
