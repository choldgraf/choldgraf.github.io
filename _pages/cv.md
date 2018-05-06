---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

If you want a hard-copy CV, you can find a [reasonably up-to-date CV here](/files/cv.pdf)

Education
======
* B.S. in Neuroscience, Tulane University, 2009
* M.S. in Neuroscience, Tulane University, 2010
* Ph.D. in Neuroscience, University of California at Berkeley, 2017

Publications
======
  <ul>{% for post in site.publications %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
