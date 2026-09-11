# Erdős #835 — SQS(20) residual completion and rigidity package

**Author:** Jared Wilder  
**Campaign:** J-SPACE v0.6/v0.7, rounds 21–40  
**Public estate release:** 2026-09-11

## Flagship status

**Erdős #835 remains OPEN.** The `k=16` prime-regime case survives. No large set of 17 SQS(20) is constructed or ruled out here.

The campaign nevertheless produced an exact graph-colouring formulation of partial-large-set completion and several finite rigidity theorems for an explicit reconstructed classical 15-pack of pairwise-disjoint SQS(20).

## Residual completion graph

Let `P={S_1,...,S_m}` be pairwise block-disjoint Steiner quadruple systems on a `v`-point set, and put

`q=(v-3)-m`.

Let `R(P)` have one vertex for every uncovered 4-subset, with two vertices adjacent exactly when the corresponding 4-subsets share a triple.

Then

> **`P` completes to a large set of SQS(v) iff `chi(R(P))=q`.**

The exact parameters are

`|V(R)| = q*C(v,3)/4`,

`deg R = 4(q-1)`,

`|E(R)| = C(v,3) C(q,2)`.

The proof is elementary: every triple has exactly `q` uncovered containing blocks, giving a `K_q` fibre. A completion colors blocks by the missing SQS; conversely a proper `q`-coloring uses every color exactly once on each triple fibre and therefore each color class is an SQS.

See `RESIDUAL-GRAPH-THEOREM.md`.

## Exact reconstruction of the classical 15-pack

The campaign deterministically reconstructed 15 pairwise-disjoint SQS(20):

- 15 systems;
- 285 blocks per system;
- 4,275 covered four-sets;
- each system covers each of the 1,140 triples exactly once;
- pairwise block-disjoint.

For the full 15-pack, `q=2`. Its residual graph has

- 570 vertices;
- 1,140 edges;
- degree 4 everywhere;
- component sizes `250, 25×12, 5×4`.

The four 5-vertex components are literal `K5`s, so the graph is not bipartite. Therefore this specific 15-pack cannot be completed simply by adding the two missing SQS(20).

More strongly, the four `K5`s use four-sets omitted by all 15 systems. If a hypothetical large set retains `m` of these systems, the obstruction survives while `q=17-m`; proper coloring requires `q>=5`, hence

`m<=12`.

So any large set containing members of this explicit 15-pack must replace **at least three** constituents. This is the campaign's **repair-radius >= 3** theorem.

## Five-colour repair wall

Sacrifice three systems and retain 12. Then `q=5`. One representative residual graph has

- 1,425 vertices;
- 11,400 edges;
- degree 16;
- 1,140 distinguished `K5` triple fibres.

The retained 12-pack extends to a large set exactly when this graph is 5-colorable. This replaces an 82,365-binary full large-set MILP by a 1,425-vertex exact graph-coloring problem.

No 5-coloring or impossibility certificate was obtained; this branch remains **INCONCLUSIVE**.

## Further exact rigidity from rounds 31–40

The later campaign block proves two finite theorems for the explicit 15-pack:

1. **One-coordinate rigidity.** Freeze any 14 constituents. The only SQS(20) disjoint from those fourteen inside the freed constituent plus the 570 holes is the original fifteenth system itself.
2. **Complete pair-trade geometry.** Among all 105 constituent pairs there are exactly two Steiner 3-trade component profiles: 30 same-construction-row pairs have per-side volumes `(30,30,225)`, while 75 cross-row pairs form one indecomposable per-side volume-285 component.

These and the spectral/trade-space interpretation are recorded in `P15-RIGIDITY-AND-TRADES.md`.

## Novelty boundary

The Etzion–Hartman 15-pack construction/lower bound, general Steiner-trade theory and the open status of large sets of SQS are prior art. The source campaign found no targeted hit for the exact one-coordinate rigidity theorem, the complete pair-trade profile of this particular pack, or the residual-completion/repair-radius packaging. That is **not a priority certificate**; specialist design-theory review is still required.

The public purpose of this directory is to expose the exact mathematics while preserving that boundary.