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

# My ORCID
orcid_id="0000-0002-2391-0678"
ORCID_RECORD_API = "https://pub.orcid.org/v3.0/"

# Download all of my ORCID records
print("Retrieving ORCID entries from API...")
response = requests.get(url=requests.utils.requote_uri(ORCID_RECORD_API + orcid_id),
                      headers={'Accept': 'application/json'})
response.raise_for_status()
orcid_record = response.json()

# +
# Just to visualize in a notebook if need be
# JSON(orcid_record)
# -

# Extract metadata for each entry
df = []
for iwork in orcid_record["activities-summary"]["works"]["group"]:
    isummary = iwork["work-summary"][0]
    title = isummary["title"]["title"]["value"]
    if isummary["type"] in ["preprint", "other"]:
        journal = isummary["type"]
    else:
        journal = isummary["journal-title"]["value"]
    created_year = isummary["publication-date"]["year"]["value"]
    doi = isummary["external-ids"]["external-id"][0]["external-id-value"]
    url = f"https://doi.org/{doi}"
    df.append({
        "url": url,
        "year": created_year,
        "doi": doi,
        "url": url,
        "journal": journal,
        "title": title,
    })
df = pd.DataFrame(df)

# +
# Print the markdown that I'll use in my site
md = []
for year, items in df.groupby("year", sort=False):
    md.append(f"## {year}")
    for _, item in items.iterrows():
        mditem = f"**{item['title']}**. _{item['journal']}_. [{item['doi']}]({item['url']})"
        md.append(mditem)
        md.append("")
    md.append("")

# This will only work if this is run as a script
mds = "\n".join(md)
path_out = Path(__file__).parent.parent / "_static/publications.txt"
path_out.write_text(mds)
print(f"Finished updating ORCID entries at: {path_out}")