# RH Encirclement II–V — recovered exact mathematics

**Author:** Jared Wilder  
**Original campaign date:** 2026-08-11  
**Recovered from session export:** 2026-09-11

This directory publishes the exact theorem spine of four RH campaigns that were present in the session archive but were not yet exposed as a coherent public mathematical packet.

The campaigns are best read as one progression:

1. **Encirclement II:** discover an exact rational orbit for the nonlinear determinant-odds lattice.
2. **Encirclement III:** normalize against a positive comparison determinant array and obtain an exact discrete comparison principle plus a boundary-homotopy positivity theorem.
3. **Encirclement IV:** use the de Bruijn–Newman flow as the canonical homotopy, derive an exact adaptive harmonic equation for homotopy velocity, prove a no-bounded-first-nucleation theorem, and obtain exact primal/dual Jacobi–Trudi coordinates.
4. **Encirclement V:** identify the bilinear harmonic blind mode, convert positive-phase determinants into rectangular Schur polynomials, prove an occupancy cap, and derive sparse angular phase criteria and a quantitative determinant-order detection delay.

The corresponding verifier packets report **7/7, 5/5, 6/6, and 6/6** successful algebraic/combinatorial checks respectively. Those verifiers check the displayed identities and finite symbolic claims; they are not substitutes for the analytic terminal lemmas that remain outside the exact core.

---

## I. Exact rational odds orbit

For consecutive Toeplitz minors

\[
D_{r,k}=\det[a_{k+j-i}]_{i,j=0}^{r-1},
\]

define

\[
R_{r,k}=\frac{D_{r,k-1}D_{r,k+1}}{D_{r,k}^2},\qquad
A_{r,k}=\frac{D_{r-1,k}D_{r+1,k}}{D_{r,k}^2},
\]

and the odds variable

\[
Y_{r,k}=\frac{A_{r,k}}{R_{r,k}}.
\]

Desnanot–Jacobi gives

\[
R_{r,k}+A_{r,k}=1.
\]

The induced exact odds recurrence is

\[
1+Y_{r+1,k}
=
\frac{Y_{r,k}^2}{1+Y_{r-1,k}}
\frac{(1+Y_{r,k-1})(1+Y_{r,k+1})}
{Y_{r,k-1}Y_{r,k+1}}.
\]

### Rational-orbit theorem

For constants \(\mu,\nu\) wherever the displayed terms are defined,

\[
\boxed{Y^{\mu,\nu}_{r,k}=\frac{r+\mu}{k+\nu}}
\]

satisfies this recurrence exactly.

The one-sided Toeplitz boundary selects the factorial member

\[
\boxed{Y^*_{r,k}=\frac rk}.
\]

This single orbit spans the cubic, quadratic and fixed-slope scaling regimes:

\[
k\asymp r^3\Rightarrow Y^*\asymp r^{-2},\qquad
k\asymp r^2\Rightarrow Y^*\asymp r^{-1},\qquad
k\asymp r\Rightarrow Y^*=O(1).
\]

For the factorial benchmark,

\[
\boxed{D^{(0)}_{r,k}=\prod_{j=0}^{r-1}\frac{j!}{(k+j)!}}.
\]

---

## II. Exact nonlinear comparison equation

Let \(B_{r,k}>0\) be any positive comparison determinant array satisfying the same Desnanot identity and set

\[
U_{r,k}=\log\frac{D_{r,k}}{B_{r,k}}.
\]

Then exactly

\[
\boxed{
R^B_{r,k}e^{\Delta_k^2U_{r,k}}
+
A^B_{r,k}e^{\Delta_r^2U_{r,k}}
=1.
}
\]

For the factorial benchmark this becomes

\[
\boxed{
k e^{\Delta_k^2U}+r e^{\Delta_r^2U}=k+r.
}
\]

### Discrete comparison principle

If \(U,V\) solve the same normalized equation in a finite lattice domain, then

\[
\boxed{
\max_\Omega(U-V)\le \max_{\partial\Omega}(U-V),\qquad
\min_\Omega(U-V)\ge \min_{\partial\Omega}(U-V).
}
\]

