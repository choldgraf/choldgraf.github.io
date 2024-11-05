---
date: 2022-12-10
category: reports
tags:
- jupyter
- webassembly
---

# Report from the JupyterLite workshop: WebAssembly is pretty cool

I recently attended [the JupyterLite community workshop in Paris](https://blog.jupyter.org/community-workshop-jupyterlite-e992c61f5d7f?source=collection_home---6------6-----------------------), here are some quick thoughts from the three-day event[^ack].

[^ack]: Many thanks to the [QuantStack](http://quantstack.com/) team for organizing this event, and to [OVHCloud](https://www.ovhcloud.com/en/) for providing a physical space for everyone. 

For those without any background, JupyterLite is a distribution of Jupyter's user interfaces and a Python kernel that runs **entirely in the browser**.
Its goal is to provide a low-overhead and accessible way to use a Jupyter interface via the browser.
See [the `jupyterlite` documentation for more information](https://jupyterlite.readthedocs.io/).

## Capytale shows that WebAssembly and JupyterLite can boost accessibility to interactive computation

We had a demonstration of [the `capytale` platform](https://www.ac-paris.fr/capytale-un-service-web-pour-creer-et-partager-des-activites-pedagogiques-de-codage-121816), a project run by the French educational system to provide remote access to **fully in-browser learning environments**.

Capytale provides a number of learning modules.
Many of them are JavaScript-based, but they also needed to provide Python as well.
Initially, they tried to run a server that launched Python sessions for every person that used their service, but found this to be unscalable.[^fr]

[^fr]: As an aside, I am continually impressed with France's innovation around technology for teaching and learning. There seems to be a lot of experimentation and trying things out with open technology and services, and lots of clever ideas come out of this. It's exciting to see people experimenting in this way instead of using vendored SaaS products (though I'm sure there's plenty of that too).

Instead, the began to use [the notebook platform `basthon.fr`](https://basthon.fr/).
This re-uses the Classic Jupyter Notebook interface and connects to [a pyodide kernel](https://pyodide.org/).
This means that **all of the learner's work is done in their own browser**.

As a result, they are able to run **nearly 60,000 notebook sessions a week**, while running only a very lightweight server.
Because the computation is done purely in the browser, they only need to run a server for authentication and for sending files to the user sessions (files for learning modules are stored in a shared database that they manage).

This was a really inspiring example to me, because it's clear that for basic and introductory learning, WebAssembly can significantly reduce the barrier to learning and the overhead of managing shared infrastructure for learning.
I hope to see more experiments like this in the future, and would love to find ways that we can build WebAssembly workflows into JupyterHub and Binder.

## JupyterLite should fit on a USB stick for low-internet communities

One problem with the WebAssembly / JupyterLite approach is that it requires you to download a pretty big bundle the first time you access some content (something like `16mb` at the smallest).
This isn't too bad, but it's still pretty large if you live in a part of the world with really bad internet.

I had a quick chat with Jeremy about this, and we had an idea to _bundle JupyterLite in a USB stick_.
In many parts of the world, it might be less work to put JupyterLite on a USB and mail it to them than to ask them to download it themselves.
I [opened up an idea post in the community forum to share and discuss](https://discourse.jupyter.org/t/idea-jupyterlite-in-a-usb-stick/17177).

## WebAssembly and JupyterLite is coming to Jupyter Book

We made progress on a bunch of places where Jupyter Book can leverage the WebAssembly / JupyterLite ecosystem.
In particular, Steve has been doing [great work on `thebe-lite`](https://github.com/executablebooks/thebe/tree/feat/integrate-thebe-core), which will allow Thebe to launch interactive kernels via JupyterLite.
This means you'll be able to make code cells on a static webpage interactive **purely in the browser**.

I also re-discovered [the `jupyterlite-sphinx` extension](https://jupyterlite-sphinx.readthedocs.io/en/latest/), which (relatively) easily packages JupyterLite for sharing with a Sphinx site.

There are many things to improve here, but I think we're making good progress.

## WebAssembly still can't work for many workflows

One final thing that I noted is that WebAssembly still trips over itself in many somewhat common situations in computation.
I had a number of conversations with teachers that mentioned there are basic things you _want_ to teach, but cannot with pyodide.
For example, things like using the `input` or the `sleep` modules in Python, or downloading files from the web.

While I suspect that most teachers will be able to work around this, and that the pyodide ecosystem will continue to patch over these paper cuts, it seems like for the forseeable future, there will be a subset of use-cases where you simply need a live Python server.
I think our challenge as technologists will be to figure out the right User Experience around moving between an in-browser pyodide workflow, a cloud-based python server workflow, and a local installation workflow.
Learnings will need to use all of these approaches (particularly as they move beyond introductory courses), and we need to make sure that we have a similar set of technology and servies that can meet each need without requiring a whole new workflow.
