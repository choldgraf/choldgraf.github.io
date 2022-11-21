---
categories: til
date: "2022-11-21"
tags: sphinx, scholarship, myst
---

# Custom roles and domains in Sphinx with one line

I was working on [the roles and structure section of the 2i2c Team Compass](https://compass.2i2c.org) and found a nifty feature in Sphinx that I hadn't known before.

You can currently add labels to any section with the following MyST Markdown structure:

```md
(mylabel)=
## My header

And now I [reference it](mylabel).
```

However, there are no **semantics** attached to this label.
Instead I'd like to be able to specify what _kind_ of a label this is.
In my case, it's because I wanted to define a **group of labels attached to our organization's roles**.

Fortunately this is pretty easy to do!
Just not well-documented.

Here's how to **define a custom role and reference it in Sphinx**:

1. **Register your new role group**. In your `conf.py` configuration, use `app.add_crossref_type` like so:
   
   ```{code-block} python
   :caption: conf.py

   def setup(app):
       app.add_crossref_type("labelmygroup", "mygrp")
   ```

   The first argument `labelmygroup` is the name of a **directive** that you'll now be able to use to attach a section of your documentation to this role group.

   The second argument `mygrp` is the name of a **role** that you can now use to refer to an group that was labeled with `labelmygroup`.
2. **Add a group label to a section with a directive**. You can do this like so:

   ````md
   ```{labelmygroup} Some name
   ```
   ## Group description
   ````

3. **Reference the label with a role**. You can now reference the `Some name` group with a role, like so: `` Here is {mygrp}`Some name` ``.
   
This is a nice way to have semantic references throughout your docs (like `` {role}`Executive Director` ``) rather than generic ones.

See [the Sphinx Documentation on this](https://www.sphinx-doc.org/en/master/extdev/appapi.html#sphinx.application.Sphinx.add_crossref_type) for more details.
