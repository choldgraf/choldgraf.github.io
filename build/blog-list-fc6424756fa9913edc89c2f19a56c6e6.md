---
date: "2024-11-09"
author: Chris Holdgraf
tags:
- myst
- jupyter
---

# Better blog lists with the MyST AST

On my journey to learn more about writing with [the new MyST engine](https:///mystmd.org), I built upon [my recent update to my blog infrastructure](./programmatic-myst-with-jupyter.md) and made some improvements to my blog post list.
Here's what it looks like now:

````{note} Click here to see how it looks now
:class: dropdown
```{postlist}
:number: 3
```
````

Here's a quick rundown of what I've improved.

## Use the MyST sandbox to determine what AST to generate

I realized that MyST cards are a first-class citizen in the AST, meaning that I should be able to generate them directly with my Python plugin. These look a lot nicer than a list of bullet points.

However, generating MyST AST from scratch is cumbersome, so I headed over to [the MyST sandbox](https://mystmd.org/sandbox) to quickly see what the AST needed to look like for card outputs.

```{figure} images/sandbox-demo.png
Using the sandbox to preview what the AST looks like.
[Here's an example of a card directive in the MyST sandbox](https://mystmd.org/sandbox?tab=demo&myst=YABgAGAAewBjAGEAcgBkAH0AIABUAGUAcwB0ACAAdABpAHQAbABlAAoAOgBmAG8AbwB0AGUAcgA6ACAAKgAqAEEAdQB0AGgAbwByADoAKgAqACAAVABlAHMAdAAgAGEAdQB0AGgAbwByACAAfAAgACoAKgBEAGEAdABlACoAKgA6ACAAVABlAHMAdAAgAGQAYQB0AGUACgBMAG8AcgBlAG0AIABpAHAAcwB1AG0ALgAgAEwAbwByAGUAbQAgAGkAcABzAHUAbQAuACAATABvAHIAZQBtACAAaQBwAHMAdQBtAC4AIABMAG8AcgBlAG0AIABpAHAAcwB1AG0ALgAgAEwAbwByAGUAbQAgAGkAcABzAHUAbQAuACAATABvAHIAZQBtACAAaQBwAHMAdQBtAC4AIABMAG8AcgBlAG0AIABpAHAAcwB1AG0ALgAgAEwAbwByAGUAbQAgAGkAcABzAHUAbQAuACAATABvAHIAZQBtACAAaQBwAHMAdQBtAC4AIABMAG8AcgBlAG0AIABpAHAAcwB1AG0ALgAgAEwAbwByAGUAbQAgAGkAcABzAHUAbQAuACAATABvAHIAZQBtACAAaQBwAHMAdQBtAC4AIABMAG8AcgBlAG0AIABpAHAAcwB1AG0ALgAgAEwAbwByAGUAbQAgAGkAcABzAHUAbQAuAAoAYABgAGAA).
```

With this in mind, I simply modified [my blogpost Python script](../../src/blogpost.py) to generate AST like the above rather than the bulleted list I was generating before.

Generating output manually with MyST AST takes some getting used-to, but the sandbox-based workflow above helps a _lot_.
I think it'll be way nicer once we can do this programmatically with Jupyter cells, [here's the issue tracking parsing cell outputs as MyST](https://github.com/jupyter-book/mystmd/issues/1026) and [this one specifically about generating AST from notebook cells](https://github.com/jupyter-book/mystmd/issues/1633).

