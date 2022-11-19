---
tags: markup, documentation
categories: til
date: 2020-01-22
---

# Build a simple timeline with `sphinx-design`

One of the nice things about [MyST Markdown](https://myst-parser.readthedocs.io) is that it is **extensible**. Any Sphinx extension will work with MyST Markdown (in the context of Jupyter Book, anyway).

One of my favorite Sphinx extensions is [Sphinx Design](https://sphinx-design.readthedocs.io/), this brings you flexible UI components that use Bootstrap CSS under the hood (though without heavy javascript). They let you do things like this:

````{grid} 2
```{grid-item-card}
A card!
^^^
With some content!
```
```{grid-item-card}
A second card!
^^^
With some more content!
```
````

I wanted to have [a nice-looking timeline](about:timeline) for my blog, and it turns out this was surprisingly easy to do with Sphinx Panels and a bit of custom CSS. You can [check out my about page for an example](about:timeline), or see the little example below:

`````{example}
:reverse:

````{grid} 2
:class-container: timeline

```{grid-item-card}
:class-item: entry left

2020
^^^

2020 body
```
```{grid-item}
:class: right
```
```{grid-item}
:class: left
```
```{grid-item-card}
:class-item: entry right

**2017**
^^^

2017 body
```
```{grid-item-card}
:class-item: entry left

**2011**
^^^

2011 body
```
```{grid-item}
:class: right
```
```{grid-item}
:class: left
```
```{grid-item-card}
:class-item: entry right

**2009**
^^^

2009 body
```
````
`````