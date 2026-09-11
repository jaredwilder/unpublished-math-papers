# Kirkman's Steiner triple-system existence theorem — Lean formalization record

**Author:** Jared Wilder  
**Campaign date:** 2026-07-24  
**Public estate release:** 2026-09-11

## Canonical public source

The original archive note said the Lean source had not been recovered into the public GitHub estate. That statement became stale during release-day reconstruction.

The canonical public source is now:

`jaredwilder/lean-contributions/mathlib-pr/Mathlib/Combinatorics/Design/SteinerTriple.lean`

with packaging notes at:

`jaredwilder/lean-contributions/mathlib-pr/PR-NOTES.md`.

The committed development is **1,473 lines**, imports `Mathlib`, contains **0 `sorry`**, and formalizes both necessity and sufficiency for Kirkman's theorem. The canonical `lean-contributions` README records **31 top-level theorem declarations (32 counting one indented declaration) and 38 lemmas**, together with the measured axiom footprint.

This archive directory is therefore **provenance only**. Do not treat it as a missing-source project or as a competing canonical home.

## The theorem

A Steiner triple system of order `v` exists if and only if

`v ≡ 1 or 3 (mod 6)`.

This is Kirkman's classical 1847 theorem, not new mathematics.

## What the formalization contributes

The public Lean development proves both directions:

- necessity from the abstract Steiner-triple-system structure by double counting;
- sufficiency by formalized Bose construction for `v ≡ 3 (mod 6)`;
- sufficiency by formalized Skolem construction for `v ≡ 1 (mod 6)`;
- the exactly-one-block property for the constructed systems.

The necessity route derives:

1. ordered-pair fiber counting, giving `6 | v(v-1)`;
2. point-fiber counting, forcing `v` odd;
3. hence `v ≡ 1 or 3 (mod 6)`.

## Priority boundary

The campaign recorded that Mathlib itself had no Steiner triple-system development at the time. Isabelle/AFP already contained design-theory formalization, so this release makes no first-anywhere formalization claim.

For mathematical reading, verification, citation, or future upstreaming, use `jaredwilder/lean-contributions`. This file remains only to preserve the historical route by which the formalization was recovered into the release.
