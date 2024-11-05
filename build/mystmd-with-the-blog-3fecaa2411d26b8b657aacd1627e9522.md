---
date: "2024-11-01"
title: Re-building my blog with MySTMD
kernelspec:
  name: python3
  display_name: 'Python 3'
---

Wow it has been a long time since I've last-written here. It turns out that having two small children and a very demanding job means you don't have as much time for blogging. But that's a whole different blog post...

I've decided to convert my blog to use the new [MyST Document Engine](https://mystmd.org). This is part of a dogfooding experiment to see what's possible with MyST, since it's where the Jupyter Book project is heading, and I want to see how close to "production-ready" we are already.

To begin, I wanted to share a few things I learned today as I tried to re-tool my old blog for use with MyST MD.

## There's no blog functionality in MyST yet

As MyST is still quite young, there's no out-of-the-box functionality for MyST (see https://github.com/jupyter-book/mystmd/issues/840 for the issue tracking that). So, I wanted to accomplish at least two things with my initial transfer:

1. Generate a list of recent blog posts that I can insert into a few places in my site.
2. Generate an RSS feed that keeps the same URLs, content, etc.

## What didn't work: using the parsed MyST documents

My first thought was to use a MyST plugin that defines a directive I could use to insert a list of blog posts.
However, I learned that MyST plugins have no way to access all of the parsed documents at build time (see [this issue about accessing all of the parsed documents](https://github.com/jupyter-book/mystmd/issues/1616) to track that one).

Fortunately, [`@rowanc1`](https://github.com/rowanc1) made me realize that I could just _manually_ parse my blog files and use that to build up something like a blog list. So that's what the rest of this post is about.

## You can run scripts in JavaScript as part of your MyST build

The [MySTMD plugins documentation](https://mystmd.org/guide/javascript-plugins) shows a few examples for how to define your own MyST plugins. These are little JavaScript files that get executed every time you build your MyST site. 

The easiest thing to do here would be to write a JavaScript plugin for MyST that I can attach to my site build. You could use a JS library to parse the markdown files in `blog/`, grab their YAML metadata, and return MyST AST structure that would be inserted into the document. But I'm not too comfortable with JavaScript, and I found two ways that are much hackier, but much more accessible for somebody that is comfortable with Python 😎.

## Write a MyST extension in Python

I bet most folks don't know that you can write MyST extensions entirely in Python (or any other language that you can execute locally). [Here is the MyST documentation on writing an executable MyST extension](https://mystmd.org/guide/executable-plugins).

Executable extensions are treated like a black box in MyST - the MyST build process simply _executes_ a file that you specify in `myst.yml`, and treats anything printed to `stdout` as MyST AST that will be inserted back into the MyST document.

:::{note} Check out the examples
There seem to be some specific ways to define the arguments that your script takes, based on whether a role, directive, or transform triggers it. See the [examples in the executable plugin docs](https://mystmd.org/guide/executable-plugins) for inspiration.
:::

## How do you know what MyST AST looks like?

I mention "all you need to do is output MyST AST", but what does that even mean?
The MyST AST is the abstract structure of a MyST document. It has all of the relevant information about the content in a document, as well as all the semantic tags for different _types_ of content that can exist (e.g., "italics", or "admonition boxes").

When a MyST Markdown document is parsed, the result is MyST AST. You can see a ton of examples of AST for various MyST markdown in [the MyST guide](https://mystmd.org/guide).
Just look for the litte "interactive demo" boxes that show off sample MyST Markdown.

:::{tip} Use the JSON representation of the AST
You'll note that clicking the AST button gives you a few different ways to view it.
By default, you'll see YAML, but JSON is closer to the structure that MyST plugins expect you to output. In my case, I grabbed the JSON output, and converted it for use as a Python dictionary (this basically just meant turning `true` into `True`).
:::

In my case, I needed a *list* of blog posts, so I found the relevant AST for what this looks like at the following locations:

- The [list items documentation](https://mystmd.org/guide/typography#bullet-points-and-numbered-lists) showed me the AST for lists.
- The [Definition lists documentation](https://mystmd.org/guide/typography#definition-lists) had sample AST for an internal link.
- The [Inline text formatting documentation](https://mystmd.org/guide/typography#inline-text-formatting) had examples for things like bold, italics, etc.

## Turning this into a Python plugin for MyST

With this in mind, I wrote a little Python extension that:

1. At build time, parses all of my blog post markdown files and extracts metadata from their YAML headers.
2. Defines a `bloglist` directive that will insert a list of blog posts where it exists.
3. Manually converts the blog post metadata into MyST AST that it prints to `stdout`.

As a result, when I call the directive in my blog, it will _replace the directive with whatever AST is spit out by the Python script_. You can take a look at [the entire Python script here](../../src/blogpost.py).

Now I can insert lists of blog posts wherever I like, for example here's a list of the latest three:

:::{postlist}
:number: 3
:::

## Adding an RSS feed

Because I'm running Python to define my MyST plugin, I can also use Python to build a custom RSS feed! This was relatively easy since I'd already parsed the metadata from each file.

I found [the `python-feedgen` package](https://github.com/lkiesow/python-feedgen), which is a little helper package for generating RSS feeds in Python. Since my MyST plugin was already written in Python, I just added a few more lines to do so.

````{note} Click to see the whole Python plugin script
:class: dropdown
```{literalinclude} ../../src/blogpost.py
```
````
