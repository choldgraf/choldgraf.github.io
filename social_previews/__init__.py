"""A small sphinx extension to add "copy" buttons to code blocks.

Design principles:

- Assume a two-line title, don't allow three lines, and one line should look OK.
"""
from docutils.nodes import paragraph
from pathlib import Path
import matplotlib
from matplotlib import pyplot as plt
import matplotlib.image as mpimg

matplotlib.use("agg")

HERE = Path(__file__).parent
MAX_CHAR_TAGLINE = 200
MAX_CHAR_PAGETITLE = 53

def render_page_card(app, pagename, templatename, context, doctree):
    """Create a social preview card using page metadata."""
    if not doctree:
        return

    social_preview_config = app.config.social_preview_config or {}
    
    # Set up metadata for the card
    sitetitle = context.get("docstitle", "")
    pagetitle = context.get("title", "")

    if social_preview_config.get("image"):
        image = Path(app.builder.srcdir) / social_preview_config.get("image")
    else:
        image = None

    # Tagline formatting
    tagline = " ".join([ii.astext() for ii in doctree.traverse(paragraph)])
    tagline = tagline.replace("\n\n", "\n")
    tagline = tagline.replace("\n", "")
    if len(tagline) > MAX_CHAR_TAGLINE:
        tagline = tagline[:MAX_CHAR_TAGLINE].rsplit(" ", 1)[0] + "..."

    # Page title formatting
    if len(pagetitle) > MAX_CHAR_PAGETITLE:
        pagetitle = pagetitle[:MAX_CHAR_PAGETITLE] + "..."

    # Generate the card
    if hasattr(app.env, "figure_social_card"):
        fig = app.env.figure_social_card
    else:
        fig = None
    fig = create_social_card(sitetitle, pagetitle, tagline, image, fig=fig)

    app.env.figure_social_card = fig
    # Save the image to a static directory
    path_images = "_images/social_previews"
    static_dir = Path(app.builder.outdir) / path_images
    static_dir.mkdir(exist_ok=True, parents=True)
    path_out = f"summary_{pagename.replace('/', '_')}.png"
    fig.savefig(static_dir / path_out)

    # Link the image in our page metadata
    url = app.config.ogp_site_url.strip("/")
    path_out_image = f"{url}/{path_images}/{path_out}"
    metatags = context["metatags"].split("\n")
    for ii, tag in enumerate(metatags):
        if "og:image" in tag:
            metatags[ii] = f'<meta property="og:image" content="{path_out_image}" />'
            break
    metatags.append('<meta name="twitter:card" content="summary_large_image" />')
    context["metatags"] = "\n".join(metatags)


def create_social_card(
    site_title,
    page_title,
    tagline,
    image=None,
    text_color="#4a4a4a",
    background_color="white",
    font="Roboto",
    fig=None,
):
    # Size of figure
    ratio = 1200 / 628
    # Because Matplotlib doesn't let you specify figures in pixels, only inches
    multiple = 3
    if fig is None:
        fig = plt.figure(figsize=(ratio * multiple, multiple))
        fig.set_facecolor(background_color)

        # Text axis
        axtext = fig.add_axes((0, 0, 1, 1))

        # Image axis
        ax_x, ax_y, ax_w, ax_h = (0.75, 0.73, 0.2, 0.2) 
        axim = fig.add_axes((ax_x, ax_y, ax_w, ax_h), anchor="NE")

        # Line at the bottom axis
        axline = fig.add_axes((-.1, -.03, 1.2, .1))
    else:
        for ax in fig.axes:
            ax.clear()
        axtext, axim, axline = fig.axes

    # Axes configuration
    left_margin = 0.07
    with plt.rc_context({"font.sans-serif": [font], "text.color": text_color}):
        # Site title
        # Smaller font, just above page title
        site_title_y_offset = 0.82
        axtext.text(
            left_margin,
            site_title_y_offset,
            site_title,
            {
                "size": 16,
            },
            ha="left",
            va="top",
            wrap=True,
        )

        # Page title
        # A larger font for more visibility
        page_title_y_offset = 0.67

        txt_page = axtext.text(
            left_margin,
            page_title_y_offset,
            page_title,
            {"size": 22, "color": "k"},
            ha="left",
            va="top",
            wrap=True,
        )
        txt_page._get_wrap_line_width = lambda: 430

        # Tagline
        # Just below site title, smallest font and many lines.
        tagline_y_axis_ofset = 0.23
        txt_tagline = axtext.text(
            left_margin,
            tagline_y_axis_ofset,
            tagline,
            {"size": 11},
            ha="left",
            va="bottom",
            wrap=True,
        )
        txt_tagline._get_wrap_line_width = lambda: 450

        # Turn off the axis so we see no ticks
        axtext.set_axis_off()

    # Put the logo in the top right if it exists
    if image:
        img = mpimg.imread(image)
        axim.imshow(img)
        axim.set_axis_off()

    # Put a colored line at the bottom of the figure
    axline.set_axis_off()
    axline.hlines(0, 0, 1, lw=8, color="#5A626B")
    return fig
