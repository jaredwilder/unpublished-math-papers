# Erdős #886 — the easy `epsilon >= 1/2` divisor-window endpoint

**Author:** Jared Wilder  
**Public extraction:** 2026-09-11  
**Status:** exact solved parameter stratum.

Consider a divisor-count question in the short interval

`(sqrt(n), sqrt(n)+n^(1/2-epsilon))`.

## Theorem

For every `epsilon>=1/2`, that interval contains at most one integer. Hence any bound asking for a uniform maximum number of divisors in the interval holds with

`K=1`.

## Proof

If `epsilon>=1/2`, then

`n^(1/2-epsilon) <= 1`.

The displayed interval therefore has length at most `1`. An open interval of length at most `1` contains at most one integer, and hence at most one divisor of `n`.

## Scope

This completely removes the `epsilon>=1/2` range. The substantive regime is `0<epsilon<1/2`.
