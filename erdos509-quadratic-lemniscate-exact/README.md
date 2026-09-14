# Exact disc-cover cost of the Bernoulli lemniscate `|z²−1|≤1`

**Author:** Jared Wilder  
**Estate origin:** Erdős #509 campaign  
**Public release:** 2026-09-14  
**Status:** exact standalone theorem; **no historical novelty claim**

Let

\[
L=\{z\in\mathbb C:|z^2-1|\le1\}.
\]

This is the filled Bernoulli lemniscate. Define its disc-cover cost by

\[
C(L)=\inf\left\{\sum_i\rho_i:
L\subseteq\bigcup_i\overline D(c_i,\rho_i)\right\}.
\]

Then

\[
\boxed{C(L)=\sqrt2.}
\]

## Upper bound

Write `z=x+iy` and `r²=x²+y²`. The condition `|z²−1|≤1` is equivalent to

\[
(x^2+y^2)^2\le2(x^2-y^2).
\tag{1}
\]

For a point of `L` with `x>=0`, (1) gives

\[
r^4\le2(x^2-y^2)\le2x^2.
\]

Since both sides are nonnegative,

\[
r^2\le\sqrt2\,x.
\]

Put

\[
a=\frac1{\sqrt2}.
\]

Then `2a=√2`, so

\[
|z-a|^2
=r^2-2ax+a^2
\le a^2.
\]

Thus the right half of `L` lies in

\[
\overline D\!\left(\frac1{\sqrt2},\frac1{\sqrt2}\right).
\]

By symmetry the left half lies in

\[
\overline D\!\left(-\frac1{\sqrt2},\frac1{\sqrt2}\right).
\]

Hence two discs cover `L` with total radius

\[
\frac1{\sqrt2}+\frac1{\sqrt2}=\sqrt2.
\]

Therefore

\[
C(L)\le\sqrt2.
\]

## Matching lower bound

On the real axis,

\[
|x^2-1|\le1
\iff
0\le x^2\le2,
\]

so

\[
[-\sqrt2,\sqrt2]\subseteq L.
\]

The intersection of a closed disc of radius `rho` with the real axis has length at most `2rho`. Consequently any collection of discs covering `L` must in particular cover the real interval of length `2√2`, giving

\[
2\sqrt2
\le
\sum_i2\rho_i.
\]

Thus

\[
C(L)\ge\sqrt2.
\]

Combining the bounds proves

\[
\boxed{C(L)=\sqrt2}.
\]

## Relation to Erdős #509

Erdős #509 asks whether every monic polynomial lemniscate `|f(z)|≤1` can be covered by discs whose radii sum to at most 2. This exact quadratic calculation is a solved slice only:

\[
f(z)=z^2-1
\quad\Longrightarrow\quad
C(L_f)=\sqrt2<2.
\]

It does not resolve the universal problem.

## Correction boundary

A different estate route tried to prove sharpness of the universal constant 2 with a mis-scaled Chebyshev family. That route was later refuted by its own endpoint calculation and is publicly retracted at

`jaredwilder/msl-ore-estate/corrections/ERDOS-509-CHEBYSHEV-SHARPNESS-RETRACTION-2026-09-14.md`.

The theorem in this file is independent of that dead route.
