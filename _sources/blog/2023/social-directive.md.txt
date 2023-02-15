---
tags: sphinx
date: "2023-02-15"
category: "til"
---

# A Sphinx directive for social media embeds

I often want to link to social and other types of web-based media in my Sphinx documentation and blog.
Rather than embedding it all in custom HTML code, I decided to write a little wrapper to turn it into a directive.

It's called `{socialpost}`, and it works with Twitter, Mastodon, and YouTube links.

## Examples

For example:

````{example} Twitter
```{socialpost} https://twitter.com/choldgraf/status/1564614538309390345
```
````

````{example} Mastodon
```{socialpost} https://hachyderm.io/@choldgraf/109858392098988533
```
````

````{example} YouTube
```{socialpost} https://www.youtube.com/watch?v=lZ2FHTkyaMU
```
````

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

## Source code

Here's the source code if you'd like to see how this works:

The directive and event code:

```{literalinclude} ../../scripts/social_media/__init__.py
```

Where I connect it to my site:

```{literalinclude} ../../conf.py
:start-at: "def setup(app):"
```
