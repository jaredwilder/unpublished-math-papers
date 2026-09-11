# Erdős #738 Encirclement Theorem Bank
**Date:** 2026-08-04  
**Mode:** theorem-generation pass from the encirclement/RSI campaign  
**Claim boundary:** every item marked `PROVED_IN_PACKET` has an elementary proof route supplied here, but **historical novelty is unknown** until the user’s novelty checker clears the exact statement. Items marked `UNPROVED_CHECKABLE_TARGET` are finite theorem-search obligations, not results.

## Source boundary
The campaign target is Erdős Problem #738 / the triangle-free case of Gyárfás–Sumner. The literature inputs used to define the frontier are:
- Tung Nguyen, Alex Scott, Paul Seymour, **A note on the Gyárfás–Sumner conjecture**, arXiv:2302.08922 — path-induced, level-stable, type-uniform rooted-tree copies.
- Tung H. Nguyen, **On polynomially high-chromatic pure pairs**, arXiv:2504.21127 — complete/anticomplete pair machinery and the complete-pair formulation.
- The attached Math Encirclement Engine plan supplied the authority split: search proposals remain separate from Court-verified claims.

## Inventory
- **62 proof-backed theorem statements/schemas**
- **12 finite, executable theorem-search targets**
- Two strongest paper-shaped packages: **Extremal Type-Tensor Theory** and **Mixing–Spider Characterization**.

## Highest-value novelty checks
1. **T06 — Sharp Slice Active-Type Bound.** Let d≥3 and let a complete ordered d-ary rooted tree of height k be embedded path-induced, level-stable, and type-uniform in a triangle-free graph. For c<a,b≤k, let A_c(a,b)=1 when incomparable vertices of ordered type (a,b,c) are adjacent. For fixed join depth c and n=k-c, the number of active ordered types satisfies |supp(A_c)|≤⌊n²/2⌋.
2. **T07 — Total Active-Type Bound.** Let d≥3 and let a complete ordered d-ary rooted tree of height k be embedded path-induced, level-stable, and type-uniform in a triangle-free graph. For c<a,b≤k, let A_c(a,b)=1 when incomparable vertices of ordered type (a,b,c) are adjacent. Across all join depths, the total number of active ordered types is at most Σ_{n=1}^k⌊n²/2⌋. If k=2m this equals m(m+1)(4m-1)/3; if k=2m+1 it equals m(m+1)(4m+5)/3.
3. **T08 — Parity-Defect Host Construction.** On a complete rooted d-ary tree, keep all tree edges and add an edge between incomparable vertices exactly when their depths have opposite parity. The resulting graph is triangle-free, the rooted tree is path-induced, level-stable, and type-uniform.
4. **T09 — Sharpness of the Active-Type Bounds.** The parity-defect host T08 has A_c(a,b)=1 exactly when a and b have opposite parity. Hence every slice has ⌊(k-c)²/2⌋ active types and T06–T07 are sharp.
5. **M06 — Exact Reach-Profile Equivalence.** For fixed positive integers r_1,…,r_q, the following are equivalent: (i) there exist pairwise anticomplete connected sets C_i with reach at least r_i from N(v)∩C_i; (ii) G contains an induced spider centered at v with arm lengths at least r_i+1.
6. **N15 — Critical Escape-Boundary Theorem.** Under N13, let C be a component of G-N[S] with χ(C)≥k-|S|. Its external neighborhood B=N(C) lies in N(S)\S, separates C from S, and is not a clique. In particular, B contains two nonadjacent vertices.
7. **P05 — Fibonacci Contact-Signature Count.** For an n-vertex induced path P in a triangle-free graph, the neighborhood signature N(x)∩V(P) of an outside vertex is a subset with no consecutive path vertices. Hence at most F_{n+2} signatures are possible.
8. **P07 — Nonempty Signature Fibers Are Stable.** In a triangle-free graph, for a fixed induced path P and a fixed nonempty signature S⊆V(P), all outside vertices x with N(x)∩V(P)=S form a stable set.
9. **C01 — Clean-Child or Large Fan Dichotomy.** Let G be triangle-free, u∈V(G), X⊆V(G)\N[u] finite and nonempty, and B⊆N(u). Then either some b∈B is anticomplete to X, or some x∈X has at least ⌈|B|/|X|⌉ neighbors in B; in the latter case {u,x} with those neighbors induces K_{2,m}.
10. **T10 — Type-Profile Determines the Defect Graph.** In a type-uniform copy, two target embeddings with identical ordered type for every incomparable target-vertex pair induce identical extra-edge patterns.
11. **T11 — Sibling-Selection Sterility.** Changing only the identities of selected sibling branches, while preserving every target pair’s ordered depth/join type, cannot turn a non-induced target copy into an induced one.
12. **N03 — Isolate-Sharp Closed-Neighborhood Bound.** Let I be the set of vertices isolated in G[S]. Then χ(G[N[S]]) ≤ |S| if I is empty, and χ(G[N[S]]) ≤ |S|+1 otherwise.
13. **N07 — Sequential Protected Deletion Ledger.** Let G0=G. For i=1,…,m, let S_i⊆V(G_{i-1}) induce no isolated vertices in G_{i-1}, and put G_i=G_{i-1}-N_{G_{i-1}}[S_i]. Then χ(G_m) ≥ χ(G)-Σ_i |S_i|.

