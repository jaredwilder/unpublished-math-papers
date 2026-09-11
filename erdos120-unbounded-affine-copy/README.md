# Erdős #120 — the unbounded-set affine-copy subcase

**Author:** Jared Wilder  
**Public extraction:** 2026-09-11  
**Status:** exact elementary subcase; bounded infinite sets remain the substantive regime.

## Theorem

Let `A⊂R` be unbounded. Then the positive-measure set

`E=[0,1]`

contains no nondegenerate affine copy

`aA+b`

with `a!=0`.

## Proof

If `A` is unbounded and `a!=0`, then multiplication by `a` and translation by `b` preserve unboundedness. Thus `aA+b` is unbounded.

But every subset of `[0,1]` is bounded. Therefore

`aA+b` cannot be contained in `[0,1]`.

Since `[0,1]` has positive Lebesgue measure, it is the required avoiding set for every unbounded `A`.

## Scope

This removes all unbounded `A` from the difficult part of the parent problem. It says nothing about bounded infinite sets, where nondegenerate affine copies remain bounded and the above obstruction disappears.
