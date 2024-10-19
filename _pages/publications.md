---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---
{% if site.author.googlescholar %}

<div class="wordwrap">You can also find my articles on <a href="{{site.author.googlescholar}}">my Google Scholar profile</a>.</div>
{% endif %}

{% include base_path %}

<ul class="publications-list">
{% assign sorted_publications = site.publications | sort: "date" | reverse %}
{% for post in sorted_publications %}
  <li>
    {% include archive-single.html %}
  </li>
{% endfor %}
</ul>
