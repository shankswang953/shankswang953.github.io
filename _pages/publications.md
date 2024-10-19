---
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

<ol class="publications-list">
{% for post in site.publications reversed %}
  <li>
    {% include archive-single.html %}
  </li>
{% endfor %}
</ol>
br
---
