# Critical-value / adjacent-gap monotonicity under the heat flow

**Author:** Jared Wilder  
**Recovered from:** RH Terminal Encirclement, Rounds 6–8

Let `H_t` be a real entire solution of the heat equation

\[
\partial_t H_t=-\partial_x^2H_t
\]

at a time for which the relevant zeros are real and simple.

Let adjacent zeros be

\[
x_j(t)<x_{j+1}(t),
\]

with gap

\[
g_j=x_{j+1}-x_j.
\]

Let `c_j(t)` be the critical point between them,

\[
H_t'(c_j)=0,
\]

and set

\[
V_j(t)=H_t(c_j(t)).
\]

Define the renormalized critical-value ratio

\[
\boxed{
R_j(t)=\frac{|V_j(t)|}{g_j(t)^2}.
}
\]

## 1. Zero dynamics

For a simple real zero,

\[
\boxed{
x_j'(t)=2\sum_{k\ne j}\frac1{x_j-x_k}.}
\]

Consequently the adjacent-gap square satisfies

\[
\boxed{
\frac d{dt}g_j^2
=
8
-
4g_j^2
\sum_{k\ne j,j+1}
\frac1{(x_j-x_k)(x_{j+1}-x_k)}.
}
\]

## 2. Critical-value dynamics

Since `H_t'(c_j)=0`, differentiating `V_j(t)=H_t(c_j(t))` gives

\[
\boxed{
V_j'(t)=-H_t''(c_j(t)).
}
\]

For real-rooted `H_t`, the logarithmic derivative at the critical value is

\[
\boxed{
\frac d{dt}\log|V_j(t)|
=
\sum_k\frac1{(c_j-x_k)^2}.
}
\]

## 3. Exact monotonicity theorem

Write

\[
a=c_j-x_j>0,\qquad
b=x_{j+1}-c_j>0,\qquad
g=a+b.
\]

Combining the preceding identities gives

\[
\frac{R_j'}{R_j}
=
\left(
\frac1{a^2}+\frac1{b^2}-\frac8{(a+b)^2}
\right)
+
\sum_{k\ne j,j+1}
\left[
\frac1{(c_j-x_k)^2}
+
\frac4{(x_j-x_k)(x_{j+1}-x_k)}
\right].
\]

The nearest-pair term factors exactly as

\[
\boxed{
\frac1{a^2}+\frac1{b^2}-\frac8{(a+b)^2}
=
\frac{(a-b)^2(a^2+4ab+b^2)}
{a^2b^2(a+b)^2}
\ge0.
}
\]

For every outer zero `x_k`, the factors

\[
x_j-x_k,\qquad x_{j+1}-x_k
\]

have the same sign, so

\[
\frac4{(x_j-x_k)(x_{j+1}-x_k)}>0,
\]

while

\[
\frac1{(c_j-x_k)^2}>0.
\]

Hence every outer-zero summand is strictly positive. Therefore

\[
\boxed{
R_j'(t)>0
}
\]

whenever the adjacent zeros remain distinct and real.

## Interpretation

The quantity

\[
|H_t(c_j)|/g_j^2
\]

is strictly increasing along the real-rooted heat-flow phase.

Equivalently, after normalizing the critical-value height by the square of the neighboring zero gap, the normalized barrier grows monotonically.

This is a generic exact heat-flow theorem; no Riemann-specific arithmetic input is used in the proof.

The theorem therefore does not by itself prevent a positive-time collision. Its value is as a reusable exact coordinate for collision geometry and as part of the larger RH heat-flow architecture.
