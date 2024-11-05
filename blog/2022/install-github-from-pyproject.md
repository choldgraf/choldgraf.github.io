---
tags:
- software development
date: "2022-12-31"
category: "til"
---

# Install dependencies from GitHub with `pyproject.toml` or `requirements.txt`

This is a short post to demonstrate how to install packages directly from GitHub with `pyprojects.toml` or `requirements.txt`, including custom branches and commits.
It will focus on `pyprojects.toml` because this is newer and there's less information about it, but the general pattern holds for `requirements.txt` as well.

In `pyproject.toml`, you can specify dependencies for a project via the `dependencies` field.
For example, to specify [Sphinx](https://sphinx-doc.org) as a dependency:

```{code-block} toml
:caption: pyproject.toml
dependencies = [
  "sphinx",
]
```

However, this will install the version that is published to [`PyPI`](Here's how to install a specific branch in `pyproject.toml`:
).
What if you want to install from `@main`, or from a specific commit or branch?

To do so, use a pattern like this:

```{code-block} toml
:caption: pyproject.toml
dependencies = [
  "<packagename>@git+<url-to-repo>#egg=<branch or hash>",
]
```

Here are a few recipes for doing this:

## Install directly from GitHub

```{code-block} toml
:caption: pyproject.toml
dependencies = [
  "sphinx@git+https://github.com/sphinx-doc/sphinx",
]
```

## Install from a specific branch

```{code-block} toml
:caption: pyproject.toml
dependencies = [
  "sphinx@git+https://github.com/sphinx-doc/sphinx#egg=branchname",
]
```

## With `requirements.txt`

Using these patterns with `requirements.txt` is nearly the same, but it's a bit simpler.[^thanks]
You don't need to specify the `packagename@` pattern used above.
You can simply add a line that points to git like this:

```{code-block} txt
:caption: requirements.txt

requirement1
requirement2
git+https://github.com/pydata/pydata-sphinx-theme
```

This will install from the default branch.
You can also specify specific branches or eggs in the same way as above.

[^thanks]: Thanks to [Matthew Feickhart for reminding me of this](https://twitter.com/HEPfeickert/status/1609280067225681920).
