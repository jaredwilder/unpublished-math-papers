# Erdős #826 — divisor-bound tail elimination

**Author:** Jared Wilder  
**Public extraction:** 2026-09-11  
**Status:** mathematically audited elementary reduction.

## Lemma

For positive integers `n,k` with

`k > sqrt(n)`, 

one has

`τ(n+k) < 3k`,

where `τ` is the divisor-counting function.

Consequently, whenever a target estimate of the form

`τ(n+k) <= C k`

has already been proved on the range `k <= sqrt(n)`, the complementary range follows automatically with constant `3`; the global bound holds with constant `max(C,3)`.

## Proof

Use the elementary bound

`τ(m) <= 2 sqrt(m)`.

Since `k>sqrt(n)`, we have `n<k²`, hence

`n+k < k²+k <= 2k²`

for `k>=1`. Therefore

`τ(n+k) <= 2 sqrt(n+k) < 2 sqrt(2) k < 3k`.

## Role

This is a tail-elimination lemma: it isolates all genuine difficulty to `k<=sqrt(n)` and prevents effort from being spent on the automatically controlled large-`k` region.
