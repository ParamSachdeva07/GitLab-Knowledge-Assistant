---
title: "GitLab Fundamentals - Hands-On Lab: Collaboration and Code Review"
description: "This Hands-On Guide walks you through collaborating on changes and creating code reviews."
---

> Estimated time to complete: 30 minutes

## Objectives

In this lab, we will explore the process of creating and merging a merge request.

## Task A. Creating a merge request

In the last lab, you created a new branch called **test-commit**. In this section, we will create a merge request to merge the changes from that branch into our main branch.

1. Navigate to your `Cool App QA` project.

1. In the left sidebar, select **Code > Branches**.

1. In the **test-commit** row, select **New**.

1. In the **Title** field, enter the title **Merging new file to main**.

1. Check the box **Mark as draft**. This will mark the merge request as a draft, and prevent it from being merged until the Draft status is removed.

1. In **Description**, enter any description you would like.

1. In **Assignees**, select **Assign to me**.

1. Leave all other options as default and select **Create merge request**.

After selecting **Create merge request**, you will be redirected to the merge request page. Let's explore this page in more detail.

## Task B. Exploring the merge request

On the main merge request page, you will see four tabs available:

- **Overview**, which shows an overview of the merge request, including approvals, merge request status, **Activity**, and a comment area to add comments to a merge request.

- **Commits**, which shows all of the commits that are part of the current merge request.

- **Pipelines**, which shows any CI/CD pipelines associated with a merge request.

- **Changes**, which shows a differential of the changes associated with the merge request.

Return to the **Overview** tab. In this tab, there are a few important details to note. In the right sidebar, you will see details about your merge request. The merge request is currently assigned to you, meaning you are the one currently working on the merge request contents.

There are also the following pieces of metadata:

- **Assignees** are the individuals directly responsible for updating the content in the merge request.

- **Reviewers** shows any reviewers that have been assigned to a merge request. Currently this is empty, since approval is optional.

- **Labels** allows you to add organizational labels to a merge request to keep track of it in context of other related work.

- **Milestone** allows you to associate a milestone to a merge request.

- **Time Tracking** lets you track time spent on a merge request, as well as the total amount of time expected to spend on a merge request.

- **Participants** shows everyone who has commented on, been mentioned in, or made a commit on a merge request.

## Task C. Performing a review

Let's add some code to our branch, and then go through the process of reviewing it.

1. From the merge request, click the **Code** dropdown list and select **Open in Web IDE**.

1. Select the **New file** button near the top-left of your screen, and add a file called `index.js`.

1. Paste the following code into the file:

      ```js
          const http = require('http');

          var users = [
          { id: 1, name: 'Alice', password: 'password123' },
          { id: 2, name: 'Bob', password: 'admin' }
          ];

          const server = http.createServer((req, res) => {
          res.statusCode = 200;

          if (req.url === '/') {
              res.setHeader('Content-Type', 'text/html');
              res.end('<h1>Welcome to My App!</h1><p>Visit /users to see all users</p>');
          } else if (req.url === '/users') {
              res.setHeader('Content-Type', 'application/json');
              res.end(JSON.stringify(users));
          } else if (req.url.startsWith('/user/')) {
              const userId = req.url.split('/')[2];
              const user = users[userId - 1];
              res.setHeader('Content-Type', 'application/json');
              res.end(JSON.stringify(user));
          } else {
              res.statusCode = 404;
              res.end('Not Found');
          }
          });

          const PORT = 3000;
          server.listen(PORT, () => {
          console.log(`Server running at http://localhost:${PORT}/`);
          });
      ```

      > Don't worry too much about what the code is doing right now - it is creating a website that displays all users of the application.

1. Select the **Source control** button on the left-hand side of the page, and commit this code to your new branch.

    > Let's now take our 'developer' hats off, and put our 'reviewer' hats on to review this code.

1. Navigate back to the merge request, and select the **Changes** tab.

1. Notice that when you hover over a line of code on this tab, you get the option to add a review comment.

1. Leave some comments on a couple of lines of the new code (anything you like), making sure to select the **Start a review** button instead of **Add comment now** for the first comment, and then pressing **Add to review** for all your subsequent comments.

1. Once you have finished your review, select the **Your review** button near the top-right corner of your screen, then select **Submit review** to submit your review comments.

1. Your review comments are now published, and can be seen by anyone on the merge request by navigating to the **Overview** tab.

## Task D. An Agentic review

Now let's see if GitLab Duo agrees with our review comments!

GitLab Duo is our in-built AI feature set. It can do many things for us: write code, check the security health of our code, help us plan our work, and also review our code for good writing practice. The latter use case is what we are going to put into practice now.

1. To get GitLab Duo to perform a code review, navigate to the **Overview** tab of the merge request.

1. In the **Reviewers** metadata section on the right-hand side of the merge request, select **Edit** and then select the **GitLab Duo** account.

      > This will trigger a GitLab Duo Code Review session.

1. Give Duo a minute or two to perform its review.

1. Once it has finished, you will see that Duo has added some review comments to the **Changes** tab of the merge request just like you did. These comments will also appear on the **Overview** tab just under yours.

1. Feel free to make any changes to the code based on Duo's suggestions, using the Web IDE from the merge request the same way you did earlier.

## Task E. Merging the MR

1. Navigate back to the **Overview** tab of your merge request.

      > In the center of the screen, you will see a message stating **Merge blocked**. In this section, you can see any issues preventing your code from being merged into main. Anything from failed pipelines to security scan results can block a merge request, depending on your configuration. Currently, the reason to request is blocked is stated below: "Merge request must not be a draft". Let's fix this issue.

1. Click **Mark as ready** in the **Merge blocked** block. If you do not see the **Mark as ready** option, click on the arrow to the right of the **Merge blocked** block to expand it.

1. Select **Merge**.

1. Once the merge completes, in the left sidebar, select **Code > Repository**.

You will now see your new file in the **main** branch of your code repository.

## Lab Guide Complete

You have completed this lab exercise. You can view the other [lab guides for this course](/handbook/customer-experience/professional-services-engineering/education-services/ilt-labs/gitlabfundamentalshandson).

## Suggestions?

If you wish to make a change to this lab, please submit your changes through a Merge Request.
