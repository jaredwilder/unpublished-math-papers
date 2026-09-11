# Erdős #968 — exact prime-ratio monotonicity rewrite

**Author:** Jared Wilder  
**Public extraction:** 2026-09-11

Let `p_n` be the `n`th prime and put

\[
u_n=\frac{p_n}{n},\qquad d_n=p_{n+1}-p_n.
\]

## Exact equivalence

\[
\boxed{
u_n<u_{n+1}
\iff
n d_n>p_n
\iff
 d_n>\frac{p_n}{n}.}
\]

## Proof

Starting from

\[
\frac{p_n}{n}<\frac{p_{n+1}}{n+1},
\]

cross-multiplication gives

\[
(n+1)p_n<n p_{n+1},
\]

or equivalently

\[
p_n<n(p_{n+1}-p_n)=n d_n.
\]

Dividing by `n` yields the final form.

## Scope

This is an exact algebraic reformulation. Questions about positive density or frequency of such indices become prime-gap questions and are not answered by this identity alone.
