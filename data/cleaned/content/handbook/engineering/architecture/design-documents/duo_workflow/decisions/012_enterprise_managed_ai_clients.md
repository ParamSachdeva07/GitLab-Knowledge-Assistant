---
title: Enterprise-Managed AI Clients
status: proposed
creation-date: "2026-09-09"
authors: [ "@erran", "@ohoral" ]
coach: [ ]
approvers: [ ]
owning-stage: "~devops::ai_powered"
participating-stages: []
toc_hide: true
description: "Architecture decision record for resolving GitLab AI client settings from multiple sources, user, project, and administrator-managed, with a documented precedence and merge strategy."
---

{{< engineering/design-document-header >}}

## Summary

Provide a consistent interface for users and administrators to manage settings
for AI Clients. Support resolving client settings from multiple sources where a
clear merge strategy is applied and documented.

## Motivation

Avoid client settings and administrator enforced settings which are implemented
inconsistently through GitLab instance settings, versioned API endpoints, and
user settings persisted in different locations by client.

The precedence and resolution of client settings for competitors is clearly
documented:

- [Claude managed settings](https://code.claude.com/docs/en/managed-settings)
- [Codex managed configuration](https://learn.chatgpt.com/docs/enterprise/managed-configuration)
- [Copilot enterprise-managed settings](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/use-managed-settings/get-started)

### Goals

> What is it trying to achieve?

- Clear client settings locations

> How will we know that this has succeeded?

- Implement user settings for:
  1. Enable telemetry
  2. Show work items in new sessions
  3. Notifications
  4. Theme
  5. Enable auto-mode
  6. Enable workspace agents
- Implement administrator managed settings for:
  1. Enable telemetry
  2. Enable auto-mode
  3. Enable workspace agents
  4. Recommended plugin marketplaces
  5. Recommended plugins
  6. Required plugin marketplaces
  7. Required plugins
- Document precedence of the above settings

> What are other less tangible opportunities here?

- Automated documentation generation for client settings.

### Non-Goals

> What is out of scope for this document?

1. Migration path for legacy settings. The one exception: the Duo CLI carries a
   recorded telemetry opt-out into `settings.json` once, so that data collection
   is never turned back on without asking. Other preferences start from their
   defaults; nothing is deleted from the old storage.
1. Implementing a Rails endpoint to fetch client settings
1. Implementing a Rails endpoint to resolve tool permissions.

## Proposal

Introduce a settings resolution service with support for loading:

- User global `settings.json` file
- MDM/Jamf managed `settings.managed.json` file

Future sources:

1. Shared project settings
   - Loaded from current working directory not remote
1. Local project settings overrides (e.g. `settings.local.json`)
   - Loaded from current working directory not remote
1. Centralized `$root_namespace/duo-workspace` project `settings.managed.json` file
   - Cached and refreshed periodically in the background for existing sessions

## Design and implementation details

### Settings sources

A settings source is anything that can supply a value for a setting. The
resolver and the file sources are shared by all clients. Each client assembles
its settings sources into one ordered list and hands it to the resolver at
startup, so the whole precedence for that client is readable in one place.
Adding a new kind of source, such as project settings or a remote file, means
implementing that source and inserting it into the list. No existing setting
or source needs to change.

The proposed order, from highest to lowest precedence:

| # | Source | Location | Enforced | Status |
|---|---|---|---|---|
| 1 | Managed settings file, deployed through MDM, Jamf or group policy | Fixed per-platform path, see [managed settings file location](#managed-settings-file-location) | Yes | First iteration |
| 2 | Remote managed settings | `settings.managed.json` in the `$root_namespace/duo-workspace` project | Yes | Future |
| 3 | Session overrides supplied by the client | CLI flags and environment variables, IDE settings, CI job variables | No | First iteration |
| 4 | Local project overrides | `.gitlab/duo/settings.local.json` in the working directory | No | Future |
| 5 | Shared project settings | `.gitlab/duo/settings.json` in the working directory | No | Future |
| 6 | Account settings | `~/.gitlab/duo/accounts/<host>/<user>/settings.json`, one flat file per GitLab account | No | Future |
| 7 | User settings | `~/.gitlab/duo/settings.json` | No | First iteration |
| 8 | Settings shipped by installed plugins | Plugin manifest; position to be confirmed | No | Future |

Local project overrides sit above shared project settings so a developer can
adjust a team default for their own checkout.

For most settings the value comes from the source with the highest precedence
that sets it. When no source sets it, the default declared in the setting's
definition applies. Every setting has a default, so resolution always produces
a value.

### Setting definitions

Every setting is declared once, in the LSP repo alongside the resolver and the
file sources. The declaration drives resolution, validation, the interactive
settings UI, the generated JSON Schema, and the generated documentation of
which settings are supported by which client. The Rails work item
[Create AI clients settings schema](https://gitlab.com/gitlab-org/gitlab/-/work_items/627579)
does not author a separate schema; instead the generated JSON Schema is
published as an LSP build artifact and synced into the Rails project by
automation, tracked in
[gitlab-org/gitlab#628967](https://gitlab.com/gitlab-org/gitlab/-/work_items/628967).

```typescript
type SourceId =
  | 'managed'
  | 'remote'
  | 'session'
  | 'project-local'
  | 'project'
  | 'account'
  | 'user'
  | 'plugin';

type MergeStrategy =
  | 'replace'
  | 'union'
  | { restrict: 'intersection' | 'union' | 'min' | 'max' | 'anyTrue' | 'allTrue' }
  | { perKey: MergeStrategy };              // records: each key resolves on its own

interface SettingDefinition<T> {
  schema: ZodType<T>;                       // validation and schema generation
  default: T;                               // required; applies when no source sets the setting
  description: string;                      // used for docs and $schema
  merge: MergeStrategy;                     // see merge strategies below
  allowedSources?: SourceId[];              // omit = any source may set it
  onUnavailable?: 'fallthrough' | { failClosedTo: T }; // when an administrator source cannot be loaded
  clients?: Array<'cli' | 'editor' | 'ci'>; // where the setting applies; omit = every client
}

interface StartupContext {
  workingDirectory: string;                 // for project sources
  homeDirectory: string;                    // for the user file
  platform: 'darwin' | 'linux' | 'win32';   // for the managed file location
  instanceUrl?: string;                     // for the remote source
  namespace?: string;                       // detected project namespace, for the remote source
  client: { kind: 'cli' | 'editor' | 'ci'; version: string };
}

interface SettingsSource {
  readonly id: SourceId;
  readonly enforced: boolean;               // true for 'managed' and 'remote'
  load(context: StartupContext): Promise<SourceResult>;
}

type SourceResult =
  | { status: 'ok'; values: Record<string, unknown> }
  | { status: 'absent' }                    // nothing to say, e.g. file missing
  | { status: 'unavailable'; reason: string }; // could not load, e.g. fetch failed

interface Resolved<T> {
  value: T;
  source: SourceId | 'default';             // which source supplied the value
  readOnly: boolean;                        // true when the source is enforced
  keys?: Record<string, { source: SourceId | 'default'; readOnly: boolean }>; // perKey settings only
}

interface SettingsResolver {
  get<T>(definition: SettingDefinition<T>): Resolved<T>;
}
```

`clients` lists the AI clients a setting applies to: `cli` is the Duo CLI,
`editor` is the language server embedded in the editor extensions, and `ci` is
a flow executed inside a GitLab CI/CD job by the workflow executor. All three
are built from the same repository and share the definitions. `clients` is
optional; omitting it applies the setting to every client. An ACP server
started by the Duo CLI inherits the `cli` profile until ACP needs values of
its own, at which point it becomes its own client kind.

`load` receives a `StartupContext` gathered once by the client before
resolution: where the working directory and home directory are, which platform
the client runs on, which GitLab instance and project namespace were detected,
and which client kind is asking. A source reads what it needs from it. The
session override source is the exception; it is constructed with the client's
parsed flags or IDE settings and ignores the context.

Sources do not know their own rank and cannot see each other. Only the
session override source is client-specific; every other source is shared.

`allowedSources` restricts which sources may set a setting. Some settings only
make sense from an administrator, such as `requiredPlugins`; some only from the
user, such as theme; most may come from anywhere, which is the default when the
field is omitted. The restriction is applied in three places:

1. At load, the resolver drops a value for a key whose definition does not list
   that source, and warns once with the file path and the key.
1. At write, the interactive settings UI only writes keys that allow the `user`
   source.
1. In the generated JSON Schema, one schema is produced per file kind from the
   same definitions, so an editor flags a misplaced key before the client runs.

`allowedSources` and `enforced` are independent. The first says which sources
may set a value, the second says whose value is final.

#### Scope of a setting

The user settings file is per operating-system user. A setting in it has one
value for every client that reads it; the file has no per-client sections.
Client-specific knobs belong in each client's own settings, IDE settings for the
editors and flags or environment variables for the CLI. Should a per-client
override ever be needed, it would be a separate flat file per client, never a
section inside the shared file.

A setting that must differ between GitLab accounts, such as a selected model
that exists on one instance but not another, names the `account` source in
`allowedSources` and lives in that account's own file, which uses the same
schema as the user file. The client writes each setting to the file its scope
points at; the user is never asked to choose a file.

Example definitions:

```typescript
const settings = defineSettings({
  telemetry: {
    enabled: setting({
      schema: z.boolean(),
      default: true,
      description: 'Send anonymous usage data to improve GitLab Duo.',
      merge: 'replace',
      clients: ['cli', 'editor'],
    }),
    url: setting({
      schema: z.string().url(),
      default: 'https://telemetry.gitlab.com',
      description: 'Endpoint that receives telemetry events.',
      merge: 'replace',
      allowedSources: ['managed'],
      clients: ['cli', 'editor'],
    }),
  },
});

resolver.get(settings.telemetry.enabled);   // Resolved<boolean>
```

The corresponding file is nested in the same way:

```json
{
  "telemetry": {
    "enabled": false
  }
}
```

### Enforcement

A value is enforced because of where it comes from, not because of which
setting it is. Two sources are administrator-controlled: the local managed file
and the remote managed settings from the `duo-workspace` project. Everything
they set is enforced; nothing from other sources is. For an enforced value the
resolver marks it read-only, and the interactive settings UI shows it as
disabled together with its source, for example "set by your organization".
Values from every other source can be overridden by a source above it.

What enforcement means depends on the merge strategy of the setting:

1. `replace`: the managed value is the value.
1. `union`: the managed entries cannot be removed. The user may add entries, so
   the result is the managed list plus the user's.
1. `restrict`: the managed value sets the limit. The user may make the setting
   more restrictive, for example by removing entries from an allowlist, but not
   less restrictive.

Enforcement applies only to settings the managed source actually sets. The
user keeps control of everything the administrator is silent about.

Administrators express recommendations as separate settings rather than as a
softer tier of enforcement. For example `recommendedPlugins` is advertised
to the client and user to install, while `requiredPlugins` is an enforced
list the client installs.

### Managed settings file location

The managed settings file is read from a fixed path on each platform. Only
administrators can write to these locations by default, which is what makes
enforcing the file's values meaningful:

- Linux: `/etc/gitlab/duo/settings.managed.json`
- macOS: `/Library/Application Support/GitLab/duo/settings.managed.json`
- Windows: `C:\Program Files\GitLab\duo\settings.managed.json`

On Windows the file is not read from `%ProgramData%`. Standard users can create
folders under `C:\ProgramData` and own what they create, so a user could create
`GitLab\duo` before the policy is deployed and later replace or delete the file.

The path is a literal and is not built from environment variables such as
`%ProgramFiles%`, because the user controls them. As a result, the client does
not find the file on a machine where `Program Files` is not on `C:`.

WSL is not covered. A client running inside WSL reads the Linux path from the
distribution, which Windows group policy does not manage.

### Merge strategies

Each setting declares how values from several sources combine. A strategy runs
over the sources that set the setting; the default is used only when none do.
A setting whose "unset" state is meaningful, such as an allowlist where no
restriction exists until an administrator adds one, declares that state in its
type and default, for example `string[] | null` with `null` meaning
unrestricted.

1. `replace`: the value from the source with the highest precedence that sets
   the setting wins. This applies to scalar preferences such as telemetry,
   theme or auto-mode.
1. `union`: values from all sources are combined as a set. This applies to
   additive lists such as additional marketplaces or recommended plugins.
1. `restrict`: a lower source may tighten the value but never loosen it. The
   strategy carries a direction, because what "tighter" means depends on the
   shape of the value:
   - `intersection` for allowlists: only entries present in every source
     remain.
   - `union` for blocklists: an entry blocked by any source stays blocked.
   - `min` and `max` for numbers and ordered choices, where the smaller or the
     larger value is the stricter one. An enum's order comes from its schema.
   - `anyTrue` and `allTrue` for booleans, depending on whether `true` or
     `false` is the safer value.
1. `perKey`: for records such as a map from plugin name to enabled flag. Each
   key is resolved on its own with the inner strategy over the sources that
   mention it, and enforcement applies per key.

The user does not need special syntax to tighten a setting. They write the
same key in their own file and the strategy combines the values.

### Failure handling

1. A missing file is `absent`. The resolver moves on to the next source.
1. A file that cannot be parsed is `unavailable`. The client warns once with the
   path and the parse error and moves on. It never deletes a settings file or
   replaces its contents to recover from an error; the file is left as it is
   for the user to fix.
1. A value that fails validation is dropped with a warning naming the key and
   the expected type. The rest of the file is kept.
1. Unknown keys are ignored, so keys can be added and removed over time.
1. When an administrator source that may set a setting cannot be loaded,
   because the managed file is unreadable or the remote fetch fails, or
   supplies a value that fails the setting's schema, the default behavior is
   `fallthrough`: the source is treated as absent and the next one applies.
   That is right for preferences, but for a governance setting it would lift
   the restriction at exactly the moment the policy is unreachable. Such a
   setting declares `onUnavailable: { failClosedTo: value }`, naming the
   value it holds while the policy cannot be read, such as an empty allowlist
   or `false` for an enable flag. The value is declared explicitly because the
   client cannot derive the safe direction from the schema for most merge
   strategies, and `default` keeps its own meaning: the value when no source
   sets the setting. The client stays usable but restricted, and the setting
   is read-only, until the policy can be read again.
1. If a settings file cannot be written, the change still applies to the
   running session and the client reports that it could not be saved.

### File format

1. Files are JSON with comments and trailing commas allowed on read. Writes
   made by the client preserve comments and unknown keys.
1. Each file may carry a `$schema` key, so editors validate the file and offer
   completion. The client writes the `$schema` line when it creates the user
   file.
1. A JSON Schema is generated for each kind of settings file from the single
   list of setting definitions and published at a fixed URL. Each schema
   contains the keys that file's source may set, so a key allowed from several
   sources appears in each of their schemas.

## Alternative Solutions

### Server managed settings

Pros:

- Single source of truth is the GitLab instance

Cons:

1. We must wait for upgrades which can take multiple milestones and cannot be
   backported outside of bug/security fixes.
1. We must merge settings across instance versions
1. We must implement defaults by instance version
1. We must consider feature flag values to determine default values
1. We continue to introduce new GraphQL queries

### Do nothing

Pros:

- No changes needed

Cons:

- Continue facing unclear requirements for precedence/merge strategy of
  different AI client settings.
