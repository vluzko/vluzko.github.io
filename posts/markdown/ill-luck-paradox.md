---
title: "The Ill Luck Paradox"
date: 2021-09-30
tags:
  - math
  - probability
  - pathological
---
## The Ill Luck Paradox

The ill luck paradox is one of my favorite counterintuitive results. I got it from [Counterexamples in Probability and Statistics](https://www.goodreads.com/book/show/2787607-counterexamples-in-probability-and-statistics?ac=1&from_search=true&qid=qjY2rhiM71&rank=4), who got it from [Feller Volume 1](https://www.goodreads.com/book/show/2378167.An_Introduction_to_Probability_Theory_and_Its_Applications_Volume_1?ac=1&from_search=true&qid=Sm7rvHRTMn&rank=3).

Here's the short version of the paradox: on average, it should take forever to set new marathon records (or any kind of record). It should also take forever to *not* set a record.

We have a sequence of continuous, iid random variables $\mathcal{X} = [X_1, X_2, \ldots]$. We could think of these as, for instance, the times achieved by an infinite sequence of marathon runners drawn from the same population.

Define the random variable $R_w$ as the smallest $i > 1$ such that $X_i < X_1$. That is, it's the number of the first runner to beat the very first runner ($w$ for win). Define $R_l$ similarly, but with $X_i > X_1$ ($l$ for lose): the number of the first runner who *doesn't* beat the very first runner.

Then $E[R_h] = E[R_l] = \infty$, i.e. it will on average take forever for anyone to beat the first runner, and it will on average take forever for anyone to *not* beat the first runner. And of course $P(R_h = 2 | R_l = 2) = 1$: the second runner is guaranteed to either beat or not beat the first runner.

### Proof
Consider the first $n$ runners. Since they're all identical, the probability that the last runner is the fastest and the first runner is the second fastest is just the number of permutations that start with $(n, 1)$ over the total number of permutations, i.e. it's $(n-2)! / n! = 1 / n(n-1)$. Note that because we assumed our distribution is continuous the probability that any two runners *tie* is zero, so there is always a strict order on the runners.

This is the probability that $R_h = n$ so the expectation is:
$$
E[R_h] = \sum n \frac{1}{n(n-1)} = \sum \frac{1}{n-1}
$$
This is a harmonic series, so $E[R_h] = \infty$.
