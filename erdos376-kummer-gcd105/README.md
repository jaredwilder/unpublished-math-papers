# Erdős #376 — Kummer carry criterion for `gcd(C(2n,n),105)`

**Author:** Jared Wilder  
**Public extraction:** 2026-09-11  
**Status:** mathematically audited exact reformulation; residual infinitude question remains open.

## Theorem

Because `105=3·5·7`,

`gcd(C(2n,n),105)=1`

if and only if adding `n+n` produces no carry in any of bases `3`, `5`, and `7`.

Equivalently:

- every base-3 digit of `n` is at most `1`;
- every base-5 digit of `n` is at most `2`;
- every base-7 digit of `n` is at most `3`.

## Proof

Kummer's theorem states that

`v_p(C(2n,n))`

is exactly the number of carries occurring when adding `n+n` in base `p`.

Therefore `p` does not divide the central binomial coefficient iff no carry occurs in base `p`.

At one digit `d`, doubling creates no carry precisely when

`2d < p`,

or equivalently

`d <= (p-1)/2`.

Apply this independently for `p=3,5,7`. Since `105` is squarefree, avoiding divisibility by all three primes is equivalent to coprimality with `105`.

## Scope

This converts the divisibility condition into an exact digital condition. It does not by itself prove the parent campaign's infinitude statement.
