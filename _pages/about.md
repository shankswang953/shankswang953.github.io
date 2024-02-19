---
permalink: /
title: "Research Interest"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

My research interests range from numerical methods for partial differential equations (PDEs), machine learning, and optimization.

**Numerical Methods in PDEs**

A key focus of my research is the development of mesh adaptation methods designed to fulfill a variety of computational needs. During my Ph.D. studies, I embarked on research into adjoint-based mesh adaptation. I developed an automatic dual consistent mesh adaptation method based on the steady Euler equations within AFVM4CFD, a library our group maintains. Furthermore, I introduced a hybrid approach combining Convolutional Neural Networks (CNNs) and a Dual solver to expedite the mesh adaptation process.

<figure>
    <img src="../images/precision.png" alt="Error" style="width:48%;">
    <img src="../images/time4dual.png" alt="Time" style="width:48%;">
    <figcaption>The CNNs solver saves time significantly while preserving the accuracy of target functional.</figcaption>
</figure>

Despite the strides made in developing such a powerful solver, challenges persist that necessitate further enhancements.Following aspects are those I am working on and should be improved upon in the future:

* Multi-mesh method for multi-target functionals

In actual applications, the target functionals are much more complicated than the drag or lift calculation. However, theoretical analysis can not guanrantee the framework can be generalized to nonlinear and composite target functionals. Thus, multi-mesh is a potential method that can fufill the requirements.

* Incorporation of More Realistic Scenarios

The existing framework, built on steady Euler equations and mirror reflection boundary conditions, offers a foundation. However, the intricacies of airfoil shape optimization demand a deeper dive, particularly into boundary layer issues. Our ambition is to incorporate more sophisticated models, including Navier-Stokes and Boltzmann equations, to capture the nuanced impacts on geometry more accurately. 

**Machine learning in PDE fields**

I believe machine learning is a competitive technique in numerical calculation. I prefer to integrate machine learning with classical methods instead of substituting them. For example, I use the convolutional neural network to enhance the mesh adaptation but remain the solver for the governing equations. Currently, I am exploring reinforcement learning for optimization and trying to enhance such a process by classical method-informed learning frameworks. For example, the shape optimization of airfoil based on the CFD model and geometrical optimization of a molecule based on the DFT model.

<figure>
    <img src="../images/minDrag.png" alt=",minDrag" style="width:48%;">
    <img src="../images/maxRatio.png" alt="maxRatio" style="width:48%;">
    <figcaption> Optimized from NACA0012 with different obejectives. Left: minimize drag, Right: Maximize lift-drag ratio.</figcaption>
</figure>



