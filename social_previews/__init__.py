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
MAX_CHAR_description = 180
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
    description = social_preview_config.get("description")
    if description is None:
        description = parse_ogp_tag(tags, "og:description")
    pagetitle = parse_ogp_tag(tags, "og:title")
    sitetitle = context.get("docstitle", "")

    if social_preview_config.get("image"):
        image = Path(app.builder.srcdir) / social_preview_config.get("image")
    else:
        image = None

    # Grab the image shadow PNG for plotting
    if social_preview_config.get("image_shadow"):
        image_shadow = Path(app.builder.srcdir) / social_preview_config.get("image_shadow")
    else:
        image_shadow = None

    # Line color at the bottom
    line_color = social_preview_config.get("line_color")

    # Page title formatting
    if len(pagetitle) > MAX_CHAR_PAGETITLE:
        pagetitle = pagetitle[:MAX_CHAR_PAGETITLE] + "..."

    # Generate the card
    if not hasattr(app.env, "figure_social_card"):
        # First time this is run we need to create a bunch of Matplotlib objects
        # This is slow so we only do it once
        fig, txt_sitetitle, txt_pagetitle, txt_description = create_social_card(sitetitle, pagetitle, description, image, image_shadow, line_color=line_color)
        app.env.figure_social_card = [fig, txt_sitetitle, txt_pagetitle, txt_description]
    else:
        # The social card figure and axes already exist
        # So we just update them in order to save time
        fig, txt_sitetitle, txt_pagetitle, txt_description = app.env.figure_social_card
        update_social_card(txt_sitetitle, txt_pagetitle, txt_description, sitetitle, pagetitle, description)

    # Save the image to a static directory
    path_images = "_images/social_previews"
    static_dir = Path(app.builder.outdir) / path_images
    static_dir.mkdir(exist_ok=True, parents=True)
    path_out = f"summary_{pagename.replace('/', '_')}.png"
    fig.savefig(static_dir / path_out)

    # Link the image in our page metadata
    url = app.config.ogp_site_url.strip("/")
    path_out_image = f"{url}/{path_images}/{path_out}"
    context[
        "metatags"
    ] += f"""
    <meta property="og:image" content="{path_out_image}" />
    <meta name="twitter:card" content="summary_large_image" />
    """


def create_social_card(
    site_title,
    page_title,
    description,
    image=None,
    image_shadow=None,
    text_color="#4a4a4a",
    background_color="white",
    line_color="#5A626B",
    font="Roboto",
    fig=None,
):
    # Size of figure
    ratio = 1200 / 628
    # Because Matplotlib doesn't let you specify figures in pixels, only inches
    multiple = 3
    fig = plt.figure(figsize=(ratio * multiple, multiple))
    fig.set_facecolor(background_color)

    # Text axis
    axtext = fig.add_axes((0, 0, 1, 1))

    # Image axis
    ax_x, ax_y, ax_w, ax_h = (0.68, 0.64, 0.25, 0.25) 
    axim_logo = fig.add_axes((ax_x, ax_y, ax_w, ax_h), anchor="NE")

    # Image shadow axis
    ax_x, ax_y, ax_w, ax_h = (0.82, 0.10, 0.1, 0.1) 
    axim_shadow = fig.add_axes((ax_x, ax_y, ax_w, ax_h), anchor="NE")

    # Line at the bottom axis
    axline = fig.add_axes((-.1, -.03, 1.2, .1))

    # Axes configuration
    left_margin = 0.05
    with plt.rc_context({"font.sans-serif": [font], "text.color": text_color}):
        # Site title
        # Smaller font, just above page title
        site_title_y_offset = 0.87
        txt_site = axtext.text(
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

        # description
        # Just below site title, smallest font and many lines.
        description_y_axis_ofset = 0.35
        txt_description = axtext.text(
            left_margin,
            description_y_axis_ofset,
            description,
            {"size": 11},
            ha="left",
            va="top",
            wrap=True,
        )
        txt_description._get_wrap_line_width = lambda: 450

        # Turn off the axis so we see no ticks
        axtext.set_axis_off()

    if image_shadow:
        img = mpimg.imread(image_shadow)
        axim_shadow.imshow(img)
        axim_shadow.set_axis_off()

    # Put the logo in the top right if it exists
    if image:
        img = mpimg.imread(image)
        axim_logo.imshow(img)
        axim_logo.set_axis_off()

    # Put a colored line at the bottom of the figure
    axline.set_axis_off()
    axline.hlines(0, 0, 1, lw=8, color=line_color)
    return fig, txt_site, txt_page, txt_description


def update_social_card(
    ax_sitetitle,
    ax_pagetitle,
    ax_description,
    site_title,
    page_title,
    description,
):
    ax_sitetitle.set_text(site_title)
    ax_pagetitle.set_text(page_title)
    ax_description.set_text(description)