## Suggested paper packages
### Package A — Extremal defect tensors in triangle-free type-uniform tree copies
Combine T01–T12. The headline is the sharp slice bound `⌊n²/2⌋`, the exact total-height formula, and the parity-defect host attaining equality. This is the most novel-looking, finite, self-contained cluster.

### Package B — Mixing profiles and induced spiders
Combine M01–M07. The headline is the exact equivalence between anticomplete connected regions with prescribed reach profile and induced spiders with the corresponding arm lengths.

### Package C — Chromatic escape from finite induced structures
Combine N03–N07 and N13–N16. The headline is a quantitative high-chromatic escape component outside a connected finite structure, together with a nonclique attachment boundary in a critical graph.

### Package D — Induced-path contact codes
Combine P01–P12. The headline is the exact cycle dictionary for consecutive contacts, Fibonacci/d-separated signature counts, and stable nonempty signature fibers.

### Package E — Contamination-fan calculus
Combine C01–C06. The headline is a clean-child/large-fan dichotomy, its weighted form, and the exact conversion of the first legal cross-branch contamination into an induced cycle.

## Lean formalization order
1. N01, N09, C07, C08 — basic triangle/clique facts.
2. M01, P01, C05 — shortest-path / induced-cycle extraction.
3. N02–N07 — finite colorings and deletion inequalities.
4. M02–M06 — pairwise anticomplete region extraction.
5. C01–C03 — finite pigeonhole and weighted averaging.
6. N14–N16 — critical graph gluing arguments.
7. T01–T12 — ordered rooted trees, types, tensor support, parity host.

## Exact theorem packets

### Triangle-Free Budget

#### N01 — Neighborhood Stability
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `C`  
**Lean difficulty:** `1/5`

**Statement.** In every finite simple triangle-free graph G and every vertex v, the open neighborhood N(v) is a stable set.

**Proof route.** If two vertices of N(v) were adjacent, they and v would form a triangle.

**Novelty query.** `Neighborhood Stability`

#### N02 — Union-of-Neighborhoods Coloring Bound
**Status:** `PROVED_IN_PACKET`  
**Novelty-search priority:** `B`  
**Lean difficulty:** `2/5`

**Statement.** For every finite S subset V(G) in a triangle-free graph, χ(G[⋃_{s∈S} N(s)]) ≤ |S|.

**Proof route.** Order S. Assign each vertex in the union to its first neighboring s. Each color class lies inside one stable neighborhood N(s).

**Dependencies.** N01

**Novelty query.** `Union-of-Neighborhoods Coloring Bound`

#### N03 ⶻ�q�^u�+v+)�����(��^��q�e�����