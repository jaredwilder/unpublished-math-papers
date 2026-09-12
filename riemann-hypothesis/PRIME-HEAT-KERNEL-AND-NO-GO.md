# Prime-side heat kernel and the atomwise complete-monotonicity obstruction

**Author of this extraction:** Jared Wilder  
**Recovered from:** RH Terminal Encirclement, Rounds 4–5

This note records the exact prime-side heat coordinate and the negative theorem that killed the naive atomwise positivity route.

## 1. Exact prime heat kernel

For the transformed logarithmic-derivative coordinate used by the terminal campaign, the prime contribution has inverse-Laplace kernel

\[
\boxed{
P(u)=
\frac{e^{-u/4}}{2\sqrt{\pi u}}
\sum_{n\ge2}
\frac{\Lambda(n)}{\sqrt n}
\exp\!\left(-\frac{(\log n)^2}{4u}\right).
}
\]

This is a Gaussian heat-kernel superposition indexed by prime powers through the von Mangoldt weight.

The smooth prime main term tends to one and cancels the constant inverse-Laplace contribution from the elementary `1/x` term in the transformed coordinate. The RH-sensitive information therefore lives in the residual after that main-term cancellation rather than in a crude pointwise domination of the full positive prime kernel.

This explains why an “archimedean term dominates the prime term” inequality is structurally misdirected: the target spectral information is in the small remainder left after two large main pieces cancel.

## 2. Individual Gaussian prime atom

For a fixed positive parameter `a`, consider

\[
p_a(u)=u^{-1/2}e^{-u/4-a^2/u}.
\]

Its logarithmic derivative is

\[
\boxed{
\frac{p_a'(u)}{p_a(u)}
=-\frac1{2u}-\frac14+\frac{a^2}{u^2}.
}
\]

The right side changes sign as `u` varies: the `a^2/u^2` term dominates for sufficiently small `u`, while the negative constant term dominates for sufficiently large `u`.

Therefore

\[
\boxed{-p_a'(u)\text{ does not have a fixed sign on }(0,\infty).}
\]

So the individual Gaussian atoms are not completely monotone in the way required by the attempted prime-by-prime sum-of-squares route.

## 3. Negative result

The campaign therefore kills the implication

\[
\text{positive prime Gaussian atoms}
\Longrightarrow
\text{atomwise complete monotonicity / literal prime SOS}.
\]

The obstruction occurs already at the level of a single atom's first derivative, before any difficult interaction among primes is considered.

This does **not** rule out a collective positivity representation after the prime atoms are summed and the main-term cancellation is performed. It rules out the naive atomwise proof architecture.

## 4. Real-rooted approximation front

A separate sufficient route survives:

If entire functions `Xi_N` each have only real zeros and

\[
\Xi_N\to\Xi
\]

locally uniformly, then standard Hurwitz/Rouché/Laguerre–Pólya closure gives real-rootedness of the limit and hence RH.

The mathematical difficulty is therefore the simultaneous construction of approximants with both properties:

1. every approximant is real-rooted;
2. the approximants converge locally uniformly to the Riemann `Xi` function.

The terminal campaign did not supply that construction.
