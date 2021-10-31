---
tags: open source, governance, community
permalink: signaling-openness
category: open source
date: 2018-10-26
---

# How do projects signal how "open" they are?

How do open projects signal their "openness" to the outside community? This is
a really hard question, particularly because nowadays "open" has become a buzzword
that doesn't just signal a project's position to the community, but is also used
as a marketing term to increase support, users, or resources.

I was thinking about this the other day, so decided to take to twitter:

{% twitter https://twitter.com/choldgraf/status/1054478362209480704 %}

I was surprised at how much this question resonated with people. Here are a few
highlights from the (very interesting) conversation that came out of that question.

## Some discussion threads

### Wishes vs. reality

Tal immediately brought up a really important point: many projects *want* to be
inclusive and welcoming to others, but they don't have time to do so.

{% twitter https://twitter.com/talyarkoni/status/1054484496769314818 %}

I think this is an important distinction, and something that should be signaled
clearly. One the one hand, if a person generally wants others to contribute to
the project, then they're some degree of openness higher than a project that
actively discourages this.

On the other hand, running open projects *does take work*,
and a project that says "well I'd like to be open but can't commit the time to do it"
also isn't *that* open in practice. No hard feelings there, but I think that
the goal of defining a "degree of openness" isn't to signal a value judgment on the
people related to the project, but on the project itself. If you really want to
grow an open community around a project, you need to dedicate time and resources to
the community itself, not just the technical pieces of the tool.

## Metrics of openness

That leaves open the question: "how do we measure the **practical** openness of a project,
rather than just what it **says**?". A few folks mentioned that the CHAOSS project
does a lot of work in this gneeral space:

{% twitter https://twitter.com/abbycabs/status/1054492219808403457 %}

CHAOSS defines standards for metrics to collect about communities. They don't necessarily
say what others should **do** with those metrics, so perhaps that's on the open community
to define for themselves.

Personally, I'd love to see more tooling that makes it possible to scrape activity
statistics from open repositories. Tal and others suggested a few things:

* time to initial response to new issues (maybe separated by new vs. old contributors)
* inequality coefficient for contributor commits
* number of unique organizations/email domains in contrbutors
* use of positive/welcoming language
* explicit roles defined, and pathways towards working more with the community

I'd love to see more thoughts along these lines. If we could define a collection of
metrics around openness, it'd paint a much more rich picture than simply "does this
project have a permissive license."

There was also a specific metric around governance that's worth highlighting:

{% twitter https://twitter.com/GeorgLink/status/1054621070945329152 %}

The paper linked above is a study that investigated "open governance" in a number of
open-source mobile projects. It's an interesting exploration of the ways that
decision-making is made (and signaled) in several projects. Perhaps unsurprisingly, they
conclude that "more open" projects are most-likely to be successful in the long term
(with a few exceptions).

Finally, apparently there's also a "badge" to signal the status of a repository (is it
active, vaporware, abandoned, etc):

{% twitter https://twitter.com/parente/status/1055053470808580098 %}

I'd love to see more of these semi-automated signals to help guide the open source community
in deciding what projects to adopt and contribute to. As more and more people do
their work online and in the open, it also creates a challenge of sifting through the noise
to make the most of your (limited) time and energy. Having better metrics like these will
make these decisions easier.

### Mozilla's archetypes of open projects

One of the most fascinating links I found was Mozilla's "archetypes of open projects"
document:

{% twitter https://twitter.com/neuromusic/status/1054517145436975104 %}

Briefly, this is an internal document that Mozilla made public. It attempts to define
the different kinds of open projects that exist. Importantly, it also explains the
value propositions of each, how it can be used strategically within an organization, and
how it supports (or doesn't) an open community around it.

I added some thoughts about how Project Jupyter fits into these archetypes on the
[Jupyter governance research issue](https://github.com/jupyter/governance/issues/60#issuecomment-432766439)
and I'd love to think more about how these archetypes fit into the pre-existing open communities
that are out there. If anybody wants to brainstorm how these archetypes fit into the scientific
open community, I'd love to chat :-)

On that note, I want to give a brief shout-out to Mozilla in general, which has
either conducted or sponsored a bunch of interesting work in open projects.
For example, they have a whole wiki dedicated to working openly:

{% twitter https://twitter.com/alex__morley/status/1054483982040121344 %}

and they also run lots of training and community programs such as the
[Mozilla Open Leaders](https://foundation.mozilla.org/opportunity/mozilla-open-leaders/) program.
Project Jupyter is in this year's cohort and [keeping track of its progress here](https://github.com/jupyter/governance/issues/57).


### Importance of ethnography:

A final note on the importance of ethnography:

{% twitter https://twitter.com/mmmpork/status/1054745690897711104 %}

For all of my talk about metrics above, I've come to appreciate that numbers
are **never** sufficient to describe the complexities of a community or group.
Over the last several years at the [Berkeley Institute for Data Science](https://bids.berkeley.edu),
I've had the pleasure of working with several ethnographers who have shared their
perspective on how to study communities. Semi-automatically-calculated numbers can
be a great way to see relatively coarse-level view of a community, but if you really
wany to understand what's going on, you need to dig in there, conduct qualitative interviews,
operate in the community, and create some stories that back up (or not) the quantitative
data that you collect. We'd all be better off if there were more ethnographers in our
respective communities <3.

OK, that's enough for now - I hope these links are useful and I'll try to
update them over time if I hear of some new projects along these lines.
If you have any suggestions, feel free to leave 'em in the comments!