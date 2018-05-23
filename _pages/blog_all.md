---
layout: archive
permalink: /archive
title: "All Posts"
author_profile: true

---

{% include base_path %}

{% for post in site.posts %}
  {% capture year %}{{ post.date | date: '%Y' }}{% endcapture %}
  {% include archive-single.html %}
{% endfor %}
