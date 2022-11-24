# %load_ext autoreload
# %autoreload 2

from social_previews import create_social_card

fig = create_social_card(
    "Chris Holdgraf's website",
    "Here's my page title, it's a bit longer",
    "This is a tagline, it's a little longer than the rest. This is a tagline, it's a little longer than the rest. This is a tagline, it's a little longer than the rest.",
    "_static/profile-bw.png",
)
fig.savefig("./tmp.png")
fig
