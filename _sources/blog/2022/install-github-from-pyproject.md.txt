---
tags: software development
date: "2022-12-31"
category: "til"
---

# Install dependencies directly from GitHub with `pyproject.toml` files

This is a short post to demonstrate how to install packages directly from GitHub with `pyprojects.toml`, including custom branches and commits.

In `pyproject.toml`, you can specify dependencies for a project via the `dependencies` field.
For example, to specify [Sphinx](https://sphinx-doc.org) as a dependency:

```toml
dependencies = [
  "sphinx",
]
```

However, this will install the version that is published to [`PyPI`](Here's how to install a specific branch in `pyproject.toml`:
).
What if you want to install from `@main`, or from a specific commit or branch?

Here are a few recipes for doing this:

## Install directly from GitHub

```toml
dependencies = [
  "sphinx@git+https://github.com/sphinx-doc/sphinx.git",
]
```

## Install from a specific branch

```toml
dependencies = [
  "sphinx@git+https://github.com/sphinx-doc/sphinx.git#egg=branchname",
]
```
