# Erdős #74 — bipartite defect and infinite chromatic number

This directory is the human-facing entry point for a 16-theorem Lean packet on the rate-free boundary of Erdős Problem #74.

The problem asks whether, for every function `f(n) → ∞`, there is a graph of infinite chromatic number whose finite `n`-vertex subgraphs can all be made bipartite by deleting at most `f(n)` edges.

The formal source is preserved at
`jaredwilder/erdos-campaign-archive/campaigns/erdos74-close-2026-09-05/lean/Attack01.lean`.

## Formal results

The Lean development proves:

- if every finite `n`-vertex subgraph has bipartite edge-deletion defect bounded by one constant `B`, then the whole graph is finitely colorable, with the explicit bound `χ(G) ≤ 2^(B+1)`;
- therefore a graph of infinite chromatic number has unbounded finite-subgraph bipartite defect;
- every bounded function `f` fails the desired conclusion;
- for monotone `f`, failure to tend to infinity implies boundedness, so the hypothesis `f(n) → ∞` is genuinely necessary;
- on finite vertex sets, deletion defect zero is equivalent to bipartiteness.

The file also proves why the finite-vertex guard in the formalized defect definition is necessary: `Set.ncard` assigns cardinality zero to infinite sets, so without the guard an infinite deleted edge set could spuriously register cost zero.

## Formal trust footprint

The campaign receipt records:

- Lean compile exit `0`;
- 16 checked named theorems;
- zero `sorryAx` occurrences;
- one axiom footprint throughout: `[propext, Classical.choice, Quot.sound]`.

## Mathematical position

This packet identifies the exact rate-free boundary: infinite chromatic number forces the defect function to be unbounded.

The substantive open question begins after that boundary: how slowly may the defect grow while still allowing infinite chromatic number? The present formalization does not establish such a growth rate.

The campaign record also notes that the explicit `2^(B+1)` coloring bound is elementary and nonoptimal; a sharper classical bound exists but is not formalized here.

## Topology

This is currently a compact formal subject packet rather than a standalone-repository-scale program. If it grows to include the quantitative constructions or negative theorems governing the true rate problem, it should graduate to a dedicated Erdős #74 repository.
