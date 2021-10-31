---
author: Chris Holdgraf
date: 2020-11-08
tags: open source, sustainability
---

# Contributing to open source: A short guide for organizations

Over the years I've had a recurring question from people who are in organizations both big and small: _how can we participate in open source communities?_

Whether it is because of altruism or strategic importance, many companies, research groups, non-profits, etc _want_ to be involved in open source projects (particularly large and impactful ones like Jupyter), but getting involved can be an opaque and confusing process if you're not already familiar with open source. Each community has its own nuances and social dynamics, and approaching from the outside can be a challenge.

So this post is a short guide to provide some ideas for how others can begin to engage with open source. My hope is that it gives people who are embedded in organizations some ideas about how they could engage with open source, or advocate for engagement internally.

:::{note}
This is all just personal opinion, and based on my own experiences so far. I'll try to keep it updated over time as my own thoughts evolve. If you've got ideas of your own I'd love to hear them in the comments.
:::

## Meet open source communities where they are

If there is anything I'd emphasize the most, it is that organizations need to meet open communities where they are - that means abiding by community values and social norms, and accepting that community priorities may be different from those of an organization.
A few quick ideas for doing this:

- **At first, treat yourself as a visitor**. It will take time to build understanding, status, and trust within a community. Until that happens, it's important to meet open source communities as peers and consider yourself a visitor. Listen, learn, engage, and adapt your behavior to that of the community. Don't assume that you should have any special status because you're a large or well-known organization.
- **Participate in community spaces**. The easiest way to learn how a community operates is to participate in the online spaces where it operates. If there are community meetings, attend them and introduce yourself. If the community has a forum, show up and say hello. If the community uses GitHub issues, watch for what kinds of things people discuss. Offer help, advise, and guidance wherever you can. This will help you understand the needs and direction of the project.
- **Abide by community culture**. For many communities, a lot of care and thought is put into building community dynamics that are open, inclusive, deliberate, and that balance power across the many stakeholders in the ecosystem. It is crucial that you abide by these cultural dynamics, especially with respect to things like Code of Conduct and interpersonal interactions. Taking this time to understand the culture will make the experience much more pleasant for everybody involved.
- **Respect the community priorities**. Many organizations reach out only at the moment where they _need_ something. This is understandable, but a very inefficient way of getting things done in open source communities. There are a variety of needs, priorities, and interests in the community. You should begin by understanding what these are and finding ways to engage with them before focusing on your own priorities or asking for (or offering) changes to suit your needs. The trust that comes from helping someone _else_ with their problem will make it much easier for you to get your own issues fixed in the future.
- **Accept that things will move more slowly**. I know that you have a product or a feature to ship, and that you want to make rapid progress. But, open source communities generally are (and generally should be) slower and more deliberate in their decision-making than many organizations are used-to. Slowing things down ensures that a diverse collection of voices have an opportunity to weigh in on questions, and keeps the community more inclusive and participatory. It also often leads to better decisions that take into consideration more perspectives.

After you spend some time engaging with open source communities, there are a few concrete steps you can take towards making contributions. Here are a few ideas...

## Help with development and repositories

After you've spent some time interacting with others in the community, perhaps you'd like to make contributions of your own to the codebase or tools. How can you do this in a way that benefits the community?

:::{admonition} A note on non-coding support
:class: note
Note that, while code is often the output of an open source community, there are many non-coding ways to contribute to that community. Many of the "code-related" activities are actually "people-related" activities, such as assisting others with their problems, or engaging in discussion in issues.
:::

### Upstream improvements when using core technology

By far the most-common way that organizations contribute back is by "upstreaming" improvements to the open source project as they notice problems or opportunities to improve the code.

If you're using a tool regularly, or building it into another tool like one of your products, look for small ways that it could be better. Rather than fixing these issues in your fork of the project or your internal codebase, open an issue in the core repository and offer to fix it if others agree it's a problem. If a team member has an idea to improve the tool, don't just build it in your products, improve it in core.

