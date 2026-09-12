# A sign obstruction for the natural theta-moment determinant lift

**Author:** Jared Wilder  
**Date:** 2026-09-12  
**Status:** exact algebraic no-go theorem; not an RH result; novelty not asserted

## Setup

Write the completed-zeta coefficient moments in the form

\[
a_n=\int_0^\infty b_n(u)\Phi(u)\,du,
\qquad
b_n(u)=\begin{cases}
\dfrac{u^{2n}}{(2n)!},&n\ge0,\\
0,&n<0,
\end{cases}
\]

with `Phi(u) >= 0` on the integration domain.

For the consecutive Toeplitz minor

\[
D_{r,k}=\det[a_{k+j-i}]_{i,j=0}^{r-1},
\]

row multilinearity gives the exact `r`-fold lift

\[
\boxed{
D_{r,k}
=
\int_{(0,\infty)^r}
\det[b_{k+j-i}(u_i)]_{i,j=0}^{r-1}
\prod_{i=0}^{r-1}\Phi(u_i)\,du_i.
}
\]

Because the outer measure is positive, a tempting route would be to prove that the inner determinant has a fixed nonnegative sign.

That route fails at the first nontrivial determinant order.

## Order-two sign theorem

For `r=2`, symmetrizing in the two integration variables `u,v` gives an inner kernel proportional to

\[
\boxed{
\mathcal S_{2,k}(u,v)
=
\frac{u^{2k-2}v^{2k-2}}{((2k)!)^2}
\left[
 u^2v^2-\frac{c_k}{2}(u^4+v^4)
\right],
}
\]

where

\[
c_k=
\frac{(2k)(2k-1)}{(2k+1)(2k+2)}\in(0,1).
\]

The bracket changes sign on `(0,infinity)^2` for every `k>=1`.

Indeed, on the diagonal `u=v`,

\[
u^2v^2-\frac{c_k}{2}(u^4+v^4)
=(1-c_k)u^4>0.
\]

But fixing `v>0` and letting `u/v -> infinity`,

\[
u^2v^2-\frac{c_k}{2}(u^4+v^4)
\sim -\frac{c_k}{2}u^4<0.
\]

Therefore

\[
\boxed{
\mathcal S_{2,k}\text{ is sign-changing for every }k\ge1.
}
\]

For example,

\[
k=2,\qquad u=10,\qquad v=1
\]

gives

\[
\mathcal S_{2,2}(10,1)=-329.895833333\ldots.
\]

## Consequence

The exact positive-measure lift does **not** turn consecutive Toeplitz-minor positivity into pointwise positivity of its most direct inner determinant kernel. In particular, the implication

\[
\Phi\ge0
\quad\Longrightarrow\quad
\text{inner determinant kernel}\ge0
\]

is false already at `r=2`.

This does not rule out:

- cancellation-based multiple-integral proofs;
- a different change of variables;
- a different determinant factorization;
- total-positivity arguments using more structure than positivity of `Phi`.

It rules out only the natural pointwise-sign shortcut above.

## Provenance and novelty

This identity/no-go pair was recovered from the August Terminal Encirclement during a second full re-mining of the RH estate on 2026-09-12. A targeted literature search finds extensive Andreief/multiple-integral representations for Toeplitz determinants, so no novelty claim is made for determinant lifting in general. The exact theta-moment specialization and sign obstruction are recorded here primarily as a reproducible route-kill and provenance artifact.
