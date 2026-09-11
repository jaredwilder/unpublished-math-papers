# Erdős #486 — summable forbidden mass gives natural density

**Author:** Jared Wilder  
**Recovered synthesis:** 2026-09-02  
**Public extraction:** 2026-09-11

This note records a strong restricted theorem recovered from the final campaign synthesis. It is
stronger than the parent asks on its stated slice, but it does **not** solve Erdős #486 in full.

## Frozen model

For every positive integer `n`, let

\[
X_n\subseteq\mathbb Z/n\mathbb Z
\]

be a set of forbidden residue classes. The source semantics use the activation threshold `n<m`:
a positive integer `m` survives when, for every modulus `n<m`, its residue modulo `n` is not in
`X_n`.

Let `B` be the set of all surviving positive integers.

The activation threshold is load-bearing. This theorem should not be quoted after silently changing
that definition.

## Theorem — summable forbidden mass

If

\[
\boxed{\sum_{n\ge1}\frac{|X_n|}{n}<\infty,}
\]

then `B` has an **ordinary natural density**. Consequently `B` also has logarithmic density.

## Proof

For `N>=1`, let `B_N` impose only the restrictions with `n<=N`. Because only finitely many congruence
conditions remain, `B_N` is eventually periodic, so it has a natural density `delta_N`.
The sets `B_N` decrease as `N` increases, hence

\[
\delta_N\downarrow\delta_*
\]

for some `delta_*>=0`.

Fix `x`. For integers `m<=x`, only moduli with `N<n<x` can newly remove an element of `B_N`: a
constraint with `n>=x` is not activated at any `m<=x` under the frozen `n<m` semantics.

A modulus `n` with `|X_n|` forbidden classes removes at most

\[
|X_n|\left(\frac{x}{n}+1\right)
\]

integers up to `x`. Therefore

\[
\frac{|(B_N\setminus B)\cap[1,x]|}{x}
\le
\sum_{N<n<x}\frac{|X_n|}{n}
+
\frac1x\sum_{N<n<x}|X_n|.
\]

The first term is bounded by the tail

\[
\sum_{n>N}\frac{|X_n|}{n}.
\]

For the second, put `a_n=|X_n|`. Since `sum a_n/n` converges, the standard Kronecker/Cesàro lemma
gives

\[
\frac1x\sum_{n\le x}a_n\to0.
\]

Hence

\[
\delta_N-\sum_{n>N}\frac{|X_n|}{n}
\le \underline d(B)
\le \overline d(B)
\le \delta_N.
\]

Letting `N->infinity`, both the tail and `delta_N-delta_*` vanish, so

\[
\underline d(B)=\overline d(B)=\delta_*.
\]

Thus

\[
\boxed{d(B)=\delta_*.}
\]

## Why this is useful

The theorem handles **arbitrary forbidden residue sets**, not merely one forbidden residue per
modulus, provided their total forbidden mass is summable. On this entire slice it gives ordinary
natural density, which is stronger than merely establishing logarithmic density.

The earlier finite-`A` periodicity theorem and the singleton-residue summable-moduli theorem become
special cases / corollaries of this framework.

## Novelty and scope boundary

The final synthesis marked this as a newly derived general theorem that should receive a specialist
Davenport–Erdős / sieve-literature collision check before any historical priority claim. No such
priority claim is made here.

The unrestricted parent problem remains open. This note proves only the exact summable-forbidden-
mass theorem above, with the exact source activation semantics stated explicitly.

## License

Apache-2.0 for repository-authored material.
