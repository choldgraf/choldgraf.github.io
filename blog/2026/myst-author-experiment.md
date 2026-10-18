---
title: Building a MyST authoring environment to find things that MyST core could improve
date: "2026-10-25"
tags:
  - myst
  - jupyter
---

Something that has bugged me for a long time is that [MyST](https://mystmd.org) doesn't have a lot of support for *authors* to write MyST documents more effectively.
MyST documents have a ton of rich metadata inside them, but it has mostly been used for making the *reader* experience more interesting, rather than the *author* experience.

For MyST to become a bigger part of the research or education workflow, I think it needs to have a cleaner author UX - at least, for some of the minimal features that writing in other languages often has.
Over the last few months I've been playing around with various ways to do this, and this is a blog post to share what I've built and learned.

**tl;dr**: I've built a few new tools in the MyST ecosystem in order to improve the authoring experience and drive the creation of a few building blocks and improvements in core MyST along the way! Here are the main things I worked on:

- An "opinionated end-user interface for authoring MyST documents" (`myst-author`).
- A bunch of "building blocks" that should be more generally useful to the community (`mystmd-lsp`, `myst-syntax`, `mystmd-client`, `myst-parser-unified`).
- [A list of upstream improvements](#upstream-improvements) that we can make in MyST that would let us remove some complexity and hacks from these tools.

Here's a list of the tools I built along the way:

:::{listing}
:source: yaml
:display: table
:columns: title,description
- title: myst-author
  url: https://chrisholdgraf.com/myst-author/
  description: An opinionated, Obsidian-style editing interface for MyST built on CodeMirror 6 (used as a web editor, or as a JupyterLab or VS Code extension).
- title: mystmd-lsp
  url: https://chrisholdgraf.com/mystmd-lsp/
  description: A language server protocol (LSP) implementation for MyST that uses the mystmd server to expose labels, references, etc. in addition to basic syntax.
- title: mystmd-client
  url: https://chrisholdgraf.com/mystmd-client/
  description: A small helper library to manage the lifecycle of a mystmd process (used by the LSP and myst-author, I hope this can be deleted once some upstream improvements are made!)
- title: myst-syntax
  url: https://chrisholdgraf.com/myst-syntax/
  description: A syntax grammar that can be re-used for highlighting across code editors.
- title: myst-parser-unified
  url: https://chrisholdgraf.com/myst-parser-unified/
  description: A remark-based parser for MyST - this is a proof of concept to understand the extra ground we'd have to cover to bring this into core.
:::

`myst-author` is the editor, and it uses `myst-syntax` for highlighting and `mystmd-lsp` for autocomplete.
Both `myst-author` and `mystmd-lsp` use `mystmd-client` to run `mystmd` in the background.
`myst-parser-unified` is a standalone experiment that isn't used in the stack above, but addresses some problems I kept running into (especially with the LSP).

## Building an end-user product to figure out what building blocks needed to exist first

Building opinionated end-user tools can be a useful way to uncover the underlying APIs and logic improvements that need to be made in *core* technologies in order to *enable* the end-user thing you're trying to build.
This is particularly interesting with LLMs, because they will often still build the thing you ask for even though it is not possible to do so the "right" way.
The result tends to be spaghetti code that hacks around the limitations of the core library, but this is a useful signal for a place to make improvements!

So, I followed a development process that looked roughly like this[^wf]:

- Build an opinionated end-user MyST authoring environment (I called it `myst-author`).
- Have this tool lean on core MyST tools (i.e., in `mystmd`) for as much as possible, and only build new things when they didn't exist.
- Look at what was built, and identify all the new technologies that had to be created along the way, because they didn't exist in `mystmd`.
- Identify the ones that feel genuinely useful on their own, and factor them out into their own repository.
- Treat them as an "upstream tool" and re-build the `myst-author` tool on this new repository.

[^wf]: I used Claude heavily in this loop, because there's no way I'd be able to iterate on MVPs without it. I don't consider this code to be "production ready", though some of it might be useful! I've licensed it all `CC0` in case anybody wants to make use of the code however they like.

## `myst-author`: An opinionated interactive authoring interface for MyST documents

The main tool that I built is called [`myst-author`](https://chrisholdgraf.com/myst-author/).

```{figure} https://raw.githubusercontent.com/choldgraf/myst-author/main/docs/images/myst-author.gif
:alt: Animated demo of myst-author switching a rendered block to its MyST source and back.

Clicking a rendered block in `myst-author` shows its MyST source, typing edits it, and clicking away renders it again.
```

I've been using [Obsidian](https://obsidian.md) a lot lately, and find that it's a great hybrid between WYSIWYG and source code writing.
It means I can use diffing and merging tools more easily when writing MyST documents, but I still get the interactivity and immediate feedback from rendering things straight away.

`myst-author` comes with VS Code and JupyterLab extensions, and you can try it out on Binder or Codespaces here:

[![Launch on Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/choldgraf/myst-author/main?urlpath=lab/tree/docs/examples/tour/index.md)
[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/choldgraf/myst-author)

It does some interesting hacky things to get around the fact that [the mystmd engine doesn't easily run on JupyterHub or Binder](#issue:jupyterhub).
Rather than running the MyST theme server, it starts `mystmd` in headless mode (which builds and serves your content without the website theme).
It then renders the AST in the browser with [the MyST react components](#issue:theme-embed).
This means that we can do all the necessary re-writing of assets, etc. at render-time, so it will work even if you're not being served from the URL root.

It uses [CodeMirror 6](https://codemirror.net) for the editing and rendering window, which means that it can be run in a bunch of different places, or potentially as part of a bigger editing application etc.
This made it a little bit more complicated for things like VS Code, but felt like a good tradeoff for the generalizability.

**What I'd like to do with this repository:** Who knows!
I'm going to keep using it myself and seeing how I can make it more useful.
It feels too opinionated to be in the core MyST organization, but maybe it could live as a standalone editor in [myst-contrib](https://github.com/myst-contrib)?
Or maybe it's best to continue existing as a driving proof of concept for more development.
I still haven't decided.

## `mystmd-lsp`: A language server protocol implementation that uses mystmd

I wanted interactive auto-complete and drop-down hints for myst-author, but I also wanted to go beyond just "give me the basic directive syntax".
I knew that `mystmd` has a ton of information about the objects in a MyST project contained inside it, so this tool is meant to use all of that information.

`mystmd-lsp` spawns its own `mystmd` process in the background.
It builds the project for whatever folder you're in, and then exposes that project's labels, references, etc. for an editor to use via the [Language Server Protocol](https://microsoft.github.io/language-server-protocol/).

This means that you can type MyST short-hand for references like `@` or `[](#` and `mystmd-lsp` will show you a list of all the labels that you can reference in the current MyST project (it even includes external references too!).

```{figure} https://raw.githubusercontent.com/choldgraf/mystmd-lsp/main/docs/images/mystmd-lsp.gif
:alt: Animated demo of mystmd-lsp autocompleting a reference and a citation in VS Code.

`mystmd-lsp` in VS Code: autocompleting a `{numref}` reference and a citation, then hovering the reference.
```

I needed a way for my LSP server, and for `myst-author`, to control the lifecycle of `mystmd`.
However, `mystmd` [doesn't expose the right APIs to do this naturally](#issue:mystmd-client).
It's built as a CLI, so there's no lightweight exported way to launch `myst start --headless`, talk to its content server, or parse a single page with the same settings that `myst build` uses.
So [`mystmd-client`](https://chrisholdgraf.com/mystmd-client/) is just a little helper that holds the logic for controlling start/stop/etc of the myst server so I can re-use it in a few places.

**What I'd like to do with this repository:** This feels like a good candidate for being in the core myst engine, since it's best to have a source of truth for this kind of thing.
`mystmd-client` feels like it should just be an upstream improvement in the MyST engine.

## `myst-syntax`: A grammar for MyST syntax highlighting

I realized that the core "grammar rules" for things like syntax highlighting were more generically useful, so that got its own repository as well!
These are essentially a bunch of `regex` style patterns that tell an editor how to chunk up the symbols on the screen (e.g. `:::{note}`) into discrete units and color them appropriately.
This is generic stuff that can be re-used across many kinds of editors, and doesn't depend on a "server" to understand.

**What I'd like to do with this repository:** Same as `mystmd-lsp`, this feels like a good candidate for being in the core myst engine.

## `myst-parser-unified`: A native unifiedjs parser for MyST syntax

I kept hitting challenges associated with MyST's current markdown parser: [`markdown-it`](https://github.com/markdown-it/markdown-it).
Right now, `mystmd` parses each document with `markdown-it`, then *converts* the document to a unifiedjs-style AST.
`markdown-it` [doesn't give you column information](#issue:columns) as it is parsing, only line information.
This is a big problem for things like an LSP, which needs to know where in the line you're typing so that it knows what to autocomplete!

[UnifiedJS](https://unifiedjs.com) has its own native parser ecosystem, built on a tool called [`remark`](https://github.com/remarkjs/remark).
In principle it should be simpler to just parse MyST markdown directly with `remark`, rather than to use `markdown-it` and then convert it over to `remark` AST.
So [this tool](https://chrisholdgraf.com/myst-parser-unified/) is an experiment at making that happen.
It's not actually used in the stack above, mostly because I wanted to keep them dependent on `mystmd` and not totally side-step the core engine.
But it seems doable to move this into the core MyST engine at some point.

At a first pass, I ran the parser against the examples in the MyST conformance tests in [myst-spec](https://github.com/jupyter-book/mystmd/tree/main/packages/myst-spec).
Because these tests have some carry-over from `markdown-it` in them, it was hard to know whether some tests were failing for the wrong reasons (`mystmd`'s own parser only matches 53 of the 90 MyST examples!).
So instead of using the tests' expected output, I compared against the tree that `mystmd`'s own parser builds for each example.
I also built a little "converter" to transform the remark AST into the idiosyncratic AST that `mystmd` produces (we should really fix that!).
This drove a few useful cycles of iteration to get the parsing to behave properly.
I split this up into commonmark tests vs. MyST Markdown tests to get a better feel for this.

Here's where things stood in October 2026 (the [parser docs](https://chrisholdgraf.com/myst-parser-unified/#score-per-file) have the latest numbers):

| Examples matching `mystmd`'s parser | MyST (of 90) | CommonMark (of 651) |
| --- | --- | --- |
| Raw parser output | 65 | 398 |
| After converting to `mystmd`'s AST | 83 | 625 |

The remaining MyST failures aren't about parsing MyST syntax.
They're about two features `markdown-it` adds on top of parsing: "smart quotes" (turning `"` into curly quotes) and "linkify" (turning bare URLs like `www.example.com` into links).
The unified ecosystem has its own plugins for both, but with slightly different rules.
So if we switch, we'll need to choose whether to port `markdown-it`'s exact rules so nobody's output changes, or use the unified plugins and accept small differences in some documents.

It wasn't too much work to get here, so I'm hopeful that with some more thoughtful iteration we could get the parser to a place where we can just drop it into the myst engine.
That said, there might be some trade-offs in that decision e.g., the unified parser is about 2x slower.
In practice that's ~0.4 ms vs. ~0.2 ms for a typical page, or ~1 s vs. ~0.5 s across ~600 real-world MyST files.
That's small next to the rest of a build, but still worth discussing.

**What I'd like to do with this repository:** I'd also love for this to serve as inspiration for an upstream contribution into the MyST engine itself!
We've been talking about [a unified-native parser](#issue:columns) for a long time, and if we improved our conformance tests I don't think that it should be too difficult.
[The conformance tests themselves haven't been updated in a while!](#issue:conformance-tests)
They are missing some core syntax features that have been added over the past year or two, and need a few more tests to make it easier for others to write their own parsers etc.

(upstream-improvements)=
## Where we could improve things

Here are the upstream improvements that would let us remove some complexity and hacks from these tools.

**`mystmd`**

- (issue:jupyterhub)=
  If `myst start` could [run on JupyterHub](https://github.com/jupyter-book/mystmd/issues/302) and [serve a live preview from a sub-path](https://github.com/jupyter-book/mystmd/issues/3012), `myst-author` could drop its custom rendering logic.
- (issue:mystmd-client)=
  `mystmd` [doesn't export helpers for tools that run it](https://github.com/jupyter-book/mystmd/issues/3095), which is why `mystmd-client` exists.
  It also works around [`myst start` only listening on IPv6 `localhost`](https://github.com/jupyter-book/mystmd/issues/2471), which breaks tools that connect to `127.0.0.1`.
- (issue:config-files)=
  `config.json` [doesn't include each page's file](https://github.com/jupyter-book/mystmd/issues/3093), so tools fetch every page's JSON to build a table of contents.
- (issue:xref)=
  `myst.xref.json` [doesn't include each label's `title` or `enumerator`](https://github.com/jupyter-book/mystmd/issues/3098), and `myst start` [doesn't update it when a page changes](https://github.com/jupyter-book/mystmd/issues/3097).
  So the LSP re-reads every page's JSON after each rebuild instead, which is pretty inefficient!
- (issue:warnings)=
  `myst start` only sends "reload" messages over its websocket, [not structured warnings](https://github.com/jupyter-book/mystmd/issues/3096), so editors can't show build warnings at the right file and line.
- (issue:directive-positions)=
  [Nodes created by directives have no position](https://github.com/jupyter-book/mystmd/issues/3094) in `mystmd`'s output, so "go to definition" for a figure lands on its caption instead of the directive.
- (issue:columns)=
  [Column-accurate positions in the parser](https://github.com/jupyter-book/mystmd/issues/2864) (e.g. via remark) would let us delete the regexes that the LSP uses to find references.
  We should decide whether we want this enough to justify [switching parsers to something like remark](https://github.com/jupyter-book/mystmd/issues/1705).
- (issue:conformance-tests)=
  [Update the MyST conformance tests](https://github.com/jupyter-book/mystmd/issues/3078) so that they describe intended MyST behavior (and not `markdown-it`'s quirks) and also cover the syntax we've added in the last couple of years.

**`myst-theme`**

- (issue:theme-embed)=
  The MyST theme's preview is [hard to embed elsewhere](https://github.com/jupyter-book/myst-theme/issues/986) (e.g., you need to know about some undocumented KaTeX CSS, and there's no pre-built CSS).

**Other projects**

- (issue:jupyterlab-lsp)=
  `jupyterlab-lsp` [doesn't send notebook Markdown cells to language servers](https://github.com/jupyter-lsp/jupyterlab-lsp/issues/1202), so `myst-author`'s JupyterLab extension carries its own LSP client just to be able to handle markdown.
- (issue:jupyterlab-codemirror)=
  JupyterLab doesn't have a [documented way to add CodeMirror extensions to a language that is already registered in JupyterLab](https://github.com/jupyterlab/jupyterlab/issues/20127), so the `myst-syntax` JupyterLab extension overwrites part of Lab's Markdown entry.
- (issue:inlay-hints)=
  CodeMirror's LSP client doesn't support [inlay hints](https://code.haverbeke.berlin/codemirror/dev/issues/1772), so `myst-author` adds its own inlay hints (the faint "Figure 1" after a reference).

## Overall what did I learn

This was a really interesting exercise! It uncovered a bunch of stuff that probably wouldn't have been discovered until somebody had tried to do something specific, and it also resulted in some hopefully useful technology. I tried to create issues for any of the clear stuff that was actionable, and will (hopefully) have time to work through those or work with others in the community that want to tackle them.
Here are a few things that stood out to me:

- It was surprisingly easy to get a pretty rich editor experience up and running with MyST.
- Having a high-quality source of truth makes this a million times easier.
  If the [MyST conformance tests](#issue:conformance-tests) were a bit better, I suspect somebody could do this in a half day of work pretty easily with an LLM.
- There are some core editing building blocks missing in MyST (like an LSP for the MyST engine), but these aren't terribly complex to build.
  I think the MyST team should just maintain some core pieces so that everybody doesn't need to write their own.
- Obsidian-style rendering feels like a nice mixture of "source" and "WYSIWYG" and I'm really enjoying writing with that workflow.
- The LSP is also super useful for MyST because of all the structured data that exists in a MyST document and project. You can do a lot of cool stuff when there is metadata and machine-readable structure! It makes me more confident in building on MyST as a core block for scientific communication.
