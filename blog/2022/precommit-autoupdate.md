---
tags: python, git
date: "2022-12-03"
category: "til"
---

# Automatically update pre-commit hook versions

I figured out a way to automatically update all of the git `pre-commit` hook versions at once!

[`pre-commit`](https://pre-commit.com/) is a useful command line tool for running simple commands before every `git` commit.
I use it to enforce things like [`flake8`](https://flake8.pycqa.org/) and [`black`](https://github.com/psf/black) in many of my projects.

However, I find it really annoying to keep manually updating my `pre-commit` hooks with new versions, particularly because `pre-commit` doesn't let you specify wild-cards.

Fortunately, I recently came across [the `pre-commit autoupdate` documentation](https://pre-commit.com/#updating-hooks-automatically).
This lets you automatically update to the latest released versions of all-precommit hooks.
Simply run:

```bash
pre-commit autoupdate
```

And it will update your `.pre-commit-config.yaml` file with the latest versions.
This feels like the easiest way to keep these configurations updated, at least until [GitHub adds `dependabot` support for `pre-commit`](https://github.com/dependabot/dependabot-core/issues/1524).

## Automate the above with `pre-commit.ci`

**Update**: A few folks mentioned that you can actually **automate this whole process** by using [pre-commit.ci](https://pre-commit.ci/), a service for using `pre-commit`'s functionality with automated jobs.

That service will both automatically run `pre-commit` on your Pull Requests, and will also update your `pre-commit` dependencies on the fly.