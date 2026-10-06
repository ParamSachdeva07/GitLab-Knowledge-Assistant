---
description: "Development environments, IDEs, and AI workflows for Developer Advocacy demos and technical work."
linkTitle: "Development environments"
title: Development Environments for Developer Advocates
---

Developer Advocates work with different types of platforms, editors and IDEs, including AI-native workflows using the GitLab Duo Agent Platform. This page compiles best practices and useful tips to help optimize developer advocacy-related setups.

## Resources

Start in the [GitLab Duo Agent Platformdocumentation](https://docs.gitlab.com/user/duo_agent_platform/) and read on for [IDEs](#ides), [CLI](#cli) and [extensibility and customization](#extensibility-and-customization) with MCP, custom rules, etc.

For architecture insights, review the [architecture design document](/handbook/engineering/architecture/design-documents/duo_workflow/).

The [GitLab Duo Agent Platform launch support issue - DevRel (internal)](https://gitlab.com/gitlab-com/marketing/developer-relations/developer-advocacy/developer-advocacy-meta/-/issues/878) collects product/engineering updates, GTM and content strategies, and use case development.

## IDEs

Developer Advocates can use different IDEs depending on their projects and content requirements. It is key to understand the IDE capabilities and use cases, put them into focus for content requests, and diversify usage for different audiences.

### AI and GitLab Duo in IDEs

GitLab Duo and the GitLab Duo Agent Platform are integrated as [IDE extensions/plugins](https://docs.gitlab.com/editor_extensions/#available-extensions).

### Visual Studio Code

Visual Studio Code (short: VS Code) supports a variety of programming languages and development tool integrations through its marketplace.

GitLab Duo can be integrated through the [GitLab Workflow extension in the VS Code marketplace](https://docs.gitlab.com/editor_extensions/visual_studio_code/).

> **Note**
>
> Review the [internal guide for Dev Environments](https://internal.gitlab.com/handbook/marketing/developer-relations/developer-advocacy/dev-environments/) after completing the initial setup.

![VS Code, light theme, with Duo Agentic Chat in the right panel. Editor shows diff view after agentic edits.](/images/handbook/marketing/product-and-technical-marketing/developer-advocacy/dev-environments/vscode_light_theme_dap_agentic_chat_right_pane_diff_view.png)

#### Tips and best practices for VS Code

1. Learn and practice frequently used [keyboard shortcuts for VS Code](https://code.visualstudio.com/docs/configure/keybindings).
    - Command palette: `cmd shift p` on macOS or `ctrl shift p` on Windows/Linux.
    - Settings: `cmd ,` on macOS or `ctrl ,` on Windows/Linux.
    - Tip: You can also ask [GitLab Duo Chat](https://docs.gitlab.com/user/gitlab_duo_chat/examples/), or [Claude](/handbook/tools-and-tips/ai/claude/) for help.
1. Open local Git repositories or directories using the `code .` shortcut from the terminal. This simplifies the workflow of editing/debugging code when you need to switch contexts between GitLab UI, VS Code and terminal.
1. Open a terminal in VS Code (shortcut: `cmd j` on macOS, or `cmd shift p` and search for `terminal`). This allows starting background tasks like running servers, compilers, Ansible playbooks, etc. while editing code and avoids context switching between different windows.

#### Recommended settings and extensions

1. Enable auto-save while editing. This avoids data loss or missing Git commit data when writing your code.
   - UI: Open the settings by clicking the gear icon in the bottom left corner (shortcut: `cmd ,` on macOS). Search for `auto save`.
   - VS Code `settings.json`: Add a new key/value for `"files.autoSave": "afterDelay"`.
1. Enable word-wrap by default. This makes long lines readable without horizontal scrolling.
   - UI: Open the settings by clicking the gear icon in the bottom left corner (shortcut: `cmd ,` on macOS). Search for `word wrap`.
   - VS Code `settings.json`: Add a new key/value for `"editor.wordWrap": "on"`.
1. Install extensions you need regularly, and only use trusted sources.
   - Review the maintained extension inventory in [@dnsmichi's dotfiles project](https://gitlab.com/dnsmichi/dotfiles/-/blob/main/vscode/extensions.txt?ref_type=heads).
   - You can install extensions on the CLI with `code --install-extension`. Example `code --install-extension gitlab.gitlab-workflow`.
   - The [vscode-extensions-install.sh](https://gitlab.com/dnsmichi/dotfiles/-/blob/main/vscode-extensions-install.sh?ref_type=heads) script installs all extensions from the inventory. Use `--discover` to list manually installed extensions, and `--update-inventory` to update the inventory file from them.

#### Demo settings: Profiles and themes in VS Code

The light theme works better on in-person event projectors, and can help with [demo recordings](/handbook/marketing/product-and-technical-marketing/developer-advocacy/content/#content-creation-guidelines), too.

Let VS Code follow the macOS appearance setting, and switch between light and dark mode for demos in one place:

```json
{
    "window.autoDetectColorScheme": true,
    "workbench.preferredDarkColorTheme": "Dark Modern",
    "workbench.preferredLightColorTheme": "Light Modern"
}
```

Review the [VS Code documentation on auto-detecting the color theme](https://code.visualstudio.com/docs/configure/themes#_automatically-switch-based-on-os-color-scheme) for more details. [@dnsmichi's dotfiles project](https://gitlab.com/dnsmichi/dotfiles#whats-inside) uses the same approach for Ghostty, Starship and neovim: Switching the macOS appearance switches all tools at once.

Alternatively, create multiple profiles to manage different themes, and extensions installed, for example `Default` and `Light theme for demos`.

For required demo recording settings, review the [video guidelines handbook](/handbook/marketing/product-and-technical-marketing/developer-advocacy/content/#content-creation-guidelines).

##### Move Chat to the right panel

By default, the Chat panel is on the left side of the VS Code UI. This might interfere with file trees in the explorer and Git commits, which are also located on the left.

In order to move the Chat to the right sidebar:

1. Open the Secondary Side bar with the icon on upper right corner.
1. Drag the Chat icon (for example, Duo Chat) and drop it to the right sidebar.
1. You can use multiple chat panels in parallel.

@dnsmichi uses this setup by default.

##### GitLab Duo Code Suggestions

Support for Code Suggestions in all languages is rolling out across IDEs. Follow [Support "all" programming languages across Duo Agent Platform](https://gitlab.com/gitlab-org/gitlab/-/work_items/571515) for the current status. VS Code no longer needs the `gitlab.duoCodeSuggestions.additionalLanguages` setting.

It is important for Code Suggestions to have proper context: Open more tabs that are relevant to your current task, as those will be used for [context](https://docs.gitlab.com/user/project/repository/code_suggestions/context/).

A full VS Code `settings.json` example is located in [@dnsmichi's dotfiles project](https://gitlab.com/dnsmichi/dotfiles/-/blob/main/.config/vscode/settings.json?ref_type=heads).

#### Debug VS Code extensions and GitLab Duo Agent Platform

An example use case: GitLab Duo Agentic Chat provides an MCP integration, and we want to verify that the MCP server is started and consumes the additional AI Context.

Need-to-know: The [GitLab Language Server](https://docs.gitlab.com/editor_extensions/language_server/) powers the backend across IDE extensions for GitLab, and handles the MCP integration for GitLab Duo Agentic Chat.

1. You can debug extensions using the `Output` view in VS Code.
1. Steps to debug:
   - Open the command palette with `cmd shift p` (macOS) and search for `View: toggle Output`.
   - Select `GitLab Language Server` in the `Output` view dropdown (next to `Filter`).
   - This view streams the extension log on the terminal. Trigger a UI action with GitLab Duo, and observe if the client sends the correct data.
1. You can use the `Filter` form to search/filter the output, for example `mcp` to isolate entries related to the MCP integration.
1. Optional: Increase the log verbosity to `debug`:
   - Open the settings by clicking the gear icon in the bottom left corner (shortcut: `cmd ,` on macOS). Search for `GitLab` or `gitlab` in the settings tree.
   - Tick the `GitLab: Debug` checkbox and restart VS Code.

### JetBrains IDEs

Developer Advocates can access [JetBrains IDEs](/handbook/tools-and-tips/editors-and-ides/jetbrains-ides/) for different purposes and use cases:

- IntelliJ IDEA Ultimate (Java, Kotlin, Scala)
- PyCharm (Python, Django)
- GoLand (Go)
- DataGrip (SQL, Databases)
- RubyMine (Ruby, Rails)
- PhpStorm (PHP)
- WebStorm (JavaScript, TypeScript, HTML/CSS)
- Rider (C#, .NET)
- CLion (C, C++)
- Android Studio (Android development)

IntelliJ IDEA also supports plugins for other languages, the availability depends on the subscription tier (Ultimate vs Community).

GitLab Duo can be integrated using the [GitLab Duo plugin in the JetBrains marketplace](https://docs.gitlab.com/editor_extensions/jetbrains_ide/).

> **Note**
>
> Review the [internal guide for Dev Environments](https://internal.gitlab.com/handbook/marketing/developer-relations/developer-advocacy/dev-environments/) after completing the initial setup.

![JetBrains IntelliJ IDEA with Duo Agentic Chat, modernizing Java 8 to 21, editor shows diff view from agentic edits.](/images/handbook/marketing/product-and-technical-marketing/developer-advocacy/dev-environments/jetbrains_intellij_idea_light_theme_dap_java_modernize_agentic_edits.png)

#### Tips and best practices for JetBrains IDEs

1. Review the [available IDE licenses](/handbook/tools-and-tips/editors-and-ides/jetbrains-ides/licenses/), and eventually create an Access Request for additional permanent IDE licenses.
1. Read the [setup and configuration guide](/handbook/tools-and-tips/editors-and-ides/jetbrains-ides/setup-and-config/) and install the [JetBrains Toolbox](https://www.jetbrains.com/toolbox-app/) to manage individual IDEs and their updates.
   - Optional tip: By default, the toolbox keeps older installed versions. If this behavior causes problems with storage consumption, disable the setting in `Tools > Keep previous versions to enable instant rollback`.
   - JetBrains IDEs can migrate/import configuration from existing setups. This is convenient to install/configure the GitLab Duo plugin once, and import it into another JetBrains IDE.

#### Demo settings: Appearance in JetBrains IDEs

The default profile in JetBrains IDEs uses a dark theme. In order to switch to a light theme, navigate into `Settings > Appearance & Behavior > Appearance` and select `Light with Light Header`.

The `Zoom` dropdown can be changed to 125% for increased details in talk live demos.

For required demo recording settings, review the [video guidelines handbook](/handbook/marketing/product-and-technical-marketing/developer-advocacy/content/#content-creation-guidelines).

### MS Visual Studio

> Note: Needs access to a Windows and Visual Studio license, and requires additional security review.
>
> Status: Research. Todos are tracked in [this internal issue](https://gitlab.com/gitlab-com/marketing/developer-relations/developer-advocacy/developer-advocacy-meta/-/issues/712).

GitLab Duo can be integrated using the [GitLab extension in the Visual Studio marketplace](https://docs.gitlab.com/editor_extensions/visual_studio/).

> **Note**
>
> Review the [internal guide for Dev Environments](https://internal.gitlab.com/handbook/marketing/developer-relations/developer-advocacy/dev-environments/) after completing the initial setup.

### Eclipse

GitLab Duo can be integrated using the [GitLab extension in the Eclipse marketplace](https://docs.gitlab.com/editor_extensions/eclipse/).

### neovim

> Tip: Start a new neovim configuration with [LazyVim](https://www.lazyvim.org/) to get a pre-configured setup with sensible defaults, and customize it with plugins. A production example is located in [@dnsmichi's dotfiles project](https://gitlab.com/dnsmichi/dotfiles/-/tree/main/.config/nvim?ref_type=heads).

GitLab Duo can be integrated using a [neovim plugin](https://docs.gitlab.com/editor_extensions/neovim/).

## CLI

### GitLab Duo CLI

The GitLab Duo CLI provides access to [GitLab Duo Agent Platform](https://docs.gitlab.com/user/duo_agent_platform/) on the terminal.

Follow the [GitLab Duo CLI documentation](https://docs.gitlab.com/user/gitlab_duo_cli/) for installation and configuration.

Tip: Add a shell alias to start the Duo CLI with `duo`, for example in your `~/.zshrc`. A production example is located in [@dnsmichi's dotfiles project](https://gitlab.com/dnsmichi/dotfiles/-/blob/main/.config/zsh/aliases.zsh?ref_type=heads).

```shell
alias duo='glab duo cli'
```

Usage examples:

```markdown
Which tools are available?

What is this repository about

Which issues need my attention

Help me implement issue 15

The pipelines in MR 23 fail. Please fix them.
```

The CLI uses the [GitLab LSP](https://gitlab.com/gitlab-org/editor-extensions/gitlab-lsp) to communicate with the AIGW and DAP services, and therefore the CLI is developed inside `gitlab-lsp`.

Follow the [product epic](https://gitlab.com/groups/gitlab-org/-/epics/19070) for functionality and roadmap updates, and add feedback into the [Duo CLI Feedback & Dogfooding epic](https://gitlab.com/groups/gitlab-org/-/epics/19806).

### Claude Code

Getting access to Claude Code is helpful for content creation, for example, in this blog tutorial: [Claude Code and GitLab: Three workflows that ship](https://about.gitlab.com/blog/claude-code-and-gitlab/).

1. Review the [AI tool requirements](https://internal.gitlab.com/handbook/ai-security-at-gitlab/ai-tool-usage-requirements/). Claude Code requires access to the GitLab Claude Enterprise subscription, see the [Claude handbook page](/handbook/tools-and-tips/ai/claude/#access).
1. Install [Claude Code](https://code.claude.com/docs/en/quickstart#step-1-install-claude-code).
1. Run `claude` and select the login method `Claude account with subscription`. Follow the login flow in the browser, and log in with your team member email address using SSO.

```shell
claude
```

Navigate into a project and prompt Claude Code with `What is this project about?`.

Tip: Add the [GitLab MCP Server into Claude Code](https://docs.gitlab.com/user/gitlab_duo/model_context_protocol/mcp_server/#connect-claude-code-to-the-gitlab-mcp-server) for better context.

### Codex

Getting access to Codex is helpful for content creation, for example, in this blog tutorial: [Codex and GitLab: From code fix to production](https://about.gitlab.com/blog/fix-bugs-with-codex-and-gitlab/)

1. Review the [AI tool requirements](https://internal.gitlab.com/handbook/ai-security-at-gitlab/ai-tool-usage-requirements/) and create an [Access Request](/handbook/eta/corporate-it/end-user-services/access-requests/) for an OpenAI key, [example (internal)](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/work_items/43999).
1. Navigate into the OpenAI platform. Select the `GitLab` organization and the `Default project` and generate an [API key](https://platform.openai.com/api-keys)
1. Install the [Codex CLI](https://developers.openai.com/codex/cli) with Homebrew.
1. Login with the `--with-api-key` parameter and read the API key from STDIN.

```shell
# Set your key in your shell environment (e.g. ~/.zshrc or a .env manager in 1Password)
export OPENAI_API_KEY="sk-..."

# Log in — key is read from the environment, not the command line
printenv OPENAI_API_KEY | codex login --with-api-key

# Verify
codex login status
```

Navigate into a project and prompt Codex with `What is this project about?`.

Tip: Add the [GitLab MCP Server into Codex](https://docs.gitlab.com/user/gitlab_duo/model_context_protocol/mcp_server/#connect-openai-codex-to-the-gitlab-mcp-server) for better context.

## Extensibility and Customization

### Skills

[Agent Skills](https://docs.gitlab.com/user/duo_agent_platform/customize/agent_skills/) are loaded on-demand by agents or users, keeping the context window small by default.

Example projects:

- [Tone of Voice for dnsmichi](https://gitlab.com/dnsmichi/dotfiles/-/tree/main/skills/tone-of-voice?ref_type=heads)

Tip: Maintain skills in one Git repository, and share them across AI tools using symlinks. Each tool loads skills from its own directory:

| AI tool | Skills directory |
| --- | --- |
| GitLab Duo Agent Platform | `~/.gitlab/duo/skills/` |
| Claude Code | `~/.claude/skills/` |
| Codex and other tools following the Agent Skills standard | `~/.agents/skills/` |

```shell
mkdir -p ~/.gitlab/duo/skills ~/.claude/skills ~/.agents/skills

ln -sfn ~/dotfiles/skills/tone-of-voice ~/.gitlab/duo/skills/tone-of-voice
ln -sfn ~/dotfiles/skills/tone-of-voice ~/.claude/skills/tone-of-voice
ln -sfn ~/dotfiles/skills/tone-of-voice ~/.agents/skills/tone-of-voice
```

The [setup.sh script in @dnsmichi's dotfiles project](https://gitlab.com/dnsmichi/dotfiles/-/blob/main/setup.sh?ref_type=heads) automates linking all skills during setup.

### AGENTS.md

The [AGENTS.md standard](https://docs.gitlab.com/user/duo_agent_platform/customize/agents_md/) is similar to custom rules. It supports root and sub-directory-level AGENTS.md files, guiding and instructing agentic AI on how to navigate and use a specific project or directory.

Example environments:

- [Tanuki IoT platform](https://gitlab.com/gitlab-da/demo-environments/tanuki-iot-platform)

### Custom Rules

**Consider adding custom rules by default to every new or existing Developer Advocacy project.**

1. [Custom rules](https://docs.gitlab.com/user/duo_agent_platform/customize/custom_rules/)
2. Custom review instructions for [Code Review Flow](https://docs.gitlab.com/user/duo_agent_platform/customize/review_instructions/).
3. System prompt for [custom agents in the AI Catalog](https://docs.gitlab.com/user/duo_agent_platform/agents/custom/)

Example environments:

- [Tanuki IoT platform](https://gitlab.com/gitlab-da/demo-environments/tanuki-iot-platform)

### MCP Clients

Refer to the [GitLab MCP Clients documentation](https://docs.gitlab.com/user/gitlab_duo/model_context_protocol/mcp_clients/) on how to integrate MCP clients into IDEs.

Internal research issue: [DAP MCP use case testing - DevRel](https://gitlab.com/gitlab-com/marketing/developer-relations/developer-advocacy/developer-advocacy-meta/-/issues/927)

### MCP Server

Refer to the [GitLab MCP Server documentation](https://docs.gitlab.com/user/gitlab_duo/model_context_protocol/mcp_server/) for setup and configuration in AI tools and IDEs.

### Knowledge Graph / Orbit

Follow the [Orbit documentation](https://docs.gitlab.com/orbit/) for setup and integration steps.

The [Orbit GA product epic](https://gitlab.com/groups/gitlab-org/-/work_items/19744) tracks the development and feature roadmap.

### Self-hosted models for Duo Agent Platform

Access to supported self-hosted models requires access to the engineering test infrastructure. Review the [self-hosted models research in FY26 (internal)](https://gitlab.com/gitlab-com/marketing/developer-relations/developer-advocacy/developer-advocacy-meta/-/issues/595#relevant-issues-epics-or-resources) for DRIs, options and ideas.

## GitLab Duo Agent Platform use cases

### Developer Advocates use case prompts

Use these prompts with [GitLab Duo Agentic Chat](https://docs.gitlab.com/user/gitlab_duo_chat/agentic_chat/) in IDEs, and the [CLI](#gitlab-duo-cli):

**Demo Environment Management**

- "Create a new demo project setup guide for `technology/feature`"
- "Document the prerequisites for this demo environment"
- "Generate a troubleshooting guide for common demo setup issues"
- "Create a quick start script for setting up `demo environment`"

**Demo Repository & Code**

- "Create a sample application demonstrating `GitLab feature`"
- "Add comprehensive README with setup instructions for this demo"
- "Generate example CI/CD pipeline for `language/framework` demo"
- "Create a demo showcasing `feature` integration with `technology`"

**Content Creation Support**

- "Extract code snippets from this demo for a blog post"
- "Generate speaker notes for demoing this feature"
- "Create a step-by-step tutorial from this demo repository"
- "Suggest improvements to make this demo more engaging"

**Environment Documentation**

- "Document the tools and versions used in this environment"
- "Create a comparison table of different setup approaches"
- "Generate installation instructions for `OS/platform`"
- "Document environment variables and configuration needed"

**Demo Maintenance**

- "Check if this demo uses deprecated GitLab features"
- "Update this demo to use the latest `framework` version"
- "Verify all demo links and references are still valid"
- "Test if this demo still works with current GitLab version"

**Workshop & Presentation Prep**

- "Create a workshop outline based on this demo"
- "Generate talking points for presenting this feature"
- "Build a hands-on exercise from this example"
- "Create a cheat sheet for workshop participants"

**Integration Examples**

- "Show how to integrate `tool` with GitLab in this demo"
- "Create examples for all `feature` configuration options"
- "Generate sample webhook payloads for testing"
- "Document API usage examples for this integration"

**Documentation & Content Management**

- "Review this page for broken links and outdated information"
- "Check if this documentation follows the handbook style guide"
- "Find all pages that mention `topic` and summarize them"
- "Suggest improvements to make this page more accessible"

**Repository Navigation & Understanding**

- "Show me the most recently updated pages in `directory`"
- "What are the main sections of this handbook?"
- "Find documentation about [specific process or policy]"
- "Who are the main contributors to `directory/file`?"

**Maintenance & Quality**

- "Find pages that haven't been updated in over 6 months"
- "Check for inconsistent formatting across similar pages"
- "Identify duplicate or overlapping content"
- "Review recent merge requests for this section"

**Workflow Automation**

- "Create a new handbook page for `topic` following the template"
- "Update all references to [old term] with [new term]"
- "Generate a changelog for recent updates to `section`"
- "Create an issue for outdated content in `directory`"

**Collaboration**

- "Summarize recent discussions on `topic` from issues and MRs"
- "Who should I ask about [specific handbook section]?"
- "Show me open merge requests that need review"
- "Find related work items for this documentation update"

**CI/CD Specific**

- "Convert this YAML anchor to use extends instead"
- "Add proper rules to this CI job"
- "Optimize the pipeline configuration for faster builds"

## Development

### mise for managing language runtimes

[mise](https://mise.jdx.dev/) is a polyglot version manager that helps manage different language runtimes and tools. It is used in the [GitLab Development Kit (GDK)](https://docs.gitlab.com/development/contributing/first_contribution/configure-dev-env-gdk/) and [GitLab handbook](https://handbook.gitlab.com/docs/development/running-locally/) to manage Node.js, Ruby, Go, and other dependencies.

Developer Advocates can use `mise` to:

1. **Manage multiple language versions**: Easily switch between different versions of Node.js, Python, Ruby, Go, etc., required for various projects or demos.

   ```shell
   mise use node@22
   mise use node@24
   ```

1. **Ensure consistent environments**: Define project-specific tool versions in a `.mise.toml` or `.tool-versions` file, ensuring that all team members (or your different projects) use the same environment.

   ```toml
   # .mise.toml example
   [tools]
   node = "25"
   python = "3.14"
   go = "1.25"
   ```

1. **Simplify tool installation**: Install and manage tools like `npm`, `yarn`, `pip`, `go` without system-wide interference.

   ```shell
   mise install node@25
   mise install python@3.14
   ```

1. **Integrate with IDEs**: Ensure that IDEs like VS Code or JetBrains IDEs pick up the correct tool versions managed by `mise` by configuring the shell environment.

#### Tips and best practices for mise

1. **Install `mise`**: Follow the [official installation guide](https://mise.jdx.dev/getting-started.html).
1. **Configure your shell**: Add `eval "$(mise activate)"` to your shell configuration file (e.g., `.zshrc`, `.bashrc`).
1. **Use `.mise.toml` or `.tool-versions`**: For project-specific versions, create one of these files in your project root. `mise` will automatically detect and activate the specified versions when you navigate into the directory.
1. **Global versions**: Set global default versions for tools using `mise global <tool>@<version>`.

    ```shell
    mise global node@22
    ```

1. **Check current versions**: Use `mise current` to see which tool versions are active in your current directory.
1. **List installed versions**: Use `mise ls` to see all installed versions of a tool.
1. **Update tools**: Keep your tools up-to-date with `mise upgrade`.

For more advanced usage and configuration, refer to the [mise documentation](https://mise.jdx.dev/dev-tools/).

#### mise environments in GitLab development

- [GitLab Development Kit (GDK)](https://gitlab.com/gitlab-org/gitlab-development-kit)
- [GitLab LSP](https://gitlab.com/gitlab-org/editor-extensions/gitlab-lsp) (integrated into [IDEs](#ides) and [CLI](#cli))

## Remote Development Workspaces

[Workspaces](https://docs.gitlab.com/user/workspace/) offer cloud development environments, running on [Developer Relations Cloud Resources](/handbook/marketing/product-and-technical-marketing/developer-advocacy/tools-and-platforms/cloud-resources/).

> Status: Inactive. Currently, there is no infrastructure maintainer. The following documentation exists for historical reference in the future.

The [remote-development sub group](https://gitlab.com/gitlab-da/use-cases/remote-development) has an agent for Kubernetes installed, which is documented in the [agent-kubernetes-gke](https://gitlab.com/gitlab-da/use-cases/remote-development/agent-kubernetes-gke) project. This includes troubleshooting when the agent becomes unresponsive, and workspaces are not created.

Resources:

1. The Kubernetes cluster `da-remote-development-1` needs to be running in GKE. Current resources: 3 nodes. Total 6 vCPU, 12 GB memory.
1. The domain `remote-dev.dev` has been purchased through the Google DNS service and points to the Kubernetes cluster's public IP.
1. The TLS certificates have been generated manually with Let's Encrypt and need to be renewed quarterly (2023-08-15), following the [documentation steps](https://gitlab.com/gitlab-da/use-cases/remote-development/agent-kubernetes-gke).

## Learning resources

### Team member examples

- [@dnsmichi's dotfiles project](https://gitlab.com/dnsmichi/dotfiles) as a production example, which documents the work environment setup including terminal, IDEs, agentic AI and development tools.

### Talks and demos highlighting Dev Environments

Review the [Developer Advocacy content library](/handbook/marketing/product-and-technical-marketing/developer-advocacy/content/) and the following resources:

1. Learning AI 101: Practical Foundations for Developers - 2025-06, Open Source @ Siemens
    - Slides: [public](https://dnsmichi.click/learning-ai-101-os-siemens-2025), [internal](https://docs.google.com/presentation/d/1PUCUrVzKnzc25md8gbh1jYznz-dUFfQcENvbR9xUJ7k/edit)
