---
tags: sphinx
date: "2023-02-15"
category: "til"
---

# A Sphinx directive for social media embeds

I often want to link to social and other types of web-based media in my Sphinx documentation and blog.
Rather than embedding it all in custom HTML code, I decided to write a little wrapper to turn it into a directive.

It's called `{socialpost}`, and it works with Twitter, Mastodon, and YouTube links.
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

## Source code

Check out the code that implements this directive below:

```{literalinclude} ../../scripts/social_media/__init__.py
```
