---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

Here's a relatively recent list of my publications.

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
