# Newman collisions force Hausdorff-witness order escape

**Author:** Jared Wilder  
**Date:** 2026-09-12  
**Status:** conditional zeta-specific cross-representation theorem; **not an RH proof**  
**Novelty boundary:** de Bruijn–Newman collision scaling and Hausdorff-moment criteria are classical. The transport of a finite Newman/Hermite collision into an explicit lower barrier for a negative Hausdorff boundary witness is new to this research estate; historical priority is **unverified**.

## 1. Statement

Let `H_t(x)` be the de Bruijn–Newman heat family in the convention

\[
\partial_tH_t=-\partial_x^2H_t.
\]

Assume hypothetically that the de Bruijn–Newman constant satisfies

\[
\Lambda>0.
\]

At `t=Lambda`, let the finitely many positive multiple zeros be

\[
x_a>0,
\]

with finite multiplicities `m_a>=2`. Let

\[
\xi_{m,\max}
\]

denote the largest positive zero of the physicists' Hermite polynomial `H_m`.

Put

\[
\delta=\Lambda-t>0.
\]

The local Hermite collision law gives, for each positive Hermite zero `xi`,

\[
x_{a,\xi}(\Lambda-\delta)
=x_a+2i\xi\sqrt\delta+O(\delta).
\tag{1}
\]

Map a heat-flow zero into the Schur/PF spectral parameter

\[
\alpha=\frac1{x^2},
\]

and then into the Hausdorff/Bernoulli parameter

\[
y=\frac{\alpha}{1+\alpha}.
\]

Thus exactly

\[
\boxed{y=\frac1{1+x^2}.}
\tag{2}
\]

Define

\[
\boxed{
B_\Lambda
:=
4\max_a
\frac{x_a\,\xi_{m_a,\max}}
{1+x_a^2}.
}
\tag{3}
\]

Then the largest angular defect among the nonreal Hausdorff spectral atoms satisfies

\[
\boxed{
\theta_{\max}(t)
=B_\Lambda\sqrt{\Lambda-t}
+O(\Lambda-t).
}
\tag{4}
\]

For the Hausdorff boundary row

\[
H_{n,0}
=4\sum_j y_j^{n+1},
\tag{5}
\]

any negative value sufficiently close below the threshold must obey

\[
\boxed{
 n+1
\ge
\frac{\pi}
{2B_\Lambda\sqrt{\Lambda-t}}
\left(1+O(\sqrt{\Lambda-t})\right).
}
\tag{6}
\]

Equivalently,

\[
\boxed{
 n+1
\ge
\frac{\pi}
{8\sqrt{\Lambda-t}}
\left(
\max_a
\frac{x_a\xi_{m_a,\max}}{1+x_a^2}
\right)^{-1}
\left(1+O(\sqrt{\Lambda-t})\right).
}
\tag{7}
\]

Therefore, for every fixed finite Hausdorff-index cap `N`, there exists `epsilon_N>0` such that

\[
\boxed{
H_{n,0}(t)>0
\qquad
(0\le n\le N)
}
\tag{8}
\]

for every

\[
\Lambda-\varepsilon_N<t<\Lambda.
\]

So the Hausdorff hierarchy, like the consecutive-Toeplitz hierarchy, becomes an **infinite-index detector** near a hypothetical positive Newman threshold.

---

## 2. Local phase transport

Let

\[
x=x_a+2i\xi\sqrt\delta+O(\delta).
\]

From (2),

\[
\log y=-\log(1+x^2).
\]

At the real baseline `x_a`,

\[
\frac{d}{dx}\log y
=-\frac{2x_a}{1+x_a^2}.
\]

Hence

\[
\log y
=
\log\frac1{1+x_a^2}
-
\frac{4ix_a\xi}{1+x_a^2}\sqrt\delta
+O(\delta).
\]

Therefore the conjugate pair of `y`-atoms has angular defect

\[
\boxed{
|\arg y|
=
\frac{4x_a\xi}{1+x_a^2}\sqrt\delta
+O(\delta).
}
\tag{9}
\]

Maximizing over the finitely many threshold collision clusters gives (4).

The collision site `x=0` does not occur for the Riemann Xi heat family at a positive threshold in the global-threshold reduction used by this estate, because the kernel value at the origin is positive. Thus the finite set in (3) consists of positive sites.

---

## 3. Positivity cone for one Hausdorff boundary index

A nonreal `y`-atom occurs with its complex conjugate. Its contribution to (5) is

\[
4\left(y^{n+1}+\bar y^{n+1}\right)
=
8|y|^{n+1}\cos((n+1)\arg y).
\tag{10}
\]

Hence that pair contributes positively whenever

\[
(n+1)|\arg y|<\frac\pi2.
\tag{11}
\]

Every real spectral atom sufficiently close below the threshold has

\[
y\in(0,1)
\]

and therefore contributes positively as well.

Consequently, if

\[
(n+1)\theta_{\max}(t)<\frac\pi2,
\tag{12}
\]

then **every term or conjugate-pair block in (5) is positive**, and therefore

