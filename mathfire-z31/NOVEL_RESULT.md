# A computer-assisted Schur–Roth theorem in `Z/31Z`

## Theorem

Let `A` be a subset of the cyclic group `Z/31Z`. Assume both:

1. `A` is **sum-free** in the standard group sense: `(A + A) ∩ A = ∅`, with repeated summands allowed;
2. `A` contains no **nontrivial three-term arithmetic progression**: there are no three distinct `x,y,z ∈ A` with `x + z = 2y (mod 31)`.

Then

```text
|A| <= 6.
```

The bound is sharp. There are exactly **330** six-element sets satisfying both conditions.
Under multiplication by the 30 units of `Z/31Z`, those 330 extremal sets form exactly **12 orbits**: two orbits of size 15 and ten orbits of size 30.

One extremal witness is

```text
{1, 3, 7, 15, 20, 24}.
```

## Exact proof

The property is hereditary: if a set contains no solution-support for either forbidden linear equation, neither does any subset.
Therefore it is enough to establish both:

- at least one valid six-element subset exists;
- no valid seven-element subset exists.

MathFire exhaustively checked every one of the

```text
C(31,6) = 736,281
```

six-element subsets and every one of the

```text
C(31,7) = 2,629,575
```

seven-element subsets.

The direct search found 330 valid six-sets and zero valid seven-sets. A verifier with different loop orientation and reconstruction logic independently reproduced both counts. A separately compiled C program independently reproduced the counts and the orbit classification.

The sorted list of all 330 valid six-sets has SHA-256 digest:

```text
8fdf96cadc52fee0a0b6f8543a15d993489bf00ac12a2ac312cff93cccef2605
```

The complete orbit representatives and stabilizers are recorded in `receipts/round7-novel-result-proof.json`.

## Authority boundary

This is an exact finite computer-assisted theorem. Its mathematical correctness does not depend on the novelty search.

The separate novelty dossier records a systematic search of exact phrases, nearby terminology, arXiv, general web indexes, and OEIS. No prior source stating this exact maximum, extremal count, or unit-orbit classification was found. The defensible public wording is therefore:

> To the best of our knowledge, this exact `Z/31Z` theorem and classification are new.

That is not a claim that unpublished or unindexed prior work cannot exist.