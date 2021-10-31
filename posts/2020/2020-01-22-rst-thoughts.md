---
tags: markup, documentation
redirect: 2020-01-22-rst-thoughts
date: 2020-01-22
---

# What do people think about rST?

Publishing computational narratives has always been a dream of the Jupyter Project,
and there is still a lot of work to be done in improving these use-cases. We've made
a lot of progress in providing open infrastructure for reproducible science with
[JupyterHub](https://jupyterhub.readthedocs.io/en/stable/) and
[the Binder Project](https://mybinder.org/), but what about the documents themselves?
We've recently been working on tools like [Jupyter Book](https://jupyterbook.org),
which aim to improve the writing and publishing process with the Jupyter ecosystem.
This is hopefully the first post of a few that ask how we can best-improve the state
of publishing with Jupyter.

:::{admonition} Update!
:class: tip
Many of the ideas in this post have now made their way into a new flavor of markdown called [Markedly Structured Text](https://myst-parser.readthedocs.io), or MyST. It brings all of the features of rST into Markdown. Check it out!
:::

Python has a fairly sophisticated publishing tool in its stack. [Sphinx](http://sphinx-doc.org/)
has been a staple for publishing documentation for packages for several years now.
Interestingly, publishing a book is more similar to publishing a package's documentation
than it is to, say, publishing a blog. Maybe we could use Sphinx more heavily for
writing computational narratives.

One of the major challenges with Sphinx is that its default markup language is reStructuredText,
a fairly old but battle-tested markup language. The benefit of reStructuredText is that it is
a *semantic language*, meaning that it has ways to store more information about the nature
of the text (e.g. something is an "author", something is a "reference", etc). It is also a standard
that has remained very stable over time (whether that's a good or bad thing I'll leave to you to decide).

However, there are a few major problems with reStructuredText that have impeded its adoption by
communities outside of the Python documentation world. I recently [asked around on Twitter](https://twitter.com/choldgraf/status/1212054861132521472)
what these problems were.
I got some interesting responses! Here is a quick summary of people's thoughts.

# The syntax of rST is too confusing

By far the most common response was that rST syntax is simply too confusing. Here were the main
pain points.

## Link syntax

Many folks particularly mentioned that they needed to look up how to construct links every time they wrote rST.

For reference, a link in rST looks like this:

```rst
This `Is a link to <https://google.com>`_.
```

Compared with markdown:

```
This [is a link to](https://google.com)
```

## Header complexity

rST uses "setext" headers, which means that you put a bunch of underline-like
characters under (or under+over) the header name itself, like so:

```rst
This is my first header
=======================

======================
This is another header
======================
```

Compare this to "ATX headers", which markdown uses and look like this:

```
# This is a header
```

Setting aside the annoyance of having to hold down the "=" a bunch of times,
the big problem with rST headers is that header **characters in rST have no single
mapping onto header hierarchy**. For example:

```rst
This is my first header
~~~~~~~~~~~~~~~~~~~~~~~

And this is my second header
============================
```
is the same as

```rst
This is my first header
=======================
And this is my second header
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

This is a case where too much flexibility makes life more difficult than it needs to be. Many
responses wished that rST simply used "ATX" headers (using `#` in front of titles) or chose
a single hierarchy of header characters.

## In-line code

Many folks also dislike the fact that in rST, you must denote in-line code blocks with **two**
backticks instead of one. For example, this is rST:

```rst
Here is some inline code: ``a = 2``
```

While here is some markdown

```
Here is some inline code: `a = 2`
```

It may seem silly, but markdown's ubiquity has given most people the assumption that backticks==code.
The fact that rST deviates from this adds unnecessary cognitive burden to most users.

## Nesting in-line markup

Finally, there were several mentions of rST's strange inability to nest in-line formatting.
E.g. being able to bold a link by nesting `**` inside of your link syntax.

## A quick summary

Here is a quick list of the tweets that touched on the topic of syntax:

* Links syntax is confusing (9 total)
    * Links are confusing: <https://twitter.com/asmeurer/status/1212468755768336384>
    * Bad syntax, esp links: <https://twitter.com/njgoldbaum/status/1212059796142055424>
    * Links structure: <https://twitter.com/SylvainCorlay/status/1212061834116816898>
    * External links: <https://twitter.com/WillingCarol/status/1212152304800894976>
    * Syntax / too complex to write: <https://twitter.com/minrk/status/1212119686009233410>
    * Syntax, esp links and tables: <https://twitter.com/_JacobTomlinson/status/1212104705809289219>
    * Improve links: <https://twitter.com/andreazonca/status/1212166686389858306>
    * Links and heading permalinks: <https://twitter.com/goerz/status/1212610069252263936>
    * Inline hyperlinks: <https://twitter.com/moorepants/status/1212072806994739200>
* Header / title syntax (3 total)
    * Using underlines for headers: <https://twitter.com/phaustin/status/1212067821976375296>
    * Titles: <https://twitter.com/mfcabrera/status/1212126606170431489>
    * Title lines are confusing: <https://twitter.com/alienghic/status/1212119125398437888>
* Two backticks for code
    * Two Backticks for code literals: <https://twitter.com/brettsky/status/1212422437683351553>
* Nested inline markup (e.g. 'em' inside of 'strong') (2 total)
    * Nested inline markup: <https://twitter.com/asmeurer/status/1212468755768336384>
    * nested "em" in "strong": <https://twitter.com/uranusjr/status/1212179877341720577>

# Error reporting and the complexity of Sphinx

The other major complaint people had was in the toolchain itself. Sphinx is an incredibly powerful tool,
but this comes with a degree of complexity that many find difficult to work through. This isn't helped
by the fact that the [Sphinx documentation](http://www.sphinx-doc.org/en/master/)
is itself incomplete in many sections (the irony of this is not lost on me).

In particular, several people commented about the difficulty in surfacing and debugging errors that happen
in the Sphinx build chain. They also mentioned that Sphinx can be slow to build sometimes, which
bogs down the development and writing process.

Here are the tweets about the Sphinx toolchain itself:

* Error reporting / complexity of Sphinx itself (3 total)
    * Error reporting: <https://twitter.com/asmeurer/status/1212468909078544384>
    * Error reporting in Sphinx etc: <https://twitter.com/GaelVaroquaux/status/1212058374981988352>
    * Documentation is bad: <https://twitter.com/AkhmerovAnton/status/1212059839033171968>

There were also a few miscellaneous responses that didn't quite fit into the above categories:

* Misc (6 total)
    * Isn't a standard: <https://twitter.com/aterrel/status/1212132546307350529>
    * Newlines in nested lists, not easy to deploy: <https://twitter.com/westurner/status/1212178375571365891>
    * No notebook support: <https://twitter.com/moorepants/status/1212062811599147008>
    * Has state: <https://twitter.com/Mbussonn/status/1212069224245551104>
    * General complexity: <https://twitter.com/mrocklin/status/1212123762595811328>

# What can be done?

Overall, it seems like **reStructuredText** could be much-improved with a few minor
modifications to its syntax. These don't seem like they are structurally
incompatible with rST, and would alleviate some of the cognitive
burden that users report when they use it. Here's a quick list of simple things:

* rST could use markdown syntax for external links.
* rST could decide on a fixed interpretation of header characters to levels in the header hierarchy
* rST could default to interpreting single backticks as raw code spans

and a list of slightly more complex things:

* rST could support nested styling inside of links and other elements
* Sphinx could improve its error reporting and debugging machinery
* Sphinx could improve its documentation so that it was easier to find an answer to a question

# Or could we bring reStructuredText into Markdown?

There is another option, of course, which is to go in the opposite direction. Start with markdown,
and then ask "how could we build the flexibility of rST into markdown" rather than bringing the
simplicity of markdown into reStructuredText. I often wonder if the easiest thing to do would be
to simply decide on a markdown syntax that maps on to "directives" and "roles" (perhaps the Pandoc
code fence `:::` for directives, and link attributes `[]{attribute}` for roles). I think that both
are worth exploring.

In summary, I was surprised at the consistency of people's complains about the rST language. It
seems that many people are hung up about the same relatively minor syntax choices, and that making
modifications to these choices would improve the experience for many. It's also clear that Sphinx
could use some developer time to make it more robust, debuggable, and well-documented. I hope that
we can make some progress on these issues in the coming years.





