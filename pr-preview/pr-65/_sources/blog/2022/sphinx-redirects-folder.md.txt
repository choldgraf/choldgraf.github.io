---
category: til
date: "2022-11-19"
---

# Automatically redirect folders in Sphinx websites

I spent a bit of time today updating my website after some changes in the MyST-NB and Sphinx Design ecosystems.
Along the way, I decided to redirect `/posts/` to `/blog/`, since it seems `/blog/` is a much more common folder to use for blog posts.

This posed a problem, because [the `sphinx-rediraffe` extension](https://github.com/wpilibsuite/sphinxext-rediraffe) does not allow you to redirect folders with wildcards.
AKA, you cannot do:

```python
rediraffe_redirects = {
    "posts/**/*.md": "blog/**/*.md",
}
```

I also didn't want to have to manually specify every single blog post, since that'd be a very long list.

Fortunately, I figured out a solution because _Sphinx's configuration is also a Python script_.
This means you can dynamically populate this configuration with `pathlib`.
I'll share the code snippet below in case it's useful for others:

```{code-block} python
:caption: conf.py

# These are posts I *want* to manually specify
rediraffe_redirects = {
    "rust-governance.md": "blog/2018/rust_governance.md",
}
# Update the posts/* section of the rediraffe redirects to find all files
redirect_folders = {
    "posts": "blog",
}
from pathlib import Path
for old, new in redirect_folders.items():
    for newpath in Path(new).rglob("**/*"):
        if newpath.suffix in [".ipynb", ".md"]:
            oldpath = str(newpath).replace("blog/", "posts/", 1)
            rediraffe_redirects[oldpath] = str(newpath)
```
