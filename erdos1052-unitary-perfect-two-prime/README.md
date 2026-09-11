# Erdős #1052 — unitary-perfect numbers with at most two prime factors

**Author:** Jared Wilder  
**Public extraction:** 2026-09-11  
**Status:** mathematically audited elementary theorem; not universally kernel-certified.

For `n=∏ p_i^{a_i}`, write the unitary divisor sum as

`σ*(n)=∏(p_i^{a_i}+1)`.

A unitary-perfect number satisfies `σ*(n)=2n`.

## Theorem

1. There is no odd unitary-perfect integer `n>1`.
2. Among unitary-perfect integers with at most two distinct prime factors, the only one is

`n=6`.

## Proof

If `n>1` is odd and has at least two distinct prime factors, every factor `p_i^{a_i}+1` is even, so `σ*(n)` is divisible by `4`, whereas `2n` has 2-adic valuation exactly `1`. If `n=p^a` is an odd prime power, `p^a+1=2p^a` would force `p^a=1`. Thus no odd example exists.

Now let a unitary-perfect number have at most two distinct prime factors. A pure power of `2` cannot work, so write

`n=2^a q^b`,

with `q` odd prime. The equation

`(2^a+1)(q^b+1)=2^{a+1}q^b`

rearranges to

`q^b(2^a-1)=2^a+1`.

Hence `2^a-1` divides `2`, because `(2^a+1)-(2^a-1)=2`. Since `2^a-1` is positive and odd, it must equal `1`; thus `a=1`. The displayed equation then gives `q^b=3`, so `q=3,b=1`, and `n=6`.

Directly, `σ*(6)=(2+1)(3+1)=12=2·6`.

## Scope

This classifies only the at-most-two-distinct-prime-factor stratum. It is not a classification of all unitary-perfect numbers.
