# Hausdorff–Schur Möbius bridge for the Riemann Xi spectrum

**Author:** Jared Wilder  
**Date:** 2026-09-12  
**Status:** exact structural synthesis / negative design law; **not an RH proof**  
**Novelty:** general Hausdorff-moment criteria for RH are prior art; novelty of the exact cross-coordinate synthesis and filter-sensitivity packaging is **unverified**

## 1. Scope

This note joins two exact coordinate systems that arose separately in the research estate:

1. the folded-zero / Hausdorff-moment coordinate based on
   \[
   \tau_\rho=\rho(1-\rho),
   \]
2. the Pólya-frequency / Schur coordinate for
   \[
   G(z)=\frac18\,\xi\!\left(\frac12+\frac{\sqrt z}{2}\right)
   =a_0\prod_j(1+\alpha_j z).
   \]

They are not merely analogous. Their spectral atoms are related by an exact fractional-linear map.

The resulting bridge turns the folded-zero moment family into a Beta-shaped two-index lattice written directly in the same `alpha` parameters that control the rectangular Schur determinants. It also exposes an exact localization-versus-angular-sensitivity tradeoff.

## 2. Exact Möbius bridge

Put

\[
u_\rho=\left(\rho-\frac12\right)^2.
\]

Then

\[
\tau_\rho=\rho(1-\rho)=\frac14-u_\rho.
\]

A zero `rho` of `xi` gives the zero

\[
z_\rho=4u_\rho
\]

of `G`. Since a zero of

\[
G(z)=a_0\prod_j(1+\alpha_j z)
\]

occurs at `z=-1/alpha`,

\[
\alpha_\rho=-\frac1{4u_\rho}.
\]

Substitution into `tau=1/4-u` gives

\[
\boxed{
\tau_\rho=\frac{1+\alpha_\rho}{4\alpha_\rho}
}
\]

and therefore

\[
\boxed{
\frac1{4\tau_\rho}
=\frac{\alpha_\rho}{1+\alpha_\rho}.
}
\tag{1}
\]

Write

\[
y_\rho:=\frac1{4\tau_\rho}.
\]

Then

\[
\boxed{y=\frac{\alpha}{1+\alpha}},
\qquad
\boxed{\alpha=\frac{y}{1-y}}.
\tag{2}
\]

On RH, `alpha>0`, equivalently `0<y<1`.

Thus the folded-zero moment coordinate and the Schur/PF coordinate are the same spectral data in two Möbius-related coordinates.

## 3. Hausdorff–Beta lattice in the Schur spectral variables

Let

\[
m_n=\sum_j\tau_j^{-(n+1)},
\qquad
b_n=\frac{m_n}{4^n}.
\]

Under RH, (1) gives

\[
b_n
=4\sum_j y_j^{n+1}.
\]

Equivalently, with the finite positive measure

\[
\mu=4\sum_j y_j\,\delta_{y_j},
\]

one has

\[
b_n=\int_0^1 y^n\,d\mu(y).
\]

Define the Hausdorff finite-difference lattice

\[
H_{n,q}:=(-1)^q\Delta^q b_n.
\]

Then

\[
\boxed{
H_{n,q}
=4\sum_j y_j^{n+1}(1-y_j)^q
}
\tag{3}
\]

and, using (2),

\[
\boxed{
H_{n,q}
=4\sum_j
\frac{\alpha_j^{n+1}}
{(1+\alpha_j)^{n+q+1}}.
}
\tag{4}
\]

So the linear Hausdorff lattice is written in **exactly the same `alpha_j` variables** as the rectangular Schur determinant

\[
D_{r,k}=a_0^r s_{(r^k)}(\alpha).
\]

The finite-difference identity also gives the exact positive splitting law

\[
\boxed{
H_{n,q}=H_{n+1,q}+H_{n,q+1}.
}
\tag{5}
\]

Thus the same Xi spectral atoms support both:

- a **linear** Pascal-type Hausdorff lattice `H_(n,q)`;
- a **nonlinear** determinant/Schur lattice `D_(r,k)`.

## 4. Prior-art boundary for the Hausdorff criterion

The statement “RH admits a Hausdorff moment / finite-difference criterion” is **not claimed as new here**.

