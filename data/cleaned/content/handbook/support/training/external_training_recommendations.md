---
title: External Training Recommendations
description: Recommended courses, learning paths and certifications from external training partners for Support Engineers
---

This page recommends specific courses, learning paths and certifications from GitLab's external training partners that are relevant to Support Engineers. The recommendation is to first complete the internal [Support Training modules](/handbook/support/training/) and [specialised domain tracks](/handbook/support/training/specialised_domain_tracks/), then use the resources below to supplement that knowledge or move into intermediate and advanced levels within a specific area.

Recommendations are split into two broad categories:

1. **General technical skills**: Linux, networking, containers, Kubernetes, Git internals, databases and observability
1. **GitLab-specific skills**: Ruby on Rails, Go (Gitaly and GitLab Runner), PostgreSQL, CI/CD concepts and Helm chart deployments

Each section notes the platform, the access method (request or free) and a suggested priority for Support Engineers. Costs for external training may be covered through the [Growth and Development Fund](/handbook/people-group/learning-and-development/growth-and-development/). If you're interested in pursuing any paid resources, discuss it with your manager in your next 1:1.

## Quick reference: access methods by platform

| Platform | Access method | Notes |
|---|---|---|
| [LevelUp](/handbook/people-group/learning-and-development/level-up/) | Free (internal) | GitLab's own learning platform |
| [Hone](/handbook/people-group/learning-and-development/hone/) | Individual team members require request/approval | Live classes; leadership and soft skills focus |
| [O'Reilly Learning](/handbook/people-group/learning-and-development/self-paced-learning/#oreilly-learning) | Engineering: request; Non-Engineering: expense | Books, videos, interactive sandboxes, live events |
| [Google Cloud Skills Boost](/handbook/people-group/learning-and-development/self-paced-learning/#google-cloud-skills-boost-learning) | Requires request | Labs, courses and certification paths on GCP |
| Codecademy | Free tier available | Interactive code-based learning; Ruby, Go, SQL, Python, Bash |

## Part 1: General technical skills

These are foundational skills that every Support Engineer benefits from, regardless of which GitLab product areas they focus on.

### Linux system administration

Support Engineers regularly troubleshoot GitLab Self-Managed instances running on Linux. Strong Linux fundamentals are essential for reading logs, understanding process management, debugging networking issues and navigating the filesystem.

#### Linux Foundation (request/approval)

| Title | Type | Level |
|---|---|---|
| [LFS101 - Introduction to Linux](https://training.linuxfoundation.org/training/introduction-to-linux/) | Course | Beginner |

#### O'Reilly Learning

| Title | Type | Level |
|---|---|---|
| [Learning Modern Linux](https://www.oreilly.com/library/view/learning-modern-linux/9781098108939/) - Michael Hausenblas | Book | Beginner |
| [How Linux Works, 3rd Edition](https://learning.oreilly.com/library/view/-/9781098128913/) - Brian Ward | Book | Beginner-Intermediate |
| [The Linux Command Line, 2nd Edition](https://www.oreilly.com/library/view/the-linux-command/9781492071235/) - William E. Shotts | Book | Beginner |
| [Linux Foundation Certified System Administrator (LFCS), 3rd Edition](https://learning.oreilly.com/videos/-/9780138230678/) - Sander van Vugt | Course (20h) | Intermediate |
| [LPIC-1 Linux Administrator (101-500)](https://learning.oreilly.com/videos/-/9781835885406/) - ACI Learning | Course (12h) | Intermediate |

### Git internals

Support Engineers troubleshoot Git operations daily: push/pull failures, repository corruption, merge conflicts, LFS issues and server-side hooks. Understanding Git internals (packfiles, refs, objects, transfer protocols) is directly applicable.

#### Linux Foundation

| Title | Type | Level |
|---|---|---|
| [LFD109 - Git for Distributed Software Development](https://training.linuxfoundation.org/training/git-for-distributed-software-development-lfd109x/) | Course | Beginner |

#### O'Reilly Learning

| Title | Type | Level |
|---|---|---|
| [Pro Git, 2nd Edition](https://git-scm.com/book/en/v2) - Scott Chacon, Ben Straub | Book | All levels |
| [Version Control with Git, 3rd Edition](https://www.oreilly.com/library/view/version-control-with/9781492091189/) - Prem Kumar Ponuthorai, Jon Loeliger | Book | Intermediate |
| [Head First Git](https://www.oreilly.com/library/view/head-first-git/9781492092506/) - Raju Gandhi | Book | Beginner |
| [Complete Git Guide: Understand and Master Git and GitHub](https://learning.oreilly.com/videos/-/9781800209855/) - Bogdan Stashchuk | Course (22h) | All levels |

### Containers and Docker

GitLab Runner uses Docker executors, GitLab.com and Dedicated uses Kubernetes, and many Self-Managed customers use container-based deployments. Understanding container fundamentals is important for debugging CI/CD job failures, registry issues and deployment problems.

#### O'Reilly Learning

| Title | Type | Level |
|---|---|---|
| [Docker Deep Dive](https://www.oreilly.com/library/view/docker-deep-dive/9781835081709/) - Nigel Poulton | Book | Beginner |
| [Docker: Up and Running, 3rd Edition](https://www.oreilly.com/library/view/docker-up/9781098131814/) - Sean P. Kane, Karl Matthias | Book | Intermediate |
| [Docker and Kubernetes Masterclass: From Beginner to Advanced](https://learning.oreilly.com/videos/-/9781837025077/) - LM Academy | Course (32h) | All levels |
| [Introduction to Docker and Containers](https://learning.oreilly.com/videos/-/9780138174309/) - Noureddin Sadawi | Course (5h) | Beginner |

### Kubernetes

GitLab can be deployed via the official Helm chart on Kubernetes, and GitLab.com itself runs on GKE. Support Engineers regularly troubleshoot Helm chart deployments, pod failures, ingress configuration, certificate issues and resource limits.

#### Linux Foundation

| Title | Type | Level |
|---|---|---|
| [LFS158 - Introduction to Kubernetes](https://training.linuxfoundation.org/training/introduction-to-kubernetes/) | Course | Beginner |

#### O'Reilly Learning

| Title | Type | Level |
|---|---|---|
| [Kubernetes: Up and Running, 3rd Edition](https://www.oreilly.com/library/view/kubernetes-up-and/9781098110192/) - Brendan Burns, Joe Beda, Kelsey Hightower, Lachlan Evenson | Book | Intermediate |
| [Kubernetes Patterns, 2nd Edition](https://www.oreilly.com/library/view/kubernetes-patterns-2nd/9781098131678/) - Bilgin Ibryam, Roland Huss | Book | Intermediate-Advanced |
| [Kubernetes for the Absolute Beginners - Hands-On](https://learning.oreilly.com/videos/-/9781838555962/) - KodeKloud (Mumshad Mannambeth) | Course (5h) | Beginner |
| [Docker and Kubernetes Masterclass: From Beginner to Advanced](https://learning.oreilly.com/videos/-/9781837025077/) - LM Academy | Course (32h) | All levels |

#### Google Cloud Skills Boost

| Title | Type | Level |
|---|---|---|
| [Getting Started with Google Kubernetes Engine](https://www.cloudskillsboost.google/course_templates/2) | Course | Beginner |
| [Architecting with Google Kubernetes Engine (series)](https://www.skills.google/course_templates/32) | Course | Intermediate |
| [Deploy Kubernetes Applications on Google Cloud](https://www.cloudskillsboost.google/course_templates/663) | Skill Badge | Intermediate |

### Networking

Networking issues are among the most common and complex problems in Support: DNS resolution failures, proxy and load balancer misconfigurations, TLS/SSL certificate problems, firewall rules blocking traffic and SSH connectivity issues.

#### O'Reilly Learning

Networking is covered well within the Linux books already recommended:

1. *How Linux Works, 3rd Edition* chapters 9-10 cover TCP/IP, DNS, firewalls, DHCP, NAT and routing
1. *Learning Modern Linux* chapter 7 covers the networking stack, DNS, SSH and Wireshark

| Title | Type | Level |
|---|---|---|
| [Networking Fundamentals](https://learning.oreilly.com/videos/-/9780134645711/) - Kevin Wallace | Course (6h) | Beginner |

#### Google Cloud Skills Boost

| Title | Type | Level |
|---|---|---|
| [Networking in Google Cloud: Fundamentals](https://www.cloudskillsboost.google/course_templates/35) (multi-module) | Course | Intermediate |
| [Build a Secure Google Cloud Network](https://www.cloudskillsboost.google/course_templates/654) | Skill Badge | Intermediate |
| [Develop Your Google Cloud Network](https://www.cloudskillsboost.google/course_templates/625) | Skill Badge | Intermediate |

### Observability: Prometheus, Grafana and logging

GitLab ships with built-in Prometheus metrics and Grafana dashboards. Support Engineers use these to diagnose performance problems, identify resource bottlenecks and understand system behaviour during incidents.

#### O'Reilly Learning

1. *Learning Modern Linux* chapter 8 covers Prometheus, Grafana and observability strategy
1. [*Prometheus: Up and Running, 2nd Edition*](https://www.oreilly.com/library/view/prometheus-up-and/9781098131135/) by Julien Pivotto and Brian Brazil (O'Reilly)

#### Google Cloud Skills Boost

| Title | Type | Level |
|---|---|---|
| [Logging and Monitoring in Google Cloud](https://www.cloudskillsboost.google/course_templates/99) | Course | Intermediate |

### DevOps and SRE concepts

Understanding DevOps and SRE principles helps Support Engineers contextualise customer workflows and speak the same language as the teams they support.

#### Linux Foundation

| Title | Type | Level |
|---|---|---|
| [LFS162 - Introduction to DevOps and Site Reliability Engineering](https://training.linuxfoundation.org/training/introduction-to-devops-and-site-reliability-engineering-lfs162/) | Course | Beginner |
| [LFS169 - Introduction to GitOps](https://training.linuxfoundation.org/training/introduction-to-gitops-lfs169/) | Course | Beginner |

#### Google Cloud Skills Boost

| Title | Type | Level |
|---|---|---|
| [Professional Cloud DevOps Engineer learning path](https://www.cloudskillsboost.google/paths/20) | Course | Advanced |

## Part 2: GitLab-specific skills

These skills relate directly to the technologies that GitLab is built on. They help Support Engineers read and understand the GitLab codebase, debug application-level issues and work more effectively with development teams.

### Ruby and Ruby on Rails

GitLab's core application is a Ruby on Rails monolith. While Support Engineers are not expected to write production Ruby code, being able to read Rails controllers, models and service objects is extremely valuable for:

1. Understanding how a feature works when the documentation is unclear
1. Tracing the root cause of a bug through the codebase
1. Writing more accurate and useful bug reports for development teams
1. Understanding error messages and stack traces in logs

#### Codecademy (free courses)

| Title | Type | Level |
|---|---|---|
| [Learn Ruby](https://www.codecademy.com/learn/learn-ruby) | Course (9h) | Beginner |

#### O'Reilly Learning

| Title | Type | Level |
|---|---|---|
| [The Well-Grounded Rubyist, 3rd Edition](https://www.oreilly.com/library/view/the-well-grounded-rubyist/9781617295218/) - David A. Black, Joe Leo | Book | Beginner-Intermediate |
| [Agile Web Development with Rails 8](https://learning.oreilly.com/library/view/-/9798888651766/) - Sam Ruby et al. | Book | Intermediate |
| [Programming Ruby 3.3, 5th Edition](https://learning.oreilly.com/library/view/-/9798888650684/) - Noel Rappin, Dave Thomas | Book | All levels |
| [Ruby on Rails Tutorial, 7th Edition](https://learning.oreilly.com/library/view/-/9780138050061/) - Michael Hartl | Course (21h) | Intermediate |

### Go

Gitaly (the Git RPC service) and GitLab Runner are both written in Go. Support Engineers encounter Go stack traces in Gitaly logs and Runner debug output. Being able to read Go code helps with:

1. Understanding Gitaly error messages and behaviour
1. Debugging GitLab Runner executor issues
1. Reading and understanding Gitaly and Runner source code when investigating bugs

#### Codecademy (free courses)

| Title | Type | Level |
|---|---|---|
| [Learn Go](https://www.codecademy.com/learn/learn-go) | Course (6h) | Beginner |
| [Learn Go: Fundamentals](https://www.codecademy.com/learn/learn-go-fundamentals) | Course (2h) | Beginner |
| [Learn Go: Functions](https://www.codecademy.com/learn/learn-go-functions) | Course (1h) | Beginner |
| [Learn Go: Loops, Arrays, Maps, and Structs](https://www.codecademy.com/learn/learn-go-loops-arrays-maps-and-structs) | Course (4h) | Beginner |
| [Learn Go: Interfaces](https://www.codecademy.com/learn/learn-go-interfaces) | Course (2h) | Beginner |

#### O'Reilly Learning

| Title | Type | Level |
|---|---|---|
| [Learning Go, 2nd Edition](https://www.oreilly.com/library/view/learning-go-2nd/9781098139285/) - Jon Bodner | Book | Beginner-Intermediate |
| [The Go Programming Language](https://www.oreilly.com/library/view/the-go-programming/9780134190570/) - Donovan and Kernighan | Book | Intermediate |
| [Concurrency in Go](https://www.oreilly.com/library/view/concurrency-in-go/9781491941294/) - Katherine Cox-Buday | Book | Intermediate-Advanced |
| [Golang: Hands-on Programming for Beginners](https://learning.oreilly.com/videos/-/9781806386253/) - KodeKloud (Priyanka Yadav) | Course | Beginner |

### PostgreSQL

PostgreSQL is GitLab's primary datastore. Support Engineers regularly help customers with database performance issues, migration failures, replication problems, Patroni/PgBouncer configuration and backup/restore procedures.

#### Codecademy (free courses)

| Title | Type | Level |
|---|---|---|
| [Learn SQL](https://www.codecademy.com/learn/learn-sql) | Course (5h) | Beginner |
| [Learn SQL: Multiple Tables](https://www.codecademy.com/learn/learn-sql-multiple-tables) | Course (1h) | Beginner |
| [Learn SQL: Aggregate Functions](https://www.codecademy.com/learn/learn-sql-aggregate-functions) | Course (1h) | Beginner |

#### O'Reilly Learning

| Title | Type | Level |
|---|---|---|
| [PostgreSQL: Up and Running, 3rd Edition](https://learning.oreilly.com/library/view/-/9798341660885/) - Regina Obe, Leo Hsu | Book | Beginner-Intermediate |
| [Learn PostgreSQL, 2nd Edition](https://learning.oreilly.com/library/view/-/9781837635641/) - Luca Ferrari, Enrico Pirozzi | Book | Beginner |
| [High Performance PostgreSQL](https://learning.oreilly.com/library/view/-/9798888651070/) | Book | Advanced |
| [PostgreSQL Essentials: Leveling Up Your Data Work](https://learning.oreilly.com/videos/-/0790145594945/) - Haki Benita | Course | Intermediate |

### Python and Bash scripting

Python and Bash are useful for writing automation scripts, parsing logs, interacting with the GitLab API and building internal tooling.

#### Codecademy (free courses)

| Title | Type | Level |
|---|---|---|
| [Python for Programmers](https://www.codecademy.com/learn/python-for-programmers) | Course (3h) | Intermediate |
| [Intro to the Command Line](https://www.codecademy.com/learn/intro-to-the-command-line) | Course (1h) | Beginner |

### Cloud platforms (GCP focus)

Many GitLab customers deploy on GCP, AWS or Azure. GitLab Dedicated runs on GCP and AWS. Understanding cloud fundamentals helps Support Engineers advise customers on infrastructure-related issues.

#### Google Cloud Skills Boost

| Title | Type | Level |
|---|---|---|
| [Google Cloud Fundamentals: Core Infrastructure](https://www.cloudskillsboost.google/course_templates/60) | Course | Beginner |
| [Associate Cloud Engineer learning path](https://www.cloudskillsboost.google/paths/11) | Course | Intermediate |
| [Develop Your Google Cloud Network](https://www.cloudskillsboost.google/course_templates/625) | Skill Badge | Intermediate |
| [Getting Started with Google Kubernetes Engine](https://www.cloudskillsboost.google/course_templates/2) | Course | Beginner |
| [Networking in Google Cloud: Fundamentals](https://www.cloudskillsboost.google/course_templates/35) | Course | Intermediate |
| [Logging and Monitoring in Google Cloud](https://www.cloudskillsboost.google/course_templates/99) | Course | Intermediate |

#### O'Reilly Learning

| Title | Type | Level |
|---|---|---|
| [Terraform: Up and Running, 3rd Edition](https://www.oreilly.com/library/view/terraform-up-and/9781098116736/) - Yevgeniy Brikman | Book | Intermediate |

## Part 3: Soft skills and leadership (Hone)

[Hone](/handbook/people-group/learning-and-development/hone/) offers live, cohort-based classes focused on professional development. While not technical, these skills are valuable for Support Engineers who collaborate across teams, mentor colleagues and communicate with customers.

Relevant class categories include:

1. **Communication skills**: giving and receiving feedback, difficult conversations, written communication
1. **Collaboration**: working across teams, influencing without authority
1. **Time management and productivity**: prioritisation, managing workload
1. **Career development**: goal setting, self-advocacy
