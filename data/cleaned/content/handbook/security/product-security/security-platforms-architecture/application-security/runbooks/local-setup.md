---
title: "AppSec Engineer's Local Setup"
---

When evaluating security issues or MRs, it can be useful to have a way to reproduce issues, dig in to root causes, look for further impacts. This can also be a great way to get familiar with GitLab during your first few weeks of onboarding. Here are some handy tips & tricks.

## How to setup a local GDK environment

1. Request a [team member license](/handbook/support/internal-support/#unlock-premiumultimate-features-on-self-managed--gdk-for-team-members) 100 seats (this would avoid removing the ~50 users allready added to the gdk at install).
1. If you plan to replace an existing local install of a GDK or do the setup for [geo](https://gitlab.com/gitlab-org/gitlab-development-kit/-/blob/main/doc/howto/geo.md), first run in the existing gdk folder `gdk kill`. This will stop the processes and release the ports used by different services.
1. General information about the gdk install steps can be found at [gitlab-development-kit](https://gitlab.com/gitlab-org/gitlab-development-kit/-/blob/main/doc/_index.md)
   - Start the [one line install](https://gitlab.com/gitlab-org/gitlab-development-kit/-/blob/main/doc/_index.md#one-line-installation ) with `curl "https://gitlab.com/gitlab-org/gitlab-development-kit/-/raw/main/support/install" | bash`
   - install in gdk, or choose the folder name
   - install with `mise`
   - once the install finished do a `gdk restart` to make sure all services started
1. Once the install is done login with `root` / `5iveL!fe` and change the default password
1. Apply the license, either via [admin/settings/addlicense](http://localhost:3333/admin/application_settings/general#js-add-license-toggle) or using the [rails console](https://docs.gitlab.com/administration/license_file/#add-a-license-through-the-console).
1. Check if the license was applied correctly in [admin/subscription](http://localhost:3000/admin/subscription)

## Enable GitLab Duo in GDK

 Follow the official wiki below to configure your local GDK with a local instance of Duo.

1. Set up and configure Duo in your local GDK following instructions [here](https://gitlab-org.gitlab.io/gitlab-development-kit/howto/ai/#prerequisites)
2. Verify your set up following instructions [here](https://gitlab-org.gitlab.io/gitlab-development-kit/howto/ai/#verify-your-setup).

The Additional Resources section [here](https://gitlab-org.gitlab.io/gitlab-development-kit/howto/ai/#additional-resources) provides documentation for troubleshooting.

## Enable Duo with VS code

1. With a user that has access to the AI features, create a PAT with API access
1. Download and install [VS code](https://code.visualstudio.com/)
1. From Extensions install GitLab
1. Configure a [VS code profile](https://code.visualstudio.com/docs/configure/profiles) for GDK go to Code > Settings > Profiles > New Profile
1. In VS code, open the Command Palette (Command + Shift + P) and select "GitLab: Validate GitLab Accounts" to switch to your GDK account. PAT should be added here.
1. GitLab Agent should be added on left tool bar

## Link the VS Code Duo extension to Language Server

The following sequence illustrates how an IDE extension authenticates with the GitLab instance and later Duo Agent Platform.

```mermaid
sequenceDiagram
    participant ext as Editor Extension
    participant lsp as GitLab Language Server
    participant sm as GitLab
    participant aigw as AI Gateway (GitLab-hosted)
    participant dws as Duo Agent Platform (GitLab-hosted)

    ext-->>lsp: Send workspace configuration
    par Fetch Personal Access Token info
        lsp->>+sm: GET /api/v4/personal_access_tokens/self
        sm->>-lsp: 200 OK {...}
    and Fetch OAuth token info
        lsp->>+sm: GET /oauth/token/info
        sm->>-lsp: 200 OK {...}
        Note right of lsp: Store OAuth access token until just before expiry
    end

    loop Every ~120 minutes
        lsp->>+sm: GET /api/v4/ai/duo_workflows/direct_access
        sm->>+dws: Send GenerateToken request (gRPC)
        Note right of dws: duo_workflow_service/server.py generates a signed JWT through the Cloud Connector library code.
        dws->>-sm: ServiceResponse.success
        sm->>-lsp: 200 OK {...}
        Note right of lsp:  Store direct access details for Duo Agent Platform for ~120 minutes
    end
```

Note: these steps are an expansion from the [existing steps in documentation](https://gitlab.com/gitlab-org/editor-extensions/gitlab-lsp/-/blob/main/README.md#connect-to-ls-in-the-vs-code-extension).

All of below steps are completed as the GitLab user profile:

1. Clone the [gitlab-vscode-extension](https://gitlab.com/gitlab-org/gitlab-vscode-extension/-/tree/main?ref_type=heads) project.
1. Clone the [gitlab-lsp](https://gitlab.com/gitlab-org/editor-extensions/gitlab-lsp) project in the same path as your VS Code extension project, for example:
   - LSP is in /Users/<USERNAME>/Projects/gitlab-lsp
   - vscode extension is in /Users/<USERNAME>/Projects/gitlab-vscode-extension
1. Have the two project open side by side in a terminal for better setup.
1. For gitlab-vscode-extension project, follow below steps:
   - Run: `npm install`
   - Run extension in dev mode:
       1. Open the project in vscode
       1. Run the View: Show Run and Debug command (Cmd+Shift+P).
       1. Ensure the Run Extension command is selected.
       1. Select the green play icon, or press F5.
1. For gitlab-lsp project, follow below steps:
    1. Open the project in vscode
    1. Run `npm install`
    1. Run `npm run build`
    1. Run `GITLAB_WORKFLOW_PATH=/Users/<USERNAME>/Projects/gitlab-vscode-extension code .`
    1. Run the Attach to VS Code Extension launch task.
    1. Run `npm run watch -- --editor=vscode --packages agentic-duo-chat webview-duo-workflow duo-chat duo-chat-v2 webview-duo-chat webview-duo-chat-v2 webview-vuln-details`
1. Verification: to verify it's working, first make sure you have enabled the GitLab debugging option in the Duo Workflow extension setting and then restart the extension so that you can see debug logs:

![Verification](/images/security/product-security/appsec/2_debug_settings.png)
![debug](/images/security/product-security/appsec/3_debug_settings.png)

## Connect LS with Local GDK Changes for Duo Development

1. Setup a GDK profile
1. Follow the two steps outlined in the [doc](https://gitlab.com/gitlab-org/editor-extensions/gitlab-lsp#connect-ls-with-local-gdk-changes-for-duo-development)

In VSCode, check for "GitLab Language Server" logs in the output pane and see there are any errors. If you come across token errors like below, then go to GitLab Workflow extension setting and make sure ignore TLS/SSL cert errors option is ticked:

```bash
2025-08-20T10:54:14:972 [warning]: Both PAT and OAuth token checks failed: PAT Token: {"valid":false,"reason":"unknown","message":"Token validation failed: Error: request to https://gdk.test:3443/api/v4/personal_access_tokens/self failed, reason: unable to verify the first certificate"}, OAuth Token: {"valid":false,"reason":"unknown","message":"Token validation failed: Error: request to https://gdk.test:3443/oauth/token/info failed, reason: unable to verify the first certificate"}
2025-08-20T10:54:14:973 [info]: [CodeSuggestionsInstanceTelemetry] Instance Telemetry: GitLab Duo Code Suggestions telemetry is always enabled in self-managed instances.
2025-08-20T10:54:14:973 [warning]: Token is invalid. Token validation failed: Error: request to https://gdk.test:3443/api/v4/personal_access_tokens/self failed, reason: unable to verify the first certificate. Reason: unknown
2025-08-20T10:54:14:973 [warning]: Token is invalid. No token provided. Reason: invalid_token
```

![Setup_language_server](/images/security/product-security/appsec/4_gitlab_workflow.png)

1. Restart the extension and to check if it's working, open a GDK folder (git clone a GDK project locally, make sure it has Duo enabled) and check the logs for errors, an example of a working agentic workflow log:

```bash
2025-08-20T11:13:46:002 [info]: [Duo Agentic Chat Plugin] Received new event
2025-08-20T11:13:46:002 [debug]: [WebviewInstanceMessageBus:agentic-duo-chat:8327ccee-1b85-48ba-abd6-eb4cfb5e3f1f] Sending notification: workflowCheckpoint
2025-08-20T11:13:46:002 [debug]: [WebviewInstanceMessageBus:agentic-duo-chat:8327ccee-1b85-48ba-abd6-eb4cfb5e3f1f] Sending notification: workflowStatus
2025-08-20T11:13:46:503 [debug]: [WorkflowTokenService] Reusing existing valid token for workflow "3"
2025-08-20T11:13:46:503 [debug]: [DuoWorkflowNodeExecutor][3] Received new checkpoint: {"workflowStatus":"RUNNING"}
```

## Run a different branch of AI Gateway and Duo Agent Platform Service

When reviewing MRs in [AI Gateway](https://gitlab.com/gitlab-org/modelops/applied-ml/code-suggestions/ai-assist), instead of following the setup steps in [README.md](https://gitlab.com/gitlab-org/modelops/applied-ml/code-suggestions/ai-assist/-/blob/main/README.md?ref_type=heads), AppSec engineers often times just need to follow these [instructions](https://gitlab.com/gitlab-org/gitlab-development-kit/-/blob/main/doc/howto/gitlab_ai_gateway.md#optional-run-a-different-branch-of-ai-gateway-and-duo-agent-platform-service) to test changes on a specific branch.

## Setting up GDK for AI Catalog Development

Follow the instructions in this [wiki page](https://gitlab.com/gitlab-org/ai-powered/ai-catalog/team-tasks/-/wikis/Setting-up-GDK-for-AI-Catalog-Development) on detailed steps.

### Step through execution chains

If you want to see the code executed as part of a web or API request, an interactive debugger may be a useful tool. Here's how to [configure Pry & Thin](https://gitlab.com/gitlab-org/gitlab-development-kit/-/blob/main/doc/howto/pry.md#using-thin)

A typical workflow might be to find the `Controller` action which kicks off the request (methods like `create` or `update` are good bets), add in `binding.pry`, save the file, then perform that request in a browser. The execution will stop and in a terminal you can inspect the current state using IRB, type `step` to go in_to_ a method, `next` to go to the next statement, and `continue` to let the request run to the next break point and/or completion.

Watching logs can be helpful: `tail -f gitlab/log/development.log`.

## Install a testing proxy

Your role might not require you to do "penetration testing", but having access to a testing proxy that lets you intercept and manipulate requests can help with reproducing HackerOne issues.

The AppSec team have a multi-user license for [Burp Suite Professional](https://portswigger.net/burp/pro). Ask the AppSec team in `#security_help` about getting a license, and ([download the latest stable version here](https://portswigger.net/burp/releases)). You can also use [OWASP ZAP](https://www.zaproxy.org/) which is free and open source.

These tools can easily cause damage to websites or eat up your CPU with active scans. In OWASP Zap, use "Safe" mode to prevent any potentially malicious requests. In Burp Suite, disable any live "audit" scans.

## Browser Profiles

When testing requires using multiple users, an Incognito / Private tab is an easy option. You can also create and use [un-signed-in Chrome Profiles](https://support.google.com/chrome/answer/2364824) or [Firefox Multi-Account Containers](https://support.mozilla.org/en-US/kb/containers) to provide "session sandboxes", which will persist beyond window closure (unlike Incognito tabs) and you can colour code them to help with visual distinction.

## Mocking Servers / tunnels

Making your local machine accessible from the internet is not permitted, which precludes tools like `ngrok` or `localtunnel`. Use GitLab's [Sandbox Cloud](/handbook/company/infrastructure-standards/realms/sandbox) to host mock servers instead. Refer to [Secure Cloud testing environments](/handbook/support/workflows/test_env/#securing-cloud-testing-environments) for advice on how to secure your Sandbox Cloud test environments.

## Debugging and GDK tips

- `gdk update` Pull application changes from Git
- `gdk tail` Tail logs for all services
- `gdk tail gitlab-ai-gateway` Tail logs for AI services
- `gdk doctor` Run diagnostics on GDK
- in the gitlab folder run: `bundle exec rake gitlab:duo:verify_self_hosted_setup` [to verify the local setup](https://docs.gitlab.com/administration/gitlab_duo_self_hosted/troubleshooting/#verify-gitlab-setup)
- `gdk kill` Forcibly kills services - usefull when a service hangs a port or when to upgrade
- [Feature flags](https://docs.gitlab.com/operations/feature_flags/) can be enabled via `http://127.0.0.1:3000/rails/features`
