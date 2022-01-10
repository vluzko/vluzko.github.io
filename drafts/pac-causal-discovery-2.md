---
title: "PAC Causal Discovery Part 2"
tags:
    - pac-causal-discovery
    - math
    - probability
    - statistical-learning-theory
---

## PAC Causal Discovery Part 2

### Approximating Causal Graphs
I'm interested in putting PAC bounds on causal discovery. The first problem with this is that it's poorly defined. How do we measure the quality of an approximation?

Often the performance of causal discovery algorithms is measured in terms of metrics on the graph (e.g. the edit distance). We could try to establish theoretical bounds on this distance, but I think this is incorrect / not measuring what we really care about, because it fails to take into account the "importance" of particular edges.

Consider a model where $Z = Y + \sum_{i=1}^{10^6} X_i$. Each $X_i$ is drawn iid from $\mathcal{N}(0, 10^{-6})$, and $Y$ is drawn uniformly from $[-10^6, 10^6]$. So $Z$ is almost entirely determined by $Y$.

The correct causal graph has an arrow from $Y$ to $Z$, and an arrow from each $X_i$ to $Z$. Imagine our algorithm learned *only* the arrows from $X_i$ to $Z$. By any reasonable graph metric, these graphs are *very* close: they differ by a single arrow. But the models we would build with such a graph are all terrible: we miss almost all of the information required to predict $Z$.

I resolve this by measuring not the distance between the learned causal graph and the true causal graph, but the distance between a learned *causal model* and the true causal model.

To formalize this a little: we start with a structural causal model. That is, we have a set of $k$ real random variables $\mathcal{V}$ indexed by $I$, a directed acyclic graph $G$ on $\mathcal{V}$, a noise variable $n_i$ and function $f_i$ for each $v_i \in \mathcal{V}$. Every variable is determined by its function, its parents in the graph, and its noise variable. That is:
\[
v_i = f_i(parents(G, v_i), n_i)
\]

We draw a collection $\mathcal{X}$ of $n$ iid samples from this model. We have a causal discovery algorithm $D: \mathbb{R}^{k \times n} \rightarrow DAG(k)$ which takes our samples and outputs a causal graph on $\mathcal{V}$.

We also have a regression algorithm $A: \mathbb{R}^{k \times n} \times DAG(k) \rightarrow \mathcal{F}^k$. It takes the sampled data and the predicted graph, and produces an approximation of each function $f_i$ (so, for instance, $A$ might produce a neural network for each random variable).

### Learning Arrows
- Generalized Covariance Measure
- Polynomial bounds for GCM

### $W_1$ distance and covariance