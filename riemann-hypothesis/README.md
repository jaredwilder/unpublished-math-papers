# Riemann zeta research program — determinant curvature, simple-zero bounds, and de Bruijn–Newman simplicity

**Author:** Jared Wilder  
**Campaign dates:** 2026-08-11 and 2026-09-11  
**Public extraction:** 2026-09-11

This directory now exposes **three distinct research lanes** around the Riemann zeta function. None is presented as a proof of the Riemann Hypothesis.

The point of this front door is to make the mathematics discoverable without asking a reader to infer status from historical workflow filenames or from whether a larger conjecture remains open.

## 1. Determinant / total-positivity program

Primary historical record:

`RH-TERMINAL-ENCIRCLEMENT-2026-08-11.md`

New adversarial extraction from the 2026-09-11 MSL snapshot:

`determinant-curvature-2026-09-11/`

The program studies the entire function

`G(z) = (1/8) xi(1/2 + sqrt(z)/2)`

through its moment coefficients and consecutive Toeplitz determinants

`D_{r,k} = det[a_{k+j-i}]`.

Surviving mathematical assets include:

- transformed-zero / Toeplitz criteria and exact determinant identities;
- a positive-atom representation for `G` and a positive-measure determinant lift;
- an exact sign obstruction to the most direct pointwise-integrand positivity route at `r=2`;
- a rectangular Schur-function interpretation of `D_{r,k}`;
- an exact tilted-measure / cumulant coordinate for normalized determinants;
- the exact Desnanot–Jacobi curvature identity
  `Z = (r/k) Q/(1-Q)`;
- an exact reciprocal/Jacobi–Trudi duality
  `Z_a(r,k) Z_b(k,r) = 1`;
- reproduced fixed-slope numerical evidence at `theta = 1/2, 2/3, 3/4`, where a positive-limit model strongly out-fits a vanishing-limit model on the available finite tails;
- five successful kernel-checked Lean fragments from the exported campaign.

The 2026-09-11 extraction also corrects two overclaims in the active source state: a gamma-factor envelope was incorrectly promoted to a global pointwise asymptotic, and a numerically observed lowest-zero velocity sign was promoted beyond what its derivation established. The exact reusable identities are retained; the overclaims are not.

The live mathematical target remains ratio-uniform asymptotic control strong enough to connect determinant curvature to the relevant total-positivity / zero-simplicity criterion. The finite fits do not supply that theorem.

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
- an Arb/python-flint verifier adapted for a second trust base, written and syntax-checked but not executed in the source environment.

Accordingly this lane is a **machine-checked candidate extension pending independent reproduction / Arb rerun / expert review**.

## 3. PTS / de Bruijn–Newman interval-certifier program

Directory:

`pts-terminal-close/`

This lane was entirely absent from the earlier public front door and was recovered from the 2026-09-11 session export.

Its frozen target is:

> For every real `x` and every `t in (0,0.2]`, if `H_t(x)=0`, then `H_t'(x) != 0`.

In words: every real zero of the heat-evolved xi flow is simple throughout that positive-time interval.

The internal program labels this statement **PTS** and treats it as a terminal sufficient theorem for its de Bruijn–Newman route. PTS remains **unproved**.

The recovered material includes:

- the frozen terminal-close record and explicit implication chain;
- a ten-mechanism close-anatomy campaign contract;
- a rigorous interval-arithmetic certifier for small-x boxes;
- historical records of three point certificates at `t=0.2` and three uniform t-box certificates over `t in [0.1,0.2]`;
- a direct-quadrature scaling wall and the resulting large-x representation problem.

During this public extraction the recovered certifier's built-in self-test was rerun from the exported source and passed **8/8, exit 0**. The original export did not carry all 23 historical receipt JSONs as named public artifacts, so those finite certificate claims are preserved as source-campaign records rather than falsely described as freshly reproduced here.

## Repository status

These three lanes now form one coherent **Riemann-zeta research program** rather than archive debris:

1. determinant / total positivity and fixed-slope curvature;
2. simple-zero proportion computation;
3. de Bruijn–Newman positive-time simplicity / interval certification.

They have different proof obligations and evidence classes. They belong together at the subject level, but their claims must not be blended.

## Reading rule

Use the exact theorem, computation, candidate, or target statement you are citing. A large RH-related campaign does not upgrade a candidate into a theorem. Conversely, the fact that RH remains open does not erase exact determinant identities, kernel-checked fragments, finite certified inequalities, or a reproducible certifier that survives its stated tests.
