---
tags:
- sphinx
date: "2023-02-15"
category: "til"
---

# A Sphinx directive for social media embeds

:::{note} This probably doesn't work anymore
I've since moved my blog to use [the MyST Document Engine](https://mystmd.org) so this example will no longer work on my personal blog. See [this permalink for the latest working version](https://github.com/choldgraf/choldgraf.github.io/blob/ae8ee9792c74aac72f46c645d19352abc439d572/blog/2023/social-directive.md).
:::

I often want to link to social and other types of web-based media in my Sphinx documentation and blog.
Rather than embedding it all in custom HTML code, I decided to write a little wrapper to turn it into a directive.

It's called `{socialpost}`, and it works with Twitter, Mastodon, and YouTube links.

## How it works

Here's a brief description of how this directive works:

1. Parse the directive content (the thing that comes after `{socialpost}`, e.g. `https://twitter.com/choldgraf/status/1564614538309390345`)
2. Do some basic pattern matching to decide if it is Twitter / Mastodon / YouTube
3. Parse the URL for the proper unique identifier for the post (e.g. above it is `1564614538309390345`)
4. Use an embed template that embeds this identifier into each service. E.g., for Twitter it is:

   ```html
   <blockquote class="twitter-tweet"><p lang="en" dir="ltr">
     <a href="https://twitter.com/choldgraf/status/1564614538309390345">Tweet from @choldgraf</a>
   </blockquote>
   ```
6. This is all wrapped up in a `Directive` object that outputs an HTML `raw` node so I can pass through raw HTML.
7. Load any necessary JS files if this directive is detected on a page.
   This is done with an `html-page-context` event.
8. I then connected them both to Sphinx in my site's `conf.py` setup function.
