---
title: 'The Stokes-Cartan Theorem (Draft)'
date: 2019-07-21
permalink: /posts/2019/07/stokes-cartan/
category: Math
tags:
  - math
  - differential-geometry
  - important-theorems
---

The Stokes-Cartan theorem is my absolute favorite theorem. In nine symbols it expresses most of undergraduate calculus (plus a lot of other math). 

Stating a theorem without context isn't particularly helpful, but the full theorem is:
\[
 \int_{\Omega} d\omega = \int_{\partial \Omega} \omega
\]
In "English" this reads: the integral of the differential form $\omega$ over the boundary of the manifold $\Omega$ is equal to the integral of the exterior derivative of $\omega$ over all of $\Omega$.

Presumably if that made sense then you already know the Stokes-Cartan theorem and reading the rest of this post would be a waste of your time, so I'll assume it didn't make sense and try to give a gentler explanation. For me the easiest way to understand the Stokes-Cartan theorem is as a generalization of the Fundamental Theorem of Calculus:
\[
  \int_a^b f dx = F(b) - F(a)
\]

There's some obvious similarity between the two equations, right?. The left hand sides are almost the same, it's that right hand side that messes things up. But! In a bit we will define manifolds and it will turn out that the boundary of $[a,b]$ is the set $\{a, b\}$, so if we can come up with a definition of $\omega$ where we can define its integral over the points $a$ and $b$ to be equal to $F(b) - F(a)$ then everything will match up.

The *reason* for all this complexity is that you need it to do calculus on curved spaces. Doing calculus in the nice flat straight world of $\mathbb{R}^n$ is easy (in terms of the structure you have to build up to do it). But if you want to, say, talk about the integral of a function defined on a sphere, things get *very complicated*. 

For the rest of this post I'll be assuming knowledge of undergraduate calculus and linear algebra, plus a certain amount of mathematical maturity. 

#### Why
* Physics

### General Topology Crash Course
First we need to generalize the notion of a continuous function, which we do by generalizing the notion of the two points being 'close'.

In calculus, '$x$ is close to $y$' means '$|x - y| < \epsilon$, for some small $\epsilon$. Geometrically, this means that $x$ lies inside an open ball of radius $\epsilon$ centered at $y$:

IMAGE

To generalize this, we're going to do two things: first, instead of working with open balls, we're going to work with arbitrary sets, which we call 'open sets'. We'll say that two points are close if they lie in the same open set, rather than lying in the same open ball. Second, we're going to allow ourselves to work with more than $mathbb{R}$. *Any* set is now an acceptable set of points.

Here is the formal definition for this generalization:

A *topological space* is a set $X$ along with a collection $T$ of subsets of $X$. The sets in $T$ are the *open sets*. We require the following:
* $X \in T$
* $\emptyset \in T$
* If $A, B \in T$, then $A \cap B \in T$.
* If for any $i$ in an index set $I$ we have $U_i \in T$, then we have $\bigcup_{i \in I} U_i \in T$

EXAMPLE: $\mathbb{R}^3$.

The first two conditions are there for convenience (is this actually true?). Any time you get a $T$ that would be valid except that it's missing either of those sets, you can always just add them to $T$.

Remember that a continuous function is just a function that is defined everywhere, and whose value at each point equals its limit at that point. So generalizing this requires us to generalize limits to work on topological spaces.

Let $X$ and $Y$ be topological spaces, and let $f: X \rightarrow Y$ be a function from $X$ to $Y$.

### Manifolds
* Definition
A topological space $M$ is a manifold if for every $x \in M$ there is a neighborhood $x \in U$ such that $U$ is homeomorphic to $\mathbb{R}^n$ for some $n$.
Examples:
* $[0, 1]$
* $\mathbb{R}^3$
* $S^2$
These will be our primary examples.

* Details of the dimensionality of a manifold
* Manifolds with boundary.

#### Differentiable Manifolds
Roughly speaking, manifolds are the spaces similar enough to $\mathbb{R}^n$ that we can do calculus on them. However, we need to define some additional structure before we can actually calculate derivatives.

A *chart* on a manifold is a pair $(U, phi)$, where $phi$ is a homeomorphism between $U$ and $\mathbb{R}^n$, *and* $phi$ is smooth. Charts let us put coordinates on the manifold.

Two charts $(U, phi)$ and $(V, psi)$ are *compatible* if $phi inv(psi)$ and $psi inv(phi)$ are smooth on $psi(U intersect V)$ and $phi(U \cap V)$, respectively. Note that they *don't* have to be *equal*, so two different charts might assign different coordinates to the same point of $M$.

* Boundary
* Smooth functions
* Diffeomorphisms
* Tangent vector
* Tangent space
* Tangent bundle
* Vector fields

#### Orientation of Manifolds

### Multilinear algebra
A tensor is a generalization of a vector. There's quite a few ways to define tensors, but we're going to stick to a nice concrete version: a *covariant* tensor is an element of $V^k$, and a *contravariant* tensor is an element of $(V^*)^l$. We call these $V^k$ and $V_l$ tensors, respectively.


* Tensors
* Alternating tensors
* Exterior product and algebra

### Differential Forms
* Differential forms
* Integrating differential forms

### Stokes-Cartan 
* Restatement of theorem
* Proof


### Fundamental Theorem of Calculus
Okay, so how does this imply the Fundamental Theorem of Calculus? On the one side, we have:
\[
  \int_{\partial M} \omega = \int_M d \omega
\]
on the other, we have:
\[
  \int_0^1 f dx = F(1) - F(0)
\]

Our manifold $M$ will be is $[0, 1]$. Our form $\omega$ will be a $0$-form with coordinate function $F$. We do this by making $\omega$ a 0-form, i.e. it's a function $\omega: [0, 1] \rightarrow \Lambda^0([0, 1])$. $\Lambda^0$ is the bundle of alternating 0-tensors on $[0,1]$. A 0-tensor is just a scalar, so we have $\omega: [0, 1] \rightarrow \mathbb{R}$. This is, of course, just a normal function.

How do we get $f dx$? As you might expect, we can take the exterior derivative of $f$ and get a $1$-form $f dx$. We have set everything up so that the integral of the $1$-form $f dx$ over $[0, 1]$ is exactly the same as the usual integral $\int_0^1 f dx$ (and of course this why is why the particular notation for differential forms has been chosen).

So, what is the exterior derivative of the $0$-form $f$? Since we're working over $\mathbb{R}^k$, the exterior derivative of $\omega$ is $\sum da_I \wedge dx_I$. But there's only one coordinate function of $omega$: $f$.

### Stokes' Theorem
