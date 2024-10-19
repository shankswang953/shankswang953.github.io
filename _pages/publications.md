---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---
{% include base_path %}

<ol reversed>
{% assign sorted_publications = site.publications | sort: "date" | reverse %}
{% for post in sorted_publications %}
  <li>
    {% include archive-single.html %}
  </li>
{% endfor %}
</ol>
