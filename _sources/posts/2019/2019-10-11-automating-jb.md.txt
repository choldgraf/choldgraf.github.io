---
tags: infrastructure
date: 2019-10-11
redirect: automating-jb
---

# Automating Jupyter Book deployments with CI/CD

Lately I've spent a lot of time trying to reduce the friction involved
in deploying Jupyter Book as well as contributing to the project.
Features are a great carrot, but ultimately getting engagement is also
about lowering barriers to entry and showing people a path forward.
Jupyter Book is a relatively straightforward project, but it involves
a few technical pieces that can be painful to use (thanks Jekyll).

Recently I experimented with whether we can **automate deploying a Jupyter Book online**.
Using continuous integration / deployment services seems like a natural place
to try this out. One can upload a barebones set of code to a GitHub repository,
then configure a build system to create a book and deploy it online from there.
This blog post is a place to keep track of the current state of affairs for this workflow.

![auto build logos](/images/2019/jb-auto-build.png)

**I'll publish the latest configuration files for this at [this repository](https://github.com/choldgraf/jupyter-book-deploy-demo/)**.

## The general set of steps involved

We'll start with the simplest possible Jupyter Book configuration:
to have a single folder with a collection of content inside. The folder looks
like this:

```bash
.
├── content
│   ├── 01
|   │   ├──── notebook1.ipynb
│   │   └──── notebook2.ipynb
│   ├── 02
|   │   ├──── notebook3.ipynb
│   │   └──── mdfile4.md
...
|
└── configuration_files_for_cicd/
```

There's no table of contents, and no configuration file (though we could add
these if we wish). If Jupyter Book is used to create a new book with some
content, but no TOC is given, it'll automatically generate one.

Our goal is to do the following in an automated fashion:

1. Build a new Jupyter Book template from this content folder (with `jupyter-book create`)
2. Build page HTML for the book (with `jupyter-book build`)
3. Generate the book's site with Jekyll (with `bundle exec jekyll build`)
4. Host the results somewhere online

Below are attempts to do this with CI/CD. I'll update this post
as new options become available (and hopefully push some stuff to
the Jupyter Book documentation).

## Netlify

By far the easiest way to accomplish the above is with the online
website provider [Netlify](https://www.netlify.com). This was my
first experience with the Netlify service, and I must say that I was
really pleased (thanks to [Elizabeth DuPre](https://github.com/emdupre)
for the recommendation and [Netlify tutorial](https://jupyterbook.org/guide/publish/netlify.html)).

Netlify has automatic deployment built into its service, since that's
the whole point of the site - to deploy websites from online repositories.
To do this, I simply had to connect Netlify to my [book content repository](https://github.com/choldgraf/jupyter-book-deploy-demo/)
and tell it to start building a site from that repository's contents.

I modified the build instructions using a custom "build" command.
Netlify runs this command every time it tries to build your site.
You can configure this by creating a `netlify.toml` file and putting it
in the root of your repository. [Here's a link to my configuration file](https://github.com/choldgraf/jupyter-book-deploy-demo/blob/master/netlify.toml).

The full text of that TOML file looks like this:

```toml
[build]
  command = """
    gem install bundler -v '2.0.2'
    pip install -U git+https://github.com/jupyter/jupyter-book
    jupyter-book create mybook --content-folder content
    cd mybook
    jupyter-book build ./ --overwrite
    make install
    bundle exec jekyll build
    """

  publish = "mybook/_site"
```

There are two pieces to this: the `command` section is the command to
run first, when a new commit is pushed to a branch. The `publish` section
defines the location where Netlify will look for the finished HTML (AKA, my book website).

Note that in the `jupyter-book create` command above, I used `--content-folder` to
tell Jupyter Book to use some pre-existing content when it generated my book template.
In addition, note that I could immediately install both Python and Ruby packages - that's
because Netlify's base build environment has both languages installed already!

<!-- #region {"tags": ["popout"]} -->
One gotcha on getting Netlify to work was configuring it to use a Python 3.X environment.
That's accomplished with the `runtime.txt` file [at this location](https://github.com/choldgraf/jupyter-book-deploy-demo/blob/master/runtime.txt).
<!-- #endregion -->

By adding this configuration to my site, Netlify immediately started building
and hosting the book. You can find [that book deployment here](https://jupyter-book-deploy-demo.netlify.com).

## CircleCI

[CircleCI](https://circleci.com) is a website most-commonly used for running
test suites and deploying things into production once those tests pass.
Fortunately, deploying an HTML book is pretty similar!

Getting Jupyter Book to build on CircleCI was a little bit trickier for two
reasons:

1. CircleCI has more specific environments in its build system. You can have a Python
   environment, or a Ruby environment, but not both.
2. CircleCI has no concept of natively "hosting" HTML content, so we had to piggy-back
   on top of GitHub pages.

Luckily, working around both of these issues was relatively straightforward.
You can find the CircleCI configuration that ended up working [in the github repository](https://github.com/choldgraf/jupyter-book-deploy-demo/blob/master/.circleci/config.yml).

There were two gotchas in there:

1. I started off with using a Ruby environment rather than a Python environment.
   That's becuase I've found Python to be much easier to install than Ruby. In fact,
   installing python was as easy as including `sudo apt-get install python3-pip` in
   my commands.
2. I had to use a GitHub SSH deploy key to be able to deploy my built HTML to GitHub
   pages. You can find [instructions for how to do so in this post](https://predictablynoisy.com/circleci-mirror).

Once that was accomplished, this is the configuration that got the job done:

```yaml
version: 2.1
jobs:
  build_book:
    docker:
      - image: circleci/ruby:2.6
    steps:
      - checkout
      - run:
          name: Install Python and dependencies to build page HTML
          command: |
            sudo apt-get install python3-pip
            pip3 install --user -r requirements.txt
            pip3 install --user -U git+https://github.com/jupyter/jupyter-book.git

      - run:
          name: Create book template and build page HTML
          command: |
            jupyter-book create mybook --content-folder content/
            jupyter-book build ./mybook

      - run:
          name: Install ruby dependencies and build the book's website
          command: |
            cd mybook
            make install
            bundle exec jekyll build

      # If we're on master, push to a gh-pages branch
      - add_ssh_keys:
          fingerprints:
            - "<my-public-fingerprint>"
      - run:
          name: Push to gh-pages (if on master)
          command: |
            if [ $CIRCLE_BRANCH	== "master" ]; then
              pip3 install ghp-import
              ghp-import -n -f -p mybook/_site;
            else
              echo "Skipping deploy because we aren't on master"
            fi


workflows:
  version: 2
  default:
    jobs:
      - build_book
```

You can find the deployed site [at this location](https://github.com/choldgraf/jupyter-book-deploy-demo).

## Wrapping up

Ultimately, it was simpler than I expected to deploy a Jupyter Book with CI/CD.
There are lots of other services to explore (in particular, TravisCI and GitHub actions),
but I find it hard to believe anything would be more straightforward than Netlify.

That said, the process also made it clear that some pieces of the Jupyter Book API
are a bit confusing. It felt natural to have my content in a single folder, and to
build a book from that content, but this isn't the "default" way that the documentation
recommends. I'll let these ideas simmer a little bit and we'll see what comes out of it.
