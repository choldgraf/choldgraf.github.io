"""
A helper script to test out what social previews look like.
I should remove this when I'm happy with the result.
"""
# %load_ext autoreload
# %autoreload 2

from social_previews import create_social_card

fig = create_social_card(
    "Chris Holdgraf's website",
    "Correlation vs. Coherence a simple simulation that is pretty long.",
    "This is a tagline, it's a little longer than the rest. This is a tagline, it's a little longer than the rest. This is a tagline, it's a little longer than the rest. This is a tagline, it's a little longer than the rest. This is a tagline, it's a little longer than the rest.",
    "_static/profile-bw.png",
)
fig.savefig("./tmp.png")
fig