The proof is the direct strict-monotonicity argument at an interior extremum.

### Boundary-homotopy positivity theorem

Let \(a_k(t)>0\), \(0\le t\le1\), be a continuous coefficient homotopy with consecutive minors \(D_{r,k}(t)\). On any finite lattice domain \(\Omega\), assume:

1. all minors are positive at the starting time;
2. boundary minors remain positive throughout the homotopy;
3. the comparison array is positive.

Then

\[
\boxed{D_{r,k}(t)>0\text{ throughout }\Omega\text{ for every }t\in[0,1].}
\]

A first interior zero would force \(U=\log(D/B)\to-\infty\), contradicting the finite-domain minimum principle with positive boundary data.

---

## III. Dynamic ellipticity along the de Bruijn–Newman flow

For

\[
\mathcal G_t(z)=\sum_{k\ge0}a_k(t)z^k
\]

under the de Bruijn–Newman heat deformation, the coefficients satisfy

\[
\partial_t a_k=(2k+2)(2k+1)a_{k+1},
\]

and

\[
\partial_t\mathcal G_t=4z\partial_z^2\mathcal G_t+2\partial_z\mathcal G_t.
\]

For

\[
U_{r,k}(t)=\log\frac{D_{r,k}(t)}{B_{r,k}},\qquad
V_{r,k}=\partial_tU_{r,k},
\]

differentiating the exact normalized determinant equation gives

\[
\boxed{
R^D_{r,k}\Delta_k^2V_{r,k}
+
A^D_{r,k}\Delta_r^2V_{r,k}=0.
}
\]

Thus the homotopy velocity is exactly discrete harmonic in the adaptive determinant metric while the neighboring minors remain positive.

Differentiating again, with \(W=\partial_t^2U\), gives

\[
\boxed{
R^D\Delta_k^2W+A^D\Delta_r^2W
=-R^D(\Delta_k^2V)^2-A^D(\Delta_r^2V)^2\le0.
}
\]

So the second time derivative is superharmonic with an explicit nonpositive quadratic source.

### No bounded first nucleation

Combine the finite-domain homotopy theorem with positive boundary data along the heat flow. A first loss of consecutive-minor positivity cannot occur at a bounded lattice point while the surrounding finite boundary remains positive.

Therefore any first-loss sequence must escape in determinant-index space:

\[
\boxed{(r_n,k_n)\to\infty.}
\]

This converts a hypothetical threshold failure into an escape-to-infinity problem rather than a bounded finite-lattice event.

---

## IV. Exact primal/dual Jacobi–Trudi coordinate

Normalize

\[
h_n=a_n/a_0,\qquad H(z)=\sum_{n\ge0}h_nz^n,
\]

and define

\[
E(z)=\sum_{n\ge0}e_nz^n=\frac1{H(-z)}.
\]

For the rectangle \(\lambda=(k^r)\), ordinary and dual Jacobi–Trudi give

\[
\boxed{
D_{r,k}(a)=a_0^r\det[e_{r+j-i}]_{i,j=0}^{k-1}.
}
\]

Thus large determinant order / small shift in the original sequence is exactly small determinant order / large shift in the reciprocal sequence.

Under a verified simple-pole expansion for the reciprocal series, the alternating residue sign and the two Vandermonde signs cancel, yielding eventual positivity of the corresponding fixed-order dual minors.

---

## V. Reciprocal heat equation and the bilinear blind mode

If

\[
H_t(z)=G_t(-z),\qquad E_t(z)=1/H_t(z),
\]

then direct differentiation gives the exact nonlinear reciprocal evolution

\[
\boxed{
\partial_tE_t
=-4zE_t''-2E_t'+8z\frac{(E_t')^2}{E_t}.
}
\]

So Jacobi–Trudi duality does not turn the heat flow into another copy of the same linear PDE.

For every adaptive operator

\[
L=R\Delta_k^2+A\Delta_r^2,
\]

one has

\[
\boxed{L(rk)=0.}
\]

