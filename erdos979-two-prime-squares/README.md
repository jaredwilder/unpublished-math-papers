# Erdős #979 — parity obstruction and an exact collision for two prime squares

**Author:** Jared Wilder  
**Public extraction:** 2026-09-11

Under the frozen campaign convention, let `f_2(n)` count unordered representations

\[
n=p^2+q^2
\]

with primes `p,q`, allowing the campaign's unordered-multiset semantics.

## Parity obstruction

If

\[
n\equiv3\pmod4,
\]

then

\[
\boxed{f_2(n)=0.}
\]

Indeed an odd prime square is `1 mod 4`, while `2^2=4` is `0 mod 4`. A sum of two prime squares can therefore be only `0,1,2 mod 4`, never 3.

## Exact collision at 410

There are at least two distinct unordered representations:

\[
410=7^2+19^2=49+361,
\]

and

\[
410=11^2+17^2=121+289.
\]

Thus

\[
\boxed{f_2(410)\ge2.}
\]

The historical finite audit records equality `f_2(410)=2` under its exact semantics; the two displayed representations themselves are independently checkable without trusting that enumeration.

## Scope

This packet records a universal congruence obstruction and a finite collision. It makes no new asymptotic claim.
