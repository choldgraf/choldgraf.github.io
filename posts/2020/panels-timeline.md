---
tags: markup, documentation
date: 2020-01-22
---

# Building a simple timeline with `sphinx-panels`

One of the nice things about [MyST Markdown](https://myst-parser.readthedocs.io) is that it is **extensible**. Any Sphinx extension will work with MyST Markdown (in the context of Jupyter Book, anyway).

One of my favorite Sphinx extensions is [Sphinx Panels](https://sphinx-panels.readthedocs.io/), this brings you flexible UI components that use Bootstrap CSS under the hood (though without heavy javascript). They let you do things like this:

```{panels}
A card!
^^^
With some content!
---
A second card!
^^^
With some more content!
```

`````{dropdown} See the code that produced this
````
```{panels}
A card!
^^^
With some content!
---
A second card!
^^^
With some more content!
```
````
`````

I wanted to have [a nice-looking timeline](about:timeline) for my blog, and it turns out this was surprisingly easy to do with Sphinx Panels and a bit of custom CSS. You can [check out my about page for an example](about:timeline), or see the little example below:

````{panels}
:container: timeline
:column: col-6 p-0
:card:

---
:column: +entry left

2020
^^^

2020 body

---
:column: +right
---
:column: +left

---
:column: +entry right

**2017**
^^^

2017 body

---
:column: +entry left

**2011**
^^^

2011 body

---
:column: +right
---
:column: +left
---
:column: +entry right

**2009**
^^^

2009 body
````