---
title: 'Concretization: Conditonal Expectation'
tags:
  - math
  - probability
  - concretization
---
## Concretization: Conditional Probability and Expectation
In modern probability theory, we don't define conditional probability with the usual formula:
$$
P(A | B) = \frac{P(A \cap B)}{P(B)}
$$

Instead we use a much more abstract formulation where we condition on an entire $\sigma$-field. This is much more general but also very far from the basic definition, and it's really quite hard to find a good exposition of how we recover usual conditional probability from this abstraction.

### General Conditional Expectation
"Normally" the conditional expectation of a random variable $X$ on a random variable $Y$ is defined as:
$$
E[X | Y=y] = \int_{-\infty}^{\infty} x P(X=x | Y=y) dx
$$
or for discrete random variables as:
$$
E[X | Y=y] = \sum_x x P(X=x | Y=y)
$$
This is nice and intuitive: we just take the formula for expectation and change the probability to a conditional probability.

*General* conditional expectation is not nearly so nice. We don't even construct it: we use the Radon-Nikodym theorem to prove that a random variable with a certain property must exist and be unique.

We define the conditional expectation of a random variable $X$ on a $\sigma$-field $\mathcal{G}$ as a random variable $E[X | \mathcal{G}]$ that satisfies:
$$
    \int_G E[X | \mathcal{G}] dP = \int_G X dP
$$
*and* we require that $E[X | \mathcal{G}]$ be $\mathcal{G}$-measurable.

### Conditional probability on a $\sigma$ - field
The conditional probability of an event $A$ on a $\sigma$-field $F$ is the conditional expectation of its indicator variable:
$$
P(A| F) = E[1_A | F]
$$


### Conditioning on an event
Okay, back to the beginning. If we want to condition on an event $B$, we just condition on the $\sigma$-algebra generated by $B, B^c$