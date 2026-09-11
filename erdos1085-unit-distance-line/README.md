# Erdős #1085 — exact one-dimensional unit-distance extremum

**Author:** Jared Wilder  
**Public extraction:** 2026-09-11  
**Status:** exact solved dimension-1 stratum.

Let `f_1(n)` be the maximum number of unit-distance pairs among `n` distinct points on the real line.

## Theorem

For every `n>=1`,

`f_1(n)=n-1`.

## Proof

Order the points as `x_1<...<x_n`. In the unit-distance graph, every connected component is a path: from any point there can be at most one neighbor at distance `1` to the left and at most one to the right, and a cycle cannot be embedded in the line with every edge of length `1` between distinct ordered points.

Thus the unit-distance graph is a forest, so it has at most `n-1` edges.

Equality is attained by the arithmetic progression

`0,1,...,n-1`,

whose `n-1` consecutive pairs are all at unit distance.

## Scope

This solves only dimension `1`. Higher-dimensional unit-distance extremal behavior is a different problem.
