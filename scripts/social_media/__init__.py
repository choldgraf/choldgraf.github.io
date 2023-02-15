"""Allows us to embed Google Drive videos into our docs.
"""
from docutils.parsers.rst import Directive
from docutils import nodes
from docutils.parsers.rst.directives import positive_int
from textwrap import dedent

# This is the structure used for tweets
# example: https://publish.twitter.com/?query=https%3A%2F%2Ftwitter.com%2Fcholdgraf%2Fstatus%2F1564614538309390345&widget=Tweet
TWITTER_TEMPLATE = """
<blockquote class="socialpost twitter-tweet"><p lang="en" dir="ltr">
  <a href="{url}">Tweet from @{author}</a>
</blockquote>
"""

MASTODON_TEMPLATE = """
<iframe src="{url}/embed" class="socialpost mastodon-embed" style="width: 100%; border: 0; border-radius: .5rem;" height="500" allowfullscreen="allowfullscreen"></iframe>'
"""
YOUTUBE_TEMPLATE = '<iframe width="{width}" class="socialpost youtube-embed" style="border-radius: .5rem;" height="{height}" src="{url}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>'


class SocialPost(Directive):
    arguments = 1
    final_argument_whitespace = False
    has_content = True

    option_spec = {"width": positive_int, "height": positive_int}

    def run(self):
        link = self.content[0]
        # Video window defaults to a 16:9 ratio
        width = self.options.get("width", 533)
        height = self.options.get("height", 300)

        # Twitter
        # If Twitter link, parse the author and insert into the frame "share" link and insert its UID into an iframe
        if "twitter.com" in link:
            author = link.split("twitter.com/")[1].split("/")[0]
            out = TWITTER_TEMPLATE.format(url=link, author=author)
        # Mastodon
        # We are making strong assumptions that mastodon links are the only links that have @ in the user field
        # e.g.: https://hachyderm.io/@choldgraf/109858560412115332
        elif link.replace("https://", "").split("/")[1].startswith("@"):
            out = MASTODON_TEMPLATE.format(url=link)
        # Youtube
        # Link ref: https://www.youtube.com/watch?v=dQw4w9WgXcQ
        elif "youtube.com" in link:
            uid = link.split("v=")[-1]
            # In case there were other arguments after the video link
            uid = uid.split("&")[0]
            out = YOUTUBE_TEMPLATE.format(
                width=width, height=height, url=f"https://www.youtube.com/embed/{uid}"
            )
        else:
            raise ValueError(f"Unidentified social link: {link}")

        # Embed in a parent div
        out = f"<div class='social-post-wrapper' style='max-width: 500px; margin: auto;'>{out}</div>"
        # Use a raw pass-through node
        para = nodes.raw("", out, format="html", **{"class": "socialpost"})
        return [para]


def add_social_media_js(app, pagename, templatename, context, doctree):
    """Embed any JS necessary to embed social media posts on a page."""
    TWITTER_EMBED_SCRIPT = "https://platform.twitter.com/widgets.js"
    if not doctree:
        return
    for rawnode in doctree.traverse(nodes.raw):
        if "socialpost" in rawnode.attributes.get("class", []):
            app.add_js_file(
                TWITTER_EMBED_SCRIPT, **{"async": "async", "charset": "utf-8"}
            )
            break
