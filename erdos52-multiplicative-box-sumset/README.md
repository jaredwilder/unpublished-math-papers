# Erdős #52 — the `2^i 3^j` multiplicative box has an almost-maximal sumset

**Author:** Jared Wilder  
**Recovered route:** `erdos52-campaign-001 / R001 / L1`  
**Public extraction:** 2026-09-11

The historical campaign recorded a lower bound

\[
|A_N+A_N|\ge \frac{N^4}{3(\log_2N+3)^3}
\]

for the multiplicative box

\[
A_N=\{2^i3^j:0\le i,j<N\}.
\]

During Release-Day reconstruction the underlying valuation-decoding argument yields a substantially cleaner and stronger exact theorem.

## Theorem

For every integer `N>=2`, let

\[
A_N=\{2^i3^j:0\le i,j<N\}.
\]

Then

\[
\boxed{|A_N+A_N|\ge {N\choose2}^2.}
\]

Since `|A_N|=N^2`, this is

\[
|A_N+A_N|\ge\frac{N^2(N-1)^2}{4}
=\left(\frac14+o(1)\right)|A_N|^2.
\]

Meanwhile

\[
A_NA_N=\{2^a3^b:0\le a,b\le2N-2\},
\]

so

\[
\boxed{|A_NA_N|=(2N-1)^2.}
\]

Thus this natural multiplicative-box family has essentially minimal multiplicative growth but essentially maximal additive growth. It cannot furnish a counterexample to the Erdős–Szemerédi sum-product phenomenon.

## Proof

Consider only sums of the form

\[
2^i3^j+2^k3^\ell
\]

with

\[
0\le i<k<N,\qquad 0\le j<\ell<N.
\]

There are exactly

\[
{N\choose2}^2
\]

such quadruples. We show all their sums are distinct.

Factor one such sum:

\[
2^i3^j+2^k3^\ell
=2^i3^j\bigl(1+2^{k-i}3^{\ell-j}\bigr).
\]

Because `k-i>=1`, the parenthesized factor is odd. Because `ell-j>=1`, it is congruent to `1 mod 3`. Therefore

\[
v_2\!\left(2^i3^j+2^k3^\ell\right)=i,
\qquad
v_3\!\left(2^i3^j+2^k3^\ell\right)=j.
\]

So the sum itself recovers `i` and `j` uniquely. Dividing by `2^i3^j` and subtracting 1 then gives

\[
2^{k-i}3^{\ell-j}.
\]

Unique factorization recovers `k-i` and `ell-j`, and therefore `k` and `ell`. Hence the map

\[
(i,j,k,\ell)
\longmapsto
2^i3^j+2^k3^\ell
\]

is injective on the indicated domain. Consequently

\[
|A_N+A_N|\ge{N\choose2}^2.
\]

For the product set, multiplication simply adds the exponents, and every pair `(a,b)` with
`0<=a,b<=2N-2` occurs, so `|A_NA_N|=(2N-1)^2`.

## Independent finite sanity check

The valuation-decoding injection was separately brute-force checked during reconstruction for
`N=2,...,7`; the numbers of restricted sums were exactly

```text
N=2:   1  = C(2,2)^2
N=3:   9  = C(3,2)^2
N=4:  36  = C(4,2)^2
N=5: 100  = C(5,2)^2
N=6: 225  = C(6,2)^2
N=7: 441  = C(7,2)^2
```

The computation is only a sanity check; the theorem is proved analytically above.

## Relationship to the recovered campaign claim

The Pass-4/Pass-6 estate preserves the original route statement as source-recorded `PROVED`:

> `A={2^i3^j:0≤i,j<N}` has a large sumset via `v_2/v_3` decoding; the multiplicative-box counterexample vehicle is closed while the canonical conjecture stays open.

The theorem above reconstructs that mechanism without relying on the source status and improves its quantitative lower bound.

## Scope / novelty boundary

This does **not** solve Erdős #52 / the general Erdős–Szemerédi sum-product conjecture. It eliminates one highly structured candidate counterexample family.

No historical novelty claim is made for the exact bound without a specialist prior-art search. The argument is elementary once the valuation-decoding coordinate is noticed.

## License

Apache-2.0 for repository-authored material.
