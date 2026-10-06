---
title: "GitLab System Admin - Hands-On Lab: Troubleshooting GitLab Kubernetes"
description: "This Hands-On Guide demonstrates how to troubleshoot your GitLab Kubernetes instance"
---

> Estimated time to complete: 30 minutes

## Objectives

The objective of this lab is to demonstrate how to troubleshoot common issues in a GitLab Kubernetes deployment using logs and diagnostic tools.

## Task A. Issues at the reverse proxy

1. From a shell session on your GitLab instance, find the Webservice pod and view its logs.

      ```bash
      kubectl get pods | grep webservice
      kubectl logs <webservice-pod-name> -c gitlab-workhorse --tail=10
      ```

      > Note: The Webservice pod contains multiple containers. Use `-c gitlab-workhorse` to see workhorse/nginx logs, or `-c webservice` to see Rails logs.

1. After typing this, navigate to your GitLab instance and try accessing various pages on the instance. Note how each request has an NGINX log message associated with it.

1. Let's cause an error in the NGINX service. Stop the NGINX service using the following command:

      ```bash
      kubectl scale deploy -lapp=webservice,release=gitlab --replicas=0
      ```

1. Attempt to navigate to `http://<your_gitlab_instance>` using a web browser. Your web browser should display "**This site can't be reached**" or a similar message.

1. Try to check the logs again (this will fail since the pod no longer exists).

      ```bash
      kubectl logs <webservice-pod-name> -c gitlab-workhorse
      ```

      > Take note that no new log messages have appeared in these logs. Since NGINX cannot be reached, it cannot log the access request. In this case, we can immediately understand that Nginx has an issue.

1. Verify no Webservice pods are running.

      ```bash
      kubectl get pods | grep webservice
      ```

      > Note: You should see no Webservice pods in the output.

1. Restart NGINX services.

      ```bash
      kubectl scale deploy -lapp=webservice,release=gitlab --replicas=1
      ```

1. Wait for the pod to be ready and view the logs to verify that it's now receiving requests.

      ```bash
      kubectl wait --for=condition=ready pod -lapp=webservice --timeout=60s
      kubectl get pods | grep webservice
      kubectl logs <new-webservice-pod-name> -c gitlab-workhorse --tail=5
      ```

1. Verify the Webservice pod is running.

      ```bash
      kubectl get pods -lapp=webservice
      ```

## Task B. Tracing issues at the GitLab Rails level

For this example, let's suppose that an issue occurred in GitLab Rails. To simulate this:

1. The first location that requests reach is the workhorse/nginx layer. Let's look at the workhorse logs:

      ```bash
      kubectl logs <webservice-pod-name> -c gitlab-workhorse --tail=20
      ```

1. In this output, search for your HTTP request. It will look something like this:

      ```bash
      173.34.175.144 - - [25/Oct/2024:14:48:00 +0000] "GET / HTTP/1.1" 502 2026 "http://34.56.107.198/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36" -
      ```

      > We can tell this is the request based on the URL being accessed and the NGINX status code. This status code is a 502 and the request is to the root of the web application.

1. The workhorse logs show requests with correlation IDs. Note the correlation ID from a request (for example `01JB22H7ENN72DH5XNMTB2170Z`).

1. In this output, look for the request that matches the URL of your `NGINX` request. It will look like this:

      ```json
      {"backend_id":"rails","content_type":"text/html; charset=utf-8","correlation_id":"01JB22H7ENN72DH5XNMTB2170Z","duration_ms":0,"host":"34.56.107.198","level":"info","method":"GET","msg":"access","proto":"HTTP/1.1","referrer":"http://34.56.107.198/","remote_addr":"173.34.175.144:0","remote_ip":"173.34.175.144","route":"","route_id":"default","status":502,"system":"http","time":"2024-10-25T14:50:49Z","ttfb_ms":0,"uri":"/favicon.ico","user_agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36","written_bytes":2026}
      ```

      > In this request, we can collect some additional important details. We can see our request was sent to rails. If the request reached rails, we can use the `correlation_id` to locate it in the logs. Let's take note of the correlation ID and search for it in the Rails log.

1. To view the log for your Rails application, run the command:

      ```bash
      kubectl logs <webservice-pod-name> -c webservice --tail=20
      ```

1. These logs have a lot of data. To search for a correlation ID in the Rails logs:

      ```bash
      kubectl logs <webservice-pod-name> -c webservice | grep -i <your-correlation-id>
      ```

1. You will get no results. This tells you the GitLab Rails did not receive the request from Workhorse. From here, we can diagnose the issue with rails, starting by looking at the status:

      ```bash
      kubectl get pods
      ```

## Task C. Collecting SOS

In some cases, troubleshooting will require the assistance of GitLab Support. To help GitLab Support troubleshoot any errors, it is helpful to provide a full account of your instance logs. For this purpose, you can use the GitLab SOS tool.

1. To run GitLab SOS, use the following commands:

      ```bash
      curl -s https://gitlab.com/gitlab-com/support/toolbox/kubesos/raw/main/kubeSOS.sh | bash -s -- -r gitlab
      ```

1. After the run completes, you will see the location of your support bundle, in the form of `./kubesos-TIMESTAMP.tar.gz`.

      > When you file support requests, you can attach this bundle to provide all of your instance logs.

## Lab Guide Complete

You have completed this lab exercise. You can view the other [lab guides for this course](/handbook/customer-experience/professional-services-engineering/education-services/ilt-labs/sysadminhandsonk8s).

## Suggestions?

If you wish to make a change to this lab, please submit your changes through a Merge Request.
