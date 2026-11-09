---
permalink: /optimal-transport-and-operations-research/
title: "Optimal Transport & Operations Research"
excerpt: "GPU-accelerated optimal transport for mixed-integer optimization."
author_profile: true
---

<a class="research-back" href="{{ '/' | relative_url }}#research">&larr; Research overview</a>

I am interested in using **optimal transport structure** to develop efficient algorithms for operations research, particularly mixed-integer optimization problems with large transport subproblems.

## OTBD

**GPU-accelerated optimal transport for mixed-integer optimization**

OTBD accelerates repeated transport subproblem evaluations using entropy-regularized optimal transport, GPU-friendly scaling, and KL projections. Applications include capacitated p-median, hub transport, and facility location problems.

<figure class="research-figure research-video">
  <video controls playsinline preload="metadata" poster="{{ '/images/otbd-preview.jpg' | relative_url }}" aria-label="OTBD research presentation">
    <source src="{{ '/files/OTBD.mp4' | relative_url }}" type="video/mp4">
    Your browser does not support embedded video. <a href="{{ '/files/OTBD.mp4' | relative_url }}">Download the OTBD presentation.</a>
  </video>
  <figcaption>An introduction to OTBD and GPU-accelerated transport optimization (2 min 32 sec).</figcaption>
</figure>

## CPU&ndash;GPU workflow

The CPU solves the master problem, while the GPU evaluates the transport subproblem through KL projections. Dual recovery produces valid cuts; optional primal recovery provides upper bounds. Cut strengthening can improve the recovered cuts, and an exact LP solve is used when the available bounds are inconclusive.

<figure class="research-figure">
  <a href="{{ '/images/otbd-overview.png' | relative_url }}" aria-label="Open the full-size OTBD workflow">
    <img src="{{ '/images/otbd-overview.png' | relative_url }}" alt="OTBD workflow: a CPU master problem exchanges decisions, cuts, and bounds with GPU transport subproblems solved using KL projections, dual recovery, and optional primal recovery." loading="lazy">
  </a>
  <figcaption>Overview of OTBD: the master problem runs on the CPU, and transport subproblem evaluation runs on the GPU. Select the figure to view it at full size.</figcaption>
</figure>

## Computational results

In the illustrated experiments, GPU OTBD achieves **nearly two orders of magnitude faster subproblem evaluation at certain problem sizes** than conventional CPU subproblem solves.

Across 50 three-index hub transport instances, GPU OTBD reduces **mean subproblem evaluation time by 85.7%** relative to the baseline using exact CPU LP subproblem solves. It solves **47 of the 50 instances within one hour**, compared with **32** for that baseline.

<figure class="research-figure">
  <a href="{{ '/images/otbd-performance.png' | relative_url }}" aria-label="Open the full-size OTBD performance results">
    <img src="{{ '/images/otbd-performance.png' | relative_url }}" alt="Left: distributions of subproblem evaluation times on a logarithmic scale across problem sizes. Right: number of instances solved within one hour, with OT-GPU reaching 47 of 50." loading="lazy">
  </a>
  <figcaption>Left: subproblem evaluation times across instance sizes. Right: cumulative instances solved over time. The near-two-order speedup refers to subproblem evaluation at selected sizes; the right panel shows overall solve progress.</figcaption>
</figure>
