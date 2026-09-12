# Branch C readjudication — the epoch-23 falsifier does not refute the global strict criterion

**Author:** Jared Wilder  
**Date:** 2026-09-12  
**Status:** correction of the epoch-23 Branch C retraction; RH remains open

## Executive result

The epoch-23 conclusion that Branch C's determinant criterion is *not sufficient* for the Riemann target was based on a domain mismatch.

The falsifier constructed **finite polynomials**, tested the criterion on an **interior subset** of their finite Toeplitz lattices, and then interpreted the surviving objects as counterexamples to the implication needed for the Riemann xi coefficient sequence.

That implication is instead a statement about an **infinite coefficient sequence with `a_k > 0` for every `k`** and a strict consecutive-minor lattice. Under that hypothesis the criterion is sufficient to force strict positivity of all consecutive minors, and a classical Schoenberg/Katkova criterion then promotes those minors to total positivity.

Therefore:

- the `1686/3059` and `1445/2284` finite-polynomial screens remain valid computations at their stated finite/interior scope;
- they **do not refute** the global infinite-positive-sequence implication;
- Branch C is **not dead for the reason stated in epoch 23**;
- this correction is **not a proof of RH**, because the campaign did not actually prove the determinant inequality globally for the xi coefficients.

The live obstruction is analytic and occurs *below* the classical total-positivity implication.

## 1. The criterion

Let

\[
D_{r,k}=\det[a_{k+j-i}]_{i,j=0}^{r-1},
\qquad a_n=0\quad(n<0),
\]

with `D_{0,k}=1`.

The original Branch C entry is

\[
\boxed{
(k+r)D_{r,k-1}D_{r,k+1}\le kD_{r,k}^2
}
\qquad(r,k\ge1).
\]

Using Desnanot–Jacobi,

\[
D_{r+1,k}D_{r-1,k}
=D_{r,k}^2-D_{r,k-1}D_{r,k+1},
\]

this is equivalent to the square-free form

\[
\boxed{
rD_{r,k-1}D_{r,k+1}
\le kD_{r+1,k}D_{r-1,k}.}
\]

## 2. Sufficiency for strict consecutive-minor positivity

Assume

\[
a_k>0\qquad\text{for every }k\ge0
\]

and assume the original criterion for every `r,k >= 1`.

Then

\[
D_{r,k-1}D_{r,k+1}
\le \frac{k}{k+r}D_{r,k}^2.
\]

Hence Desnanot–Jacobi gives

\[
\begin{aligned}
D_{r+1,k}D_{r-1,k}
&=D_{r,k}^2-D_{r,k-1}D_{r,k+1}\\
&\ge \frac{r}{k+r}D_{r,k}^2.
\end{aligned}
\]

If `D_{r-1,k}>0` and `D_{r,k}>0`, the right side is strictly positive, so

\[
D_{r+1,k}>0.
\]

The bases are

\[
D_{0,k}=1,
\qquad
D_{1,k}=a_k>0.
\]

Thus two-step induction in `r` yields

\[
\boxed{D_{r,k}>0\quad\text{for every }r\ge0,\ k\ge1.}
\]

At `k=0` the Toeplitz block is triangular with diagonal `a_0`, so

\[
D_{r,0}=a_0^r>0.
\]

Therefore the criterion plus everywhere-positive coefficients forces the **entire strict consecutive-minor lattice**.

## 3. Classical promotion to total positivity

Katkova's 2005 paper *Multiple positivity and the Riemann zeta-function* states the relevant classical criterion explicitly in Section 2:

> if all minors of orders `1,...,m` composed of consecutive rows and consecutive columns are positive, then all minors of those orders are positive.

The paper also gives the Toeplitz-sequence version (Lemma 3) for a positive sequence and consecutive-column minors, concluding membership in `PF_m`.

Source:

