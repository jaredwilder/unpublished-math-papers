# Finite-multiplicity Newman collisions and the Hermite determinant-order barrier

**Author:** Jared Wilder  
**Date:** 2026-09-12  
**Status:** conditional local transport theorem; **not an RH proof**  
**Novelty boundary:** Hermite scaling of multiple zeros for the heat equation is classical. The transport of that scaling into the rectangular-Schur / consecutive-Toeplitz order barrier is the new-to-this-estate synthesis; literature priority remains unverified.

## 1. Statement

Let `H_t(x)` be real analytic near `(Lambda,x_*)`, solve

\[
\partial_t H_t=-\partial_x^2H_t,
\tag{1}
\]

and suppose that at `t=Lambda` the point `x_* != 0` is a zero of finite multiplicity `m>=2`:

\[
\partial_x^jH_\Lambda(x_*)=0
\quad(0\le j<m),
\qquad
\partial_x^mH_\Lambda(x_*)\ne0.
\tag{2}
\]

Write

\[
\delta=\Lambda-t>0.
\]

Let `H_m` denote the physicists' Hermite polynomial, whose real simple zeros are

\[
\xi_{m,1}<\cdots<\xi_{m,m}.
\]

Then the local zero cluster of `H_{Lambda-delta}` has the universal scaling

\[
\boxed{
x_j(\Lambda-\delta)
=x_*+2i\xi_{m,j}\sqrt\delta+O(\delta),
\qquad 1\le j\le m.
}
\tag{3}
\]

For odd `m`, one Hermite zero is zero and the corresponding local branch remains real to leading order; the remaining roots occur in conjugate pairs.

Now map the zeros into the determinant spectral coordinate

\[
\alpha=\frac1{x^2}.
\tag{4}
\]

For every positive Hermite zero `xi>0`, the associated conjugate `alpha` pair has angular defect

\[
\boxed{
\theta_\xi(\delta)
=2\arctan\!\left(\frac{2\xi\sqrt\delta}{|x_*|}\right)
+O(\delta).
}
\tag{5}
\]

Let

\[
S_m:=\sum_{\xi_{m,j}>0}\xi_{m,j}.
\tag{6}
\]

Assume that, in the determinant/Schur representation under consideration, every spectral parameter outside this local cluster is positive real. Then the sparse angular phase theorem implies that every consecutive determinant of order `r` remains positive whenever

\[
r\sum_{\xi_{m,j}>0}\theta_{\xi_{m,j}}(\delta)<\frac\pi2.
\tag{7}
\]

Consequently any determinant order at which this collision cluster can possibly force a sign failure must obey the asymptotic lower barrier

\[
\boxed{
r
\ge
\frac{\pi|x_*|}
{8S_m\sqrt{\Lambda-t}}
\left(1+O(\sqrt{\Lambda-t})\right).
}
\tag{8}
\]

In particular, for **every fixed finite multiplicity** `m>=2`,

\[
\boxed{
r_{\rm barrier}(t)\asymp(\Lambda-t)^{-1/2}.}
\tag{9}
\]

Multiplicity changes the Hermite constant, not the square-root exponent.

## 2. Universal Hermite local profile

Set

\[
a_m:=\frac{\partial_x^mH_\Lambda(x_*)}{m!}\ne0.
\]

Consider the rescaled local function

\[
F_\delta(v)
:=\delta^{-m/2}
H_{\Lambda-\delta}(x_*+\sqrt\delta\,v).
\tag{10}
\]

Analyticity and the heat equation give

\[
\partial_t^pH=(-1)^p\partial_x^{2p}H.
\]

In the joint Taylor expansion at `(Lambda,x_*)`, all terms with total parabolic degree

\[
2p+q<m
\]

vanish because of the multiplicity assumption (2). The first surviving layer is `2p+q=m`. Therefore, uniformly on compact `v`-sets,

\[
F_\delta(v)
\longrightarrow
a_m Q_m(v),
\tag{11}
\]

where

\[
Q_m(v)
=
\sum_{p=0}^{\lfloor m/2\rfloor}
\frac{m!}{p!(m-2p)!}
v^{m-2p}.
\tag{12}
\]

The polynomial is exactly an imaginary-axis Hermite transform:

\[
\boxed{
Q_m(v)=i^m H_m\!\left(\frac{v}{2i}\right).
}
\tag{13}
\]

Since the Hermite zeros are real and simple, the zeros of `Q_m` are the simple imaginary points

\[
v_j=2i\xi_{m,j}.
\tag{14}
\]

