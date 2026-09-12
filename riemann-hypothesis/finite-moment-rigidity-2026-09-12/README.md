# Finite even-moment rigidity for reflection-symmetric off-line packets

**Author:** Jared Wilder  
**Date:** 2026-09-12  
**Status:** proved finite algebraic theorem; not a proof of the Riemann Hypothesis  
**Provenance:** extracted and strengthened during the second full re-mining of the RH research estate

## Theorem

Fix an integer `Q >= 1`. For `j=1,...,Q`, let

\[
\frac12\pm d_j\pm i t_j
\]

be `Q` reflection/conjugation quadruples, with `d_j,t_j` real. Compare them with `2Q` critical-line conjugate pairs

\[
\frac12\pm i y_\ell,
\qquad \ell=1,\dots,2Q,
\]

where every `y_\ell` is real.

Assume the two configurations have the same first `2Q` raw even power sums:

\[
\sum_{\rho\in\mathcal O}\rho^{2m}
=
\sum_{\rho\in\mathcal L}\rho^{2m},
\qquad m=1,\dots,2Q.
\]

Then

\[
\boxed{d_1=\cdots=d_Q=0.}
\]

Equivalently: a genuine off-line packet of `Q` reflection quadruples cannot be moment-matched by `2Q` critical-line pairs through raw even order `4Q`.

A stronger reconstruction statement holds. The moment equalities force the multiset of squared critical-line heights to be

\[
\boxed{
\{y_1^2,\dots,y_{2Q}^2\}
=
\{(t_j+i d_j)^2,(t_j-i d_j)^2:1\le j\le Q\}.
}
\]

Since the left side consists of nonnegative real numbers, every `d_j` must vanish.

## Proof

Center the configurations at `1/2`. Reflection symmetry makes every centered odd power sum vanish on both sides. Because the two configurations have the same cardinality `4Q`, the binomial expansion

\[
(\tfrac12+x)^{2m}
=
\sum_{r=0}^{2m}\binom{2m}{r}2^{-(2m-r)}x^r
\]

is triangular in the centered even power sums. Therefore equality of the raw even moments for `m=1,...,2Q` implies equality of the centered even moments through order `4Q`.

For one off-line quadruple, the centered points are

\[
d+it,\quad d-it,\quad -d-it,\quad -d+it.
\]

Hence its centered `2m`-th power sum equals

\[
2\big((d+it)^{2m}+(d-it)^{2m}\big)
=
2(-1)^m\big((t+id)^{2m}+(t-id)^{2m}\big).
\]

Define the `2Q` complex numbers

\[
U_{2j-1}=(t_j+i d_j)^2,
\qquad
U_{2j}=(t_j-i d_j)^2.
\]

The centered even moment equalities therefore give

\[
\sum_{\ell=1}^{2Q} y_\ell^{2m}
=
\sum_{r=1}^{2Q}U_r^m,
\qquad m=1,\dots,2Q.
\]

Thus the first `2Q` power sums of the two `2Q`-element multisets

\[
\{y_\ell^2\}_{\ell=1}^{2Q}
\quad\text{and}\quad
\{U_r\}_{r=1}^{2Q}
\]

are identical. Newton's identities recover all elementary symmetric polynomials of `2Q` variables from those first `2Q` power sums. Consequently the corresponding monic polynomials are identical, so the multisets themselves are identical:

\[
\{y_1^2,\dots,y_{2Q}^2\}
=
\{(t_j+i d_j)^2,(t_j-i d_j)^2:1\le j\le Q\}.
\]

Every element on the left is a nonnegative real number. If `d_j t_j != 0`, the two numbers `(t_j +/- i d_j)^2` are nonreal. If `t_j=0` and `d_j != 0`, they equal `-d_j^2<0`. Therefore nonnegative reality forces `d_j=0` for every `j`. QED.

## What this does and does not say

This is a finite algebraic rigidity theorem about reflection-symmetric point configurations. It does **not** prove that finitely many moments characterize the full zero set of the Riemann zeta function, and it does **not** prove RH.

Its relevance to the RH campaign is narrower: a finite adversary consisting of `Q` off-critical reflection quadruples cannot hide behind an equal-cardinality critical-line model once the first `2Q` raw even moments are fixed.

## Verification

`verify_finite_moment_rigidity.py` performs exact symbolic checks for `Q=1,2,3,4`. It verifies:

1. the triangular raw-to-centered moment conversion;
2. the power-sum reduction to the numbers `(t_j +/- i d_j)^2`;
3. exact Newton reconstruction of the monic polynomial;
4. failure of nonnegative-real squared heights for genuine off-line test packets.

The script is a sanity check, not a substitute for the proof above.

## Novelty status

A targeted literature search on 2026-09-12 found standard use of Newton identities to reconstruct zero power sums from `xi`-data and extensive moment criteria around RH, but no exact match for the finite reflection-quadruple versus critical-line-pair rigidity theorem above.

**Novelty is therefore not asserted as settled.** This public note records the theorem, proof, scope, date, and provenance while broader expert/literature review continues.
