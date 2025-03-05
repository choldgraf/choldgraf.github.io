---
date: "2025-03-02"
authors:
  - id: chris
tags:
- jupyter
---

# The relationship between the Jupyter Executive Council, Software Steering Council, and Foundation

This is a question that I've been asked many times now that I'm serving on the JEC and the JF. I'm writing up a quick response so that I have something to refer back to and align my own thinking on.

**How most LF projects seem to work**. Most Linux Foundation projects seem to have a single vertical governing structure. Projects have their own "Foundation", and this controls the strategy, direction, and financial resources of the project. Foundations have a pay-to-play model where companies pay for a decision-making seat on the Foundation, and this allows them to help with the project's direction (both for generous and for self-interested reasons).

**How Jupyter is different**. When Jupyter moved to the Linux Foundation, the JEC strongly advocated for _separating the financial and the decision-making aspects of the project_. Jupyter has always had a mix of large and small organizations, as well as individual contributors. They wanted to avoid creating a governing model where you couldn't meaningfully participate unless you worked at a large tech company. For this reason, the **Jupyter Foundation operates independently from Jupyter's subcommunities**.

Here's a high-level overview of how I think Jupyter is structured. Below I'll share what I think this means in words.

```{figure} ./images/jupyter-foundation-structure.svg
A high-level overview of Jupyter's organizational structure, and the relationship between the Foundation, the Executive Council, and the Software Steering Council. This is Chris' best understanding as of March 2025.
```

**The Jupyter Executive Council is the ultimate authority within Jupyter**. It defines the strategic direction, and is the source of all authority within the project. It delegates that authority very liberally to sub-projects. It is also **responsible for all operations in the project**, again delegating this responsibility to others wherever they are willing to volunteer (and when they can't find others to volunteer, the JEC ends up taking the responsibility themselves, often in unsustainable ways). It is also the primary representative of "Jupyter's Interests" to the Foundation.

**The Software Steering Council is about helping sub-projects align and decide between one another**. The JEC delegates responsibility and authority for product and technical direction to the SSC. The SSC is there to help Jupyter have a coordinated technical vision and implementation across a bunch of totally independent sub-projects. It has representatives from each sub-project, and focuses its operations on cross-project discussion and decision-making like [the Jupyter Enhancement Proposal process](https://jupyter.org/enhancement-proposals/).

**Sub-projects sit underneath the Software Steering Council**. The SSC delegates technical and product direction to each sub-project and working group according to its mission and operations.[^tech] Each sub-project has its own governance and working dynamics, and a more focused mission around a part of Jupyter's technical stack or impact. The goals and responsibilities of each sub-project are given to the sub-projects from the SSC (which gets its authority from the JEC), and in practice they act almost totally autonomously from the JEC. There is an informal understanding that the JEC should focus on empowering the community rather than telling people what to do.

[^tech]: "Technical" isn't the right word here, because some subprojects aren't primarily software creation efforts, but a similar principle exists.

**The Jupyter Foundation is a way to raise funds to support these efforts**. The Jupyter Foundation is a _sister organization_ to the Jupyter Executive Council. Its primary goal is to create a space for companies to participate in having _cross-company discussions_ about Jupyter's mission in a way that benefits them, as well as to _raise financial resources to support the project_. Why do companies do this? Because Jupyter is a key technology inside of many of these companies, an under-resourced Jupyter project is a technical risk to companies, and paying $150K a year for one of your most important data science technologies is not that expensive. Member organizations pay annual membership fees to the Jupyter Foundation, to be used to support the project.

**The Jupyter Foundation Board makes decisions about how to use the funds**. The Jupyter Foundation Board is responsible for deciding what to do with all the foundation money. They must balance the interests of the Jupyter Executive Council (which has seats on the Foundation Board) with those of the Foundation members. Premier tier foundation members each get a seat on the board as well. Importantly, the _Jupyter Foundation doesn't have any technical or strategic decision-making authority for Jupyter's sub-projects_. It only decides how the Foundations funding should be used to support the project.[^funding]

[^funding]: I think this is both a benefit and a challenge. It's probably the right thing to do from a governance perspective (so that companies with $$$ can't take over the project). But it means we're creating a tension between one group with authority and responsibility over Jupyter itself, but no authority over _financial resources_, and another group with no formal authority over Jupyter, but _with financial resources to spend_. It will be an interesting interplay between formal and informal power dynamics, and it'll only work in the Jupyter Foundation is genuinely aligned with the interests of the broader Jupyter community.

What does this group use the funds for? We are still figuring that out! Thus far, I have been heartened to see that the Jupyter Foundation seems genuinely interested in supporting a broadly healthy Jupyter Project, and [I have some thoughts on the best ways to use funds here](./os-support.md), but we are still figuring this out and I hope to share more updates in the future.

## Caveat: This is my best-effort understanding as of now!

I am still learning about this high-level structure of the project, so I may get some things wrong. But I hope that this is an interesting or useful description of the project at-large. If you have comments or questions, I would love to hear them, and I will try to update this if I learn of something major that I missed.


