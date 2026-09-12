# No fixed finite Hausdorff/Toeplitz sign battery can characterize the positive-real spectral cone

**Author:** Jared Wilder  
**Date:** 2026-09-12  
**Status:** exact generic no-go theorems; **not an RH theorem**  
**Novelty:** not asserted. The value is constructive route-kill / regression mathematics.

## 1. Executive statement

There are three levels of obstruction.

1. A soft continuity theorem: any fixed finite list of strict Hausdorff/Toeplitz signs can survive a sufficiently small nonreal conjugate perturbation.
2. An explicit arbitrary-depth theorem: **any prescribed finite Hausdorff rectangle** can be positive while a later Toeplitz determinant is negative.
3. A converse explicit arbitrary-depth theorem: **any prescribed finite Toeplitz rectangle** can be positive while a later Hausdorff moment is negative.

Thus the failure is bidirectional and persists at arbitrary finite depth.

This does **not** say RH cannot have a finite proof. It says a finite proof cannot consist only of a bounded prefix of these generic sign hierarchies unless an additional theorem controls the tail.

---

## 2. Coordinates

Let

\[
G(z)=a_0\prod_j(1+\alpha_j z)
=\sum_{k\ge0}a_kz^k.
\]

Write

\[
y_j=\frac{\alpha_j}{1+\alpha_j}.
\]

The Hausdorff/Beta hierarchy is

\[
\boxed{
H_{n,q}
=4\sum_j y_j^{n+1}(1-y_j)^q.
}
\tag{1}
\]

The consecutive Toeplitz hierarchy is

\[
\boxed{
D_{r,k}
=\det[a_{k+j-i}]_{i,j=0}^{r-1}.
}
\tag{2}
\]

In the positive-real spectral cone these are positive in their natural ranges.

---

## 3. Exactly solvable conjugate-pair model

Take only

\[
\alpha_\pm=e^{\pm i\theta},
\qquad
0<\theta<\pi.
\]

Then

\[
G(z)=1+2\cos\theta\,z+z^2.
\]

### Determinant side

For `k=1`, the tridiagonal determinant obeys

\[
D_{r,1}
=2\cos\theta\,D_{r-1,1}-D_{r-2,1},
\]

so

\[
\boxed{
D_{r,1}
=\frac{\sin((r+1)\theta)}{\sin\theta}.
}
\tag{3}
\]

Also

\[
D_{r,2}=1.
\]

### Hausdorff side

Since

\[
1+e^{i\theta}
=2\cos(\theta/2)e^{i\theta/2},
\]

one obtains

\[
\boxed{
H_{n,q}
=
\frac{8}
{(2\cos(\theta/2))^{n+q+1}}
\cos\!\left(\frac{(n+1-q)\theta}{2}\right).
}
\tag{4}
\]

For the isolated pair, the first sign crossing of `D_(r,1)` and `H_(r,0)` occurs at the same scale

\[
(r+1)\theta=\pi.
\]

The finite-transfer pathology is therefore not caused by incompatible single-pair physics. It appears once background spectral mass is allowed to mask defects.

---

## 4. Arbitrary-depth theorem I — any finite Hausdorff rectangle can miss a determinant failure

Fix arbitrary finite integers

\[
N,Q\ge0.
\]

For the conjugate-pair model (4),

\[
H_{n,q}>0
\]

whenever

\[
|(n+1-q)\theta|<\pi.
\]

Choose `theta>0` so small that

\[
\boxed{
\theta
<
\frac{\pi}
{\max_{0\le n\le N,\,0\le q\le Q}|n+1-q|}
}
\tag{5}
\]

(with the obvious convention if the maximum is zero).

Then

\[
\boxed{
H_{n,q}>0
\qquad
(0\le n\le N,\ 0\le q\le Q).
}
\tag{6}
\]

Now choose `r` with

\[
\pi<(r+1)\theta<2\pi.
\]

Equation (3) gives

\[
\boxed{D_{r,1}<0.}
\tag{7}
\]

Therefore

\[
\boxed{
\text{no fixed finite Hausdorff sign rectangle implies global determinant positivity.}
}
\tag{8}
\]

This is explicit at arbitrary depth; it is not a continuity argument.

---

## 5. Arbitrary-depth theorem II — any finite determinant rectangle can miss a Hausdorff failure

Fix arbitrary finite

\[
R,K\ge1.
\]

Choose `M>=K` and start from

\[
\alpha_1=\cdots=\alpha_M=1,
\qquad
G_0(z)=(1+z)^M.
\]

Every relevant rectangular Schur evaluation is strictly positive, hence

\[
D_{r,k}>0
\qquad
(r\ge1,\ 1\le k\le M).
\]

Replace two parameters by

\[
e^{\pm i\theta}
\]

