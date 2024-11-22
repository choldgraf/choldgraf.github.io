import nox
from shlex import split
from os.path import realpath

nox.options.reuse_existing_virtualenvs = True
nox.options.default_venv_backend = "uv"

@nox.session
def start(session):
    for ii in ["requirements.txt", "execute-requirements.txt"]:
        session.run("uv", "pip", "install", "-U", "-r", ii, silent=True)
    session.run(*"myst start".split(), *session.posargs)

@nox.session
def test(session):
    for ii in ["requirements.txt", "execute-requirements.txt"]:
        session.run("uv", "pip", "install", "-U", "-r", ii, silent=True)
    session.run("python", "src/blogpost.py") 

@nox.session
def lab(session):
    for ii in ["requirements.txt", "execute-requirements.txt"]:
        session.run("uv", "pip", "install", "-U", "-r", ii, silent=True)
    session.run(*split("jupyter lab ."))
