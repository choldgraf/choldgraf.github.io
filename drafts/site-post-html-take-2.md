---
tags: [jupyter, open source, nbconvert, publishing, blogging]
title: Blogging with Jupyter Book
category: open science
---

In [a post last year](https://predictablynoisy.com/jekyll-markdown-nbconvert) I described
the build system that I was using to blog using Jupyter Notebooks. This is a follow-up
to describe the *new* system that I'm using, which is in many ways an evolution of the
previous build system. It's much simpler (from the blogger's perspective) and I hope
others will be able to use it as well.

## What problem am I trying to solve?

First off, here are the things that we'd like to do:

* Store this content in Jupyter Notebooks for posts involving "literate computing".
* Convert this content to a format that can be served in Jekyll/Hugo/etc websites.
* Keep as much interactivity as possible
* Style the output so that it looks like a nice hybrid of Jupyter Notebooks and a blog

## Moving from custom nbconvert templates to Jupyter Book

I was previously using a custom nbconvert template along with
a few CSS and JS files to convert notebooks into Jekyll Markdown.
Since writing that post, I built in much of the nbconvert / jinja templates
into [Jupyter Book](https://jupyterbook.org), a tool for build HTML books out of a
collection of Jupyter Notebooks.

There is now a feature in Jupyter Book that lets you
**[build individual pages from a single `.ipynb` file](https://jupyterbook.org/features/page.html)**.
This means that I can run

```bash
jupyter-book page path/to/mypage.ipynb
```

And the result will be a single HTML file with CSS and JS embedded in it, styled
like a Jupyter Book.

## Integrating Jupyter Book into my site

The new build process for this blog is now totally controlled from
[this Python script](https://github.com/choldgraf/choldgraf.github.io/blob/master/scripts/build_html.py).
It uses the Python API of Jupyter Book to do the following things:

1. Generate the latest copies of the Jupyter Page's CSS and JS ([here](https://github.com/choldgraf/choldgraf.github.io/blob/master/scripts/build_html.py#L22)). Write these to my blog's respective CSS/JS
folders and [link them in the site's head file](https://github.com/choldgraf/choldgraf.github.io/blob/master/_includes/head.html#L25).
2. Use [Jupytext](https://jupytext.readthedocs.io) to read in the `ipynb` files in my blog's content folder.
3. Convert the `.ipynb` files to a Jupyter Page HTML file, and write it to my Jekyll site's posts folder.
   ([here](https://github.com/choldgraf/choldgraf.github.io/blob/master/scripts/build_html.py#L51)).

This greatly simplified the amount of custom code etc that I needed to maintain in order
to build blog-worthy HTML for my posts. It also means that I can use some of the nifty features
of Jupyter Book like sidebars, epigraphs, and hidden inputs/outputs. As Jupyter Book builds new
features and functionality, these will automatically propagate to my blog. Pretty cool!
