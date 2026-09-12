# Riemann zeta research program — audited public record

**Author:** Jared Wilder  
**Campaign dates:** 2026-08-11 through 2026-09-12  
**Last forensic update:** 2026-09-12

This directory is the public subject home for the RH/zeta mathematics recovered from a large research campaign and its subsequent full-estate audits.

## Current headline

**There is no proof of the Riemann Hypothesis in this repository. RH remains open.**

The later forensic process is deliberately separating:

- exact generic mathematics;
- zeta-specific finite certificates;
- computational evidence;
- formal proof plumbing;
- open sufficient criteria;
- failed routes and negative theorems.

A 100-round raw-estate ingest traversed **1,476 / 1,476 unique SHA-256 objects** and independently recovered **4,475 raw MSL theorem/state blocks**. That audit found a real auxiliary-mathematics estate, but no new proved theorem about the zeta function itself that should be advertised as major RH progress.

The audit is still being re-mined. The first adjudication was a compression layer, not an exhaustive mathematical inventory.

---

## New theorem / structure releases from repeated re-mining

### Finite even-moment rigidity

Directory:

`finite-moment-rigidity-2026-09-12/`

For `Q` reflection/conjugation off-line quadruples

\[
\frac12\pm d_j\pm i t_j
\]

versus `2Q` critical-line conjugate pairs, equality of the first `2Q` raw even power sums forces

\[
\{y_1^2,\dots,y_{2Q}^2\}
=
\{(t_j+i d_j)^2,(t_j-i d_j)^2:1\le j\le Q\}.
\]

Newton identities then force every `d_j=0` if the comparison heights are real. This is a finite algebraic rigidity theorem, not an RH theorem. Exact symbolic sanity checks for `Q=1,2,3,4` are included. Literature novelty remains under review.

### Tilted-theta CGF / Toeplitz coordinate

Directory:

`theta-cgf-toeplitz-coordinate-2026-09-12/`

Under the coefficient-tilted theta measure

\[
d\nu_k(u)=\frac{u^{2k}\Phi(u)}{m_{2k}}du,
\qquad X_k=2\log U,
\]

every normalized Toeplitz entry is a factorial/gamma correction times the moment-generating function of the **same** random variable:

\[
\frac{a_{k+s}}{a_k}
=
\frac{\Gamma(2k+1)}{\Gamma(2k+2s+1)}
\mathbb E e^{sX_k}.
\]

Thus the full normalized consecutive determinant is encoded by one cumulant-generating function `K_k(s)`. This identifies the campaign's earlier variance/Turán work as the local-shift face of the same object whose macroscopic shifts govern fixed-slope determinants. This is published as an exact structural synthesis; novelty is not asserted.

### Natural determinant-integral sign obstruction

Directory:

`determinant-integral-sign-no-go-2026-09-12/`

The exact positive-measure multilinear lift of a consecutive Toeplitz determinant does **not** have a pointwise-positive inner kernel. At order two the symmetrized kernel contains

\[
u^2v^2-\frac{c_k}{2}(u^4+v^4),
\]

which is positive on the diagonal and negative for sufficiently large `u/v`. This kills the most direct pointwise-positivity shortcut while leaving cancellation-based integral methods open.

---

## 1. Determinant / total-positivity mathematics

Primary historical record:

`RH-TERMINAL-ENCIRCLEMENT-2026-08-11.md`

Recovered Encirclement II–V theorem spine:

`encirclement-ii-v-recovered/`

2026-09-11 determinant-curvature extraction:

`determinant-curvature-2026-09-11/`

Exact theta-kernel certificates recovered from epochs 20–22:

`theta-kernel-certificates/`

Additional quartic/Gamma bridge:

`gamma-theta-quartic-bridge/`

Surviving exact structural results include:

- the Desnanot–Jacobi normalized determinant identities;
- the rational odds-orbit family and factorial benchmark;
- a normalized nonlinear comparison equation for two positive determinant arrays;
- a finite-domain comparison/maximum principle and boundary-homotopy consequence under their stated positivity hypotheses;
- adaptive harmonic/superharmonic identities obtained by differentiating the normalized determinant equation along a coefficient flow;
- dual Jacobi–Trudi order/shift symmetry;
- rectangular-Schur occupancy and angular phase bounds;
- the top-`k` sufficient angular budget
  \[
  r\sum_{j=1}^k\theta_j<\frac\pi2\Longrightarrow D_{r,k}>0
  \]
  under its stated conjugation/reality hypotheses.

The recovered Encirclement II–V algebra verifiers freshly reproduced **24/24** stated checks. These verifiers establish their own algebraic claims, not RH.

---

## 2. Branch C — valid sufficient criterion, analytic proof incomplete

Directory:

`branch-c-five-link-reduction/`

The global weighted determinant criterion is

