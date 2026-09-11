# Result B — Product-free and geometric-progression-free subsets of `[50]`

## Theorem

Let `A⊆{1,…,50}`. Assume:

1. no `x,y,z∈A` satisfy `xy=z`, with repetitions allowed;
2. no distinct `a<b<c` in `A` satisfy `b²=ac`.

Then `|A|≤35`. The bound is sharp. There are exactly 240 extremal sets.

## Exact reduction

Create one forbidden hyperedge for every product relation and every nontrivial three-term geometric progression. A valid set is an independent set in this hypergraph. Its complement is a transversal. Therefore

\[
\alpha=50-\tau.
\]

Two independent Python algorithms and one independent C implementation prove `τ=15`, hence `α=35`, while enumerating all 240 minimum transversals/extremal independent sets.

## Bound objects

The theorem certificate includes:

- all 149 forbidden hyperedges through the declared generator;
- minimum transversal 15;
- maximum 35;
- 240 extremizers;
- canonical digest `cea2d1f707e94d388369a9c61030dd3ce9908b8a0b981419bb90f7cfa4721188`;
- a concrete witness;
- the exact intersection core of all extremizers.