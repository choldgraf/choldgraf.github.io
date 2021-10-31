---
tags: python open-science dev-ops
category: dev-ops jupyterhub teams
date: 2018-05-18
---

# An academic scientist goes to DevOps Days

Last week I took a few days to attend [DevOpsDays Silicon Valley](https://www.devopsdays.org/events/2018-silicon-valley/program/). My goal
was to learn a bit about how the DevOps culture works, what are the things
people are excited about and discuss in this community. I'm also interested in
learning a thing or two that could be brought back into the scientific / academic world.
Here are a couple of thoughts from the experience.

> **tl;dr**: DevOps is more about culture and team process than it is about technology, maybe science should be too...

## What is DevOps anyway?

This one is going to be hard to define ([though here's one definition](https://theagileadmin.com/what-is-devops/)),
as I'm new to the community as well.
But, my take on this is that DevOps is a coming-together of what was once
a bunch of different roles within companies. The process of releasing technology
(or doing anything really) involves many different steps with different specializations
needed at each step. The 'old way' of doing things involved teams that'd build
prototypes, teams that would adapt those prototypes to a company's infrastructure,
teams that would maintain and service the "production" deployments, etc. The whole
process was quite slow, partially because of the lack of communication between these
very different kinds of groups.

Instead, DevOps attempts to encapsulate this entire process under one moniker. It is
generally recognized that people do have different skills and roles, but they should
be working _together_ in a group to create, mature, and ship new code iteratively
and as a single continuous process. DevOps is intently focused on "[agile processes](https://www.versionone.com/agile-101/)",
and values being quick and lightweight, focusing on metrics like "time between development
and deployment." This is only possible with a large focus on team dynamics and
how the relationships between people with different skillsets and responsibilities
should work with one another effectively. Perhaps unsurprisingly, this is the
kind of thing that people talk about **a lot** at DevOps conferences (well, at least
at the one I went to).

## DevOpsDays was more about people than tech

More than anything else, what struck me was how little emphasis was paid on
the technology itself. There are a billion moving parts in the cloud orchestration
and container technology space, but they got relatively little discussion time at
the conference (with the exception of [Jennelle Crothers](https://twitter.com/@jkc137)
talking about how Microsoft was trying to make its Windows containers super lightweight,
which was pretty neat). In general the only people consistently talking about
the greatness of XXX new software/tool/etc were salespeople trying to
get you to buy their product. Instead, the vast majority of conversations,
discussions, brainstorms, etc were about **people** and **process**, not
technology per-se.

Obviously, it's difficult to disentangle the tech from the people when
you're in the tech industry, but it was illustrative to see the
relative focus that got placed on the "squishier" questions. For example,
a few that came up pretty frequently:

* How can we disseminate information across a distributed team most effectively?
* How can we create a team culture that welcomes newcomers?
* How can we avoid alienating members of the team?
* How can we avoid single points of failure in the team?
* How can we do things faster, more efficiently, and more reliably as a team?

It's no coincidence that the word "team" was in each of the bullet points above.

## Scientific DevOps?

As a member of the scientific / academic community, this is quite interesting
to me. A whole conference where people talk about creating positive culture and effective
yeams? Yes please. However, I realize that the incentives and
problems associated with DevOps are not the same as those faced by scientists. For
example, a big part of DevOps (and SREs more generally) is ensuring that services,
tools, and sites are reliable and stable over time. You can design tech around this
idea all you want, but at some point you'll need a team of people to manage that tech.
The DevOps world has seemed to realize that this means the social dynamics of that
team are just as important as the technology itself, which is a breath of fresh
air.

I wonder what scientific DevOps would look like. Scientists are theoretically also
operating in team-based environments (at least, the ones in scientific labs). The
incentives of reward and recognition are totally misaligned, but it's still the
case that successful teams produce more effective work in general. Perhaps it's
worth exploring how the DevOps take on operations and team dynamics ports to
the academic scientific community.

## Open and (relatively) diverse culture

A final point that I noticed was that, relative to other tech conferences I've
attended, this one had a general air of positivity and open culture. There were
all kinds of people there, and while the general makeup of attendees definitely
still had a lot of white dudes in it, the room nonetheless never felt like it was
_dominated_ by this group of people. There was also a great culture of supporting
people as they were giving talks - some of the speakers were clearly more nervous
than others, and the audience did a good job of trying to disarm their anxiety.
Perhaps this is the kind of culture that comes with a profession that depends on
(and focuses on) team dynamics and culture.

Ultimately, as with any good conference, I left having more questions than answers.
How can scientists improve their own team dynamics using principles from the
DevOps community? How can the open-source community do the same but for distributed team
workloads and responsibility? Where is the balance between "solve this with tech" and
"solve this with people"? How can we encourage more cross-talk between the world of
scientific research and the world of tech? Either way, it was an interesting and
informative experience, and I'm looking forward to learning more about this community.


## Highlights and takeaways
* Amy Nguyen and Adam Barber shared their strategies for taking a [data-driven approach](https://www.devopsdays.org/events/2018-silicon-valley/program/amy-nguyen-adam-barber/) to user interface / experience design.
    * *Always collect data* from people you design things for.
    * Put in the legwork to interview and gather diverse perspectives before you build tools.
* Fatema Boxwala ([@fatty_box](https://twitter.com/@fatty_box)) shared her experience as an intern, and gave some pointers for how to create a welcoming and productive environment for intern positions.
    * Don't forget that interns have lives too. If they just moved to a new city, help them settle in.
    * Align your intern's project with something a team member (or yourself) will be actively work on.
* Katy Farmer ([@TheKaterTot](https://twitter.com/@TheKaterTot)) reminded everybody that teams shouldn't _automatically_ aspire to use the workflows that gigantic tech companies use.
    * Just because it works for a big tech company doesn't mean it'll work for you.
    * Being a smaller-sized company isn't better or worse, it's just different. Don't treat company size as a reflection of quality, and don't assume larger companies do operations more effectively.
* Frances Hocutt reassured everybody that it's OK if your tests wouldn't satisfy a production-level standard _all the time_.
    * Make sure your tests reflect _the current state of your code_.
    * Don't let perfect be an enemy of good. Testing 10% of the code is still better than testing 0%.
* Jennelle Crothers ([@jkc137](https://twitter.com/@jkc137)) described how Windows is trying to shrink images that run Windows so that you can run them in containers more easily.
    * It turns out that shrinking something from several GB to a few hundred MB makes it much easier to ship around :-)
    * As an aside, it's fascinating to see Microsoft focus on integrating itself with the container ecosystem (as opposed to trying to replace or compete with it). Maybe they really have learned something from their "[linux is a cancer](https://www.theregister.co.uk/2001/06/02/ballmer_linux_is_a_cancer/)" debacle.
* Adrian Cockcroft ([@adrianco](https://twitter.com/@adrianco)) explained the importance of creating a [culture of reporting and logging](https://www.devopsdays.org/events/2018-silicon-valley/program/adrian-cockcroft/) incidents, even the small ones!
    * Instrument and study the "non-events" - look for "near-misses" and outliers. Never throw away information just because something catastrophic didn't happen.
    * Plan and practice for chaos! What will your team do if "everything goes wrong"?