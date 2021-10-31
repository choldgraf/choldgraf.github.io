---
tags: [open communities, open culture, sustainability]
permalink: open-communities-free-labor
category: open source
date: 2018-12-05
---

# Open communities need to be partners, not sources of free labor

In the last couple of years, we've seen an increasing number of organizations start to
spawn products that take a largely open stack (e.g., the SciPy ecosystem) and wrap
it in a thin layer of proprietary/custom interface + infrastructure.
On the face of it, this isn't a problem - I really want people to be able to
make money using the open source stack - however, there is a big caveat. When you look
at the work that those organizations have done over time, you often see a pretty thin trail
of contributions *back* to those open source projects.

I'd argue that using an open community's software without contributing back is straight-up
exploitative (legal, sure, but still exploitative), and we should think about ways to
suppress this kind of behavior. This post is a collection of thoughts on that topic.

But first....

## Why should I care whether I'm being a "good citizen in the open community"?

Organizations are driven by incentives, and ultimately if a behavior isn't conducive
to the organization's bottom-line, then we can't expect them to adopt that behavior.
I'd argue that interacting with the open community has a number of bottom-line benefits, here are a few:

* **It makes you a more attractive place to work**. Operating in open communities is
  often where people learn their technical skills, and while people come and go through
  organizations, the open community remains. Employees want to interact in these communities,
  and employers that have a good relationship with open communities are more attractive
  places to work.
* **Open communities can be a great training resource**. Have some improvements to make in
  your Python or R skills? Need to tool-up on your ability to write CI/CD pipelines? Open
  communities are a great place to get feedback and guidance from others with more experience.
  The open community is a resource for constantly tooling-up your technical skills. Use it!
* **Open communities can make better team-members**. Making complex technical/social decisions
  with a diverse community distributed across the world is really difficult! For the communities
  that do this well, interacting with them can be a fantastic learning experience in team-work,
  communication, coalition-building, critical feedback, and leadership.
* **Interacting with open communities gives you influence**. If you're using an open
  tool, don't you want to have a say in how that tool grows and evolves? Being a passive consumer
  of open technology means you're at the whim of that community's wishes. If you're a *part* of
  that community, you can influence its direction to align with your organization's goals.
* **Interacting with open communities means you write less code**. I suspect that in the long-term,
  writing your own code will almost cost more than using somebody else's code (in terms of
  person-hours it requires). If you've got a say in an open project, you minimize the chance that
  you must either maintain an internal fork w/ significant changes, or create your own new thing
  that you must now maintain on your own.
* **Interacting with open communities can make them more robust**. Finally, let's not forget
  that communities can and do fail all the time. What happens if a project you depend on
  stops making bug fixes? Or doesn't have bandwidth to maintain security patches? By contributing
  resources to these communities, we keep them thriving and healthy creators of open-source
  tools. We all benefit from this, and more importantly you don't have a dead project that your
  core product or teams depend on.

