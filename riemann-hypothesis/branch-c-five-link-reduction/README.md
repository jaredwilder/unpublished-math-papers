# Branch C — determinant criterion: readjudicated and open as a route

**Author:** Jared Wilder  
**Historical reduction:** 2026-09-11 / epochs 20–22  
**Erroneous retraction:** 2026-09-12 / epoch 23  
**Readjudication:** 2026-09-12

## Current verdict

**Branch C is not refuted by the epoch-23 finite-polynomial falsifier. It is also not a proof of RH.**

The current state is sharper:

1. the global determinant criterion used by the branch is a valid sufficient criterion for the Riemann target when applied to the infinite xi coefficient sequence with `a_k>0` for every `k`;
2. the epoch-23 `1686/3059` and `1445/2284` counterexamples are finite-support objects tested only on an interior lattice and therefore lie outside the load-bearing strict/infinite hypothesis;
3. the campaign nevertheless did **not** prove the global criterion for the xi coefficients, because several analytic reductions remained measured or open and were later promoted too aggressively to a certificate.

The full readjudication is in:

`BRANCH-C-READJUDICATION-2026-09-12.md`

## The global criterion

For consecutive Toeplitz minors

\[
D_{r,k}=\det[a_{k+j-i}]_{i,j=0}^{r-1},
\qquad a_n=0\ (n<0),
\]

Branch C studies

\[
\boxed{
(k+r)D_{r,k-1}D_{r,k+1}\le kD_{r,k}^2
}
\qquad(r,k\ge1),
\]

or equivalently, using Desnanot–Jacobi,

\[
\boxed{
rD_{r,k-1}D_{r,k+1}
\le kD_{r+1,k}D_{r-1,k}.}
\]

If `a_k>0` for every `k`, the original form gives

\[
D_{r+1,k}D_{r-1,k}
\ge \frac{r}{k+r}D_{r,k}^2>0.
\]

Starting from `D_{0,k}=1` and `D_{1,k}=a_k>0`, two-step induction in `r` yields strict positivity of every consecutive minor. The `k=0` blocks are triangular and have determinant `a_0^r>0`.

A classical consecutive-minor criterion, explicitly quoted as Theorem D and in Toeplitz-sequence form as Lemma 3 in Katkova's 2005 paper *Multiple positivity and the Riemann zeta-function*, promotes strict consecutive-minor positivity to the relevant `PF_m` property for every finite `m`, hence to `PF_infinity`.

Source: https://arxiv.org/html/math/0505174v1

For the transformed xi generating function, `PF_infinity` is the classical Laguerre–Pólya/ASWE condition equivalent to RH.

So the top implication is real.

## Why the epoch-23 kill fails

The old audit deliberately restricted to the interior of a finite polynomial coefficient window:

```python
if k+r+1>=N: continue
```

Every test object is a polynomial. Hence after its last coefficient,

\[
a_N=0,
\qquad D_{1,N}=0.
\]

It therefore cannot satisfy the infinite positive-coefficient / strict-consecutive-minor hypothesis of the Riemann sequence.

The fresh exact re-audit reproduces the historical counts and records the domain failure:

```text
seeded non-real-rooted polynomials tested: 2284
interior hits for original criterion: 1445
hits violating everywhere-positive coefficient premise: 1445
```

See:

- `branchc_reaudit_20260912.py`
- `branchc_reaudit_20260912.out.txt`

The small sequence `a=(1,0,0,0,0,1)` remains a valid counterexample to **nonnegative** consecutive-minor positivity implying total positivity. It does not refute the **strict** criterion.

## What remains genuinely proved or certified

The readjudication does not disturb the standalone mathematics accumulated by the branch, including:

- Desnanot–Jacobi identities and exact rearrangements;
- determinant/curvature normalizations;
- exact factorial/exponential benchmark identities;
- the exact first-rung/corner reductions;
- rational interval certifications of theta-kernel inequalities;
- the Gaussian-normalized moment formulation;
- the exact theta-tail enclosure;
- recovered kernel-checked algebraic receipts;
- the August determinant geometry, boundary comparison and Schur/phase results.

Those objects retain their stated scope.

## What is *not* proved

The epoch-22 sentence that the criterion's “lower half is complete” does not survive dependency-level review.

Load-bearing unresolved steps include:

- **order/local ascent:** the campaign measured the determinant-lattice order step but explicitly left its proof open;
- **exact order-arm reduction:** the identification of the order-arm residue with the tilted-log variance was numerical/asymptotic with exact error terms left open;
- **variance comparison:** the theta tilted-log variance was measured below the Gaussian/trigamma target, not proved globally;
- **localization:** the tilted density is log-convex in a far-left region, so global Brascamp–Lieb cannot be invoked as written;
- **mode curvature is not variance control:** the reciprocal curvature at the mode was observed to track the variance from below. Proving a lower bound on curvature at one point cannot by itself provide the required global upper bound on variance.

The campaign itself had correctly identified the need for a restricted-measure/localization repair before later skipping it.

## Correct frontier

Branch C is therefore a **live sufficient-criterion route with a real analytic gap**, not a dead route and not a solved one.

The decisive remaining tasks are:

1. prove or refute the order/local-ascent statement on the actual xi determinant lattice;
2. establish an exact localization/variance inequality for the tilted theta measure, including the non-log-concave far-left tail and its contribution;
3. reconstruct an exact implication from those analytic statements to the determinant criterion at every order and shift;
4. then apply the strict consecutive-minor theorem.

RH remains open.

## Historical record

The epoch-23 falsifier sources and outputs remain in this directory. They should now be read as a negative-control lesson:

> a false-target test only refutes an implication when the false-target object satisfies the **same global hypotheses** as the intended theorem.

The earlier campaign checked an interior finite analogue and silently dropped the infinite-support/strictness hypothesis. The readjudication corrects that scope error without deleting the original evidence.
