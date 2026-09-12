# Generic Newman collision implies a diverging determinant-order barrier

**Author:** Jared Wilder  
**Date:** 2026-09-12  
**Status:** conditional local cross-representation theorem; **not an RH proof**  
**Novelty:** targeted search found adjacent de Bruijn–Newman / Toeplitz work but no exact collision-to-Schur-order statement; historical priority remains unverified

## 1. Statement and an important scope correction

Assume a **generic double collision** at a hypothetical positive de Bruijn–Newman threshold `Lambda`:

\[
H_\Lambda(x_*)=0,
\qquad
H_\Lambda'(x_*)=0,
\qquad
H_\Lambda''(x_*)\ne0,
\qquad
x_*\ne0.
\tag{1}
\]

Let

\[
\delta=\Lambda-t>0.
\]

Then the colliding zeros just below the threshold leave the real axis with square-root scale

\[
\boxed{
 x_\pm(t)
 =x_*\pm i\sqrt{2\delta}+O(\delta).
}
\tag{2}
\]

Under the Xi determinant spectral transform, this produces one conjugate pair of PF/Schur parameters whose angular defect satisfies

\[
\boxed{
|\theta(t)|
=2\arctan\frac{\sqrt{2\delta}}{|x_*|}
+O(\delta/|x_*|^2).
}
\tag{3}
\]

The existing single-pair Schur phase theorem guarantees positivity of every consecutive minor of order `r` while

\[
r|\theta|<\frac\pi2.
\]

Therefore any determinant order at which this pair can possibly force a sign failure must satisfy the lower barrier

\[
\boxed{
r\ge
\frac{\pi}{2|\theta(t)|}.
}
\tag{4}
\]

To leading collision order,

\[
\boxed{
r\gtrsim
\frac{\pi}
{4\arctan(\sqrt{2(\Lambda-t)}/|x_*|)}
\sim
\frac{\pi|x_*|}
{4\sqrt{2(\Lambda-t)}}.
}
\tag{5}
\]

### Correction to the internal Pass-4 wording

The archive called the right side of (5) the asymptotic of the **actual first detector order**. That is stronger than the argument proves.

The Schur phase theorem gives a **forbidden-order region**: below the barrier, the conjugate pair cannot make the determinant negative. It does not prove that a negative determinant appears as soon as the barrier is crossed.

Accordingly, this public note records the rigorous conclusion as

\[
\boxed{
\text{actual first negative-minor order, if any}
\ \ge\
\text{angular-certification barrier}
\asymp(\Lambda-t)^{-1/2}.
}
\tag{6}
\]

That distinction is load-bearing.

## 2. Local collision law

The heat deformation satisfies

\[
\partial_tH=-H_{xx}.
\tag{7}
\]

Write

\[
A=H_\Lambda''(x_*)\ne0.
\]

Taylor expansion at `(Lambda,x_*)` gives

\[
H_{\Lambda-\delta}(x_*+u)
=A\delta+\frac A2u^2
+O(\delta|u|+|u|^3+\delta^2).
\tag{8}
\]

At leading order the zero equation is

\[
\delta+\frac12u^2=0,
\]

so

\[
u=\pm i\sqrt{2\delta}.
\]

Standard local perturbation of the generic quadratic collision yields (2).

The striking feature is that the leading square-root constant is independent of the nonzero value of `A`; `A` cancels from the quadratic balance.

## 3. Transport to the determinant spectral parameter

Use the determinant transform

\[
\mathcal G_t(z)=H_t(i\sqrt z).
\tag{9}
\]

A zero `x` of `H_t` corresponds to

\[
z=-x^2.
\]

Writing

\[
\mathcal G_t(z)=a_0\prod_j(1+\alpha_jz),
\]

the corresponding spectral parameter is

\[
\boxed{\alpha=\frac1{x^2}.}
\tag{10}
\]

For the conjugate pair

\[
x=x_*\pm i\eta,
\qquad
\eta=\sqrt{2\delta}+O(\delta),
\]

the parameters `alpha` are conjugate and approach the positive real axis. Their absolute angular defect is

\[
|\arg\alpha|
=2\left|\arctan\frac{\eta}{x_*}\right|,
\]

which gives (3).

## 4. Schur phase barrier

For a rectangular Schur determinant with exactly one conjugate parameter pair of angular defect `theta` and all other parameters positive real, the previously extracted sparse-phase theorem gives

\[
\boxed{
r|\theta|<\frac\pi2
\quad\Longrightarrow\quad
D_{r,k}>0
\quad\text{for every }k.
}
\tag{11}
\]

Hence the pair is **provably invisible to determinant sign** below

\[
r_{\rm barrier}(t)
:=\frac{\pi}{2|\theta(t)|}.
\tag{12}
\]

Using (3),

\[
r_{\rm barrier}(t)
\sim
\frac{\pi|x_*|}{4\sqrt{2(\Lambda-t)}}.
\tag{13}
\]

Thus

\[
\boxed{
r_{\rm barrier}(t)\to\infty
\qquad(t\uparrow\Lambda).}
\]

## 5. Interpretation: finite collision, infinite-order encoding

PTS sees a hypothetical positive Newman obstruction as a **finite collision at finite physical location** `x_*`.

The Schur determinant representation sees the same local event as a conjugate spectral pair whose angle tends to zero. The phase theorem then pushes every possible determinant sign witness to unbounded order as the collision is approached.

This supplies a concrete mathematical mechanism behind the estate's earlier “no bounded first determinant nucleation” phenomenon:

> a finite physical-space obstruction can migrate to the determinant boundary at infinity purely because of the spectral coordinate map.

A natural double-scaling variable is

\[
\chi
=\frac{r\sqrt{\Lambda-t}}{|x_*|}.
\tag{14}
\]

The **positivity barrier** occurs at

\[
\chi\approx\frac{\pi}{4\sqrt2}.
\]

Again, that is a barrier below which negativity is excluded, not a theorem that negativity occurs at that constant.

## 6. Strategic consequence

For the narrow task “exclude a positive de Bruijn–Newman threshold,” the physical collision coordinate is better conditioned than a direct search for a negative high-order determinant near the transition.

This does not weaken the determinant route as a global RH program. It says the two representations should specialize:

- PTS / heat-flow work should attack finite collision and transversality directly;
- determinant work should attack its native rational-orbit / curvature geometry;
- neither route should recreate the other's badly conditioned coordinate unless a theorem requires it.

## 7. Literature boundary

Current literature contains substantial work on both de Bruijn–Newman heat flow and Toeplitz/Pólya-frequency phenomena. A targeted search for a published theorem explicitly transporting a generic Newman double collision into the Schur determinant-order barrier (13) did not locate an exact counterpart.

That search is not exhaustive, so novelty remains **unverified**.

## 8. What is not claimed

This note does **not** claim:

- `Lambda>0`;
- RH or its negation;
- existence of an actual negative determinant after the barrier;
- that every Newman collision is generic;
- the same exponent for higher-multiplicity collisions;
- settled literature novelty.

It proves a conditional local transport law and, crucially, a diverging **lower barrier** on determinant order near a generic double collision.
