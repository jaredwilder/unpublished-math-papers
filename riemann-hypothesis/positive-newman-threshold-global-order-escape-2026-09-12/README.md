# A positive Newman threshold forces global determinant-order escape

**Author:** Jared Wilder  
**Date:** 2026-09-12  
**Status:** conditional cross-representation theorem; **not an RH proof**  
**Novelty boundary:** published de Bruijn–Newman high-zero theory and classical heat-equation multiple-zero/Hermite scaling are inputs. The global transport into the coefficient-Schur determinant-order barrier is new to this estate; literature priority remains unverified.

## 1. Headline theorem

Assume, for contradiction/analysis, that the de Bruijn–Newman constant satisfies

\[
\Lambda>0.
\]

At the threshold `t=Lambda`, list the **positive** multiple zeros of `H_Lambda` as

\[
0<x_1<\cdots<x_J,
\]

with finite multiplicities

\[
m_a\ge2.
\]

There are only finitely many such sites.

Let `H_m` denote the physicists' Hermite polynomial, and define

\[
S_m:=\sum_{\substack{\xi>0\\H_m(\xi)=0}}\xi,
\qquad
\mathcal S_\Lambda
:=\sum_{a=1}^J\frac{S_{m_a}}{x_a}.
\tag{1}
\]

Then `S_Lambda>0`. For

\[
\delta=\Lambda-t\downarrow0,
\]

the complete nonreal spectral defect in the coefficient/PF coordinate has total angular budget

\[
\boxed{
\Theta(t)
=
4\mathcal S_\Lambda\sqrt\delta
+O(\delta).
}
\tag{2}
\]

Consequently, for all sufficiently small `delta>0`, every consecutive coefficient Toeplitz/Schur minor `D_(r,k)(t)` remains positive for every shift `k` whenever

\[
r\Theta(t)<\frac\pi2.
\]

Thus **any negative consecutive minor**, if one exists at `t=Lambda-delta`, must have determinant order satisfying

\[
\boxed{
r
\ge
\frac{\pi}
{8\mathcal S_\Lambda\sqrt{\Lambda-t}}
\left(1+O(\sqrt{\Lambda-t})\right).
}
\tag{3}
\]

In particular,

\[
\boxed{
\text{if }\Lambda>0,\qquad
r_{\rm first\ possible\ sign\ failure}(t)\to\infty
\quad\text{at least on the scale }(\Lambda-t)^{-1/2}.
}
\tag{4}
\]

This is a **lower barrier** on the order of any negative determinant. It does not assert that a negative determinant appears at the barrier.

## 2. Why the threshold collision sites are finite and nonzero

Two facts remove the caveats present in a purely local collision model.

### 2.1 The origin cannot be a zero

For `u>=0`, each summand in the standard Xi kernel satisfies

\[
2\pi^2n^4e^{9u}-3\pi n^2e^{5u}
=
\pi n^2e^{5u}
\bigl(2\pi n^2e^{4u}-3\bigr)>0,
\]

because `2*pi-3>0`.

Hence

\[
\Phi(u)>0
\qquad(u\ge0),
\]

and therefore, for every real `t`,

\[
\boxed{
H_t(0)
=
\int_0^\infty e^{tu^2}\Phi(u)\,du
>0.
}
\tag{5}
\]

So no threshold multiple zero can occur at `x=0`. The spectral map `alpha=1/x^2` is therefore nonsingular at every collision site.

### 2.2 Only finitely many threshold zeros can be multiple

If `Lambda>0`, choose

\[
t_-:=\Lambda/2>0.
\]

Polymath 15's positive-time high-zero theorem gives one finite `X` such that throughout

\[
t\in[t_-,\Lambda]
\]

all zeros with sufficiently large `|Re z|` are real and lie in the isolated high-zero regime; in particular the high threshold zeros are simple. Earlier work of Ki–Kim–Lee also proves that for every fixed positive time all but finitely many zeros are real and simple.

Therefore every multiple zero of `H_Lambda` lies in a bounded real interval. Since `H_Lambda` is a nonzero entire function, a compact interval contains only finitely many zeros. Hence there are finitely many multiple sites.

Evenness gives the reflected sites `-x_a` with the same multiplicities, so it is enough to list the positive sites.

## 3. Every nonreal zero just below the threshold comes from those sites

The de Bruijn strip theorem gives a uniform bound on the imaginary parts of zeros on the compact positive-time interval `[t_-,Lambda]`. Together with the uniform high-zero theorem, all potentially nonreal zeros therefore live in one compact rectangle.

At `t=Lambda`, every zero is real.

Inside that compact rectangle there are finitely many threshold zeros. Split them into:

- simple real zeros;
- the finitely many multiple sites `±x_a`.

A simple threshold zero has a unique analytic zero branch in `t`. Reality symmetry

\[
H_t(\bar z)=\overline{H_t(z)}
\]

forces that unique branch to remain real for real `t` sufficiently close to `Lambda`.

Choose disjoint small neighborhoods around all threshold zeros. On the compact complement, `H_Lambda` is bounded away from zero, so joint continuity excludes new zeros there for `t` sufficiently close to `Lambda`.

Hence:

