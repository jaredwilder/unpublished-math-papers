# Top-k distortion theorem for rectangular Schur polynomials

**Author:** Jared Wilder  
**Date:** 2026-09-12  
**Status:** exact elementary theorem; **not an RH proof**  
**Novelty:** new to this research estate; literature priority **unverified**

## 1. The theorem

Let

\[
\lambda=(r^k)
\]

be the rectangle with `k` rows and `r` columns. Let

\[
x=(x_1,\ldots,x_N),\qquad y=(y_1,\ldots,y_N),
\]

with `N>=k` and every `x_i,y_i>0`. Put

\[
\delta_i=\log(x_i/y_i),
\]

and let

\[
\delta_1^*\ge\delta_2^*\ge\cdots\ge\delta_N^*\ge0
\]

be the decreasing rearrangement of the absolute values `|delta_i|`.

Then

\[
\boxed{
\left|
\log\frac{s_{(r^k)}(x)}{s_{(r^k)}(y)}
\right|
\le
r\sum_{j=1}^{k}\delta_j^*.
}
\tag{1}
\]

Equivalently, after normalization by the rectangle area `rk`,

\[
\boxed{
\frac1{rk}
\left|
\log\frac{s_{(r^k)}(x)}{s_{(r^k)}(y)}
\right|
\le
\frac1k\sum_{j=1}^{k}\delta_j^*.
}
\tag{2}
\]

This is the magnitude analogue of the previously extracted top-`k` angular phase budget.

## 2. Proof

Use the positive semistandard-tableau expansion

\[
s_{(r^k)}(x)=\sum_T x^{m(T)}.
\]

For a tableau `T`, write `m_i(T)` for the number of occurrences of symbol `i`.

Because columns are strictly increasing, a fixed symbol can occur at most once in each of the `r` columns. Hence

\[
0\le m_i(T)\le r.
\tag{3}
\]

The tableau contains exactly `rk` boxes, so

\[
\sum_i m_i(T)=rk.
\tag{4}
\]

Now

\[
x^{m(T)}
=y^{m(T)}
\exp\!\left(\sum_i m_i(T)\delta_i\right).
\]

By (3)-(4), the largest possible absolute value of the linear form is obtained by spending the capacity `r` on the `k` largest `|delta_i|`:

\[
\left|
\sum_i m_i(T)\delta_i
\right|
\le
r\sum_{j=1}^{k}\delta_j^*.
\tag{5}
\]

Set

\[
B=r\sum_{j=1}^{k}\delta_j^*.
\]

Every tableau term therefore obeys

\[
e^{-B}y^{m(T)}
\le x^{m(T)}\le
e^B y^{m(T)}.
\]

Summing over tableaux gives

\[
e^{-B}s_{(r^k)}(y)
\le s_{(r^k)}(x)
\le e^B s_{(r^k)}(y),
\]

which is exactly (1).

QED.

## 3. Occupancy-cap theorem as the infinitesimal face

Define

\[
q_i(x)=x_i\frac{\partial}{\partial x_i}
\log s_{(r^k)}(x).
\]

Under the positive tableau weights, `q_i` is the expected value of `m_i(T)`. Therefore (3)-(4) immediately give

\[
\boxed{0\le q_i\le r},
\qquad
\boxed{\sum_iq_i=rk}.
\tag{6}
\]

With normalized sensitivity

\[
p_i=\frac{q_i}{rk},
\]

one gets

\[
\boxed{0\le p_i\le\frac1k},
\qquad
\boxed{\sum_i p_i=1}.
\tag{7}
\]

Thus no single spectral variable can carry more than `1/k` of the normalized logarithmic sensitivity of a rectangular Schur polynomial.

The occupancy cap is the local/derivative version of the global finite-distortion theorem (1).

## 4. Finite-defect blindness of bulk free energy

Suppose `x` and `y` differ in only `J` coordinates, where `J` is fixed as `k -> infinity`, and assume

\[
\sum_{i=1}^{J}|\delta_i|<\infty.
\]

For every `k>=J`, (2) gives

\[
\frac1{rk}
\left|
\log\frac{s_{(r^k)}(x)}{s_{(r^k)}(y)}
\right|
\le
\frac1k\sum_{i=1}^{J}|\delta_i|.
\]

Hence

\[
\boxed{
\frac1{rk}
\log\frac{s_{(r^k)}(x)}{s_{(r^k)}(y)}
\longrightarrow0
\qquad(k\to\infty).
}
\tag{8}
\]

So the leading `rk`-scale Schur free energy is asymptotically blind to any fixed finite number of bounded multiplicative spectral defects.

This is a structural warning for RH-motivated saddle analysis: a theorem that controls only

\[
\frac1{rk}\log|D_{r,k}|
\]

cannot by itself adjudicate a finite off-line defect. One must retain a defect-sensitive observable such as sign, phase, inertia, a relative-error gap, or an explicit finite-rank correction.

## 5. Relation to the angular theorem

If instead

\[
x_i=y_i e^{i\theta_i}
\]

with positive `y_i`, the same exponent-budget argument gives the monomial phase bound

\[
|\arg x^{m(T)}|
\le
r\sum_{j=1}^{k}\theta_j^*,
\]

where `theta_j^*` are the `k` largest absolute angular defects.

Thus the magnitude theorem here and the previously released top-`k` angular-budget theorem are two faces of one tableau-capacity law:

> a rectangular shape `(r^k)` has total exponent mass `rk`, but capacity at most `r` per spectral variable.

## 6. Infinite-variable extension

The theorem above is stated for finitely many positive variables, where no convergence issue is hidden.

For an infinite positive sequence, the same inequality passes to any setting in which the relevant Schur evaluations are defined as limits of the finite-variable truncations and both sides converge. No stronger infinite-dimensional claim is needed for the finite theorem itself.

## 7. Prior-art / novelty boundary

The ingredients are classical:

- semistandard-tableau expansion of Schur polynomials;
- strict increase down columns;
- homogeneity of `s_(r^k)`.

A targeted search did not locate this exact top-`k` log-distortion inequality packaged as a theorem, but that is not an exhaustive literature review. The result is therefore recorded as **exact and new to this estate**, with external novelty unresolved.

## 8. What is not claimed

This note does **not** claim:

- RH;
- a new definition of Schur polynomials;
- positivity of the Riemann consecutive minors outside their already established regions;
- that bulk free energy is useless;
- settled historical priority.

It isolates the exact amount of spectral perturbation a rectangular Schur object can feel and the precise reason fixed finite defects disappear from its normalized bulk free energy.
