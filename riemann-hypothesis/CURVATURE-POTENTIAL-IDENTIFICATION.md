# Exact identification of the September curvature variable with the Encirclement II–III potential

**Author:** Jared Wilder  
**Synthesis:** 2026-09-11, connecting the recovered August Encirclement II–III program to the September fixed-slope computation

This note identifies two variables introduced in different RH campaigns and shows that the September computation measures an exact discrete-curvature anisotropy of the August comparison potential.

## 1. Two neighboring-minor ratios

For consecutive Toeplitz minors `D_{r,k}`, define

\[
R_{r,k}
=
\frac{D_{r,k-1}D_{r,k+1}}{D_{r,k}^2},
\]

and

\[
A_{r,k}
=
\frac{D_{r-1,k}D_{r+1,k}}{D_{r,k}^2}.
\]

Desnanot–Jacobi gives the exact relation

\[
\boxed{R_{r,k}+A_{r,k}=1.}
\]

Encirclement II used the odds

\[
Y_{r,k}=\frac{A_{r,k}}{R_{r,k}}.
\]

Its exact factorial/rational benchmark is

\[
Y^*_{r,k}=\frac rk.
\]

The corresponding Encirclement-II normalized field is

\[
\boxed{
Z_{\rm II}(r,k)
=
\frac{k}{r}\frac{A_{r,k}}{R_{r,k}}.
}
\]

It is identically one on the factorial benchmark.

## 2. September normalized curvature variable

The September run instead defined

\[
\boxed{
Z_{\rm Sep}(r,k)
=
\frac{r}{k}\frac{R_{r,k}}{A_{r,k}}.
}
\]

Therefore the two independently introduced normalizations satisfy the exact identity

\[
\boxed{
Z_{\rm Sep}(r,k)=\frac1{Z_{\rm II}(r,k)}.
}
\]

So the September fixed-slope experiment is not a new unrelated statistic. It is the reciprocal coordinate on the exact normalized odds field isolated by Encirclement II.

---

## 3. Identification with the Encirclement-III comparison potential

Let `B_{r,k}>0` be the factorial comparison determinant and define

\[
U_{r,k}=\log\frac{D_{r,k}}{B_{r,k}}.
\]

Encirclement III proved the exact nonlinear comparison equation

\[
R^B_{r,k}e^{\Delta_k^2U_{r,k}}
+
A^B_{r,k}e^{\Delta_r^2U_{r,k}}
=1.
\]

For the factorial benchmark,

\[
R^B_{r,k}=\frac{k}{k+r},
\qquad
A^B_{r,k}=\frac{r}{k+r}.
\]

Put

\[
\theta=\frac{k}{k+r}.
\]

Then

\[
R=\theta e^{\Delta_k^2U},
\qquad
A=(1-\theta)e^{\Delta_r^2U}.
\]

Substituting into the September normalization gives complete cancellation of the benchmark factors:

\[
Z_{\rm Sep}
=
\frac{1-\theta}{\theta}
\frac{\theta e^{\Delta_k^2U}}
{(1-\theta)e^{\Delta_r^2U}}.
\]

Hence

\[
\boxed{
Z_{\rm Sep}
=
e^{\Delta_k^2U-\Delta_r^2U}.
}
\]

Equivalently,

\[
\boxed{
\log Z_{\rm Sep}
=
\Delta_k^2U-\Delta_r^2U.
}
\]

The September observable is therefore **exactly the anisotropy between the shift-direction and order-direction discrete curvatures of the normalized log-determinant potential**.

---

## 4. Recovering both curvatures from `Z`

Write

\[
x=\Delta_k^2U,
\qquad
y=\Delta_r^2U,
\qquad Z=Z_{\rm Sep}.
\]

The exact equations are

\[
\theta e^x+(1-\theta)e^y=1,
\]

and

\[
e^{x-y}=Z.
\]

Therefore

\[
e^y=\frac1{(1-\theta)+\theta Z},
\]

so

\[
\boxed{
\Delta_r^2U
=-\log\big((1-\theta)+\theta Z\big),
}
\]

and

\[
\boxed{
\Delta_k^2U
=
\log Z-
\log\big((1-\theta)+\theta Z\big).
}
\]

Thus a fixed-slope limit for `Z` immediately determines a candidate limiting pair of discrete curvatures.

---

## 5. Meaning of the September fixed-slope data

The reproduced September computation gives positive-limit fits

\[
A(1/2)\approx0.278934,
\qquad
A(2/3)\approx0.397941,
\qquad
A(3/4)\approx0.444954
\]

on the three adequately deep tested slices.

If those finite-slope limits persist asymptotically, they are not merely limits of an arbitrary determinant ratio: they are finite nonzero limits of

\[
e^{\Delta_k^2U-\Delta_r^2U}.
\]

Equivalently, they specify a nontrivial aspect-ratio profile for the anisotropy of the exact Encirclement-III comparison potential.

The numerical evidence does not prove existence of that profile. The identification of the measured quantity with the curvature anisotropy is exact.

---

## 6. Connection to the reciprocal/Jacobi–Trudi involution

The September run also proved

\[
Z_a(r,k)Z_e(k,r)=1
\]

for a sequence and its reciprocal/Jacobi–Trudi dual.

Under the compactified ratio

\[
\theta=\frac{k}{k+r},
\]

the transpose sends

\[
\theta\longmapsto1-\theta.
\]

Therefore any limiting profile satisfies, wherever both sides exist,

\[
\boxed{
A_a(\theta)A_e(1-\theta)=1.
}
\]

The two halves of the aspect-ratio problem are thus linked by an exact reciprocal-series duality rather than being independent asymptotic regimes.

---

## 7. Programmatic consequence

The August and September campaigns are studying the same nonlinear object in reciprocal coordinates:

\[
\boxed{
\text{Encirclement II normalized odds}
\;\longleftrightarrow\;
\text{September determinant curvature}
\;\longleftrightarrow\;
\text{Encirclement III discrete-curvature anisotropy}.
}
\]

This identification turns the September fixed-slope experiment into a direct numerical probe of the exact nonlinear comparison geometry isolated by Encirclement II–III.
