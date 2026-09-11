# Erdős #247 — sparse binary-position irrationality theorem

**Author:** Jared Wilder  
**Recovered from:** September 2026 MSL audit  
**Public extraction:** 2026-09-11

## Theorem

Let

\[
a_1<a_2<a_3<\cdots
\]

be a strictly increasing sequence of positive integers. If

\[
\limsup_{n\to\infty}\frac{a_n}{n}=\infty,
\]

then

\[
\sum_{n\ge1}2^{-a_n}
\]

is irrational.

## Proof

Because the exponents are distinct, the sum has binary expansion whose `1` digits occur exactly in
positions `a_n`; there are no binary carries.

The hypothesis forces the gaps `a_{n+1}-a_n` to be unbounded. Indeed, if all sufficiently late gaps
were bounded by a constant `G`, then `a_n <= a_1 + G(n-1)`, contradicting the unbounded limsup of
`a_n/n`.

A rational real number has an eventually periodic base-2 expansion. An infinite eventually periodic
binary expansion that contains infinitely many `1` digits has bounded gaps between successive `1`
digits: after the preperiod, one repeats a finite block containing a `1`. Our expansion has infinitely
many `1` digits and unbounded `1`-gaps. Therefore it is not eventually periodic and the sum is
irrational.

## Scope boundary

This does **not** solve Erdős #247. The canonical problem asks for **transcendence** under this
sparsity hypothesis. The recovered campaign explicitly stops at irrationality. In particular,
`a_n=n^2` already satisfies the hypothesis and leads to the much harder theta-value
`sum 2^{-n^2}` at `q=1/2`; no transcendence claim is made here.

The September novelty audit labelled this theorem `CANDIDATE_NOVEL_PARTIAL`: targeted searches did
not locate the exact statement, but specialist/MathSciNet review was not completed. Historical
priority is therefore **unresolved**.

## Companion exact density equivalence

If `A(N)=#{n:a_n<=N}`, then for strictly increasing `a_n`,

\[
\limsup a_n/n=\infty
\quad\Longleftrightarrow\quad
\liminf A(N)/N=0.
\]

One direction evaluates at `N=a_n`; the other takes `n=A(N)+1` along a sequence where `A(N)/N`
tends to zero. This equivalence was also recovered during the audit after a stale workflow label
had incorrectly marked it false.

## License

Apache-2.0 for repository-authored material.
