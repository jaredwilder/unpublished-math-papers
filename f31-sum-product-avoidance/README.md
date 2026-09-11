# Simultaneous additive and multiplicative avoidance in F_31

**Author:** Jared Wilder  
**Source:** MathFire Round 10  
**Public release:** 2026-09-11

## Theorem

Let `A ⊆ F_31* = {1,...,30}`. Suppose there are no `x,y,z ∈ A`, with repetitions allowed, satisfying either

```text
x + y = z (mod 31)
```

or

```text
x y = z (mod 31).
```

Then

```text
|A| ≤ 8.
```

The bound is sharp. Exactly **nine** eight-element extremizers exist:

```text
{2,3,7,15,16,24,28,29}
{2,3,10,15,16,21,28,29}
{2,3,12,13,18,19,28,29}
{2,5,9,15,16,22,26,29}
{2,5,11,14,17,20,26,29}
{2,6,7,15,16,24,25,29}
{2,6,11,15,16,20,25,29}
{2,9,10,15,16,21,22,29}
{10,12,13,15,16,18,19,21}
```

Canonical extremizer digest:

`9e8335483eecaf3e5e7dcb747053613dabf848c24734126330551d5327901d17`

## Exact finite proof

The property is hereditary. Exhaustive canonical increasing-extension enumeration gives the complete size distribution

```text
size 0:    1
size 1:   29
size 2:  353
size 3: 1866
size 4: 3532
size 5: 2072
size 6:  483
size 7:   76
size 8:    9
size 9:    0
```

Thus valid eight-sets exist, no valid nine-set exists, and heredity excludes every larger set.

`verification/mixed_sum_product_f31_independent.c` is an independent C verifier. It tests the defining equations directly, shares no MathFire search/hypergraph implementation, visits 8,421 valid search states, and reproduces the complete distribution and all nine extremizers.

Compile with:

```bash
cc -O2 -std=c11 -Wall -Wextra -pedantic verification/mixed_sum_product_f31_independent.c -o verify
./verify
```

The sealed source receipt records verifier source SHA-256 `071114edde1b5928e0813f40978a5439baef062bdb21c1ffb289a093ffe71c1e` and independent-output SHA-256 `bb97041645e1a5d3392cb6b1594694587b3a1281a561465d7a96777585f39a25`.

## Novelty boundary

Historical novelty is separate from mathematical correctness. The source campaign's literature search found no collision for this exact finite-field classification. The authorized wording is:

> Apparently new after systematic search; to the best of our knowledge, this exact theorem and classification are new.

That is a search conclusion, not a proof of historical nonexistence. See `NOVELTY.md`.