---
title: 'Working merge requests'
description: 'Documentation on working merge requests'
---

This guide explains how to create, review, and merge requests (MRs) for Customer Support Systems projects. Following these practices ensures code quality, maintains security standards, and enables collaborative development across the team.

## Understanding merge requests

### Why we use merge requests

Merge requests provide several critical benefits:

- **Peer review**: Ensures code quality and catches potential issues before deployment
- **Collaboration**: Enables discussion and knowledge sharing among team members
- **Audit trail**: Creates documented history of what changed, why, and who approved it
- **Quality gates**: Prevents problematic code from reaching production
- **Version control**: Allows easy rollback if changes cause issues

## Creating a merge request

### Prerequisites

Before creating a merge request, ensure you have:

- A corresponding issue (Feature Request, Administrative, Bug, etc.) unless it's a trivial documentation fix
- A properly named branch following the format: `USERNAME-PROJECT-IID`
  - Example: `jcolyer-support-ops-project-1963`
  - See [Coding Standards - Branches](/handbook/eta/css/resources/coding-standards#version-control) for details
- Committed your changes with descriptive commit messages
- Tested your changes locally (when applicable)

### Creating the merge request

To create a merge request:

1. Navigate to your project on GitLab.com
1. Go to **Merge requests** in the left sidebar
1. Click the **New merge request** button
1. Select your source branch (your working branch) and target branch (usually `master` or `main`)
1. Click **Compare branches and continue**
1. Fill out the merge request details:
   - **Title**: Use a clear, descriptive title summarizing the changes
     - Good: "Add new trigger for premium support routing"
     - Bad: "Update triggers" or "Fix stuff"
   - **Description**: Provide context including:
     - Link to the related issue: `Relates to ISSUE_URL`
     - Summary of what changed and why
     - Any special testing or deployment considerations
     - Breaking changes or dependencies (if applicable)
   - **Assignee**: Assign to yourself
   - **Reviewer**: Assign to a team member for review (see [Requesting a review](#requesting-a-review))
1. Click **Create merge request**

### For sync repositories

When creating merge requests in sync repositories (triggers, views, automations, etc.), the MR will automatically run comparison pipelines that:

- Validate YAML syntax
- Check for required fields
- Compare proposed changes against current Zendesk configuration
- Generate comparison reports

Review the pipeline results to ensure your changes are correct before requesting review.

## Requesting a review

### Who to request review from

- **For standard changes**: Request review from any available team member with knowledge of the area
- **For complex or risky changes**: Request review from multiple team members or senior engineers
- **For security-sensitive changes**: Include security-aware reviewers
- **When unsure**: Ask in the team channel for reviewer recommendations

### What reviewers should check

When conducting a peer review, reviewers should verify:

- **Functionality**: Changes accomplish the stated goal
- **Code quality**: Follows [coding standards](/handbook/eta/css/resources/coding-standards)
- **Security**: No hardcoded secrets, proper input validation, secure practices
- **Testing**: Changes have been tested (when applicable)
- **Documentation**: Complex logic is commented, README updated if needed
- **Side effects**: Changes don't break existing functionality
- **Deployment impact**: Understand what will happen when deployed

## Reviewing a merge request

### How to review

When assigned as a reviewer:

1. Read the related issue to understand the context
1. Review the changes in the **Changes** tab
   - Look at the diff for each file
   - Check for issues listed in [What reviewers should check](#what-reviewers-should-check)
1. Check pipeline results (especially for sync repos)
   - Ensure pipelines pass
   - Review comparison reports
1. Test the changes locally if needed (for code changes)
1. Leave feedback using one of these methods:
   - **Approve**: If changes look good, click **Approve** on the merge request
   - **Request changes**: Add comments on specific lines or general comments explaining concerns
   - **Ask questions**: Use comments to clarify unclear aspects

### Providing feedback

When leaving feedback:

- **Be specific**: Point to exact lines and explain the issue
- **Be constructive**: Suggest improvements, don't just criticize
- **Be timely**: Review within 1-2 business days when possible
- **Ask questions**: If something is unclear, ask rather than assume
- **Acknowledge good work**: Call out clever solutions or improvements

### Approving a merge request

To approve a merge request:

1. Ensure all your concerns are addressed
1. Click **Approve** in the right sidebar
1. Optionally add a comment: "Looks good! ✅" or noting what you verified

## Merging a merge request

### When to merge

A merge request can be merged when:

- ✅ It has been approved by at least one peer reviewer
- ✅ All pipeline checks pass (green checkmarks)
- ✅ All discussions are resolved (or explicitly marked as non-blocking)
- ✅ The related issue confirms this is ready to deploy
- ✅ For Standard deployments: you're ready for it to deploy on the next deployment date

### How to merge

To merge an approved merge request:

1. Verify all [merge criteria](#when-to-merge) are met
1. Click **Merge**

### After merging

After your MR is merged:

- **For Ad-hoc deployments**: Changes deploy immediately or on next script run
- **For Standard deployments**: Changes will deploy on the next scheduled deployment (1st of the month)
- **Add a comment on the related issue**: Note that the MR has been merged
- **Monitor for issues**: Watch for any unexpected behavior after deployment
- **Perform exception deployment if urgent**: See individual documentation pages for exception deployment procedures

## Common merge request scenarios

### Making changes after review

If a reviewer requests changes:

1. Make the requested changes in your local branch
1. Commit and push the changes
1. The MR will automatically update with your new commits
1. Reply to reviewer comments explaining what you changed
1. Request re-review if needed

### Handling merge conflicts

If your MR shows merge conflicts, you can resolve it via CLI using the following method:

1. Navigate to the project repo on your computer
1. Checkout the source branch (we'll use `jcolyer-source-branch` as an example)

   ```bash
   git checkout jcolyer-source-branch
   ```

1. Rebase your branch from the target branch (we'll use `jcolyer-target-branch` as an example):

   ```bash
   git rebase origin/jcolyer-target-branch
   ```

1. Review the output to locate the files containing conflicts
1. Edit the files in question to resolve the conflicts
1. Add the files you have modified (we'll use `public/index.html` as an example):

   ```bash
   git add public/index.html
   ```

1. Continue the rebase:

   ```bash
   git rebase --continue
   ```

1. Repeat from step 4 as needed (until the output says the rebase is complete)
1. Push your changes to the source branch using the flag `--force-with-lease`:

   ```bash
   git push origin jcolyer-source-branch --force-with-lease
   ```

1. The MR will update automatically

### Closing a merge request without merging

If you decide not to proceed with the changes:

1. Add a comment explaining why the MR is being closed
1. Close the related issue (if appropriate)
1. Click **Close merge request** at the bottom of the MR
1. Optionally delete the source branch

## Best practices

- **Keep MRs focused**: One MR should address one issue or feature. Avoid mixing unrelated changes.
- **Keep MRs small**: Smaller MRs are easier to review and less risky to merge. Aim for under 500 lines changed when possible.
- **Write clear descriptions**: Future you (and your teammates) will appreciate context about why changes were made.
- **Respond to reviews promptly**: Address feedback within 1-2 days to keep work moving.
- **Test before requesting review**: Don't use reviewers as QA. Test your changes first.
- **Update documentation**: If your changes affect processes or usage, update relevant documentation.
- **Link to related issues**: Always connect MRs to the issue they address for traceability.

## Common issues and troubleshooting

### Pipeline failures in sync repositories

If the comparison pipeline fails:

- Review the pipeline logs to identify the issue
- Common causes:
  - YAML syntax errors (check indentation, colons, quotes)
  - Missing required fields (title, position, etc.)
  - Duplicate titles in sync repo
  - Missing managed content files (for triggers/views with contains_managed_content: true)
- Fix the issues and push new commits

### Cannot push to branch

If you get permission errors when pushing:

- Verify you have at least **Developer** access to the project
- Ensure you're pushing to your own branch, not a protected branch
- Check that branch name matches expected format

### Reviewer not responding

If your reviewer hasn't responded within 2-3 business days:

- Send a polite ping in the MR comments: "@reviewer - gentle reminder for review when you have a moment"
- Reach out in the team Slack channel if urgent
- Request a different reviewer if the original is unavailable

### MR has been open too long

If an MR sits unmerged for extended periods:

- Resolve any open discussions
- Ping reviewers for final approval
- Rebase on latest master if conflicts develop
- Consider if the changes are still needed/relevant
- Close if no longer applicable

## Useful links

- [GitLab Merge Request documentation](https://docs.gitlab.com/ee/user/project/merge_requests/)
- [Customer Support Systems Coding Standards](/handbook/eta/css/resources/coding-standards)
- [Customer Support Systems Criticalities](/handbook/eta/css/criticalities/)
