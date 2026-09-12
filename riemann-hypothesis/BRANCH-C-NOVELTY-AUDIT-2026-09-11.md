# Branch C novelty audit — superseded by refutation

**Author:** Jared Wilder  
**Initial audit:** 2026-09-11  
**Superseded:** 2026-09-12

## Current verdict

The earlier novelty question — whether a five-link sufficient RH architecture had reduced one analytic link to finite certification — is no longer the right question.

The 2026-09-12 campaign falsified the top implication of that route.

The determinant criterion

\[
rD_{r,k-1}D_{r,k+1}\le kD_{r+1,k}D_{r-1,k}
\]

is **not sufficient for real-rootedness**.

Fresh exact-rational reruns from the exported source reproduce:

- 1,686 criterion-satisfying objects among 3,059 explicitly non-real-rooted test polynomials;
- after demanding full available depth, interior shifts and both the square-free and original forms, 1,445 of 2,284 still pass, identically in both forms.

Therefore Branch C is not an RH route.

## The publishable object has changed

The correct mathematical object is now a **negative theorem / structural obstruction**:

> This determinant-lattice inequality, even imposed throughout the full available lattice of a finite polynomial and in its original entry form, does not characterize real-rootedness.

An explicit degree-five witness is recorded in `branch-c-five-link-reduction/README.md`, and the exact falsifier/audit scripts are published beside it.

## What remains mathematically valid

The refutation does not erase the lower exact mathematics developed by the campaign:

- Desnanot–Jacobi identities;
- determinant normalizations and curvature coordinates;
- exact first-rung reductions;
- certified theta-kernel inequalities;
- formal algebraic implications;
- multiplicity-blindness of consecutive Toeplitz positivity;
- the Encirclement II–V determinant geometry.

Those results should be cited individually at their true scope.

## Historical note

The 2026-09-11 novelty audit compared the then-live five-link architecture against Turán/Laguerre/Jensen/kernel-concavity literature. That comparison is retained in repository history, but its proposed RH-route novelty target is superseded by the 2026-09-12 falsifier.

The campaign's own strongest methodological result is now simple:

> **Test sufficiency against an explicit false-target family before investing in proving a criterion on the target object.**

Branch C was killed by exactly that test.