# Top-k angular budget theorem for rectangular Toeplitz minors

**Author:** Jared Wilder  
**Recovered from:** RH Encirclement V, Round 9  
**Forensic scope correction:** 2026-09-12

Assume a consecutive Toeplitz minor is represented in zero-parameter coordinates by a rectangular Schur polynomial of shape `(r^k)`:

\[
D_{r,k}=a_0^r\,s_{(r^k)}(\alpha_1,\alpha_2,\ldots),
\qquad a_0>0,
\]

at a parameter point where the Schur expansion is absolutely meaningful (for a finite parameter set this is automatic).

Write

\[
\alpha_j=|\alpha_j|e^{i\theta_j}
\]

and sort the absolute angular defects

\[
\vartheta_1\ge \vartheta_2\ge\cdots\ge0,
\qquad \{\vartheta_j\}=\{|\theta_j|\}.
\]

## Phase-budget theorem

A semistandard-tableau monomial of shape `(r^k)` has total degree `rk`, while the exponent of any individual variable is at most `r` because columns are strictly increasing.

If its exponent vector is `(e_j)`, then

\[
0\le e_j\le r,
\qquad
\sum_j e_j=rk.
\]

Therefore

\[
|\arg M|
=\left|\sum_j e_j\theta_j\right|
\le \sum_j e_j\vartheta_j
\le r\sum_{j=1}^k\vartheta_j.
\]

The last inequality is the elementary linear-programming extremum obtained by spending the available exponent budget `r` on the `k` largest angular defects.

Hence every tableau monomial satisfies

\[
\boxed{
|\arg M|\le r\sum_{j=1}^{k}\vartheta_j.
}
\]

Consequently, if

\[
\boxed{
r\sum_{j=1}^{k}\vartheta_j<\frac{\pi}{2},}
\]

then every tableau monomial lies in the open right half-plane. Since every tableau coefficient is positive,

\[
\boxed{
\operatorname{Re}s_{(r^k)}(\alpha)>0.
}
\]

This is the unconditional conclusion of the phase argument.

## Real Toeplitz-minor corollary

To conclude the ordered real inequality `D_{r,k}>0`, one needs the determinant to be real. A sufficient hypothesis is that the parameter multiset is invariant under complex conjugation (with real parameters allowed), so that the symmetric polynomial satisfies

\[
\overline{s_{(r^k)}(\alpha)}=s_{(r^k)}(\overline\alpha)=s_{(r^k)}(\alpha).
\]

Under this reality/conjugation hypothesis,

\[
\operatorname{Re}s_{(r^k)}(\alpha)>0
\]

becomes

\[
s_{(r^k)}(\alpha)>0,
\]

and therefore

\[
\boxed{
r\sum_{j=1}^{k}\vartheta_j<\frac{\pi}{2}
\quad\Longrightarrow\quad
D_{r,k}>0.}
\]

For applications to reflection/conjugation-symmetric zero configurations, this is the intended real corollary.

## Relation to the earlier sparse phase bound

The earlier sparse criterion

\[
r\sum_\ell |\theta_\ell|<\pi/2
\]

charges every angular defect. The top-`k` theorem is sharper: a rectangle of width `k` can allocate exponent `r` to at most `k` variables in the extremal phase budget, so only the `k` largest defects control the universal monomial-angle bound.

## Detection interpretation

At a real/conjugation-symmetric parameter point, a determinant at scale `(r,k)` cannot lose positivity through phase accumulation while the top-`k` angular budget remains below `pi/2`.

Thus any phase-driven first-loss mechanism at that scale must satisfy

\[
\boxed{
\sum_{j=1}^{k}\vartheta_j\ge \frac{\pi}{2r}.}
\]

This is the two-parameter refinement of the single-pair detection-delay bound.

## Frontier exposed by the theorem

If a hypothetical loss sequence escapes with both `r,k -> infinity`, finite information about any fixed number of low parameters is not by itself enough: the relevant positivity test samples an increasing top-`k` angular budget.

The remaining analytic target isolated by Encirclement V is therefore a bound on

\[
r\sum_{j=1}^{k}\vartheta_j(t)
\]

in the critical two-scale regime.

## Scope note

The phase-budget inequality itself gives a **positive real part** without any reality assumption. The ordered statement `D_{r,k}>0` is only asserted when the determinant is known to be real, for example by conjugation symmetry. This hypothesis was present in the later estate adjudication and is made explicit here to prevent the stronger statement from being read outside its valid domain.
