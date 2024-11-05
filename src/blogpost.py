#!/usr/bin/env python3
import argparse
import json
import sys
from yaml import safe_load
from pathlib import Path
import pandas as pd
from feedgen.feed import FeedGenerator

DEFAULTS = {"number": 10}

root = Path(__file__).parent.parent

# Aggregate all posts from the markdown and ipynb files
posts = []
for ifile in root.rglob("blog/**/*.md"):
    text = ifile.read_text()
    yaml = safe_load(text.split("---")[1])
    yaml["path"] = ifile.relative_to(root).with_suffix("")
    if "title" not in yaml:
        lines = text.splitlines()
        for ii in lines:
            if ii.strip().startswith("#"):
                yaml["title"] = ii.replace("#", "").strip()
                break
    content = text.split("---", 2)[-1]
    content = "\n".join(ii for ii in content.splitlines() if not ii.startswith("#"))
    N_WORDS = 100
    words = " ".join(content.split(" ")[:N_WORDS])
    yaml["content"] = yaml.get("description", words)
    posts.append(yaml)
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
fg.atom_file(root / "../atom.xml", pretty=True)
fg.rss_file(root / "rss.xml", pretty=True)

plugin = {
    "name": "Blog Post list",
    "directives": [
        {
            "name": "postlist",
            "doc": "An example directive for showing a nice random image at a custom size.",
            "alias": ["bloglist"],
            "arg": {},
            "options": {
                "number": {
                    "type": "int",
                    "doc": "The number of posts to include",
                }
            },
        }
    ],
}

children = []
for ix, irow in posts.iterrows():
    children.append(
        {
            "type": "listItem",
            "spread": True,
            "children": [
                {
                    "type": "link",
                    "url": f"/{irow['path'].with_suffix('')}",
                    "children": [
                        {
                            "type": "text",
                            "value": irow["title"],
                        }
                    ],
                },
                {"type": "text", "value": f' - {irow["date"]:%B %d, %Y}'},
            ],
        }
    )


def declare_result(content):
    """Declare result as JSON to stdout

    :param content: content to declare as the result
    """

    # Format result and write to stdout
    json.dump(content, sys.stdout, indent=2)
    # Successfully exit
    raise SystemExit(0)


def run_directive(name, data):
    """Execute a directive with the given name and data

    :param name: name of the directive to run
    :param data: data of the directive to run
    """
    assert name == "postlist"
    opts = data["node"].get("options", {})
    number = int(opts.get("number", DEFAULTS["number"]))
    output = (
        {
            "type": "list",
            "ordered": False,
            "spread": False,
            "children": [
                {
                    "type": "listItem",
                    "spread": True,
                    "children": children[:number],
                }
            ],
        },
    )
    return output


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--role")
    group.add_argument("--directive")
    group.add_argument("--transform")
    args = parser.parse_args()

    if args.directive:
        data = json.load(sys.stdin)
        declare_result(run_directive(args.directive, data))
    elif args.transform:
        raise NotImplementedError
    elif args.role:
        raise NotImplementedError
    else:
        declare_result(plugin)