\[
\boxed{
\text{for }t<\Lambda\text{ sufficiently close to }\Lambda,
\text{ every nonreal zero belongs to a local cluster born at some }\pm x_a.
}
\tag{6}
\]

This is the step that globalizes the local collision theorem.

## 4. Universal Hermite unfolding at each site

At a positive multiple site `x_a` of multiplicity `m_a`, put

\[
\delta=\Lambda-t.
\]

The heat equation and local analyticity give the rescaled Hermite profile

\[
\delta^{-m_a/2}
H_{\Lambda-\delta}(x_a+\sqrt\delta\,v)
\longrightarrow
\frac{H_\Lambda^{(m_a)}(x_a)}{m_a!}
\,i^{m_a}H_{m_a}\!\left(\frac{v}{2i}\right)
\tag{7}
\]

uniformly on compact `v`-sets.

Thus, if `xi` runs over the zeros of the physicists' Hermite polynomial `H_(m_a)`, the local zeros satisfy

\[
x_{a,\xi}(\Lambda-\delta)
=
x_a+2i\xi\sqrt\delta+O(\delta).
\tag{8}
\]

The classical appearance of Hermite polynomials in heat-equation multiple-zero scaling is not claimed as new here.

## 5. Transport to the coefficient/PF spectral angles

The coefficient determinant coordinate identifies a zero `x` with

\[
\alpha=\frac1{x^2}.
\tag{9}
\]

Because the whole family is even, the clusters at `+x_a` and `-x_a` map to the same spectral cluster; they must **not** be double-counted.

For every positive Hermite zero `xi>0`, the conjugate local pair gives a conjugate pair of `alpha` parameters with angular defect

\[
\theta_{a,\xi}(\delta)
=
2\arctan\!\left(
\frac{2\xi\sqrt\delta}{x_a}
\right)
+O(\delta)
=
\frac{4\xi}{x_a}\sqrt\delta+O(\delta).
\tag{10}
\]

For odd multiplicity, the zero Hermite root contributes a real branch and no first-order angular defect.

By (6), all other zero parameters are positive real for `t` sufficiently close to `Lambda`. Therefore the **entire** nonreal angular budget is the finite sum

\[
\Theta(t)
:=
\sum_{a=1}^{J}
\sum_{\substack{\xi>0\\H_{m_a}(\xi)=0}}
\theta_{a,\xi}(\Lambda-t).
\tag{11}
\]

Using (10),

\[
\Theta(t)
=
4\sqrt\delta
\sum_{a=1}^J\frac{S_{m_a}}{x_a}
+O(\delta),
\]

which is (2).

## 6. Rectangular Schur phase theorem

For the coefficient sequence, the consecutive determinant has the rectangular-Schur form

\[
D_{r,k}=a_0^r s_{(r^k)}(\alpha).
\]

The previously released sparse angular theorem gives, when the nonreal spectral parameters occur in conjugate pairs and all remaining parameters are positive real,

\[
\boxed{
r\sum_\ell\theta_\ell<\frac\pi2
\quad\Longrightarrow\quad
D_{r,k}>0
\quad\text{for every }k.
}
\tag{12}
\]

Applying (12) to the complete budget (11) gives the global barrier (3).

The theorem is uniform in the shift `k`: no bounded determinant order can detect the hypothetical threshold arbitrarily close from below.

## 7. Relation to Positive-Time Simplicity

A separate finite-attainment lemma shows

\[
\Lambda>0
\quad\Longrightarrow\quad
H_\Lambda\text{ has at least one finite multiple real zero}.
\]

Equation (5) shows every such zero is nonzero. Thus the collision sites used in this theorem are not an extra speculative event: under `Lambda>0`, at least one necessarily exists.

Positive-Time Simplicity attacks the same hypothetical obstruction in the physical coordinate by trying to prove that **no** such multiple zero exists for `0<t<=0.2`.

The present theorem explains why a direct bounded-order determinant search is intrinsically badly conditioned near that same event: its possible sign witness is forced to infinity in determinant order.

## 8. External literature boundary

The proof uses published/classical ingredients:

- de Bruijn–Newman threshold and strip theory;
- positive-time high-zero localization/simplicity from Ki–Kim–Lee and Polymath 15;
- classical Hermite scaling of multiple zeros under the linear heat equation.

Recent work also studies Toeplitz/Pólya-frequency properties of the **de Bruijn–Newman kernel** itself. That is a different Toeplitz object from the coefficient-Schur minors used here.

A targeted search did not locate the exact global theorem (3), which transports the complete finite threshold collision set into a coefficient-Schur determinant-order escape law. This negative search is not proof of historical novelty, so priority remains unresolved.

## 9. What is not claimed

This note does **not** claim:

- `Lambda>0`;
- RH or its negation;
- existence of a negative determinant after the barrier;
- that every threshold multiple zero is double;
- that the de Bruijn–Newman kernel's PF order is the same object as the coefficient Toeplitz hierarchy;
- settled literature priority.

It proves a conditional global structural consequence: **if a positive Newman threshold existed, every coefficient-determinant sign witness would be pushed to unbounded order as the threshold is approached from below, with an explicit square-root lower barrier determined by the finitely many threshold collision sites.**
