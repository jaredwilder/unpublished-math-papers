# Exact rational certificates for Riemann Xi theta-kernel moment inequalities

**Author:** Jared Wilder  
**Recovered from:** 2026-09-12 RH campaign export

This directory publishes a set of self-contained or exact-rational certificate programs for inequalities involving the classical Riemann Xi theta kernel.

These certificates were originally developed inside a determinant criterion later shown **not sufficient for RH**. That later route failure does not invalidate the certified integral inequalities recorded here.

## 1. First-rung self-contained certificate

`certify_first_rung.py` derives everything it uses internally:

- `pi` from the Machin formula with alternating-series remainder bounds;
- exponential bounds by rational Taylor enclosures;
- the large-x tail analytically;
- all quadrature cells by exact rational outward bounds.

Its final quadratic certificate is

\[
P(3)\in[1.487365741170569\times10^{-6},\ 8.824883179857477\times10^{-5}],
\]

hence

\[
\boxed{P(3)>0}.
\]

Historical output: `certify_first_rung.log`.

## 2. Full-kernel first moment inequality

`certify_full_kernel.py` encloses the full theta kernel, including the theta-series remainder and the truncation tail, and proves

\[
\boxed{3I_2^2-I_0I_4>0}.
\]

The certified interval is

\[
3I_2^2-I_0I_4
\in
[3.144319836807\times10^{-4},\ 5.675693447454\times10^{-4}].
\]

Historical output: `certify_full_kernel.log`.

## 3. First four binding rungs

`certify_four_rungs.py` uses kernel-sealed unimodality plus rational peak bracketing and monotone cell bounds. It certifies four successive inequalities:

\[
\begin{array}{c|c}
k & \text{certified positive interval}\\\hline
1 &[1.56335252\times10^{-3},1.96426203\times10^{-3}]\\
2 &[1.73415563\times10^{-3},2.24619876\times10^{-3}]\\
3 &[2.72502080\times10^{-3},3.63976614\times10^{-3}]\\
4 &[5.87924581\times10^{-3},8.13406217\times10^{-3}]
\end{array}
\]

Every enclosure includes both the theta-series remainder and the truncation tail.

Historical output: `certify_four_rungs.log`.

## 4. Curvature threshold certificates

`certify_curvature.py` gives exact-rational lower certificates for the relevant mode/curvature threshold at

\[
m=2,4,6,8,10,12,16,24.
\]

At every tested index the stationarity left side at

\[
U=\frac{m-1}{4(m+1)}
\]

is strictly less than `m+1`, implying the true mode exceeds the threshold and therefore the stated curvature requirement holds at those indices.

This file certifies the **listed indices**. A claimed uniform all-index extension elsewhere in the campaign should be audited separately before being promoted to a theorem.

## 5. Certified theta-series tail

`certify_tail.py` proves at the worst tested point `u=0`:

\[
\text{relative theta tail}
\le
2.477138004562849053\times10^{-3}
<\frac1{300}.
\]

The calculation uses exact rational Machin/Taylor bounds.

## 6. Gaussian-normalized moment row

`row_is_log_concavity.py` proves algebraically that the binding row

\[
(2k-1)I_{2k+2}I_{2k-2}\le(2k+1)I_{2k}^2
\]

is exactly the log-concavity condition

\[
\boxed{J_{k+1}J_{k-1}\le J_k^2},
\qquad
J_k=\frac{I_{2k}}{\Gamma(k+1/2)}.
\]

Its numerical probe for the theta kernel gives ratios below one for `k=1,...,9`, rising from approximately `0.93037` to `0.96968`.

Those finite numerical ratios are evidence only; the algebraic equivalence itself is exact.

## Status

The package certifies **theta-kernel inequalities**. It does not certify RH, and the determinant criterion that originally motivated these computations has since been refuted as sufficient for real-rootedness.

That distinction is why these certificates are published separately from the historical Branch C route.