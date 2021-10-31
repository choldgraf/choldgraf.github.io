---
tags: python blogging jekyll
permalink: jekyll-markdown-nbconvert
category: blogging
date: 2018-05-23
---

# Blogging with Jupyter Notebooks and Jekyll using nbconvert templates

Here's a quick (and hopefully helpful) post for those wishing to blog in
Jekyll using Jupyter notebooks. As some of you may know, `nbconvert` can
easily convert your `.ipynb` files to markdown, which Jekyll can easily
turn into blog posts for you.

```
nbconvert --to markdown myfile.ipynb
```

However, an annoying part of this is that Markdown doesn't include classes
for input and outputs, which means they each get treated the same in the
output. Not ideal.

Fortunately, [you can customize nbconvert extensively](https://nbconvert.readthedocs.io/en/latest/external_exporters.html).
First, it's possible to [create your *own* exporter class](https://nbconvert.readthedocs.io/en/latest/external_exporters.html#writing-a-custom-exporter), but this is a bit heavy for what we want to do. In our case, we'd
simply like to _extend_ the markdown exporter so that it outputs Jekyll-friendly
markdown.

## Extending `nbconvert's` markdown template

Because `nbconvert` uses Liquid Templates for its exporters, this is
relatively easy! For example,
[here is `nbconvert`'s markdown template](https://github.com/jupyter/nbconvert/blob/master/nbconvert/templates/markdown.tpl).
You can see how it extends another template, then adds some modifications of
its own. What we need to do is create a new template that slightly modifies
the functionality of `nbconvert`'s markdown template. Then we can use the same
markdown exporter, but with our custom template defining how the markdown is
created.

To treat input and output text differently, we'll extend `nbconvert`'s base
markdown template by creating a template file of our own. Simply write the
following lines into a file called `mytemplate.tpl`.

{% highlight html %}
{% raw %}
  {% extends 'markdown.tpl' %}

  <!-- Add Div for input area -->
  {% block input %}
  <div class="input_area" markdown="1">
  {{ super() }}
  </div>
  {% endblock input %}

  <!-- Remove indentations for output text and add div classes  -->
  {% block stream %}
  {:.output_stream}
  ```
  {{ output.text }}
  ```
  {% endblock stream %}


  {% block data_text %}
  {:.output_data_text}
  ```
  {{ output.data['text/plain'] }}
  ```
  {% endblock data_text %}


  {% block traceback_line  %}
  {:.output_traceback_line}
  ```
  {{ line | strip_ansi }}
  ```
  {% endblock traceback_line  %}

  <!-- Tell Jekyll not to render HTML output blocks as markdown -->
  {% block data_html %}
  <div markdown="0">
  {{ output.data['text/html'] }}
  </div>
  {% endblock data_html %}
{% endraw %}
{% endhighlight %}

Above, we're doing two things:

1. Overriding the input area block so that it is now wrapped in `<div>` tags.
   Note that we can set a custom class, and set `markdown="1"` so that the
   markdown conversion occurs within the div.
2. Overriding various output text blocks so that we remove the indentation
   that was used to denote a "code" cell. Instead, we'll wrap the output text
   in more common ```` ``` ```` characters, and use a trick to add a class to
   code blocks: `{:.class_name}` syntax.

We can then directly reference this template when we call `nbconvert`:

```
nbconvert --to markdown --template path/to/mytemplate.tpl myfile.ipynb
```

As a result, we now have classes around each of these divs that we can style
however we like. For example, here are the CSS rules I added to remove the
theme's "code box" around each of the output areas:

```css
.input_area div.highlighter-rouge {
  background-color: #f7f7f7  !important;
}

.output_stream, .output_data_text, .output_traceback_line {
  margin-left: 2% !important;
  border: none !important;
  border-radius: 4px !important;
  background-color: #fafafa !important;
  box-shadow: none !important;
}

.output_stream:before, .output_data_text:before, .output_traceback_line:before{
  content: none !important;
}
```

It took me a while to figure out this pattern, so hopefully other people find
it useful as well!
