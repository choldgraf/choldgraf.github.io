---
tags: python blogging sphinx documentation
title: Adding copy buttons to code blocks in Sphinx
permalink: sphinx-copy-buttons
category: documentation
date: 2018-07-05
---

[Sphinx](http://www.sphinx-doc.org/en/master/) is a fantastic way to build
documentation for your Python package. On the Jupyter project, we use it
for almost all of our repositories.

A common use for Sphinx is to step people through a chunk of code. For example,
in the [Zero to JupyterHub for Kubernetes](https://zero-to-jupyterhub.readthedocs.io/en/latest/)
guide we step users through a number of installation and configuration steps.

A common annoyance here is that there is lots of copy/pasting involved. Sometimes
you accidentally miss a character or some whitespace. So, I spent a bit of time
figuring out how to **automatically embed a copy button into code blocks**. It
turns out this is pretty easy!


## Adding a copy button to your Sphinx code blocks

To accomplish this we'll use the excellent [clipboard.js](https://clipboardjs.com/)
which provides the machinery for copying the contents of an HTML element as well
as [jquery](https://jquery.com/) for modifying our built documentation on-demand.

The result will be a Sphinx site with code blocks that display a copy button
when you hover over them. You can demo this on this very page, which uses a
similar method (but is built with Jekyll).

Here's what you should do:

1. Create a javascript script called `doc/_static/custom.js`. In the file, put the following
   code (see comments for explanation):

    ```javascript
    function addCopyButtonToCode(){
    // get all code elements
    var allCodeBlocksElements = $( "div.highlight pre" );

    allCodeBlocksElements.each(function(ii) {
    // add different id for each code block
    // target
    var currentId = "codeblock" + (ii + 1);
    $(this).attr('id', currentId);

    //trigger
    var clipButton = '<button class="btn copybtn" data-clipboard-target="#' + currentId + '"><img src="https://clipboardjs.com/assets/images/clippy.svg" width="13" alt="Copy to clipboard"></button>';
       $(this).after(clipButton);
    });

    new Clipboard('.btn');
    }

    $(document).ready(function () {
    // Highlight current page in sidebar
    console.log('hi');
    addCopyButtonToCode();
    });
    ```

2. Create a custom CSS file called `doc/_static/custom.css` (or add to one you've
   already got). In the file, put these lines:

   ```css
   /* Copy buttons */
   button.copybtn {
     webkit-transition: opacity .3s ease-in-out;
     -o-transition: opacity .3s ease-in-out;
     transition: opacity .3s ease-in-out;
     opacity: 0;
     padding: 2px 6px;
     position: absolute;
     right: 4px;
     top: 4px;
   }
   div.highlight:hover .copybtn, div.highlight .copybtn:focus {
       opacity: .3;
   }
   div.highlight .copybtn:hover {
       opacity: 1;
   }
   div.highlight {
       position: relative;
   }
  ```

3. Link your custom JS and CSS scripts, as well as the clipboard.js script. In
   your `conf.py` file, add the following function/lines (or add to one you've already
   got defined).

   ```python
   def setup(app):
       # For copy buttons
       app.add_stylesheet('custom.css')
       app.add_javascript("custom.js")
       app.add_javascript("https://cdn.jsdelivr.net/npm/clipboard@1/dist/clipboard.min.js")
   ```

And that's it! Once you clear your Sphinx cache and re-build your site, you should
now have buttons that appear when you hover over them, and that copy
the text inside when you click them.

## Thanks

Many thanks to [this StackOverflow post](https://stackoverflow.com/a/48078807/1927102)
for the majority of the code that led to this hack!
