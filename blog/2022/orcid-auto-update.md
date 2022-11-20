---
tags: scholarship, doi, orcid
category: til
date: "2022-11-19"
---

# Automatically updating my publications page with ORCID

For a while I've had a hand-crafted `.bibtex` file stored locally for [my `publications/` page](../../publications.md).
However, manually updating local text file is a pain to remember, especially since there are many services out there that automatically track new publications.

Here's the workflow I'd prefer:

- Treat one online service provider as a **Single Source of Truth** for my publications list.
- Use an API to programmatically ask this provider for the _latest_ data about my publications.
- Reshape that data into a form that I can insert into my website.

Fortunately, [ORCID is a service for identifying scholars and their contributions](https://info.orcid.org/what-is-orcid/).
It links various kinds of publications and activities to a unique account for each person.
It doesn't cover _all_ kinds of outputs (like talks, posters, etc), but it seems to cover the most important ones.

👉 Here is my ORCID ID and page: [`https://orcid.org/0000-0002-2391-0678`](https://orcid.org/0000-0002-2391-0678).

ORCID has [a public-facing API](https://info.orcid.org/documentation/features/public-api/) that allows you to automatically query information about an ORCID ID.
Following [an example notebook shared from the TAPIR project](https://github.com/Project-TAPIR/pidgraph-notebooks/blob/main/person-works/orcid_get_works_by_person.ipynb), I wrote a little script that runs each time my Sphinx site is built.
It generates a markdown snippet that is then inserted into my `publications.md` page.

````{dropdown} Python snippet to download ORCID data
_Note that the below is [a `jupytext` document](https://jupytext.readthedocs.io/en/latest/install.html) which is why there's extra metadata at the top_.

```{literalinclude} ../../scripts/orcid-publications.py
:language: python
```
````

In the future I'd like this to pull out even more data from my ORCID record, like lists of authors, grants, affiliations, etc.
However this seems like a good start and most importantly, it means I can delete my `.bibtex` file!
