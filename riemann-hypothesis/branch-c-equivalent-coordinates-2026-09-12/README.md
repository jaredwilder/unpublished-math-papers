# Branch C in three exact coordinates: determinant inequality, rational orbit, and discrete curvature

**Author:** Jared Wilder  
**Date:** 2026-09-12  
**Status:** exact algebraic synthesis inside the positive determinant domain; **not an RH proof**  
**Novelty:** cross-epoch synthesis; historical priority not asserted

## 1. The live criterion

For consecutive Toeplitz minors `D_(r,k)`, the live Branch-C sufficient criterion is

\[
\boxed{
(k+r)D_{r,k-1}D_{r,k+1}
\le
kD_{r,k}^2
}
\qquad(r,k\ge1).
\tag{C}
\]

On an infinite coefficient sequence with `a_k>0` for every `k`, a global proof of (C), together with Desnanot–Jacobi, inductively forces all consecutive minors positive. The classical strict-consecutive-minor / Pólya-frequency machinery then gives the standard total-positivity route used in the Xi setting.

That global Xi proof is **not** present here.

This note records that three apparently separate campaigns were in fact attacking exact equivalent forms of (C).

## 2. Desnanot normalized coordinates

Define

\[
R_{r,k}
=
\frac{D_{r,k-1}D_{r,k+1}}{D_{r,k}^2},
\qquad
A_{r,k}
=
\frac{D_{r-1,k}D_{r+1,k}}{D_{r,k}^2}.
\]

In the positive determinant region, the Desnanot–Jacobi identity gives

\[
\boxed{R_{r,k}+A_{r,k}=1.}
\tag{1}
\]

Criterion (C) is exactly

\[
R_{r,k}\le\frac{k}{k+r}.
\tag{2}
\]

## 3. Rational-orbit form

Introduce the odds variable

\[
Y_{r,k}:=\frac{A_{r,k}}{R_{r,k}}.
\]

Using (1),

\[
Y=\frac{1-R}{R}.
\]

Therefore (2) is equivalent to

\[
\boxed{
Y_{r,k}\ge\frac{r}{k}.
}
\tag{3}
\]

The earlier Encirclement-II analysis independently found the exact rational solution family

\[
Y_{r,k}^{\mu,\nu}
=
\frac{r+\mu}{k+\nu},
\]

and the factorial Toeplitz benchmark selects

\[
\boxed{Y^*_{r,k}=\frac{r}{k}.}
\tag{4}
\]

Thus Branch C is precisely the assertion that the Xi odds lattice stays on or above the factorial rational orbit.

Define

\[
Z_{r,k}:=\frac{k}{r}Y_{r,k}.
\]

Then

\[
\boxed{
(C)
\iff
Z_{r,k}\ge1.
}
\tag{5}
\]

So the September Branch-C inequality and the August rational-orbit program were not different terminal targets. They were two coordinates for the same target.

## 4. Factorial-normalized curvature form

Let `B_(r,k)>0` be the factorial benchmark determinant array and set

\[
U_{r,k}:=\log\frac{D_{r,k}}{B_{r,k}}.
\]

The normalized comparison identity gives

\[
R^D_{r,k}
=
R^B_{r,k}
\exp(\Delta_k^2 U_{r,k}),
\tag{6}
\]

where

\[
\Delta_k^2U_{r,k}
:=U_{r,k-1}-2U_{r,k}+U_{r,k+1}
\]

and for the factorial benchmark

\[
R^B_{r,k}=\frac{k}{k+r}.
\tag{7}
\]

Combining (2), (6), and (7),

\[
\boxed{
(C)
\iff
\Delta_k^2U_{r,k}\le0.
}
\tag{8}
\]

Thus Branch C is also exactly the statement that the factorial-normalized log determinant is discretely concave in the shift direction.

## 5. The exact equivalence package

Inside the positive determinant domain,

\[
\boxed{
\begin{array}{c}
(k+r)D_{r,k-1}D_{r,k+1}\le kD_{r,k}^2
\\[1mm]\Updownarrow\\[1mm]
R_{r,k}\le k/(k+r)
\\[1mm]\Updownarrow\\[1mm]
Y_{r,k}\ge r/k
\\[1mm]\Updownarrow\\[1mm]
Z_{r,k}\ge1
\\[1mm]\Updownarrow\\[1mm]
\Delta_k^2\log(D/B)\le0.
\end{array}
}
\tag{9}
\]

This is algebraic, not heuristic.

## 6. Why the synthesis matters

Three older research programs now become three proof engines for one theorem:

### Orbit engine

Construct an invariant region around the exact background orbit `Z=1` and prove the Xi seed never crosses below it.

### Discrete-elliptic engine

Use the normalized potential `U=log(D/B)`, its comparison principle, and boundary/homotopy machinery to propagate the curvature sign through finite domains.

### Theta/localization engine

Prove the needed tilted-theta localization/variance inequality strongly enough to derive the same shift-curvature sign directly.

These should not be scheduled as independent RH programs anymore. Any advance or counterexample in one coordinate should immediately be translated into the other two.

## 7. Relation to the external cubic wedge

An external 2026 result proves positivity of the Xi consecutive minors in a large cubic tail region. That removes a large portion of the positivity lattice, but it does **not** establish (C), (5), or (8) in the complementary two-scale region.

Therefore the live target remains the orbit/curvature inequality itself, not merely “prove positivity somewhere at large indices.”

## 8. What is not claimed

This note does **not** claim:

- RH;
- a proof of (C) for all Xi indices;
- that discrete concavity holds outside the positive determinant domain where `log(D/B)` is defined;
- that the historical rational-orbit family itself is novel;
- that any one of the three proof engines is complete.

It records the exact identification of a single live theorem that the estate had been treating as several different programs.
