---
title: "Why open source foundations try to fund systems, not development"
date: 2025-05-31
tags:
  - jec
---
This is a brief reflection on something that I've been hearing consistently from the Linux Foundation and its member projects as part of serving on the [Board of the Jupyter Foundation](https://jupyterfoundation.org). Here's a point that originally surprised me when I heard it:

> Most foundations within the Linux Foundation network recommend **against** using foundation resources for software development. Instead they recommend funding _systems that lead to more and better development from volunteer contributions_.

This was counter-intuitive to me at first, and I think may be counter-intuitive to others as well, so I wanted to share how I think about this.
## The core thesis of open source is that participatory development leads to the best products

At its core, open source development models rest on a belief that **you'll build something better, in the long run, if you give many different people the opportunity to co-create and co-lead together**. This is in contrast to models where you centralize the vision, roadmap, and development with a single organization.[^os]

[^os]: You may be wondering: what about all those open source projects that companies put out all the time? The ones where a single company is releasing a technical product under an open license, and developing in the open. To me, these are not really "open source projects" in the way that I'm talking about here. They're a product team choosing to work transparently and release code with permissive licenses, but they miss the key differentiator that makes open source projects great, which is co-creation and multi-stakeholder leadership. That's a whole other conversation that I won't get into here.

To me, this is *the most important part of open source*, and something projects must lean into. If not, then why be an open source _project_ at all?

## Writing code is easy - Reviewing, organizing, and aligning people is hard

That said, open source creation is _incredibly complex and time-consuming_. As projects grow in size, they grow their technical and social complexity at an incredible rate. The challenge is no longer writing code, it's **organizing teams of volunteer contributors to write the right code in a dependable and sustainable way**. These are _social problems_, not technical problems. For example:

- How do you set a collective vision and strategy when you have 5, 10, 50, 100 people without a formal hierarchy?
- How do you pay down technical debt when major components of a project have been written by people with different technical philosophies?
- How do you align teams on a roadmap of development priorities when they're all working remotely and on volunteer time?
- How do you spread the burden of maintenance and development when only one or two maintainers understand the codebase?
- How do you hold people accountable for working on the team's priorities when everyone is a volunteer?

These problems only get worse and worse as projects grow. And **this is a huge risks to stakeholders that want to depend on an open source project**. If I run a product team at a company, I use open source in-part because I have the ability to influence and improve the technology I depend on. If there's no reliable way for me to learn about a project's goals and participate in its development processes, it loses a lot of its core open source value as a project, and may be a liability as a dependency.

## Foundations should fund the hard parts since they need expertise and dedicated time

For this reason, foundations use their resources to _fund a system that leads to better, more productive co-creation_. This makes it easier for others to participate in the project, to set a shared direction, and to get things done reliably. It leans into the core strategy of a big open source project.

For example, this might include roles and work like:

- Fund roles that align open source projects on what they _want to develop_.
- Fund roles that spread knowledge so that there aren't silos of information and skills.
- Fund roles that give guidance to contributors so that there's coherence to technical implementation across the project.
- Fund roles that _solve problems for technical contributors on the project_ rather than doing technical contributions for them.
- Fund roles that help marketing and sales of the foundation, so that it has more resources to fund the above roles.

## This will make it easier for ecosystems of contributors to grow

If you fund systems like this, it will be easier for many stakeholders to participate in an open source ecosystem. These might be individuals, companies, university teams, etc. They'll all have different motivations and interests - some may be building internal products, some will be scratching an itch, some will be selling consulting contracts.

Crucially, they'll all need a _system_ that directs their energy in the right direction, and provides the guidance necessary for them to make a helpful contribution. That system is the thing that foundations want to fund.

Don't get me wrong, foundations _do care about writing code_ - that's the whole point of most open source project. However, funding development work directly cuts against your main thesis that software development can be done collaboratively by a community, and not just by dedicated staff. For this reason, I've come around to the idea that foundations should use their resources to grow a contributor ecosystem rather than develop code directly. It's the funding approach that leans into what open source is supposed to be all about.

## Appendix: Exceptions to this strategy

I've heard of a few exceptions to this strategy that are worth noting. Here are the cases where I've seen foundations directly fund software development:

- Crucial maintenance and technical development that _must_ be perceived as vendor-neutral. If there is something fundamental to a tool, and that might be a leverage point for stakeholders to bias the project in their favor, foundations might fund a role that oversees technical development or direction in order to avoid the (real or perceived) bias towards whoever employs that developer.
- Rotating roles for core project support and maintenance. Some projects fund a "developer in residence" type of role, which is a "chopping wood and carrying water" type of role to help projects do basic maintenance. I've seen this most-effectively used when a project has relatively few repositories or technical products (in my opinion, this would be hard to scale with Jupyter, which has dozens).
- Special projects that have separate fundraising. For example, the Rust Foundation has a [security initiative](https://rustfoundation.org/security-initiative/) that I believe it does separate fundraising for. In this case, the "core foundation funds" cover the time of the people that _do the fundraising_ for focused initiatives like this.
