# Erdős–Gyárfás power-of-two cycle theorem forge

**Author:** Jared Wilder  
**Campaign:** `power-cycle-terminal-encirclement-v2`  
**Source date:** 2026-08-04  
**Public extraction:** 2026-09-10/11

## Flagship status: OPEN

The source-bound conjecture is

\[
\delta(G)\ge3\Longrightarrow G\text{ contains a cycle of length }2^k\text{ for some }k\ge2.
\]

This repository section **does not claim the Erdős–Gyárfás conjecture is solved**.

## Estate size

The V2 forge contains **202 exact theorem cards**:

- `PROVED_IN_PACKET`: 120;
- `PROVED_FROM_SOURCE_PREMISE`: 1;
- `PROVED_USING_STANDARD_THEOREM`: 2;
- `SOURCE_DERIVED`: 2;
- `CONDITIONAL_DEDUCTION`: 7;
- `COMPUTATIONALLY_CERTIFIED`: 16;
- `PROVED_NEGATIVE_THEOREM`: 9;
- `REFUTED_ROUTE`: 9;
- `UNPROVED_CHECKABLE_TARGET`: 34;
- `WITHDRAWN_UNSUPPORTED`: 2.

The bank is split into the same families used by the source campaign:

- `MC` — minimum-counterexample / sparse-criticality structure;
- `CY` — C4-free and dyadic-avoidance lemmas;
- `DS` — cubic/high-degree census and bounded defect kernels;
- `TR` — perfect-matching transition quotients and exchange congruences;
- `BR` — boundary-routing / switching-cycle lemmas;
- `NG` — proved negative theorems and dead routes;
- `TG` — explicit search targets;
- `OE` — ordinary-ear theory;
- `CS` — cubic suppression / Mersenne certificates;
- `LC` — lens chains and mixed-route subset-sum structure;
- `HP` — packet hypergraphs, CNF reduction, and finite obstruction certificates.

## Authority vocabulary

`PROVED_IN_PACKET` means the campaign supplies an explicit mathematical proof route, but the statement has not thereby been upgraded to kernel verification or historical novelty.

`COMPUTATIONALLY_CERTIFIED` means the frozen finite statement was replayed by the campaign's verifier.

`UNPROVED_CHECKABLE_TARGET` is a theorem-search obligation, **not a result**.

`Lean mission` names in the source are formalization targets, **not Lean receipts**.

Historical novelty is `UNRUN` card-by-card unless separately adjudicated.

## Strong V2 finite facts

The replay-certified packet layer records:

- exact `N=0` candidate set: **13** edges;
- exact minimal forbidden hypergraph: **56** hyperedges = 48 rank-2 + 8 rank-3;
- a compact human `N=0` contradiction;
- complete one-hub census: **21** configurations, all candidate-isolated;
- complete two-hub census: **24** configurations = 16 nonadjacent + 8 adjacent, all candidate-isolated;
- fixed-packet realization lower bound: **at least 3 added vertices**;
- deficit hub-conflict graph: **40** edges, independence number **4**, unique maximum independent set;
- exact two-hub deficit coverage: **7**, unique up to hub order;
- canonical candidate-isolation witness SHA-256: `fe2adefe67664121baaf3b8b4a6cf7cafaa5a62ebcc7c8fb2a69ca41aa2ac179`.

These are finite packet statements. They do not imply the full conjecture.

## Strong structural chains

Among the proved-in-packet mathematics are:

- proper-set `(2,3)` sparsity and arboricity-two structure for a minimum counterexample;
- C4-free second-neighborhood expansion;
- an exact cubic-surplus identity and bounded cubic-defect kernel;
- a quotient representation of the equality branch and its elimination;
- perfect-matching alternating-cycle exchange congruences (`odd-lock` theory);
- ordinary-ear double barriers and multi-cycle connector packets;
- cubic suppression producing `2^k+1` near-dyadic cycles and `2^k-1` Mersenne neighbor paths;
- ordered lens decomposition, mixed-route cubes, and dyadic subset-sum criteria;
- canonical forbidden-hypergraph / monotone-CNF completion equivalence;
- exact `N=0,1,2` packet obstruction certificates.

## Release layout

The card files preserve, for every card, its ID, source status, authority class, title, exact statement, dependencies when recorded, and claim hash. This is intentionally more complete than a “best results” summary, while remaining much easier to audit than the 4,390-line internal theorem-forge transcript.

Negative theorems, refuted routes, conditional deductions, and open targets remain visible. Nothing is silently promoted by adjacency to a proved card.