\[
\boxed{H_{n,0}(t)>0.}
\tag{13}
\]

Taking the contrapositive and inserting (4) gives (6)–(7).

This is a lower barrier only. Crossing the barrier removes the termwise-positive guarantee; it does not force `H_(n,0)` to become negative.

---

## 4. Why the theorem is global near the threshold

The local computation becomes a global statement because the standard positive-threshold reduction supplies the following structure in a one-sided neighborhood below `Lambda`:

1. all sufficiently high zeros are real and simple;
2. there are only finitely many multiple threshold zeros;
3. every simple threshold zero continues as a real zero locally by the analytic implicit-function theorem;
4. every nonreal zero sufficiently close below the threshold therefore belongs to one of the finitely many Hermite collision clusters.

Thus `theta_max(t)` in (4) controls the entire nonreal Hausdorff spectral cloud near the hypothetical threshold, not merely one toy collision.

---

## 5. Comparison with determinant-order escape

The previously released determinant theorem shows that near the same hypothetical positive threshold, any negative consecutive Toeplitz/Schur minor must escape to determinant order

\[
r\asymp(\Lambda-t)^{-1/2}
\]

at the level of the phase lower barrier.

The present theorem shows that the Hausdorff boundary hierarchy has the **same universal escape exponent**:

\[
\boxed{
n_{\rm barrier}(t)\asymp(\Lambda-t)^{-1/2}.}
\tag{14}
\]

The constants differ because the two representations transform the same physical collision differently:

- determinant/Schur phase uses `alpha=1/x^2`;
- Hausdorff phase uses `y=1/(1+x^2)`.

But both turn an `O(sqrt(delta))` physical imaginary displacement into an `O(sqrt(delta))` angular defect, and both sign tests have phase tolerance of order inverse index.

---

## 6. Cross-route conclusion

This gives a sharper version of the estate's representation-conditioning diagnosis.

A hypothetical positive Newman threshold is a **finite physical-space collision**. Yet two independent spectral positivity hierarchies encode it as a defect whose first possible sign witness runs to infinity:

\[
\boxed{
\begin{array}{c}
\text{finite Newman/Hermite collision}\[1mm]
\Downarrow\\[1mm]
\text{Toeplitz witness order }r\to\infty\\[1mm]
\text{Hausdorff witness index }n\to\infty
\end{array}
\qquad
\text{at rate }(\Lambda-t)^{-1/2}.
}
\tag{15}
\]

Positive-Time Simplicity does not suffer this representation blow-up: it asks directly whether the finite physical event

\[
H_t(x)=H_t'(x)=0
\]

occurs.

So for excluding `Lambda>0`, the conclusion is now stronger than “determinants are badly conditioned near collision”:

> **Both coefficient-total-positivity and Hausdorff-moment sign hierarchies push the same finite collision to an infinite-index boundary. The physical PTS coordinate keeps it finite.**

This does not make either spectral hierarchy useless globally. It identifies their conditioning near the specific Newman-threshold obstruction.

---

## 7. Double-collision constant

For `m=2`, the physicists' Hermite polynomial has positive zero

\[
\xi_{2,\max}=\frac1{\sqrt2}.
\]

A double collision at `x_*` therefore gives

\[
B_\Lambda
=
\frac{2\sqrt2\,x_*}{1+x_*^2}
\]

for a single collision site, and hence any negative Hausdorff boundary witness must satisfy

\[
\boxed{
 n+1
\ge
\frac{\pi(1+x_*^2)}
{4\sqrt2\,x_*\sqrt{\Lambda-t}}
\left(1+O(\sqrt{\Lambda-t})\right).
}
\tag{16}
\]

Again this is a forbidden-region bound, not an assertion that a negative `H_(n,0)` exists at the threshold scale.

---

## 8. Literature / novelty boundary

The following layers are classical or already external:

- de Bruijn–Newman heat deformation and threshold theory;
- Hermite scaling of finite-multiplicity heat-equation zero collisions;
- Hausdorff-moment formulations associated with RH;
- the general fact that a conjugate pair contributes a cosine phase to a power sum.

A targeted current search on 2026-09-12 did not locate the exact theorem transporting the Newman/Hermite collision through

\[
x\mapsto\alpha=1/x^2\mapsto y=\alpha/(1+\alpha)=1/(1+x^2)
\]

into the explicit Hausdorff witness-order barrier (6), or the joint conclusion that both Hausdorff and consecutive-Toeplitz witnesses escape with exponent `1/2` near a hypothetical positive threshold.

That search result is **not proof of historical novelty**. Priority remains unresolved.

---

## 9. What is not claimed

This note does **not** claim:

- that `Lambda>0`;
- RH or its negation;
- existence of a negative Hausdorff moment near the barrier;
- that every possible RH proof through Hausdorff moments must use a single raw boundary sign;
- historical novelty of Hermite collision scaling or Hausdorff criteria;
- settled literature priority for the cross-representation transport theorem.

It proves a conditional phase barrier and the resulting fixed-index positivity neighborhood below a hypothetical positive Newman threshold.