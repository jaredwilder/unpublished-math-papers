# Dual verified-pole eventual positivity

**Author:** Jared Wilder  
**Recovered from:** RH Encirclement IV, Rounds 6–8  
**Forensic scope correction:** 2026-09-12

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

Assume that `E` is meromorphic in a disk large enough to contain its first `m+1` singularities in modulus and that those singularities are simple positive poles

\[
0<\rho_1<\rho_2<\cdots<\rho_{m+1},
\]

with no other singularity of modulus at most `rho_{m+1}` competing with this ordered block.

Under that hypothesis, standard residue/singularity analysis gives

\[
\boxed{
e_n=\sum_{j=1}^{m}c_j\rho_j^{-n}+O(\rho_{m+1}^{-n}).}
\]

When `E=1/Q` with `Q(0)>0` real on the real axis and `rho_1,...,rho_{m+1}` are successive simple positive zeros of `Q`, the sign of `Q` flips at each zero, so the residues alternate:

\[
\boxed{\operatorname{sgn}c_j=(-1)^{j-1}.}
\]

The phrase **first singularities in modulus** is load-bearing. Knowing merely that some positive real poles exist does not establish this hypothesis.

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

The first Vandermonde is positive for

\[
0<\rho_1<\cdots<\rho_m,
\]

while the inverse-pole Vandermonde contributes sign

\[
(-1)^{m(m-1)/2}.
\]

The alternating residue product contributes the same sign:

\[
\operatorname{sgn}\prod_{j=1}^{m}c_j
=(-1)^{m(m-1)/2}.
\]

The signs therefore cancel, so the leading term is positive.

Because the next singularity is strictly farther away in modulus, every determinant contribution replacing one of the first `m` poles by a later singularity is exponentially smaller in `n` than the leading `m`-pole contribution.

Hence:

## Theorem

For `n` sufficiently large (and in particular `n>=m-1` so every displayed coefficient index is nonnegative),

\[
\boxed{
\det[e_{n+j-i}]_{i,j=0}^{m-1}>0.
}
\]

By the exact Jacobi–Trudi transpose,

\[
\boxed{
D_{r,m}(a)>0
\quad\text{for all sufficiently large }r.
}
\]

So any fixed original shift whose reciprocal generating function satisfies the stated verified initial-pole hypothesis has an eventual strictly positive large-order tail.

---

## 4. Two-coordinate escape corollary

Suppose, in addition, that a determinant program has established:

1. **no bounded first nucleation:** a first-loss sequence cannot remain in a finite `(r,k)` box;
2. **primal large-shift positivity:** for every fixed order `r`, all sufficiently large shifts `k` are positive;
3. **dual fixed-shift positivity:** for each fixed shift under consideration, the reciprocal generating function satisfies the pole hypothesis above, so the theorem supplies positivity for all sufficiently large `r`.

Then a hypothetical escaping negative-minor sequence cannot have either coordinate bounded, and therefore

\[
\boxed{
r_n\to\infty,\qquad k_n\to\infty.}
\]

This is a conditional structural corollary. It isolates the remaining obstruction as a genuinely two-scale regime once both one-coordinate tails are independently certified.

---

## Riemann application — exact requirement

For the Riemann/Xi coefficient sequence, a finite list of numerically located critical-line zeros is **not by itself** enough to invoke the theorem.

To instantiate a fixed shift `m`, one needs a rigorous zero/singularity certification strong enough to establish that the corresponding poles

\[
\rho_1,\ldots,\rho_{m+1}
\]

are in fact the **first `m+1` singularities in modulus**, are simple and positive, and have no competing singularity of equal or smaller modulus.

An exhaustive verified-zero computation with a correct zero count up to the required height can in principle provide that input. Once such an initial pole block is established, the theorem gives an unconditional eventual-positive large-order tail **conditional only on that certified block and the analytic pole-expansion hypotheses above**.

The theorem itself is generic asymptotic determinant algebra. It does not prove the needed Riemann pole block, does not control shifts beyond the certified block, and does not prove RH.
