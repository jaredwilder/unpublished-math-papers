# Erdős #359 — two universal invariants for the MacMahon segmented-number sequence

**Author:** Jared Wilder  
**Public extraction:** 2026-09-11  
**Status:** exact elementary structural theorems; parent asymptotic problem remains open

Let

\[
a_1=1<a_2<a_3<\cdots
\]

be the greedy segmented-number sequence: after `a_1,...,a_k` have been chosen, `a_{k+1}` is the least positive integer that cannot be represented as a sum of a consecutive block of already chosen terms.

The beginning of the true sequence is

`1, 2, 4, 5, 8, 10, 14, 15, ...`.

This note records two universal consequences of the greedy definition.

## Theorem 1 — reciprocal-prefix invariant

For every `k>=1`,

\[
\boxed{\sum_{i=1}^k \frac1{a_i}\ge 1.}
\]

### Proof

Set

\[
A=a_{k+1}-1.
\]

By the greedy definition, every integer `t` with `1<=t<=A` has at least one representation as a consecutive block

\[
t=a_i+a_{i+1}+\cdots+a_j
\]

using only the first `k` terms.

For a fixed starting index `i`, any block of length `ell` beginning at `a_i` has sum at least

\[
\ell a_i,
\]

because the sequence is increasing. Therefore the number of blocks beginning at `i` whose sum is at most `A` is at most

\[
\left\lfloor\frac A{a_i}\right\rfloor.
\]

Choose one representing block for each of the `A` distinct integers `1,...,A`. Blocks chosen for different integers are distinct, since their sums differ. Hence

\[
A
\le \sum_{i=1}^k\left\lfloor\frac A{a_i}\right\rfloor
\le A\sum_{i=1}^k\frac1{a_i}.
\]

Since `A>0`, division by `A` proves the claim.

## Theorem 2 — universal quadratic upper bound

For every `k>=1`,

\[
\boxed{a_{k+1}\le \frac{k(k+1)}2+1.}
\]

### Proof

Again every integer `1,...,a_{k+1}-1` has a consecutive-block representation using `a_1,...,a_k`.

There are exactly

\[
\binom{k+1}{2}=\frac{k(k+1)}2
\]

nonempty consecutive blocks of a `k`-term sequence. Distinct represented integers require distinct blocks. Thus

\[
a_{k+1}-1\le\frac{k(k+1)}2,
\]

which is the stated inequality.

## What these theorems say

The first theorem gives a persistent harmonic-density constraint on every prefix of the greedy sequence. The second gives a completely unconditional polynomial envelope on the next term.

Neither result determines the much finer asymptotic behavior of `a_k`; they are structural invariants, not a close of Erdős #359.

## Audit correction

A historical green receipt elsewhere in the estate encoded the wrong initial sequence value `a_2=5`. That receipt is not authority for this note. The proofs above use only the actual greedy definition and the true sequence beginning `1,2,4,5,...`.

## Priority boundary

The September 2026 estate audit performed targeted searches of the current problem page, discussion, and OEIS-facing literature summaries and did not locate these exact two formulations, especially the reciprocal-prefix inequality. Both arguments are elementary, so historical folklore risk remains substantial. Accordingly this release says **no exact hit located in targeted search**, not “globally novel.”

## Scope

- The reciprocal-prefix inequality is exact for every prefix.
- The quadratic upper bound is exact as an inequality for every `k`.
- No asymptotic equivalent for `a_k` is claimed here.
- Erdős #359 remains open at its asymptotic frontier.

## License

Apache-2.0 for repository-authored material.
