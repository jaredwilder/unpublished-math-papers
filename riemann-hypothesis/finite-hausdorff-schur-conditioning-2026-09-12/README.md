# Finite Hausdorff-to-Schur conditioning through separated spectral atoms

**Author:** Jared Wilder  
**Date:** 2026-09-12  
**Status:** exact finite-spectrum stability theorem; **not an RH proof**  
**Novelty:** Prony/Vandermonde moment inversion and its collision conditioning are classical. The exact composition from the Hausdorff boundary row through the Xi Möbius coordinate into rectangular-Schur determinant distortion is new to this research estate; historical priority is **unverified**.

## 1. Why this theorem exists

The finite-spectrum reconstruction theorem says that, for a known `m`-atom spectrum, the first `m` values of the Hausdorff boundary row determine the entire polynomial and hence the whole consecutive Toeplitz determinant lattice.

That theorem is qualitative.

The present theorem asks the quantitative question that matters for any attempt to pass from finite data to an infinite spectral cloud:

> If the first `m` Hausdorff values are perturbed by a certified amount, how much can a rectangular Schur / Toeplitz determinant move?

The answer is explicit. The price is governed by the inverse Vandermonde conditioning of the spectral atoms, hence by a power of their minimum separation.

---

## 2. Setup

Let

\[
0<y_1<\cdots<y_m<1
\]

be a finite spectral cloud. Define

\[
\alpha_j=\frac{y_j}{1-y_j}>0.
\tag{1}
\]

For `s=1,...,m`, let

\[
p_s=\sum_{j=1}^m y_j^s.
\tag{2}
\]

In the Hausdorff coordinate used in the Xi program,

\[
\boxed{
p_s=\frac14 H_{s-1,0}.}
\tag{3}
\]

For a rectangle `(r^k)` with `1<=k<=m`, define

\[
S_{r,k}(y):=s_{(r^k)}(\alpha_1,\ldots,\alpha_m).
\tag{4}
\]

If

\[
G(z)=a_0\prod_{j=1}^m(1+\alpha_j z),
\]

then the corresponding consecutive Toeplitz minor is

\[
D_{r,k}=a_0^r S_{r,k}.
\tag{5}
\]

---

## 3. The separated-interior region

Fix

\[
0<\eta<\frac14,
\qquad
\Delta>0.
\]

Call a cloud **safe** when

\[
\eta\le y_j\le1-\eta
\]

and

\[
|y_i-y_j|\ge\Delta
\qquad(i\ne j).
\tag{6}
\]

Define the explicit inverse-Vandermonde constant

\[
\boxed{
C_{m}(\eta,\Delta)
:=
\frac{(2-\eta)^{m-1}}{\Delta^{m-1}}.
}
\tag{7}
\]

The exponent `m-1` is the important feature: reconstruction becomes badly conditioned when atoms collide.

---

## 4. Pathwise theorem

Let `y(t)=(y_1(t),...,y_m(t))`, `0<=t<=1`, be a `C^1` path of safe clouds. Let

\[
p_s(t)=\sum_j y_j(t)^s.
\]

Then

\[
\boxed{
\max_j |\dot y_j(t)|
\le
C_m(\eta,\Delta)
\max_{1\le s\le m}|\dot p_s(t)|.
}
\tag{8}
\]

Consequently,

\[
\boxed{
\left|
\frac{d}{dt}\log S_{r,k}(y(t))
\right|
\le
\frac{rk\,C_m(\eta,\Delta)}
{\eta(1-\eta)}
\max_{1\le s\le m}|\dot p_s(t)|.
}
\tag{9}
\]

Using (3), this is equivalently

\[
\boxed{
\left|
\frac{d}{dt}\log S_{r,k}(y(t))
\right|
\le
\frac{rk\,C_m(\eta,\Delta)}
{4\eta(1-\eta)}
\max_{0\le n<m}|\dot H_{n,0}(t)|.
}
\tag{10}
\]

### Interpretation

A certified perturbation in the first `m` Hausdorff boundary values produces a certified multiplicative perturbation of **every** rectangular Schur determinant with `k<=m`.

The transfer cost is explicit:

