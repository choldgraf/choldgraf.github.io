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
    "sphinxcontrib.twitter",
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

html_favicon = "_static/favicon.ico"
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

# -- ABlog ---------------------------------------------------

blog_baseurl = "https://chrisholdgraf.com"
blog_title = "Chris Holdgraf"
blog_path = "blog"
fontawesome_included = True
blog_post_pattern = "blog/*/*"
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
nb_execution_mode = "auto"

def setup(app):
    app.add_css_file("custom.css")
