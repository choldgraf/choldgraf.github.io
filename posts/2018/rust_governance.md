---
tags: python, governance, community
permalink: rust-governance
category: open source
date: 2018-10-18
---

# I like Rust's governance structure

Recently I've been reading up on governance models for several large-ish open
source projects. This is partially because I'm involved in a bunch of
these projects myself, and partially because it's fascinating to see distributed groups
of people organizing themselves in effective (or not) ways on the internet.

## Why is governance in open projects important?

Governance is tricky, because there is an inherent tension between:

* Being able to make important, complex, or sensitive decisions quickly
* Being transparent and inclusive in the decision-making process

For most companies and organizations, the above is (sort-of) solved with a relatively
hierarchical decision-making structure. The "Chief Executive Officer" can
decide high-level directions for the whole company. The team manager can
define the priorities for the group.

This generally isn't the case in open-source, where nobody is beholden to the
opinion of anybody else. In this case, leading and decision-making are done
by persuading others and building coalitions. The effects of this difference often
aren't felt in the early days of an open-source project, when the team is
small, everybody knows one another, and developers often have the same perspective.
However, as a project grows in its size and complexity, it becomes more important
to create an organizational structure that recognizes, manages, and *leverages* that complexity.

So, this is why I like Rust's governance model.

I won't go into detail about what "Rust" is, except to say that it's an open-source
language that has had a lot of support from the Mozilla foundation. In this case,
I'm less interested in the specific technical pieces of that project, and want
to focus on the people and the organizations in it.

![Rust teams](/images/2018/2018-10-19-rust_logo.png)


Here's the challenge that the Rust community faces:

Because Rust is an open-source language, it has a lot of technical pieces to it that
are very diverse in the kinds of demands they have. People working on low-level kernel
implementation will have a different perspective from those designing libraries for
the language. Moreover, because this language is used by many organizations, there's
a strong diversity in the type of user that make up the Rust community. A open-source
lead in a company has a different incentive structure than a researcher at a university.

This means that a single decision-making body would

1. have most of its members unable
to make strong technical decisions about most of the sub-communities within Rust (e.g.,
a libraries and APIs person making decisions about kernel implementations).
2. would be susceptible to inertia in decision-making because of the size needed to represent
all of the Rust community with a single group of people.
3. would probably be skewed towards one set of decisions over another (since whoever was
   most powerful within this group would set the "agenda" for the whole project)

So, here are two ways that Rust tries to address this problem:

1. Divide the governance structure into sub-teams and a "core" team.
2. Use an explicit "Request for Comments" process to handle all non-trivial decisions.

I'll describe each of these as I understand them so far:

## The Rust Governance structure - sub-teams and communities

The Rust governance structure is based on the idea that most decisions should
not need to be escalated to the highest decision-making authority in the community.
Moreover, these decisions need to be made by people with a keen understanding of the
details of the problem. Finally, these problems are *not just technical in nature*, but
also span community operations, organization, communication, etc.

So, Rust is divided into sub-teams that are broken down by topic. By my count, there are
**15 teams** in total. Each team is tasked with a specific **responsibility** to
oversee in the Rust community. For example, the *language team* is responsible for
*designing new language features*. The *release team* is responsible for
*tracking regressions, stabilizations, and producing Rust releases*. The *community team*
is responsible for *coordinating events, outreach, commercial users, teaching materials, and exposure*.

[Here is a page with all the Rust teams](https://www.rust-lang.org/en-US/team.html) (and their
members).

![Rust teams](/images/2018/2018-10-19-rust_teams.png)