More generally \(c_0+c_1r+c_2k+c_3rk\) lies in the kernel. This identifies the bilinear \(rk\) scale as an exact blind mode of the naive harmonic-growth close.

---

## VI. Rectangular Schur representation and occupancy cap

In the PF-infinity / real-negative-zero phase, write

\[
G_t(z)=a_0(t)\prod_j(1+\alpha_j(t)z),\qquad \alpha_j(t)>0.
\]

Then

\[
\boxed{
D_{r,k}(t)=a_0(t)^r s_{(r^k)}(\alpha(t)).
}
\]

Define

\[
q_j=\alpha_j\frac{\partial}{\partial\alpha_j}\log s_{(r^k)}(\alpha).
\]

By the positive semistandard-tableau expansion, \(q_j\) is the expected occupancy of symbol \(j\). Since columns are strictly increasing, any symbol appears at most once per column:

\[
\boxed{0\le q_j\le r.}
\]

Homogeneity gives

\[
\boxed{\sum_jq_j=rk.}
\]

Therefore the normalized sensitivities

\[
p_j=q_j/(rk)
\]

satisfy

\[
\boxed{0\le p_j\le1/k,\qquad \sum_jp_j=1.}
\]

No individual zero parameter can carry more than \(1/k\) of the normalized logarithmic sensitivity of a rectangular minor.

---

## VII. Schur distortion bound

For positive parameter sequences \(\alpha,\beta\), put

\[
\delta_j=\log(\alpha_j/\beta_j).
\]

If \(|\delta_j|\le M_J\) for \(j\le J\) and \(|\delta_j|\le\varepsilon_J\) for \(j>J\), then every tableau monomial has exponent vector satisfying \(0\le m_j\le r\) and \(\sum m_j=rk\). Hence

\[
\boxed{
\left|\log\frac{s_{(r^k)}(\alpha)}{s_{(r^k)}(\beta)}\right|
\le rJM_J+\varepsilon_Jrk.
}
\]

Equivalently,

\[
\boxed{
\frac1{rk}\left|\log\frac{s_{(r^k)}(\alpha)}{s_{(r^k)}(\beta)}\right|
\le \frac{JM_J}{k}+\varepsilon_J.
}
\]

---

## VIII. Sparse angular phase positivity

Allow complex-conjugate parameter pairs \(\rho_\ell e^{\pm i\theta_\ell}\) while all remaining parameters are positive real.

Every tableau monomial has phase bounded by

\[
|\arg M|\le r\sum_\ell|\theta_\ell|.
\]

Therefore

\[
\boxed{
r\sum_\ell|\theta_\ell|<\pi/2
\quad\Longrightarrow\quad
D_{r,k}>0.
}
\]

For a single conjugate pair,

\[
\boxed{
r|\theta|<\pi/2\Longrightarrow D_{r,k}>0\text{ for every }k.}
\]

Thus any consecutive Toeplitz minor capable of detecting that angular defect must have order at least

\[
\boxed{r\ge \frac{\pi}{2|\theta|}.}
\]

This gives an exact determinant-order detection delay as an off-axis pair approaches the real-negative axis.

---

## IX. What these four campaigns collectively established

The exact progression is now public:

\[
\text{nonlinear odds lattice}
\to
\text{exact rational orbit}
\to
\text{discrete elliptic comparison}
\to
\text{heat-flow harmonic velocity}
\to
\text{no bounded first nucleation}
\to
\text{primal/dual coordinate}
\to
\text{Schur occupancy dilution}
\to
\text{angular detection delay}.
\]

The remaining frontier identified by the packets is an escape-to-infinity / collision-angle problem, not a missing finite determinant calculation.

## Verification receipts carried by the recovered export

- Encirclement II: **7/7** terminal algebra checks passed.
- Encirclement III: **5/5** exact algebra checks passed.
- Encirclement IV: **6/6** algebraic checks passed.
- Encirclement V: **6/6** algebraic/combinatorial checks passed.

See `VERIFIER-SUMMARY.md` and the recovered theorem ledgers in this directory.