Ruiming Zhang, *An Application of Hausdorff Moment Problem*, arXiv:2303.09396 (2023), develops Hausdorff finite-difference conditions for genus-zero entire functions and applies them to RH/GRH. Related secondary-zeta moment/Hankel formulations also appear in the 2026 literature.

The contribution recorded here is narrower:

- the exact Xi-specific Möbius identification (1) between the folded-zero and PF/Schur spectral coordinates;
- the resulting expression (4) of the Hausdorff lattice in the Schur variables;
- the exact filter-sensitivity identity below;
- the research consequence that radial localization and first-order angular sensitivity conflict for a single centered filter.

No literature-priority claim is made for that package pending a deeper dedicated search.

## 5. A single Hausdorff atom is a Beta-shaped spectral filter

For one positive spectral parameter `alpha`, define

\[
K_{n,q}(\alpha)
:=4\frac{\alpha^{n+1}}
{(1+\alpha)^{n+q+1}}.
\tag{6}
\]

Equivalently, in `y=alpha/(1+alpha)`,

\[
K_{n,q}=4y^{n+1}(1-y)^q.
\]

For `q>0`, the positive-axis maximum occurs at

\[
\boxed{
\alpha_*=\frac{n+1}{q}
}
\tag{7}
\]

or equivalently

\[
y_*=\frac{n+1}{n+q+1}.
\]

Hence `(n,q)` tunes a spectral window.

## 6. Exact localization / angular-blindness identity

Rotate the atom slightly off the positive axis:

\[
\alpha=a e^{i\theta},\qquad a>0.
\]

From (6),

\[
\log K
=\log4+(n+1)\log\alpha
-(n+q+1)\log(1+\alpha).
\]

Let `Phi(theta)=arg K_(n,q)(a e^{i theta})`. Direct differentiation at `theta=0` gives

\[
\boxed{
\Phi'(0)
=\frac{n+1-qa}{1+a}.
}
\tag{8}
\]

But the positive-axis radial logarithmic derivative is exactly the same quantity:

\[
\boxed{
\frac{\partial}{\partial\log a}
\log K_{n,q}(a)
=\frac{n+1-qa}{1+a}.
}
\tag{9}
\]

Therefore

\[
\boxed{
\left.\frac{\partial}{\partial\theta}\arg K_{n,q}(ae^{i\theta})\right|_{\theta=0}
=
\frac{\partial}{\partial\log a}\log K_{n,q}(a).
}
\tag{10}
\]

At the radial saddle `a=(n+1)/q`, both sides vanish:

\[
\boxed{
\Phi'(0)=0.
}
\tag{11}
\]

### Consequence

> **The single Hausdorff/Beta filter optimally centered on a spectral radius is first-order insensitive to an infinitesimal angular defect at exactly that radius.**

This is an exact local statement, not a numerical observation.

It does **not** invalidate the global Hausdorff criterion. It says that the most obvious single-filter localization strategy has a built-in first-order blindness to precisely the off-axis perturbation one wants to detect.

## 7. Research interpretation

The estate now has two exact views of the same spectral atoms:

\[
\text{Hausdorff/Beta filters}
\quad\longleftrightarrow\quad
\alpha_j
\quad\longleftrightarrow\quad
\text{rectangular Schur determinants}.
\]

This matters because the two views have different sensitivity geometry.

The Hausdorff lattice is linear and radially tunable. The Schur determinant hierarchy carries collective phase/sign information. Formula (11) shows why “center the scalar filter perfectly on the suspected spectral scale” is not automatically the best detector for an off-axis zero.

A future cross-route theorem should therefore use the two coordinates as complements rather than expecting either finite scalar localization or bulk determinant free energy alone to expose every possible RH violation.

## 8. What is not claimed

This note does **not** claim:

- a proof of RH;
- a new Hausdorff criterion for RH;
- positivity of `H_(n,q)` without RH;
- positivity of all Schur/Toeplitz minors;
- a complete detector for off-axis zeros;
- settled literature novelty for the Möbius-bridge / sensitivity synthesis.

It records exact algebra that was previously split across separate branches of the research estate, plus an exact local sensitivity obstruction that follows once those branches are joined.