\[
\text{Hausdorff error}
\times
\underbrace{\Delta^{-(m-1)}}_{\text{moment inversion}}
\times
\underbrace{\frac1{\eta(1-\eta)}}_{\text{Möbius map}}
\times
\underbrace{rk}_{\text{Schur sensitivity}}.
\]

---

## 5. Proof of the spectral-motion bound

The Jacobian of the power-sum map is

\[
J_{s,j}
=
\frac{\partial p_s}{\partial y_j}
=
s y_j^{s-1},
\qquad
1\le s,j\le m.
\tag{11}
\]

Write

\[
J=DV,
\]

where

\[
D=\operatorname{diag}(1,2,\ldots,m)
\]

and

\[
V_{s,j}=y_j^{s-1}.
\]

Thus

\[
\dot y=V^{-1}D^{-1}\dot p.
\tag{12}
\]

The `j`th row of `V^{-1}` is the coefficient vector of the Lagrange polynomial

\[
L_j(x)
=
\prod_{\ell\ne j}
\frac{x-y_\ell}{y_j-y_\ell}.
\tag{13}
\]

Its coefficient `ell^1` norm is bounded by

\[
\|L_j\|_{\ell^1}
\le
\frac{\prod_{\ell\ne j}(1+|y_\ell|)}
{\prod_{\ell\ne j}|y_j-y_\ell|}.
\]

On the safe region,

\[
1+|y_\ell|\le2-\eta,
\qquad
|y_j-y_\ell|\ge\Delta.
\]

Therefore

\[
\|V^{-1}\|_{\infty}
\le
\frac{(2-\eta)^{m-1}}
{\Delta^{m-1}}
=C_m(\eta,\Delta).
\tag{14}
\]

Since every diagonal entry of `D^{-1}` is at most one, (12) gives (8).

---

## 6. Proof of the Schur bound

From

\[
\alpha_j=\frac{y_j}{1-y_j}
\]

one has

\[
\frac{d}{dt}\log\alpha_j
=
\frac{\dot y_j}{y_j(1-y_j)}.
\tag{15}
\]

Hence, on the safe region,

\[
\left|
\frac{d}{dt}\log\alpha_j
\right|
\le
\frac{|\dot y_j|}{\eta(1-\eta)}.
\tag{16}
\]

For the rectangular Schur polynomial define its logarithmic occupancies

\[
q_j
:=
\alpha_j\,\partial_{\alpha_j}
\log s_{(r^k)}(\alpha).
\tag{17}
\]

The semistandard-tableau expansion gives

\[
0\le q_j\le r
\]

and homogeneity gives

\[
\boxed{
\sum_{j=1}^m q_j=rk.
}
\tag{18}
\]

Therefore

\[
\begin{aligned}
\left|\frac d{dt}\log S_{r,k}\right|
&=
\left|\sum_j q_j\frac d{dt}\log\alpha_j\right|\\
&\le
rk\max_j\left|\frac d{dt}\log\alpha_j\right|.
\end{aligned}
\]

Combining (8), (16), and (18) proves (9), and (3) gives (10).

---

## 7. Endpoint theorem with an explicit bootstrap

The path hypothesis above can be generated from sufficiently close endpoint moment data.

Let the initial cloud satisfy the stronger conditions

\[
2\eta\le y_j^{(0)}\le1-2\eta,
\qquad
|y_i^{(0)}-y_j^{(0)}|\ge2\Delta.
\tag{19}
\]

Let a second real `m`-atom cloud have power sums `p_s^(1)`, and put

\[
\varepsilon
:=
\max_{1\le s\le m}
|p_s^{(1)}-p_s^{(0)}|.
\tag{20}
\]

If

\[
\boxed{
C_m(\eta,\Delta)\,\varepsilon
<
\min\!\left(\eta,\frac\Delta2\right),
}
\tag{21}
\]

then the local inverse branch of the power-sum map along the straight moment path

\[
p(t)=(1-t)p^{(0)}+tp^{(1)}
\]

cannot reach the boundary of the safe region. It therefore continues to `t=1`; Newton/Vieta uniqueness identifies its endpoint with the second cloud up to permutation.

Integrating (9) gives

