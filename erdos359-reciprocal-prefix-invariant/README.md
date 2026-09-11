# Erdős #359 — reciprocal-prefix invariant for the true greedy sequence

**Author:** Jared Wilder  
**Recovered from:** September 2026 theorem audit  
**Public extraction:** 2026-09-11

## Theorem

For the true `n=1` MacMahon / segmented-number greedy sequence `a_1,a_2,...` used in the frozen
Erdős #359 formulation,

\[
\boxed{\sum_{i=1}^{k}\frac1{a_i}\ge1\qquad\text{for every }k.}
\]

## Proof capsule

By the defining greedy property, every positive integer

\[
t<a_{k+1}
\]

has a contiguous representation using the current prefix. For a fixed starting term `a_i`, the
number of contiguous sums starting there that can remain below `a_{k+1}` is at most

\[
\left\lfloor\frac{a_{k+1}-1}{a_i}\right\rfloor.
\]

All integers `1,...,a_{k+1}-1` must be represented, so counting the available starting-position
capacities gives

\[
a_{k+1}-1
\le
\sum_{i=1}^{k}
\left\lfloor\frac{a_{k+1}-1}{a_i}\right\rfloor
\le
(a_{k+1}-1)\sum_{i=1}^{k}\frac1{a_i}.
\]

Dividing by `a_{k+1}-1>0` yields the claimed invariant.

## Correction boundary

A separate historical green receipt in the campaign encoded the wrong initial value `a_2=5`.
That receipt is **not** evidence for this theorem and should remain quarantined. The invariant above
is attached to the true greedy definition and its independent counting proof.

## Novelty boundary

The September audit checked the live problem page/discussion and nearby sources by Andrews,
Porubský and OEIS A002048 and did not locate this exact reciprocal-prefix inequality. Because the
argument is elementary, folklore risk remains. The safe status is **apparently unrecorded in the
targeted search**, not a global priority guarantee.

## License

Apache-2.0 for repository-authored material.
