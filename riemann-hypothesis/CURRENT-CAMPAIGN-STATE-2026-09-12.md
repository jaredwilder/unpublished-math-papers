# RH campaign state — 2026-09-12 forensic readjudication

**Author:** Jared Wilder  
**Source snapshot:** active session export through absolute MSL round 647  
**Readjudication:** full-dump forensic pass, 2026-09-12  
**Evidence-level correction:** 2026-09-12

This note supersedes the earlier same-day status that called Branch C dead.

## Headline

**RH remains open. Branch C is a live sufficient-criterion route, but its global analytic proof is incomplete.**

- **Branch C:** reopened after the epoch-23 falsifier was found to test finite terminating polynomials outside the infinite positive-coefficient / strict-minor hypothesis. The classical top implication is valid. The remaining gap is below it: the campaign did not prove the full determinant inequality for every order and shift.
- **Branch A:** its pair-energy and natural polynomial-truncation/Hermite candidates were falsified or rendered uninformative; its heat-flow computations remain useful exploratory numerics, but a later source audit found that the historical 64-piece envelope was **not** a rigorous interval certificate.
- **Branch B:** screened and arithmetically clean, but only probed finitely through `x=200000` in this export.

## Branch C — corrected adjudication

The determinant criterion is

\[
(k+r)D_{r,k-1}D_{r,k+1}\le kD_{r,k}^2,
\qquad r,k\ge1.
\]

Equivalently by Desnanot–Jacobi,

\[
rD_{r,k-1}D_{r,k+1}
\le kD_{r+1,k}D_{r-1,k}.
\]

For an infinite coefficient sequence with `a_k>0` for every `k`, the original form gives

\[
D_{r+1,k}D_{r-1,k}
\ge \frac{r}{k+r}D_{r,k}^2>0.
\]

Starting from `D_{0,k}=1` and `D_{1,k}=a_k>0`, induction gives strict positivity of every consecutive Toeplitz minor. The `k=0` minors equal `a_0^r`.

Katkova's 2005 paper *Multiple positivity and the Riemann zeta-function* explicitly quotes the classical strict-consecutive-minor criterion (Theorem D) and a Toeplitz-sequence form (Lemma 3) that promote these minors to `PF_m`; applying this for every finite `m` gives `PF_infinity`. For the transformed xi generating function, the classical ASWE/Laguerre–Pólya equivalence identifies that with RH.

Source: https://arxiv.org/html/math/0505174v1

### Why the epoch-23 falsifier does not apply

The historical falsifier constructed finite non-real-rooted polynomials and skipped the terminating boundary with

```python
if k+r+1>=N: continue
```

A finite polynomial has `a_N=0`, hence `D_{1,N}=0`; it cannot satisfy the everywhere-positive infinite-support premise used above.

A fresh exact seeded re-audit reproduces the historical count:

```text
2284 tested
1445 interior hits
1445/1445 violate the everywhere-positive coefficient premise
```

Therefore the old `1445/2284` screen is not a counterexample to the global theorem.

See `branch-c-five-link-reduction/BRANCH-C-READJUDICATION-2026-09-12.md`.

## Why this still does not prove RH

The epoch-22 “lower half complete” label also fails forensic review.

The archive itself records the missing steps:

1. **Order/local-ascent proof missing.** `K347` is `COMPUTATION_SUPPORTED` and explicitly leaves the order-step proof open.
2. **Exact order-arm reduction missing.** `K384` identifies the order-arm residue with the tilted-log variance only numerically/asymptotically and leaves exact error terms open.
3. **Variance inequality unproved.** `K385` measures the theta tilted-log variance below the Gaussian/trigamma target and explicitly records the variance comparison as open.
4. **Global curvature hypothesis false.** `K308` finds a far-left region where the tilted density is log-convex, so a global Brascamp–Lieb application is unavailable.
5. **Localization repair incomplete.** `K310` proposes restricting away the bad region but leaves the crossing location, discarded mass, and exact induced variance error to be proved.
6. **Mode-curvature promotion is invalid as stated.** `K389` says reciprocal curvature at the mode tracks variance from below; that direction cannot upper-bound the variance. `K390` correctly says a localization estimate is required. `K391` then nevertheless promotes a mode-curvature bound to the whole criterion.
7. **The final certificate inherited computation-supported ancestors.** `K428` labels the lower half a certificate even though its transitive dependency graph contains the unresolved nodes above.

The correct live Branch C obligation is therefore an exact global implication

\[
\text{theta-kernel analysis}
\Longrightarrow
\text{determinant criterion for every }(r,k),
\]

with no empirical monotonicity and no unproved variance/localization substitution.

## Branch A — heat-flow instruments and obstructions

The campaign's pair energy

\[
E(t)=\sum_{i<j}(z_i-z_j)^{-2}
\]

is not a sufficient statistic for real-rootedness: exact complex-root controls can have energy zero while real controls have positive energy.

The Hermite/minor separator works on exact finite controls but becomes uninformative on natural polynomial truncations of the target entire function because those truncations themselves carry many spurious complex roots.

### Correction: the historical 64-piece envelope is numerical, not rigorous

The source code used to justify the truncation envelope computes each quantity called a cell maximum by sampling only 41 equally spaced points in that cell:

```python
PM = [
    max(abs(Phi(edges[p] + (edges[p+1]-edges[p])*i/40)) for i in range(41))
    for p in range(P)
]
```

That is not an enclosure of the true supremum. The moment, derivative and zero-shift calculations also use ordinary `mpmath` floating-point arithmetic rather than directed-rounding interval arithmetic.

Therefore the historical tail/zero-shift table is **numerical evidence only**. It does not rigorously validate the finite zero window.

A rigorous replacement would require certified cell suprema (or proved analytic monotonicity bounds), directed-rounding control of the tail/moments, a certified derivative lower bound, and a root-existence/uniqueness argument converting those enclosures into a zero interval.

See `branch-a-heat-flow-audit/README.md` for the corrected evidence-level statement.

## Branch B — screened, not solved

The arithmetic Chebyshev-error lane was only probed directly from prime powers through `x=200000`. Those finite values make no asymptotic RH claim.

Branch B remains a clean alternative lane, but Branch C is no longer excluded.

## Current handoff

The corrected state is

\[
\boxed{
\begin{array}{ll}
\text{Branch A:}&\text{useful exploratory finite numerics; proposed certificates failed;}\\
\text{Branch B:}&\text{screened and largely untouched;}\\
\text{Branch C:}&\text{valid sufficient criterion, analytic proof incomplete;}\\
\text{RH:}&\text{open.}
\end{array}}
\]

The highest-value Branch C work is now adversarial and specific: prove or kill the order/local-ascent law and the tilted-theta localization/variance inequality, then rebuild the exact dependency chain to every determinant entry before any closure claim is entertained.
