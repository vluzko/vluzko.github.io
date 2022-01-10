---
title: "PAC Causal Discovery Part 1: Background"
tags:
    - pac-causal-discovery
    - math
    - probability
    - statistical-learning-theory
---

## PAC Causal Discovery Part 1: Background

I'm writing this mostly as practice for writing/editing the corresponding paper. Experience says I'm quite slow when it comes to academic writing, and I'm hoping an informal draft will help.

### PAC Bounds
In statistical learning theory, we frequently obtain *probably approximately correct* (PAC) bounds on learning algorithms. In other fields we usually just get approximation bounds, e.g. "if I approximate this analytic function with a Taylor series of this many terms my approximation error is at most this much". In machine learning these bounds are often unobtainable, because there's always some chance that you get an extremely weird sample and learn entirely the wrong function.

Here's some more formal setup. We have some process generating data, governed by the true rule $r$. We have a learning algorithm $A$, which will take samples from $r$ and produce a hypothesis $h$ for what $r$ is. And we have some loss function $\mathcal{L}$ that takes $r$ and $h$ and tells us how close $h$ is to $r$. Our goal is to find an $A$ that minimizes the loss.

We say that $A$ is PAC if for any $\epsilon$ and $\delta$, there is some sample size $N$ such that for any sample of size $n > N$, we can guarantee:
\[
    P(L(h_n, r) > \epsilon) < \delta
\]
Usually we are interested in a tighter bound on $N$, ideally that $N$ is a polynomial in $1/\epsilon$ and $1/\delta$ (it's polynomial in the reciprocals because of course we want $\epsilon$ and $\delta$ to be as *small* as possible.)


### Causal Discovery
In causality theory, causal discovery is the problem of learning a causal graph given samples from the model.

- Structural causal model
- Causal graph
- Causal discovery
    - Constraint based methods


