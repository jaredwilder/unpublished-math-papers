# Finite Hardy–Littlewood admissibility counting for prime-gap constellations

**Author:** Jared Wilder  
**Campaign date:** 2026-05-23  
**Public release:** 2026-09-10/11  
**Status:** formal finite-combinatorial packet recovered from the estate. **No asymptotic prime-gap theorem is claimed.**

## What survived the campaign

The durable mathematical core is a finite counting problem for residue constellations, formalized in a Lean/mathlib chain under names including:

```text
PrimeGapInclusionExclusion
PrimeGapIEChain
PrimeGapAdmissibleClosedForm
PrimeGapHLBridge
PrimeGapMod2Exact
PrimeGapMod2General
PrimeGapMod3General
PrimeGapSurjectionBoundary
PrimeGapPermBoundary
```

The source campaign defines finite tuples of residues/increments, the residue set reached by `{0, partial sums}`, and an `admissibleCount p k` counting the tuples that do **not** cover every residue class modulo `p`.

## Source-recorded inclusion–exclusion formula

The campaign records the closed form

\[
\operatorname{admissibleCount}(p,k)
= p^{k-1}
- \sum_{t\subseteq \operatorname{nonzeroRes}(p)}
(-1)^{|t|}(p-|t|)^{k-1}.
\]

This is a finite inclusion–exclusion identity inside the declared residue-coverage model. It is not a statement about the asymptotic distribution of primes.

## Exact specializations recorded in the formal chain

### Modulo 2

\[
\forall k,\qquad \operatorname{admissibleCount}(2,k)=1.
\]

### Modulo 3

For `k≥1`,

\[
\operatorname{admissibleCount}(3,k)=2^k-1.
\]

## First-cover boundary: finite witnesses

The campaign also records the following exact values at `k=p`:

\[
\operatorname{admissibleCount}(3,3)=7=9-2,
\]

\[
\operatorname{admissibleCount}(5,5)=601=625-24,
\]

\[
\operatorname{admissibleCount}(7,7)=116929=117649-720.
\]

The complementary cover counts were matched to permutation counts in these three cases:

\[
\operatorname{coversCount}(3,3)=2!=(2),
\]

\[
\operatorname{coversCount}(5,5)=4!=24,
\]

\[
\operatorname{coversCount}(7,7)=6!=720.
\]

## Open boundary theorem

The source campaign explicitly left the general theorem

\[
\operatorname{coversCount}(p,p)=(p-1)!
\]

**open**. The expected proof route is a bijection between first-cover tuples and permutations/surjections onto the nonzero residue classes. The finite `p=3,5,7` witnesses do not prove the universal formula.

## Hardy–Littlewood bridge

The formal packet also defined finite residue coverage predicates such as `coverAllResidues p H` and `isHLAdmissibleAt`, connecting residue coverage to the standard finite notion of Hardy–Littlewood admissibility of a constellation at a prime modulus.

This is the correct scope of the formal contribution: **finite residue combinatorics and its admissibility bridge**.

## Additional exact finite observations retained from the campaign

The estate records, with mixed formal/computational authority:

- modulo 30, **175 / 900** two-step residue-transition cells are structurally reachable;
- small-`k` admissibility fractions recorded as
  - `k=3`: `7/36`,
  - `k=4`: `5/72`,
  - `k=5`: `18631/810000`;
- the `7/36` value was checked across moduli `30`, `210`, and `2310`;
- a modulo-2310 reachable-cell count of `1,037,575` was recorded as matching the formal prediction.

These finite counts are retained as campaign outputs, not promoted here to new asymptotic number theory.

## Audit warning from the original session

The original final dossier said “74 Lean theorems across 8 modules,” while its own inventory listed 9 modules and the displayed per-module counts appeared to total 71 rather than 74. Therefore this release does **not** repeat either theorem/module total as an audited fact.

Before claiming complete kernel coverage of the original source tree, the estate requires a fresh clean compile and theorem counter over the actual `.lean` files.

## Claims explicitly rejected

This packet does **not** claim:

- Cramér's conjecture is proved;
- Granville's refinement is proved;
- any new asymptotic prime-gap law is established;
- Lemke Oliver–Soundararajan is superseded;
- empirical residue biases are globally novel;
- the general `coversCount(p,p)=(p-1)!` theorem is proved.

The strongest durable release is the finite combinatorial/formal admissibility-counting program above.
