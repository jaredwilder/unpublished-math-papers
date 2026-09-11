# Erdős #168 — a two-thirds construction avoiding `{n,2n,3n}`

**Author:** Jared Wilder  
**Public extraction:** 2026-09-11  
**Status:** exact constructive lower bound.

## Theorem

For every positive integer `N`, the set

`A_N = {1<=m<=N : 3 does not divide m}`

contains no complete triple of the form

`{n,2n,3n}`.

Moreover

`|A_N| = N-floor(N/3) = ceil(2N/3)`.

Thus any extremal function asking for the largest subset of `[N]` avoiding every `{n,2n,3n}` satisfies the lower bound

`F(N) >= ceil(2N/3)`.

## Proof

Every triple `{n,2n,3n}` contains the element `3n`, which is divisible by `3`. But `A_N` contains no multiple of `3`. Hence no such triple is entirely contained in `A_N`.

The cardinality follows by removing the `floor(N/3)` multiples of `3` from `[N]`.

## Scope

This is a construction and lower bound only. No matching upper bound is asserted here.
