---
permalink: /optimal-transport-modeling-and-biological-application/
title: "Optimal Transport Modeling and Biological Application"
excerpt: "Dynamic and unbalanced optimal transport for biological data, including cross-omics trajectory inference with COATI."
author_profile: true
---

<a class="research-back" href="{{ '/' | relative_url }}#research">&larr; Research overview</a>

I study **dynamic and unbalanced optimal transport** and their applications to biological data. A particular focus is modeling how cell populations evolve over time while combining information from different measurement spaces.

## COATI

**Cross-Omics Aligned Trajectory Inference**

COATI reconstructs continuous cell-state dynamics from time-indexed single-cell snapshots. It uses synchronized optimal transport and neural ODEs to couple trajectory inference across modalities, including gene expression and chromatin accessibility.

A flow learned in the RNA feature space is mapped into the ATAC space through a pretrained cross-modal map. Observations in both spaces constrain the dynamics, while each modality retains its own representation.

<div class="research-resource-links" aria-label="COATI resources">
  <a href="https://shankswang953.github.io/COATI_website/index.html">Project website <span aria-hidden="true">&nearr;</span></a>
  <a href="https://github.com/shankswang953/COATI">Code on GitHub <span aria-hidden="true">&nearr;</span></a>
  <a href="https://shankswang953.github.io/COATI_website/tutorials.html">Tutorials <span aria-hidden="true">&nearr;</span></a>
</div>

<figure class="research-figure research-video">
  <video controls playsinline preload="metadata" poster="{{ '/images/coati-preview.jpg' | relative_url }}" aria-label="COATI research presentation">
    <source src="{{ '/files/COATI.mp4' | relative_url }}" type="video/mp4">
    Your browser does not support embedded video. <a href="{{ '/files/COATI.mp4' | relative_url }}">Download the COATI presentation.</a>
  </video>
  <figcaption>A short introduction to COATI and cross-omics trajectory inference (2 min 57 sec).</figcaption>
</figure>

### Modeling population dynamics across modalities

- **Synchronized trajectories.** A neural ODE describes cell-state evolution in the primary space, and a fixed cross-modal map projects the trajectories into the secondary space.
- **Balanced and unbalanced models.** Balanced COATI conserves population mass; unbalanced COATI additionally models growth and depletion.
- **Trajectory readouts.** The package supports visualization of inferred flows, model-based population changes, and local gene-expression and accessibility readouts along trajectories.

The [project documentation](https://shankswang953.github.io/COATI_website/index.html) includes synthetic and biological examples, installation instructions, and the mathematical formulation.

## Related work

- [Synchronization of unbalanced dynamical optimal transport across multiple spaces]({{ '/publication/sync_ot_multispaces' | relative_url }})
- [Cross-modality trajectory inference integrating scRNA-seq and scATAC-seq]({{ '/publication/sync_ot_crossmodality' | relative_url }})
- [RAFT-UP: spatial transcriptomics alignment]({{ '/publication/raftup' | relative_url }})
