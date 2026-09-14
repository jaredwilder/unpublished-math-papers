# A corrected pairwise-powers-of-two lemma recovered from the #126 estate

**Author:** Jared Wilder  
**Public release:** 2026-09-14  
**Status:** elementary exact lemma; no novelty claim; not a new resolution of Erdős #126

## Theorem

There do not exist three distinct **positive** integers `x,y,z` such that all three pairwise sums

\[
x+y,\qquad x+z,\qquad y+z
\]

are powers of two.

### Proof

Assume

\[
0<x<y<z
\]

and write

\[
x+y=2^p,\qquad x+z=2^q,\qquad y+z=2^r.
\]

The strict ordering of the sums gives

\[
p<q<r.
\]

Adding the first two equations and subtracting the third gives

\[
2x=2^p+2^q-2^r.
\]

But `p<q` implies

\[
2^p\le2^{q-1},
\]

while `r>q` implies

\[
2^r\ge2^{q+1}.
\]

Hence

\[
2^p+2^q
\le3\cdot2^{q-1}
<2^{q+1}
\le2^r,
\]

so the right-hand side is negative. This contradicts `x>0`.

Therefore no such positive triple exists. ∎

## Why the positivity hypothesis is load-bearing

An earlier theorem-bank version silently widened the domain from positive integers to all integers. That version is false:

\[
\{-1,3,5\}
\]

has pairwise sums

\[
2,4,8.
\]

So the correct reusable theorem is the **positive-integer** statement above.

## Scope relative to Erdős #126

This lemma arose in the historical #126 campaign, but it is not represented here as a solution of the canonical problem. It is a clean standalone arithmetic obstruction recovered from the estate and published with its corrected domain.

The current public record for Erdős #126 changed substantially in September 2026; this packet makes no priority or canonical-status claim. Its purpose is to preserve exactly the mathematics that survived the estate audit.

## Provenance

A raw Pass-3 certifier row records the positive theorem as an exact integer certificate. The broader Release-Day quarantine layer separately records the integer-domain counterexample above.
