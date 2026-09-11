# Erdős #579 — common-neighborhood reduction for `K_{2,2,2}`-free graphs

**Author:** Jared Wilder  
**Public extraction:** 2026-09-11

## Theorem

If a graph `G` contains no copy of `K_{2,2,2}`, then for every pair of vertices `u,v`, the graph induced by their common neighborhood

\[
G[N(u)\cap N(v)]
\]

is `K_{2,2}`-free.

## Proof

Suppose four vertices in `N(u)∩N(v)` span a `K_{2,2}` with bipartition `{a,b}` and `{c,d}`. Then the three two-vertex classes

\[
\{u,v\},\qquad\{a,b\},\qquad\{c,d\}
\]

have every required cross-edge: `a,b,c,d` are all adjacent to both `u` and `v`, and the middle four contain the `K_{2,2}` cross-edges. This is a copy of `K_{2,2,2}`. Whether `u` and `v` are adjacent is irrelevant because containment is non-induced.

Contradiction.

## Scope

This is a universal structural reduction only. It does not settle the parent extremal problem by itself.
