---
author: Chris Holdgraf
date: 2020-10-10
tags: sphinx, blogging, jupyter
---

# A new blog with Sphinx

I recently re-wrote all of the infrastructure for my blog so that it now builds on top of the Sphinx ecosystem! This is a short post to describe the reasons for doing so, and a bit about the implementation.

```{image} https://www.sphinx-doc.org/en/master/_static/sphinxheader.png
:class: bg-dark
:target: https://www.sphinx-doc.org/en/master/
```

## Why did you re-write your blog?

This is a great question. The answer to "should you re-work your blog to use a new SSG" is almost always "no, it's a waste of your time", but I think I had a few good reasons ;-)

🐶 Dog Fooding
: First, I've been doing a lot of work with the [Executable Books Project](https://executablebooks.org) lately. As a result, [Jupyter Book now depends on Sphinx](https://executablebooks.org/en/latest/updates/2020-08-07-announce-book.html). The more I use Sphinx in my own workflows, the more I'll be equipped to improve the Sphinx ecosystem and Jupyter Book in ways that will benefit its users.

🎁 Upstreaming
: A big reason for moving Jupyter Book to Sphinx was to give ourselves more excuse to upstream improvements to the broader community. Switching over my own blog is for the same reason.

🌷 Simplicity
: I understand the Sphinx ecosystem relatively well, and use it across many of my projects. It's got a number of great themes and a ton of extensions to do more things with my content. Moreover, it's 💯 Python and I don't have to worry about installing extra languages etc to build my pages.

🚀 Features
: It turns out that building your blog (or any content for that matter) on top of a documentation engine gives you a lot of extra things to try that you don't usually get from a SSG. Being able to use [Sphinx roles/directives](https://myst-parser.readthedocs.io/en/latest/using/syntax.html#syntax-directives) from within a page is pretty cool. I can do stuff like this:

  ````{panels}
    ```{dropdown} Here's a dropdown!
    And here's some stuff inside!
    ```
  ---
  :::{admonition} Wow, a tip!
  :class: tip
  What a great tip!
  :::
  ````

🪐 Executable content and notebooks
: On top of the base Sphinx features, [MyST-NB](https://myst-nb.readthedocs.io) now lets me write my entire post in notebooks, and will execute and cache the content for me if I wish. I can also [write the whole notebook as markdown](https://myst-nb.readthedocs.io/en/latest/use/markdown.html) which keeps my posts easily diff-able.


## The components that make up this blog

OK so how is this blog actually built now? Here is a quick rundown.

- **Where is the blog source code?** At [this github repository](https://github.com/choldgraf/choldgraf.github.io)
- **What engine builds the website?** The [Sphinx documentation engine](https://www.sphinx-doc.org/en/master/) is the core documentation engine.
- **What engine builds the blog?** I use the [ablog Sphinx blog extension](https://ablog.readthedocs.io/) to host the actual blog.
- **What theme do you use for the blog?** I use the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/)
- **How do you write Sphinx docs in markdown?** I use the [myst-parser package](https://myst-parser.readthedocs.io/en/latest/)
- **How do you write content in notebooks?** I use the [MyST-NB package](https://myst-nb.readthedocs.io/en/latest/).
- **How did you make those fancy buttons and dropdowns?** That was the [sphinx-panels Sphinx extension](https://sphinx-panels.readthedocs.io/en/latest/).

Specifically, [my website is hosted here](https://github.com/choldgraf/choldgraf.github.io) and all of the blog posts are [in this folder](https://github.com/choldgraf/choldgraf.github.io/tree/main/posts).
I'm configuring ABlog to [find any markdown files in this folder and treat them as blog posts](https://github.com/choldgraf/choldgraf.github.io/blob/main/conf.py#L80).

## In conclusion

So far, I quite like this new blog setup. Sphinx is familiar to me, and I think that using this for my own blog will help me understand how the ecosystem could be further-improved to support blogs in other contexts. If you want to check out this blog's setup, see [this blog's repository](https://github.com/choldgraf/choldgraf.github.io) to get started! Next up, I'm going to see how easy it is to do this in Jupyter Book!
