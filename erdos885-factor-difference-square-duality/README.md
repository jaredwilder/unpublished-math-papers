# Erdős #885 — factor-difference / square duality

**Author:** Jared Wilder  
**Public extraction:** 2026-09-11  
**Status:** mathematically audited exact equivalence.

For `N>=1`, let

`D(N) = { |a-b| : a,b positive integers, ab=N }`.

## Theorem

For every integer `d>=0`,

`d ∈ D(N)`

if and only if there exists an integer `s>=0` such that

`s² = d² + 4N`.

Equivalently, factor-difference questions for `N` are exactly integral-point questions on

`s²-d²=4N`.

## Proof

If `N=ab` and `d=|a-b|`, then

`d²+4N = (a-b)²+4ab = (a+b)²`,

so take `s=a+b`.

Conversely, suppose

`s²=d²+4N`.

Then `(s-d)(s+d)=4N`. Since `s²-d²` is divisible by `4`, `s` and `d` have the same parity. Put

`a=(s+d)/2`, `b=(s-d)/2`.

These are positive integers, satisfy `ab=N`, and `|a-b|=d`.

## Use

Intersections of factor-difference sets become simultaneous-square constraints. This was recovered as a clean child theorem after a larger LCM-based route in the source campaign failed; the failed global route is not part of this theorem.
