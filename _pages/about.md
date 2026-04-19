---
permalink: /
title: "About Me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

I am Jingfeng Wang, a postdoctoral research scholar at North Carolina State University. I received my Ph.D. from the University of Macau in 2024, and my B.S. from Sichuan University in 2020. My research lies at the intersection of partial differential equations, optimization, and machine learning. Discussions and collaborations are warmly welcomed.

## Research Interest

My work spans **numerical methods for PDEs**, **machine learning in PDE fields**, and their integration for scientific computing.

---

### Numerical Methods for PDEs

A central theme of my work is **adjoint-based mesh adaptation**. During my Ph.D. I built an automatic dual-consistent mesh adaptation method for the steady Euler equations within AFVM4CFD (a library maintained by our group), and proposed a hybrid CNN+Dual approach that significantly accelerates the adaptation procedure.

<figure>
    <img src="../images/precision.png" alt="Error" style="width:48%;">
    <img src="../images/time4dual.png" alt="Time" style="width:48%;">
    <figcaption>The CNN-based solver substantially reduces computation time while preserving the accuracy of target functionals.</figcaption>
</figure>

**Multi-mesh method for multi-target functionals.** Real applications often involve nonlinear or composite functionals beyond simple drag/lift, where existing theoretical guarantees no longer apply. A multi-mesh framework offers a principled way to handle such cases by allocating an adapted mesh to each target.

<figure>
    <img src="../images/multimeshProcess.png" alt="Multi-mesh process" style="width:75%;">
    <figcaption>Workflow of the multi-mesh adaptation procedure.</figcaption>
</figure>

<figure>
    <img src="../images/qoiLift.png" alt="QoI Lift" style="width:48%;">
    <img src="../images/qoiDrag.png" alt="QoI Drag" style="width:48%;">
    <figcaption>Convergence of lift (left) and drag (right) under the multi-mesh framework.</figcaption>
</figure>

**Towards more realistic models.** The current framework relies on the steady Euler equations with mirror-reflection boundary conditions. Capturing boundary-layer effects in airfoil shape optimization will require richer models such as Navier&ndash;Stokes and Boltzmann equations.

---

### Machine Learning in PDE Fields

I view machine learning as a complement to&mdash;not a replacement for&mdash;classical numerical methods. My recent work explores **reinforcement learning for shape and geometry optimization**, with classical-method-informed learning frameworks: e.g., airfoil shape optimization driven by a CFD solver, and molecular geometry optimization driven by DFT.

<figure>
    <img src="../images/Loop.png" alt="RL training loop" style="width:48%;">
    <img src="../images/Detail.png" alt="Algorithm detail" style="width:48%;">
    <figcaption>Left: the overall RL optimization loop. Right: the mechanism-driven algorithmic details.</figcaption>
</figure>

**Multi-agent exploration.** Multi-agent training accelerates data collection&mdash;a classical bottleneck of RL exploration&mdash;and naturally accommodates conventional optimization tools such as the adjoint method within the learning loop.

**Data-driven discretization with classical structure.** Classical discretization remains indispensable for an efficient and credible solver: it informs network design (e.g., handling rotational/translational invariance in molecules, or non-smooth airfoil geometries) and provides reliable evaluations during optimization. I am developing data-driven discretizations that retain these structural guarantees while leveraging the speed of learned components.