:::{admonition} Example: The Jupyter Server
:class: tip
The [Jupyter Server](https://github.com/jupyter/jupyter_server) project is an attempt at pulling out much of the server architecture from the original Notebook application. It's a very low-level library that is re-usable across a number of other potential tools. Its presence benefits the whole ecosystem, but because it is so generically useful, it has few dedicated resources to maintian and develop.
:::

:::{admonition} Example: Accessibility
:class: tip
This is one of those things that is *super* hard to get volunteer support for because it is not sexy and it is hard work. Many organizations care about accessibility for a variety of reasons, and taking the time to give back guidance and development to make core tools more accessible is a huge benefit. On this point in particular, I think it is important that organizations not make accessibility a competetive advantage over open source tools, but instead contribute to the common good so that these tools are more inclusive and available to all.
:::

### Contribute to the documentation

Documentation is crucial to the success of open source, as it is the interface between people and the code. Documentation should be clear, searchable and findable, and should cover all of the functionality in a tool. However, it's very difficult to properly-document open source software!

New users are in an extremely good position to point out inconsistencies, missing information, and unclear explanations in the documentation. If someone in your organization is trying to use an open-source tool for the first time, ask them to spend a few moments providing feedback about how the documentation could be improved, or even better, making a PR to the docs.

### Work on major features the community has prioritized

If you've got more substantial development time to devote to a project, see what kinds of features people want, and offer to help tackle something that aligns with your own interests. This is much easier if you do so after interacting with the community for a bit, as you will understand its priorities, as well as the underlying codebase, enough to be more efficient and productive.

Take a look at the issues or roadmap of a project and find ones that you'd also benefit from, chime in and mention that you'd like to try and make these changes to see if others are excited about it. Then, follow-through and engage with the community as you make changes. Don't be resistant to feedback - remember that you are a part of a broader community with its own norms and expectations around code style, structure, etc.

:::{admonition} Example: Look for 👍 in issues
:class: tip
The Executable Books Project has [a feature voting leaderboard](https://executablebooks.org/en/latest/feature-vote.html) that it uses to let users vote with a 👍. You can even see this list for *any* GitHub repository by **sorting issues by 👍 reactions**. For example, [here are the issues with the most 👍 in JupyterLab](https://github.com/jupyterlab/jupyterlab/issues?q=is%3Aissue+is%3Aopen+sort%3Areactions-%2B1-desc).
:::

### Provide core maintenance and support

If you have spent some time interacting with a community, working through bugs and features, etc, you may consider providing more ongoing core support for a project. This is the holy grail of engagement, as core support and maintenance are one of the scarcest resources. Offer to read through issues and triage on a regular basis, routinely engage in pull requests and provide feedback and advise, spot-check bugs over time that others have brought up, do community work to organize meetings or work plans.

When I try to figure out who is being helpful in the Jupyter ecosystem, I ask questions like "who is doing the things that nobody else is doing?". E.g., who is the first person to respond to an issue? who is making documentation improvements, or helping an inexperienced contributor improve their PR? These little "carrying water and chopping wood" tasks are not flashy and exciting, but they are *crucial* to keeping the community dynamic, welcoming, and productive.

:::{admonition} Example: Contributing guidelines
:class: tip
Take a look at the [JupyterHub Team contributing guidelines](https://jupyterhub-team-compass.readthedocs.io/en/latest/team/skills.html#a-few-general-ways-to-help-out) - most of them aren't strictly technical, they're about helping others, helping the team in conversations, and generally just being friendly and productive community members.
:::

## Collaborate with open source projects

Beyond directly working inside of an open source community, there are also plenty of ways that you engage with them as collaborators and partners. Here are a few concrete ideas.

### Collaborate on open standards and APIs

Beyond the open source core, there are often places where you wish to build out your _own_ functionality. In these cases, it's important that new APIs and patterns of interaction happen in conversation with the open source community, in order to ensure as much standardization as possible across ecosystems.

Any time that you'd like to extend functionality beyond what's already there, and have to make a semi-arbitrary decision of what pattern to expose to users, standardize on something the community already uses so that there isn't unnecessary duplication and fracturing across ecosystems. If no standard exists, don't just create one - reach out to the open source community and lead a process that gets others to brainstorm and buy-in to a new standard.

:::{admonition} Example: The `ipynb` format
:class: tip
The `ipynb` format. One of Jupyter's core goals is to standardize tools and patterns across the data science community. The `ipynb` format is probably the most common example. As more tools build their own notebook functionality and wish to *extend* `ipynb` to do new things, they should follow metadata standards (or lead processes to create new ones). For example, we don't want `ipynb` files that have platform-specific metadata. Even little stuff like "for cell-level metadata to hide inputs, do we call it `hide_input` or `hideInput`?" This can seem trivial and arbitrary but it is important and in many ways the most important thing that open communities do! When in doubt, ask around and get buy-in from others. 
:::

### Advocate for open tools from the community

While developing and improving technology is a core part of open source, there is also a great deal of *advocacy* needed to expand their use and to get feedback. Organizational partners can be a huge help here by finding ways to support and highlight open source tooling in their stack, and by explicitly highlighting this tooling in tandem with organizational products.

This can be a bit tricky (competive landscape etc), but the rubric that I shoot for is: use community-led products wherever possible, and if that's not possible, make sure to highlight and advocate for community-led products in-tandem with your own products.

:::{admonition} Example: Workshops and training material
:class: tip
Many organizations run workshops, demos, and training sessions for their products. They also have sizeable marketing departments for the work they do. In all of these efforts, make it clear when you are relying on an open source tool for support, and highlight the ways in which you are engaging with its community and giving back.

For example, [spacy.io](https://spacy.io/) is an NLP framework built by [explosion.ai](https://explosion.ai/). As part of their online documentation, they include interactive code sessions powered by [Binder kernels](https://mybinder.org). They make sure to include the name "Binder" whenever these kernels are spun-up in order to give credit and thanks to the free mybinder.org service.
:::

### Financially support open source projects

Some open source projects have ways to support them directly through funding. For those that do, an easy way to contribute is to provide some of your own financial resources for these things. Check whether the project, or any major contributors in the project, have a [GitHub Sponsors](https://github.com/sponsors) or a [Patreon](https://www.patreon.com/) page. Investigate whether the [project is fiscally sponsored](https://numfocus.org/donate) and can accept donations. Other projects perform focused fundraising, for example the Jupyter Project has a [Jupyter Contributor in Residence](https://blog.jupyter.org/the-jupyterhub-and-binder-contributor-in-residence-56708d1e3069) position that it must raise funds for.

Alternatively, look into whether you can sponsor open-source work via other companies or contractors. Many companies do contract-style work in open source, and welcome funding to "buy out" open source time.  Fundraising can be a time-consuming effort, and offering your resources can help make a quick impact if the project is in a good position to accept them.

## Bottom-line

There are many different ways that you can participate in open source communities. Fundamentally, this comes down to being attentive, flexible, and generous. Each community is different, but some combination of the above steps will help you make progress and make an impact in working with many open source communities.

If I've missed something important, please do chime in and suggest other ways that organizations can get involved. I would love to continue updating this list as new ideas come to light.
