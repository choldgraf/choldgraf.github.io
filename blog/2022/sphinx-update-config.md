---
tags: sphinx
date: "2022-12-05"
category: "til"
---

# How to update Sphinx options during the build

As part of [the `pydata-sphinx-theme`](https://github.com/pydata/pydata-sphinx-theme/pull/1075) we have a few settings that auto-enable extensions and configure them on behalf of the user.
It has always been mysterious to me how to do this properly **during the Sphinx build**.
It's easy to configure things with `conf.py` ahead of time, but what if you want to manually set a value during the build?

I finally figured it out, so documenting the process here.

## Use the `builder-inited` event

**Define a Sphinx event for `builder-inited`**. This will trigger after the builder has been selected, but before the environent is finalized for the build.
This should be a function that takes a single `(app)` parameter.

:::{seealso}
See [the Sphinx Core Events documentation](https://www.sphinx-doc.org/en/master/extdev/appapi.html#sphinx-core-events) for more information about Sphinx's events system.
:::

## Use `app._raw_config` to find the user-provided config

**Use the `app._raw_config` object to detect user-given config**. [This is first written when Sphinx is initialized](https://github.com/sphinx-doc/sphinx/blob/ba080286b06cb9e0cadec59a6cf1f96aa11aef5a/sphinx/config.py#L151-L155) and should be a good indication of what the user provided.

This is useful if you only want to over-ride something if the _user didn't set it themselves_.
However, the `app.config` object will have _all_ of the config options, including defaults.

## Update configuration options with the `app.config` object

**Update `app.config.keyname`**.
You can set and update configuration values directly with `app.config.keyname = "foo"`.
The way [Sphinx does this](https://github.com/sphinx-doc/sphinx/blob/b1ca6b3e120d83c9bb64fdea310574afb9897c1a/sphinx/config.py#L233-L238) is by directly setting `app.config.__dict__["keyname"] = "foo"`, but this doesn't seem to be necessary and I'm not sure why they do it that way.

:::{admonition} `app.config.values` has the defaults!
It might seem like `app.config.values is the right place for this, but that isn't the case.
`app.config.values` has the *defaults* for Sphinx, and if you directly replace items, then Sphinx will behave unpredictably.
[Here's where Sphinx configures these defaults](https://github.com/sphinx-doc/sphinx/blob/b1ca6b3e120d83c9bb64fdea310574afb9897c1a/sphinx/config.py#L186-L195)
:::

## Update HTML theme options with `app.builder.theme_options`

**Update `app.builder.theme_options`**.
Many people (including myself) incorrectly try to update `app.config.html_theme_options` during a build event.
But this doesn't do anything because the've already been copied over to `app.builder.theme_options` early in the build process.
Annoyingly, the copied dictionary in `app.builder.theme_options` does not point to the same points in memory as `app.config.html_theme_options`.

This [copy action is done here](https://github.com/sphinx-doc/sphinx/blob/ba080286b06cb9e0cadec59a6cf1f96aa11aef5a/sphinx/builders/html/__init__.py#L301-L307).

## An example

Here's an example of the whole process in action:

```python
# This function will update a single configuration value
def update_config(app):
   # Check if a value was provided by the user
   if "foo" in app.config._raw_values:
      # Update a config value
      app.config.__dict__["foo"] = "bar"

   # Update an HTML theme value
   app.builder.theme_options["foo2"] = "bar2"

# Register the above function to be called during the builder-inited phase
def setup(app):
  app.connect("builder-inited", update_config)
```
