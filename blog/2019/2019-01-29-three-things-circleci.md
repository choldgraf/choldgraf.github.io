---
tags: CI, CD, continuous integration, dev ops, software development
redirect: three-things-circleci
category: coding
date: 2019-01-29
---

# Three things I love about CircleCI

I recently had to beef up the continuous deployment of Jupyter Book, and used
it as an opportunity to learn a bit more about CircleCI's features. It turns out,
they're pretty cool! Here are a few of the things that I learned this time around.

For those who aren't familiar with CircleCI, it is a service that runs Continuous
Integration and Continuous Deployment (CI/CD) workflows for projects. This basically
means that they manage many kinds of infrastructure that can launch jobs that run
test suites, deploy applications, and test on many different environments.

Here are some cool things that I now have a much better appreciation for:

## Re-run a job with SSH access

Often when tests don't pass or a build otherwise fails, it's really helpful to be
able to get into the machine itself and just start poking around. It turns out that
CircleCI makes this really easy! If a build has failed, then you can use the drop-down
menu next to the "Restart Job" button to select "Restart Job with SSH". The next time
the job fails (which it probably will, since you've just restarted a job that already
failed once), CircleCI will print the IP address and SSH command to connect to that
machine remotely.

## Persisting files between jobs with Workspaces

Everything CircleCI does is based around containers - each job has a Docker image
environment specified (and CircleCI curates a large list of containers for testing).
One challenge this introduces is that it can be more complex to use jobs that have
*multiple* languages or tools installed. You can always manually configure this, but
I've found that another easy solution is to split your task across multiple jobs,
and persist some of the files between them with CircleCI workspaces.

To set up a CircleCI workspace, you first need two jobs, then

```yaml
jobs:
  build_files:
    docker:
      # We use a Python image to test our files and run the test suite
      - image: circleci/python:3.6-stretch
    steps:
      # Some steps to build files we need in another job
      # Assume it places the built files into a folder called `_build/`
      - run: build_stuff_with_python

      # Persist the specified paths (see https://circleci.com/docs/2.0/workflows/#using-workspaces-to-share-data-among-jobs)
      - persist_to_workspace:
          # The root of the workspace, here just the CWD
          root: .
          # The sub-paths of the workspace to persist
          paths:
            - _build/

  deploy_files:
    docker:
      # We'll use a Ruby image to deploy our files
      - image: circleci/ruby:2.6
    steps:
      # Connect the files from the last job to this job
      - attach_workspace:
          # Must be absolute path or relative path from working_directory
          at: /tmp/workspace

      # Our final deployment steps
      - run: deploy_files_with_ruby
```

Finally, we'll set up a CircleCI workflow that runs the deployment job only after the
build job as finished, since the deploy job depends on files that are created by the
build job.

```yaml
workflows:
  version: 2
  default:
    jobs:
      - build_files
      #
      - deploy_files:
          requires:
            - build_files
```

In this way, we've split our task (build a bunch of files, then deploy them online)
into two different jobs. One that builds files with a Python container, and another that
deploys them with a Ruby container.

## Re-use code snippets with Commands

Finally, many times you'd like to re-use the same set of snippets across multiple
points of your CircleCI jobs. In 2.1, CircleCI added a new feature called Commands
that does this fairly simply. Commands are kind of like functions in that they
wrap up a collection of steps that can be re-used and parameterized. This means you
can define a "template" of a collection of steps, then fill-in missing fields in that
template in order to modify its behavior.

For example, here's a Command template to build a site with Jekyll:

```yaml
commands:
  build_site:
    description: "Build the site with Jekyll"
    parameters:
      # We'll define one parameter that lets us pass build arguments to Jekyll build
      build_args:
        type: string
        default: ""
    steps:
      - run:
          name: Build the website
          # Note the << parameters.param >> syntax that lets you define your own inputs
          command: bundle exec jekyll build << parameters.build_args >>
```

Now, we can re-use this command throughout our build steps. Here are two jobs that use
this command in different ways:

```yaml
jobs:
  # Build the site to store artifacts
  build_with_params:
    steps:
      # Build the site's HTML w/ the base_url for CircleCI artifacts
      - build_site:
          build_args: --baseurl /0/html/
  # Build the site to store artifacts
  build_without_params:
    steps:
      # Build the site's HTML w/ defaults for Jekyll
      - build_site:
          build_args: ""
```

Each of these jobs uses the command specified above in `build_site`, but
they use the `build_args` parameter to modify its behavior each time.
