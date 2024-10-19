---
title: "A mechanism-informed reinforcement learning framework for shape optimization of airfoils"
#collection: publications
permalink: /publication/rl4opt
excerpt: 'Available on Arxiv:https://arxiv.org/abs/2403.04329. In this work, we proposed the mechanism-informed reinforcement learning framwork based on the AFVM4CFD, aiming at conducting the shape optimization with the powerful PDE solver we constructed.'
date: 2024-06-01
#venue: 'Communications in Computational Physics'
status: "prepare"
collaborators: Guanghui Hu
paperurl:'https://raw.githubusercontent.com/shankswang953/shankswang953.github.io/master/files/rl4opt.pdf'
---
paperurl:'https://raw.githubusercontent.com/shankswang953/shankswang953.github.io/master/files/towardsII.pdf'
-------------------------------------------------------------------------------------------------------------

---

In this study, we present the mechanism-informed reinforcement learning framework for airfoil shape optimization. By leveraging the twin delayed deep deterministic policy gradient algorithm for its notable stability, our approach addresses the complexities of optimizing shapes governed by fluid dynamics. The PDEs-based solver is adopted for its accuracy even when the configurations and geometries are extraordinarily changed during the exploration. Dual-weighted residual-based mesh refinement strategy is applied to ensure the accurate calculation of target functionals. To streamline the iterative optimization process and handle geometric deformations, our approach integrates Laplacian smoothing, adaptive refinement, and a Bézier fitting strategy. This combination not only remits mesh tangling but also guarantees a precise manipulation of the airfoil geometry. Our neural network architecture leverages Bézier curves for efficient dimensionality reduction, thereby enhancing the learning process and ensuring the geometric accuracy of the airfoil shapes. An attention mechanism is embedded within the network to calculate potential action on the state as well. Furthermore, we have introduced different reward and penalty mechanisms tailored to the specific challenges of airfoil optimization. This algorithm is designed to support the optimization task, facilitating a more targeted and effective approach for airfoil shape optimization.

[Download paper here](https://arxiv.org/abs/2403.04329)
