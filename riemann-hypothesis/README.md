# Riemann zeta research program — determinant geometry, live branch audit, simple-zero bounds, and de Bruijn–Newman simplicity

**Author:** Jared Wilder  
**Campaign dates:** 2026-08-11 through 2026-09-12

This directory is the public subject home for the RH/zeta mathematics recovered from the release estate.

> **2026-09-12 forensic correction:** the earlier same-day statement that Branch C was dead has been superseded. The epoch-23 finite-polynomial falsifier does not satisfy the infinite positive-coefficient / strict-minor hypothesis needed by the global criterion. Branch C is therefore reopened as a valid sufficient-criterion route. **RH remains open** because the campaign did not prove that criterion globally for the xi coefficients; the remaining gaps are analytic and are now stated explicitly below.

See:

- `CURRENT-CAMPAIGN-STATE-2026-09-12.md`
- `branch-c-five-link-reduction/BRANCH-C-READJUDICATION-2026-09-12.md`

## Current live campaign state

The 2026-09-12 export reaches absolute MSL round 647. After full-dump readjudication:

- **Branch C:** valid sufficient criterion, but global analytic proof incomplete;
- **Branch A:** finite heat-flow instrumentation survives, but its pair-energy and natural polynomial-truncation/Hermite certificate candidates failed;
- **Branch B:** screened and arithmetically clean, but otherwise largely untouched;
- **RH:** open.

## 1. Determinant / total-positivity mathematics

Primary historical record:

`RH-TERMINAL-ENCIRCLEMENT-2026-08-11.md`

Recovered Encirclement II–V theorem spine:

`encirclement-ii-v-recovered/`

2026-09-11 determinant-curvature extraction:

`determinant-curvature-2026-09-11/`

Exact theta-kernel certificates recovered from epochs 20–22:

`theta-kernel-certificates/`

Additional exact quartic/Gamma bridge:

`gamma-theta-quartic-bridge/`

### Exact determinant geometry now public

- Desnanot–Jacobi gives `R+A=1` for the two normalized neighboring-minor ratios.
- The nonlinear odds lattice admits the exact rational family `Y_(r,k)=(r+mu)/(k+nu)`; the Toeplitz boundary selects `Y*=r/k`.
- For the factorial comparison determinant,
  `D0_(r,k)=prod_{j=0}^{r-1} j!/(k+j)!`.
- Writing `U=log(D/B)` against a positive comparison determinant array gives the exact nonlinear comparison equation
  `R_B exp(Delta_k^2 U) + A_B exp(Delta_r^2 U) = 1`.
- On finite lattice domains this equation has a strong maximum/comparison principle and a boundary-homotopy positivity theorem under the stated positivity hypotheses.
- Along the de Bruijn–Newman coefficient flow, `V=partial_t U` satisfies a weighted discrete harmonic equation while `partial_t^2 U` has the recorded quadratic-source structure.
- Dual Jacobi–Trudi gives an exact order/shift swap through the reciprocal series.
- In the real-zero phase, consecutive minors are rectangular Schur polynomials; their normalized zero-parameter sensitivities satisfy the recorded occupancy bounds.
- Sorted angular defects satisfy the top-k sufficient phase criterion
  `r * sum_{j=1}^k theta_j < pi/2  =>  D_(r,k) > 0`
  under the conjugation/reality assumptions of the application.
- Under the stated verified reciprocal-pole hypotheses, fixed-shift dual determinants are eventually strictly positive; combined with the primal large-shift frontier, a hypothetical escaping failure must enter a two-scale regime.

Fresh public reruns of the recovered Encirclement II–V source verifiers gave

**7/7 + 5/5 + 6/6 + 6/6 = 24/24 successful algebraic checks.**

These verifiers establish their stated algebra/finite identities, not RH.

### Strict versus nonnegative consecutive minors

The sequence

`a=(1,0,0,0,0,1)`

has nonnegative consecutive minors in the tested hierarchy but a negative non-consecutive Toeplitz minor. It therefore refutes the **nonnegative** shortcut

> consecutive nonnegativity => total positivity.

It does **not** refute the classical **strict** consecutive-minor criterion.

For an everywhere-positive infinite coefficient sequence satisfying the Branch C inequality globally, Desnanot–Jacobi inductively forces every consecutive minor to be strictly positive. Schoenberg's strict-consecutive-minor theorem, quoted explicitly as Theorem D and in Toeplitz-sequence form as Lemma 3 in Katkova's 2005 paper, then promotes those minors to total positivity / `PF_m` at every finite order.

Source: https://arxiv.org/html/math/0505174v1

## 2. Branch C — readjudicated: valid criterion, incomplete analytic proof

Directory:

`branch-c-five-link-reduction/`

The global criterion is

\[
(k+r)D_{r,k-1}D_{r,k+1}\le kD_{r,k}^2
\qquad(r,k\ge1),
\]

