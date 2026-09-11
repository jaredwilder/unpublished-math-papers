# Erdős #146 — degenerate bipartite Turán bounds

This directory is the human-facing entry point for a three-file Lean program on the Erdős–Simonovits degenerate Turán conjecture.

For a bipartite graph `H` that is `r`-degenerate, the target asks for the scale

\[
\operatorname{ex}(n,H) \ll n^{\,2-1/r}.
\]

The formal sources currently live in the historical campaign archive at
`jaredwilder/erdos-campaign-archive/campaigns/erdos146-attack-2026-09-05/`.
They contain 51 named, successfully checked declarations across `Attack01.lean`, `Attack02.lean`, and `Attack03.lean`.

## What the formal program proves

### 1. The exponent scales are genuinely distinct

Writing

\[
\operatorname{scale}_r(n)=n^{2-1/r},
\]

`Attack01.lean` proves that for `1 <= r < s`,

\[
\operatorname{scale}_r \ll \operatorname{scale}_s,
\qquad
\operatorname{scale}_s \not\ll \operatorname{scale}_r.
\]

More generally, a strictly larger real power is never Vinogradov-bounded by a smaller one.

This gives an exact obstruction to using a weaker exponent bound as a black box. In particular, the cited Alon–Krivelevich–Sudakov conclusion at exponent `2 - 1/(4r)` cannot by itself imply the desired exponent `2 - 1/r`: the function `scale (4r)` satisfies the weaker bound and violates the stronger one.

This is a statement about logical strength of the bound, not a criticism of the cited theorem.

### 2. The degeneracy hierarchy is strict inside bipartite graphs

`Attack02.lean` uses the complete bipartite graph `K_{r,r}` to prove that, whenever `k < r`, there is a bipartite graph which is `r`-degenerate but not `k`-degenerate.

Thus the hypothesis classes

\[
\mathrm{Degenerate}(0) \subsetneq
\mathrm{Degenerate}(1) \subsetneq
\mathrm{Degenerate}(2) \subsetneq \cdots
\]

remain strictly nested even after restricting to the bipartite graphs occurring in the conjecture.

So increasing `r` simultaneously enlarges the graph class and weakens the target exponent. Neither axis collapses to another value of `r`.

### 3. Every finite degenerate graph has a degeneracy ordering

`Attack01.lean` constructs, by finite induction, a list of all vertices such that each vertex has at most `r` neighbours later in the list whenever the graph is `r`-degenerate.

This is the standard ordering needed for greedy embedding arguments, but here it is proved directly from the exact degeneracy predicate used by the frozen problem statement.

### 4. The problem reduces to graphs on `Fin m`

`Attack01.lean` proves that it is enough to establish the conjectured bound for every finite graph whose vertex type is `Fin m`.

At universe level zero this is an equivalence. The useful direction is universe-independent: a proof for all `Fin m` graphs transfers to every finite vertex type.

This removes the ambient type/universe from the mathematical search space and leaves a genuinely finite graph problem at each order `m`.

### 5. Minimum-degree subgraph extraction

`Attack03.lean` proves the classical deletion lemma in the exact vocabulary needed here:

> If a finite graph on `n` vertices has more than `k n` edges, then it contains a nonempty induced vertex set on which every vertex has more than `k` neighbours inside the set.

The development proves relative `Finset`, global edge-count, and explicit `SimpleGraph.Subgraph` versions.

### 6. Quantitative sparsity of degenerate graphs

As an immediate consequence of the extraction theorem, `Attack03.lean` proves

\[
H\text{ is }r\text{-degenerate}
\quad\Longrightarrow\quad
|E(H)|\le r|V(H)|.
\]

It also proves the corresponding relative degree-sum inequality on every finite vertex subset.

This is the first quantitative consequence of the degeneracy hypothesis in the program; the earlier hierarchy results are structural.

## Formal trust footprint

The historical compile logs record:

- `Attack01.lean`: 26 named declarations;
- `Attack02.lean`: 11 named declarations;
- `Attack03.lean`: 14 named declarations.

All 51 recorded declarations have axiom footprints contained in

`[propext, Classical.choice, Quot.sound]`.

Several need only a strict subset of that footprint. The receipts contain no `sorryAx` and no `native_decide` for these 51 declarations.

A separate `Probe01.lean` was a failed exploratory probe. It is not part of the 51-declaration result set and is not cited as evidence.

## Current frontier

The program has already closed one of the two concrete lemmas originally identified on the route toward the `r = 1` case: minimum-degree extraction.

The remaining constructive ingredient is a greedy embedding theorem along the degeneracy ordering. Even with that theorem, the containment argument would still have to be assembled into the required Vinogradov bound on `ex(n,H)`.

The general conjecture, including the `r = 2` instance, remains outside the proved statements above.

## Source map

- `Attack01.lean` — exponent separation, obstruction map, graph-containment monotonicity, degeneracy ordering, finite-universe reduction
- `Attack02.lean` — strict bipartite degeneracy hierarchy via `K_{r,r}`
- `Attack03.lean` — minimum-degree extraction and sparsity of degenerate graphs
- `Attack01.log`, `Attack02.log`, `Attack03.log` — named theorem axiom footprints
- `TERMINAL-attack03.json` — exact remaining frontier and historical campaign record

This is a coherent formal research program and should migrate intact to a dedicated Erdős #146 repository when repository creation is available in the active GitHub session.
