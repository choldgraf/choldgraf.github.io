# -- Project information -----------------------------------------------------

project = 'Predictably Noisy'
copyright = '2022, Chris Holdgraf'
author = 'Chris Holdgraf'

# -- General configuration ---------------------------------------------------

extensions = [
    "myst_nb",
    "ablog",
    "sphinx_panels",
    "sphinxcontrib.bibtex",
    "sphinxext.opengraph",
    "sphinxext.rediraffe",
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', "*import_posts*", "**/pandoc_ipynb/inputs/*", ".nox/*", "README.md"]


# -- Options for HTML output -------------------------------------------------

html_theme = 'pydata_sphinx_theme'

html_theme_options = {
  "github_url": "https://github.com/choldgraf/",
  "twitter_url": "https://twitter.com/choldgraf",
  "search_bar_text": "Search this site...",
  "google_analytics_id": "UA-88310237-1",
  "navbar_end": ["search-field.html", "theme-switcher", "navbar-icon-links"],
}

html_favicon = "_static/favicon.ico"
html_title = "Predictably Noisy"
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
