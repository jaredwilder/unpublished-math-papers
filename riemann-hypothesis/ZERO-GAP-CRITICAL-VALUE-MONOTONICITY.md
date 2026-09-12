# Critical-value / adjacent-gap monotonicity under a real-rooted heat flow

**Author:** Jared Wilder  
**Recovered from:** RH Terminal Encirclement, Rounds 6–8  
**Forensic scope correction:** 2026-09-12

## Hypotheses

Let `H_t` solve the backward heat equation

\[
\partial_tH_t=-\partial_x^2H_t
\]

on a time interval on which the zeros under discussion are real and simple.

Assume, in addition, that the standard zero-dynamics and logarithmic-derivative identities are valid with convergent (or canonically symmetric) sums:

\[
\boxed{
x_j'(t)=2\sum_{k\ne j}\frac1{x_j-x_k},
}
\]

and, at a nonzero critical value `c` with `H_t'(c)=0`,

\[
\boxed{
-\frac{H_t''(c)}{H_t(c)}
=
\sum_k\frac1{(c-x_k)^2}.
}
\]

These identities are automatic for the corresponding finite polynomial heat flow. They also hold in the standard de Bruijn–Newman real-zero setting under the usual canonical-product/summation conventions used in the zero-dynamics literature. They are **not** asserted here for an arbitrary real entire heat solution without such hypotheses.

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

and assume its critical value

\[
V_j(t)=H_t(c_j(t))
\]

is nonzero (automatic between distinct consecutive simple real zeros in the real-rooted polynomial/canonical-product setting).

Define

\[
\boxed{
R_j(t)=\frac{|V_j(t)|}{g_j(t)^2}.
}
\]

## 1. Adjacent-gap dynamics

From the zero ODE,

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

Indeed,

\[
g_j'
=
\frac4{g_j}
-2g_j\sum_{k\ne j,j+1}
\frac1{(x_j-x_k)(x_{j+1}-x_k)}.
\]

## 2. Critical-value dynamics

Since `H_t'(c_j)=0`, differentiating `V_j(t)=H_t(c_j(t))` gives

\[
\boxed{
V_j'(t)=-H_t''(c_j(t)).
}
\]

Using the stated logarithmic-derivative identity,

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

For every outer zero `x_k`, adjacency implies that

\[
x_j-x_k,\qquad x_{j+1}-x_k
\]

have the same sign. Hence

\[
\frac4{(x_j-x_k)(x_{j+1}-x_k)}>0,
\qquad
\frac1{(c_j-x_k)^2}>0.
\]

Therefore every outer-zero summand is strictly positive, and

\[
\boxed{
R_j'(t)>0
}
\]

whenever the hypotheses above hold and the adjacent zeros remain distinct and real.

## Interpretation

Within the real-zero phase of a heat flow for which the stated canonical-product dynamics are valid, the quantity

\[
\boxed{
\frac{|H_t(c_j)|}{(x_{j+1}-x_j)^2}
}
\]

is strictly increasing in `t`.

The theorem is exact once the zero-dynamics/log-derivative hypotheses are available. It is not, by itself, an obstruction to a later collision and contains no Riemann-specific arithmetic input.

## Scope note

The previous public version described this as a theorem for a generic “real entire solution” of the heat equation. That wording was too broad. The proof uses the zero-sum identities displayed at the beginning, so the correct theorem class is:

- finite real-rooted polynomial heat flows; and
- infinite canonical-product heat flows, including the de Bruijn–Newman family in the real-zero phase, when those sums and identities are justified.

No claim is made outside that class.
