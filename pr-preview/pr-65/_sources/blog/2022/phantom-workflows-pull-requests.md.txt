---
tags: cicd, "github actions"
date: "2022-11-27"
category: "til"
---

# Fix phantom GitHub workflows in your ci-cd with protected branch rules

Have you ever had a GitHub pull request show "phantom" workflows that never pass?
This looks like one or more workflows that are in a constant **waiting state**, with a yellow status indicator, and that never complete.

It looks something like this:

```{image} https://user-images.githubusercontent.com/1839645/204134864-da2541f0-ff4f-4d9f-8c80-aa8c4437d8a0.png
```

If you run into this, it may be because of [branch protection rules](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/defining-the-mergeability-of-pull-requests/about-protected-branches) in their repository.
These allow you to ensure that certain conditions are met before a pull request can be merged.

In particular, a common step is to **ensure that a certain GitHub Workflow passes before you can merge**.
This is often the source of the phantom workflows that never complete.
This is configured via `settings` -> `branches` -> `branch protection rules`, like so:

```{image} https://user-images.githubusercontent.com/1839645/204134952-fb5b8aa5-f8bb-4bd9-92ec-c66bf653387a.png
```

If you **specify a test here, and then delete it in your `YAML` configuration file, this will cause phantom workflows in your Pull Requests**.
GitHub will wait for the test to finish, because it is specified in your repository settings, but it will never finish because the test isn't configured in your workflow configuration.

So, to fix it, you simply **delete the entry in your protected branch rules associated with that test**.
As a result, GitHub will no longer wait for that test to complete, and you can merge away.

This one has bitten me several times, and so I decided to just document it here for future reference.
[Jacob Tomlinson](https://jacobtomlinson.dev/) was the one that first told me about this fix!
