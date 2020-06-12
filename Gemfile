source "https://rubygems.org"

# Hello! This is where you manage which Jekyll version is used to run.
# When you want to use a different version, change it below, save the
# file and run `bundle install`. Run Jekyll with `bundle exec`, like so:
#
#     bundle exec jekyll serve
#
# This will help ensure the proper Jekyll version is running.
# Happy Jekylling!

gem "github-pages", group: :jekyll_plugins
gem "jekyll-auto-image"
# If you want to use Jekyll native, uncomment the line below.
# To upgrade, run `bundle update`.

# gem "jekyll"

gem "wdm", "~> 0.1.0" if Gem.win_platform?

# If you have any plugins, put them here!
group :jekyll_plugins do
  # gem "jekyll-archives"
  gem "jekyll-feed"
  gem 'jekyll-sitemap'
  gem 'hawkins'
  # Blogging tools
  gem 'jekyll-twitter-plugin'
end


# Development tools
gem 'guard', '~> 2.14.2'
gem 'guard-jekyll-plus', '~> 2.0.2'
gem 'guard-livereload', '~> 2.5.2'

# To avoid build errors, see https://github.com/jekyll/jekyll/issues/2938
exclude: [vendor]
