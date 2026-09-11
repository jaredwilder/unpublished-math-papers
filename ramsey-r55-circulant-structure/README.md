# R(5,5) — exact structure of the 41-vertex circulant Ramsey graph

**Author:** Jared Wilder  
**Campaign:** unattended R55, 2026-09-03/04  
**Public estate release:** 2026-09-11

## Global boundary first

This directory does **not** solve `R(5,5)` and does not improve the world bound. The audited literature state in the source packet is

`43 <= R(5,5) <= 46`.

The graph studied here is an old 41-vertex circulant Ramsey graph; the contribution of this release is the exact structural mathematics recovered and mined around that graph, plus a sharp non-extension theorem.

## The graph

Let

`G = Cay(Z_41,S)`

with

`S = ±{1,2,3,5,7,10,13,15,16,17}`.

Equivalently,

`S={1,2,3,5,7,10,13,15,16,17,24,25,26,28,31,34,36,38,39,40}`.

Direct verification gives:

- no `K5`;
- no independent 5-set;
- `omega(G)=alpha(G)=4`.

Thus `G` is a valid 41-vertex `(5,5)` Ramsey graph. This only proves `R(5,5)>=42`, weaker than the known global lower bound.

## Complete classification inside the 41-vertex circulant family

`Z_41` has 20 inverse-paired positive distance classes. Exhaustion establishes:

1. there is no valid circulant `(5,5)` graph using at most 9 positive distance classes;
2. by complementation there is none using at least 11 classes;
3. among all `C(20,10)=184756` half-density circulants, exactly **20** labelled connection sets survive;
4. those 20 sets form one orbit under multiplication by units of `Z_41`;
5. the multiplier stabilizer of the displayed `S` is exactly `{+1,-1}`.

Therefore:

> **Up to multiplier/affine isomorphism, there is exactly one circulant `(5,5)` Ramsey graph on 41 vertices.**

Every such graph is 20-regular.

The underlying connection set appears in earlier literature, so this classification is published here with **novelty unresolved**, not as a priority claim.

## Explicit self-complementation

Multiplication by `9` satisfies

`9S = Z_41^× \ S`

and

`9^2 = -1 (mod 41)`.

Hence

`x -> 9x (mod 41)`

is an explicit graph-to-complement isomorphism `G ≅ complement(G)`.

The only multiplicative units preserving `S` are `±1`; the only units swapping `S` with its complement are `±9`.

Thus the obvious affine graph automorphisms have order `41*2=82`, while the full affine color-symmetry group has order `41*4=164`.

## Exact chromatic structure

The Ramsey property gives `alpha(G)=4`, so

`chi(G) >= ceil(41/4)=11`.

For `k=0,...,9`, define

`C_k={4(4k+1),4(4k+2),4(4k+3),4(4k+4)} mod 41`.

These ten four-sets partition the 40 nonzero residues, and their pair differences are among `±4,±8,±12`, none of which lies in `S`. Hence the `C_k` are independent; adding `{0}` gives an 11-coloring. Therefore

`chi(G)=11`.

Moreover `G-{0}` is 10-colorable by the ten `C_k`; the independence bound gives the reverse inequality. Since `G` is vertex-transitive,

> `chi(G-v)=10` for every vertex `v`.

So `G` is 11-chromatic and vertex-critical.

The stronger circular/fractional statement is

`chi_f(G)=chi_c(G)=41/4`.

Indeed vertex transitivity gives `chi_f=41/4`, and multiplication by `31=4^{-1} mod 41` gives an explicit `(41,4)` circular coloring.

## Exact combinatorial fingerprint

The audited enumeration gives:

- vertices: `41`;
- regular degree: `20`;
- edges: `410`;
- triangles: `1230`;
- `K4`s: `1025`;
- independent 4-sets: `1025`;
- `K5`s: `0`;
- independent 5-sets: `0`.

Hence the clique polynomial is

`1 + 41x + 410x^2 + 1230x^3 + 1025x^4`,

and by self-complementarity it is also the independence polynomial.

Every vertex lies in exactly `90` triangles and `100` copies of `K4`.

The graph is not strongly regular: common-neighbor counts are not constant on all edges/nonedges.

## Automorphism group

A direct automorphism census gives exactly 82 automorphisms. The theoretical identification is

`Aut(G) ≅ D_41`.

Translations act regularly; for a nontrivial prime-degree Cayley graph the Burnside prime-degree argument places the automorphism group inside `AGL(1,41)`, and the only graph-preserving multipliers are `±1`.

## Stronger results in this directory

- `ONE-VERTEX-EXTENSION.md`: the unique 41-vertex circulant class cannot be extended by **one arbitrary new vertex** to a 42-vertex `(5,5)` Ramsey graph.
- `SPECTRAL-AND-CODING.md`: exact circular/fractional coloring, strong-square code, Shannon capacity, dual `K4`/independent-set resolutions, and the exact spectral symmetry polynomial.
- `SAT-INTERFACE.md`: the honest finite `n=42/43` global Ramsey decision interface and its two unfilled proof obligations.

## Novelty / literature discipline

The graph itself and the 40/41 circulant constructions are not new. The source audit specifically refused to claim novelty for the exact invariants without deeper catalog/original-source checking. Focused searches did not locate explicit prior statements of the one-isomorphism-class result, the one-vertex nonextension theorem, or `chi_c(G)=41/4`, but that absence is not a novelty proof.

The release therefore establishes provenance and makes the mathematics inspectable without claiming a new global Ramsey bound or historical priority.