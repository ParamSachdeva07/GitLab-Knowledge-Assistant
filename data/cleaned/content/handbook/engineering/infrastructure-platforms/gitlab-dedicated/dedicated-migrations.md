---
title: Dedicated Migration Team
description: Team focused on smoothing the path of Geo migrations to Dedicated; tooling, process, and engineering
---

[[_TOC_]]

## Team Mission

Partner with the field, customers, and engineering to deliver seamless, fast, and reliable migrations. The team executes and improves processes to eliminate uncertainty and ensures readiness for cutover in Geo-based Dedicated migrations.

### Priorities

* Deliver and refine toolkits that include the documentation, templates, talk-tracks, and tooling to smoother Geo Dedicated migrations for ourselves and our customers
* Work with our engineering peers on features that enable self-serve customer migrations
* Deliver in-flight Geo migration engagements
* Enable our PS peers to deliver Geo migration engagements to scale up and out
* Delivery tooling and process to enable faster scoping and sizing for the field in the pre-sales process

### Team members

| Name          | Role                                 |
|---------------|--------------------------------------|
| Douglas Alexandre | Staff Backend Engineer           |
| Eren Akca     | Staff Migration Engineer             |
| Petar Prokić  | Staff Migration Engineer             |
| Jessykah Bird | Senior Migration Engineer            |
| Glen Miller   | Senior Manager, Software Engineering |

### Roles & Responsibilities

The team:

During the Geo migration portion of a Dedicated engagement, the team has the following responsibilities:

* Works directly with the field and customers to produce automated solutions for technical discovery, validation of data, and capacity planning of their target instance  
* Owns communications, providing internal and external alignment of plans, status, and timings  
* Owns Project Management alignment with the customer Project Planning Office for clear synchronization of activities, comms, timelines, and responsibilities  
* Enables confident production switchovers with minimal risk and maximum speed  

### Operating Principles

#### Customer-Centric Excellence

* **Clear Expectations First**: Every engagement begins with explicit alignment on migration cadence, platform capabilities, and service model boundaries  
* **Consultative Partnership**: We act as trusted advisors, not order-takers, providing honest guidance even when difficult  
* **Transparent Communication**: Regular, structured updates with no surprises \- customers always know where they stand

#### Technical Rigor

* **Discovery Before Design**: Comprehensive technical and business discovery drives all solution approaches  
* **Validation at Every Step**: Multi-layered validation ensures accuracy before any production changes  
* **Automation Where Possible**: Standardized, repeatable processes reduce risk and improve consistency

#### Structured Delivery

* **Milestone-Driven Progress**: Clear checkpoints with customer sign-off prevent scope creep and misalignment  
* **Risk-First Planning**: Identify and mitigate risks early rather than hope for the best  
* **Documentation as Code**: Every process, decision, and artifact is documented for repeatability and knowledge transfer

#### Continuous Improvement

* **Learning Organization**: Every project contributes to improved processes, tools, and methodologies  
* **Cross-Functional Collaboration**: Regular feedback loops with Engineering, Product, and Customer Success teams  
* **Scalable Solutions**: Build capabilities that enable future self-service and automation

#### Internal Alignment

* **One Team Approach**: Clear role definitions with flexible collaboration across disciplines  
* **Shared Accountability**: Success is measured at the team level, not individual contribution  
* **Proactive Communication**: Internal stakeholders are informed and aligned before customer commitments

#### Success Metrics

* To be aligned with larger team metrics in progress

## Process

### Engaging with Others

#### Geo Engagement Model For Dedicated Migrations

##### Support During a Cutover

Dedicated Migrations owns first-line troubleshooting during an execution. When Geo expertise is needed, try these in order:

