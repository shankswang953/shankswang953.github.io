---
permalink: /numerical-methods-for-pdes/
title: "Numerical Methods for PDEs"
excerpt: "Goal-oriented mesh adaptation, multi-mesh methods, and learning-assisted PDE optimization."
author_profile: true
---

<a class="research-back" href="{{ '/' | relative_url }}#research">&larr; Research overview</a>

My work spans **numerical methods for PDEs**, **machine learning in PDE fields**, and their integration for scientific computing.

<nav class="research-sections" aria-label="On this page">
  <a href="#mesh-adaptation">Mesh adaptation</a>
  <a href="#multi-mesh">Multi-mesh methods</a>
  <a href="#learning-assisted-optimization">Learning &amp; optimization</a>
  <a href="#tutorials">Tutorials</a>
</nav>

## Goal-oriented mesh adaptation
{: #mesh-adaptation}

A central theme of my work is **adjoint-based mesh adaptation**. During my Ph.D., in joint work with my advisor Prof. Guanghui Hu, I developed an automatic dual-consistent mesh adaptation method for the steady Euler equations within [AFVM4CFD](https://ghhu.github.io/software.html), the CFD library maintained by our group, and proposed a hybrid CNN+Dual approach that significantly accelerates the adaptation procedure.

## Multi-mesh methods for multiple target functionals
{: #multi-mesh}

Real applications often involve nonlinear or composite functionals beyond simple drag/lift, where existing theoretical guarantees no longer apply. A multi-mesh framework offers a principled way to handle such cases by allocating an adapted mesh to each target.

<figure class="research-figure">
  <a href="{{ '/images/multimeshProcess.pdf' | relative_url }}" aria-label="Open the full-size multi-mesh workflow PDF">
    <img src="{{ '/images/multimeshProcess.png' | relative_url }}" alt="Multi-mesh adaptation workflow: separate meshes are refined for each target functional and merged into a union space." loading="lazy">
  </a>
  <figcaption>Workflow of the multi-mesh adaptation procedure. Select the figure to open the full-size PDF.</figcaption>
</figure>

<figure class="research-figure">
  <div class="research-figure__pair">
    <img src="{{ '/images/qoiLift.png' | relative_url }}" alt="Lift error comparison for single-mesh and multi-mesh calculations." loading="lazy">
    <img src="{{ '/images/qoiDrag.png' | relative_url }}" alt="Drag error comparison for single-mesh and multi-mesh calculations." loading="lazy">
  </div>
  <figcaption>Lift (left) and drag (right) errors when computing the lift-to-drag ratio. Single-mesh accuracy fluctuates sharply with the lift&ndash;drag weighting (1:1 to 1:500), whereas the multi-mesh framework remains stable and parameter-insensitive.</figcaption>
</figure>

**Towards more realistic models.** The current framework relies on the steady Euler equations with mirror-reflection boundary conditions. Capturing boundary-layer effects in airfoil shape optimization will require richer models such as Navier&ndash;Stokes and Boltzmann equations.

## Machine learning for PDE-based optimization
{: #learning-assisted-optimization}

I view machine learning as a complement to classical numerical methods. My recent work explores **reinforcement learning for shape and geometry optimization**, with classical-method-informed learning frameworks: e.g., airfoil shape optimization driven by a CFD solver, and molecular geometry optimization driven by DFT.

<figure class="research-figure">
  <a href="{{ '/images/Loop-2.pdf' | relative_url }}" aria-label="Open the full-size reinforcement learning workflow PDF">
    <img src="{{ '/images/rl-optimization-loop.svg' | relative_url }}" alt="Reinforcement learning loop for airfoil shape optimization: geometry optimization, mesh processing, and the AFVM4CFD environment are linked through a replay buffer." loading="lazy">
  </a>
  <figcaption>The overall reinforcement learning optimization loop in AFVM4CFD. Select the figure to open the full-size PDF.</figcaption>
</figure>

<figure class="research-figure">
  <img src="{{ '/images/Detail.png' | relative_url }}" alt="Mechanism-driven reinforcement learning algorithm for PDE-based shape optimization." loading="lazy">
  <figcaption>Mechanism-driven algorithmic details.</figcaption>
</figure>

**Multi-agent exploration.** Multi-agent training accelerates data collection&mdash;a classical bottleneck of RL exploration&mdash;and naturally accommodates conventional optimization tools such as the adjoint method within the learning loop.

**Data-driven discretization with classical structure.** Classical discretization remains indispensable for an efficient and credible solver: it informs network design (e.g., handling rotational/translational invariance in molecules, or non-smooth airfoil geometries) and provides reliable evaluations during optimization. I am developing data-driven discretizations that retain these structural guarantees while leveraging the speed of learned components.

## Tutorials
{: #tutorials}

### Mesh operations with AFEPack

Materials from my Tianyuan Mathematics Center short course on finite-element computation and adaptive meshes using **AFEPack**. Examples progress from a P1 Poisson solver to residual-based and goal-oriented refinement, dual problems, mesh merging, mesh motion, and shape optimization.

[View the tutorial on GitHub](https://github.com/shankswang953/AFEPack_Tianyuan_shortcourse)

## Related work and software

- [Dual-consistent DWR-based adaptive Newton&ndash;GMG solver]({{ '/publication/towards2023' | relative_url }})
- [CNN-based automatic mesh adaptation]({{ '/publication/towards2024' | relative_url }})
- [Multi-mesh methods for multi-target functionals]({{ '/publication/multimesh' | relative_url }})
- [Reinforcement learning for airfoil shape optimization]({{ '/publication/rl4opt' | relative_url }})
- [AFVM4CFD software](https://ghhu.github.io/software.html)
