# Caccetta–Häggkvist directed-triangle case — Rounds 18–19

**Campaign dates:** 2026-08-06/07  
**Flagship:** every finite oriented graph with minimum outdegree `> (n-1)/3` contains a directed triangle  
**Court:** **OPEN — no proof of the flagship is asserted here**

This file publishes the later terminal work that postdates the 15-round theorem ledger. The packets refine the smallest-counterexample geometry, correct an earlier opposite-fan mistake, derive an exact critical-cycle defect telescope, and isolate one final global inequality.

## Round 18

Assume a smallest counterexample, then minimize arcs. Put `d=ceil(n/3)`. Arc minimality makes the graph `d`-outregular, and vertex deletion leaves only

`n = 3d-1` or `n = 3d`.

### Theorem 158 — Minimal Deletion-Cover Theorem

For every nonempty proper `S subset V(D)`, some `x outside S` satisfies

`d_S^+(x) >= d - ceil((n-|S|)/3) + 1`.

The proof is the direct minimal-counterexample argument: otherwise `D-S` would still have minimum outdegree at least `ceil((n-|S|)/3)`.

### Corollary 159 — Universal Critical Escape / indegree barrier

For every root `v`, writing `A=N+(v)`, `B=N-(v)`, and `M` for the nonneighbors of `v`, some `a in A` has

`d_M^+(a) >= floor(2d/3)+1`.

Hence

`|M_v| >= floor(2d/3)+1`

and

`d^-(v) <= n-1-d-(floor(2d/3)+1)`.

### Corollary 160 — Pair common-inneighbour theorem in the `3d-1` branch

If `n=3d-1`, every pair of vertices has a common inneighbour.

### Theorem 161 — Uncovered-pair graph is triangle-free in the `3d` branch

For `n=3d`, define an undirected graph `U` on `V(D)` by putting an edge `ab` when `a,b` have no common inneighbour. Then `U` is triangle-free.

### Theorem 162 — Opposite-Fan Anticompleteness

If `x,y` are nonadjacent and

`P=N+(x) cap N-(y)`, `R=N+(y) cap N-(x)`,

then **there are no arcs in either direction between `P` and `R`**.

This is a Court correction. An earlier branch allowed `R -> P` as a legal reservoir. That was false, and any estimate relying on it must be reopened.

### Theorem 163 — Directed-C4 diagonal graph is triangle-free

Let `H(D)` have one vertex for each unordered nonedge of `D`, with two nonedges adjacent iff they occur as the opposite diagonals of a directed 4-cycle. Then

`H(D)` is triangle-free,

and exactly

`|E(H(D))| = C4(D)`.

Thus the earlier cubic directed-`C4` lower bound translates to a triangle-free auxiliary graph with an exact edge count.

### Theorem 164 — Pointwise edge-local potential no-go

No proof can be obtained by assigning to each directed edge a potential whose free-vertex contribution depends only on the labelled three-vertex relation to that edge and then proving the desired local inequality pointwise. A free vertex dominated by all three vertices of a directed 2-path gives identical edge states but indicator contribution three.

This kills that *specific* potential architecture; it does not rule out higher-memory or global potentials.

### Theorem 165 — Critical-cycle fragmentation

Choosing from each vertex an outgoing edge minimizing common-outneighbour count gives, for a critical edge `u->v`,

`|N+(u) cap N+(v)| <= ceil(d/3)-1`

and therefore

`|N+(v) cap M_u| >= floor(2d/3)+1`.

Along a directed cycle of critical edges, each outside vertex has a constrained `+/-/0` relation word; the packet develops this as the local combinatorial substrate for a telescoping proof.

### Exact finite audit for Round 18

The supplied dependency-free checker exhausts all oriented graphs on 3, 4 and 5 vertices:

- 27 on 3 vertices;
- 729 on 4 vertices;
- 59,049 on 5 vertices.

Every triangle-free instance passed opposite-fan anticompleteness and the triangle-freeness of the `C4`-diagonal graph. This is finite verification only.

---

## Round 19 — exact critical-defect telescope

Round 19 finishes the local algebra for both possible second-step types on a shortest directed cycle of critical edges.

### Theorem 168 — Exact Edge-Potential Identity

The packet introduces an exact edge-potential identity for a directed edge and its rooted degree/common-neighbour data. This is the algebraic object whose differences telescope around a critical cycle.

### Theorem 169 — Independent-Path Twisted-Circle Defect

For a critical path `u->v->w` with `u` nonadjacent to `w`, the edge-potential difference plus the boundary term is controlled by an explicitly enumerated local defect. The exact relation-state table is checked exhaustively.

### Theorem 170 — Critical Induction Defect

For critical `u->v`, `v->w`, and `u` nonadjacent to `w`, put

