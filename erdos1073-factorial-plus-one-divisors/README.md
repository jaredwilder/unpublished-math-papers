# Erdős #1073 — divisor shape of `n!+1`

**Author:** Jared Wilder  
**Public extraction:** 2026-09-11  
**Status:** mathematically audited elementary theorem; parent problem remains open.

## Theorem

Let `u>1` divide `n!+1`. Then every prime divisor `p` of `u` satisfies

`p>n`.

In particular, if `u` is composite, then

`u>n²`.

## Proof

If a prime `p<=n` divided `u`, then `p|n!`. Since `u|n!+1`, the same prime would also divide `n!+1`, so it would divide their difference `1`, impossible. Thus every prime divisor of `u` is larger than `n`.

If `u` is composite, its prime factorization contains at least two prime factors counted with multiplicity. Each exceeds `n`, so `u>n²`.

## Scope boundary

The source campaign contained stronger proposed consequences about counting such divisors and Wilson-type prime-power behavior. Those are **not** implied by this lemma and are not released here as theorems. This packet preserves only the exact divisor-shape statement that survived audit.
