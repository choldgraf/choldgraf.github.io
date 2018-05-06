BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
ARTICLESDIR=$(INPUTDIR)/articles
OUTPUTDIR=$(BASEDIR)/output
INTERACTCOPY=$(HOME)/Dropbox/github/publicRepos/jupyterblog/create_interactive_notebooks.py
PATHCV=$(HOME)/Dropbox/docs/cv_and_resume/Chris_Holdgraf_CV_science.pdf
GITHUB_PAGES_BRANCH=gh-pages

notebooks:
	python ../src/notebooks_to_markdown.py
	python $(INTERACTCOPY) $(ARTICLESDIR)/*/*/*.ipynb $(INPUTDIR)/notebooks --update-path $(INPUTDIR)
	cp $(PATHCV) content/extras/cv.pdf

blog: notebooks
	jekyll build

clean:
	[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)

github: blog
	ghp-import -m "Generate jekyll site" -b $(GITHUB_PAGES_BRANCH) $(OUTPUTDIR)
	git push origin $(GITHUB_PAGES_BRANCH)

.PHONY: blog clean github
