---
tags: sphinx
date: "2022-12-05"
category: "til"
---

# Update Sphinx configuration during the build with your own extension

As part of [the `pydata-sphinx-theme`](https://github.com/pydata/pydata-sphinx-theme/pull/1075) we have a few settings that auto-enable extensions and configure them on behalf of the user.
It has always been mysterious to me how to do this properly **during the Sphinx build**.
It's easy to configure things with `conf.py` ahead of time, but what if you want to manually set a value during the build?

I finally figured it out, so documenting the process here:

1. **Define a Sphinx event for `builder-inited`**. This will trigger after the builder has been selected, but before the environent is finalized for the build.
   This should be a function that takes a single `(app)` parameter.
2. **Grab the `app.config` object**. This is the configuration for your build.
   Altering its values will alter Sphinx's behavior.
   However, it has a weird way of being updated...
3. **Update the `__dict__` attribute of the `Config` object**.
   For some reason, it seems you need to update `__dict__` within the `app.config` object.
   This will update the configuration as expected.
   For example:

   ```python
   app.config.__dict__["mykey"] = "myvalue"
   ```

This seems to mirror [how Sphinx sets up the config internally](https://github.com/sphinx-doc/sphinx/blob/b1ca6b3e120d83c9bb64fdea310574afb9897c1a/sphinx/config.py#L227-L240), and leads to the behavior I want.
