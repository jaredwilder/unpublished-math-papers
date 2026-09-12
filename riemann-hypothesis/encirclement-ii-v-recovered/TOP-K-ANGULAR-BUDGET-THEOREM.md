# Top-k angular budget theorem for rectangular Toeplitz minors

**Author:** Jared Wilder  
**Recovered from:** RH Encirclement V, Round 9

Assume a consecutive Toeplitz minor is represented in the zero-parameter coordinate by a rectangular Schur polynomial of shape `(r^k)`.

Let the absolute angular defects of the relevant complex zero parameters be sorted

\[
\vartheta_1\ge \vartheta_2\ge\cdots\ge0.
\]

A semistandard tableau monomial of shape `(r^k)` has total degree `rk`, while the exponent of any individual variable is at most `r` because columns are strictly increasing.

Therefore the largest possible total absolute phase is obtained by spending the available exponent budget `r` on the `k` largest angular defects. Hence every tableau monomial satisfies

\[
\boxed{
|\arg M|\le r\sum_{j=1}^{k}\vartheta_j.
}
\]

Consequently, if

\[
\boxed{
r\sum_{j=1}^{k}\vartheta_j<\frac{\pi}{2},
}
\]

then every tableau monomial lies in the open right half-plane. Their positive-coefficient sum therefore has positive real part, and in particular the rectangular Schur polynomial—and hence the corresponding consecutive Toeplitz minor—is strictly positive:

\[
\boxed{
r\sum_{j=1}^{k}\vartheta_j<\frac{\pi}{2}
\quad\Longrightarrow\quad
D_{r,k}>0.
}
\]

## Relation to the earlier sparse phase bound

The earlier sparse criterion

\[
r\sum_\ell |\theta_\ell|<\pi/2
\]

charges every angular defect. The top-`k` theorem is sharper: a rectangle of width `k` can allocate exponent `r` to at most `k` variables in the extremal phase budget, so only the `k` largest defects control the universal monomial-angle bound.

## Detection interpretation

A determinant at scale `(r,k)` cannot change sign through phase accumulation while the top-`k` angular budget remains below `pi/2`.

Thus any phase-driven first-loss mechanism at that scale must satisfy

\[
\boxed{
\sum_{j=1}^{k}\vartheta_j\ge \frac{\pi}{2r}.
}
\]

This is the two-parameter refinement of the single-pair detection-delay bound.

## Frontier exposed by the theorem

If a hypothetical loss sequence escapes with both `r,k -> infinity`, finite information about any fixed number of low zeros is not by itself enough: the relevant positivity test samples an increasing top-`k` angular budget.

The remaining analytic target isolated by Encirclement V is therefore a bound on

\[
r\sum_{j=1}^{k}\vartheta_j(t)
\]

in the critical two-scale regime.
