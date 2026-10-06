---
title: "Demo Systems Onboarding"
description: "This guide is meant for getting any new hire to the CS Org set up on demo systems and prepared to start demoing the product. The full walkthroughs are maintained in the internal Demo Systems Initial Set Up project."
---

## Demo Systems Initial Set Up

### Preface

The full onboarding guide, including the current step-by-step walkthroughs, is maintained in the [Demo Systems Initial Set Up](https://gitlab.com/gitlab-com/customer-success/demo-engineering/demo-systems-initial-set-up) project (internal only). This page summarizes the environments and resources you need.

If you experience any roadblocks while setting up your environment, ask in the `#demo-architect-partners` Slack channel, open an [issue in the original project](https://gitlab.com/gitlab-com/customer-success/demo-engineering/demo-systems-initial-set-up/-/issues/new), or attend the office hours linked below.

The goal is that you will be able to use and contribute to the shared [gitlab-learn-labs/webinars](https://gitlab.com/gitlab-learn-labs/webinars) demo group by the time you complete this.

You can collaborate with your onboarding buddy and your colleagues to remove this blocker, and open a merge request to improve the instructions and make onboarding easier for everyone.

### Demo Systems & Shared Demos Office Hours

Feel free to join our bi-weekly office hours to ask any questions if you get stuck. There are EMEA/AMER and APJ sessions. Scheduling details are in the [office hours notes doc](https://docs.google.com/document/d/1foLXt9XIptbl4ZLmMWR_TzhvFHzdo6sp_2dkSVCWL20/edit) (internal only).

## Environments

You have access to three types of environments for performing demos.

### GitLab.com SaaS Groups

You will have two of your own groups on GitLab.com that allow you to showcase features with each SaaS license tier.

- `https://gitlab.com/gl-demo-ultimate-{handle}`
- `https://gitlab.com/gl-demo-premium-{handle}`

These groups should then be where you store all of your demo projects as they will not be constrained by the limitations of trying to just keep your demos in your personal namespace (ex. [Epics](https://docs.gitlab.com/ee/user/group/epics/#epics), [Security Dashboard](https://docs.gitlab.com/ee/user/application_security/security_dashboard/#gitlab-security-dashboards-and-security-center) and other [group features](https://docs.gitlab.com/ee/user/group/#groups)).

- [ ] **Action:** Do not try to create these groups yourself. Open an access request using the [GitlabCom_Licensed_Demo_Group_Request](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/issues/new?issuable_template=GitlabCom_Licensed_Demo_Group_Request) (internal only) template.

### Self-Managed Omnibus Shared Instances

You have access to an always-on GitLab Demo Cloud self-managed GitLab Omnibus instance that you have admin rights to for showing all of the features of the Admin UI that are not shown in GitLab SaaS. This also provides a backup for demos if something goes wrong with GitLab.com.

After you provision your credentials, log in and make sure your user can create top-level groups. In the Admin area, go to **Overview** > **Users**, select your own user, select **Edit**, and confirm **Can create top-level group** is checked. If it is not, check it for your own user only. You can then create your own top-level group to store your projects in, along with any test projects for learning if needed. This is a shared environment, so apart from that one setting on your own user, please do not change any admin-level settings so that you don't break another team member's demo.

- [ ] **Action:** Follow the [self-service instructions](/handbook/customer-experience/demo-systems/#access-shared-omnibus-instances) to request credentials for the Sales CS shared instance through the Demo Architect Portal.
- [ ] **Action:** Join the `#demo-architect-partners` Slack channel for announcements and a safe space to ask questions if you have any problems.

### Personal AWS Account and GCP Project

Each team member can use the [GitLab Sandbox Cloud](/handbook/company/infrastructure-standards/realms/sandbox/) to provision their own AWS account or GCP project for deploying infrastructure themselves.

> For the purposes of onboarding, we will focus on GCP. You will not need your AWS account right away, so you can always come back later.

- [ ] **Action:** Follow the [self-service instructions](/handbook/company/infrastructure-standards/realms/sandbox/#individual-aws-account-or-gcp-project) to provision a GCP project.
- [ ] **Action:** Follow the [self-service instructions](/handbook/company/infrastructure-standards/realms/sandbox/#individual-aws-account-or-gcp-project) to provision an AWS account.
- [ ] **Action:** Read about how [Terraform Environments](/handbook/company/infrastructure-standards/realms/sandbox/#terraform-environments) have been automated with the Sandbox Cloud and explore the [available templates](https://gitlab.com/gitlab-com/infra-standards/project-templates). You can follow the [self-service instructions](/handbook/company/infrastructure-standards/realms/sandbox/#how-to-create-a-terraform-environment) to create an environment using one of the templates or create any resources manually yourself in your AWS account or GCP project.

Please note that services may take a few minutes before being ready. If you log in and immediately see an error, wait a few minutes then try to access the account again.

You can ask for help from other peers in the `#sandbox-cloud-questions` or `#demo-architect-partners` Slack channels.

## Set Up the GitLab Agent for Kubernetes for Your Group

At this point you should have your own group on GitLab.com SaaS as well as a GCP project created using [gitlabsandbox.cloud](https://gitlabsandbox.cloud/cloud) (internal only).

The current step-by-step walkthrough, which creates a GKE Autopilot cluster, registers and installs the agent, configures the group-level CI/CD variables and ingress, and deploys a sample application, is maintained in the [Demo Systems Initial Set Up](https://gitlab.com/gitlab-com/customer-success/demo-engineering/demo-systems-initial-set-up) project (internal only). Allow about 75 minutes.

## Sample Demo Projects

### Adding Ready-To-Go Demos

- [ ] **Fork one demo into your personal ultimate group**

There is a shared demo group for webinars at [https://gitlab.com/gitlab-learn-labs/webinars](https://gitlab.com/gitlab-learn-labs/webinars) that you can fork projects out of and into your new ultimate group & have them running in under 5 minutes.

We suggest reading the [documentation](https://gitlab.com/gitlab-learn-labs/webinars/how-to-use-these-projects) about how these shared projects work. These demos are great because they all come with suggested talk tracks as well for how you might present the various topics.

By forking the project, you can use them how you want and then submit MRs to the original project to collaborate with others on fixing any bugs or adding any new features.

Learn more about setting up these demos at [gitlab.com/gitlab-learn-labs/webinars/how-to-use-these-projects](https://gitlab.com/gitlab-learn-labs/webinars/how-to-use-these-projects).

### Installing Personal GitLab Runners

- [ ] **Install GitLab Runners**

You only need to do this if you find yourself running out of shared runner minutes. It is typical that SAs + CSM/Es exhaust their quota of compute minutes. While installing and running a runner is an advanced topic, it is something that our customers ask a lot of questions about so it's best to be well versed on the topic. If you are brave you can [follow our docs](https://docs.gitlab.com/runner/install/) to set up the runner in a different way.

The current walkthrough, which creates a GCP VM, installs Docker and GitLab Runner, and creates and registers the runner, is maintained in the [Demo Systems Initial Set Up](https://gitlab.com/gitlab-com/customer-success/demo-engineering/demo-systems-initial-set-up) project (internal only). Allow about 45 minutes.

### Troubleshooting The Agent

If the agent or your deployments fail, see the troubleshooting section of the [Demo Systems Initial Set Up](https://gitlab.com/gitlab-com/customer-success/demo-engineering/demo-systems-initial-set-up) project (internal only). It covers the group-level `KUBE_CONTEXT` and `KUBE_INGRESS_BASE_DOMAIN` variables, agent connection and `config.yaml` errors, ingress IP delays, and image pull failures. You can also check the `#f_agent_for_kubernetes` Slack channel for ongoing issues or bring questions to the [office hours](#demo-systems--shared-demos-office-hours).

### Next steps

Now that you have your own instance and projects spun up, go ahead and try out some of the customer-facing workshops we put on. In the [Demo Architect Portal](https://cloud.gitlabdap.com/) (internal only), open **Content/Lab Request**, select **Customer Workshop/Lab**, choose an official course, and select **Internal training** on the request form. Do not select Self Paced Training (SPT), which is reserved for the paid offering. These workshops cover the basics of Advanced CI/CD and DevSecOps and are a good reference point for later.

### Additional Notes

- If a `Learn Labs Group` or `a group that was set up for you` is mentioned, this is your group that you created above.

- Both labs have a `Kubernetes Agent` section that you can skip over because we have already done that.

- Recordings have been provided for you to follow along with an Instructor if you would like, but keep in mind not to try to redeem a group at the start of the recording.

Official workshop content is in the Content Discovery section of the [Demo Architect Portal](https://cloud.gitlabdap.com/) (internal only).
