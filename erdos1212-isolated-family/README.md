# Erdős #1212 — infinitely many isolated admissible vertices

**Author:** Jared Wilder  
**Recovered from:** September 2026 theorem audit  
**Public extraction:** 2026-09-11

## Setup

The campaign studies the coprime lattice graph in which vertices are coprime integer pairs and
adjacency is by a unit coordinate move. The admissible induced subgraph imposes the source condition

\[
\min(x,y)>1.
\]

## Theorem

For every integer `k>=2`, the vertex

\[
\boxed{(2,3^k)}
\]

is isolated in the admissible induced graph.

Equivalently, before imposing `min(x,y)>1`, its only coprime unit-coordinate neighbor is

\[
(1,3^k).
\]

Thus the admissible graph contains infinitely many singleton connected components.

## Proof

The four unit-coordinate candidates adjacent to `(2,3^k)` are

\[
(1,3^k),\quad(3,3^k),\quad(2,3^k-1),\quad(2,3^k+1).
\]

Because `k>=2`, `3` divides `3^k`, so

\[
\gcd(3,3^k)>1.
\]

Both `3^k-1` and `3^k+1` are even, hence

\[
\gcd(2,3^k\pm1)=2.
\]

Therefore the only coprime neighbor in the full lattice graph is `(1,3^k)`. That vertex is removed
by the admissibility condition `min(x,y)>1`, so `(2,3^k)` has degree zero in the induced graph.

## Scope boundary

This is a structural obstruction family, not a solution of Erdős #1212. It shows that naive global
connectivity is impossible and that infinitely many dead-end components exist; it does **not** rule
out another infinite component satisfying the target conditions.

The September prior-art audit did not locate this exact `3^k` degree-one/dead-end family in the
searched #1212 material. The safe novelty status is **apparently unrecorded after targeted search**.

## License

Apache-2.0 for repository-authored material.
