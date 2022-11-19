---
tags: python conferences communities jupyter
permalink: summer-conferences-2018
category: conferences
date: 2018-08-01
---

# Summer conference report back

This is a short update on several of the conferences and workshops over the
summer of this year. There's all kinds of exciting things going on in open
source and open communities, so this is a quick way for me to collect my
thoughts on some things I've learned this summer.

## SciPy

### The Pangeo project demoed their JupyterHub for big-data geoscience

Pangeo is a project that provides
**access to a gigantic geosciences dataset**. They use lots of tools in the
open-source community, including Dask for efficient numerical computation,
the SciPy stack for a bunch of data analytics, and JupyterHub on
Kubernetes for managing user instances and deploying on remote infrastructure.
Pangeo has a neat demo of their hosted JupyterHub instance that people can use
to access this otherwise-inaccessible dataset! See their video from SciPy below.

<iframe width="560" height="315" src="https://www.youtube.com/embed/2rgD5AJsAbE" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

### Wholetale shared some ideas on getting data to work with reproducible pipelines

Wholetale is a collection
of technology that makes it easier to do reproducible work. It is NSF-funded,
so tries to be fairly open about how it interfaces with the ecosystem around it.
They Wholetale team gave an interesting talk about how to handle **data in
reproducible environments**. This is a big unsolved problem in the space, since
datasets are often difficult to ship around or copy, and it doesn't usually make
sense to bake them into things like container images.

Check out their presentation below

<iframe width="560" height="315" src="https://www.youtube.com/embed/X0UX4bW_4w0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

### Binder 2.0 was unveiled!

Min Ragan-Kelley and I presented Binder 2.0 on
behalf of the Binder community. We talked a bit about the philosophy behind Binder,
how we connect with the broader open-source ecosystem (hint: BinderHub is 70% jupyterhub),
dove into the technical pieces a bit, and laid out some ideas for how Binder can
grow in the future. We'd love to see a world where there are **BinderHubs all over
the scientific landscape** (e.g. "binder.berkeley.edu") that users can select based
on their institutional affiliation or address.

In addition, the Binder team collaborated on [a "Binder 2.0"
paper](https://github.com/scipy-conference/scipy_proceedings/pull/386),
which will be published in the proceedings from SciPy. Hooray citable
research artifacts!

Here's our Binder talk:

<iframe width="560" height="315" src="https://www.youtube.com/embed/KcC0W5LP9GM" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

## PEARC

PEARC is a scientific and research computing conference held each year. It's
interesting because it exists at the intersection of a few different communities.
As the scientific world has become more "data-intensive", new parts of the academy
overlap with technical infrastructure that was traditionally just for physics/
astronomy/simulation kinds of folks. PEARC is (sort of) where a lot of "old school"
and "new school" parts of research infrastructure intersect.

### Lots of high-performance computing centers use JupyterHub

Perhaps the most exciting thing I noticed was how much chatter is in the HPC
world around JupyterHub on high-performance compute. I think this makes sense,
since JupyterHub provides an interface people are familiar with, and obviates
the need to be a skilled computer scientist just to interact with high-performance
hardware.  In particular, the [Minnesota Supercomputing Institute](https://www.msi.umn.edu/)
and the [National Energy Research Scientific Computing Center](http://www.nersc.gov/)
showed some promising examples of providing access to large-scale compute via an
interactive environment that was hosted by JupyterHub.

### HPC centers are curious about Kubernetes

There was also a lot of talk about Kubernetes at the conference, though it was
clear that many people simply didn't have the experience with it to know whether
it was a "good" option or not. Systems administrators tend to be lower-case "c"
conservative when it comes to technology, and it seems that this community
is lagging behind the tech world by many years when it comes to the adoption
of "cloud" technologies. Hopefully we'll see more experiments with Kubernetes
in the HPC world, and that people report back their experiences as this happens.

### Research computing has a weird relationship with cloud companies

A lot of research computing folks also expressed some combination of excitement
and hesitation at outsourcing their computing to large-scale cloud companies
(such as Google, Amazon, or Microsoft). On the one hand, paying Google to
run your compute means you can accomplish some things for less money. On the other,
it's hard to avoid building an institutional dependency on a single company's
technical infrastructure. Once you've got that 100 petabyte dataset hosted with
one company, it'll probably be staying there for quite a long time. All the cloud
companies are offering "free" services to cool-sounding research projects right now,
but never forget that many of these companies have built business models on converting
"free-tier" customers into locked-in paying customers. A few HPC people shared
stories along the lines of "well they said it would be free to host our scientific
data, until they started sending us bills for it several years later."

### We gave a JupyterHub and BinderHub on Kubernetes tutorial

Last week, Aaron Culich, Jessica Forde, Felix-Antoine Fortin, and I presented a
day-long tutorial on deploying JupyterHub and BinderHub with Kubernetes. You can
[find a copy of our slides here](https://bit.ly/pearc-2018-jhub). In particular, I'm
excited to see some improvement in the methods for deploying Kubernetes on
OpenStack. OpenStack is *much* more common in scientific research, and exists
on pre-existing hardware. Deploying **Kubernetes on OpenStack** would open up this
technology to the academic community in a way that won't happen with cloud
companies any time soon. In particular, Felix shared [Etienne's terraform scripts
to deploy Kubernetes on OpenStack](https://github.com/etiennedub/terraform-binderhub).
I'd love to see people try this out and report back their experiences.

## Open Source Alliance for Open Scholarship

Finally, I attended [a meeting in New York
City](https://osaos.org/convening-the-community-looking-towards-the-future/) organized
by [OSAOS](https://osaos.org/about-us/). What's OSAOS? My take is that it's an
organization dedicated to building connections, best-practices, and leadership
between organizations in open scholarship (AKA, organizations that operate on
open principles with a goal of creating and sharing knowledge). More than anything,
I am thrilled to see more interest in the "soft skills" side of open communities.
It's easy to treat all of these things as technical projects, but in my experience
the biggest challenges are social and systemic, and won't be solved with code.
However, leaders of open groups are often isolated, underappreciated, and don't
have a lot of training in how to lead communities and projects. It's great to see
organizations such as OSAOS trying to improve this!
