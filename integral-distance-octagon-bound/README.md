# Integral point sets in general position: a 30,000 lower bound for the octagon

**Author:** Jared Wilder  
**Campaign date:** 2026-07-25  
**Public release:** 2026-09-11

## Result 1 — both published Kreisel–Kurz heptagons are maximal

Let an **integral point set in general position** be a finite subset of the Euclidean plane with all pairwise distances integral, no three points collinear, and no four concyclic.

Kreisel and Kurz exhibited two seven-point examples, here called `H1` and `H2`, with diameters

- `diam(H1)=22270`,
- `diam(H2)=66810`.

The campaign proves, by exhaustive exact arithmetic:

> **Theorem A.** There is no point `X` in the plane, other than the existing seven vertices, whose distance to every vertex of `H1` is integral. The same holds for `H2`.

Hence neither known heptagon admits an integral eighth point.

This is an **unbounded-plane** statement. It is not a bounded-box search. The exhaustive parameterization is finite because the triangle inequality forces distance differences

`c_j = |XP_b|-|XP_j|`

to be integers in the finite intervals

`-d_bj <= c_j <= d_bj`,

independently of how far `X` is from the configuration. Every resulting cell reduces to an exact integer-algebraic consistency test.

## Result 2 — new lower bound for the eight-point diameter

Write `d_dot(2,n)` for the minimum diameter of an `n`-point integral set in the plane in general position.

Kreisel–Kurz proved by exhaustive orderly generation that

`d_dot(2,7)=22270`

and that their diameter-22270 heptagon `H1` is the **only** integral general-position heptagon of diameter at most `30000`.

Combining that published uniqueness result with Theorem A gives:

> **Theorem B.** `d_dot(2,8) > 30000`.

### Proof

Assume an eight-point integral general-position set `P` has diameter at most `30000`. Every seven-point subset of `P` is again integral and in general position, with diameter at most `30000`. By the Kreisel–Kurz exhaustive classification, each such seven-subset is congruent to `H1`. In particular, deleting one point from `P` gives a copy of `H1`, so the deleted point would be an integral extension of `H1`. Theorem A says no such extension exists. Contradiction.

Therefore every integral octagon in general position, if one exists at all, has diameter strictly greater than `30000`.

## Exact computation

The original producer performed three exact sweeps:

- `H1`: `136,801,313` cells using one base triple;
- `H1`: `205,982,337` cells using an independent base triple;
- `H2`: `1,335,425,575` cells.

Total: approximately **1.678 billion exact cells**. No floating-point comparison was used in the decision path.

A later independent checker was required because repeated runs of the same producer are not independent verification. The checker used different algebra: linear differencing of squared-distance equations followed by an exact `2×2` solve, rather than the producer's quadratic-cell formulation. It also chose its own base triple and did not assume in advance that the unknown point lay in `Q(sqrt(2002))`.

The independent verdict was:

- `H1`: PASS, `136,801,313` cells, returning exactly the seven known vertices;
- `H2`: PASS, `1,335,425,575` cells, returning exactly the seven known vertices.

Two defects discovered while constructing that checker are preserved in `VERIFICATION.md` because they are part of the proof audit.

## Scope

This does **not** prove that no eight-point integral set in general position exists. It proves only that:

1. neither of the two known Kreisel–Kurz heptagons extends to eight points; and
2. any integral octagon in general position must have diameter greater than `30000`.

An octagon of larger diameter built from a different seven-point subsystem remains possible.

## Prior work and novelty boundary

The external input is Tobias Kreisel and Sascha Kurz, *There are integral heptagons, no three points on a line, no four on a circle*, Discrete & Computational Geometry 39 (2008), 786–790, arXiv:0804.1303. Their paper gives the two heptagons, proves `d_dot(2,7)=22270`, and states that the diameter-22270 example is the only one with diameter at most `30000`.

As of the 2026-09-11 release sweep, OEIS A096873 still lists the sequence only through `n=7`, with no value for `n=8`. A web/literature search found no prior publication of the `>30000` octagon bound or the maximality of these two specific heptagons. The defensible wording is therefore:

> **Apparently new after systematic search; to the best of our knowledge, Theorems A and B were not previously published.**

That is a historical-search statement, not a logical proof that no obscure or unpublished prior result exists.