---
title: "PAC Causal Discovery Part 2"
date: 2022-04-03
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

Consider a model where $Z = Y + \sum_{i=1}^{10^6} X_i$. Each $X_i$ is drawn iid from $\mathcal{N}(0, 10^{-6})$, and $Y$ is drawn from $\mathcal{N}(0, 100)$. So $Z$ is sampled from $\mathcal{N}(0, 101)$, and its value is almost entirely determined by the value of $Y$.

The correct causal graph has an arrow from $Y$ to $Z$, and an arrow from each $X_i$ to $Z$. Imagine our algorithm learned *only* the arrows from $X_i$ to $Z$. By most graph metrics, these graphs are very close: they differ by a single arrow. But the models we would build with such a graph are all terrible: we miss almost all of the information required to predict $Z$. And of course we can make this situation arbitrarily bad: you can construct graphs that are an arbitrarily small (non-zero) distance from the true graph, whose corresponding models are arbitrarily inaccurate.

The solution is to measure not the distance between the learned causal graph and the true causal graph, but the distance between a learned *causal model* and the true causal model. This complicates the question, because there are many ways to learn a causal model for some particular causal graph. We need to make sure that after we extend this we're still really comparing just the causal discovery algorithms, and not the entire causal model learning algorithm.

To formalize this a little: we start with a structural causal model $M$. We draw a collection $\mathcal{X}$ of $n$ iid samples from this model. We have a causal discovery algorithm $D: \mathbb{R}^{k \times n} \rightarrow DAG(k)$ which takes our samples and outputs a causal graph on $\mathcal{V}$.

We also have a regression algorithm $A: \mathbb{R}^{k \times n} \times DAG(k) \rightarrow \mathcal{F}^k$. It takes the sampled data and the predicted graph, and produces an approximation of each function $f_i$ (so, for instance, $A$ might produce a neural network for each random variable).

This gives us an algorithm that produces structural causal models. Let $\hat{M} = A(D(\mathcal{X}), \mathcal{X})$ be the structural causal model produced by the causal discovery algorithm. We can now compare $\hat{M}$ to $M$, and use that as a measure of the quality of $D$. I chose to use
$$
W_1(M_O, \hat{M}_O)
$$
as the metric (here $M_O$ is the observational distribution associated with the model $M$).

Of course for this to be meaningful we need to require that $A$ is a "good" regression algorithm in some sense. For instance we might require that there be a PAC learning result for $A$ (that is that its output achieves some low error with high probability for a reasonable number of samples).

We could also drop $A$ entirely and instead compare, for instance, the best *possible* model built with $D(\mathcal{X})$, with the restriction that all the functions be members of $\mathcal{F}$. I didn't really pursue this though, mostly because I think the regression algorithm scenario is closer to life.

### Learning Arrows
In constraint-based causal discovery, the fundamental relationship is conditional dependence. Unfortunately, it is [impossible in general to reliably learn conditional dependence relationships](https://arxiv.org/abs/1804.07203). Fortunately, the same paper introduces a measure of conditional dependence whose core assumption is the presence of a "good enough" regression algorithm. Since we have to assume the a good regression algorithm *anyway*, this is basically free.

The test itself can only distinguish conditional dependence (of $X$ and $Y$ on $Z$) when $X$ and $Y$ have non-zero conditional covariance.

### $W_1$ distance and covariance