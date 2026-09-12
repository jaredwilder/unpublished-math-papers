# Discrete elliptic comparison and boundary-homotopy positivity

**Author:** Jared Wilder  
**Recovered from:** RH Encirclement III

Let `D_{r,k}>0` and `B_{r,k}>0` be two positive consecutive-minor arrays satisfying the same Desnanot–Jacobi identity. Define

\[
U_{r,k}=\log\frac{D_{r,k}}{B_{r,k}}.
\]

With

\[
R^B_{r,k}=\frac{B_{r,k-1}B_{r,k+1}}{B_{r,k}^2},
\qquad
A^B_{r,k}=\frac{B_{r-1,k}B_{r+1,k}}{B_{r,k}^2},
\]

one has the exact normalized equation

\[
\boxed{
R^B_{r,k}e^{\Delta_k^2U_{r,k}}
+
A^B_{r,k}e^{\Delta_r^2U_{r,k}}
=1.
}
\]

For the factorial benchmark,

\[
R^B=\frac{k}{k+r},\qquad
A^B=\frac{r}{k+r},
\]

so

\[
\boxed{
k e^{\Delta_k^2U}+r e^{\Delta_r^2U}=k+r.}
\]

## Strong comparison principle

Let `U,V` solve the same normalized equation in a finite lattice domain `Omega`.

If

\[
W=U-V
\]

had a strict interior maximum, then

\[
\Delta_k^2W\le0,
\qquad
\Delta_r^2W\le0,
\]

with at least one strict inequality at a strict local extremum. Hence

\[
\Delta_k^2U\le\Delta_k^2V,
\qquad
\Delta_r^2U\le\Delta_r^2V,
\]

and strict monotonicity of the exponential contradicts equality of the two normalized equations.

The same argument applies to an interior minimum. Therefore

\[
\boxed{
\max_\Omega(U-V)
\le
\max_{\partial\Omega}(U-V),
}
\]

and

\[
\boxed{
\min_\Omega(U-V)
\ge
\min_{\partial\Omega}(U-V).
}
\]

A strong form follows by plateau propagation.

## Boundary-homotopy positivity theorem

Let `a_k(t)>0`, `0<=t<=1`, be a continuous coefficient homotopy and let `D_{r,k}(t)` be its consecutive Toeplitz minors.

Fix a finite lattice domain `Omega` with positive indices. Assume:

1. `D_{r,k}(0)>0` throughout `Omega` and its boundary;
2. `D_{r,k}(t)>0` on the boundary for every `t in [0,1]`;
3. the comparison determinant array `B` is positive.

Then

\[
\boxed{
D_{r,k}(t)>0
\quad\text{throughout }\Omega
\quad\text{for all }t\in[0,1].
}
\]

### Proof

Assume an interior determinant first vanishes at time `t_*`.

For `t<t_*`,

\[
U(t)=\log(D(t)/B)
\]

is finite and satisfies the normalized elliptic equation.

Boundary positivity and compactness in time give a uniform finite lower bound for `U` on `partial Omega`. The minimum principle gives the same lower bound in the interior.

But an interior determinant approaching zero would force

\[
U\to-\infty,
\]

contradicting that lower bound.

Therefore no such first interior zero exists.

QED.

## Role in the RH program

This theorem converts a two-dimensional determinant-positivity problem into a boundary-certification problem **along a homotopy**.

Target-time boundary positivity alone is insufficient because `log(D/B)` ceases to be defined after an interior determinant becomes negative. The homotopy hypothesis is therefore load-bearing, not cosmetic.
