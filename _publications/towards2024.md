---
title: "Towards the efficient calculation of quantity of interest from steady Euler equations II: a CNNs-based automatic implementation."
#collection: publications
permalink: /publication/towards2024
excerpt: 'This paper is about the CNNs-Dual algorithm.'
date: 2024-01-01
venue: 'Communications in Computational Physics'
status: "accepted"
paperurl:'https://raw.githubusercontent.com/shankswang953/shankswang953.github.io/master/files/towardsII.pdf'
---
In [J. Wang, G. Hu, arxiv: 2302.14262], a dual-consistent
  dual-weighted residual-based $h$-adaptive method has been proposed
  based on a Newton-GMG framework, toward the accurate calculation of a
  given quantity of interest from Euler equations. The performance of
  such a numerical method is satisfactory, i.e., the stable
  convergence of the quantity of interest can be observed. In this paper, we will focus on the
  efficiency issue to further develop this method. Three approaches are studied
  for addressing the efficiency issue, i.e., i). using convolutional
  neural networks as a solver for dual equations, ii). designing an
  automatic adjustment strategy for the tolerance in the $h$-adaptive
  process to conduct the local refinement and/or coarsening of mesh
  grids, and iii). introducing OpenMP, a shared memory parallelization
  technique, to accelerate the module such as the solution
  reconstruction in the method. The feasibility of each approach and
  numerical issues are discussed in depth, and significant
  acceleration from those approaches in simulations can be observed
  clearly from a number of numerical experiments. In convolutional
  neural networks, it is worth mentioning that the dual consistency
  plays an important role in guaranteeing the efficiency of the whole
  method and that unstructured meshes are employed in all
  simulations.

[Download paper here](https://raw.githubusercontent.com/shankswang953/shankswang953.github.io/master/files/towardsII.pdf)
