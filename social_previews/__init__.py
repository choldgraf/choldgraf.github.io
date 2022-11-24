"""A small sphinx extension to add "copy" buttons to code blocks."""
from docutils.nodes import paragraph
from pathlib import Path
import matplotlib
from matplotlib import pyplot as plt
import matplotlib.image as mpimg

matplotlib.use("agg")

HERE = Path(__file__).parent
MAX_CHAR = 150


def render_page_card(app, pagename, templatename, context, doctree):
    """Create a social preview card using page metadata."""
    if not doctree:
        return

    # Set up metadata for the card
    sitetitle = context.get("docstitle", "")
    pagetitle = context.get("title", "")
    image = context.get("logo", "")
    if image:
        image = Path(app.builder.srcdir) / "_static" / image

    tagline = " ".join([ii.astext() for ii in doctree.traverse(paragraph)])
    tagline = tagline.replace("\n\n", "\n")
    tagline = tagline.replace("\n", "")
    if len(tagline) > MAX_CHAR:
        tagline = tagline[:MAX_CHAR].rsplit(" ", 1)[0] + "..."

    # Generate the card
    fig = create_social_card(sitetitle, pagetitle, tagline, image)

    # Save the image to a static directory
    static_dir = Path(app.builder.outdir) / "_static/images/social_previews"
    static_dir.mkdir(exist_ok=True, parents=True)
    path_out = f"summary_{pagename.replace('/', '_')}.png"
    fig.savefig(static_dir / path_out)

    # Link the image in our page metadata
    url = app.config.ogp_site_url.strip("/")
    path_out_image = f"{url}/_static/images/social_previews/{path_out}"
    context[
        "metatags"
    ] += f"""
    <meta property="og:image" content="{path_out_image}" />
    <meta name="twitter:card" content="summary_large_image" />
    """


def create_social_card(
    site_title,
    page_title,
    tagline,
    image=None,
    text_color="#4a4a4a",
    background_color="white",
    font="Roboto",
):
    # Size of figure
    ratio = 1200 / 628
    # Because Matplotlib doesn't let you specify figures in pixels, only inches
    multiple = 3
    fig = plt.figure(figsize=(ratio * multiple, multiple))
    fig.set_facecolor(background_color)
    left_margin = 0.07

    with plt.rc_context({"font.sans-serif": [font], "text.color": text_color}):
        # Site title
        # Smaller font, just above page title
        axtext = fig.add_axes((0, 0, 1, 1))
        site_title_y_offset = 0.87
        txt_title = axtext.text(
            left_margin,
            site_title_y_offset,
            site_title,
            {
                "size": 12,
            },
            ha="left",
            va="top",
            wrap=True,
        )

        # Page title
        # A larger font for more visibility
        page_title_y_offset = 0.72
        txt_page = axtext.text(
            left_margin,
            page_title_y_offset,
            page_title,
            {"size": 24, "color": "k"},
            ha="left",
            va="top",
            wrap=True,
        )
        txt_page._get_wrap_line_width = lambda: 430

        # Tagline
        # Just below site title, smallest font and many lines.
        tagline_y_axis_ofset = 0.25
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
        ax_x, ax_y, ax_w, ax_h = (0.75, 0.73, 0.2, 0.2) 
        axim = fig.add_axes((ax_x, ax_y, ax_w, ax_h), anchor="NE")
        axim.imshow(img)
        axim.set_axis_off()

    # Put a colored line at the bottom of the figure
    axline = fig.add_axes((-.1, -.03, 1.2, .1))
    axline.set_axis_off()
    axline.hlines(0, 0, 1, lw=8, color="#5A626B")
    return fig
