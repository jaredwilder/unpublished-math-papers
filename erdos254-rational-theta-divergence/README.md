# Erdős #254 — exact rational-`theta` divergence criterion

**Author:** Jared Wilder  
**Public extraction:** 2026-09-11  
**Status:** exact characterization of the rational-parameter part of the hypothesis.

Let `A⊂N`, and let

`theta=a/q ∈ (0,1)`

be rational in lowest terms. Write `||x||` for distance from `x` to the nearest integer.

## Theorem

The series

`Σ_{n∈A} ||theta n||`

diverges if and only if `A` contains infinitely many integers not divisible by `q`.

## Proof

If `q|n`, then `theta n=an/q` is an integer, so the summand is `0`.

If `q` does not divide `n`, then, because `gcd(a,q)=1`, the residue `an mod q` is nonzero. Therefore the fractional part of `an/q` is one of

`1/q,2/q,...,(q-1)/q`.

Its distance to the nearest integer is consequently at least `1/q`.

Thus infinitely many `n∈A` with `q∤n` contribute at least `1/q` each, forcing divergence. If only finitely many such `n` occur, all remaining summands vanish, so the series is finite.

## Scope

This exactly characterizes the rational-`theta` portion of the parent hypothesis. It does not prove the parent subset-sum conclusion or address irrational `theta`.
