---
layout: archive
permalink: /
title: "Recent Posts"
author_profile: true
redirect_from:
  - /wordpress/blog-posts/
  - /blog/
---

{% include base_path %}

{% for post in site.posts limit:20 %}
  {% capture year %}{{ post.date | date: '%Y' }}{% endcapture %}
  {% include archive-single.html %}
{% endfor %}

**([Blog Archive](/archive))**
