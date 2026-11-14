---
tags:
- sphinx
date: "2023-01-19"
category: "til"
---

# Bundle extensions with your Sphinx theme

Sphinx is great because it has a ton of useful extensions that let you grow its functionality.
However, a downside of this is that users have to actually _learn about_ those extensions and activate them manually.
It's not hard, but it's a non-trivial amount of discovery work.

One way to solve this is for **themes to bundle extensions on their own**.
This way they can include functionality via an extension rather than writing custom code on their own.

However, this doesn't often happen, I think because it can be pretty confusing how to do so.
I believe I've figured out the major gotchas to avoid and patterns to follow, so here's a quick overview.

## Use `app.setup_extension` to add the extension

First off, the [Sphinx docs mention `app.setup_extension`](https://www.sphinx-doc.org/en/master/extdev/appapi.html#sphinx.application.Sphinx.setup_extension) as "the" way to set up a Sphinx extension.

This activates the extension as if you'd put it in the `extensions` variable.
However, it leaves out a lot of nuance.

## Don't forget the theme is activated _after_ `config-inited`

Many extensions add functionality in [Sphinx events](https://www.sphinx-doc.org/en/master/extdev/appapi.html#sphinx-core-events).
These are emitted throughout the build process and you can hook into them with functions to modify the document etc.

However, **your theme is activated after the `config-inited` event**.
That means that if you manually activate an extension, but that extension registers a callback that waits for `config-inited`, then **nothing will happen**.

So in general, if something doesn't seem like it's happening, then double check that your extension isn't using a `config-inited` event hook.

:::{admonition} Sphinx extension authors: don't use `config-inited`!
Because of this limitation, I'd recommend that Sphinx extension authors use `builder-inited` rather than `config-inited`.
It is also early in the build process, but *after* the theme is activated.
:::

## Workaround: You can try emitting your own `config-inited`

I think I figured out a workaround to the above limitation in case you can't control which events your extensions hook into.
It's based on the idea that Sphinx has a **registry of event listeners** at `app.events.listeners`.
This is a dictionary of `event-name:[list-of-listener-objects]` pairs.
When `app.emit(event)` is triggered, it loops through the respective list and runs each listener object.

So we should be able to just remove that list, then activate our extensions (which will add to the list), and then manually trigger the `config-inited` event.
Try the following steps:

1. **Store a copy of the old event listeners**.
   They've already been run (since `config-inited` has happened already), but we'll keep them just in case.

   ```python
   old_listeners = app.events.listeners["config-inited"]
   ```
2. **Replace the old listeners with an empty list**.
   This means there are effectively no listeners for the event.

   ```python
   app.events.listeners["config-inited"] = []
   ```
3. **Activate your extra extensions**.
   You can now loop through the list of extensions you want to bundle and activate each one.

   ```python
   for ext in your_extensions:
      app.setup_extension(ext)
   ```

   This will _add event listeners to `config-inited`_ for any extensions that require it.
   Any extension that has already been activated will be a no-op.
4. **Emit your own `config-inited` event**.
   Now that you've activated the extensions and added their event listeners, re-emit the `config-inited` event.
   This will now *only call the new listeners you've added*.

   ```python
   app.emit("config-inited", app.config)
   ```
5. **Combine the two lists of listeners**.
   Finally, combine the two lists of listeners just so that your Sphinx application's state matches what has actually happened (I have no idea if this is actually needed).

   ```python
   # This prepends the list
   # ref: https://stackoverflow.com/questions/19736058/can-i-extend-list-in-python-with-prepend-elements-instead-of-append
   app.events.listeners["config-inited"][:0] = old_listeners 
   ```

Now you can let the Sphinx build move forward as normal.
You will have manually emitted the `config-inited` event for your new extensions, and they'll be picked up for any future events that happen.

## Addendum: you could also make your theme an extension

If you _really_ don't want to do the hacky steps above, another option is to ask users to add your theme as an _extension_ as well as a theme.
For example:

```python
extensions = ["my_theme"]
html_theme = "my_theme"
```

However, I've found that this usually confuses people and is pretty clunky from a UX perspective.
I'd much rather try to handle the complexity under the hood.
