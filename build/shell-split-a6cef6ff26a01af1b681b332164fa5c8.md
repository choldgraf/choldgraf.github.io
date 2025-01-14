---
tags:
- shell
- python
date: "2022-11-29"
category: "til"
---

# `subprocess.run` can execute shell commands directly

I often run shell commands in Python via the [`subprocess.run` command](https://docs.python.org/3/library/subprocess.html#subprocess.run).
One thing that has always bugged me is that this required you to split commands into a list before it'd work properly.
For example, you'd have to do:

```python
import subprocess
import shlex

subprocess.run(*shlex.split("ls -l"))
```

Today I discovered that you don't have to do this!
There's a `shell=` keyword that can be used to tell subprocess to simply run the command directly in the shell.

For example:

```python
import subprocess
subprocess.run("ls -l", shell=True)
```

Apparently there are some [security considerations](https://docs.python.org/3/library/subprocess.html#security-considerations) but this seems like a big papercut saver to me.
