---
jupytext:
  formats: md:myst
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

% TODO: Add a count of number of words written by month and total

# GitHub year in review

https://docs.github.com/en/graphql/overview/explorer

```python
from github_activity.graphql import GitHubGraphQlQuery
import os
from rich import print
from IPython.display import Markdown
import pandas as pd
import altair as alt
from itertools import product
```

```python
dates = [
    "2022-01-01..2022-06-01",
    "2022-06-01..2022-12-31",
]
kinds = ["author", "commenter"]
username = "choldgraf"
data = []
for date, kind in product(dates, kinds):
    query = f"{kind}:{username} updated:{date} is:issue"
    resp = GitHubGraphQlQuery(query=query, auth=os.environ["GITHUB_TOKEN"])
    resp.request()
    data.append(resp.data)
```

```python
issues = pd.concat(data)
orig = issues.shape[0]
issues = issues.drop_duplicates(subset="id")
new = issues.shape[0]
Markdown(f"Dropped **{orig-new}** duplicate issues...")
```

```python
# Extract comments into a standalone df
comments = []
for ix, row in issues.iterrows():
    # Extract comments
    for edge in row["comments"]["edges"]:
        comment = edge["node"]
        comment["issue_id"] = row["id"]
        comment["repo"] = row["repo"]
        comment["org"] = row["org"]
        comments.append(comment)
comments = pd.DataFrame(comments)

# Convert date fields into datetime objects
date_fields = ["updatedAt", "createdAt", "closedAt"]
for field in date_fields:
    if field in comments.columns:
        comments[field] = pd.to_datetime(comments[field])
    if field in issues.columns:
        issues[field] = pd.to_datetime(issues[field])
    
# Only include comments from this year
comments = comments[comments["updatedAt"] > "2022-01-01"]
```

## Issues created

```python
opened = issues[issues["createdAt"] > "2022-01-01"]
closed = issues[issues["closedAt"] > "2022-01-01"]
```

### Over time

```python
weekly = opened.groupby(["org"]).resample("M", on="createdAt").count()["state"].reset_index()
top_orgs = weekly.groupby("org").sum().sort_values("state", ascending=False).head(10).index.values
weekly = weekly.query("org in @top_orgs")
alt.Chart(weekly, width=500).mark_bar(width=25).encode(
    x="createdAt",
    y="state",
    color="org",
    order=alt.Order('sum(state):Q', sort='descending'),
    tooltip=["state", "org"],
).interactive()
```

### By repository

```python
charts = []
for kind, name in [(opened, "opened"), (closed, "closed")]:
    counts = kind.groupby(["org", "repo"]).agg({"state": "count"}).rename(columns={"state": "count"})
    plt_counts = counts.reset_index().sort_values("count", ascending=False).head(20)
    plt_counts["orgrepo"] = plt_counts.apply(lambda a: f"{a['org']}/{a['repo']}", axis=1)
    ch = alt.Chart(plt_counts, title=f"{name} issues in 2022").mark_bar().encode(
        x=alt.X("orgrepo", sort=alt.SortField("count", order="descending")),
        y="count",
        tooltip=["org", "repo", "count"],
        color="org",
    ).interactive()
    charts.append(ch)
charts[0] & charts[1]
```

### By activity


Most comments

```python
my_issues = opened.query("author=='choldgraf'").copy()
my_issues["ncomments"] = my_issues["comments"].map(lambda a: len(a["edges"]))
my_issues.sort_values("ncomments", ascending=False).query("ncomments > 5")
```

Most thumbs up

```python
opened.query("author=='choldgraf'").sort_values(["thumbsup"], ascending=False)
```

## GitHub Comments

```python
Markdown(f"Total comments: **{comments.shape[0]}**")
```

```python
counts = comments.groupby(["org", "repo"]).agg({"url": "count"}).rename(columns={"url": "count"}).reset_index()
```

```python
counts
```

```python
top_orgs = counts.groupby("org").sum().sort_values("count", ascending=False).head(10).index.values
plt_counts = counts.query("org in @top_orgs")
alt.Chart(plt_counts, width=500).mark_bar(width=25).encode(
    x=alt.X("org", sort=alt.SortField("count")),
    y="count",
    color="org",
    tooltip=["count", "org"],
).interactive()
```