My favorite thing about this structure is that roles within the Rust community are
**explicitly stated** and people performing those roles are **explicitly credited** with
that work. You may notice that a lot of the teams that are listed involve work that is
**not** releasing features of Rust, or writing code. This kind of work is crucial for a
community to grow, but is often unrecognized or underappreciated (which has all kinds of
implications for diversity and inclusion, but that's another conversation).

OK, so these teams exist, but do they actually do? That takes us to the second part:

## The Rust "Request for Comments" process

All significant design changes in the Rust community are **not** be submitted directly
as a PR to the codebase. Instead, Rust has [a separate repository](https://github.com/rust-lang/rfcs) called `rfcs`. This
repository manages the process by which Rust sub-teams decide whether to support the high-level
design of a feature. It's a process to make a decision about whether something is worth doing (note here that
when I say "feature" I don't just mean code. In fact, the `rfcs` process *itself* was
an `rfc` at one point). Here's how it works:

If someone wants to make a change within the Rust community, they must make a Pull Request
to the `rfcs` repository that proposes this change. They [fill out a template](https://github.com/rust-lang/rfcs/blob/master/0000-template.md) (in markdown)
that covers things like "why should this change be made?", "what is this change?", "what
are the alternatives?", "what happens if we do nothing?" etc.

This person fills out the form and submits a Pull Request. At this point, one of the members
of the sub-team associated with the topic of the PR is assigned to be the **shephard** of the RFC.
This simply means that their job is to ensure the conversation moves forward in a
transparent and inclusive manner. They are *not* tasked with deciding or implementing the feature.

Once the PR is made, the pull request enters an "open comments" period where people can
discuss the proposal. Often this results in modifications to the PR as new ideas come up
and old ideas get refined. Throughout this process, the shephard's responsibility is to keep
things moving forward productively.

Once a member of the sub-team (usually the shephard) believes that enough discussion has
happened, they call for a "final comments"
period. This is their formal statement that "we're ready to make a decision, so speak now or
forever hold your peace". If no *major* new concerns are brought up, the sub-team associated
with the RFC then must reach a consensus about whether to *merge* or *close* the PR. If the
PR is merged, then the Rust community has now officially "supported the idea" *in theory*. Often
this is just the beginning of the hard work, and specific implementations get hashed out in the
PR to the codebase.

This process is about giving *more power to the Rust sub-teams*. In fact,
[sub-teams can also modify this RFC process for their own purposes](https://github.com/rust-lang/rfcs#sub-team-specific-guidelines).

## How do these teams stay on the same page?

One question you may have from all of this is "how does the Rust community stay cohesive
when all the teams are making decisions on their own?". That's what the **core team** is
for. In short, the core team is *at least* made up of leaders from each of the sub-teams
within Rust. The job of the core team is to have a *global* perspective on the Rust
community. They make decisions about *values* that Rust uses in making decisions, and high-level goals that the community should pursue. They also perform project-wide decision making such
as creating (or shutting down) specific sub-teams.

## Wrapping up

I like the Rust community governance structure because it is flexible, transparent, and explicit.

It's flexible because this structure treats the complexity of Rust as a feature, not a bug.
By giving decision-making power to the sub-teams within the community, they're recognizing
the unique perspective those teams bring to the table, and credit them with the ability to
make the right decision over their domains.

The governance structure is explicit in that it formally defines roles in the Rust
community so it's clear "who is responsible for what". Note that many of these roles
are of a non-technical nature. These are often "glossed over" in other projects, but they
are a crucial part of building an open community.

Finally, the RFC process is transparent in that all discussion happens in the open (on the Pull Request).
Moreover, it is also explicit because there's a clearly-stated process for how these
decisions happen. This curbs the possibility that decisions will be seen as made in "back-room"
conversations and builds trust in the process.

Over the next few weeks I'll keep exploring the Rust community's structure because I think
it's fascinating. Some questions that I've still got are:

* What does it look like when sub-teams make decisions that span the whole community?
* Is there tension between the core team and individual community members (because there's
  an extra layer of bureaucracy in the sub-teams)
* How do they ensure that these teams are comprised of stakeholders from different perspectives?
* What's going wrong with this structure? What are the downsides?
* Who decides the membership of the teams? How do the grow / shrink / disappear?

If anybody has thoughts or comments on the above, I'd love to hear them!