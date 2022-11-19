# Chris' personal website

This is my personal website, built with Sphinx!

## Build and preview the docs

**Build the docs**. Use `nox`, which handles all of the environment generation automatically.
To do so, follow these steps:

1. Install `nox`.

   ```shell
   pip install -U nox
   ```
2. Run `tox`

   ```shell
   nox -s docs
   ```

this should install a Sphinx environment and build the site, putting the output files in `_build/html`.

## Execute and interact with the code

**Run a live webserver**:

```shell
nox -s docs -- live
```

**Run a JupyterLab environment with necessary packages installed:

```shell
nox -s lab
```

## Update my publications

The script in `scripts/orcid-publications.py` will use [the ORCID APi](https://info.orcid.org/documentation/api-tutorials/api-tutorial-read-data-on-a-record/) to download all of the records associated with my ORCID account.

It generates some markdown that is then inserted into my documentation in `publications.md`.
