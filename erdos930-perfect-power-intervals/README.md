# Erdős #930 — perfect-power products of disjoint intervals

**Author:** Jared Wilder  
**Public extraction:** 2026-09-11  
**Status:** exact partial results and infinite obstruction family; parent problem remains open.

## Frozen problem

For every `r`, does there exist a `k` such that whenever `I_1,...,I_r` are pairwise-disjoint intervals of consecutive positive integers, all of length at least `k`, the total product

`∏_{i=1}^r ∏_{m∈I_i} m`

is not a perfect power?

The material below concerns the `r=2` lower-threshold side only.

## Theorem 1 — infinite length-2 square-product family

For every nontrivial positive solution of the Pell equation

`x² - 24 y² = 1`

with `x>5`, put

`a=(x-1)/2`.

Then `a` is a positive integer and

`a(a+1)=6y²`.

Hence the two disjoint consecutive intervals

`I_1={2,3}` and `I_2={a,a+1}`

have square total product:

`∏I_1 · ∏I_2 = 6a(a+1) = (6y)²`.

Since the Pell equation has infinitely many positive solutions, there are infinitely many exact `r=2`, length-2 square-product examples.

### Proof

From `x²-24y²=1`, `x` is odd, so `a=(x-1)/2` is integral. Then

`4a(a+1)=(x-1)(x+1)=x²-1=24y²`,

therefore `a(a+1)=6y²`. The product of `{2,3}` is `6`, so the combined product is `36y²=(6y)²`.

## Theorem 2 — exact length-3 obstruction to any threshold below 4

The disjoint intervals

`{1,2,3}` and `{48,49,50}`

have total product

`1·2·3·48·49·50 = 705600 = 840²`.

Therefore any `k` that could work for `r=2` in the frozen problem must satisfy

`k ≥ 4`.

This is an exact theorem: a purported threshold `k≤3` would have to rule out every pair of disjoint intervals whose lengths are at least `k`, but the displayed length-3 pair is already a counterexample.

## Additional finite record

The source campaign also records:

- `{1,2}` and `{8,9}` give `144=12²`;
- exact verification of the displayed length-2 and length-3 witnesses;
- for the special shape `{1,2,3,4} × {t,t+1,t+2,t+3}`, no square-product example was found for `t≤10^6` by the preserved exact integer verifier.

That last item is **finite computation only**. It is not a proof that length 4 works, and it does not close the parent problem.

## What remains open

The recovered campaign explicitly refused to turn the absence of a small `k=4` witness into a global theorem. The `r=2` problem for arbitrary interval placements at length `≥4`, and the full `∀r ∃k` statement, remain outside this release.

## Provenance

Recovered from the September 2026 Day-2 theorem estate and the Erdős #930 forensic card. Source statuses include `MANUAL_EXACT`, `PROVED` finite certificate, and finite `COMPUTATION_SUPPORTED` records. The Pell family is an exact elementary derivation; no novelty claim is made here without a separate literature review.
