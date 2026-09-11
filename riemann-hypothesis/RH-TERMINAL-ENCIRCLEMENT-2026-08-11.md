# Riemann Hypothesis — Terminal Encirclement

**Campaign:** 2026-08-11, ten rounds  
**Disposition:** `StrictFrontierTheorem / SurvivingCapability`  
**Court:** **RH IS NOT PROVED BY THIS PACKET.**

This is the public mathematical extraction of the terminal campaign. It publishes exact criteria, identities, determinant representations, killed shortcuts, and the final residual theorem without presenting them as an RH proof.

## Terminal object

Let

\[
G(z)=\sum_{k\ge0}a_kz^k
=\frac18\,\xi\!\left(\frac12+\frac{\sqrt z}{2}\right),
\]

with positive moment coefficients

\[
a_k=\frac1{(2k)!}\int_0^\infty u^{2k}\Phi(u)\,du,
\qquad \Phi(u)>0.
\]

The campaign focuses on consecutive Toeplitz determinants

\[
D_{r,k}=\det[a_{k+j-i}]_{i,j=0}^{r-1},
\qquad a_\ell=0\ (\ell<0).
\]

The certified tail available to the campaign does **not** by itself reach the RH-critical regime, and no Court-valid path in the packet proves `D_{r,k}>0` for every `r,k`.

## Banked theorem/negative-theorem inventory recovered from the estate atlas

### A — Real-rooted approximants + local uniform convergence
**Status:** exact sufficient lemma; construction with both properties remains open.

If entire functions `Xi_N` have only real zeros and converge locally uniformly to `Xi`, then the standard Hurwitz/Rouché/Laguerre–Pólya closure mechanism yields RH. The campaign did not construct the required approximants.

### R2-C — weighted transformed-zero moment criterion
**Status:** `BANKED`

The recovered ledger records an equivalence between RH and a uniform bound, by the reference constant `M0`, on an absolutely convergent family of weighted transformed-zero moments.

### R2-D — Toeplitz PSD hierarchy
**Status:** `BANKED`

The recovered ledger records a Toeplitz positive-semidefinite hierarchy built from the transformed weighted moments as an equivalent RH criterion.

### R3-A — quadratic variable / genus-zero transform
**Status:** `BANKED`

The campaign uses

\[
\xi(s)=F(s(1-s)),
\]

with the transformed entire function `F` of order `1/2` and genus zero.

### R3-D — logarithmic-derivative coordinate
**Status:** `BANKED`

For the campaign's real coordinate `x` and corresponding `sigma>1`, it records

