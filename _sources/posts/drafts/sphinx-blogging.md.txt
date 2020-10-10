---
author: Chris Holdgraf
---

# Re-working my blog to use Sphinx

Over the last couple of months we have been hard at work on [re-building Jupyter Book from the ground up](https://executablebooks.org/en/latest/updates/2020-08-07-announce-book.html). One of the guiding principles of the re-write was to build around a pre-existing ecosystem (Sphinx) rather than building our own bespoke tools. This means that there are now a ton of new tools to try out in Sphinx.

Most notably, you can now write Sphinx documentation entirely in markdown with the new [myst-parser](https://myst-parser.readthedocs.io) package. As my blog had already been written with markdown, I thought it would be a fun experiment to try re-writing its infrastructure to use Sphinx instead of Jekyll. The result turned out good enough that I decided to switch over my blog! Here is a quick rundown of my experience...

## Why switch blogging infrastructure?

The age-old question. Why does one ever switch static-site generators? Other than finding a new reason to procrastinate, I had a few reasons for wanting to switch:

- Standardize my website build on Python, a language/ecosystem I am more familiar with
- More naturally incorporate computational material into my blog (e.g. I can now write posts with auto-executed Jupyter Notebooks!)
- Have access to roles and directives in Sphinx. This means I can do things like...
  
  :::{admonition,tip} Adding admonitions to my blog posts!
  Pretty cool huh?
  :::
- Build around an ecosystem I could contribute to. I enjoyed using Jekyll but felt that I never had an ability to contribute to that community, largely because I am not a web developer. Using a Python stack means that I can upstream my changes to the broader ecosystem.
- Prototype how blogging could work in Jupyter Book. Finally, I wanted to see if it's possible to use Jupyter Book for blogging, and this is a first step in that direction.

## What's under the stack of this blog?

Here are a few of the major technical pieces of this new blog structure.

- **Sphinx** is used


This is a test site for blogging with Sphinx. It should let me do things like
include dropdowns via sphinx panels!

````{panels}
```{dropdown} Here's a dropdown!
And here's some stuff inside!
```
---

And here's some other stuff
````

```{tabbed} Here's a tab!
Hey!
```

```{tabbed} Here's another tab!
Wow!
```
