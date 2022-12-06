---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.2
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
mystnb:
  execution_mode: "cache"
date: "2022-12-06"
tags: matplotlib
category: til
---

# Load and plot a remote font with Matplotlib

As part of [my `sphinx-social-previews`](https://github.com/choldgraf/sphinx-social-previews) prototype, I wanted to be able to use the [Roboto Font from Google](https://fonts.google.com/specimen/Roboto) in image previews.
However, Roboto is often not loaded on your local filesystem, so it took some digging to figure out how to make it possible to load via [Matplotlib's text plotting functionality](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.text.html).

Here's the solution that finally worked for me, inspired [from this Tweet with a similar implementation](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.text.html) from [the `dmol` book](https://github.com/whitead/dmol-book/blob/master/package/dmol/__init__.py).

Below I'll use [the `Fira Code` font from Mozilla](http://mozilla.github.io/Fira/) but you could do this with any open font that you have the `.ttf` file for.

## Create a temporary folder and download the font file

I'll show how to do this with a local folder, so it'll re-download each time you run the code.
Alternatively you could download the font locally and just register the path instead of downloading it:

First, **download the `.ttf` of the font locally** via `urlretrieve`.
For example, the `Fira Code` font from Mozilla is located [at this URL](https://github.com/google/fonts/raw/main/ofl/firacode/FiraCode%5Bwght%5D.ttf).
To download it locally into a **temporary folder** using [the `tempfile.mkdtemp` function](https://docs.python.org/3/library/tempfile.html#tempfile.mkdtemp), run this code:

```{code-cell} ipython3
import tempfile
from pathlib import Path
import urllib
from rich import print

# Create a temporary directory for the font file
path = Path(tempfile.mkdtemp())

# URL and downloaded path of the font
url_font = "https://github.com/google/fonts/raw/main/ofl/firacode/FiraCode%5Bwght%5D.ttf"
path_font = path / "Fira-Code.ttf"


# Download the font to our temporary directory
urllib.request.urlretrieve(url_font, path_font)
```

## Link the font with the `font_manager` API

+++

Now that the file is loaded, we can link it using [Matplotlib's `font_manager` API](https://matplotlib.org/stable/api/font_manager_api.html).
This allows you to **register fonts that Matplotlib knows how to use**.

```{code-cell} ipython3
from matplotlib import font_manager

# Create a Matplotlib Font object from our `.ttf` file
font = font_manager.FontEntry(fname=str(path_font), name="Fira-Downloaded")

# Register this object with Matplotlib's ttf list
font_manager.fontManager.ttflist.append(font)
# Print the last few items to see what they look like
print(font_manager.fontManager.ttflist[-3:])
```

:::{tip}
To list all of the fonts that Matplotlib knows how to plot, inspect the list `matplotlib.font_manager.fontManager.ttflist`.
:::

+++

## Make a plot with this font

Now that we've registered the font, we can plot it with `ax.text`.
To do so, use the `plt.rc_context` context manager to temporarily update our default font:

```{code-cell} ipython3
import matplotlib.pyplot as plt

fig, axs = plt.subplots(1, 3, figsize=(9, 5))

# This will now render as a `Roboto Flex` font
axs[0].text(.1, .5, "The default font!", fontdict={"fontsize": 15})
axs[1].text(.1, .5, "A Matplotlib font", fontdict={"fontsize": 15, "family": "cmmi10"})
axs[2].text(.1, .5, "The Fira Code font!", fontdict={"fontsize": 15, "family": font.name})

for ax in axs:
  ax.set_axis_off()
```

And that's it!
