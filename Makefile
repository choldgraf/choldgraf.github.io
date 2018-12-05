BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
ARTICLESDIR=$(INPUTDIR)/articles
OUTPUTDIR=$(BASEDIR)/output
INTERACTCOPY=$(HOME)/Dropbox/github/publicRepos/jupyterblog/create_interactive_notebooks.py
PATHCV=$(HOME)/Dropbox/docs/cv_and_resume/Chris_Holdgraf_CV_science.pdf
GITHUB_PAGES_BRANCH=gh-pages

install:
	gem install bundler
	bundle install

posts:
	python ./scripts/notebooks_to_markdown.py

serve: posts
	bundle exec guard

publish: posts
	bundle exec jekyll build
	ghp-import -n -c predictablynoisy.com -m "jekyll auto update" -p -f -b master _site
	git add content scripts _posts
	git commit -m "publishing posts"
	git push

clean:
	[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)

.PHONY: posts serve clean
