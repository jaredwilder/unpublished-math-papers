# Erdős #1104 — monotonicity of the triangle-free chromatic extremum

**Author:** Jared Wilder  
**Public extraction:** 2026-09-11  
**Status:** exact elementary structural lemma.

Let `f(n)` be the maximum chromatic number of a triangle-free graph on `n` vertices.

## Theorem

For every `n>=1`,

`f(n+1) >= f(n)`.

## Proof

Choose an `n`-vertex triangle-free graph `G` with chromatic number `f(n)`. Add one isolated vertex to obtain `G'` on `n+1` vertices.

Adding an isolated vertex creates no triangle and does not change the chromatic number. Hence

`chi(G')=chi(G)=f(n)`.

By maximality of `f(n+1)`,

`f(n+1)>=chi(G')=f(n)`.

## Scope

This monotonicity lemma carries no asymptotic estimate by itself; it is reusable infrastructure for the parent extremal problem.
