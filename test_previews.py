"""
A helper script to test out what social previews look like.
I should remove this when I'm happy with the result.
"""
# %load_ext autoreload
# %autoreload 2

from social_previews import create_social_card_objects

tagline = "This is a tagline, it's a little longer than the rest. This is a tagline, it's a little longer than the rest. This is a tagline, it's a little longer than the rest. This is a tagline, it's a little longer than the rest. This is a tagline, it's a little longer than the rest."
fig, txtsite, txtpage, txtdesc, txturl = create_social_card_objects(
    image="_static/profile-bw.png",
    image_shadow="_static/logo-shadow.png",
)

# These are roughly the max characters we enforce
# Leaving here for texting
MAX_CHAR_PAGETITLE = 65
MAX_CHAR_DESCRIPTION = 160

txtsite.set_text("Chris Holdgraf's website")
txtpage.set_text(("A " * (MAX_CHAR_PAGETITLE // 2)) + "...")
txtdesc.set_text(("B " * (MAX_CHAR_DESCRIPTION // 2)) + "...")
txturl.set_text("chrisholdgraf.com")
fig.savefig("./tmp.png")
