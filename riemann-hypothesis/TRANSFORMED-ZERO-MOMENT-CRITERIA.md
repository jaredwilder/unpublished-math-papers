# Three transformed-zero / moment criteria for the Riemann Hypothesis

**Author of this extraction:** Jared Wilder  
**Recovered from:** RH Terminal Encirclement, Rounds 2–3  
**Novelty claim:** none; these are banked equivalent coordinates assembled from classical zero-transform and moment theory.

This note publishes the exact formulas that were only named in the earlier public asset summary.

---

## 1. Reciprocal-spectrum transform

For a nontrivial zero `rho`, define

\[
\boxed{
z_\rho=\frac{\rho-1}{\rho}=1-\frac1\rho.
}
\]

Then

\[
|z_\rho|^2
=
\frac{(\Re\rho-1)^2+(\Im\rho)^2}
{(\Re\rho)^2+(\Im\rho)^2}.
\]

Therefore

\[
\boxed{
\Re\rho=\frac12
\iff
|z_\rho|=1.
}
\]

The functional-equation symmetries become

\[
\boxed{
z_{1-\rho}=z_\rho^{-1},
\qquad
z_{\bar\rho}=\overline{z_\rho}.
}
\]

The symmetric coordinate is

\[
\boxed{
z_\rho+z_\rho^{-1}
=2-\frac1{\rho(1-\rho)}.
}
\]

---

## 2. Absolutely convergent weighted power moments

Define positive weights

\[
w_\rho=\frac1{|\rho(1-\rho)|^2}
\]

and, for integer `n`,

\[
M_n=\sum_\rho w_\rho z_\rho^n.
\]

For each fixed `n`, the packet records absolute convergence.

Under RH, every transformed zero lies on the unit circle, so immediately

\[
|M_n|
\le
\sum_\rho w_\rho
=M_0.
\]

Conversely, if RH fails, the transformed moduli include values larger than one. Since

\[
|z_\rho|\to1
\]

as zero height tends to infinity, the maximal modulus

\[
R=\max_\rho |z_\rho|>1
\]

is attained among bounded-height zeros. After division by `R^n`, the contribution of the finitely many extremal transformed zeros is a nonzero finite exponential sum in `n`; its limsup is nonzero. Hence `|M_n|` has exponentially large subsequences and eventually violates the uniform `M_0` bound.

Thus the packet obtains the criterion

\[
\boxed{
\mathrm{RH}
\iff
|M_n|\le M_0
\quad\text{for every }n\ge1.
}
\]

### Toeplitz PSD form

Let

\[
T_N=(M_{j-k})_{j,k=0}^{N}.
\]

Under RH, with `|z_rho|=1`,

\[
M_{j-k}
=
\sum_\rho w_\rho z_\rho^j\overline{z_\rho^k},
\]

so `T_N` is a Gram matrix and therefore positive semidefinite.

If `|M_n|>M_0`, the principal `2x2` block

\[
\begin{pmatrix}
M_0&M_n\\
M_{-n}&M_0
\end{pmatrix}
\]

has negative determinant.

Hence

\[
\boxed{
\mathrm{RH}
\iff
T_N\succeq0
\quad\text{for every }N.
}
\]

---

## 3. Quotient by the functional equation

Set

\[
t=s(1-s).
\]

Since

\[
\xi(s)=\xi(1-s),
\]

there is an entire function `F` such that

\[
\boxed{
\xi(s)=F(s(1-s)).
}
\]

The order drops from one to one half, hence `F` is genus zero.

For a nontrivial zero `rho`, put

\[
\tau_\rho=\rho(1-\rho).
\]

Using the absence of nontrivial real zeta zeros in `0<s<1`, the critical-line condition becomes

\[
\boxed{
\mathrm{RH}
\iff
\text{every zero of }F\text{ is positive real}.
}
\]

---

## 4. Genus-zero power sums

The logarithmic derivative is

\[
-\frac{F'(t)}{F(t)}
=
\sum_k\frac1{\tau_k-t}.
\]

Near `t=0`,

\[
-\frac{F'(t)}{F(t)}
=
\sum_{n\ge0}m_nt^n,
\]

where

\[
\boxed{
m_n=\sum_k\tau_k^{-(n+1)}.
}
\]

If all `tau_k` are positive real, this is the moment sequence of the positive atomic measure supported at `1/tau_k`, with corresponding positive masses.

Conversely, the packet uses the classical Stieltjes moment theorem together with the determinacy/analytic-continuation information supplied by the bounded exponential growth of these moments to recover positivity of the transformed zero support.

Thus

\[
\boxed{
\mathrm{RH}
\iff
(m_n)_{n\ge0}
\text{ is a Stieltjes moment sequence}.
}
\]

By the classical Stieltjes criterion this is equivalent to

\[
\boxed{
H_N^{(0)}=(m_{i+j})_{i,j=0}^{N}\succeq0,
\qquad
H_N^{(1)}=(m_{i+j+1})_{i,j=0}^{N}\succeq0
\quad\forall N.
}
\]

---

## 5. Arithmetic coordinate on the half-plane `sigma>1`

For `x>0`, define

\[
\sigma(x)=\frac{1+\sqrt{1+4x}}2,
\]

so that

\[
\sigma(1-\sigma)=-x.
\]

Then

\[
\boxed{
h(x):=-\frac{F'(-x)}{F(-x)}
=
\frac1{2\sigma-1}\frac{\xi'(\sigma)}{\xi(\sigma)}.
}
\]

Because `sigma>1`, the prime-series representation of `xi'/xi` is absolutely convergent in this coordinate.

This gives a direct arithmetic representation of the transformed Stieltjes/logarithmic-derivative object on the positive `x` axis.

---

## Relation between the criteria

The two transforms expose the same zero geometry in different ways:

- `z_rho=(rho-1)/rho` converts the critical line into the unit circle and produces a Toeplitz/Gram criterion;
- `tau_rho=rho(1-rho)` quotients the functional equation, converts RH into positivity of a genus-zero zero set, and produces a Stieltjes/Hankel criterion.

They are banked equivalent coordinates, not separate proof claims of RH.
