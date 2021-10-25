---
title: "PAC Causal Discovery Part 1"
tags:
    - pac-causal-discovery
    - math
    - probability
    - statistical-learning-theory
---

## PAC Causal Discovery Part 1

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
In causality theory, *causal discovery* is the problem of learning a causal graph (a graph of the causal relationships in the model) given samples from the model.

- Structural causal model
- Causal graph
- Causal discovery
    - Constraint based methods


### Approximating Causal Graphs
I'm interested in putting PAC bounds on causal discovery. The first problem with this is that it's ill-defined. What does it mean to approximate a graph?

Often the performance of causal discovery algorithms is measured in terms of metrics on the graph (e.g. the Hamming distance). We could try to establish theoretical bounds on this distance, but I think this is incorrect / not measuring what we really care about, because it fails to take into account the *importance* of particular edges.

Consider a model where $Z = Y + \sum_{i=1}^{10^6} X_i$. Each $X_i$ is drawn iid from $\mathcal{N}(0, 10^{-6})$, and $Y$ is drawn uniformly from $[-10^6, 10^6]$. So $Z$ is almost entirely determined by $Y$.

The correct causal graph has an arrow from $Y$ to $Z$, and an arrow from each $X_i$ to $Z$. Imagine our algorithm learned *only* the arrows from $X_i$ to $Z$. By a graph metric, these graphs are *very* close: one arrow wrong, a million right. But the models we would build with such a graph are all terrible: we miss almost all of the information required to predict $Z$.

I resolve this by measuring not the distance between the learned causal graph and the true causal graph, but the distance between a learned *causal model* and the true causal model.

To formalize this a little: we start with a structural causal model. That is, we have a set of random variables $\mathcal{V}$, a directed acyclic graph $G$ on $\mathcal{V}$, a noise variable $N_V$ and function $f_V$ for each $V \in \mathcal{V}$. Every variable is determined by its function, its parents in the graph, and its noise variable. That is:
\[
V = f_V(parents(G, V), N_V)
\]

We draw a collection $X$ of iid samples from this model. We have a causal discovery algorithm $D$ which takes $X$ and outputs a causal graph