`U=N+(u) cap N-(w)` and `h=|U|`.

Choose `v* in U` with

`d_U^+(v*) <= floor((h-1)/3)`.

Writing

`C(u,w)=|N+(u) cap N+(w)|`

and

`B(u,v*,w)=|{x : u->x, v*->x, x nonadjacent to w}|`,

the packet proves

`J(u,v,w) <= 3(C(u,w)+B(u,v*,w))`.

### Corollary 171 — Independent Critical-Path Defect

The independent-second-step edge-potential difference is bounded by the twisted local term plus `3C+3B`.

### Theorem 172 — Shortest Critical-Cycle Chord Gap

On a shortest directed cycle of critical edges, for a consecutive path `u->v->w`, the reverse chord is impossible. If the forward chord `u->w` exists, it is noncritical and

`G(u,v,w)=O(u,w)-O(u,v) >= 1`,

where `O(a,b)` is the common-outneighbour count used by the criticality rule.

### Theorem 173 — Transitive Critical-Path Defect

For a transitive path `u->v`, `v->w`, `u->w`, define

`D_tr = 2 N_{+++} + 2 N_{+0+} + N_{++0} + N_{++-}`.

Then

`delta + F(u,v)-F(v,w) <= D_tr - G(u,v,w)`.

On a shortest critical cycle, `G>=1`.

### Theorem 174 — Full Critical-Cycle Defect Telescope

Let `I` index independent second steps and `H` index transitive second steps on a shortest critical cycle of length `ell`. With the packet's exact local defects,

`delta*ell + sum_{i in H} G_i <= sum_{i in I} D_i^ind + sum_{i in H} D_i^tr`.

Since every `G_i>=1`, also

`delta*ell + |H| <= sum_{i in I} D_i^ind + sum_{i in H} D_i^tr`.

This is the exact terminal telescope: the potential terms cancel completely around the cycle.

### Theorem 175 — Four-Middle-Set Disjointness

For a directed 4-cycle `a->b->c->d->a`, the four two-path middle sets associated with opposite directions of the two diagonals are pairwise disjoint. Hence

`Q_ac + Q_ca + Q_bd + Q_db <= n`.

### Corollary 176 — Local degree inequality in the C4-diagonal graph

If two nonedges `e,f` are adjacent in `H(D)`, then

`sqrt(d_H(e)) + sqrt(d_H(f)) <= n/2`.

### Theorem 177 — Safe-Switch Normal Form

Among smallest `d`-outregular counterexamples, further minimize

`Xi(D)=sum_v d^-(v)^2`.

If `x,y` are nonadjacent and there is no two-path `y -> * -> x`, then replacing `x->z` by `x->y` creates no directed triangle. Minimality of `Xi` forces

`d^-(z) <= d^-(y)+1`

for every `z in N+(x)`.

### Theorem 178 — Root Reverse-Layer Extraction

For root `x`, with `B=N-(x)` and `r=|B|`, some nonneighbor `m` of `x` satisfies

`d_B^+(m) >= d - ceil((n-r-1)/3) + 1`.

Thus in the two branches:

- `n=3d`: `d_B^+(m) >= floor((r+1)/3)+1`;
- `n=3d-1`: `d_B^+(m) >= floor((r+2)/3)+1`.

### Theorem 179 — Inneighborhood dominating cycle in the `3d-1` branch

When `n=3d-1`, every pair has a common inneighbour. Consequently for every root `x`, the induced digraph on `B=N-(x)` has minimum indegree at least one and therefore contains a directed cycle of length at least four. The packet also derives

`|B|(d-1) >= 3d-2`,

so in the nontrivial branch `|B|>=4`.

## Exact remaining theorem

The flagship would close if one proves the **Terminal Critical-Defect Upper Bound**

`sum_{i in I} D_i^ind + sum_{i in H} D_i^tr < delta*ell + sum_{i in H} G_i`

for every shortest critical cycle in a smallest counterexample.

That inequality is **OPEN** in the packet. Therefore the Caccetta–Häggkvist triangle case is not declared solved.

## Round-19 finite receipt

The supplied checker verifies:

- the complete 21-state independent-path table;
- the complete 20-state transitive-path table;
- the complete 47-state directed-`C4` middle-set table;
- the edge-potential identity on every triangle-free oriented graph through order 5;
- the local defect inequalities on every regular triangle-free oriented graph through order 5;
- the corrected opposite-fan and `C4`-diagonal facts through order 5.

The exhaustive universe counts are 27, 729 and 59,049 oriented graphs at orders 3, 4 and 5 respectively; among them the packet reports 25, 549 and 30,535 triangle-free instances. This finite audit certifies the local algebra only, not the unbounded flagship.
