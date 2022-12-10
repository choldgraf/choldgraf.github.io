---
# date: "2022-12-07"
category: thoughts
---

# Pyodide needs to avoid the uncanny UX valley

[The uncanny valley of voice recognition](https://zachholman.com/posts/uncanny-valley/).

Basically the point here is that the pyodide workflow is really powerful, but it runs the risk of having too many unexpected papercuts to be useful.

In voice recognition, there's the idea that you can't have something that works 95% of the time, it really needs to work 99.999% of the time.
If it only works 95%, then it's cool but not reliable enough to be really useful.

I wonder if pyodide faces the same challenge.
It has an initial "wow" factor, but if you routinely (maybe once a week? month?) hit a road block that doesn't let you do a basic thing, it won't be perceived as reliable.

Think of a classroom that might use pyodide instead of a Python server.
If there's an important topic you want to cover that you _can't_ cover with pyodide, you can't easily ask students to run their own python servers for just one week.
This might prevent broader adoption.

Note that documentation and guides to using pyodide for teaching could be a helpful bridge for this.