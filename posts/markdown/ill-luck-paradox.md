---
title: 'The Ill-Luck Paradox'
tags:
  - math
  - probability
  - pathological
---
## Ill Luck Paradox

This is one of my favorite counterintuitive results. I got it from [Counterexamples in Probability and Statistics](https://www.goodreads.com/book/show/2787607-counterexamples-in-probability-and-statistics?ac=1&from_search=true&qid=qjY2rhiM71&rank=4), who got it from [Feller Volume 1](https://www.goodreads.com/book/show/2378167.An_Introduction_to_Probability_Theory_and_Its_Applications_Volume_1?ac=1&from_search=true&qid=Sm7rvHRTMn&rank=3).

We have a sequence of continuous, iid random variables $\mathcal{X} = [X_1, X_2, \ldots]$. We'll think of these as identical marathon runners running in sequence (technically our variables can be negative and as far as I know marathon runners cannot get negative times but let's ignore that).

 Define the random variable $R_w$ as the smallest $i > 1$ such that $X_i > X_1$. Define $R_l$ similarly, but with $X_i < X_1$. If we think of $X_1$ as the first marathon runner, then $R_w$ is the first runner to beat $X_1$ and $R_l$ is the first runner to lose to $X_1$.

Then $E[R_h] = E[R_l] = \infty$. However, $P(R_h = 2 | R_l = 2) = 1$. So it "should" take forever for a record to be set, but at least one record (either winning or losing) is guaranteed to be set immediately.


### Proof
Consider the first $n$ runners. Since they're all identical, the probability that the last runner is the fastest and the first runner is the second fastest is just the number of permutations that start with $\(n, 1\)$ over the total number of permutations, i.e. it's $(n-2)! / n! = 1 / n(n-1)$.

This is the probability that $R_h = n$ so the expectation is:

$$
E[R_h] = \sum n \frac{1}{n(n-1)} = \sum \frac{1}{n-1}
$$
This is of course a harmonic series, so it diverges and $E[R_h] = \infty$.