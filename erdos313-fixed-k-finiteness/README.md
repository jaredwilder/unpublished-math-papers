# Erdős #313 — fixed-k finiteness for reciprocal-prime solutions

**Author:** Jared Wilder  
**Recovered status:** `MATHEMATICALLY_AUDITED_LEAN_READY`  
**Public extraction:** 2026-09-11

## Theorem

Fix a positive integer `k`. Consider solutions in distinct primes

\[
p_1<\cdots<p_k
\]

and a positive integer `m` of

\[
\sum_{i=1}^{k}\frac1{p_i}=1-\frac1m.
\]

For each fixed `k`, there are only finitely many such solutions.
Consequently, any infinite family of solutions to the surrounding problem must have unbounded `k`.

## Step 1 — the denominator is forced

Let

\[
P=\prod_{i=1}^k p_i.
\]

Rewrite the equation as

\[
\sum_i\frac1{p_i}+\frac1m=1.
\]

Clearing denominators by `mP` gives

\[
m\sum_i\frac{P}{p_i}+P=mP.
\]

Reduce modulo a fixed `p_i`. Every term in the sum except

\[
m\frac{P}{p_i}
\]

vanishes modulo `p_i`, while `P/p_i` is invertible modulo `p_i`. Therefore

\[
p_i\mid m
\]

for every `i`, so

\[
P\mid m.
\]

On the other hand, the cleared identity gives

\[
P=m\left(P-\sum_iP/p_i\right),
\]

so

\[
m\mid P.
\]

Hence

\[
\boxed{m=P.}
\]

The equation is therefore equivalent to

\[
\boxed{\sum_{i=1}^k\frac1{p_i}+\frac1P=1.}
\]

## Step 2 — finite branching

Since

\[
1<\sum_{i=1}^k\frac1{p_i}+\frac1{p_1}
\le\frac{k+1}{p_1},
\]

we obtain a finite upper bound on `p_1`; the recovered campaign used the coarser convenient bound

\[
p_1\le k+1.
\]

More generally, after fixing

\[
p_1,\ldots,p_j,
\]

let the remaining positive residual be

\[
R_j=1-\sum_{i=1}^{j}\frac1{p_i}>0.
\]

Because

\[
p_{j+1}\le p_{j+2}\le\cdots\le p_k,
\]

we have

\[
R_j
=\sum_{i=j+1}^{k}\frac1{p_i}+\frac1P
\le\frac{k-j+1}{p_{j+1}},
\]

up to the harmless final product term absorbed in the same coarse count. Thus

\[
\boxed{p_{j+1}\le\frac{k-j+1}{R_j}.}
\]

At every depth there are therefore only finitely many possible next primes. Since the recursion has fixed depth `k`, only finitely many prime tuples can occur.

## Scope boundary

This theorem does not prove or disprove the existence of infinitely many solutions when `k` is allowed to grow. It proves that **fixed-k mechanisms cannot generate an infinite family**.

The larger #313 campaign contained failed grand routes as well as true child theorems. This statement was separately retained by the September canonical audit as a universal fixed-k result.

## Novelty boundary

No historical priority claim is made here without a specialist Egyptian-fraction / reciprocal-prime literature review.

## License

Apache-2.0 for repository-authored material.
