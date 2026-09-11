# Erdős #371 — consecutive integers cannot share the same largest prime factor

**Author:** Jared Wilder  
**Public extraction:** 2026-09-11  
**Status:** elementary exact theorem; parent density question remains open.

Let `P(n)` denote the largest prime factor of `n` for `n>=2`.

## Theorem

For every `n>=2`,

`P(n) != P(n+1)`.

## Proof

If `P(n)=P(n+1)=p`, then the same prime `p` divides both `n` and `n+1`. Hence

`p | gcd(n,n+1)=1`,

impossible.

## Scope

This only excludes exact ties between consecutive largest-prime-factor values. It does not determine the sign of `P(n+1)-P(n)` or settle any density statement about which side is larger.
