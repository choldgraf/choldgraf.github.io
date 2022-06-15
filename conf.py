# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Predictably Noisy'
copyright = '2020, Chris Holdgraf'
author = 'Chris Holdgraf'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_nb",
    "ablog",
    "sphinx_panels",
    "sphinxcontrib.bibtex",
    "sphinxext.opengraph",
    "sphinxext.rediraffe",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', "*import_posts*", "**/pandoc_ipynb/inputs/*", ".nox/*", "README.md"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'pydata_sphinx_theme'

html_theme_options = {
  "github_url": "https://github.com/choldgraf/",
  "twitter_url": "https://twitter.com/choldgraf",
  "search_bar_text": "Search this site...",
  "google_analytics_id": "UA-88310237-1",
  "navbar_end": ["search-field.html", "navbar-icon-links"],
}

html_favicon = "_static/favicon.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_extra_path = ["feed.xml"]
html_sidebars = {
    "index": ["hello.html"],
    "about": ["hello.html"],
    "publications": ["hello.html"],
    "projects": ["hello.html"],
    "talks": ["hello.html"],
    "posts/**": ['postcard.html', 'recentposts.html', 'archives.html'],
    "blog": ['tagcloud.html', 'archives.html'],
    "blog/**": ['postcard.html', 'recentposts.html', 'archives.html']
}
blog_baseurl = "https://predictablynoisy.com"
blog_title = "Predictably Noisy"
blog_path = "blog"
fontawesome_included = True
blog_post_pattern = "posts/*/*"
post_redirect_refresh = 1
post_auto_image = 1
post_auto_excerpt = 2

# Panels config
panels_add_bootstrap_css = False

# MyST config
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "html_image",
]

# Bibliography and citations
bibtex_bibfiles = ["_static/works.bib"]

# OpenGraph config
ogp_site_url = "https://predictablynoisy.com"
ogp_image = "https://predictablynoisy.com/_static/profile-bw.png"

# Temporarily stored as off until we fix it
jupyter_execute_notebooks = "off"

rediraffe_redirects = {
    "rust-governance.md": "posts/2018/rust_governance.md",
}

def setup(app):
    app.add_css_file("custom.css")
