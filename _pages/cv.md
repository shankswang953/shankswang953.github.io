---
layout: archive
title: "Curriculum Vitae"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---
{% assign cv_version = site.time | date: '%Y%m%d%H%M%S' %}
{% assign cv_pdf_url = '/files/JingfengWang_Resume.pdf' | relative_url | append: '?v=' | append: cv_version %}

<p class="cv-updated">Last updated: <time datetime="2026-11-09">November 9, 2026</time></p>

<div class="cv-actions">
  <a class="btn btn--primary" href="{{ cv_pdf_url }}" download="Jingfeng_Wang_CV.pdf">Download CV</a>
</div>

<div class="cv-preview" data-pdf-url="{{ cv_pdf_url }}" role="region" aria-label="CV preview" aria-busy="true" tabindex="0">
  <p class="cv-preview__status" role="status">Loading CV&hellip;</p>
  <noscript><p>Please use the download link above to read the CV.</p></noscript>
</div>

<script type="module" src="{{ '/assets/js/cv-preview.js' | relative_url }}?v={{ cv_version }}"></script>