or equivalently

\[
rD_{r,k-1}D_{r,k+1}\le kD_{r+1,k}D_{r-1,k}.
\]

For `a_k>0` at every index, it implies

\[
D_{r+1,k}D_{r-1,k}\ge \frac{r}{k+r}D_{r,k}^2>0,
\]

so every consecutive minor is strictly positive by induction. Combined with the classical strict-consecutive-minor theorem and the ASWE/Laguerre–Pólya characterization, this is a genuine sufficient route to RH.

### Why the epoch-23 retraction was wrong

The historical falsifier constructed finite non-real-rooted polynomials and explicitly discarded the terminating boundary. A fresh exact rerun reproduces its `1445/2284` interior hits and shows **1445/1445** have finite support and therefore violate the everywhere-positive coefficient premise.

The historical falsifier is preserved as a negative-control lesson; it is no longer the current Branch C verdict.

### Why Branch C still does not prove RH

The epoch-22 “lower half complete” label also overreached. The archive itself preserves unresolved steps:

- the determinant-lattice order/local-ascent law was measured, not proved;
- the order-arm identification with the tilted-log variance had exact error terms left open;
- the theta-vs-Gaussian variance comparison was measured, not proved;
- the tilted density is log-convex in a far-left region, invalidating a naive global Brascamp–Lieb argument;
- the proposed restricted-tail repair did not rigorously close its crossing/mass/error terms;
- curvature at the moving mode does not by itself control global variance, yet the later chain promoted such a mode-curvature estimate to the whole criterion.

Therefore the current Branch C status is:

> **valid sufficient criterion; exact theta-kernel and determinant mathematics survives; global proof of the criterion for every `(r,k)` remains open.**

## 3. Branch A — de Bruijn–Newman heat-flow instruments

Directory:

`branch-a-heat-flow-audit/`

The campaign built a flat-cost moment-series evaluator, derived a cancellation precision rule, and rigorously validated a finite zero window with a 64-piece truncation envelope.

Its first candidate quantity, pair energy

`E(t)=sum_{i<j} 1/(z_i-z_j)^2`,

was falsified as a sufficient statistic: an exact complex-root control has energy zero while real controls can have substantially larger energy.

A Hermite/minor separator calibrates correctly on exact finite controls but becomes uninformative on the natural polynomial truncations of the entire function because those truncations themselves carry many spurious complex roots.

The directory records the finite data and control source.

## 4. Branch B — arithmetic Chebyshev-error lane

Directory:

`branch-b-chebyshev-handoff/`

The current export contains only a finite prime-power probe through `x=200000`; those values are not evidence for RH beyond their stated finite range.

Branch B remains a clean alternative lane, not a solved result.

## 5. Formal epoch-22/23 layer

Directory:

`formal-epoch22-23/`

This is the recovered Lean layer from the final two epochs. It contains algebraic and logical campaign lemmas and negative-control logic.

The formal files do **not** prove RH facts by themselves. In particular, a formally correct generic statement that a genuine counterexample refutes an implication does not establish that the epoch-23 finite polynomial satisfied the global hypotheses of the implication; the readjudication found that it did not.

## 6. Simple-zero proportion candidate

Directory:

`simple-zero-67.301545-candidate/`

The recovered verifier records the local inequality for

`q = 29/100000`, `L = 341/100000`

on two subdivision grids. The exact propagation algebra gives the candidate lower bound

`0.673015452606376894...`

for the simple-zero proportion within the stated seven-point stability framework.

This is a standalone analytic-number-theory candidate, not an RH claim. Its historical novelty/priority must be judged against the fast-moving 2026 simple-zero literature by exact date and proof status.

## 7. PTS / de Bruijn–Newman interval-certifier program

Directory:

`pts-terminal-close/`

Frozen target:

> For every real `x` and every `t in (0,0.2]`, if `H_t(x)=0`, then `H_t'(x) != 0`.

Recovered material includes the target chain and interval-certifier source. During the forensic pass the certifier self-test again passed **8/8**. The original full receipt bundle is not present in this export, and a fresh full certification run exceeded the current execution window, so the historical point/t-box certificates remain distinguished from fresh reproduction.

PTS remains unproved.

## 8. Full-dump reading rule

Use each result at its actual mathematical scope. Exact determinant identities, comparison theorems, Schur bounds, formal fragments, finite certifications, negative theorems, computational asymptotics and open analytic lemmas are different evidence classes.

Two corrections from this audit are especially important:

1. **A false-target test only refutes a theorem when the test object satisfies the theorem's complete hypotheses.**
2. **A certificate cannot inherit stronger status than unresolved empirical or analytic steps in its dependency chain.**

The continuing forensic audit is extracting every surviving theorem, obstruction and reproducibility artifact from the 1,284-file export rather than treating the session summary as the mathematics.
