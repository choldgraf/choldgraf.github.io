---
date: "2022-12-06"
category: til
tags: visualization
---

# Load and plot a remote font with Matplotlib

As part of [my `sphinx-social-previews`](https://github.com/choldgraf/sphinx-social-previews) prototype, I wanted to be able to use the [Roboto Font from Google](https://fonts.google.com/specimen/Roboto) in image previews.
However, Roboto is often not loaded on your local filesystem, so it took some digging to figure out how to make it possible to load via [Matplotlib's text plotting functionality](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.text.html).

Here's the solution that finally worked for me, inspired [from this Tweet with a similar implementation](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.text.html) from [the `dmol` book](https://github.com/whitead/dmol-book/blob/master/package/dmol/__init__.py).

All of the following can be run at build-time.
I'll show how to do this with a local folder, so it'll re-download each time you run the code.
Alternatively you could download the font locally and just register the path instead of downloading it:

First, **download the `.ttf` of the font locally** via `urlretrieve`.
For example, the `Roboto Flex` font from Google is located [at this URL](https://github.com/google/fonts/raw/main/ofl/robotoflex/RobotoFlex%5BGRAD%2CXOPQ%2CXTRA%2CYOPQ%2CYTAS%2CYTDE%2CYTFI%2CYTLC%2CYTUC%2Copsz%2Cslnt%2Cwdth%2Cwght%5D.ttf).
To download it locally into a **temporary folder** using [the `tempfile.mkdtemp` function](https://docs.python.org/3/library/tempfile.html#tempfile.mkdtemp), run this code: 

```python
import tempfile
from pathlib import Path
import urllib

# Create a temporary directory for the font file
path = Path(tempfile.mkdtemp())

# URL and downloaded path of the font
url_font = "https://github.com/google/fonts/raw/main/ofl/robotoflex/RobotoFlex%5BGRAD%2CXOPQ%2CXTRA%2CYOPQ%2CYTAS%2CYTDE%2CYTFI%2CYTLC%2CYTUC%2Copsz%2Cslnt%2Cwdth%2Cwght%5D.ttf"
path_font = path / "Roboto-Mono.ttf"
# Download the font to our temporary directory
urllib.request.urlretrieve(url_font, path_font)
```

Now that the file is loaded, we can link it using [Matplotlib's `font_manager` API](https://matplotlib.org/stable/api/font_manager_api.html).
This allows you to **register fonts that Matplotlib knows how to use**.

```python
from matplotlib import font_manager

# Create a Matplotlib Font object from our `.ttf` file
font = font_manager.FontEntry(fname=str(path_font), name="Roboto")

# Register this object with Matplotlib's ttf list
font_manager.fontManager.ttflist.append(font)
```

:::{tip}
To list all of the fonts that Matplotlib knows how to plot, inspect the list `matplotlib.font_manager.fontManager.ttflist`.
:::

Now that we've registered the font, we can plot it with `ax.text`.
To do so, use the `plt.rc_context` context manager to temporarily update our default font:

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
# Temporarily set `font.family` to `Roboto` (or whatever is the name of `font` above)
with plt.rc_context({"font.family": font.name}):
  # This will now render as a `Roboto Flex` font
  ax.text("hi there!")
```

And that's it!
