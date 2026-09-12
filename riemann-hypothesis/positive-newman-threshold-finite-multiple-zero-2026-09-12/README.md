# A positive de Bruijn–Newman threshold is attained at a finite multiple zero

**Author:** Jared Wilder  
**Date:** 2026-09-12  
**Status:** exact reduction from published high-zero / strip theorems; **not an RH proof**  
**Novelty:** not asserted. The ingredients are classical/published; this note records the compact reduction explicitly because it is load-bearing for the PTS program.

## 1. Statement

Let

\[
H_t(z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du
\]

be the de Bruijn–Newman heat deformation, and let `Lambda` be the de Bruijn–Newman constant:

\[
H_t\text{ has only real zeros}
\quad\Longleftrightarrow\quad
t\ge\Lambda.
\]

Then:

> **Finite-attainment lemma.** If `Lambda>0`, there exists a finite real number `x_*` such that
> \[
> \boxed{
> H_\Lambda(x_*)=H_\Lambda'(x_*)=0.
> }
> \tag{1}
> \]

Thus a hypothetical positive threshold cannot be lost only through nonreal zeros escaping to spatial infinity. It must be attained by a finite multiple real zero.

## 2. Published inputs

The proof uses three standard/published facts.

### A. Threshold property

By de Bruijn and Newman, `H_t` has only real zeros exactly for `t>=Lambda`.

### B. Uniform high-zero reality for positive time

Polymath 15, Theorem 1.5, proves that for `0<t<=1/2`, once

\[
x\ge \exp(C/t)
\]

for a sufficiently large absolute `C`, every zero `H_t(x+iy)=0` is real; the theorem moreover localizes the high zeros sharply. Earlier work of Ki–Kim–Lee also proves that for each fixed positive time all but finitely many zeros are real and simple.

For a compact positive-time interval `[t_-,t_+]`, the Polymath threshold is uniform because

\[
\exp(C/t)\le \exp(C/t_-).
\]

### C. Uniform zero strip

De Bruijn's strip theorem propagates the known initial critical-strip bound into a bounded horizontal strip for the heat-deformed functions. In particular, on any compact positive-time interval relevant here, the imaginary parts of zeros are uniformly bounded.

No RH assumption is used in these inputs.

## 3. Proof

Assume

\[
\Lambda>0.
\]

Set

\[
t_-:=\Lambda/2>0.
\]

Because the unconditional upper bounds give `Lambda<1/2`, the interval `[t_-,Lambda]` lies inside the positive-time regime where the published high-zero estimates apply.

Take any sequence

\[
t_n\uparrow\Lambda,
\qquad
t_n<\Lambda.
\]

By the defining property of `Lambda`, each `H_(t_n)` has at least one nonreal zero; choose one and call it `z_n`.

### Real parts cannot escape

For every `t in [t_-,Lambda]`, Polymath 15 gives reality of every zero once

\[
|\Re z|\ge X_\Lambda
\]

for one finite `X_Lambda` depending only on `t_-` (evenness handles the negative side).

Since each `z_n` is nonreal,

\[
|\Re z_n|<X_\Lambda.
\tag{2}
\]

### Imaginary parts cannot escape

The de Bruijn strip theorem gives one finite bound `Y_Lambda` on the imaginary parts throughout the same compact time range:

\[
|\Im z_n|\le Y_\Lambda.
\tag{3}
\]

Hence the sequence `(z_n)` lies in a fixed compact rectangle. Passing to a subsequence,

\[
z_n\to z_*
\]

for some finite complex `z_*`.

Joint continuity/analyticity of `(t,z) -> H_t(z)` gives

\[
H_\Lambda(z_*)=0.
\tag{4}
\]

At `t=Lambda`, every zero is real by the threshold property, so

\[
z_*=x_*\in\mathbb R.
\tag{5}
\]

### The limiting zero cannot be simple

Suppose for contradiction that

\[
H_\Lambda'(x_*)\ne0.
\]

The analytic implicit-function theorem then gives a unique zero branch `z(t)` in a neighborhood of `(Lambda,x_*)`.

For real `t`, the functions satisfy the reality symmetry

\[
H_t(\bar z)=\overline{H_t(z)}.
\]

Therefore `\overline{z(t)}` is also a zero branch through the same point. By local uniqueness,

\[
z(t)=\overline{z(t)},
\]

so the branch is real for real `t` near `Lambda`.

But the selected nonreal zeros `z_n` converge to `x_*`, and for all sufficiently large `n` they lie in that uniqueness neighborhood. Contradiction.

Therefore

\[
H_\Lambda'(x_*)=0.
\]

Together with (4)-(5), this proves (1).

QED.

## 4. Consequence for Positive-Time Simplicity

Define the Positive-Time Simplicity statement

\[
\boxed{
0<t\le0.2,\quad H_t(x)=0
\Longrightarrow
H_t'(x)\ne0
\quad\text{for every real }x.
}
\tag{PTS}
\]

The current unconditional literature gives

\[
0\le\Lambda\le0.2.
\]

If PTS held but `Lambda>0`, the finite-attainment lemma would produce a multiple real zero at

\[
t=\Lambda\in(0,0.2],
\]

contradicting PTS.

Hence PTS would imply

\[
\Lambda\le0.
\]

Together with Rodgers–Tao's `Lambda>=0`, this gives

\[
\Lambda=0,
\]

and therefore RH.

So, under the published upper/lower bounds,

\[
\boxed{
\mathrm{PTS}\Longrightarrow\mathrm{RH}.
}
\tag{6}
\]

The missing Millennium-strength theorem is PTS itself, **not** the finite-attainment reduction.

## 5. Relation to the collision-order results

This reduction justifies taking finite multiple zeros at a hypothetical positive threshold seriously.

Separate notes in this repository show that:

- a generic double threshold collision generates a determinant-order positivity barrier of scale `(Lambda-t)^(-1/2)`;
- more generally, every finite-multiplicity threshold collision has a Hermite local profile and the same square-root determinant-order escape exponent, with a multiplicity-dependent Hermite constant.

Those are conditional transport theorems. The present note supplies the finite-attainment bridge from a hypothetical `Lambda>0` to at least one finite multiple zero.

It does **not** prove that the multiplicity is two, that it is isolated, or that no simultaneous collision occurs elsewhere.

## 6. Literature / novelty boundary

This note does not claim a new theorem of the scale of the published de Bruijn–Newman results. Its inputs are explicitly credited:

- de Bruijn / Newman: threshold and strip machinery;
- Ki–Kim–Lee: positive-time high-zero reality and simplicity;
- D.H.J. Polymath: effective uniform high-zero localization for positive `t`;
- Rodgers–Tao and later upper-bound work: current bounds on `Lambda`.

A targeted search did not immediately locate this compactness-plus-implicit-function reduction stated in exactly this form, but that is not a priority claim. The value of the note is to make the PTS implication chain explicit and auditable.

## 7. What is not claimed

This note does **not** claim:

- PTS;
- RH;
- `Lambda>0`;
- a new upper or lower bound for `Lambda`;
- that a threshold multiple zero must be a double zero;
- settled historical novelty.
