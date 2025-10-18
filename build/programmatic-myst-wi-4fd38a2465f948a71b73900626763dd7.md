---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.4
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
date: "2024-11-04"
tags:
- myst
- jupyter
---

+++ {"editable": true, "slideshow": {"slide_type": ""}}

# Generate MyST with Jupyter and insert it into content programmatically

While I've been [converting my blog to use the new MyST engine](./mystmd-with-the-blog.md), I discovered a useful MyST feature. It's not yet possible to [natively parse Jupyter Markdown outputs as MyST](https://github.com/jupyter-book/mystmd/issues/1026) but there's a workaround if you don't mind generating a temporary file.

The trick is to _write to a temporary file_ in your Jupyter cell, and then _include the temporary output file with an `{include}` directive_ in your MyST markdown.
This allows you to directly write MyST Markdown without worrying about what the MyST AST specification looks like.

For example, the following code cell writes some sample text to a `.txt` file in my MyST build directory.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
from pathlib import Path
p = Path("../_build/txt/tmp.txt")
p.parent.mkdir(parents=True, exist_ok=True)
# Grab a list of all the filenames
files = list(p.rglob("../**/*.md"))
txt = "\n- ".join(files)
_ = p.write_text(txt)
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

And we can then include it in the page with MyST markdown like so:

````md
```{include} ../_build/txt/tmp.txt
```
````

```{include} ../_build/txt/tmp.txt
```

The page will be executed first, and afterward, the page will be parsed into MyST, thus using the temporary file we've included.
