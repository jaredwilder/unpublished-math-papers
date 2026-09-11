# Riemann zeta research program — determinant criteria and simple-zero bounds

**Author:** Jared Wilder  
**Campaign date:** 2026-08-11  
**Public extraction:** 2026-09-11

This directory contains **two distinct research lanes** around the Riemann zeta function. Neither is presented here as a proof of the Riemann Hypothesis.

The point of this README is to make the mathematics discoverable without asking a reader to infer status from historical workflow filenames.

## 1. Determinant / total-positivity program

Primary record:

`RH-TERMINAL-ENCIRCLEMENT-2026-08-11.md`

The program studies the entire function

`G(z) = (1/8) xi(1/2 + sqrt(z)/2)`

through its positive moment coefficients and the consecutive Toeplitz determinants

`D_{r,k} = det[a_{k+j-i}]`.

The surviving mathematical assets include:

- several equivalent or sufficient RH criteria recorded in transformed-zero / Toeplitz language;
- the genus-zero transform `xi(s)=F(s(1-s))`;
- exact heat-flow and critical-value identities from the campaign;
- a positive-atom representation for `G`;
- an exact positive-measure determinant lift;
- an exact sign obstruction showing the most direct pointwise-integrand positivity route already fails at `r=2`;
- a rectangular Schur-function interpretation of `D_{r,k}`;
- an exact tilted-measure / cumulant-generating-function coordinate for normalized determinants;
- a scale diagnosis distinguishing the local cubic-wedge regime from the macroscopic-tilt regime `k=alpha r`.

The terminal mathematical target is a **ratio-uniform collective-saddle positivity theorem**: a normalization of `D_{r,k}` whose asymptotic main term stays positive uniformly in the compactified ratio `k/(k+r)`, followed by a finite-order/all-shift completion step.

The released packet does not supply those final two ingredients. The determinant program is therefore a substantial research frontier, not an RH proof.

## 2. Simple-zero proportion candidate

Directory:

`simple-zero-67.301545-candidate/`

This is a computer-assisted extension of a seven-point Gram-stability argument for simple zeros.

The recovered verifier establishes the finite local inequality for

`q = 29/100000`, `L = 341/100000`

on two independent subdivision grids. The exact propagation algebra then gives the candidate lower bound

`0.673015452606376894...`

for the simple-zero proportion in the precise framework of the underlying stability argument.

The packet includes:

- the generalized seven-point block lemma;
- the exact transfer formula
  `kappa(q,L,m) = [m H_MT - 6q(m-1)] / [m - L(m-6)]`;
- two successful outward-rounded interval-verifier runs;
- an Arb/python-flint verifier adapted for a second trust base, which was written and syntax-checked but **not executed** in the source environment.

Accordingly this lane is best described as a **machine-checked candidate extension pending independent reproduction / Arb rerun / expert review**.

## Repository status

This directory is large enough to be treated as a coherent **Riemann-zeta research program** rather than miscellaneous archive debris. At present it remains in the public intake archive because the strongest simple-zero result is still awaiting independent reproduction and the determinant program has an explicit open terminal target.

If promoted to a dedicated repository, the correct structure is one zeta/RH research home with these two clearly separated lanes—not separate repos for every historical campaign artifact and not an “RH solved” headline.

## Reading rule

Use the exact theorem or candidate statement you are citing. The existence of a large RH-related campaign does not upgrade a candidate into a theorem, and the fact that RH remains open does not erase the exact determinant identities, structural falsifiers, or finite verified inequality already obtained here.