\[
(k+r)D_{r,k-1}D_{r,k+1}\le kD_{r,k}^2.
\]

For an everywhere-positive infinite coefficient sequence, a global proof of this inequality would inductively force all consecutive minors positive; the classical strict-consecutive-minor theorem then feeds the `PF_\infty` / Laguerre–Pólya route.

The historical finite-polynomial falsifier did **not** satisfy the complete infinite/everywhere-positive hypothesis, so it does not kill this global sufficient route.

But the criterion has **not** been proved for the actual xi coefficient sequence. The surviving analytic gaps include determinant-lattice transport, tilted-measure variance/large-deviation control, and the fixed-slope region not covered by existing tail results.

Current status:

> **valid sufficient criterion; open analytic target; not an RH result.**

---

## 3. Important literature correction — the order-one moment row is classical

Repeated re-mining found that the campaign's binding order-one theta-moment inequality

\[
\frac{m_{2k-2}m_{2k+2}}{m_{2k}^2}
\le
\frac{2k+1}{2k-1}
\]

is not a new campaign theorem. It is the classical Turán moment inequality proved for the Riemann `Xi` kernel by **George Csordas and Richard S. Varga, _Moment Inequalities and the Riemann Hypothesis_, Constructive Approximation 4 (1988), 175–198**, in a stronger deformed-family setting.

Consequences:

- the campaign's finite first-row certificates remain reproducibility artifacts;
- they are **not** a novelty headline;
- earlier language calling this row “sub-Gaussianity” was too strong: it is a Turán/fourth-moment statement, not an MGF or tail-domination theorem.

---

## 4. Branch A — de Bruijn–Newman heat-flow instruments

Directory:

`branch-a-heat-flow-audit/`

The campaign built several useful finite heat-flow instruments and falsified multiple candidate sufficient statistics.

### Forensic correction to the truncation claim

An earlier version of this README said that a 64-piece truncation envelope **rigorously validated a finite zero window**. That statement was too strong and is retracted.

The source code computes the per-cell quantity called a maximum by evaluating the kernel on a **finite grid of 41 sample points** with ordinary `mpmath` arithmetic. It does not supply interval enclosures of the true cell suprema. The subsequent derivative and zero-shift calculations are likewise floating-point computations.

Therefore that packet is useful **numerical evidence / instrumentation**, but it is **not a rigorous zero-localization certificate** in its present form.

A rigorous replacement would need, at minimum, certified interval bounds for each cell supremum (or an analytic monotonicity bound), directed-rounding control of the moments/tail, and a certified lower bound for the derivative on the localization interval.

The pair-energy statistic was also falsified as a sufficient statistic, and the natural polynomial-truncation/Hermite route became uninformative because the truncations introduced spurious complex roots.

---

## 5. Branch B — arithmetic Chebyshev-error lane

Directory:

`branch-b-chebyshev-handoff/`

The export contains finite prime-power probes only. They do not establish an asymptotic theorem and are not RH evidence beyond their finite ranges.

---

## 6. Formal layer

Directory:

`formal-epoch22-23/`

The full estate contains **181 unique Lean source files** after alias-aware deduplication. Source audit found no `sorry`, `sorryAx`, `nativeDecide`, or `ofReduceBool` in the audited set, but it also found **zero files directly formalizing analytic `RiemannZeta`**.

The formal estate is therefore useful algebraic/logical infrastructure, not a formal proof of RH.

---

## 7. Simple-zero proportion candidate

Directory:

`simple-zero-67.301545-candidate/`

This remains a historical/certificate-method asset. Its heavy certifiers did not freshly complete under the bounded hostile replay used in the 100-round audit, and its numerical headline has been overtaken by later 2026 claims. It is not the current front-page result.

---

## 8. PTS / de Bruijn–Newman interval-certifier program

Directory:

`pts-terminal-close/`

Frozen target:

> For every real `x` and every `t in (0,0.2]`, if `H_t(x)=0`, then `H_t'(x) != 0`.

The finite/local certification machinery contains real algebra and useful interval ideas. The global all-`x`, all-`t` PTS statement remains **unproved**.

---

## 9. Public-reading rule

Use every item at its actual scope.

A public theorem note may be:

- a generic exact theorem motivated by RH;
- a zeta-specific finite certificate;
- a negative theorem killing a route;
- a structural reformulation;
- an open sufficient criterion.

Those are not interchangeable.

The release doctrine after the 100-round audit is:

1. source-replay the claim;
2. attack its hypotheses and boundary cases;
3. perform a targeted prior-art check;
4. publish surviving mathematics promptly with exact scope and provenance;
5. keep re-mining the estate, because no single adjudication sweep is treated as exhaustive.

The goal of this directory is now a **correct, timestamped mathematical record**, not a dramatic RH headline.
