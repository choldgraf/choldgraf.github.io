---
tags: jupyter, community
title: Thoughts from the Jupyter team meeting 2019
redirect: jupyter-team-meeting-2019
category: community
date: 2019-03-30
---

I just got back from a week-long Jupyter team meeting that was somehow both
very tiring and energizing at the same time. In the spirit of openness, I'd
like to share some of my experience. While it's still fresh in my mind,
here are a few takeaways that occurred to me throughout the week.

*Note that these are my personal (rough) impressions, but they shouldn't be taken as a
statement from the project/community itself.*

# Jupyter has a huge and diverse set of users

The first thing is probably unsurprising to many people, but was really driven
home at this meeting, is that there are **so many** Jupyter users our there. These
people come from all different walks of life - some are at huge tech companies,
some are scientists, some are educators, some are students. Some are from western
countries but many are not, some have wealth, some do not. Jupyter
(notebooks, anyway...more on that in a second) has really caught fire across
a wide slice of society.

This is both a great thing and a challenge. Appreciating the size of the Jupyter
user community also made me realize that many of these groups have different
motives and goals. Jupyter was originally born out of a mission to serve
scientists and educators, to create public goods,
and to be a democratizing technology that empowers
many different kinds of people in the world. I think Jupyter is still serving
this role, but that as the Jupyter user community has grown, the voices of
science and education may be getting smaller relative to the gigantic and
well-resourced community of "enterprise users". I hope that we can find ways
to balance these interests in the project in a way that keeps Jupyter a
project for *all*.

# Jupyter needs to grow its contributor community

While the *user-base* of Jupyter is fairly large and complex, the community
of *contributors* (people that help in issues, help grow the community, help others
use Jupyter, or contribute code to Jupyter tools) needs to grow. We have had a
relatively stable group of contributors in the Jupyter ecosystem, but I think
we need to foster more "organic" growth with others who jump in and become core parts
of the team. As an open project, we depend on the good-will and volunteer
time of others who want to join the community and participate. The fact that we
haven't seen a steady growth in contributors (particularly from a pool of people
more diverse than the current contributors), tells me that we have a lot of work
to do in creating obvious pathways to connect with, and grow within, the Jupyter
community.

