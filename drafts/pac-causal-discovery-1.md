---
title: "PAC Causal Discovery Part 1: Background"
tags:
    - pac-causal-discovery
    - math
    - probability
    - statistical-learning-theory
---

## PAC Causal Discovery Part 1: Background
A lot of my time is spent on statistical learning theory applied to causality. In particular I'm interested in the causal discovery problem: the problem of determining the causal relationships between a set of random variables. For various reasons I think the usual ways of comparing algorithms for causal discovery are fine for practical purposes but not really right for theoretical analysis, so much of my work has just been defining what a "good" algorithm is.

### PAC Bounds
In statistical learning theory, one measure of the quality of a learning algorithm is a probably approximately correct (PAC) bound. A PAC bound says the algorithm has high probability of producing an approximately correct output, given some "reasonable" number of samples to learn from.

More formally: we have some process generating data, governed by the true rule $r \in \mathcal{H}$. We have a learning algorithm $A$, which will take samples from $r$ and produce a hypothesis $h \in \mathcal{H}$ for what $r$ is. And we have some loss function $\mathcal{L}: \mathcal{H} \times \mathcal{H} \rightarrow \mathbb{R}$. Our goal is to find an $A$ that minimizes $\mathcal{L}$.

We say that $A$ is PAC if for any $\epsilon$ and $\delta$, there is some sample size $N$ such that for any sample of size $n > N$, we can guarantee:
\[
    P(L(h_n, r) > \epsilon) < \delta
\]
Usually we are interested in a tighter bound on $N$, ideally that $N$ is a polynomial in $1/\epsilon$ and $1/\delta$ (it's polynomial in the reciprocals because of course we want $\epsilon$ and $\delta$ to be as *small* as possible.)

As a general rule, PAC bounds are as good as we can get when we're learning from random samples. We cannot eliminate the possibility of getting an extremely weird set of samples, so there is always going to be *some* probability that we learn a completely incorrect rule. And for any problem where we're trying to learn one or more continuous values we aren't going to be able to learn the exact value, so even if we do get a good sample it will only be an approximation.


### Causal Discovery
In causality theory, we think of causal relationships as a directed acyclic graph between random variables, where an edge from $A$ to $B$ means that $A$ is a direct cause of $B$. Causal discovery is the problem of determining the graph of causal relationships given samples from the random variables you're studying.

Explaining all the details is rather more than I can do in one blog post, so let's quickly touch some basics.


A *structural causal model* $M$ is a set of $k$ real random variables $\mathcal{V}$ indexed by some set $I$, a directed acyclic graph $G$ on $\mathcal{V}$, a noise variable $n_i$ and function $f_i$ for each $v_i \in \mathcal{V}$. Every variable is determined by its function, its parents in the graph, and its noise variable. That is:
\[
v_i = f_i(\textrm{parents}(G, v_i), n_i)
\]
We might also stipulate that each $f_i$ is a member of some class of functions $\mathcal{F}$ (e.g. all linear functions).

$M$ determines a distribution over all of $\mathcal{V}$, which I will denote $M_O$ ($O$ for "observational distribution"). Causality focuses heavily on the further notions of *intervention* and *counterfactual*, both of which are operations we can perform on structural causal models, but I don't actually need them for this explanation so I won't go into more detail.

*Causal discovery* is the problem of taking samples from $M_O$, and finding a DAG $\hat{G}$ that is as close as possible to the true graph $G$.

In general this is impossible, however we *can* (in theory) recover the *skeleton* of $G$, just not necessarily the direction of every single edge (one of the most interesting results in causality is that we can sometimes discover the direction of *some* of the edges, purely from observation. This is contrary to standard wisdom about always needing to run controlled experiments to establish causality.)