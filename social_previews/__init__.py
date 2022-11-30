"""A small sphinx extension to add "copy" buttons to code blocks.

Design principles:

- Assume a two-line title, don't allow three lines, and one line should look OK.
"""
from pathlib import Path
import matplotlib
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
from sphinxext.opengraph import get_tags

matplotlib.use("agg")

HERE = Path(__file__).parent
MAX_CHAR_TAGLINE = 180
MAX_CHAR_PAGETITLE = 65

def render_page_card(app, pagename, templatename, context, doctree):
    """Create a social preview card using page metadata."""
    if not doctree:
        return

    social_preview_config = app.config.social_preview_config or {}
    
    # Set up metadata for the card
    tags = get_tags(app, context, doctree, app.config)

    def parse_ogp_tag(tags, entry):
        return tags.split(entry)[-1].split("content=")[1].split('/>')[0].strip().strip('"')
    tagline = parse_ogp_tag(tags, "og:description")
    pagetitle = parse_ogp_tag(tags, "og:title")
    sitetitle = context.get("docstitle", "")

    if social_preview_config.get("image"):
        image = Path(app.builder.srcdir) / social_preview_config.get("image")
    else:
        image = None

    if social_preview_config.get("image_shadow"):
        image_shadow = Path(app.builder.srcdir) / social_preview_config.get("image_shadow")
    else:
        image_shadow = None

    # Page title formatting
    if len(pagetitle) > MAX_CHAR_PAGETITLE:
        pagetitle = pagetitle[:MAX_CHAR_PAGETITLE] + "..."

    # Generate the card
    if hasattr(app.env, "figure_social_card"):
        fig = app.env.figure_social_card
    else:
        fig = None
    fig = create_social_card(sitetitle, pagetitle, tagline, image, image_shadow, fig=fig)

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
    image_shadow=None,
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
        ax_x, ax_y, ax_w, ax_h = (0.68, 0.64, 0.25, 0.25) 
        axim = fig.add_axes((ax_x, ax_y, ax_w, ax_h), anchor="NE")

        # Image shadow axis
        ax_x, ax_y, ax_w, ax_h = (0.82, 0.12, 0.1, 0.1) 
        aximsh = fig.add_axes((ax_x, ax_y, ax_w, ax_h), anchor="NE")

        # Line at the bottom axis
        axline = fig.add_axes((-.1, -.03, 1.2, .1))
    else:
        for ax in fig.axes:
            ax.clear()
        axtext, axim, aximsh, axline = fig.axes

    # Axes configuration
    left_margin = 0.05
    with plt.rc_context({"font.sans-serif": [font], "text.color": text_color}):
        # Site title
        # Smaller font, just above page title
        site_title_y_offset = 0.87
        axtext.text(
            left_margin,
            site_title_y_offset,
            site_title,
            {
                "size": 14,
            },
            ha="left",
            va="top",
            wrap=True,
        )

        # Page title
        # A larger font for more visibility
        page_title_y_offset = 0.75

        txt_page = axtext.text(
            left_margin,
            page_title_y_offset,
            page_title,
            {"size": 22, "color": "k"},
            ha="left",
            va="top",
            wrap=True,
        )
        txt_page._get_wrap_line_width = lambda: 400

        # Tagline
        # Just below site title, smallest font and many lines.
        tagline_y_axis_ofset = 0.15
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

    if image_shadow:
        img = mpimg.imread(image_shadow)
        aximsh.imshow(img)
        aximsh.set_axis_off()

    # Put a colored line at the bottom of the figure
    axline.set_axis_off()
    axline.hlines(0, 0, 1, lw=8, color="#5A626B")
    return fig
