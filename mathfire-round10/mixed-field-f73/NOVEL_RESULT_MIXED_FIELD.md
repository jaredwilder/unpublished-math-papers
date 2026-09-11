# Round Ten Novel Result II

## A mixed additive–multiplicative extremal classification in `F_73`

Let `A` be a subset of the nonzero elements of the prime field `F_73`.

Require all three conditions:

1. **sum-free:** there are no `x,y,z in A`, with repetitions allowed, satisfying `x+y=z`;
2. **product-free:** there are no `x,y,z in A`, with repetitions allowed, satisfying `xy=z`;
3. **nontrivial 3-AP-free:** there are no three distinct `a,b,c in A` satisfying `a+c=2b`.

All equations are in `F_73`.

## Theorem

\[
\boxed{|A|\le 12.}
\]

The bound is sharp. Exactly three subsets attain size 12:

```text
{13,15,19,31,33,36,37,40,42,54,58,60}
{10,22,24,28,33,36,37,40,45,49,51,63}
{2,3,10,19,24,31,42,49,54,63,70,71}
```

The equivalent minimum forbidden-hypergraph transversal has size 60. The compiled forbidden hypergraph has 7,422 distinct edges.

The canonical SHA-256 identity of the complete ordered extremal layer is:

```text
50842bb25cfc9f387b70077733000817f4368e16ad29dc9cd010c3ab4fe6dd8a
```

## Exact proof mechanism

Each forbidden equation contributes a one-, two-, or three-vertex hyperedge. A valid set is exactly an independent set of the resulting hypergraph.

The primary solver removes forced forbidden vertices, compiles two-vertex constraints into a compatibility graph, retains three-vertex constraints as pair-conditioned exclusions, performs exact branch-and-bound, uses greedy coloring as a valid upper bound, and enumerates the complete maximum layer. It proves maximum 12 and enumerates exactly three extremizers after 271,416 search nodes.

## Independent verification

`verification/mixed_field_p73_independent.cpp` shares no MathFire package code. It independently reconstructs every forbidden relation, runs a separate C++ exact search, and returns the same 7,422 forbidden edges, maximum 12, exactly three extremizers, 271,416 search nodes, and identical extremal sets.

## Authority boundary

This is a complete finite theorem for the stated simultaneous constraints in `F_73^×`. It is not an asymptotic theorem for arbitrary primes.