The convergence in (11), together with simple-root perturbation / Hurwitz-Rouche arguments, gives (3). The next parabolic layer is higher by one half-power, so the correction in physical `x` is `O(delta)`.

### Classical boundary

The appearance of Hermite polynomials in the local classification of multiple zeros of the one-dimensional heat equation is classical zero-set theory. This note does **not** claim that phenomenon as new.

## 3. Transport into the PF / Schur coordinate

A zero `x` of the heat-flowed entire function corresponds, in the determinant product coordinate used by this program, to

\[
\alpha=\frac1{x^2}.
\]

For a positive Hermite zero `xi`, (3) gives the conjugate pair

\[
x_\pm
=x_*\pm2i\xi\sqrt\delta+O(\delta).
\]

Squaring and inverting rotates the positive baseline `1/x_*^2` by twice the argument of `x_*/x_\pm`. Hence

\[
|\arg\alpha_\pm|
=
2\arctan\left(\frac{2\xi\sqrt\delta}{|x_*|}\right)
+O(\delta),
\]

which is (5).

Summing over the positive Hermite zeros,

\[
\sum_{\xi>0}\theta_\xi(\delta)
=
\frac{4S_m}{|x_*|}\sqrt\delta
+O(\delta).
\tag{15}
\]

## 4. Schur phase budget and the order barrier

For a rectangular Schur determinant of order `r`, the sparse angular theorem states that if the non-real spectral parameters occur in conjugate pairs with positive angular defects `theta_l`, while all remaining parameters are positive real, then

\[
\boxed{
r\sum_l\theta_l<\frac\pi2
\quad\Longrightarrow\quad
D_{r,k}>0
\quad\text{for every shift }k.
}
\tag{16}
\]

Insert (15). Any order capable of a sign failure caused by the local collision cluster must satisfy

\[
r\left(
\frac{4S_m}{|x_*|}\sqrt\delta+O(\delta)
\right)
\ge\frac\pi2.
\]

Solving gives (8).

This is a **lower barrier**, not an existence theorem for a negative determinant. Crossing the barrier only removes the phase-budget guarantee; it does not force sign loss.

## 5. Double collision recovered

For `m=2`,

\[
H_2(x)=4x^2-2,
\]

whose positive zero is

\[
\xi=\frac1{\sqrt2}.
\]

Thus `S_2=1/sqrt(2)`, and (8) becomes

\[
r
\ge
\frac{\pi|x_*|}
{4\sqrt{2(\Lambda-t)}}
\left(1+O(\sqrt{\Lambda-t})\right),
\]

which is exactly the previously released generic-double-collision barrier.

So that theorem is the `m=2` member of the finite-multiplicity Hermite family.

## 6. Examples of the Hermite constant

The first few positive-root sums are:

- `m=2`: `S_2 = 1/sqrt(2)`;
- `m=3`: one positive Hermite root `sqrt(3/2)`;
- `m=4`: two positive Hermite roots;
- in general `S_m` is the sum of the positive zeros of the physicists' `H_m`.

The exact value of `S_m` changes the constant in (8), but for every fixed `m` the divergence exponent remains `1/2`.

## 7. Interpretation

A finite physical-space multiple collision does **not** stay finite-complexity in the determinant coordinate as the threshold is approached.

The heat equation first resolves the collision into a universal Hermite micro-profile at scale `sqrt(Lambda-t)`. The spectral map then turns those imaginary displacements into angular defects of the same scale. Rectangular Schur positivity can tolerate total phase only of order `1/r`, so the determinant order required even to *permit* sign detection diverges like

\[
(\Lambda-t)^{-1/2}.
\]

This gives a multiplicity-robust explanation for determinant-order escape near a finite Newman collision.

## 8. Literature / novelty boundary

Two layers must be kept separate.

**Classical layer.** Hermite polynomials govern the rescaled local structure of multiple zeros for the linear heat equation; this belongs to classical Sturm/heat-equation zero-set theory and later parabolic zero-set literature.

**Estate synthesis.** A targeted search did not locate the exact theorem transporting the Hermite collision profile through `alpha=1/x^2` into the rectangular-Schur angular budget and the explicit order barrier (8). That negative search is not proof of novelty, so priority is left unresolved.

## 9. What is not claimed

This note does **not** claim:

- that `Lambda>0`;
- RH or its negation;
- that every threshold collision has finite multiplicity;
- that this local cluster is the only possible non-real cluster without the explicit hypothesis above;
- existence of a negative determinant at the barrier;
- historical novelty of Hermite multiple-zero scaling;
- settled literature priority for the transport theorem.

It records an exact finite-multiplicity transport law and its universal determinant-order escape exponent.
