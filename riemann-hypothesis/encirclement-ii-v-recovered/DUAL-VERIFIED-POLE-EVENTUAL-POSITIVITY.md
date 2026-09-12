# Dual verified-pole eventual positivity

**Author:** Jared Wilder  
**Recovered from:** RH Encirclement IV, Rounds 6–8

This theorem gives a positivity frontier orthogonal to the large-shift cubic wedge: **fixed original shift, large determinant order**.

## 1. Exact primal/dual coordinate

Normalize

\[
h_n=\frac{a_n}{a_0},\qquad
H(z)=\sum_{n\ge0}h_nz^n,
\]

and define

\[
E(z)=\sum_{n\ge0}e_nz^n=\frac1{H(-z)}.
\]

For the rectangular partition `(k^r)`, ordinary and dual Jacobi–Trudi give

\[
\boxed{
D_{r,k}(a)
=
a_0^r\det[e_{r+j-i}]_{i,j=0}^{k-1}.
}
\]

Thus large original determinant order / fixed shift is exactly fixed dual determinant order / large dual shift.

---

## 2. Pole hypothesis

Fix a positive integer `m`.

Assume the first `m+1` singularities of `E` in modulus are simple positive poles

\[
0<\rho_1<\rho_2<\cdots<\rho_{m+1},
\]

with no competing singularity of the same modulus.

Then the coefficient sequence has an expansion

\[
\boxed{
e_n=\sum_{j=1}^{m}c_j\rho_j^{-n}+O(\rho_{m+1}^{-n}).}
\]

When `E(0)>0` and its real denominator crosses successive simple real zeros, the residues alternate:

\[
\boxed{\operatorname{sgn}c_j=(-1)^{j-1}.}
\]

---

## 3. Leading dual determinant

Insert the pole expansion into

\[
\det[e_{n+j-i}]_{i,j=0}^{m-1}.
\]

Cauchy–Binet gives the leading contribution

\[
\left(\prod_{j=1}^{m}c_j\rho_j^{-n}\right)
\det[\rho_j^{\,i}]_{i,j=0}^{m-1}
\det[\rho_j^{-q}]_{j,q=0}^{m-1}.
\]

The two Vandermonde factors contribute total sign

\[
(-1)^{m(m-1)/2},
\]

while the alternating residue product contributes

\[
\operatorname{sgn}\prod_{j=1}^{m}c_j
=(-1)^{m(m-1)/2}.
\]

The signs therefore cancel.

Because the next singularity is strictly farther away, the remainder is exponentially smaller than the leading term.

Hence:

## Theorem

\[
\boxed{
\det[e_{n+j-i}]_{i,j=0}^{m-1}>0
\quad\text{for all sufficiently large }n.
}
\]

By the exact Jacobi–Trudi transpose,

\[
\boxed{
D_{r,m}(a)>0
\quad\text{for all sufficiently large }r.
}
\]

So any fixed original shift covered by a verified initial block of simple real reciprocal poles has an eventual strictly positive large-order tail.

---

## 4. Two-coordinate escape corollary

The Encirclement IV program has three pieces:

1. **no bounded first nucleation:** a first-loss sequence cannot remain in a finite `(r,k)` box;
2. **primal large-shift positivity:** for every fixed order `r`, the established cubic-wedge region eventually contains all sufficiently large shifts `k`;
3. **dual fixed-shift positivity:** the theorem above gives eventual positivity as `r -> infinity` for each fixed verified shift `k`.

Consequently a hypothetical escaping negative-minor sequence cannot have either coordinate bounded.

Therefore

\[
\boxed{
r_n\to\infty,\qquad k_n\to\infty.}
\]

The remaining determinant obstruction is genuinely a two-scale / collective regime rather than either coordinate tail separately.

---

## Riemann application

Verified critical-line zeros give a finite initial collection of positive real poles in the reciprocal coordinate used by the program. For every fixed shift supported by such a verified pole block, the theorem supplies an unconditional eventual-positive large-order tail.

The theorem itself is conditional only on the explicitly stated pole hypotheses; finite zero verification determines how large a fixed-shift block can currently be instantiated for the Riemann sequence.
