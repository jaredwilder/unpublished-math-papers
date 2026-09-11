# Erdős #602 — every countable family of infinite sets is bichromatically 2-colorable

**Author:** Jared Wilder  
**Public extraction:** 2026-09-11

The historical campaign stated the theorem under the stronger hypothesis that the sets are countably infinite and pairwise have finite intersections. The finite-intersection hypothesis is unnecessary for the countable-family conclusion.

## Theorem

Let

\[
\mathcal A=\{A_1,A_2,\ldots\}
\]

be a countable family of infinite sets. Then the union admits a red/blue coloring such that every `A_i` contains at least one red point and at least one blue point.

## Proof

Proceed recursively. At stage `i`, only finitely many points have been deliberately selected at earlier stages. Since `A_i` is infinite, choose two previously unselected points

\[
r_i,b_i\in A_i.
\]

Color `r_i` red and `b_i` blue. After all stages, color every still-uncolored point arbitrarily.

For each `i`, the two selected witnesses `r_i,b_i` remain oppositely colored and both lie in `A_i`. Hence every member of the family is bichromatic.

## Scope

This disposes of the countable-family stratum. The corresponding uncountable-family problem is separate. No novelty claim is made for this elementary strengthening.
