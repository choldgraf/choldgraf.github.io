---
# date: "2022-12-07"
category: thoughts
---
# Issues should answer why what and how to do work

Issues are a place to discuss ideas for work before they actually happen. They are a way for team members to align themselves on an action and decide to move forward (or not). But what kind of information is actually useful for issues? What do you put in an issue conversation, vs. leave to a pull request? I think that there are three key things, most important first:

- **Why**: Why is this issue worth resolving in the first place? Whose problem is it solving? What key stakeholder would care about it, and why would it make their life better?
	- To define this, you must also define the key stakeholders that should care about this issue. In an open source project there almost always at least two: users and maintainers. The "Why" may be different for each, and their goals may be conflicting! But it's important to consider both explicitly.
- **What**: What are the actions that would resolve this issue? Is it a new feature, a change in process, a bug to spot-check? This should be relatively high-level like "We should add the ability to customize the icon people see."
- **How**: Once there's agreement about **why** this is a problem to solve, and **what** will solve it, you can begin describing **how** it might happen. This could involve design documents, implementation constraints, or pointers to a codebase where things could happen.

When people open Pull Requests, at least "Why" and "What" should have already been defined and agreed upon by key stakeholders in a project. That way the PR can focus on the "how" without getting bogged down in whether it was a problem worth solving in the first place.

## References

- Inspired by [[Jacob Tomlinson]]'s post here: https://jacobtomlinson.dev/posts/2022/the-secret-to-making-code-contributions-that-stand-the-test-of-time/
- especially:
  > I also find it helpful to think about the issue as the foundation that will eventually become the documentation and write it in a way that communicates to the community what my intentions are rather than communicating to a developer what my intentions are.