for sufficiently small `theta>0` and leave the other `M-2` parameters equal to `1`.

Because only finitely many determinants

\[
D_{r,k},
\qquad
1\le r\le R,\ 1\le k\le K,
\]

are under consideration and all are strictly positive at `theta=0`, continuity gives

\[
\boxed{
D_{r,k}>0
\qquad
(1\le r\le R,\ 1\le k\le K)
}
\tag{9}
\]

for all sufficiently small nonzero `theta`.

But the two transformed Bernoulli parameters satisfy

\[
\left|\frac{e^{i\theta}}{1+e^{i\theta}}\right|
=
\frac1{2\cos(\theta/2)}
>
\frac12,
\]

whereas every untouched parameter has `y=1/2`.

Choose, for example,

\[
\theta=\frac{2\pi}{L}
\]

with `L` large enough to preserve (9). At indices

\[
n+1=(2j+1)L,
\]

the conjugate pair has negative phase, while its modulus advantage over the `M-2` real background atoms grows exponentially. Hence for sufficiently large `j`,

\[
\boxed{H_{n,0}<0.}
\tag{10}
\]

Therefore

\[
\boxed{
\text{no fixed finite determinant sign rectangle implies global Hausdorff positivity.}
}
\tag{11}
\]

---

## 6. Exact finite counterexample A

Take

\[
\alpha=\left\{\frac{i}{10},-\frac{i}{10},\frac14\right\}.
\]

Then

\[
G(z)=1+\frac14z+\frac1{100}z^2+\frac1{400}z^3.
\]

Every one of the sixteen exact quantities

\[
H_{n,q},
\qquad
0\le n,q\le3,
\]

is strictly positive. The smallest is

\[
H_{3,3}
=
\frac{32405996263939456}
{8376057438336015625}
>0.
\]

Yet

\[
\boxed{
D_{2,2}=-\frac{21}{40000}<0.
}
\]

So even a complete positive `4x4` Hausdorff block does not force the nearby determinant sign.

---

## 7. Exact finite counterexample B

Take

\[
\alpha=\left\{\frac{i}{10},-\frac{i}{10},4,4,4\right\}.
\]

Then every determinant

\[
D_{r,k},
\qquad
1\le r,k\le3,
\]

is strictly positive, while

\[
\boxed{
H_{1,3}
=-\frac{233310703808}{32844064065625}<0.
}
\]

Thus finite-prefix implication fails in the reverse direction as well.

---

## 8. Stronger soft theorem — arbitrary finite mixed sign battery

Take any finite list of strict requirements selected from

\[
H_{n,q}>0
\]

and

\[
D_{r,k}>0.
\]

Choose `M` larger than every determinant shift appearing in the list and begin at

\[
\alpha_1=\cdots=\alpha_M=1.
\]

Every selected quantity is strictly positive.

Perturb two coordinates to

\[
\alpha_1=e^{i\theta},
\qquad
\alpha_2=e^{-i\theta}.
\]

For sufficiently small nonzero `theta`, continuity preserves every selected strict inequality, but the spectrum is no longer positive real.

Hence

\[
\boxed{
\text{no fixed finite mixed H/D sign battery characterizes the positive-real spectral cone.}
}
\tag{12}
\]

---

## 9. Operational consequence

The correct conclusion is not “finite computation is useless.”

It is:

> **A bounded prefix of generic sign tests needs a genuine tail theorem.**

A finite RH proof could still work if zeta-specific structure supplies, for example,

- an exact recurrence propagating finitely many signs to all indices;
- a tail estimate converting finite numerical values into uniform control;
- a rigidity theorem excluding the generic perturbations used above;
- an analytic monotonicity or continuation theorem collapsing the infinite hierarchy.

Without such structure, simply checking a larger finite sign rectangle cannot logically close the spectral problem.

This is why the companion reconstruction program has moved from sign testing to **quantitative tail-controlled reconstruction**.

---

## 10. Prior-art boundary

The ingredients used here—continuity, Chebyshev-type sine recurrences, Schur positivity on positive variables, and elementary conjugate-pair algebra—are classical.

A targeted search during the originating Pass-4 audit did not locate these exact cross-hierarchy arbitrary-depth constructions. That does **not** establish novelty, and no novelty claim is made here.

The reason for publishing them is stronger regression coverage: future RH campaigns should be mechanically prevented from interpreting any bounded generic Hausdorff or Toeplitz sign prefix as a global spectral certificate.

---

## 11. What is not claimed

This note does **not** claim:

- RH or its negation;
- impossibility of a finite RH proof;
- impossibility of a zeta-specific finite certificate;
- that Hausdorff or Toeplitz criteria are globally invalid;
- settled literature novelty.

It proves only the generic bounded-prefix no-go statements above, with explicit constructions in both directions.