install:
	gem install bundler
	bundle install

posts:
	python ./scripts/build_html.py

serve: posts
	bundle exec jekyll serve

.PHONY: posts serve clean
