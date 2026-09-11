# Erdős #20 — sunflower bounds and formal constructions

This directory is the human-facing entry point for a Lean development on the sunflower extremal function

\[
f(n,k)=\min\{m:\text{ every }n\text{-uniform family of size at least }m\text{ contains a }k\text{-sunflower}\}.
\]

The formal sources currently live in the historical campaign archive at
`jaredwilder/erdos-campaign-archive/campaigns/erdos20-close-2026-09-05/`.
They form a coherent six-file program and should be migrated intact to a dedicated Erdős #20 repository when a repository shell is available.

## Formal results

The Lean development proves the following results about the same `f` and sunflower predicates used by the Formal Conjectures corpus.

### Erdős–Rado upper bound

For `n > 0` and `k >= 2`,

\[
f(n,k)\le (k-1)^n n!+1.
\]

`Attack01.lean` proves the finite sunflower lemma from scratch. `Attack02.lean` transfers it to the exact corpus definition of `f`.

### Product-construction lower bound

For `n > 0` and `k >= 2`,

\[
(k-1)^n < f(n,k).
\]

The witness is the usual transversal family of `n` disjoint blocks of size `k-1`, formalized in `Attack03.lean`.

Together the two bounds give

\[
(k-1)^n < f(n,k)\le (k-1)^n n!+1.
\]

The same file proves the exact boundary value

\[
f(1,k)=k \qquad (k\ge2).
\]

### Exact two-petal value

`Attack04.lean` proves, for every `n>0`,

\[
f(n,2)=2.
\]

It also packages a reusable lower-bound principle: any explicit `k`-sunflower-free `n`-uniform family of size at least `M` gives `M<f(n,k)`.

### Multiplication of sunflower-free witnesses

`Attack05.lean` proves that sunflower-free constructions multiply on disjoint ground sets. If there are witnesses of sizes `M_1,M_2` in uniformities `n_1,n_2`, then

\[
M_1M_2 < f(n_1+n_2,k).
\]

This turns any improved finite seed into an asymptotic lower-bound base.

### A stronger `k=3` seed

`Attack06.lean` uses the six edges of two disjoint triangles as a 3-sunflower-free 2-uniform family. Iterating the product theorem gives

\[
6^t < f(2t,3) \qquad (t\ge1),
\]

improving the elementary product-construction base from `2` to `sqrt(6)` along the even subsequence. In particular,

\[
6<f(2,3)\le9.
\]

## Formal trust footprint

`AXIOMS.txt` records 19 named declarations from the six files. Every recorded declaration has the axiom footprint

`[propext, Classical.choice, Quot.sound]`.

No `sorryAx` or `native_decide` appears in that recorded footprint. The finite six-edge seed is discharged by kernel reduction (`decide`), not `native_decide`.

## Source map

- `Attack01.lean` — finite Erdős–Rado sunflower lemma
- `Attack02.lean` — exact transfer to the Formal Conjectures definition of `f`
- `Attack03.lean` — transversal lower construction and the full sandwich
- `Attack04.lean` — lower-bound engine, `f(n,2)=2`, and the constraint on any exponential constant
- `Attack05.lean` — multiplication theorem for sunflower-free witnesses
- `Attack06.lean` — six-edge seed and the `6^t` lower bound for `k=3`
- `AXIOMS.txt` — recorded axiom footprints
- `SHA256SUMS.txt` — historical source hashes

## Scope

These results formalize classical bounds, exact boundary cases, a product principle, and an explicit strengthened lower construction. They do not by themselves settle the general asymptotic sunflower question.

The parent problem's status does not change the status of the proved statements above: those statements are the mathematical content of this program.
