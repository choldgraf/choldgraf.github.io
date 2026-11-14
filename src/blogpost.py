#!/usr/bin/env python3
import argparse
import json
import sys
from yaml import safe_load
from pathlib import Path
import pandas as pd
from feedgen.feed import FeedGenerator

root = Path(__file__).parent.parent

# Aggregate all posts from the markdown and ipynb files
posts = []
for ifile in root.rglob("blog/**/*.md"):
    if "drafts" in str(ifile):
        continue

    text = ifile.read_text()
    try:
        _, meta, content = text.split("---", 2)
    except Exception:
        print(f"Skipping file with error: {ifile}", file=sys.stderr)
        continue

    # Load in YAML metadata
    meta = safe_load(meta)
    meta["path"] = ifile.relative_to(root).with_suffix("")
    if "title" not in meta:
        lines = text.splitlines()
        for ii in lines:
            if ii.strip().startswith("#"):
                meta["title"] = ii.replace("#", "").strip()
                break

    # Summarize content
    skip_lines = ["#", "--", "%", "++"]
    content = "\n".join(
        ii
        for ii in content.splitlines()
        if not any(ii.startswith(char) for char in skip_lines)
    )
    N_WORDS = 50
    words = " ".join(content.split(" ")[:N_WORDS])
    if not "author" in meta or not meta["author"]:
        meta["author"] = "Chris Holdgraf"
    meta["content"] = meta.get("description", words)
    posts.append(meta)
posts = pd.DataFrame(posts)
posts["date"] = pd.to_datetime(posts["date"]).dt.tz_localize("US/Pacific")
posts = posts.dropna(subset=["date"])
posts = posts.sort_values("date", ascending=False)

# Generate an RSS feed
fg = FeedGenerator()
fg.id("http://chrisholdgraf.com")
fg.title("Chris Holdgraf's blog")
fg.author({"name": "Chris Holdgraf", "email": "choldgraf@gmail.com"})
fg.link(href="http://chrisholdgraf.com", rel="alternate")
fg.logo("http://chrisholdgraf.com/_static/profile.jpg")
fg.subtitle("Chris' personal blog!")
fg.link(href="http://chrisholdgraf.com/rss.xml", rel="self")
fg.language("en")

# Add all my posts to it
for ix, irow in posts.iterrows():
    fe = fg.add_entry()
    fe.id(f"http://chrisholdgraf.com/{irow['path']}")
    fe.published(irow["date"])
    fe.title(irow["title"])
    fe.link(href=f"http://chrisholdgraf.com/{irow['path']}")
    fe.content(content=irow["content"])

# Write an RSS feed with latest posts
fg.atom_file(root / "atom.xml", pretty=True)
fg.rss_file(root / "rss.xml", pretty=True)

# ponytail: no directives; loading this as a plugin is what regenerates the RSS feed each build.
plugin = {"name": "Blog RSS feed", "directives": []}


def declare_result(content):
    """Declare result as JSON to stdout

    :param content: content to declare as the result
    """

    # Format result and write to stdout
    json.dump(content, sys.stdout, indent=2)
    # Successfully exit
    raise SystemExit(0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--role")
    group.add_argument("--directive")
    group.add_argument("--transform")
    args = parser.parse_args()

    if args.directive or args.transform or args.role:
        raise NotImplementedError
    declare_result(plugin)
