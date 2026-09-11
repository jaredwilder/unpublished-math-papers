# Erdős #913 — distinct prime exponents force a powerful neighbor

**Author:** Jared Wilder  
**Public extraction:** 2026-09-11

Let

\[
n(n+1)=\prod_i p_i^{e_i}
\]

and suppose the nonzero exponents `e_i` are pairwise distinct.

## Theorem

Then at least one of `n,n+1` is a powerful number: every prime dividing that number occurs to exponent at least 2.

Consequently the number of such candidate integers `n<=X` is

\[
\boxed{O(\sqrt X)}.
\]

## Proof of the structural statement

Because `gcd(n,n+1)=1`, the prime factors of `n` and `n+1` are disjoint. If both `n` and `n+1` had a prime occurring to exponent exactly 1, then the full factorization of `n(n+1)` would contain the exponent 1 at least twice, contradicting pairwise distinctness of the exponents.

Therefore at least one of `n,n+1` has no exponent equal to 1, hence is powerful.

## Counting consequence

Every powerful integer has a representation

\[
m=a^2b^3
\]

with `b` squarefree. Hence the number of powerful `m<=X` is at most

\[
\sum_{b\le X^{1/3}}\sqrt{X/b^3}
\le
\sqrt X\sum_{b\ge1}b^{-3/2}
=O(\sqrt X).
\]

If a candidate `n` has either `n` or `n+1` powerful, the number of candidates up to `X` is therefore also `O(sqrt X)`.

## Scope

This is a sparsity reduction, not a classification of all candidates and not a solution of the parent problem. No historical novelty claim is made here.
