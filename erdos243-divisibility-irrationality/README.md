# Erdős #243 — divisibility-chain irrationality criterion

**Author:** Jared Wilder  
**Recovered from:** September 2026 theorem audit  
**Public extraction:** 2026-09-11

## Theorem

Let `a_1,a_2,...` be positive integers. Suppose that eventually

\[
a_m\mid a_{m+1}
\]

and

\[
\frac{a_{m+1}}{a_m}\longrightarrow\infty.
\]

Then

\[
\boxed{\sum_{m\ge1}\frac1{a_m}\notin\mathbb Q.}
\]

The same conclusion holds if the divisibility and growth hypotheses begin only after a finite
initial segment.

## Proof

Discarding a finite initial segment changes the sum by a rational number, so it is enough to prove
irrationality for a tail on which the divisibility chain holds.

Assume for contradiction that

\[
\sum_{m\ge M_0}\frac1{a_m}=\frac uv
\]

with positive integers `u,v`. Choose `M` so far out that the divisibility chain holds through `M`
and every later ratio is larger than a fixed constant `R>2v`.

Because

\[
a_{M_0}\mid a_{M_0+1}\mid\cdots\mid a_M,
\]

multiplying by `v a_M` makes the rational side and every term through `M` integral. Hence

\[
v a_M\sum_{m>M}\frac1{a_m}
\]

must be an integer.

It is strictly positive. On the other hand the ratio bound gives

\[
a_{M+j}\ge R^j a_M,
\]

so

\[
0< v a_M\sum_{m>M}\frac1{a_m}
\le
v\sum_{j\ge1}R^{-j}
=
\frac{v}{R-1}
<1.
\]

This is impossible for an integer. Therefore the series is irrational.

## Scope boundary

This is a restricted structural theorem relevant to the #243 campaign, not the canonical converse or
the strongest known result around the parent problem.

The September novelty audit classified it `FOLKLORE_RISK`: the mechanism is a classical
Cantor-series-style argument and no global novelty claim should be made without a specialist search.
The point of this release is to preserve the exact theorem and proof, not to inflate its priority.

## License

Apache-2.0 for repository-authored material.
