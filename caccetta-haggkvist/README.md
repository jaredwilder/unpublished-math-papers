# Caccetta–Häggkvist directed-triangle research program

**Author:** Jared Wilder  
**Research dates:** 2026-08-06/07  
**Public extraction:** 2026-09-11

This is a research-program-scale body of mathematics on the directed-triangle case of the Caccetta–Häggkvist conjecture: a 23KB theorem ledger, a later terminal-defect package, finite exhaustive checks, and a newly recovered exact-boundary defect layer from the archive seam.

It warrants a dedicated repository. Until a writable shell exists, this directory is the public source of record.

## What is here

- [`CH3-THEOREM-LEDGER-2026-08-06.md`](CH3-THEOREM-LEDGER-2026-08-06.md) — a **23KB theorem ledger** from the first fifteen rounds, preserving supported statements, conditional reductions, proposals, structural diagnoses and retractions;
- [`CH3-ROUNDS18-19-TERMINAL-DEFECT-PACKAGE.md`](CH3-ROUNDS18-19-TERMINAL-DEFECT-PACKAGE.md) — the later **8.5KB terminal-defect package**, sharpening smallest-counterexample geometry, correcting an earlier opposite-fan mistake, and deriving the critical-cycle defect telescope;
- [`RECOVERED-R3-DEFECT-BUDGET-2026-09-11.md`](RECOVERED-R3-DEFECT-BUDGET-2026-09-11.md) — the release-day archive recovery of the two-regime boundary reduction, fourth-moment inequality, critical-edge overlap bound, exact local defect identity, and 21-state relation-table certificate.

## Exact-boundary kernel studied

A central branch studies triangle-free oriented graphs arising from smallest-counterexample / arc-minimal reductions. The recovered archive layer sharpens the size boundary to

\[
n\in\{3d-1,3d\},\qquad d=\lceil n/3\rceil,
\]

with uniform outdegree `d`. Thus the defect from the `3d` boundary has only two possible values.

Major structural layers include:

- neighborhood acyclicity and escape mass;
- hereditary deficit and exact escape inequalities;
- three- and four-chamber decompositions;
- common-in/common-out fan energy;
- bridge multiplicity and one-way/forbidden rectangles;
- two-path matrix identities;
- fourth-moment / directed-`C4` structure;
- critical-edge cycles and exact defect telescoping.

## Fourth-moment and local-defect structure

The source ledger's strongest named quantitative asset is the **Cubic Directed-C4 Theorem**, stated there as

`C_4(D) >= ceil(3 d^3 / 2)`

and equivalently

`tr(A^4) >= 6 d^3`

for the exact-boundary kernel. The source itself marks this statement as requiring independent machine verification and historical novelty review, so this README does not silently upgrade its authority.

A surviving exact fourth-moment identity is

`tr(A^4) = ||A^2||_F^2 - (1/2)||A^2-(A^T)^2||_F^2`.

The archive-seam package additionally records the structural lower bound

`tr(A^4) >= n d^2 (3d+2-n)`

and, on critical edges `(a,b)`,

`O(a,b) <= ceil(d/3)-1`.

It replaces an abandoned edge-local potential route by the exact identity

`F(a,b)=O(a,b)+d^-(b)-1-Q_ab`,

with the key local inequality classified by a **21-state relation table**: twenty admissible states have score at most 1, and the unique score-2 state is the Twisted-Circle witness.

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

The Round-18 checker exhausts all oriented graphs on 3, 4 and 5 vertices—27, 729 and 59,049 respectively—for the stated finite checks.

## Evidence boundary

The ledger deliberately mixes theorem statuses. `SUPPORTED`, conditional, proposal, structural diagnosis, and retracted/overclaim entries remain distinct.

The archive-recovered 21-state relation table and defect package are now visible here, but their original checker/source bytes still need to be routed into this directory and rerun. That is an evidence-recovery obligation, not a reason to leave the mathematics buried in the archive seam.

The parent Caccetta–Häggkvist directed-triangle problem is not presented here as solved. The program's independent structural statements stand or fall at their own proof/evidence level.

## Repository promotion

This program is on the release's highest-priority standalone-repository queue. Its current public surface is already coherent enough to migrate directly when a dedicated writable shell appears.
