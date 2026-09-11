# Erdős #774 — finite union of dissociated sets implies proportional dissociation

**Author:** Jared Wilder  
**Public extraction:** 2026-09-11  
**Status:** exact easy direction of the parent equivalence question.

A set is **dissociated** if it has no nontrivial relation

`Σ ε_i a_i = 0`, with `ε_i∈{-1,0,1}`,

using finitely many distinct elements.

## Theorem

Suppose

`A = D_1 ∪ ... ∪ D_k`

with each `D_i` dissociated. Then every finite set `B⊂A` contains a dissociated subset of size at least

`|B|/k`.

Equivalently, `A` is proportionately dissociated with constant at least `1/k`.

## Proof

The finite set `B` is covered by the `k` sets `B∩D_i`. By pigeonhole, for some `i`,

`|B∩D_i| >= |B|/k`.

Every subset of a dissociated set is dissociated, so `B∩D_i` is the required subset.

## Scope

This is the easy converse direction. The difficult direction asks whether an a priori proportional-dissociation property forces a finite union decomposition into dissociated sets.
