# Erdős #595 theorem refinery — 65-card public ledger

Source date: 2026-08-04. Historical novelty and Lean status were UNRUN. The flagship Erdős #595 problem remains open. This ledger preserves the source status of every card; conditional/source-derived/refuted cards are not promoted.

| ID | Status | Title | Statement / scope |
|---|---|---|---|
| T01 | `PROVED_IN_PACKET` | Cover-to-partition refinement | For every graph G and cardinal κ, if E(G) is the union of κ triangle-free edge sets, then E(G) can be partitioned into κ triangle-free edge sets. |
| T02 | `PROVED_IN_PACKET` | Triangle-hypergraph chromatic equivalence | Let Tri(G) be the 3-uniform hypergraph with vertex set E(G) and one hyperedge for each triangle of G. Then the triangle-cover number tc(G) equals the vertex chromatic number χ(Tri(G)), where a hypergraph coloring is proper when no hyperedge is monochromatic. |
| T03 | `PROVED_IN_PACKET` | Edge-coloring formulation | For every graph G and cardinal κ, tc(G) ≤ κ if and only if there exists c : E(G) → κ such that the three edges of every triangle are not all assigned the same value. |
| T04 | `PROVED_IN_PACKET` | General blocker-centeredness duality | For every hypergraph H on vertex set X and every cardinal κ, χ(H) ≤ κ if and only if there exist κ vertex covers D_i of H with ⋂_{i<κ} D_i = ∅. Consequently, χ(H) is the least cardinality of a subfamily of vertex covers having empty intersection. |
| T05 | `PROVED_IN_PACKET` | Triangle-transversal centeredness equivalence | Let Tr(G) be the family of edge sets meeting every triangle of G. For every cardinal κ, tc(G) > κ if and only if every subfamily of Tr(G) of cardinality at most κ has nonempty intersection. |
| T06 | `PROVED_IN_PACKET` | Centeredness trichotomy | For a graph G with at least one triangle: (i) tc(G)=n<ω exactly when n is the least size of a triangle-transversal family with empty intersection; (ii) tc(G)=ℵ₀ exactly when Tr(G) has the finite-intersection property but has a countable subfamily with empty intersection; (iii) tc(G)>ℵ₀ exactly when Tr(G) is countably centered. |
| T07 | `PROVED_IN_PACKET` | Exact bipartite-cover cardinal theorem | Let bc(G) be the least cardinal κ such that E(G) is covered by κ bipartite subgraphs. Then bc(G) is the least κ satisfying χ(G) ≤ 2^κ. |
| T08 | `PROVED_IN_PACKET` | Finite logarithmic bipartite cover | For every finite graph G with at least one edge, bc(G)=⌈log₂ χ(G)⌉. |
| T09 | `PROVED_IN_PACKET` | Triangle cover bounded by bipartite cover | For every graph G, tc(G) ≤ bc(G). |
| T10 | `PROVED_IN_PACKET` | Cardinal chromatic upper bound | For every graph G and cardinal κ, χ(G) ≤ 2^κ implies tc(G) ≤ κ. |
| T11 | `PROVED_IN_PACKET` | Cardinal chromatic obstruction | For every graph G and cardinal κ, tc(G)>κ implies χ(G)>2^κ. |
| T12 | `PROVED_IN_PACKET` | Continuum barrier for Erdős #595 | Any graph G that is not a union of countably many triangle-free subgraphs satisfies χ(G)>2^{ℵ₀}; in particular |V(G)|>2^{ℵ₀} and |E(G)|>2^{ℵ₀}. |
| T13 | `PROVED_IN_PACKET` | Countable-edge trivial cover | Every graph with at most countably many edges is a union of countably many one-edge, hence triangle-free, subgraphs. |
| T14 | `PROVED_IN_PACKET` | Subgraph monotonicity | If H is a subgraph of G, then tc(H)≤tc(G). |
| T15 | `PROVED_IN_PACKET` | Homomorphism pullback monotonicity | If there is a graph homomorphism f:G→H between simple graphs, then tc(G)≤tc(H). |
| T16 | `PROVED_IN_PACKET` | Independent blow-up invariance | If B is obtained from a graph G by replacing every vertex with a nonempty independent set and every edge with the corresponding complete bipartite pair, then tc(B)=tc(G). |
| T17 | `PROVED_IN_PACKET` | Disjoint-union formula | For every family of graphs (G_i)_{i∈I}, tc(⊔_{i∈I}G_i)=sup_{i∈I} tc(G_i). |
| T18 | `PROVED_IN_PACKET` | Clique–Ramsey identity | For every integer n≥3, tc(K_n) is the least positive integer k such that n<R_k(3), where R_k(3) is the diagonal k-color Ramsey number for triangles. |
| T19 | `PROVED_IN_PACKET` | Union subadditivity | For any family of subgraphs (G_i)_{i∈I} with G=⋃_{i∈I}G_i, tc(G)≤Σ_{i∈I}tc(G_i) in cardinal arithmetic. |
| T20 | `PROVED_IN_PACKET` | κ-union closure | For every infinite cardinal κ, the class {G:tc(G)≤κ} is closed under unions of at most κ subgraphs from the same class. |
| T21 | `PROVED_IN_PACKET` | Countable-union closure | A countable union of graphs that are each countable unions of triangle-free subgraphs is itself a countable union of triangle-free subgraphs. |
| T22 | `PROVED_IN_PACKET` | Chain cover bound | If G=⋃_{i<δ}G_i and tc(G_i)≤κ for every i, then tc(G)≤κ·|δ|. |
| T23 | `PROVED_IN_PACKET` | Minimal edge-cardinality cofinality theorem | Fix an infinite cardinal κ. If λ is the least edge cardinality of a graph G with tc(G)>κ, then cf(λ)>κ. |
| T24 | `PROVED_IN_PACKET` | Minimal vertex-cardinality cofinality theorem | Fix an infinite cardinal κ. If λ is the least vertex cardinality of a graph G with tc(G)>κ, then cf(λ)>κ. |
| T25 | `PROVED_IN_PACKET` | Uncountable-cofinality witness constraint | The least vertex cardinality and the least edge cardinality of an Erdős #595 witness, if either minimum is taken over all witnesses, must each have uncountable cofinality. |
| T26 | `PROVED_USING_STANDARD_COMPACTNESS` | Fixed-finite compactness | For each fixed positive integer k, tc(G)≤k if and only if tc(F)≤k for every finite subgraph F of G. |
| T27 | `PROVED_IN_PACKET` | Finite obstruction extraction | If tc(G)>ℵ₀, then for every positive integer k, G contains a finite subgraph F with tc(F)>k. |
| T28 | `PROVED_IN_PACKET` | Countable exact-ℵ₀ core extraction | If tc(G)>ℵ₀, then G contains a countable subgraph H with tc(H)=ℵ₀. If G is K₄-free, H may be chosen K₄-free. |
| T29 | `PROVED_IN_PACKET` | Countable exact-ℵ₀ criterion | For a countable-edge graph H, tc(H)=ℵ₀ if and only if the values tc(F) over finite subgraphs F⊆H are unbounded in the positive integers. |
| T30 | `PROVED_IN_PACKET` | Countable finite-stage sterility | No graph obtained as a countable union of finite subgraphs can be an Erdős #595 witness. |
| T31 | `PROVED_IN_PACKET` | Triangle-inert bridge invariance | If G' is obtained from G by adding edges that lie in no triangle of G', then tc(G')=max(tc(G),1) (and equals tc(G) whenever G has an edge). |
| T32 | `PROVED_IN_PACKET` | Vertex-sum formula | If a graph G is formed by gluing a family of graphs along vertices only, with no edge shared between distinct pieces and no edge joining their nonshared vertices, then tc(G)=sup_i tc(G_i). |
| T33 | `PROVED_FROM_FINITE_FOLKMAN_INPUT` | Connected locally finite one-ended exact-ℵ₀ core | Assume that for every k there exists a finite K₄-free graph F_k with tc(F_k)>k. Then there exists a connected, locally finite, one-ended, countable K₄-free graph H with tc(H)=ℵ₀. |
| T34 | `PROVED_IN_PACKET` | Bounded-degree cover bound | If a graph G has finite maximum degree Δ, then tc(G)≤⌈log₂(Δ+1)⌉. |
| T35 | `PROVED_IN_PACKET` | Unbounded-degree necessity for exact-ℵ₀ locally finite cores | Every locally finite graph H with tc(H)=ℵ₀ has unbounded vertex degrees. |
| T36 | `PROVED_IN_PACKET` | Finite critical-density consequence | If a finite graph G satisfies tc(G)>k, then G contains a subgraph H with minimum degree at least 2^k. |
| T37 | `PROVED_IN_PACKET` | Finite dense obstructions inside every witness | Every Erdős #595 witness contains, for each positive integer k, a finite K₄-free subgraph having minimum degree at least 2^k. |
| T38 | `PROVED_IN_PACKET` | Product-coloring lemma | If E(G)=⋃_{i∈I}E(H_i) and each H_i has a proper vertex coloring with μ_i colors, then χ(G)≤∏_{i∈I} μ_i. |
| T39 | `PROVED_IN_PACKET` | Uniform product bound | If G is the union of κ subgraphs each of chromatic number at most μ, then χ(G)≤μ^κ. |
| T40 | `PROVED_IN_PACKET` | Triangle-free chromatic ceiling | Define τ(G)=sup{χ(H):H⊆G and H is triangle-free}. If tc(G)≤κ, then χ(G)≤τ(G)^κ. |
| T41 | `PROVED_IN_PACKET` | Chromatic-dispersion obstruction | For every graph G and cardinal κ, χ(G)>τ(G)^κ implies tc(G)>κ. |
| T42 | `PROVED_IN_PACKET` | Countable-power fixed-point close lemma | If κ^{ℵ₀}=κ and a graph G satisfies χ(G)=κ^+ and τ(G)≤κ, then tc(G)>ℵ₀. |
| T43 | `PROVED_IN_PACKET` | Continuum-gap close lemma | If χ(G)=(2^{ℵ₀})^+ and every triangle-free subgraph of G has chromatic number at most 2^{ℵ₀}, then G is not a countable union of triangle-free subgraphs. |
| T44 | `PROVED_IN_PACKET` | Finite-layer dispersion criterion | If every triangle-free subgraph of a finite graph G is μ-colorable and χ(G)>μ^k, then tc(G)>k. |
| T45 | `PROVED_IN_PACKET` | Triangle-transversal formula for τ | For every graph G, τ(G)=sup{χ(G−D):D⊆E(G) meets every triangle of G}. |
| T46 | `PROVED_IN_PACKET` | Transversal-collapse criterion | For cardinals μ, τ(G)≤μ if and only if every triangle transversal D of G satisfies χ(G−D)≤μ. |
| T47 | `PROVED_IN_PACKET` | General H-free product bound | Fix a graph H₀ and define τ_{H₀}(G)=sup{χ(F):F⊆G and F is H₀-free}. If G is the union of κ H₀-free subgraphs, then χ(G)≤τ_{H₀}(G)^κ. |
| T48 | `PROVED_IN_PACKET` | General hereditary-class product bound | Let C be any class of graphs closed under taking subgraphs, and let τ_C(G)=sup{χ(F):F⊆G and F∈C}. If E(G) is covered by κ subgraphs in C, then χ(G)≤τ_C(G)^κ. |
| T49 | `PROVED_IN_PACKET` | Dispersion lower-bound parameter | Let d_△(G) be the least cardinal κ such that χ(G)≤τ(G)^κ. Then d_△(G)≤tc(G). |
| T50 | `PROVED_IN_PACKET` | Exact-ℵ₀ core has countable vertex chromatic number | If H has countably many edges and tc(H)=ℵ₀, then χ(H)=ℵ₀ after isolated vertices are discarded. |
| T51 | `SOURCE_DERIVED_PRIOR_ART_RECHECK_REQUIRED` | K₄-free high-chromatic triangle-free-subgraph anchor | Session-derived prior-art anchor: if G is K₄-free and χ(G)>2^{ℵ₀}, then G contains a triangle-free subgraph of uncountable chromatic number. |
| T52 | `PROVED_IN_PACKET` | Triangle hypergraphs are linear 3-uniform | For every simple graph G, Tri(G) is a 3-uniform linear hypergraph: every hyperedge has three vertices and any two distinct hyperedges intersect in at most one vertex. |
| T53 | `PROVED_IN_PACKET` | K₄–Berge-triangle equivalence | A simple graph G is K₄-free if and only if Tri(G) contains no Berge 3-cycle, meaning no three triangle-hyperedges pairwise intersect in three distinct graph-edge vertices. |
| T54 | `PROVED_IN_PACKET` | Common-neighbor independence | If G is K₄-free and uv∈E(G), then the common neighborhood N(u)∩N(v) is an independent set. |
| T55 | `PROVED_IN_PACKET` | Triangle multiplicity is unbounded in K₄-free graphs | For every positive integer m there exists a finite K₄-free graph containing an edge that belongs to exactly m triangles. |
| T56 | `PROVED_IN_PACKET` | Book graphs have triangle-cover number two | For every m≥1, the m-page book graph B_m has tc(B_m)=2. |
| T58 | `PROVED_IN_PACKET` | Exact endpoint representation theorem | A 3-uniform hypergraph H is isomorphic to Tri(G) for some simple graph G if and only if there exist a set X and an injective map ρ:V(H)→[X]^2 such that: (i) for every hyperedge {a,b,c} of H, the pairs ρ(a),ρ(b),ρ(c) are exactly the three 2-subsets of some 3-element subset of X; and (ii) every 3-element subset of X whose three pairs lie in ρ(V(H)) corresponds to a hyperedge of H. |
| T59 | `PROVED_IN_PACKET` | Triangle-hypergraph embedding theorem | A 3-uniform hypergraph H embeds as a subhypergraph of Tri(G) for some simple graph G if and only if there exist X and an injective map ρ:V(H)→[X]^2 satisfying condition (i) of T58 for every hyperedge of H; extra graph triangles are permitted. |
| T60 | `PROVED_IN_PACKET` | Finite triangle-hypergraph realizability lies in NP | The decision problem 'given a finite 3-uniform hypergraph H, is H isomorphic to Tri(G) for some finite simple graph G?' belongs to NP. |
| T61 | `PROVED_IN_PACKET` | K₄-free realization certificate | If a finite 3-uniform hypergraph H has an exact endpoint representation as in T58 and H has no Berge 3-cycle, then the realizing graph G is K₄-free. |
| T62 | `PROVED_IN_PACKET` | Line-graph plus Krausz-partition recovery | Given the line graph L(G) together with its canonical Krausz family of cliques corresponding to stars at vertices of G, Tri(G) consists exactly of the 3-cliques of L(G) that are not contained in a single star clique. |
| T63 | `PROVED_IN_PACKET` | Realizable-hypergraph witness reduction | If H is an uncountably chromatic 3-uniform hypergraph with no Berge 3-cycle and H is exactly realizable as Tri(G), then G is a K₄-free Erdős #595 witness. |
| T64 | `PROVED_IN_PACKET` | Embedded-hypergraph witness reduction | If H is an uncountably chromatic 3-uniform hypergraph that embeds into Tri(G), and G is independently known to be K₄-free, then G is an Erdős #595 witness. |
| T65 | `CONDITIONAL_REDUCTION` | Broad realizability bridge | Conditional theorem: if every linear Berge-C3-free 3-uniform hypergraph admits an exact endpoint representation, then Erdős #595 is equivalent to the existence of an uncountably chromatic linear Berge-C3-free 3-uniform hypergraph. |
| T66 | `REFUTED_ROUTE` | Triangle-degree bound refutation | The assertion 'every edge of a K₄-free graph belongs to at most a fixed constant number of triangles' is false, even for finite graphs. |

## Status counts

- `PROVED_IN_PACKET`: 60
- `PROVED_USING_STANDARD_COMPACTNESS`: 1
- `PROVED_FROM_FINITE_FOLKMAN_INPUT`: 1
- `SOURCE_DERIVED_PRIOR_ART_RECHECK_REQUIRED`: 1
- `CONDITIONAL_REDUCTION`: 1
- `REFUTED_ROUTE`: 1

## Flagship boundary

The source target is the existence of a K4-free graph whose edge set is not the union of countably many triangle-free edge sets, equivalently a K4-free graph G with tc(G)>aleph_0. This theorem bank does not claim that such a graph exists or does not exist.