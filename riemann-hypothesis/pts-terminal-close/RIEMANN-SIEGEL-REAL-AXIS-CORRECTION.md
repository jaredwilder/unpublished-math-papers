# Riemann–Siegel real-axis correction and derivative adapter

**Author:** Jared Wilder  
**Source anchor:** D.H.J. Polymath, arXiv:1904.12438, Theorem 1.3 / Eq. (14) and surrounding definitions

This note preserves a source-faithfulness correction recovered from the August 2026 PTS packet.

## 1. Correction to the earlier internal packet

An earlier internal proof packet incorrectly replaced the real-axis main term by

\[
f_t=(1+\gamma_t)S_t.
\]

That is not what the cited Polymath formula says.

Theorem 1.3, Eq. (14), has the form

\[
f_t(x+iy)
=
\sum_{n=1}^N\frac{b_n^t}{n^{s_*}}
+
\gamma
\sum_{n=1}^N
n^y\frac{b_n^t}{n^{\overline{s_*}+\kappa}}.
\]

At `y=0`, one has `kappa=0`, so if

\[
S_t(x)=\sum_{n\le N}b_n^t n^{-s_*(x)},
\]

then the correct real-axis expression is

\[
\boxed{f_t(x)=S_t(x)+\gamma_t(x)\overline{S_t(x)}.}
\]

The earlier retraction of the real-axis branch based on `(1+gamma)S` is therefore itself retracted.

## 2. Normalization correction

The exact `M_0` normalization used by the source packet contains the factor

\[
\boxed{\frac18\frac{s(s-1)}2}
\]

rather than merely `1/8 * s(s-1)`.

The corrected asymptotic factor is

\[
M_0(s)
=
\frac18\frac{s(s-1)}2\pi^{-s/2}\sqrt{2\pi}
\exp\left[
\left(\frac s2-\frac12\right)\Log\frac s2-\frac s2
\right].
\]

## 3. Real-axis derivative formulas

Let

\[
a=\frac{1-ix}{2},
\qquad
s_*=a+\frac t2\alpha(a).
\]

Then

\[
\alpha'(s)
=-\frac1{2s^2}-\frac1{(s-1)^2}+\frac1{2s},
\]

and

\[
\boxed{
s_*'
=-\frac i2\left(1+\frac t2\alpha'(a)\right).
}
\]

Therefore

\[
\boxed{
S_t'(x)
=-s_*'\sum_{n\le N}(\log n)b_n^tn^{-s_*}.
}
\]

If

\[
\beta_t(s)=\frac{M_t'(s)}{M_t(s)}
=\alpha(s)+\frac t2\alpha(s)\alpha'(s),
\]

then

\[
\boxed{
\gamma_t'(x)
=\frac{i\gamma_t(x)}2
\left[
\beta_t(\bar a)+\beta_t(a)
\right].
}
\]

Consequently, on intervals where `N` is constant,

\[
\boxed{
f_t'
=S_t'+\gamma_t'\overline{S_t}
+\gamma_t\overline{S_t'}.
}
\]

Any rigorous implementation must split boxes at the source formula's `N`-jump locations before differentiating this fixed-`N` expression.

## 4. High-x simplicity use

Suppose the normalized target has

\[
G_t=f_t+E_t
\]

on a complex disk of radius `rho`, with a rigorous value-error bound

\[
|E_t|\le\varepsilon_0.
\]

Cauchy's estimate supplies

\[
|E_t'|\le \varepsilon_1:=\varepsilon_0/\rho
\]

(or any sharper certified derivative error).

A double real zero would force both

\[
|f_t|\le\varepsilon_0,
\qquad
|f_t'|\le\varepsilon_1.
\]

Thus the disjunction

\[
\boxed{
|f_t|>\varepsilon_0
\quad\text{or}\quad
|f_t'|>\varepsilon_1
}
\]

uniformly on a box is a rigorous high-x transversality certificate.

## 5. Scope

This note corrects the source adapter and restores a valid high-x proof branch. It does not by itself supply the global covering argument required for PTS; it supplies the correct real-axis formula and derivative machinery that such a covering would use.
