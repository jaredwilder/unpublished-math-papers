# Erdős #247 — sparse-position irrationality in every integer base

**Author:** Jared Wilder  
**Recovered from:** September 2026 MSL audit and final synthesis  
**Public extraction:** 2026-09-11

## Theorem

Let

\[
a_1<a_2<a_3<\cdots
\]

be a strictly increasing sequence of positive integers, and let `b>=2` be any integer base. If

\[
\limsup_{n\to\infty}\frac{a_n}{n}=\infty,
\]

then

\[
\boxed{\sum_{n\ge1}b^{-a_n}\notin\mathbb Q.}
\]

The previously released base-2 statement is therefore only the first member of an all-integer-base theorem.

## Proof

Because the exponents are distinct, the base-`b` expansion of the sum has digit `1` exactly in the
positions `a_n` and digit `0` elsewhere; there are no carries because every occupied digit is 1 and
`1<b`.

The hypothesis forces the gaps `a_{n+1}-a_n` to be unbounded. Indeed, if all sufficiently late gaps
were bounded by a constant `G`, then

\[
a_n\le a_1+G(n-1),
\]

contradicting the unbounded limsup of `a_n/n`.

A rational real number has an eventually periodic expansion in every integer base. An infinite
eventually periodic digit string containing infinitely many `1` digits has bounded gaps between
successive `1` positions: after the preperiod, a finite repeating block containing a `1` recurs at
bounded spacing. Our expansion has infinitely many `1` digits and unbounded `1`-gaps. Hence it is
not eventually periodic and the sum is irrational.

## Companion density equivalence

If

\[
A(N)=\#\{n:a_n\le N\},
\]

then for strictly increasing `a_n`,

\[
\boxed{
\limsup a_n/n=\infty
\quad\Longleftrightarrow\quad
\liminf A(N)/N=0.
}
\]

One direction evaluates at `N=a_n`, where `A(a_n)=n`. Conversely, along integers `N_j` with
`A(N_j)/N_j->0`, put `n_j=A(N_j)+1`; then `a_{n_j}>N_j` and

\[
\frac{a_{n_j}}{n_j}>\frac{N_j}{A(N_j)+1}\to\infty.
\]

This equivalence was recovered after a stale workflow label had incorrectly marked it false.

## Scope boundary

This does **not** solve Erdős #247. The canonical problem asks for **transcendence** under the same
sparsity hypothesis. This theorem proves irrationality only. In particular `a_n=n^2` satisfies the
hypothesis and leads already in base 2 to a theta-type value whose transcendence is far beyond the
argument here.

The September novelty audit labelled the exact-hypothesis irrationality result a candidate novel
partial after targeted searches failed to find the same statement. The all-base strengthening came
from the final synthesis. Specialist/MathSciNet review was not completed, so historical priority
remains **unresolved**.

## License

Apache-2.0 for repository-authored material.