We spent a morning session discussing diversity and inclusion, reading
[an excellent slideshow on 10 actionable steps to increase D+I](https://www.ncwit.org/sites/default/files/resources/10actionablewaysincreasediversitytech_openview.pdf).
It was a good reminder that recognizing systemic biases against certain groups
of people does not mean abdicating responsibility as an *individual* to personally
create a more inclusive environment. A couple of particular points that I hope
we can make progress on in the coming months:

* **Have a moderator and an agenda for meetings**. Conduct meetings (in-person or remote)
  with a moderator who builds a queue of
  speakers and gives the floor to each of them in turn. While it's easy to
  treat an unstructured meeting as "informal and fun", it also makes them significantly
  less-productive and harder to participate for many. I really enjoyed reading
  the article [how to make remote meetings not suck](https://chelseatroy.com/2018/04/05/how-do-we-make-remote-meetings-not-suck/)
  (SPOILER: the answer is to make **all** meetings not suck by providing structure
  and moderation). Taking small steps towards team processes that make meetings more
  participatory and predictable would go a long way.

* **Make more active efforts to bring new+diverse members into
  the community**. You can't expect organic contributor growth from populations that
  have very little representation on the project already. We need to continue
  making *active* efforts at engaging these communities and bringing in new people.
  For example, we had a new team member join the meeting as part of an
  [Outreachy internship](https://www.outreachy.org/), and I really appreciated their
  perspective on many of the issues we discussed. Had we not taken these active steps
  to bringing a new Jovyan into the community, those perspectives would never have been
  shared at the meeting.

* **Create explicit roles and ways to contribute**. We also spoke at length about
  the **many** different things that must be done to have not only cycles of code
  development, but also a healthy community around that code. Many times this work
  is done in an unstructured and ad-hoc way. This is stressful for the people doing
  the work (I often have no idea how much time I've sunk into responding to issues,
  for example), and it also makes the project team more opaque to others who might
  wish to join. If I am vaguely interested in contributing to JupyterHub, where
  do I start? Some people have a clear path for how they could contribute, but I
  suspect that there are many other ways that we can tell people "it would be
  helpful if you do XXX".

# The Jupyter ecosystem needs better explaining

Another topic we discussed was the fact that Jupyter hasn't clearly
explained its technology stack, how everything fits together, what problems
it's meant to solve, and how it interfaces with the outside community. The
majority of people think of "Jupyter Notebooks" when they think of Jupyter,
but often don't recognize that there are a lot of pieces under the hood as
well (e.g. the Notebook application is both a kernel / server architecture, an
underlying notebook document specification / format, and a particular notebook UI).

Jupyter still has challenges in making other major projects more discoverable
(e.g. JupyterHub for sharing Jupyter environments on shared infrastructure,
or other user interfaces like Jupyter Lab or Nteract). Moreover, the project is
also starting to be picked up by companies and projects that
are fairly liberal with the use of the "Jupyter" name. Is your tool still
"a Jupyter Notebook interface" if it only has the ability to export to a
Jupyter Notebook, but uses no other Jupyter tech? I'm not sure - but either way,
there should be a clear answer to that question otherwise the project will
start to be defined by other people rather than itself.

# Governing open projects is really hard

Finally, something I've grown to appreciate more over the last year
is how difficult it is to balance decision-making, power, and participatory
community dynamics in a large, multi-stakeholder, open project like Jupyter.
There were a lot of conversations around the current governance model of
the project, and how this wasn't currently serving the community in a satisfying
way. As the number of stakeholders in the project grows, their
needs may start to move in opposing directions. Keeping a project functional
and productive, while still balancing between these needs, is a massive task.

This becomes particularly challenging when the stakeholders in the project have
differing levels of resources. For example, Jupyter has always been dedicated
to building tools for scientists and educators. However, these individuals are
often part of organizations with *vastly* fewer resources than tech companies.
How can we ensure that the voices of these two groups have a balanced weight?
If company X decides they want to contribute a new feature the Jupyter
Notebook interface, and they put a team of 10 people on it, how does this team
interact with the decision-making processes of the Jupyter project? What if the
core maintainers are volunteers with limited time to review PRs? What if there are
disagreements between the company team's internal mandate, and what is best for the
Jupyter community? Finally, what if there aren't good channels of communication
and processes of decision-making that encourage nuanced, in-depth discussion to
facilitate the above points?

From a company's perspective, there's always the option of going off and doing your
own thing. But Jupyter doesn't have this option. In its current state, Jupyter's resources
are contrained to the groups that decide to participate. To that extent, a few
things that we need to improve:

* Make it easier for others to open new topics of discussion with
  the Jupyter community in a "formal" decision-making process. I think
  [recent efforts to improve the Jupyter Enhancement Proposal](https://github.com/jupyter/enhancement-proposals/issues/27)
  process are a great start. This should make it easier for stakeholders to voice
  their concerns and needs in an open way that allows many in the community to
  participate.
* Find a way to avoid the "governance by resources" trap. Many open projects in the
  tech community adopt a model like "you have decision-making power
  that scales with the resources you devote to the project". That's fine if everybody
  has a similar amount of resources, but many of Jupyter's stakeholders don't.
  If we want members of the
  educational and scientific/academic community to participate, or people that aren't
  represented in the current tech and data industry to participate, we need to find a
  way that **encourages the contribution of resources** from organizations that have
  them, but that **normalizes decision-making power** so that resources don't guarantee
  you a larger voice than others. Ultimately, the goal of the Jupyter project is
  to create public goods that benefit everybody, and I fear we'll lose sight of this
  goal if you need to be able to fund a team of developers in order to participate
  in the project.
* Vest power in more systems and processes, rather than in individual people. Part of
  the challenges currently facing Jupyter is that it began as a relatively small project
  with a tight-knit team of developers that all knew each other. In that case, it made
  sense to adopt a traditional BDFL+governing council kind of model. It's now clear that
  this model is inadequate at balancing the nuanced issues described above. Given the
  complexity of Jupyter's community, I think that we need to move away from thinking about
  individual people as the sources of power, and instead think about a *system* that
  divides power in intentional ways, as well as a *process* for how individuals can
  move through that system in a way that addresses some of the concerns above.

So there are a few thoughts of my own, and I look forward to seeing how others feel
moving forward. There's a lot happening in the Jupyter ecosystem,
and I'm excited to be a part of it.
