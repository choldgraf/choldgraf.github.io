---
tags: scholarship, doi, orcid
category: til
date: "2022-11-19"
---

# Automatically updating my publications page with ORCID

For a while I've had a hand-crafted `.bibtex` file stored locally for [my `publications/` page](../../publications.md).
However, manually updating local text file is a pain to remember, especially since there are many services out there that automatically track new publications.

:::{admonition} Update!
A [helpful suggestion on Twitter](https://twitter.com/temorrell/status/1594749942316208128) allowed me to include the full citation information, including lists of authors, using the doi.org API!
:::

Here's the workflow I'd prefer:

- Treat one online service provider as a **Single Source of Truth** for my publications list.
- Use an API to programmatically ask this provider for the _latest_ data about my publications.
- Reshape that data into a form that I can insert into my website.

Here's how I accomplished this:

## Use ORCID to grab a list of DOIs for my publications

[ORCID is a service for identifying scholars and their contributions](https://info.orcid.org/what-is-orcid/).
It links various kinds of publications and activities to a unique account for each person.
It doesn't cover _all_ kinds of outputs (like talks, posters, etc), but it seems to cover the most important ones.

👉 Here is my ORCID ID and page: [`https://orcid.org/0000-0002-2391-0678`](https://orcid.org/0000-0002-2391-0678).

ORCID has [a public-facing API](https://info.orcid.org/documentation/features/public-api/) that allows you to automatically query information about an ORCID ID.
Following [an example notebook shared from the TAPIR project](https://github.com/Project-TAPIR/pidgraph-notebooks/blob/main/person-works/orcid_get_works_by_person.ipynb).

## Use the doi.org API to grab citation information

While the ORCID API has a lot of useful information in it, there were some important pieces missing, like **co-author information**.
Fortunately, I learned [from a suggestion on Twitter](https://twitter.com/temorrell/status/1594749942316208128) that [doi.org](https://doi.org) is accessible via an API call!

You can ask `doi.org` for the reference, bibtex file, or a JSON structure of reference data by adding a header to a doi.org URL, like so:

```
curl -LH "Accept:text/x-bibliography; syle=apa" https://dx.doi.org/10.1371/journal.pcbi.1009651
```

This returns a fully-resolved reference like so:

```
DuPre, E., Holdgraf, C., Karakuzu, A., Tetrel, L., Bellec, P., Stikov, N., & Poline, J.-B. (2022). Beyond advertising: New infrastructures for publishing integrated research objects. PLOS Computational Biology, 18(1), e1009651. https://doi.org/10.1371/journal.pcbi.1009651
```

In Python, the same call looks like this:

```python
from requests import get
doi = "10.1371/journal.pcbi.1009651"
url = f"https://dx.doi.org/{doi}"
header = {'accept': "text/x-bibliography; style=apa"}
r = requests.get(url, headers=header)
print(r.content)
```

You can also use other kinds of header configuration, like:

```python
# A citeproc-styled JSON structure
header = {'accept': "citeproc+json"}
# A bibtex entry
header = {'accept': "bibtex"}
```

The citeproc JSON structure has a ton of information in it, including information about all of the co-authors (and an extra bonus - a link to their ORCID pages!).
This is all the information I needed for my website.

## A script to do this all at once

I wrote a little script that runs each time my Sphinx site is built.
It generates a markdown snippet that is then inserted into my `publications.md` page.

````{dropdown} Python snippet to download ORCID data
_Note that the below is [a `jupytext` document](https://jupytext.readthedocs.io/en/latest/install.html) which is why there's extra metadata at the top_.

```{literalinclude} ../../scripts/orcid-publications.py
:language: python
```
````