- Olga M. Katkova, *Multiple positivity and the Riemann zeta-function*, arXiv:math/0505174 (2005): https://arxiv.org/html/math/0505174v1

Applying the statement for every finite `m` gives `PF_infinity`. For the transformed xi generating function, the Aissen–Schoenberg–Whitney–Edrei/Laguerre–Pólya equivalence is the standard bridge from `PF_infinity` to real nonpositive zeros, hence to RH under the xi substitution.

So the classical top link is real.

## 4. Why the epoch-23 counterexamples miss the hypothesis

The exact audit source contains the line

```python
if k+r+1>=N: continue
```

which deliberately discards the terminating-polynomial boundary.

Every constructed object is a polynomial of finite degree. Therefore, if its coefficient array has length `N`,

\[
a_N=0,
\qquad
D_{1,N}=0.
\]

Such an object cannot satisfy the everywhere-positive coefficient premise or the strict infinite consecutive-minor premise used above.

A fresh seeded rerun reproduces the epoch-23 count exactly:

```text
seeded non-real-rooted polynomials tested: 2284
interior hits for original criterion: 1445
hits violating everywhere-positive coefficient premise: 1445
```

Thus **1445/1445 purported counterexamples lie outside the load-bearing hypothesis**.

The smaller witness `1+z^5` remains a valid refutation of the statement

> nonnegative consecutive minors imply total positivity,

but it does not refute the strict version. Its zeros in the coefficient sequence are exactly why.

## 5. What the correction does *not* prove

Restoring the classical implication does not close RH, because the epoch-22 claim that the criterion's "lower half is complete" does not survive a dependency audit.

Several load-bearing steps were still recorded as `COMPUTATION_SUPPORTED` or explicitly open:

1. **Order/local-ascent step.** `K347` says the order step ascends at every measured entry but names as open "a proof of the order step's ascent."
2. **Order-arm to variance bridge.** `K384` says the moment log-convexity excess is identified with the tilted-log variance only *to within a percent* and explicitly leaves the exact error terms open.
3. **Variance comparison.** `K385` records the desired theta-vs-Gaussian variance inequality as measured and explicitly open.
4. **Curvature-at-mode substitution.** `K389` says the reciprocal mode curvature tracks the variance **from below**. That direction cannot upper-bound the variance. `K390` correctly notes that a localization estimate is required because a mode curvature bound is not a global Poincare/Brascamp–Lieb bound.
5. **Failed global log-concavity.** `K308` records that the tilted density is log-convex in the far-left tail, so the naive global Brascamp–Lieb hypothesis is false. `K310` proposes a restricted-measure repair but leaves the crossing, discarded mass and induced variance error to be made rigorous.
6. **Unsupported promotion.** `K391` nevertheless promotes the mode-curvature condition to the whole criterion, and `K428` later labels the lower half a certificate. That promotion skips the unresolved localization/variance theorem and the earlier exact order-axis gaps.

The correct current status is therefore:

\[
\boxed{
\text{global determinant criterion is sufficient for RH, but it has not been proved for the xi coefficients.}
}
\]

## 6. Current Branch C frontier

Branch C should be reopened as a mathematically valid route with a precise proof obligation rather than marked dead.

At minimum, a complete proof still needs an exact route from the theta-kernel estimates to the **full two-dimensional determinant inequality for every `r,k`**. The campaign's measured order-ascent statements and its mode-curvature/variance localization step are not yet such a proof.

The correct next adversarial tests are therefore not more finite non-real-rooted polynomials. They are:

1. prove or refute the order/local-ascent statement on the actual xi determinant lattice;
2. derive an exact variance/localization inequality for the tilted theta measure, with the far-left non-log-concave tail paid rigorously;
3. reconstruct the dependency chain from those statements to every `D_{r,k}` without replacing exact implications by asymptotic numerical agreement;
4. only then combine the resulting global criterion with the strict consecutive-minor theorem above.

RH remains open pending those steps.
