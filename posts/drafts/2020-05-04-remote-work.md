---
tags: open communities
redirect: 2020-05-04-remote-work
---

# A few tips for working remotely

Now that many have shifted to some form of remote work, I've had quite a few
conversations where others were asking for best-practices or tips in working in
distributed and remote teams/communities. Most of my work over the past few years has been
remote in some form or another, so here are a few things I've learned in the process.

:::{admonition} `tl;dr`
:class: tip
There are a million things to consider in organizing remote teams and communities, but here are three that I've found important: be *explicit*, *discoverable*, and *consistent*.
:::

## Guiding principles

There should be **explicit** places for conversation, explicit roles, explicit expectations for behavior.
Where you prefer to be wishy-washy about things, be *explicitly wishy-washy* so people know
it's intentional.

All of the information relevant to your group should be in a **discoverable**, obvious place
that is accessible to everyone (unless explicitly stated that some do not have access).
These locations of information should be treated as "canonical" sources of truth, and avoid
important information existing anywhere else -
minimize "back-channels" especially if it conflicts with publicly-available
channels ("oh the zoom link on that page isn't correct anymore, it's actually a different one").
Avoid having clusters of information islands in the team ("oh we actually submitted that proposal yesterday, sorry for not pinging the group")

Finally, processes should **be carried out the same way for everybody** and over time. Don't
deviate from the process unless everyone agrees that the process should be changed. Don't
let certain people in your community get special treatment (unless that is made explicit
in your team rules).

### A red flag to look out for

A red flag to keep an eye out for is *"oh, sorry about that"*. This is often in the context
of a miscommunication or member of the team having mis-information. As in, "Oh, sorry,
we moved the meeting to Wednesday instead of Thursday". While "oh, sorry" usually means there was no harm _intended_, it is often a symptom of broken team information flow and communication.

Usually, tension comes in remote settings because of unintentional team practices, and
unequal access to information is one of the most-common. If you find team members consistently
apologizing to others for not keeping them in the loop, consider re-working your team's
remote work practices.

## General resources

I have found a few super useful general tools for managing online organizations etc. Here are two of them:

* [GitLab's remote work guide](https://about.gitlab.com/company/culture/all-remote/guide/) is
  an excellent overview and general guide about *many* aspects of running a remote company.
  (GitLab is a ~1000+ person company and is fully remote, so they are experts in this topic)
* [The Mozilla Open Leadership Framework](https://mozilla.github.io/open-leadership-framework/framework/)
  is another fantastic and diverse resource, particularly around managing community dynamics
  and culture in open projects. Many of the ideas here port nicely to a remote team.

## Organizing online events and projects

It's *really, really* important to have transparent and canonical sources of truth. Working remotely makes you realize how much information you get by just leaning around the corner and asking somebody. In a remote work situation, everybody needs to know where to find the information that is relevant to them, and they need to know that this information is up-to-date.  This helps avoid people feeling "left out" or being frustrated because they don't have the same information that everybody else does.

In JupyterHub we've found that it's really important to have lots of good [documentation around team processes, expectations, and resources](https://jupyterhub-team-compass.readthedocs.io/en/latest/index-team_guides.html).

## Organizing online meetings

For meetings, we've found that it's particularly important to have meeting structure ahead of time, and in a public place. We try to be pretty strict about "if you didn't put it on the agenda before the meeting, you shouldn't expect it to be discussed at the meeting". We also explicitly make space for people to give "quick updates, shout-outs, etc" which helps people give their input without needing to hold the floor for an extended period of time.

Think about what is really important to discuss in-person. Treat "synchronous" time - where everybody is paying attention at the same time - as a precious resource, and only choose to discuss things that really benefit from this style of conversation. For other things, use asynchronous communication like a discussion forum.

After the meeting, it's also important that all notes are posted in a place that the whole team has access to. Many times people cannot make the meeting (e.g. if the team is spread out around the world, at least one person will be sleeping). It's important that discussion items for those people are easily discoverable so they can follow up later on.

For example, [here are guidelines around JupyterHub meeting agendas](https://jupyterhub-team-compass.readthedocs.io/en/latest/meetings.html#updating-the-team-meeting-agenda).

And [here are meeting notes from all of our meetings](https://jupyterhub-team-compass.readthedocs.io/en/latest/monthly-meeting/monthly_report_index.html).

For the meetings themselves, it's important to have processes for when and how people start talking - otherwise you get that awkward situation where it's two people talking the whole time. It's good to have a moderator that "gives people the floor" and controls the flow of the conversation. Also good to use "non-speaking" features like the "raise hand button" and the chat window. Some people feel more comfortable asking questions via text instead of via speaker.

[Here's a blog post that covers some of this](https://chelseatroy.com/2018/04/05/how-do-we-make-remote-meetings-not-suck/).

## Organizing online discussion

Finally, it's important to have places where people have conversations "asynchronously"
(AKA, not chatting with each other live. There are a ton of places for this, but the two
big types are live chat rooms (e.g. gitter, Slack) and
online forums (e.g., Discourse). I have found that chat rooms are difficult to scale for
larger communities, and Jupyter has shifted almost entirely to
an [online forum platform called Discourse](https://discourse.jupyter.org). The benefit of
this is that it allows for people to participate more
productively over extended periods of time, and the threads are more discoverable. You
don't have to worry about whether or not you "missed a conversation"
because it's easy to loop in later on.

I really like Discourse for managing online conversation in our community, though
again it does take time to draw people to it and keep people engaged. Make sure
to have somebody that cross-links important conversations, topics, etc in the Discourse,
and encourages them to post their questions there.

[Here is a nice post about the challenges with live chat rooms](https://matthewrocklin.com/blog/2019/02/28/slack-github) such as Slack.

And here is a long thread of conversation in the JupyterHub community where we [discussed the pros/cons of Discourse](https://github.com/jupyterhub/team-compass/issues/73).

## Wrapping up

To wrap up, I want to re-highlight the three pieces from above. Information should be *explicit*, *discoverable*, and *consistent*. Following these guidelines along should make your team's work more inclusive, productive, and enjoyable.
