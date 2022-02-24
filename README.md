# Chris' personal website

This is my personal website, built with Sphinx!

The easiest way to build the website is to use `nox`, which handles all of the environment generation automatically.
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

To run a live webserver that will auto-build and reload when you make changes, run:

```shell
nox -s docs-live
```

## 2 test

Test

## v2 test

Test 2 
