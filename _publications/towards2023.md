---
title: "Towards the efficient calculation of quantity of interest from steady Euler equations I: a dual-consistent DWR-based h-adaptive Newton-GMG solver"
#collection: publications
permalink: /publication/towards2023
excerpt: 'This paper is about the number 1. The number 2 is left for future work.'
#date: 2009-10-01
venue: 'Communications in Computational Physics'
status: "accepted"
paperurl: 'http://academicpages.github.io/files/paper1.pdf'
---
The dual consistency is an important issue in developing stable DWR error estimation towards the goal-oriented mesh adaptivity. In this paper, such an issue is studied in depth based on a Newton-GMG framework for the steady Euler equations. Theoretically, the numerical framework is redescribed using the Petrov-Galerkin scheme, based on which the dual consistency is depicted. It is found that for a problem with general configuration, a boundary modification technique is an effective approach to preserve the dual consistency in our numerical framework. Numerically, a geometrical multigrid is proposed for solving the dual problem, and a regularization term is designed to guarantee the convergence of the iteration. The following features of our method can be observed from numerical experiments, i). a stable numerical convergence of the quantity of interest can be obtained smoothly for problems with different configurations, and ii). towards accurate calculation of quantity of interest, mesh grids can be saved significantly using the proposed dual-consistent DWR method, compared with the dual-inconsistent one.

[Download paper here](https://raw.githubusercontent.com/shankswang953/shankswang953.github.io/master/files/towardsI.pdf)

