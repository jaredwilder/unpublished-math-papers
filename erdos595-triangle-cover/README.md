# Erdős #595 — triangle-cover theorem refinery

**Author:** Jared Wilder  
**Source date:** 2026-08-04  
**Public release:** 2026-09-11

This directory publishes a recovered pure-mathematics theorem bank from the Erdős #595 campaign.

## Flagship problem boundary

For a graph `G`, let `tc(G)` be the least cardinal number of triangle-free subgraphs whose edge sets cover `E(G)`. The campaign's flagship asks whether there exists a `K4`-free graph with

`tc(G) > aleph_0`.

**This release does not claim the flagship problem is solved.**

The source theorem refinery contains **65 theorem cards** (`T01`–`T66`, with no `T57` card):

- 60 `PROVED_IN_PACKET`;
- 1 `PROVED_USING_STANDARD_COMPACTNESS`;
- 1 `PROVED_FROM_FINITE_FOLKMAN_INPUT`;
- 1 `SOURCE_DERIVED_PRIOR_ART_RECHECK_REQUIRED`;
- 1 `CONDITIONAL_REDUCTION`;
- 1 `REFUTED_ROUTE`.

Historical novelty and Lean verification were both **UNRUN** in the source. Publication does not upgrade either.

## Highest-leverage results

The theorem bank includes, among other things:

- an exact blocker/triangle-transversal centeredness duality for `tc(G)`;
- an exact formula for the bipartite-cover cardinal `bc(G)` in terms of chromatic number;
- the implication `tc(G)>kappa => chi(G)>2^kappa` and hence a strict continuum-size barrier for any #595 witness;
- cofinality restrictions on minimal witness cardinalities;
- extraction of a countable `K4`-free exact-`aleph_0` core from any hypothetical uncountable-cover witness;
- a construction of a connected, locally finite, one-ended exact-`aleph_0` core from standard finite Folkman inputs;
- product-coloring and chromatic-dispersion lower bounds for `tc(G)`;
- the exact equivalence between `K4`-freeness of `G` and Berge-`C3`-freeness of its triangle hypergraph `Tri(G)`;
- exact endpoint-representation criteria for which 3-uniform hypergraphs arise as triangle hypergraphs of graphs;
- finite NP membership for triangle-hypergraph realizability;
- a preserved negative result showing that triangle multiplicity along an edge is unbounded even in finite `K4`-free graphs.

## Important correction / negative gold

The bank explicitly kills the route claiming a fixed upper bound on the number of triangles containing an edge in a `K4`-free graph. Book graphs give arbitrarily large triangle multiplicity while staying `K4`-free. That route is permanently marked `REFUTED_ROUTE` rather than silently discarded.

## Files

- `THEOREM-LEDGER.md` — compact 65-card status-preserving public ledger.

A separate external-verification packet exists in the estate for an earlier/self-growth subset. It is being treated as provenance/audit material rather than as authority to upgrade the source cards automatically.