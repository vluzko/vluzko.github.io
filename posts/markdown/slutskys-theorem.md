---
title: "Slutsky's Theorem"
date: 2022-04-07
tags:
    - pac-causal-discovery
    - math
    - probability
    - statistical-learning-theory
---
## Slutsky's Theorem

Slutsky's Theorem is a very useful theorem that for some reason doesn't get covered very often (maybe because it follows easily from other results?). It's the convergence in probability version of the theorems about performing arithmetic on limits. The formal statement:

Let $X_n \overset{d}{\rightarrow} X$ and $Y_n \overset{p}{\rightarrow} c$, where $X$ is a random variable and $c$ is a constant. Then:

\\begin{align}
    X_n + Y_n &\overset{d}{\rightarrow} X + c\\\\
    X_n Y_n &\overset{d}{\rightarrow} cX\\\\
    X_n / Y_n &\overset{d}{\rightarrow} X / c
\\end{align}

where the last only holds when $c \neq 0$

## Proof
The proof is extremely easy (and can be easily adapted to any other continuous operation). Since $X_n$ converges in distribution and $Y_n$ converges in probability, $(X_n, Y_n)$ converges in distribution to $(X, c)$. The continuous mapping theorem then implies that continuous functions of $(X_n, Y_n)$ (e.g. addition, multiplication, and division) will preserve the convergence in distribution.

## Extension with Sample Complexity
At one point in my work I needed a version of Slutsky's Theorem that worked with sample complexity, specifically where instead of the usual convergence in probability we had some function $f$ telling us how quickly $X_n$ and $Y_n$ converged:
$$
\forall \epsilon > 0: \forall \delta > 0: \forall n > f(1/\epsilon, 1/ \delta): P(|X_n - X| > \epsilon) < \delta
$$
which immediately implies $X_m \overset{p}{\rightarrow} X$ (notice the similarity to a PAC learning setup, which was the original motivation).

We can't directly use Slutsky's Theorem here, because we lose control over $f$ when we allow for arbitrary continuous functions of $(X_n, Y_n)$. However if we pick a particular class of functions $\mathcal{F}$ that we care about (e.g. we want to preserve a polynomial sample complexity bound), then we can come up with a class of functions that preserves $\mathcal{F}$. For polynomial bounds, we can apply any "polynomial Lipschitz" function, that is any function $g$ that satisfies:
$$
    d(g(x), g(y)) < p(d(x, y))
$$
where $p$ is a polynomial (for a normal $\lambda$-Lipschitz function we just set $p(x) = \lambda x$).