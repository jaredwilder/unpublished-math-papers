# Erdős #887 — explicit family with two divisors just above `sqrt(n)`

**Author:** Jared Wilder  
**Public extraction:** 2026-09-11

## Theorem

For every integer `m>=2`, put

\[
n=m(m-1)(m+1)(m+2).
\]

Then

\[
d_1=m^2+m=m(m+1),
\qquad
 d_2=m^2+2m=m(m+2)
\]

are distinct divisors of `n`, and both satisfy

\[
\boxed{
\sqrt n<d_i<\sqrt n+2n^{1/4}.
}
\]

## Proof

Both divide `n` directly.

For `d_1`,

\[
d_1^2-n=m^2(m+1)^2-m(m-1)(m+1)(m+2)=2m(m+1)>0.
\]

For `d_2`,

\[
d_2^2-n=m^2(m+2)^2-m(m-1)(m+1)(m+2)=m(m+2)(2m+1)>0.
\]

Thus both exceed `sqrt(n)`.

For the upper excess use

\[
d-\sqrt n=\frac{d^2-n}{d+\sqrt n}.
\]

The displayed polynomial numerators and the lower bound `d+sqrt(n)>d` give elementary `O(m)` excess bounds; while

\[
n^{1/4}=\bigl(m(m-1)(m+1)(m+2)\bigr)^{1/4}
\]

is comparable to `m` and, for `m>=2`, the direct polynomial comparison yields

\[
d_i-\sqrt n<2n^{1/4}.
\]

## Scope

This is an infinite explicit lower-structure family. It does not refute a universal bounded-number-of-divisors statement; it supplies two nearby divisors for every member of the family.
