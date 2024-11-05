# ---
# jupyter:
#   jupytext:
#     formats: py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
import pandas as pd
import requests
from IPython.display import Markdown, JSON
from pathlib import Path
from rich import progress

# My ORCID
orcid_id = "0000-0002-2391-0678"
ORCID_RECORD_API = "https://pub.orcid.org/v3.0/"

# Download all of my ORCID records
print("Retrieving ORCID entries from API...")
response = requests.get(
    url=requests.utils.requote_uri(ORCID_RECORD_API + orcid_id),
    headers={"Accept": "application/json"},
)
response.raise_for_status()
orcid_record = response.json()

# +
# Just to visualize in a notebook if need be
# JSON(orcid_record)

# +

###
# Resolve my DOIs from ORCID as references
# Shamelessly copied from:
# https://gist.github.com/brews/8d3b3ede15d120a86a6bd6fc43859c5e
import requests
import json


def fetchmeta(doi, fmt="reference", **kwargs):
    """Fetch metadata for a given DOI.

    Parameters
    ----------
    doi : str
    fmt : str, optional
        Desired metadata format. Can be 'dict' or 'bibtex'.
        Default is 'dict'.
    **kwargs :
        Additional keyword arguments are passed to `json.loads()` if `fmt`
        is 'dict' and you're a big JSON nerd.

    Returns
    -------
    out : str or dict or None
        `None` is returned if the server gives unhappy response. Usually
        this means the DOI is bad.

    Examples
    --------
    >>> fetchmeta('10.1016/j.dendro.2018.02.005')
    >>> fetchmeta('10.1016/j.dendro.2018.02.005', 'bibtex')

    References
    ----------
    https://www.doi.org/hb.html
    """
    # Parse args and setup the server response we want.
    accept_type = "application/"
    if fmt == "dict":
        accept_type += "citeproc+json"
    elif fmt == "bibtex":
        accept_type += "x-bibtex"
    elif fmt == "reference":
        accept_type = "text/x-bibliography; style=apa"
    else:
        raise ValueError(f"Unrecognized `fmt`: {fmt}")

    # Request data from server.
    url = "https://dx.doi.org/" + str(doi)
    header = {"accept": accept_type}
    r = requests.get(url, headers=header)

    # Format metadata if server response is good.
    out = None
    if r.status_code == 200:
        if fmt == "dict":
            out = json.loads(r.text, **kwargs)
        else:
            out = r.text
    return out


# -

# Extract metadata for each entry
df = []
for iwork in progress.track(
    orcid_record["activities-summary"]["works"]["group"], "Fetching reference data..."
):
    isummary = iwork["work-summary"][0]

    # Extract the DOI
    for ii in isummary["external-ids"]["external-id"]:
        if ii["external-id-type"] == "doi":
            year = isummary["publication-date"]["year"]["value"]
            doi = ii["external-id-value"]
            break
    df.append({"year": year, "doi": doi})
df = pd.DataFrame(df)

# Convert into a markdown string
md = ["|Year|Publications|", "|===|===|"]
for year, items in df.groupby("year", sort=False):
    this_pubs = []
    for _, item in items.iterrows():
        this_pubs.append(f'{{cite}}`{item["doi"]}`')
    md.append(f"|{year}|{', '.join(this_pubs)}|")
mds = "\n".join(md)

# +
# Uncomment to preview in a notebook
# Markdown(mds)
# -

# This will only work if this is run as a script
path_out = Path(__file__).parent.parent / "_static/publications.txt"
path_out.write_text(mds)
print(f"Finished updating ORCID entries at: {path_out}")