\[
h(x)=\frac{\xi'(\sigma)}{(2\sigma-1)\xi(\sigma)}.
\]

### R6-G — adjacent heat-flow gap evolution
**Status:** `BANKED`

An exact adjacent-gap evolution identity was banked for the heat-flow deformation used by the campaign.

### R7-V — critical-value inverse-square energy identity
**Status:** `BANKED`

The logarithmic derivative at a critical value is represented by an inverse-square zero-energy sum.

### R8-A — monotonic transformed-gap ratio
**Status:** `BANKED`

The recovered ledger records strict increase of the ratio

\[
R_j=|H_t(c_j)|/g_j^2
\]

while the adjacent zeros remain real and distinct.

### T10-1 — positive-atom representation
**Status:** `BANKED`

\[
G(z)=\int_0^\infty \Phi(u)\cosh(u\sqrt z)\,du.
\]

For fixed `u`, the coefficient sequence of the `cosh` atom is PF-infinity. A central negative result of the campaign is that **positive mixtures of those atoms need not preserve even PF2**, so atomwise total positivity does not prove RH.

### T10-3 — exact determinant lift
**Status:** `BANKED`

With

\[
b_n(u)=\begin{cases}u^{2n}/(2n)!,&n\ge0,\\0,&n<0,\end{cases}
\]

the campaign derives the exact positive-measure lift

\[
D_{r,k}
=\int_{(0,\infty)^r}
\det[b_{k+j-i}(u_i)]_{i,j=0}^{r-1}
\prod_{i=0}^{r-1}\Phi(u_i)\,du_i.
\]

The outer measure is positive. The inner determinant, however, is not pointwise nonnegative in general.

### Natural determinant-integrand positivity fails already at `r=2`
**Status:** killed route / exact sign obstruction

For `r=2`, symmetrizing the row-assignment kernel gives

\[
\mathcal S_{2,k}(u,v)=
\frac{u^{2k-2}v^{2k-2}}{((2k)!)^2}
\left[u^2v^2-\frac{c_k}{2}(u^4+v^4)\right],
\]

where

\[
c_k=\frac{(2k)(2k-1)}{(2k+1)(2k+2)}\in(0,1).
\]

For fixed `v>0` and `u/v -> infinity`, the bracket is negative. Thus the direct Andréief/Vandermonde-style pointwise-positivity shortcut fails already at order two. This does not rule out other multiple-integral mechanisms.

### Rectangular Schur identification

Setting `h_n=a_n` and `h_n=0` for `n<0`, Jacobi–Trudi gives

\[
D_{r,k}=s_{(k^r)}\big|_{h_n=a_n}.
\]

Thus the consecutive observables are rectangular Schur values of the Riemann specialization.

### T10-8 — exact tilted-measure coordinate
**Status:** `BANKED`

Define

\[
m_{2k}=\int_0^\infty u^{2k}\Phi(u)\,du,
\qquad
d\nu_k(u)=\frac{u^{2k}\Phi(u)}{m_{2k}}\,du,
\]

and for `U~nu_k`, let `X_k=2 log U`. Then for integer `s>=-k`,

\[
\frac{a_{k+s}}{a_k}
=
\frac{\Gamma(2k+1)}{\Gamma(2k+2s+1)}
\mathbb E_{\nu_k}[e^{sX_k}].
\]

Consequently

\[
\frac{D_{r,k}}{a_k^r}
=
\det_{0\le i,j<r}
\left[
\frac{\Gamma(2k+1)}{\Gamma(2k+2(j-i)+1)}
\mathbb E_{\nu_k}(e^{(j-i)X_k})
\right].
\]

Writing `K_k(s)=log E[e^{sX_k}]` exposes every matrix entry as a gamma-factor correction plus the **full** cumulant-generating function.

## The scale diagnosis

The campaign's earlier cubic-wedge control is a **local** cumulant/CLT regime: when `r^3/k << 1`, only small `s/k` is sampled and a quadratic local model can dominate.

When `k = alpha r` with `alpha=O(1)`, however, `|s|=O(r)=O(k)`. The determinant samples the moment-generating function at **macroscopic tilt**. A finite Taylor/cumulant truncation around zero cannot be the primary model.

The terminal missing object is therefore a ratio-uniform, nonperturbative large-deviation description of `X_k`.

## Terminal target: compactified-ratio collective-saddle positivity

Set

\[
\theta=\frac{k}{k+r}\in[0,1).
\]

The campaign's explicit terminal target is to find positive normalizations `N_{r,k}`, a positive function `F(theta)`, and errors `epsilon_{r,k}` such that

\[
N_{r,k}D_{r,k}
=F\!\left(\frac{k}{k+r}\right)(1+\varepsilon_{r,k}),
\]

with

\[
\sup_{k\ge0}|\varepsilon_{r,k}|\to0
\qquad(r\to\infty).
\]

That would give determinant positivity for all sufficiently large **orders**, uniformly in the shift. It would still leave a second gate: for every remaining finite order, one needs either an effective all-shift tail cutoff plus finite core verification, or a fixed-order strictification theorem. Only after that additional gate could the determinant program close RH.

## Killed routes retained publicly

The atlas records the following negative results as killed rather than silently forgotten:

- `R1-X`: unjustified positive rank-one decomposition of the prime side;
- `R4-X`: crude archimedean domination of the prime kernel;
- `R5-X`: atomwise complete monotonicity / literal prime SOS;
- `R6-X`: generic derivative-to-function hyperbolicity propagation;
- `R9-X`: condensation alone propagates tail positivity inward.

The ten-round terminal chain is therefore:

\[
\text{RH coefficient problem}
\to
\text{rectangular Schur/Toeplitz determinants}
\to
\text{positive PF}_\infty\text{-atom mixture}
\to
\text{collective scale-mixing obstruction}
\to
\text{ratio-uniform large-deviation determinant}.
\]

That is a strict reduction and obstruction map, **not an RH proof**.