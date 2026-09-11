# Caccetta–Häggkvist directed-triangle research program

**Author:** Jared Wilder  
**Research dates:** 2026-08-06/07  
**Public extraction:** 2026-09-11

This directory contains a substantial research program on the directed-triangle case of the Caccetta–Häggkvist conjecture. It is awaiting promotion to a dedicated repository; this README exists so the mathematics is discoverable in the meantime.

## What is here

The program currently has two large public records:

- [`CH3-THEOREM-LEDGER-2026-08-06.md`](CH3-THEOREM-LEDGER-2026-08-06.md) — a **23KB theorem ledger** from the first fifteen rounds, preserving supported statements, conditional reductions, proposals, structural diagnoses and retractions;
- [`CH3-ROUNDS18-19-TERMINAL-DEFECT-PACKAGE.md`](CH3-ROUNDS18-19-TERMINAL-DEFECT-PACKAGE.md) — the later **8.5KB terminal-defect package**, which sharpens the smallest-counterexample geometry, corrects an earlier opposite-fan mistake, and derives the critical-cycle defect telescope.

This is therefore a research-program-scale object, not an isolated note.

## Exact-boundary kernel studied

A central branch studies a triangle-free oriented graph on `n=3d` vertices with every outdegree `d`, arising from smallest-counterexample / arc-minimal reductions.

Major structural layers include:

- neighborhood acyclicity and escape mass;
- hereditary deficit and exact escape inequalities;
- three- and four-chamber decompositions;
- common-in/common-out fan energy;
- bridge multiplicity and one-way/forbidden rectangles;
- two-path matrix identities;
- fourth-moment / directed-`C4` structure;
- critical-edge cycles and exact defect telescoping.

## Principal surviving quantitative candidate

The source ledger's strongest named quantitative asset is the **Cubic Directed-C4 Theorem**, stated there as

`C_4(D) >= ceil(3 d^3 / 2)`

and equivalently

`tr(A^4) >= 6 d^3`

for the exact-boundary kernel. The source itself marks this statement as requiring independent machine verification and historical novelty review, so this README does not silently upgrade its authority.

A surviving exact fourth-moment identity is

`tr(A^4) = ||A^2||_F^2 - (1/2)||A^2-(A^T)^2||_F^2`.

The remaining closure pressure is expressed as control of the skew two-path energy / terminal defect strongly enough to eliminate the exact-boundary kernel.

## Later corrections and defect telescope

Rounds 18–19 add several exact results and one important repair:

- the minimal deletion-cover theorem and universal critical escape/indegree barrier;
- in the `n=3d-1` branch, every pair has a common inneighbour;
- in the `n=3d` branch, the uncovered-pair graph is triangle-free;
- **opposite-fan anticompleteness:** for a nonedge `x,y`, the two opposite bridge sets are anticomplete in both directions, correcting an earlier branch that incorrectly allowed one orientation;
- the directed-`C4` diagonal graph is triangle-free, with its edge count exactly equal to the directed-`C4` count;
- a pointwise edge-local potential architecture is ruled out by an explicit local obstruction;
- critical-cycle fragmentation and an exact edge-potential identity;
- independent and transitive critical-path defect inequalities;
- the full critical-cycle defect telescope.

The Round-18 checker exhausts all oriented graphs on 3, 4 and 5 vertices—27, 729 and 59,049 respectively—for the stated finite checks. This is finite supporting evidence, not a replacement for the general proofs.

## Status discipline

The ledger deliberately mixes theorem statuses. A theorem-shaped title is not enough: `SUPPORTED`, conditional, proposal, structural diagnosis, and retracted/overclaim entries must remain distinct.

The parent Caccetta–Häggkvist directed-triangle problem is not presented here as solved. That does not reduce the independent structural results to “failed work”; each surviving statement should be read and cited at its own proved/evidence level.

## Repository promotion

This program is on the release's highest-priority standalone-repository queue. Until a writable dedicated repository is initialized, this archive directory is the public source of record.
