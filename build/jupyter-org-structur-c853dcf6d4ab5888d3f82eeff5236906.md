---
date: "2025-03-02"
authors:
  - id: chris
tags:
- jupyter
---

# The relationship between the Jupyter Executive Council, Software Steering Council, and Foundation

This is a question that I've been asked many times now that I'm serving on the JEC and the JF. I'm writing up a quick response so that I have something to refer back to and align my own thinking on.

**How most Linux Foundation projects seem to be structured**. Linux Foundation projects seem to have two key groups: a *Project Authority* that oversees the project (usually a technical steering committee of some kind) and an optional *Project Foundation* that raises and spends funds for the project[^found]. For projects that have a foundation, the foundation only has decision-making authority over its funding, and this is separate from the Project Authority's decision making. By separating the Project Foundation from the Project Authority, companies can't directly buy decision-making influence over the project while still being able to contribute funds for it.[^motives]

[^found]: Not all projects have a foundation (I think only about half do), and this is offered as an optional LF service for those that are big enough to warrant a dedicated foundation. Many projects couldn't realistically sustain a foundation on their own, though in some cases LF can create an "ecosystem foundation" that raises and spends funds to support a collection of projects.

[^motives]: This leaves the question "why would companies pay into a Foundation if they don't get any kind of direct project control?" It's a good question! Simply put, I think that a lot of companies view the Foundations as a vehicle to support open source projects in a general sense, and "a seat on the Foundation board" is simply a way to provide a level of accountability and control to ensure that the foundation resources are being spent reasonably. Foundations also seem like a useful way for companies to facilitate conversations and coordination with a project's leadership and amongst themselves. I hope to learn more about this dynamic in the coming months!

**How this applies to Jupyter**. When Jupyter moved to the Linux Foundation, it already had project and governance structure. The Jupyter Executive Council (JEC) and the Software Steering Council (SSC) had already been defined [in the Jupyter Governance docs](https://jupyter.org/governance/intro.html). As such, the JEC became the "Project Authority" in the model above. The JEC decided that a foundation might drive much-needed financial resources to the project, and asked LF to set one up. Thus, [The Jupyter Foundation](https://jupyterfoundation.org/) was created. The hope is that this will allow Jupyter to raise funds that benefit the project (via the foundation) while retaining the technical direction and open source spirit of its pre-existing community (which has always had a mix of large and small organizations, as well as individual contributors). So to summarize: the **Jupyter Foundation operates independently from Jupyter's Executive Council, Software Steering Council, and subcommunities**.

Here's an overview of how I think Jupyter is structured at the highest level. Below I'll share what I think this means in words.

```{figure} ./images/jupyter-foundation-structure.svg
A high-level overview of Jupyter's organizational structure, and the relationship between the Foundation, the Executive Council, and the Software Steering Council. This is Chris' best understanding as of March 2025.
```

**The Jupyter Executive Council is the ultimate authority within Jupyter**. It defines the strategic direction, and is the source of all authority within the project. It delegates that authority very liberally to sub-projects. It is also **responsible for all operations in the project**, again delegating this responsibility to others wherever they are willing to volunteer (and when they can't find others to volunteer, the JEC ends up taking the responsibility themselves, often in unsustainable ways). It is also the primary representative of "Jupyter's Interests" to the Foundation.

**The Software Steering Council is about helping sub-projects align and decide between one another**. The JEC delegates responsibility and authority for product and technical direction to the SSC. The SSC is there to help Jupyter have a coordinated technical vision and implementation across a bunch of totally independent sub-projects. It has representatives from each sub-project, and focuses its operations on cross-project discussion and decision-making like [the Jupyter Enhancement Proposal process](https://jupyter.org/enhancement-proposals/).

**Sub-projects sit underneath the Software Steering Council**. The SSC delegates technical and product direction to each sub-project and working group according to its mission and operations.[^tech] Each sub-project has its own governance and working dynamics, and a more focused mission around a part of Jupyter's technical stack or impact. The goals and responsibilities of each sub-project are given to the sub-projects from the SSC (which gets its authority from the JEC), and in practice they act almost totally autonomously from the JEC. There is an informal understanding that the JEC should focus on empowering the community rather than telling people what to do.

[^tech]: "Technical" isn't the right word here, because some subprojects aren't primarily software creation efforts, but a similar principle exists.

**The Jupyter Foundation is a way to raise funds to support these efforts**. The Jupyter Foundation is a _sister organization_ to the Jupyter Executive Council. Its primary goal is to create a space for companies to participate in having _cross-company discussions_ about Jupyter's mission in a way that benefits them, as well as to _raise financial resources to support the project_. Why do companies do this? Because Jupyter is a key technology inside of many of these companies, an under-resourced Jupyter project is a technical risk to companies, and paying $150K a year for one of your most important data science technologies is not that expensive. Member organizations pay annual membership fees to the Jupyter Foundation, to be used to support the project.

**The Jupyter Foundation Board makes decisions about how to use the funds**. The Jupyter Foundation Board is responsible for deciding what to do with all the foundation money. They must balance the interests of the Jupyter Executive Council (which has seats on the Foundation Board) with those of the Foundation members. Premier tier foundation members each get a seat on the board as well. Importantly, the _Jupyter Foundation doesn't have any technical or strategic decision-making authority for Jupyter's sub-projects_. It only decides how the Foundation's funding should be used to support the project.[^funding]

[^funding]: I think separating the project's governance from the foundation's governance is a good idea, though I suspect it will create a natural (and I think healthy) tension between the Jupyter Foundation's decisions for spending, and the wishes of Jupyter's volunteer community. I view the JEC as a key group to align the interests of these two groups, and I hope that we can ensure that this healthy tension doesn't become an unhealthy one. If others have experience serving in boards like this, I would love to learn from you! 

What does the Jupyter Foundation use the funds for? We are still figuring that out! Thus far, I have been heartened to see that the Foundation Board members seem genuinely interested in supporting a broadly healthy Jupyter Project, and [I have some thoughts on the best ways to use funds here](./os-support.md), but we are still figuring this out and I hope to share more updates in the future.

## Caveat: This is my best-effort understanding as of now!

I am still learning about this high-level structure of the project, so I may get some things wrong. But I hope that this is an interesting or useful description of the project at-large. If you have comments or questions, I would love to hear them, and I will try to update this if I learn of something major that I missed.


