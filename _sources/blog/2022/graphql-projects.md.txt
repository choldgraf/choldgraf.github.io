---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.2
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
date: "2022-12-07"
tags: github, graphql
category: til
---

# Convert a GitHub Project into a Pandas DataFrame with GraphQL

Had to create a new Personal Access Token and add the `projects:read` scope to it.

## Create a query to find a Project ID

[Here's the project I used](https://github.com/users/choldgraf/projects/3).
And here's the query to return its Unique ID:

```
query{
  organization(login: "choldgraf"){
    projectV2(number: 3) {
      id
    }
  }
}
```

## Create a query to grab information about this project

From [the GitHub Projects (beta) GraphQL docs](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/using-the-api-to-manage-projects).

Copy/paste the section on **Finding information about items in a project**.

```
curl --request POST \
  --url https://api.github.com/graphql \
  --header 'Authorization: Bearer TOKEN' \
  --data '{"query":"query{ node(id: \"PROJECT_ID\") { ... on ProjectV2 { items(first: 20) { nodes{ id fieldValues(first: 8) { nodes{ ... on ProjectV2ItemFieldTextValue { text field { ... on ProjectV2FieldCommon {  name }}} ... on ProjectV2ItemFieldDateValue { date field { ... on ProjectV2FieldCommon { name } } } ... on ProjectV2ItemFieldSingleSelectValue { name field { ... on ProjectV2FieldCommon { name }}}}} content{ ... on DraftIssue { title body } ...on Issue { title assignees(first: 10) { nodes{ login }}} ...on PullRequest { title assignees(first: 10) { nodes{ login }}}}}}}}}"}'
```

We need to make this prettier in order to figure out how to work with it.
To do so, head to the [GitHub GraphQL Explorer](https://docs.github.com/en/graphql/overview/explorer).
Paste in the query and fix the `\"PROJECT_UD\"` to be correct.
Hit **`Prettify`** so that it looks nice and is easier to work with.
Debug there until the output looks correct.

````{admonition} Here's how it looks when prettified!
:class: dropdown
```
{
  node(id: "%s") {
    ... on ProjectV2 {
      items(first: 20) {
        nodes {
          id
          fieldValues(first: 8) {
            nodes {
              ... on ProjectV2ItemFieldTextValue {
                text
                field {
                  ... on ProjectV2FieldCommon {
                    name
                  }
                }
              }
              ... on ProjectV2ItemFieldDateValue {
                date
                field {
                  ... on ProjectV2FieldCommon {
                    name
                  }
                }
              }
              ... on ProjectV2ItemFieldSingleSelectValue {
                name
                field {
                  ... on ProjectV2FieldCommon {
                    name
                  }
                }
              }
            }
          }
          content {
            ... on DraftIssue {
              title
              body
            }
            ... on Issue {
              title
              body
              url
            }
            ... on PullRequest {
              title
              body
              url
            }
          }
        }
      }
    }
  }
}
```
````

This gives us the data we need, but now we need to turn it into something usable.
To do so, let's use Python to parse the data and turn it into a DataFrame.

## Wrap it into Python

Below is a collection of Python code that will do the following:

1. Authenticate with a Personal Access Token
2. Run a GraphQL query to find the Project ID, given a `project number` and `org`
3. Run a GraphQL query to list metadata about `Project ID`.
4. Convert it into a Pandas DataFrame

First off, we handle imports and authenticate:

```{code-cell}
import requests
import os
from rich import print

# An authentication token that provides access
auth = os.environ["GITHUB_TOKEN"]

# The GitHub GraphQL API endpoint
url = "https://api.github.com/graphql"
```

### Find the project ID

Next we list the Unique ID of the project I want:

```{code-cell}
# List the unique ID of a project number for this organization
name = "choldgraf"
kind = "user"  # or `organization`
number = "3"
query = {"query": """
{
  %s(login: "%s") {
    projectV2(number: %s) {
      id
    }
  }
}
""" % (kind, name, number)}
resp = requests.post(url, json=query, headers={"Authorization": f"Bearer {auth}"})
pid = resp.json()["data"]["user"]["projectV2"]["id"]
print(resp.json()["data"])
```

### Grab metadata for each item in the project

Finally, we use that ID to list the values of various fields in this project for each item.

```{code-cell}
# For each entry in the project, grab all of the Text, Date, and SingleSelect fields
query = {"query": """
{
  node(id: "%s") {
    ... on ProjectV2 {
      items(first: 20) {
        nodes {
          id
          fieldValues(first: 8) {
            nodes {
              ... on ProjectV2ItemFieldTextValue {
                text
                field {
                  ... on ProjectV2FieldCommon {
                    name
                  }
                }
              }
              ... on ProjectV2ItemFieldDateValue {
                date
                field {
                  ... on ProjectV2FieldCommon {
                    name
                  }
                }
              }
              ... on ProjectV2ItemFieldSingleSelectValue {
                name
                field {
                  ... on ProjectV2FieldCommon {
                    name
                  }
                }
              }
            }
          }
          content {
            ... on DraftIssue {
              body
            }
            ... on Issue {
              body
              url
            }
            ... on PullRequest {
              body
              url
            }
          }
        }
      }
    }
  }
}
""" % (pid)}
resp = requests.post(url, json=query, headers={"Authorization": f"Bearer {auth}"})
print(resp.json()["data"]["node"]["items"]["nodes"])
```

### Convert into a DataFrame

Finally we convert it into a DataFrame for nice printing.

```{code-cell}
import pandas as pd
df = []
for itemnode in resp.json()["data"]["node"]["items"]["nodes"]:
    # We'll use this to collect metadata about this post
    dfrow = {}

    # A few metadata values we pass straight through (if they exist)
    passthrough = {"body":"issuebody", "url":"url"}
    for key, newkey in passthrough.items():
        if key in itemnode:
            dfrow[newkey] = itemnode[key]
    
    # This will add the title and body of the project item
    dfrow.update(itemnode["content"])
    
    for fieldnode in itemnode["fieldValues"]["nodes"]:
        if not fieldnode:
            continue
        name = fieldnode["field"]["name"]
        entry = fieldnode.get("text", fieldnode.get("date", fieldnode.get("name")))
        dfrow[name] = entry
    df.append(dfrow)

# Convert to DF and rename    
df = pd.DataFrame(df)
df = df.rename(columns={"body": "Body", "url": "URL"})
df = df.loc[:, ["Title", "Date", "URL", "Status", "Body"]]
```

And voila, we now have a nicely-formatted table from our GitHub Project:

```{code-cell}
df.style.hide(axis="index")
```