Those are just a few benefits, but I'm sure there are others. For more information and ideas about
how open source communities can be a benefit to your organization, I recommend Mozilla's
[Open Source Archetypes](https://blog.mozilla.org/wp-content/uploads/2018/05/MZOTS_OS_Archetypes_report_ext_scr.pdf)
research paper.

Now that we've got that out
of the way, let's move on to deciding whether or not your organization is, in fact, being
a positive actor in the open-source community.

## How can I tell if my organization is not being a good citizen in the open community?

I suspect that many organizations simply haven't put a ton of thought into whether they've got a positive-or-negative
relationship with the open communities that intersect with their work. Here's a quick set of questions
to ask yourself:

* Do your employees routinely use open-source software in their work?
* Does your organization create a product that depends on open-source software?
* Does your organization depend on proprietary software that depends on open-source software?

If you answered "yes" to any of those questions, then ask yourself the following questions:

* Do you have explicit policies that encourage employees to contribute back to open projects?
* Do you have explicit funding mechanisms to give resources to open projects?
* Do you explicitly call out and acknowledge the importance of those open tools in your presentations and (some kinds of) marketing?
* Do you have regular, open channels of communication with those open communities?
* Do these behaviors scale with the amount of value you derive from open communities?

If you answered "no" to these questions, then you're probably exploiting the open community.
You should stop that!

However, avoiding this kind of one-way relationship with the open source community is complex
and requires some new efforts and thinking from both sides of the equation.
The rest of this post includes a few ideas on how open projects, as well as organizations,
can improve this relationship.

## How can open communities encourage organizations to be good citizens

How can the open community encourage better interactions
with organizations that depend on our tools?

First off, I think these are *not* problems that we should have to solve with licensing [1]
. These are **social**, **moral**, and **incentives** problems.
There are plenty of organizations that make money from open-source, but that still
manage to spend time being part of the communities that they draw value from. How do we encourage this
kind of behavior? I have a few ideas, but we should spend more time thinking about this:

1. **Open communities need more ways to signal "thank you" to organization that behave well**. For
   example, the Kubernetes community runs a [service called stackalytics](http://stackalytics.com/?project_type=kubernetes-group&metric=commits)
   that lists contributions broken down by company. It would be great to adapt this kind of visualization
   for the broader OSS community. More generally, "thank-you"s should be for specific behavior, and it should be clear whether that behavior is a one-off or is on-going. Organizations are incentive-driven, so we should create more
   positive incentives for them to interact.

2. **Open communities need a better vocabulary to describe bad behavior when it exists**. I've had
   a number of conversations with folks that are frustrated when an organization uses their tool without
   giving back. These people often feel like there is no medium through which they can "call-out" the
   offending organization without sounding "whiny", and so they internalize this stress. If there were a way to
   quickly describe what this behavior is, it could be easier for people to call it when they see it.
3. **Open communities need to make it clear *how* organizations can get involved**. This is a two-way street.
   While we need more participation from organizations making products or services around open-source, we also
   need to position our open communities so that there are clear pathways for interaction and contribution.
   Things like roadmaps, clear community governance, and well-tuned practices around encouraging outsiders to
   join the community would go a long way.
4. **Funding bodies should consider open-source participation when giving out money**. Perhaps this one only
   applies to some sub-fields, but private philanthropies or public funding bodies (like the NSF) should consider
   a project's intersection with the pre-existing open community when deciding whether to fund a project.
   If you propose creating a new tool, you should be required to do due-diligence on other tools in that space,
   and explain why you won't just contribute to those communities instead of building your own. If you propose
   building a product off of open-source software, you should have a plan for how you'll contribute back to those
   communities. Saying that you'll open-source your code and throw it over the wall is *not enough*.

## What could organizations do now to support open communities?

All of the steps above are fairly long-term solutions to a problem that exists right now. What are some things
that organizations can do now in order to make sure they're perceived as more positive actors in open communities?
Here's a short "off the top of my head" list.

1. If you're an employee, find allies and **pressure management to support open-source software**. Often, organizations
   contribute to open source only because employees make a case for it.
2. If you're at management-level, **create space for your employees to contribute to open-source software**. They'll
   be happier employees (OSS is a gratifying experience), you'll have more say in the tools you use, and you'll be
   a more attractive place to work for developers.
3. If you're at the executive / strategic level, **incorporate an open-source strategy in your business plan**. Open source
   can be an incredible resource if harnessed properly. Your organization will be better off in the long term if you treat
   open communities as partners rather than sources of free labor.
4. If you're creating a new open-source tool, **write a justification for why you're creating a new thing, instead of contributing to an existing thing**.
   Sometimes there's a great reason not to jump on-board with a pre-existing tool. However, you need to signal that you've
   thought hard about this, and recognize the downside to creating yet-another open source tool when alternatives exist.
4. If you've got a product that directly uses open-source, **have an open-source plan for giving back**. Signal to the
   community what you're doing to say "thank you" for all of the value you're getting from the open community. Maybe it's
   people's time to contribute back, maybe it's money, maybe it's marketing for OSS communities.
5. **Write an annual "contributing back to open source" report** that details the ways you've contributed back. It'll highlight your organization's role as a leader in this space, and signal the value that these tools provide for you.

That's it for now, though as you can probably tell, this is a complex topic with a lot of nuance. If you've got any thoughts of your own, feel free to leave a comment below, or [reach out to me on twitter](https://twitter.com/choldgraf)


**[1] A note on licenses**

When I talk about this stuff, people often mention **copyleft** licenses as an option. Basically,
this means releasing something under a permissive license, with the caveat that nobody else can
change the license to be less-permissive. I think this is a reasonable step to take if you *really* want to
curb this kind of bad behavior. However, it's also a blunt instrument. I **want** organizations to be
able to make money using open-source software, and I think copyleft licenses may reduce a lot of
the fluid, open practices that make open-source such a powerful force in our society.

*Many thanks to [Yuvi Panda](https://twitter.com/yuvipanda), [Tim Head](https://twitter.com/betatim), and [Joe Hamman](https://twitter.com/HammanHydro) for comments on iterations of this post*