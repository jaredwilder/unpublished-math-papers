# Desnanot log-odds dynamics and the exact Fisher-source identity

**Author:** Jared Wilder  
**Date:** 2026-09-12  
**Status:** exact corollary for positive determinant homotopies; **not an RH proof**  
**Novelty:** cross-route synthesis new to this estate; historical priority unverified

## 1. Setup

Let `D_(r,k)(t)>0` be a `C^2` positive determinant homotopy satisfying the normalized Desnanot identity

\[
R_{r,k}(t)+A_{r,k}(t)=1,
\]

where

\[
R:=\frac{D_{r,k-1}D_{r,k+1}}{D_{r,k}^2},
\qquad
A:=\frac{D_{r-1,k}D_{r+1,k}}{D_{r,k}^2}.
\]

Let `B` be a fixed positive comparison array satisfying the same identity and put

\[
U=\log(D/B),
\qquad
V=\partial_tU,
\qquad
W=\partial_t^2U.
\]

The dynamic Desnanot theorem gives

\[
R\Delta_k^2V+A\Delta_r^2V=0
\tag{1}
\]

and

\[
L_DW
:=R\Delta_k^2W+A\Delta_r^2W
=-R(\Delta_k^2V)^2-A(\Delta_r^2V)^2.
\tag{2}
\]

## 2. Log-odds coordinate

Define the determinant log-odds

\[
\boxed{
\ell:=\log\frac{A}{R}.
}
\tag{3}
\]

Because

\[
\partial_t\log R=\Delta_k^2V,
\qquad
\partial_t\log A=\Delta_r^2V,
\]

we have

\[
\dot\ell
=\Delta_r^2V-\Delta_k^2V.
\tag{4}
\]

Set

\[
u:=\Delta_k^2V,
\qquad
v:=\Delta_r^2V.
\]

Equation (1) is

\[
Ru+Av=0,
\]

while (4) is

\[
v-u=\dot\ell.
\]

Solving the two scalar equations gives the exact identities

\[
\boxed{
\Delta_k^2V=-A\dot\ell,
\qquad
\Delta_r^2V=R\dot\ell.
}
\tag{5}
\]

Thus the two lattice curvatures of the logarithmic velocity are not independent. They are the two complementary shares of one scalar log-odds velocity.

## 3. Logistic evolution of the Desnanot weights

Since

\[
\dot R=R\Delta_k^2V,
\qquad
\dot A=A\Delta_r^2V,
\]

substituting (5) yields

\[
\boxed{
\dot R=-RA\dot\ell,
\qquad
\dot A=RA\dot\ell.
}
\tag{6}
\]

Because `A=1-R`, this is exactly the differential identity for the logit coordinate

\[
\ell=\log\frac{1-R}{R}.
\]

The rational-orbit / odds formulation and the dynamic determinant formulation are therefore not merely compatible coordinate systems: their time evolution is algebraically locked.

## 4. Exact Fisher-source collapse

Insert (5) into the quadratic source in (2):

\[
R(\Delta_k^2V)^2+A(\Delta_r^2V)^2
=RA^2\dot\ell^2+AR^2\dot\ell^2.
\]

Since `R+A=1`,

\[
\boxed{
R(\Delta_k^2V)^2+A(\Delta_r^2V)^2
=RA\dot\ell^2.
}
\tag{7}
\]

Hence the acceleration equation becomes

\[
\boxed{
L_DW=-RA\dot\ell^2.
}
\tag{8}
\]

Using (6), the same source can be written

\[
\boxed{
L_DW
=-\frac{\dot R^2}{R(1-R)}
=-\frac{\dot A^2}{A(1-A)}.
}
\tag{9}
\]

The quantity

\[
\frac{\dot R^2}{R(1-R)}
\]

is exactly the one-dimensional Fisher-information metric density for a Bernoulli parameter moving along the path `R(t)`. Thus the negative forcing of the determinant-potential acceleration is the negative Bernoulli Fisher energy of the moving Desnanot split.

This interpretation is optional; equations (7)-(9) are purely algebraic.

## 5. Relation to the rational orbit

The odds variable used in the earlier determinant program is

\[
Y:=\frac{A}{R}=e^\ell.
\]

For the factorial background,

\[
Y^*_{r,k}=\frac rk.
\]

The live Branch-C criterion in the positive determinant region is exactly

\[
Y\ge\frac rk.
\]

The present theorem shows that the **motion** of this same odds coordinate controls the signed second variation of the normalized determinant potential:

\[
\boxed{
L_D(\partial_t^2U)
=-RA\bigl(\partial_t\log Y\bigr)^2.
}
\tag{10}
\]

So the static rational-orbit program and the dynamic heat/homotopy program meet in one scalar quantity `partial_t log Y`.

## 6. Rigidity of zero source

At a lattice point in the positive phase, the following are equivalent:

\[
L_DW=0,
\]

\[
\dot\ell=0,
\]

\[
\dot R=\dot A=0,
\]

and, by (5),

\[
\Delta_k^2V=\Delta_r^2V=0.
\]

Thus the quadratic source vanishes exactly when the local Desnanot odds are instantaneously stationary.

## 7. Scope

No de Bruijn–Newman PDE is required for this generic identity. It applies to any `C^2` positive determinant homotopy with a fixed positive comparison array.

For the Xi coefficient heat flow, it gives an exact interpretation of the adaptive-superharmonic source while all neighboring minors remain positive.

It does **not** prove:

- Branch C for Xi;
- persistence of determinant positivity;
- a global no-escape theorem;
- monotonicity of the odds in time;
- RH.

## 8. Prior-art boundary

Dodgson/Desnanot condensation, octahedron recurrences, Toda systems and information-geometric Bernoulli metrics are classical subjects. A targeted search did not locate this exact log-odds reduction of the dynamic normalized-Desnanot source.

Because the derivation is short once both coordinate systems are placed side by side, historical novelty is left **unverified** rather than asserted.
