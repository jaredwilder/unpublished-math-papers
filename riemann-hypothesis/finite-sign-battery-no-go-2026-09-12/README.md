# No fixed finite sign battery can characterize the positive-real spectral cone

**Author:** Jared Wilder  
**Date:** 2026-09-12  
**Status:** proved generic continuity obstruction; not an RH theorem; novelty not asserted

## Statement

Consider a finite collection of strict inequalities selected from two common real-rootedness / RH-motivated hierarchies:

\[
H_{n,q}(\alpha)>0
\]

and

\[
D_{r,k}(\alpha)>0,
\]

where the selected Hausdorff-type quantities and consecutive Toeplitz minors are continuous functions of a finite parameter vector

\[
\alpha=(\alpha_1,\ldots,\alpha_M).
\]

Assume that at the positive-real base point

\[
\alpha_1=\cdots=\alpha_M=1
\]

every selected inequality is strict.

Then there exists a parameter vector with a nonreal conjugate pair for which **every inequality in the same finite battery remains strict**.

Consequently,

\[
\boxed{
\text{no fixed finite collection of these generic strict sign tests}
}
\]

can by itself characterize the cone

\[
\alpha_j>0\quad\text{for all }j.
\]

## Proof

Because only finitely many tests have been selected and each test is continuous in the parameters, strict positivity at the base point has a common open neighborhood on which all selected inequalities remain positive.

Replace two coordinates continuously by

\[
\alpha_1=e^{i\theta},\qquad \alpha_2=e^{-i\theta}
\]

and leave all remaining coordinates equal to `1`.

At `theta=0` this is the original positive-real point. Therefore for sufficiently small nonzero `theta`, the perturbed parameter vector remains inside the common positivity neighborhood of every selected test.

Yet for every nonzero `theta`, the parameter vector contains a genuinely nonreal conjugate pair.

Hence the finite battery cannot distinguish the positive-real spectral cone from all nearby nonreal spectra. QED.

## Operational consequence

This does **not** say that RH cannot have a finite proof or a finite certificate.

It says something narrower:

> A proof cannot consist only of checking a fixed finite prefix of generic Hausdorff/finite-difference and Toeplitz-minor sign hierarchies unless additional structure supplies a theorem controlling the untested tail.

The missing ingredient could be, for example,

- a zeta-specific tail theorem;
- an exact recurrence propagating finitely many signs to all indices;
- a quantitative rigidity theorem unavailable to generic spectra;
- an analytic continuation or monotonicity theorem that collapses the infinite hierarchy.

Without such structure, simply increasing a finite sign battery cannot logically close the spectral problem.

## Provenance

This theorem was extracted in the 2026-09-12 post-ingest re-mining of the RH research estate after exact counterexamples killed naive finite transfer in both directions between the Hausdorff and Toeplitz hierarchies.

The argument is elementary continuity. **No literature-novelty claim is made.** Its value is as a clean route-kill and a guardrail for future finite-computation campaigns.
