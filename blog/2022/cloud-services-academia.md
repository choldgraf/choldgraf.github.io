---
tags: cloud
date: "2022-09-05"
category: "reports"
---

# Ask Twitter: Why don't academic researchers use cloud services?

_this is an experiment at making my [Twitter conversations](https://twitter.com/choldgraf) a bit more useful and archivable over time. It's going to be a bit messy and unpolished, but hopefully that makes it more likely I'll actually do it :-)_

Over the past decade, cloud infrastructure has become increasingly popular in industry.
An ecosystem of modular tools and cloud services (often called [the Modern Data Stack](https://future.com/emerging-architectures-modern-data-infrastructure/)) has filled many data needs for companies.

However, academic research and education still largely does not utilize this stack.
Instead, they optimize for local workflows or shared infrastructure that exists on-premise.
If you believe (as I do) that cloud infrastructure has the potential to help people do work more effectively and collaboratively, then it's important to understand why people don't use these kinds of tools.

So, I decided to ask Twitter why academics tend to not utilize cloud infrastructure:

% This script is what renders the tweets
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

% This is the structure used for tweets 
% example: https://publish.twitter.com/?query=https%3A%2F%2Ftwitter.com%2Fcholdgraf%2Fstatus%2F1564614538309390345&widget=Tweet
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">
  <a href="https://twitter.com/choldgraf/status/1564614538309390345">tweet</a>
</blockquote>

Below is a brief summary of the major points that several people made.

## Fear of high costs

The most common challenge is the fear of over-running cloud costs.
With on-prem infrastructure, you pay for allotments of time up-front (or don't pay at all).
Cloud infrastructure allows you to "pay as you go", but this sometimes means _over-paying_ if you used resources you didn't expect:

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">
  <a href="https://twitter.com/anshulkundaje/status/1551585264262295552">tweet</a>
</blockquote>

**Cost monitoring needs to be a more obvious part of cloud services**.
Fortunately, most cloud providers have their own budgeting and cost monitoring services to prevent this from happening.
However, these don't seem to be well-understood or utilized.
That brings us to the next concern:

## A confusing landscape of tools and services

There are hundreds of cloud services for data workflows in existence.
All of them make one thing a little bit easier, but you still need knowledge to:

- Choose the right cloud services
- Integrate them together

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">
  <a href="https://twitter.com/cboettig/status/1564671199547838464">tweet</a>
</blockquote>


As a result, many cloud services that _might_ be useful are effectively not used because they get lost in all the noise out there.

In short, **researchers need support in navigating this space**.
They need organizations to understand their workflows and recommend a few specific things to use instead of exposing them to the hundreds of options out there.

## High start-up costs and no DevOps experience

Even if you _do_ find the set of services that you want, you need some way to expose these services to your collaborators or research group.
You also need to manage this integration over time as things change, break, etc.
University groups often do not have dedicated cloud expertise, and so this lands at the feet of post-docs and graduate students with energy and interest to try things out.

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">
  <a href="https://twitter.com/ixek/status/1565645082275057664">tweet</a>
</blockquote>


However, asking a student to learn and run your cloud infrastructure is also a risky move.
Students move on, and DevOps skills are in high demand.
What happens if you lose that person, or if your grant runs out?

**Researchers need others to manage cloud infrastructure for them**.
Integrating and using most services still requires expertise similar to a systems administrator (but now with cloud infrastructure as well).
We need more services that manage this complexity for them.

## Pain to first compute is higher for cloud

Universities recognize that managed services are useful to research - they just prioritize on-premises infrastructure over everything else.
For example, many people noted that HPC is more heavily used simply because the university puts most of their resources into easing the use of this infrastructure.

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">
  <a href="https://twitter.com/SpectralFilter/status/1564697622660763648">tweet</a>
</blockquote>


**Universities need to invest in lowering the energy barrier to cloud services as well as on-prem infrastructure**. We don't want universities to divest from all of their on-prem hardware and services, but we should make at least marginal investments in similarly reducing the barriers to using cloud infrastructure. What would it look like if universities made it as easy to set up and pay for cloud infrastructure as they do for HPC? I bet a lot more people would experiment and learn with the cloud.

## Continuity of service / lock-in concerns

When you're relying on a service exposed by some other organization, you must hope that the service continues to be useful.
Many academics have been burned when services discontinue.

This might happen for a number of reasons:

- An **internal service** discontinues because the organization no-longer has capacity to manage it themselves. This is particularly challenging in the context of research funding, which tends to be "boom or bust".
You get a grant and are well-funded for 3 years.
After it runs out, maybe you've got a few months of a gap without dedicated resources for infrastructure.
What happens if your DevOps person's salary depends on that grant?
- An **external service** discontinues because the organization running it pivoted to a new model or cost structure. This is challenging because many cloud services are designed for enterprise, the research community. They are also not accountible to the research community, and do not give it direct representation or governing power over the direction of the services.

Moreover, when our workflows are not easily portable, it creates extra switching cost and strain on a researcher's workflow.
Many services (both external and internal) do not properly leverage pre-existing and modular tools to make it easy to switch (and why would they, if they're optimizing for their own growth over the growth of the ecosystem).

**Researchers need cost-sharing mechanisms for cloud infrastructure that is designed for them**.
This would allow them to pool their resources and ensure continuity and quality of service without relying on boom and bust cycles of single grants.[^funding-ideas]
It would also allow them to support reliable and sustainable services that are designed for the unique problems that the research community has (like being a huge, globally-distributed, heterogeneous community with almost no top-down control and thousands of different workflows).

[^funding-ideas]: A few quick ideas: central funding from universities, multi-year grant allotments from funding agencies, asking users to pay the cost of running the service for them, asking organizations to pay for infrastructure onbehalf of their users, philanthropic gifts to cover costs on behalf of a group of users. Really it'll need to be a subset of all of these things.

## Wrap-up: we need more cloud-native services for research

Others shared a few examples of successful cloud services.
For example, the [CyVerse](https://twitter.com/astrochunly/status/1564620778443718661) project was largely seen as helpful to academics, though it depended initially on NSF funding to support it and so did not develop a self-sustaining cost recovery model.
Other projects like [Pangeo](https://pangeo.io) have shown the value that hosted infrastructure can bring to distributed communities that wish to standardize on similar tools, workflows, and data.[^ithaka]

Ultimately, it sounds like what we need are a combination of two things:

- More organizations that are dedicated to serving cloud infrastructure to the research community. These should experiment with various models of service delivery as well as cost recovery to provide stable and reliable services for many stakeholders.
- More bureaucratic innovation at easing cloud workflows in large research organizations. These should reduce the artificial barriers to using and paying for cloud infrastructure, to make it easier for researchers to experiment with the cloud and learn how it can be most useful for their work.

I hope that [2i2c](https://2i2c.org) can help be a part of the solution here - I think there's a lot of potential for impact!


[^ithaka]: Apparently there's also [a great landscape analysis from Ithaka](https://sr.ithaka.org/publications/big-data-infrastructure-at-the-crossroads/) that I have yet to read but it looks promising.