1. The Geo engineer currently on the [support rotation](https://gitlab.com/groups/gitlab-org/geo-team/-/work_items/3#customersupport-rotation).
2. If that engineer is unavailable, including outside their working hours, one of the Geo for Self-Managed domain experts below.

No Geo engineer is pre-assigned to a cutover.

##### Geo for Self-Managed Domain Experts

These engineers previously worked on Geo and can help when the support rotation DRI is unavailable. This is a backup contact list, not an on-call schedule. Nobody on it is guaranteed to respond immediately or after hours, and they can say no if something else has priority. Their manager is listed for context if you need to escalate or can't reach them directly.

| Engineer | Manager |
|---|---|
| [Brian Legault](https://gitlab.com/brianlegault) | {{< manager-by-report-name "Brian Legault" >}} |
| [Douglas Alexandre](https://gitlab.com/dbalexandre) | {{< manager-by-report-name "Douglas Barbosa Alexandre" >}} |
| [Michael Kozono](https://gitlab.com/mkozono) | {{< manager-by-report-name "Michael Kozono" >}} |
| [Natanael Silva](https://gitlab.com/nsilva5) | {{< manager-by-report-name "Natanael Silva" >}} |
| [Victor Prêté](https://gitlab.com/victorprete) | {{< manager-by-report-name "Victor Prêté" >}} |

They are not part of the current Geo rotation. Log the problem, investigation, and outcome on the Dedicated Migrations work item or Geo support request issue, not Slack, so there's a durable record either way.

##### RFH Process

For sync issues outside the production cutover window, teams submit a [Geo Support Request](https://gitlab.com/gitlab-com/request-for-help/-/issues/new?issuable_template=SupportRequestTemplate-Geo) indicating priority (P1-P3), sync start time, cutover deadline, tenant, and request. These are triaged by the weekly customer support DRI. Geo engineers need access to Opensearch, Grafana, and ideally break glass access to support effectively.

| Priority | Description |
|----------|-------------|
| 1        | Immediate blocker to data sync or pre-production cutover. Cannot proceed without a fix |
| 2        | Needs to be solved before the end of the pre-production cutover phase, but not a blocker to start |
| 3        | Needs to be solved before production cutover. Can be handled within the production cutover support window |

#### SRE Engagement Model for Dedicated Migrations

##### Pre-production Cutover

A rotating team of SREs is assigned to the pre-production cutover. This is generally the same team that will support the production cutover. Pre-production cutover is often a more measured process that often runs for multiple days. It is where we map out any potential issues with the production cutover. Teams are not required to be on a call bridge. Execution, communication, and hand-overs can be coordinated in #g_dedicated-migrations channel and in the issues for the engagements in the [Dedicated Migrations](https://gitlab.com/gitlab-com/gl-infra/gitlab-dedicated/dedicated-migrations-group/dedicated-migrations) project

##### Production Cutover and Production Support Window

A team of SREs is assigned for a 2-week window around each migration: 1 week before, the migration weekend, and 1 week after. This is generally the same team that supported the pre-production cutover. The assigned SREs are to treat all migrations issues as Priority 1 during pre/post weeks. Communication can occur in the #g_dedicated-migrations channel and in the issues for the engagements in the [Dedicated Migrations](https://gitlab.com/gitlab-com/gl-infra/gitlab-dedicated/dedicated-migrations-group/dedicated-migrations) project

###### Migration Weekend Responsibilities

The assigned SREs are fully committed to migration issues via Slack during pre/post weeks and will alternate duties during cutover weekends based on their location/timezone. The SRE team will be responsible for executing scripts outside the permission framework of the Dedicated Migrations team, and assisting in troubleshooting of infrastructure (networking, nodes, configuration) concerns.

**Note** 

Many customers need to perform "catch-up" GitLab upgrades in the post-support window. The Dedicated Migrations team should be responsible for coordinating with the customer, scheduling, and executing on these upgrades, with support from the SRE team.

##### Outside the 2-Week Window

Support is primarily asynchronous via Request for Help (RFH) tickets. Per `@fviegas` all Dedicated Migrations RFH are considered priority 1. Synchronous customer calls are handled adhoc on a case-by-case basis, requiring approval from one of Matt Kirkevold/Oriol Lluch Parellada based on team availability.

##### RFH Process

For sync issues outside the dedicated window, teams submit a [Dedicated Support Request](https://gitlab.com/gitlab-com/request-for-help/-/work_items/new?description_template=SupportRequestTemplate-GitLabDedicated) indicating the tenant and request.

#### Scheduling

##### SRE and Geo Coverage

The engineering managers will coordinate finding the proper resources for cutover windows. When PMs have locked-in dates and times for cutovers, and need coverage confirmation, they can reach out to @glen_miller to coordinate with the other EMs. The EMs will use a single epic to track the coverage for each cutover slot.

* [FY27](https://gitlab.com/groups/gitlab-com/gl-infra/gitlab-dedicated/dedicated-migrations-group/-/work_items/179)

##### Cutover Slots

Geo migration cutover slots are currently a limited resource. Available slots can be referenced [here](https://docs.google.com/spreadsheets/d/1KRDNw2mXOSAc4DE1hceAWZTRqDGkoV-t5yNymKyXSIo/edit?gid=2116571451#gid=2116571451). Establishing these slots should be part of the pre-sales process. Work with your Dedicated PMs and EMs to reserve a slot.

###### Scheduling Cutover Slots

When scheduling cutover slots, the following guidelines apply:

* Cutover slots are scheduled on a first-come, first-served basis
* Slots are typically available on weekends to minimize customer impact
* Slots should be set at time of deal close. If not, they should be confirmed no later than 14 weeks before the slot date.
* Slots are confirmed only after SRE and Geo coverage is confirmed by the respective EMs

### Dedicated Migration Team Time Off

The Dedicated Migration team follows [GitLab's paid time off policy](/handbook/people-group/time-off-and-absence/).
We balance that with the need to deliver support to our customers every day.
This page is intended to provide an understanding of what we need to do to achieve that balance, making it possible for all to take time off as needed and desired, while we as a team continue to deliver for our customers.

#### One-time setup actions

##### Dedicated Migration Team calendar

1. Be sure you have access to the
[**Dedicated Migrations Team Calendar**](https://calendar.google.com/calendar/embed?src=c_fb53e24f590edfb8f313253126123e48d57254dd73266fae6547a2a4890b0c82%40group.calendar.google.com&ctz=America%2FVancouver)
team calendar.
   1. If you don't have it, verify whether you are part of the Dedicated Migrations Team (`dedicated-migrations-team@`) if you are not, ask to be added via an Access Request.

1. Set up the Google Calendar integration with Time Off by Deel, so that you do not need to populate your personal and "Dedicated Migrations Team" calendars manually.
   1. In Slack, click the `+` sign next to 'Apps' at the bottom of the left sidebar
   1. Search for 'Time Off by Deel' and click 'View'
   1. Under 'Home', click on 'Your Events' to show a dropdown
   1. Click on 'Calendar Sync' under the Settings break
   1. Click on 'Connect your Calendar' and complete the actions to sync your calendar to Time Off by Deel
      * You will see a 'Success! Your calendar has been connected.' message and
        your calendar listed under 'Your synced calendar' in Time Off by Deel on Slack
   1. After your personal calendar is linked, click 'Add calendar' under
   'Additional calendars to include?'. The 'Dedicated Migrations Team Calendar' calendar ID is
   `c_fb53e24f590edfb8f313253126123e48d57254dd73266fae6547a2a4890b0c82@group.calendar.google.com`

#### Choosing and recording time off

Please take time off whenever you need it.

A little thoughtfulness on everybody's part will go a long way toward making it
possible for everyone to take their desired days off. As you look to plan your
time off, please:

* Ensure you know the [company wide paid time off guidelines](/handbook/people-group/time-off-and-absence/time-away-philosophy/)
* Check the calendar and coordinate with the team to ensure we have sufficient cover for days with low availability.
* schedule your time off as far in advance as you can
* Don't lock yourself into nonrefundable travel itineraries before you've taken steps such as the above to be sure you can get the planned days off
* If possible, plan your time off to avoid disruptions

#### Communicate through a coverage issue

Please put together a [coverage issue](https://gitlab.com/gitlab-com/gl-infra/gitlab-dedicated/dedicated-migrations-group/pto-coverage/-/issues/new?description_template=pto_coverage) for any PTO longer than 5 days. Some Divisions may have other guidance (for example [Engineering PTO Coverage](/handbook/engineering/#taking-time-off)). Please follow your Division procedures if there is any conflict, and circulate with the team.

#### After PTO

See [returning from pto](/handbook/people-group/time-off-and-absence/time-away-philosophy/#transitioning-back-mindfully).

## Resources

* [GitLab group](https://gitlab.com/gitlab-com/gl-infra/gitlab-dedicated/dedicated-migrations-group)
* [GitLab project](https://gitlab.com/gitlab-com/gl-infra/gitlab-dedicated/dedicated-migrations-group/dedicated-migrations)
* [Migrating Customers to Dedicated internal documentation](https://internal.gitlab.com/handbook/engineering/dedicated/migrating-customers-to-dedicated/)
* [Cutover Cancellation Impact](https://drive.google.com/drive/folders/12GInLFxnT5BPbPJh1JsemUE089-Ctj0e)
