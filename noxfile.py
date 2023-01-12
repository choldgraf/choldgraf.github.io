import nox
from shlex import split
from pathlib import Path

nox.options.reuse_existing_virtualenvs = True


@nox.session
def docs(session):
    session.install("-r", "requirements.txt")
    session.install("-r", "execute-requirements.txt")
    if "live" in session.posargs:
        IGNORE_DIRS = ["_build/**/*"]
        IGNORE_DIRS = [f"--ignore {Path(ii).resolve()}" for ii in IGNORE_DIRS]
        ignore_str = " ".join(IGNORE_DIRS)
        session.run(
            *split(f"sphinx-autobuild -b dirhtml . _build/dirhtml {ignore_str}")
        )
    else:
        session.run(
            *"sphinx-build -nW --keep-going -b dirhtml . _build/dirhtml".split()
        )
        session.log("open ./_build/dirhtml}/index.html")


@nox.session
def lab(session):
    session.install("-r", "requirements.txt")
    session.install("-r", "execute-requirements.txt")
    session.run(*split("jupyter lab ."))
