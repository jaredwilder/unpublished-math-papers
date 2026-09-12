# A tilted-theta cumulant coordinate for consecutive Toeplitz determinants

**Author:** Jared Wilder  
**Date:** 2026-09-12  
**Status:** exact reformulation / cross-epoch synthesis; no RH claim; novelty not asserted

## Setup

Let

\[
m_{2k}=\int_0^\infty u^{2k}\Phi(u)\,du,
\qquad
a_k=\frac{m_{2k}}{\Gamma(2k+1)},
\]

where `Phi` is the positive theta kernel used in the standard cosine-transform representation of the completed zeta function.

For each `k` with `m_{2k}>0`, define the probability measure

\[
d\nu_k(u)=\frac{u^{2k}\Phi(u)}{m_{2k}}\,du,
\]

and, for `U ~ nu_k`, define

\[
X_k=2\log U,
\qquad
K_k(s)=\log \mathbb E_{\nu_k} e^{sX_k}
\]

whenever the expectation is finite.

## Exact coefficient-ratio identity

For every integer shift `s` for which the coefficient index is nonnegative,

\[
\boxed{
\frac{a_{k+s}}{a_k}
=
\frac{\Gamma(2k+1)}{\Gamma(2k+2s+1)}
\,\mathbb E_{\nu_k}e^{sX_k}.
}
\]

This is immediate from

\[
\mathbb E_{\nu_k}e^{sX_k}
=
\frac{1}{m_{2k}}
\int_0^\infty u^{2k+2s}\Phi(u)\,du
=
\frac{m_{2k+2s}}{m_{2k}}.
\]

Therefore, writing the consecutive Toeplitz minor as

\[
D_{r,k}=\det[a_{k+j-i}]_{0\le i,j<r},
\]

we obtain, whenever `k >= r-1`,

\[
\boxed{
\frac{D_{r,k}}{a_k^r}
=
\det_{0\le i,j<r}
\left[
\frac{\Gamma(2k+1)}{\Gamma(2k+2(j-i)+1)}
\exp(K_k(j-i))
\right].
}
\]

Thus the full normalized `r x r` determinant is encoded by a **single** tilted random variable `X_k`: the matrix samples its cumulant-generating function at the integer differences

\[
s=j-i\in\{-(r-1),\dots,r-1\}.
\]

## The first Toeplitz row is the symmetric CGF increment

At determinant order two / the first log-concavity row, the relevant moment ratio is

\[
\frac{m_{2k-2}m_{2k+2}}{m_{2k}^2}.
\]

Under the same tilted law,

\[
\boxed{
K_k(1)+K_k(-1)
=
\log\frac{m_{2k+2}m_{2k-2}}{m_{2k}^2}.
}
\]

Hence the classical theta-kernel Turan inequality

\[
\frac{m_{2k-2}m_{2k+2}}{m_{2k}^2}
\le
\frac{2k+1}{2k-1}
\]

is equivalently

\[
\boxed{
K_k(1)+K_k(-1)
\le
\log\frac{2k+1}{2k-1}.
}
\]

When `K_k` is analytic on `[-1,1]`, its symmetric expansion is

\[
K_k(1)+K_k(-1)
=
\kappa_2(X_k)
+\frac{\kappa_4(X_k)}{12}
+\frac{\kappa_6(X_k)}{360}
+\cdots.
\]

This identifies the campaign's earlier variance/cumulant calculations as the **local-shift expansion of the same object** that controls the whole Toeplitz determinant.

## Local versus fixed-slope regimes

This coordinate makes a useful distinction explicit.

For `r` small compared with `k`, the determinant samples `K_k(s)` only at relatively small `|s|`; low cumulants may be informative.

For fixed-slope scaling `r ~ theta k`, the determinant samples shifts as large as `|s| = Theta(k)`. Low-order cumulants alone cannot describe that regime. The natural analytic object is then the macroscopic scaled CGF / large-deviation transform.

So two research lanes that appeared separate in the original campaign are the same coordinate at different scales:

\[
\boxed{
\text{local moments / variance}
\quad\longleftrightarrow\quad
K_k(s)
\quad\longleftrightarrow\quad
\text{fixed-slope Toeplitz geometry}.
}
\]

## Scope and novelty

The displayed identities are exact. They do **not** establish positivity of the determinants and do **not** prove RH.

Probabilistic and moment representations of the Riemann `Xi` kernel are classical and active subjects. A targeted search performed on 2026-09-12 did not locate this exact coefficient-tilted determinant packaging, but that is not enough to assert literature novelty. This note is therefore published as a **structural coordinate/synthesis**, with provenance and date recorded, while broader literature review continues.
