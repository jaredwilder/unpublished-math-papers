# Erdős #412 — forward sigma-orbits are strictly increasing above 1

**Author:** Jared Wilder  
**Public extraction:** 2026-09-11  
**Status:** elementary exact theorem; intersections of different orbits remain outside this result.

Let `sigma(n)` be the sum of the positive divisors of `n`.

## Theorem

For every `n>=2`,

`sigma(n) >= n+1 > n`.

Consequently every forward orbit

`n, sigma(n), sigma(sigma(n)), ...`

starting from `n>=2` is strictly increasing and contains no repetitions.

## Proof

The positive divisors `1` and `n` are distinct when `n>=2`, so both occur in the divisor sum. Therefore

`sigma(n) >= 1+n > n`.

Applying the same inequality at each subsequent value gives strict increase throughout the forward orbit.

## Scope

This rules out cycles and self-intersections within one forward orbit above 1. It does not prove that two distinct starting values have disjoint orbits.
