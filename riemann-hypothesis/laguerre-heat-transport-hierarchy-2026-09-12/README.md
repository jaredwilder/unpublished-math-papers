# Laguerre heat-transport hierarchy for de Bruijn–Newman / PTS certification

**Author:** Jared Wilder  
**Date:** 2026-09-12  
**Status:** exact differential identity / certification synthesis; **not an RH proof**  
**Novelty:** the first Laguerre difference and its use for the de Bruijn–Newman family are classical. No novelty is claimed for the individual ingredients. Historical priority for the all-order transport packaging is **unverified**.

## 1. Classical boundary first

For a real function `H`, the first Laguerre difference is

\[
\mathcal L_1[H]
:=H_x^2-HH_{xx}.
\tag{1}
\]

For the de Bruijn–Newman family this is not new machinery. Csordas, Ruttan and Varga used precisely this Laguerre difference in their 1991 work on lower bounds for the de Bruijn–Newman constant.

The present note does **not** claim (1) as an estate invention.

What the estate's PTS machinery suggests is to put (1), its higher-derivative analogues, and the transversality energy into one exact heat-transport hierarchy.

---

## 2. Backward heat convention

Let

\[
H=H(t,x)
\]

be a sufficiently smooth real solution of

\[
\boxed{H_t=-H_{xx}.}
\tag{2}
\]

This is the convention of the de Bruijn–Newman family used in the estate.

Write

\[
H_n:=\partial_x^nH.
\]

Then every derivative satisfies the same equation:

\[
\partial_tH_n=-H_{n+2}.
\tag{3}
\]

Define the parabolic transport operator

\[
\boxed{\mathscr P:=\partial_t+\partial_x^2.}
\tag{4}
\]

---

## 3. Square hierarchy

For

\[
Q_n:=H_n^2,
\qquad n\ge0,
\]

direct differentiation gives

\[
\partial_tQ_n=-2H_nH_{n+2},
\]

while

\[
\partial_x^2Q_n
=2H_{n+1}^2+2H_nH_{n+2}.
\]

Hence

\[
\boxed{
\mathscr P Q_n
=2Q_{n+1}.
}
\tag{5}
\]

This already upgrades the PTS transversality quantity

\[
Q(t,x)=H^2+H_x^2
=Q_0+Q_1.
\]

Indeed,

\[
\boxed{
\mathscr P(H^2+\lambda H_x^2)
=2H_x^2+2\lambda H_{xx}^2
\ge0
\qquad(\lambda\ge0).
}
\tag{6}
\]

So the zero-independent box certificate `H^2+lambda H_x^2` is not merely an algebraic norm: it is a nonnegative parabolic subsolution for the transport operator (4).

This identity alone does **not** prove it has a positive global lower bound.

---

## 4. All-order Laguerre ladder

For `n>=1`, define the adjacent-derivative Laguerre differences

\[
\boxed{
\mathcal L_n
:=
H_n^2-H_{n-1}H_{n+1}.
}
\tag{7}
\]

Thus

\[
\mathcal L_1=H_x^2-HH_{xx}.
\]

### Theorem — heat transport of Laguerre differences

For every `n>=1`,

\[
\boxed{
\mathscr P\mathcal L_n
=2\mathcal L_{n+1}.
}
\tag{8}
\]

### Proof

First,

\[
\partial_t\mathcal L_n
=
-2H_nH_{n+2}
+H_{n+1}^2
+H_{n-1}H_{n+3}.
\tag{9}
\]

Second,

\[
\partial_x^2\mathcal L_n
=
H_{n+1}^2
-H_{n-1}H_{n+3}.
\tag{10}
\]

Adding (9) and (10),

\[
\mathscr P\mathcal L_n
=
2H_{n+1}^2-2H_nH_{n+2}
=2\mathcal L_{n+1}.
\]

QED.

---

## 5. Generating-function form

The ladder (5) can be compressed into one transport equation.

Whenever the derivative-energy series converges, set

\[
\mathcal E(\sigma;t,x)
:=
\sum_{n=0}^{\infty}
\frac{\sigma^n}{n!}H_n(t,x)^2.
\tag{11}
\]

Then termwise application of (5) gives

\[
\boxed{
\mathscr P\mathcal E
=2\,\partial_\sigma\mathcal E.
}
\tag{12}
\]

Likewise define

\[
\mathcal G(\sigma;t,x)
:=
\sum_{n=1}^{\infty}
\frac{\sigma^{n-1}}{(n-1)!}\mathcal L_n(t,x).
\tag{13}
\]

Then (8) gives

\[
\boxed{
\mathscr P\mathcal G
=2\,\partial_\sigma\mathcal G.
}
\tag{14}
\]

Thus derivative order becomes a literal transport coordinate for both square energies and Laguerre differences.

---

## 6. Real-rooted phase interpretation

If, at a fixed `t`, `H_t` lies in an appropriate Laguerre–Pólya / real-rooted class for which the generalized Laguerre inequalities apply, then

\[
\mathcal L_n(t,x)\ge0
\]

for the relevant derivative orders and real `x`.

Equation (8) then reads

\[
\mathscr P\mathcal L_n\ge0.
\tag{15}
\]

This does **not** by itself propagate real-rootedness backward in time. The estate already has an elementary counterexample to that kind of Rolle-based shortcut.

What (8) does provide is a structured hierarchy of local certification quantities rather than a collection of unrelated derivative tests.

---

## 7. PTS interpretation

Positive-Time Simplicity asks for

\[
H_t(x)=0\Longrightarrow H_x(t,x)\ne0
\qquad(0<t\le0.2).
\]

At a real zero,

\[
\boxed{
\mathcal L_1(t,x)=H_x(t,x)^2.
}
\tag{16}
\]

Therefore any rigorous lower bound

\[
\mathcal L_1>0
\]

on a spacetime box certifies simplicity for every zero in that box.

The PTS packet already used this first-rung observation as an alternate interval certifier. The new organizational point is that its evolution is coupled exactly to the next rung:

\[
\boxed{
(\partial_t+\partial_x^2)\mathcal L_1
=2\mathcal L_2.
}
\tag{17}
\]

and recursively to every higher rung.

This suggests a rigorous certification strategy in which higher Laguerre inequalities are used as signed source terms controlling lower-order witnesses. Whether that produces a cheaper or global PTS proof is an **open engineering/analysis question**, not a theorem claimed here.

---

## 8. Why this is not being sold as novelty

The surrounding literature is old and directly relevant:

- classical Laguerre inequalities and the Laguerre–Pólya class;
- G. Csordas, A. Ruttan and R. S. Varga, *The Laguerre inequalities with applications to a problem associated with the Riemann hypothesis*, Numerical Algorithms 1 (1991), 305–329;
- later work on Laguerre inequalities, real entire functions, and de Bruijn–Newman theory.

A targeted search did not immediately locate the exact all-order transport formula (8) or the generating transport equations (12)–(14), but the identities are elementary once (2) and (7) are written down. Absence from a targeted search is not a novelty certificate.

The reason to publish this note is **structural reuse and provenance**, not an aggressive priority claim.

---

## 9. What is not claimed

This note does **not** claim:

- RH;
- PTS;
- a new Laguerre inequality;
- that positivity of one Laguerre rung propagates backward in time;
- that (8) is historically new;
- a global positive lower bound for `H^2+H_x^2` or `mathcal L_1`.

It records the exact heat-transport ladder that unifies several previously separate PTS certification primitives.