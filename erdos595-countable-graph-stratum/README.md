# Erdős #595 — the countable-graph stratum is trivial

**Author:** Jared Wilder  
**Public extraction:** 2026-09-11

## Theorem

Every countable graph is a countable union of triangle-free graphs.

## Proof

Enumerate the edges

\[
E(G)=\{e_1,e_2,\ldots\}
\]

(finite graphs are included). For each edge `e_i`, let `G_i` be the graph consisting of that single edge and all vertices needed to regard it as a subgraph of `G`. A single-edge graph is triangle-free, and

\[
G=\bigcup_i G_i
\]

at the level of edge sets.

Thus any genuinely difficult witness for a statement asserting that a graph cannot be covered by countably many triangle-free subgraphs must be uncountable.

## Scope

This is a cardinality reduction only. It does not solve the uncountable parent problem.
