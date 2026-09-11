# Erdős #156 — repaired maximal-Sidon N^(1/3) barrier

**Author:** Jared Wilder  
**Recovered from:** September 2026 proof-repair audit  
**Public extraction:** 2026-09-11

## Theorem

Let `A⊆[N]` be a maximal Sidon set and put `m=|A|`. Then

\[
\boxed{N\le m+m^3+m^2.}
\]

In particular

\[
N\le m+2m^3
\]

for `m>=1`, so

\[
\boxed{m=\Omega(N^{1/3}).}
\]

## Why a repair was necessary

The raw campaign argument claimed that every `x∉A` lies in a set of the form

\[
(A+A)-A.
\]

That is incomplete. Adding `x` to a Sidon set can also create a collision in which `x` appears
twice:

\[
2x=a+b.
\]

The September audit rejected the raw inclusion and supplied the missing blocker.

## Correct blocker dichotomy

Because `A` is maximal, for every `x∈[N]\A`, the enlarged set `A∪{x}` is not Sidon. Hence two
unordered pair-with-repetition sums coincide in `A∪{x}`.

Since all sums internal to `A` were already distinct, the new collision must involve `x`. There are
only two essential forms:

1. `x+a=b+c` for some `a,b,c∈A`;
2. `2x=a+b` for some `a,b∈A`.

Thus the number of possible excluded `x` is at most `m^3+m^2` by a deliberately coarse union bound.
Adding the `m` members of `A` itself yields

\[
N\le m+m^3+m^2.
\]

This proves the theorem.

## Scope boundary

This is a universal analytic lower barrier for maximal Sidon sets, not a close of the parent problem.
The point of this release is also methodological: the conclusion survives, but only after the broken
proof is replaced. The false `A+A-A`-only derivation remains part of the public correction record.

Historical novelty is not claimed; the audit treats this as an elementary repaired theorem with
substantial folklore risk.

## License

Apache-2.0 for repository-authored material.
