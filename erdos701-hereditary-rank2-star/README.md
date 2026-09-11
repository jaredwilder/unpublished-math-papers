# Erdős #701 / Chvátal-star route — the rank-2 hereditary case

**Author:** Jared Wilder  
**Recovered campaign:** `erdos701-campaign-001 / R014`  
**Public extraction:** 2026-09-11

This note isolates a universal child theorem recovered from a campaign aimed at the much harder hereditary-family star problem.

## Definitions

Let `F` be a finite hereditary family of finite sets: whenever `A∈F` and `B⊆A`, one has `B∈F`.
Assume every member of `F` has size at most two.

Let

\[
m(F)=\max\{|G|:G\subseteq F\text{ is pairwise intersecting}\}
\]

and

\[
\Delta(F)=\max_x |\{A\in F:x\in A\}|.
\]

Here pairwise intersecting means every two members of `G` have nonempty intersection; in particular the empty set cannot belong to a nonempty intersecting subfamily.

## Theorem

For every finite hereditary family `F` of rank at most two,

\[
\boxed{m(F)=\Delta(F).}
\]

Thus the Chvátal star bound is exact throughout the complete rank-2 hereditary class.

## Proof

The lower bound is immediate: for any point `x`, the full star

\[
F(x)=\{A\in F:x\in A\}
\]

is pairwise intersecting. Hence

\[
m(F)\ge\Delta(F).
\]

For the reverse inequality, let `G⊆F` be pairwise intersecting.

If some singleton `{x}` belongs to `G`, then every member of `G` must contain `x`, so `G` is contained in the star at `x` and

\[
|G|\le\Delta(F).
\]

We may therefore assume every member of `G` has size two. Regard `G` as an intersecting family of edges in a simple graph.

If all edges of `G` share a common endpoint `x`, again

\[
|G|\le\Delta(F).
\]

Otherwise choose two edges `xy` and `xz` sharing `x`, and choose an edge of `G` not containing `x`. Because it must intersect both `xy` and `xz`, that edge is necessarily `yz`. Now any further edge meeting each of

\[
xy,\quad xz,\quad yz
\]

must itself be one of those three edges. Hence

\[
G=\{xy,xz,yz\}
\]

and `|G|=3`.

Because `F` is hereditary and contains `xy` and `xz`, it also contains `{x}`. Therefore the star at `x` contains at least

\[
\{x\},\quad xy,\quad xz,
\]

so

\[
\Delta(F)\ge3=|G|.
\]

Thus every pairwise intersecting `G⊆F` has size at most `Delta(F)`, proving

\[
m(F)=\Delta(F).
\]

## Audit history

The recovered campaign first used exact finite enumeration on small ground sets. The later certifier pass extracted the general structural reduction above for **all finite ground sets** when the hereditary family has maximum member size at most two. It explicitly refused to extrapolate this argument to arbitrary rank.

That distinction is retained here: this is a complete rank-2 theorem, not a proof of the full Chvátal conjecture / surrounding Erdős problem.

## Novelty boundary

No historical novelty claim is made. This is elementary graph/intersection structure and should be treated as a clean independently reconstructed restricted theorem unless a specialist literature review establishes otherwise.

## License

Apache-2.0 for repository-authored material.
