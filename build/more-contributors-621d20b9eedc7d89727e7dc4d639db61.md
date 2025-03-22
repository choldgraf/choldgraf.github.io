---
title: Jupyter can align the needs of its community and its foundation by enabling contribution
date: "2025-03-22"
---

This week was my first time attending the [Linux Foundation Member Summit](https://events.linuxfoundation.org/lf-member-summit/). This is an annual meeting for all of the Linux Foundation member organizations and projects. I joined because of my new role [on the Jupyter Executive Council](./jec.md), and so I tried to go into this meeting with the goal of learning how [Jupyter's new Foundation](https://jupyterfoundation.org) could be more impactful, and to understand the Linux Foundation space in general. In particular, I wanted to get ideas for where the Foundation should invest its first year of funding.

The LF Summit is designed for the "corporate open source" world - it's held at a fancy resort in Napa, and its content is structured for people navigating open source questions inside of a company context. There was a heavy representation from OSPOs, and a lot of the discussions were about how to navigate opportunities in open source with internal stakeholders, how to make a value proposition for open source to your management, how to identify risks in open source strategy, etc. I was heartened to see that most folks at the conference were coming at this with good intentions - most of them genuinely wanted to find ways for their company to adopt and support open source, while recognizing that there is usually somebody up their reporting chain that has a much more skeptical or naive view of open source.

## Companies want to know that communities are healthy

Companies are _really worried about open source safety_, probably because larger organizations are inherently more conservative and prone to see risk, and also because they have a leveraged dependence on open source when their core business operations or products depend on it. There was a lot of conversation about supply-chain, signing, provenance, etc. However there was also **a lot of conversation about the social side of open source**.

Company reps were sharing best practices for how to gauge the health and willingness to contribute from open source communities. Perhaps the biggest perceived risk was that a community would simply cease to function, and thus leave their code to bitrot or hostile takeover. A secondary risk was that a community would be totally unresponsive to the needs of engineers within the company, which made them feel like they have no ability to contribute to (and influence) the project.

In short, companies see less risk and more opportunity when an open source project feels responsive and dynamic. There were discussions about how many issues were getting regular triage and discussion, how quickly PRs were merged, how efficiently and transparently decisions were being made, etc. They wanted to see good governance, and a path towards contributing to these processes (again this is not out of their generosity, but because they want to see a pathway to having their interests represented, which is totally reasonable). 

There are plenty of ways that I worry about an outsized interest of corporate needs in open source projects, but given the reality of where many projects are at now, I also think this is a significant opportunity.

## Open source projects need more capacity to facilitate contributions

One of the most common challenges that open source communities face is the **lack of capacity** to get things done. There is an enormous amount of work to keep a community moving forward. This is especially true if it navigates a complex technical and product space and needs to make decisions that don't have easy answers.

At the heart of this matter is **a lack of capacity to grow capacity**. Communities want more contributors, but they don't have the combination of skills, infrastructure, and time to grow them efficiently. This puts communities into a downward spiral where they spend all of their time doing day-to-day work without growing capacity. Work always grows, and so it leaves a growing gap between community capacity and the work that needs to be done.

This is risky for the community. Having over-worked maintainers leads to inefficient and frustrating conversations, slow turnaround for issues and enhancements, unreliable releases, unmaintained infrastructure, etc.

## That's an opportunity to solve two problems with one investment

So I left the LF summit feeling like, for now, Jupyter's biggest challenge is also the same challenge felt by its member organizations. It is something like this:

- Jupyter's community is over-burdened and over-capacity. It has several dedicated maintainers, but they're spending all of their time keeping the project afloat. They aren't trained in community management or contribution support, and they don't have much time for this work anyway, so they aren't able to grow the number of contributors in general.
- Companies have many engineers and team members who _want to contribute to Jupyter_. This is both for company interests (to upstream changes they want) but also just because engineers tend to like working on open source projects like Jupyter. However, company engineers aren't comfortable navigating messy open source projects, and Jupyter doesn't do itself any favors by making this easier. As a result, **there's an untapped pool of contributors in the Jupyter Foundation's member organizations**.

When I think about the best place to invest the Foundation's funds, I think **growing Jupyter's capacity to facilitate community discussions, onboarding, contributions, and decisions should be its highest priority**. How are some ways that we could do this?

## A few ideas for how to grow Jupyter's contributor capacity

Here are a few ideas that come to mind, I'd love to discuss each of these with our board.

**Hire a Developer Experience Engineer**. I've been interested in the Developer Experience Engineer role since first [hearing about it from the SustainOSS podcast](https://podcast.sustainoss.org/141) in an interview with [Melissa Mendonca](https://github.com/melissawm). My understanding is that this role is someone with _technical skills_ and an interest to _use those skills in making it easier to contribute_. For example, this might be improving infrastructure that facilitates CI/CD and testing, it might be improving technical documentation for onboarding, or it might be providing mentorship to newcomers that need help with the technical work.

**Hire a Community Manager**. I also think that Jupyter's contributor and user communities are complex and large enough that they could also benefit from dedicated expertise to help them coordinate, connect, communicate, and grow more effectively. Jupyter has around a dozen sub-projects, each with their own technical vision and a (theoretical) vision that ties them all together. Aligning that whole group is a lot of work. It sounds like [a Community Manager](xref:ttw#cl-infrastructure-community-managers-tasks) could be a great way to facilitate these conversations. For example, by hosting [Collaboration Cafes](#community-handbook/coworking/coworking-collabcafe) across the project.

**Improve our documentation with a technical writer**. We have a _lot_ of documentation debt to pay down, and I think we could make a lot of progress with a concerted effort aimed at improving our documentation across the board. I know there are technical writers out there that do contract work, and finding one that specializes in documentation could be a great way to quickly boost the clarity and structure of our documentation across the project. This could start with a high-level overview of Jupyter, and end with the contributing documentation of each sub-project. What'd be even better is if the DevEx Engineer above could help make some contributions to MyST that would allow us to standardize its use across Jupyter.

**Fund in-person community meetings**. If we had capacity to help manage and organize meetings in the form of a community manager, I'd love to use more funds to help us make _in-person_ meetings happen. This could bring together current or potential contributors across the Jupyter community, with a focus on having conversations or collaboration sessions that are best-done in-person.

## I suspect it'll be best to bring in skills from outside the Jupyter community...

Finally, I've been thinking about _where to find skills_ for roles and responsibilities like what I've described above. There are certainly many in the Jupyter community that have done things like what I've described above (for example, the [Jupyter Releaser](https://github.com/jupyter-server/jupyter_releaser) is a good example of a DevEx engineering project). However, I also think this kind of work is often done because it _has_ to be done, not necessarily because someone _wants_ to do it, or because they're the _right person_ to do it.

I'll go out on a limb and say that this is an opportunity to bring in new skills and voices into Jupyter, and we should consider using these funds to bring in outside expertise, either in the form of people that would do this work directly, or consultation and training they can provide Jupyter's members. Ideally we could work out a "train the trainer" style model where Jupyter can grow its own capacity over time to do this kind of thing.

OK that's what I've got for now... I'm going to think about these above, and if anybody has ideas for where to start, I'd love to hear them.