\[
\boxed{
\left|
\log\frac{S_{r,k}^{(1)}}{S_{r,k}^{(0)}}
\right|
\le
\frac{rk\,C_m(\eta,\Delta)}
{\eta(1-\eta)}
\varepsilon.
}
\tag{22}
\]

In Hausdorff coordinates,

\[
\varepsilon
=
\frac14
\max_{0\le n<m}
|H_{n,0}^{(1)}-H_{n,0}^{(0)}|,
\]

so

\[
\boxed{
\left|
\log\frac{S_{r,k}^{(1)}}{S_{r,k}^{(0)}}
\right|
\le
\frac{rk(2-\eta)^{m-1}}
{4\eta(1-\eta)\Delta^{m-1}}
\max_{0\le n<m}
|H_{n,0}^{(1)}-H_{n,0}^{(0)}|.
}
\tag{23}
\]

For the actual consecutive minors,

\[
D_{r,k}=a_0^rS_{r,k},
\]

so the normalized determinant obeys exactly (23):

\[
\boxed{
\left|
\log
\frac{D_{r,k}^{(1)}/(a_0^{(1)})^r}
{D_{r,k}^{(0)}/(a_0^{(0)})^r}
\right|
\le
\frac{rk(2-\eta)^{m-1}}
{4\eta(1-\eta)\Delta^{m-1}}
\max_{0\le n<m}
|\Delta H_{n,0}|.
}
\tag{24}
\]

If the two systems have the same `a_0`, (24) is directly a bound on `D_(r,k)^(1)/D_(r,k)^(0)`. Otherwise add

\[
r\left|\log\frac{a_0^{(1)}}{a_0^{(0)}}\right|
\]

to the right-hand side for the unnormalized determinants.

---

## 8. What the theorem says about the infinite RH problem

This finite theorem does **not** solve tail-controlled reconstruction. It tells us what that missing theorem must beat.

Even before the infinite tail is considered, finite moment inversion pays a crowding factor of order

\[
\Delta^{-(m-1)}.
\]

Thus a reconstruction strategy that keeps increasing `m` without exploiting additional zeta-specific structure can become exponentially ill-conditioned in the number of resolved atoms.

That gives a quantitative version of the qualitative scheduling law already visible in the estate:

> **More moments are not automatically more proof. Their value depends on whether the residual spectral cloud can be controlled without paying catastrophic separation conditioning.**

The right infinite theorem should therefore use known asymptotic zero geometry / tail structure, rather than treating the high spectrum as an arbitrary finite Prony system of ever-increasing size.

---

## 9. Prior-art boundary

Classical moment inversion / Prony theory already studies exactly the instability caused by colliding nodes. In particular, work of Batenkov and Yomdin on the geometry and singularities of the Prony mapping makes the collision singularity and Vandermonde conditioning explicit. None of that is claimed as estate novelty.

Likewise, Newton identities, Lagrange interpolation, the Möbius map `alpha=y/(1-y)`, and standard Schur homogeneity/tableau facts are individually classical.

The object recorded here is the **composition**

\[
\boxed{
\text{Hausdorff boundary-row error}
\to
\text{power-sum node motion}
\to
\text{Xi Möbius spectral motion}
\to
\text{rectangular-Schur determinant distortion}.
}
\]

A targeted search did not locate this exact stability theorem. That is not proof of historical novelty. Priority remains **unverified**.

Relevant classical references include:

- D. Batenkov and Y. Yomdin, *Geometry and Singularities of the Prony Mapping*, Journal of Singularities 10 (2014), 1–25, arXiv:1301.1336.
- D. Batenkov and Y. Yomdin, *Local and global geometry of Prony systems and Fourier reconstruction of piecewise-smooth functions*, arXiv:1301.1187.

---

## 10. What is not claimed

This note does **not** claim:

- RH;
- a stable inversion theorem for an infinite spectral cloud;
- a uniform bound as `m->infinity`;
- that the explicit constant is sharp;
- that the straight moment path remains realizable without the smallness/bootstrap condition;
- settled literature priority.

It supplies the finite quantitative transfer law that the earlier exact reconstruction theorem lacked, and makes the spectral-crowding obstruction explicit.