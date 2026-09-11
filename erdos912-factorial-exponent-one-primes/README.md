# Erdős #912 — primes occurring to exponent one in `n!`

**Author:** Jared Wilder  
**Public extraction:** 2026-09-11  
**Status:** exact valuation characterization.

## Theorem

For a prime `p`,

`v_p(n!)=1`

if and only if

`n/2 < p <= n`.

Consequently the number of primes whose exponent in `n!` is exactly one equals

`pi(n)-pi(floor(n/2))`.

## Proof

Legendre's formula gives

`v_p(n!) = floor(n/p)+floor(n/p^2)+...`.

If `n/2<p<=n`, then `floor(n/p)=1` and `p^2>n`, so every later term vanishes; hence the valuation is `1`.

Conversely, if `v_p(n!)=1`, then necessarily `floor(n/p)=1`, so `n/2<p<=n`.

Counting such primes gives the displayed prime-counting difference.

## Scope

This isolates one exact exponent stratum of the factorial factorization. It does not determine the full number of distinct exponent values occurring in `n!`.
