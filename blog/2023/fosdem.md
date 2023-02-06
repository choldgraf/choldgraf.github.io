---
tags: cloud
date: "2023-02-06"
category: "report"
---

# Reflections from FOSDEM23: the beautiful chaos of open source in a conference

I recently attended [FOSDEM 2023](https://fosdem.org/2023/), my first FOSDEM!
I had heard of the conference before, but hadn't really looked into it too much.
Fortunately, after some urging from friends and social media, I took a deeper look and decided I should join to see what all the fuss was about.

Here are a few things that I noticed while I was there.

## FOSDEM is beautiful chaos

I feel like FOSDEM tries to bring the "beautiful chaos" of open source communities into a conference setting.
There's no registration, and little "conference infrastructure" compared to other conferences of its size and scope.
People who attended for the first time seemed to be overwhelmed in a similar way to when they navigate a large open source community for the first time.

The conference relies heavily on volunteer labor, and only has a few roles and responsibilities where they deploy paid resources and equipment.
Generally speaking, this seemed to work surprisingly well!
The conference is **very big**, and the fact that thousands of people can swarm a university in Brussels and largely have a productive time is a testament to FOSDEM's ability to self-organize.

## But yes, it is very chaotic 🙃

That said, the chaos occasionally gets in the way of having a good conference experience.
I probably spent 20% of my time being confused about how to find the talk I was trying to attend, and it didn't help that the [ULB Campus](https://www.ulb.be/en) is large and hard to navigate.

There was also a lack of organization-wide policy and enforcement for a few high-level things.
For example, there didn't seem to be any kind of official policy towards COVID and masking procedures.
The general vibe seemed to be "if you're feeling sick you should probably wear a mask or stay home", but there was no mechanism to enforce this.
Some sessions had facilitators with stronger opinions on this, some had less-strong opinions, but your experience depended a lot on the specific groups you were hanging around with.

I suspect that this makes FOSDEM less accessible.
Without a strong policy for community behavior in certain key areas, people will not know what to expect when they arrive.
With enough uncertainty over important topics (e.g. if a person who really needs to avoid COVID), some people will simply filter themselves out.
I bet this is one place where FOSDEM suffers from its lack of structure or resources - something like setting and enforcing a COVID policy takes a _lot_ of work and resources.
It reminds me of the community policing and policy-setting parts of open communities that are often under-apprciated, very stressful, and very complex.

## It is HUGE, as is the open source community

FOSDEM reminded me just how gigantic the open source community is.
I tend to spend my time in the scientific python and open research space (there was an [Open Research Tools and Technology devroom](https://fosdem.org/2023/schedule/track/open_research_tools_and_technology/)), but this was just a _tiny_ part of the FOSDEM conference.

I often think of [Project Jupyter](https://jupyter.org) as a "large" open source project, but you really get a feel for how tiny it is when see how many people show up representing [Fedora Linux](https://getfedora.org/).
There are large and complex communities out there, with their own stakeholder dynamics and focus areas.
A place like FOSDEM is an opportunity to cross community boundaries and learn about the problems others have, and how they're trying to solve them.

## All of our communities have the same problems

And on that note, every community seems to have the same problems.
I spoke with a number of folks from adjacent communities, and many of the stories were the same:

- We want to give sub-communities the freedom to do what they want, but find that it becomes hard to get everybody moving in the same direction.
- We have a few large stakeholders that employ people to work directly on the project, and this gives them a level of power that many are not comfortable with.
- We have a hard time attracting new core contributors unless they end up working at a specific subset of companies.
- We are worried about company XXX building a similar tool that competes with our open source project because they didn't want to abide by our community governance.
- We systemically under-resource community guidance, management, and strategy efforts.
- We are worried about our increasing reliance on a software and services that are controlled by a few giant tech companies.

The list goes on.
In some ways, this was reassuring, the problems in all of my communities are certainly not unique.
In other ways, it was discouraging that so many of these projects have the same problems and yet none have really managed to solve them.
Maybe that's because solving these problems can't happen with a single action, but more like a series of mini-solutoins and continued improvements over time.

## It is really a bunch of mini-conferences all strung together

As a result of a general lack of structure, FOSDEM really felt like a bunch of little conferences all strung together.
The main "unit" of the conference is a [**devroom**](https://submission.fosdem.org/submission/devroom), which is a way to organize talks and people around a particular subject.

Many people seemed to pick a single devroom and stick with it the whole time.
You could also tell that there was a lot of cultural correlation between people in the same devroom, so you could have more consistent behavioal norms within each one.
Devrooms were places where colleagues were more likely too meet up with each other, and the way to ensure you're meeting other people with similar interests.
You heard statements like "I'm going to spend the day hanging out in the security devroom."
Some of the devrooms even provided their own baked goods and snacks for those who attended!

If I go to FOSDEM again, I'll pay more attention to the devrooms and pick one to three where I should hang out and learn.
This seems like a better strategy than cherry-picking each talk.

## The community devroom is pretty great

The devroom where I spent the most time was [the community devroom](https://fosdem.org/2023/schedule/event/welcome_community/).
Perhaps unsurprisingly, I really enjoyed the talks that I heard, and felt that most people there came with a similar perspective to myself.
I was happy to see that there was so much emphasis on the human and community aspects of open source, especially in light of recent [cultural tensions in the "Free Software Foundation" world](https://arstechnica.com/gadgets/2021/04/free-software-foundation-and-rms-issue-statements-on-stallmans-return/).
It was worried that there would be a "it's just code, don't bother me with human problems like diversity and inclusion" vibe, but for the spaces that I participated in, this was not a huge issue (I suspect it would have been different in other devrooms).

## "We don't do that here" is a nice tool for policing behavior

One thing that stood out to me was the following phrase[^thx]:

> We don't do that here.

This described a way to politely but firmly tell somebody that their behavior wasn't acceptible in a community.
It is a way of making expectations clear without opening the floor up for debate about the cultural expectations themselves (there's a time and a place for this, but the middle of a violation of that culture is not the moment to debate it).
I'll spend more time thinking about this and how I can practice it in my own work.

[^thx]: This was originally [written about in this blog post from Aja Hammerly](https://thagomizer.com/blog/2017/09/29/we-don-t-do-that-here.html) and described at the conference in [a talk by Floor'd](https://floord.github.io/) for teaching me about it in their talk.

## People were more explicit about their open-source and employer hats

One thing that I felt in almost all of the devrooms was a tension between "corporate" and "non-corporate" tech.
On the one hand, you have those driven by ideals and values who believe in "Free as in speech" open source and see corporations as inherently mis-aligned with those ideals.
On the other hand, there's representation from a _lot_ of big tech companies at the conference and they clearly see it as a strategically important conference to attend.
This is something that I've felt in basically every tech conference, but especially felt it at FOSDEM[^other-conferences].

[^other-conferences]: Perhaps that is because the corporate side of tech has largely won the battle in many other tech conferences that have become expensive and inaccessible to many people who refuse to join the corporate secetor.

One way that this became clear is the fact that more people spoke about "hats" at this conference than I usually notice.
I heard several stories of people intentionally not attending their company's booth because they explicitly wanted to attend via their affiliation to an open source project.
In some cases I heard of people not reimbursing their expenses because they didn't want to feel beholden to their employer's strategy at the conference.
I thought that was pretty cool, as I'm a big fan of recognizing that employers and open source communities have distinct missions and goals.

## More conferences need to be free

Finally, it really stood out to me that FOSDEM was free for **anybody to attend**.
I had many conversations with people who noted that they wouldn't have attended if they had to pay a significant cost to do so (travel and hotels is already expensive enough!), and the extra effort of requiring "applications for financial aid" is both off-putting and a burden (why should people have to do extra work to attend just because they don't make as much money?).

I wish that more conferences found a way to make attendence **free with zero extra effort from attendees**.
For example, I [really like how Open News prototyped a "pay what you can" model](https://source.opennews.org/articles/one-easy-way-make-conference-ticket-prices-more-eq/) for their annual conference.
If that means that we need to say in cities and venues with lower cost, and lower our production values a little bit, then I think that is 100% worth it.

I know that it takes (some financial) resources to run something complex like a conference.
But come on, many of the organizations represented there have market capitalizations in the billions, we should be able to find a way to subsidize many tickets down to zero.

## A conference that reflects the open source community

It really is extraordinary that a conference like FOSDEM exists in the first place.
The fact that thousands of people around the world just...show up in Brussles and arrive at the same place without any official registration is pretty cool.
It reminds me of the ways that many people are surprised when they first learn how open source communities work.

And just as with open source communities, I suspect that there is **a lot of unpaid and under-appreciated labor** that goes into organizing FOSDEM.
So a million thanks to the organizers and those who participated.
It is a conference format and a cultural phenomenon that shows off the power of open community models (as well as some of its challenges).
Maybe I'll see you in a devroom next time!
