# Positive de Bruijn–Newman threshold implies a finite multiple real zero

**Author of this reduction:** Jared Wilder  
**External inputs:** the classical de Bruijn–Newman threshold framework, Rodgers–Tao, Platt–Trudgian, and the uniform positive-time high-zero localization/simplicity theorem from Polymath 15.

## Theorem

Assume the de Bruijn–Newman constant satisfies

\[
\Lambda>0.
\]

Then there exists a finite real number `x_*` such that

\[
\boxed{
H_\Lambda(x_*)=H_\Lambda'(x_*)=0.
}
\]

In other words, a positive threshold must be attained at a finite multiple real zero.

## Proof

Set

\[
t_- = \Lambda/2>0.
\]

The positive-time high-zero theorem used by the campaign gives uniform realness and isolation/simplicity of all sufficiently high zeros for times in a compact interval bounded away from zero. Hence there exists a finite `X_Λ` such that every zero with

\[
|\Re z|\ge X_\Lambda
\]

is real and simple uniformly for

\[
t\in[t_-,\Lambda].
\]

Choose any sequence

\[
t_n\uparrow\Lambda,\qquad t_n<\Lambda.
\]

By definition of the threshold, each `H_{t_n}` has at least one nonreal zero `z_n`.

The uniform high-zero statement bounds the real parts of all such nonreal zeros, while the de Bruijn strip bound controls their imaginary parts on the same compact time interval. Therefore a subsequence satisfies

\[
z_n\to z_*
\]

for some finite complex `z_*`.

Continuity in `(t,z)` gives

\[
H_\Lambda(z_*)=0.
\]

At time `t=Λ`, all zeros are real, so

\[
z_*=x_*\in\mathbb R.
\]

Suppose instead that

\[
H_\Lambda'(x_*)\ne0.
\]

Then the analytic implicit-function theorem gives a unique local zero branch `z(t)` through `(Λ,x_*)`.

For real `t`, the coefficients are real on the real axis, so complex conjugation sends a zero branch to a zero branch. Local uniqueness forces

\[
z(t)=\overline{z(t)},
\]

hence the branch is real for all real `t` sufficiently near `Λ`.

But this contradicts the chosen sequence of nonreal zeros

\[
z_n\to x_*.
\]

Therefore

\[
\boxed{H_\Lambda'(x_*)=0.}
\]

QED.

## PTS consequence

The frozen Positive-Time Simplicity target is

\[
\forall t\in(0,0.2],\ \forall x\in\mathbb R,
\qquad
H_t(x)=0\Longrightarrow H_t'(x)\ne0.
\]

If PTS holds and `Λ>0`, the theorem above produces a multiple real zero at `t=Λ`.

The published upper bound used by the campaign places

\[
0<\Lambda\le0.2,
\]

so this contradicts PTS.

Thus PTS implies

\[
\Lambda\le0.
\]

Together with the published lower bound

\[
\Lambda\ge0,
\]

one obtains

\[
\boxed{\Lambda=0},
\]

which is equivalent to RH in the de Bruijn–Newman framework.

Therefore

\[
\boxed{
\mathrm{PTS}\Longrightarrow\mathrm{RH}.
}
\]

This note isolates the reduction only. It does not claim PTS itself is proved.
