# Kirkman's Steiner triple-system existence theorem — Lean formalization record

**Author:** Jared Wilder  
**Campaign date:** 2026-07-24  
**Public estate release:** 2026-09-11

## The theorem

A Steiner triple system of order `v` exists if and only if

`v ≡ 1 or 3 (mod 6)`.

This is **Kirkman's classical 1847 theorem**, not new mathematics.

## What this estate contributed

The recovered campaign state records a complete Lean 4 / Mathlib proof in both directions, with:

- **0 `sorry`**;
- **0 custom axioms**;
- necessity proved from the abstract Steiner-triple-system structure by double counting;
- sufficiency proved by formalized **Bose** construction for `v ≡ 3 (mod 6)` and **Skolem** construction for `v ≡ 1 (mod 6)`;
- the exactly-one-block property proved universally for the constructed systems.

The necessity route recorded in the estate derives:

1. ordered-pair fiber counting, giving `6 | v(v-1)`;
2. point-fiber counting, forcing `v` odd;
3. hence `v ≡ 1 or 3 (mod 6)`.

The sufficiency route constructs a valid STS in both admissible residue classes via the classical Bose/Skolem constructions.

## Provenance limitation of this release

The atlas identifies the original internal source as the STS/Kirkman Lean campaign and records the terminal status `PROVEN_BOTH_DIRECTIONS`. During this release sweep, the **standalone `.lean` source file was not recovered from the ChatGPT Library or the existing public GitHub estate**.

Therefore this directory publishes the theorem/formalization record now rather than fabricating Lean code from a summary. It does **not** pretend the proof source bytes are included.

The source-recovery obligation is explicit:

> recover the original Lean file(s), preserve their exact bytes / hashes if available, run a current `lake build`, record `#print axioms`, and add them here without rewriting the historical artifact.

## Priority boundary

The campaign noted that Mathlib itself appeared to contain no design-theory development at the time, making this plausibly an early Lean formalization of Kirkman's theorem. Isabelle/AFP already contains design-theory formalization, so **no first-anywhere priority claim is made here**.

This release claims only what the recovered estate state supports: a completed Lean formalization was produced in the campaign; the original source bytes still need provenance recovery for a fully reproducible public package.