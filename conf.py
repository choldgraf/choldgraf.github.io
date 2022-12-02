# -- Project information -----------------------------------------------------

project = "Chris Holdgraf"
copyright = "2022, Chris Holdgraf"
author = "Chris Holdgraf"

extensions = [
    "myst_nb",
    "ablog",
    "sphinx_design",
    "sphinx_copybutton",
    "sphinx_examples",
    "sphinxext.opengraph",
    "sphinxext.rediraffe",
]

templates_path = ["_templates"]
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "*import_posts*",
    "**/pandoc_ipynb/inputs/*",
    ".nox/*",
    "README.md",
    "**/.ipynb_checkpoints/*"
]
import sys
sys.path.append(".")

# -- HTML output -------------------------------------------------

html_theme = "pydata_sphinx_theme"

html_theme_options = {
    "search_bar_text": "Search this site...",
    "analytics": {"google_analytics_id": "UA-88310237-1"},
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/choldgraf/",
            "icon": "fa-brands fa-github",
        },
        {
            "name": "Twitter",
            "url": "https://twitter.com/choldgraf",
            "icon": "fa-brands fa-twitter",
        },
        {
            "name": "Mastodon",
            "url": "https://hachyderm.io/@choldgraf",
            "icon": "fa-brands fa-mastodon",
            "attributes": {"rel": "me"},
        },
        {
            "name": "Blog RSS feed",
            "url": "https://chrisholdgraf.com/blog/atom.xml",
            "icon": "fa-solid fa-rss",
        },
    ],
}

html_favicon = "_static/profile-color-circle-small.png"
html_title = "Chris Holdgraf"
html_static_path = ["_static"]
html_extra_path = ["feed.xml"]
html_sidebars = {
    "index": ["hello.html"],
    "about": ["hello.html"],
    "publications": ["hello.html"],
    "projects": ["hello.html"],
    "talks": ["hello.html"],
    "blog": ["categories.html", "tagcloud.html", "archives.html"],
    "blog/**": ["postcard.html", "recentposts.html", "archives.html"],
}

# OpenGraph config
ogp_site_url = "https://chrisholdgraf.com"
ogp_image = "https://chrisholdgraf.com/_static/profile-bw.png"

rediraffe_redirects = {
    "rust-governance.md": "blog/2018/rust_governance.md",
}
# Update the posts/* section of the rediraffe redirects to find all files
redirect_folders = {
    "posts": "blog",
}
from pathlib import Path

for old, new in redirect_folders.items():
    for newpath in Path(new).rglob("**/*"):
        if newpath.suffix in [".ipynb", ".md"] and "ipynb_checkpoints" not in str(newpath):
            oldpath = str(newpath).replace("blog/", "posts/", 1)
            # Skip pandoc because for some reason it's broken
            if "pandoc" not in str(newpath):
                rediraffe_redirects[oldpath] = str(newpath)


# -- Social Previews -----------------------------------------

# social_preview = {
#     "image": 
#     "tagline":
#     "color_bar":
# }

# -- ABlog ---------------------------------------------------

blog_baseurl = "https://chrisholdgraf.com"
blog_title = "Chris Holdgraf"
blog_path = "blog"
blog_post_pattern = "blog/*/*"
blog_feed_fulltext = True
blog_feed_subtitle = "Open communities, open science, communication, and data."
fontawesome_included = True
post_redirect_refresh = 1
post_auto_image = 1
post_auto_excerpt = 2

# -- MyST and MyST-NB ---------------------------------------------------

# MyST
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "html_image",
]

# MyST-NB
# Don't execute anything by default because many old posts don't execute anymore
# and this slows down build times.
# Instead if I want something to execute, manually set it in the post's metadata.
nb_execution_mode = "off"

from social_previews import render_page_card, setup_social_card_images

def setup(app):
    app.add_css_file("custom.css")
    app.connect("builder-inited", setup_social_card_images)
    app.connect("html-page-context", render_page_card)
    app.add_config_value("social_preview_config", None, True)

social_preview_config = {
    "image": "_static/profile-color-circle.png",
    "image_shadow": "_static/logo-shadow.png",
    "tagline": "Thoughts and ideas from Chris' blog.",
    "line_color": "#4078c0",
    "add_site_url": True,
}
