# Riemann zeta research program — determinant curvature, simple-zero bounds, and de Bruijn–Newman simplicity

**Author:** Jared Wilder  
**Campaign dates:** 2026-08-11 and 2026-09-11  
**Public extraction:** 2026-09-11

This directory exposes **three distinct research lanes** around the Riemann zeta function. None is presented as a proof of the Riemann Hypothesis.

The point of this front door is to make the mathematics discoverable without asking a reader to infer status from historical workflow filenames or from whether a larger conjecture remains open.

## 1. Determinant / total-positivity program

Primary historical record:

`RH-TERMINAL-ENCIRCLEMENT-2026-08-11.md`

Adversarial extraction from the 2026-09-11 MSL snapshot:

`determinant-curvature-2026-09-11/`

Additional exact bridge recovered from live result W131:

`gamma-theta-quartic-bridge/`

The program studies

`G(z) = (1/8) xi(1/2 + sqrt(z)/2)`

through its moment coefficients and consecutive Toeplitz determinants

`D_{r,k} = det[a_{k+j-i}]`.

### Exact results now surfaced

- **Desnanot–Jacobi curvature identity**
  `Z = (r/k) Q/(1-Q)`.
- **Reciprocal/Jacobi–Trudi duality**
  `Z_a(r,k) Z_b(k,r) = 1`, exchanging compactified ratio `theta` with `1-theta`.
- **Gamma–theta quartic coordinate bridge.** The substitution `y=pi x^4` maps the normalized quartic theta density `exp(-pi x^4)` exactly to a `Gamma(1/4,1)` law. The campaign's numerical proportionality constant `1.3313353638...` is exactly `pi^(1/4)`. Its squared-variable dispersion is the closed form
  `Gamma(1/4)^2/[4 Gamma(3/4)^2]-1 = 1.188439615226... < 2`.
  The same calculation gives dispersion `5` for an exponential density and exactly `2` for the Gaussian case, proving that ordinary log concavity alone is not the relevant sufficient property. See `gamma-theta-quartic-bridge/`.
- **Strict consecutive Toeplitz positivity does not imply simple zeros.** The explicit entire function
  `(1+z)^2 e^z`
  has a double zero at `-1`, yet every consecutive Toeplitz minor is strictly positive. The global proof is in
  `determinant-curvature-2026-09-11/MULTIPLICITY-BLINDNESS-THEOREM.md`.
- **Rigorous order-one curvature anchor.** Combining the exact curvature identity with Michalowski's published coefficient-curvature window gives, for every `k>=2`,
  `1/[k(exp(4/k)-1)] < Z_{1,k} < 1/[k(exp(1/(2k))-1)]`,
  so asymptotically the order-one corridor lies between `1/4` and `2`. See
  `determinant-curvature-2026-09-11/ORDER-ONE-CURVATURE-COROLLARY.md`.
- Five successful kernel-checked Lean fragments from the exported campaign, including an empty-axiom abstract falsifier for a universal “determinant positivity implies simplicity” implication.

### Computational frontier

The extracted fixed-slope computation was independently rerun against its carried coefficient cache. At `theta=1/2, 2/3, 3/4`, a positive-limit model strongly out-fits a vanishing-limit model on the available finite tails, with residual ratios about `169`, `159`, and `137` respectively.

That is finite numerical evidence, not an asymptotic theorem. The live target is still ratio-uniform control as `r,k` grow together.

### Audit corrections

The source state was not accepted as an authority ledger without review. In particular:

- a gamma-factor envelope had been promoted to a global pointwise asymptotic without controlling the zeta factor;
- a tested lowest-zero velocity sign had been promoted beyond what its derivation established;
- an exact curvature equivalence had been marked stale only because of a non-load-bearing dependency on a retracted fit;
- a finite tested repeated-zero example had been promoted to a universal theorem without proof — the missing all-minors proof has now been supplied separately.

The corrected release keeps the exact reusable mathematics and drops the overclaims.

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
- the recovered interval-arithmetic certifier, preserved with source hashes and deterministic reconstruction instructions;
- historical records of three point certificates at `t=0.2` and three uniform t-box certificates over `t in [0.1,0.2]`;
- a direct-quadrature scaling wall and the resulting large-x representation problem.

During this public extraction the certifier's built-in self-test was rerun from the exported source and passed **8/8, exit 0**. The export did not carry all 23 historical receipt JSONs as named public artifacts, so those finite certificate claims are preserved as source-campaign records rather than falsely described as freshly reproduced here.

## Repository status

These three lanes form one coherent **Riemann-zeta research program** rather than archive debris:

1. determinant / total positivity and fixed-slope curvature;
2. simple-zero proportion computation;
3. de Bruijn–Newman positive-time simplicity / interval certification.

They have different proof obligations and evidence classes. They belong together at the subject level, but their claims must not be blended.

## Reading rule

Use the exact theorem, computation, candidate, or target statement you are citing. A large RH-related campaign does not upgrade a candidate into a theorem. Conversely, the fact that RH remains open does not erase exact determinant identities, proven structural separations, kernel-checked fragments, finite certified inequalities, or a reproducible certifier that survives its stated tests.
