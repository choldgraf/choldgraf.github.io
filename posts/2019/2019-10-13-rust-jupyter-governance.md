---
tags: governance
title: What would Rust-style governance look like in Jupyter?
date: 2019-10-13
redirect: rust-jupyter-governance
---

# What would Rust-style governance look like in Jupyter?

As I've written about before, I [like Rust's governance structure](https://predictablynoisy.com/rust-governance).
I mean, who can't get behind a community that
[lists governance as a top-level page on its website](https://www.rust-lang.org/governance)?

Jupyter is currently in the middle of
[figuring out the next phase of its governance structure](https://discourse.jupyter.org/t/governance-office-hours-meeting-minutes/1480/26),
and so I have been thinking about
what this might look like. This post is a quick thought-experiment to explore what it'd mean
to port over Rust's governance directly into the Jupyter community.

*Note: I'm not an expert in Rust governance, so there are some assumptions made about its model
based on my outside perspective. Apologies if I miss any important details about the Rust model,
but this is mostly meant as as inspiration, not a report on Rust's governance :-)*

## A quick recap of Rust's governance structure

First off, how does Rust govern and organize itself? There are a few few
key pieces:

* Any significant changes to the codebase are proposed and discussed with a
  [Request for Comments process](https://github.com/rust-lang/rfcs).
* The Rust community is broken down into topic-specific teams. Each has a particular
  domain over which they make decisions. For a list of several teams, check out
  the [Rust governance page](https://www.rust-lang.org/governance/).
* There is also a core-team that cuts across topic teams and has representatives
  from each topic team, they discuss project-wide matters (but rarely).
* A new RFC is assigned a team, as well as a "shepherd" from that team. This person's
  job is to move the RFC process forward, not to comment on or implement the RFC.
* After a discussion period, all members of the sub-team must vote to enter
  a Final Comment Period. This should happen when "enough information is presented in
  the RFC to make a decision". It triggers a week-long review window.
* At the end of this window, a decision is made about what to do with the RFC. This
  is made by the members of the sub-team, who (I don't think) have any strict decision-making
  rules, they can organize themselves in terms of decision-making.
* If it is accepted, the RFC becomes "active" which is an invitation for people
  to work on implementing it.


## What would this look like in Jupyter?

Jupyter is a complex and multi-faceted community, but so is Rust, so let's see
what this decision-making structure would look like in the Jupyter community.

### General decision-making principles and goals

First off, we would adopt many of the same decision-making goals of the RFC
process. Here are a few key ones as I understand it:

* Be transparent - information about decision-making should be publicly available and
  easy to discover at any moment in time.
* Be inclusive - decision-making should strive to include many diverse voices in
  the conversation.
* Be informative - the goal of the RFC process is to surface relevant information
  and perspectives for making a decision.
* Be productive - the goal of the RFC process is to move ideas forward in the community.
  It should achieve a net-positive in "energy spent" vs. "generated value to the community".
* Be impactful - don't use RFCs to bike-shed minor details, or implementation details for a PR.
  They should be used for significant changes in a repository that require discussion at a high level.

### An RFC in the Jupyter Community

First off, the mechanism for proposing, iterating on, and making decisions. In
Rust this is an RFC. in Jupyter, such a mechanism has already been proposed!

The [Jupyter Enhancement Proposals](https://github.com/jupyter/enhancement-proposals)
have been around for quite some time, though have never been codified into law official
decision-making and have become a bit stale. I suspect this is partially because it's
unclear what kind of "power" the JEP process has.

Recently, [Safia](https://github.com/captainsafia) kick-started a process to
[revitalize the JEP process](https://github.com/jupyter/enhancement-proposals/pull/29), and
the proposed process is quite close to what the Rust community uses. I generally think
that this PR is a huge improvement, though for the sake of this thought experiment, I'm
just going to directly port over my understanding of Rust into this blog post.

Here's how a Rust-like process could work in Jupyter. Since already have JEPs, I'll
replace "RFC" with "JEP".

* We have a single "enhancement-proposals" repository where JEP discussion happens
* This repository has a template for new JEPs help people get started.
* New JEPs begin with general conversations in the community. People get informal
  buy-in and feedback through discussing in the [community forum](https://discourse.jupyter.org)
  or in GitHub repositories.
* If a person wants to make their JEP "official", they fill in the JEP template and
  make a pull-request to the repository.
* After an initial overview, a Jupyter team is assigned to the JEP.
* That team then picks a shepherd (how the teams do this is up to them).
* The shepherd oversees a process of feedback, asks for input from others in the
  community, and directs attention to the JEP on the listservs, community forum, etc.
* When the shepherd thinks that the JEP is ready for a decision, they ask their
  team to vote on whether it should enter a "final review" phase. No more modifications
  should be made to the JEP at this point.
* This triggers a 7-day window for team members to review the JEP. At the
  end of the 7 days, the team votes (say, by a lazy consensus with 50% quorum)
  on whether to accept the JEP.
* If accepted, the JEP enters an "active" state and pull-requests are welcome to
  implement it.

### The teams and peronnel needed to manage this process

The JEP process is the *mechanism* by which decisions get made, but what
are the groups that oversee this mechanism? In the Rust community,
these teams are broken down by either technical or community topics
(e.g., "compilers", "community", or "packaging"). The Jupyter community
similarly has several focus-groups that touch different parts of the
interactive computing stack. Here are a few core ones that basically already exist:

* **JupyterLab core**
* **JupyterHub core**
* **Infrastructure**
* **Community**
* **Events**

One could imagine beginning with this subset of teams, and adding others organically
over time. Each of the teams listed above would manage JEP processes for their respective
domain. They would be given a list of repositories (and maybe a GitHub organization)
to oversee, and when a new JEP came in, one of the the team members would be
chosen to shepherd the process. The team would be the definitive source of
decision-making for topics in that domain.

Here are a few others that come to mind - they're a bit less well-defined and might
be good candidates for team growth in the future.

* **The notebook specification**
* **Kernels and communication protocols**
* **Visualizations and widgets**
* **Publishing and document formats**
* **Data specifications**
* **Finance and accounting**
* **Technical accessibility**
* **Documentation**

There are a few other roles that would need to be created to facilitate this process:

* **A JEP communicator** - someone would need to manage the JEP infrastructure and process
  at a generic level. This doesn't mean getting involved in individual JEPs, but making sure
  the process as a whole is functioning, and potentially managing infrastructure around it
  (for example, maintaining a website that lists currently-active JEPs).
* **A core team** - would need to be created that cuts across the topic-specific teams.
  This team would exercise large-scale decisions within the community but generally
  rarely exercise their power. Similar to a BDFL.
* **A shepherd role** - we'd need to formalize what a "shepherd" is in the Jupyter community.
  Potentially sub-teams would modify this slightly to fit their own needs.


## What's the difference between current Jupyter and JEP Jupyter?

Thinking through the above scenario, I don't see too much distance between
our current situation and a JEP-like process. We:

* Already have *informal* topic groups, in the form of GitHub organizations,
  forum channels, and meetings (e.g. JupyterLab and JupyterHub come to mind).
* Already have a JEP repository with some past proposals in it.
* Already have the skeleton of a modernized JEP process thanks to Safia's awesome work.

What we'd need to do:

* more officially codify the JEP process
* make some topic-based teams official, and get people to accept roles on those teams
* build some infrastructure to support the JEP process (e.g. a website to make them searchable
  and discoverable)
* re-work team processes to encourage them to follow the JEP process over time (I suspect this would
  be the hardest thing to do)


## What's the difference between Jupyter and Rust?

Finally, while it's interesting to port one community's governance model directly onto another,
there are difference between the Jupyter and Rust projects, both technical and social ones.
Here are a few differences I can think of that might have an impact on how this model would work.

* **Jupyter evolves fairly quickly** - Whether it is JupyterLab development, the growth of new
  protocols or deployments in the JupyterHub stack, or extensions of Jupyter tools for new
  use-cases, Jupyter seems to move fairly quickly. The RFC (or JEP) model is one that intentionally
  slows things down, so perhaps we'd need to be more picky about when to follow such a model
  vs. when to allow codebases to grow more quickly.
* **Jupyter doesn't have a process like this already** - The recent JEP updates notwithstanding,
  Jupyter doesn't have a culture of following the JEP process already. This makes me think that
  adopting this process would need to be rolled out slowly over time, and in smaller increments
  in order to make sure teams buy-in to the process.
* **Jupyter doesn't have many official roles/titles** - Adding extra complexity to governance
  also adds extra responsibility and labor needed to manage that complexity. In order to
  ensure that the work gets done, and credit is given to those doing the work, we'd need to grow
  a culture of creating specific roles and responsibility for those roles.

## Wrapping up

I'm probably missing some things, but this seems like a reasonable plan! As I mentioned
above, this post has mostly been a thought-experiment, but if anybody has thoughts on bringing
this into the governance refactoring process, I'd be happy to talk more.