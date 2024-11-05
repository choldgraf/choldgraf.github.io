import nox
from shlex import split
from os.path import realpath

nox.options.reuse_existing_virtualenvs = True


@nox.session
def start(session):
    session.install("-r", "requirements.txt")
    session.install("-r", "execute-requirements.txt")
    session.run(*"myst start".split())

@nox.session
def lab(session):
    session.install("-r", "requirements.txt")
    session.install("-r", "execute-requirements.txt")
    session.run(*split("jupyter lab ."))
