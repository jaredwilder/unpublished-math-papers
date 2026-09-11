# Validated New Gold — independently rechecked long-tail theorem ledger

**Author:** Jared Wilder  
**Recovered source:** September 2026 continued audit  
**Public extraction:** 2026-09-11

These proof sheets were independently rechecked in the estate. They are **not described as kernel-certified unless an individual statement says so**. Historical novelty is separate from truth.

## Erdős #477 — no square-image exact tiling of Z

Let

\[
B=\{k^2:k\in\mathbb Z\}.
\]

Then

\[
B-B=\{m\in\mathbb Z:m\not\equiv2\pmod4\}.
\]

If `m` is odd, it is a difference of consecutive squares up to sign. If `4|m`, write

\[
4t=(t+1)^2-(t-1)^2
\]

up to sign. A difference of two squares is never `2 mod 4`.

If `Z=A⊕B` uniquely, then

\[
(A-A)\cap(B-B)=\{0\},
\]

because a nonzero common difference would produce two representations. Hence every nonzero
difference between two elements of `A` must be `2 mod 4`. Three distinct elements are impossible:
from `a-b≡2` and `b-c≡2` one gets `a-c≡0 mod4`, forbidden. Thus `|A|<=2`. But finite `A` plus
nonnegative squares is bounded below and cannot cover all of `Z`.

## Erdős #700 — exact semiprime formula

For `n=pq` with primes `p<=q`, define

\[
f(n)=\min_{1<k\le n/2}\gcd\!\left(n,{n\choose k}\right).
\]

Then

\[
\boxed{f(pq)=p.}
\]

Use

\[
k{n\choose k}=n{n-1\choose k-1}.
\]

Therefore

\[
\frac{n}{\gcd(n,{n\choose k})}\mid k.
\]

If `p<q`, a gcd of 1 would force `pq|k`, impossible for `k<=pq/2`, so every admissible gcd is at least `p`. At `k=q`,

\[
{pq\choose q}=p{pq-1\choose q-1}.
\]

Lucas modulo `q` gives

\[
{pq-1\choose q-1}\equiv1\pmod q,
\]

so `q` does not divide this binomial while `p` does; the gcd is exactly `p`. For `p=q`, take `k=p` and use the same Lucas/valuation observation.

Independent exact sanity values recovered in the audit:

```text
f(21)=3, f(33)=3, f(35)=5, f(49)=7, f(77)=7.
```

## Erdős #479 — infinite parametric witness family

For `j>=0` and odd prime `p`, put

\[
k=2^{2^j},\qquad n=2^j p.
\]

Then

\[
\boxed{2^n\equiv k\pmod n.}
\]

Modulo `p`, Fermat gives

\[
2^{2^jp}/2^{2^j}=2^{2^j(p-1)}\equiv1.
\]

Modulo `2^j`, both powers vanish (for `j=0` the modulus is 1). Since `gcd(2^j,p)=1`, CRT gives the congruence modulo `n`. Varying `p` yields infinitely many `n` for every `k=2^{2^j}`.

## Erdős #885 — factor-difference / square duality

For `N>=1`, let

\[
D(N)=\{|a-b|:ab=N\}.
\]

Then

\[
\boxed{d\in D(N)\iff \exists s\ge0:\ s^2=d^2+4N.}
\]

Forward, if `N=ab` and `d=|a-b|`, then

\[
(a+b)^2=(a-b)^2+4ab=d^2+4N.
\]

Conversely, if `s^2-d^2=4N`, then `s,d` have the same parity and `s>d`; set

\[
a=(s+d)/2,\qquad b=(s-d)/2.
\]

Then `a,b` are positive integers, `ab=N`, and `|a-b|=d`.

## Erdős #456 — prime-index equality family

For every odd prime `p`, put `n=p-1`. For all `m<=n`,

\[
\varphi(m)\le m-1<n,
\]

so `n` does not divide `φ(m)`. But `φ(p)=p-1=n`, hence the smallest `m` with `n|φ(m)` is `p`: `m_n=p`.

Also `p≡1 mod n`, and any prime congruent to 1 mod `n` is at least `n+1=p`, so `p_n=p`. Therefore

\[
\boxed{m_{p-1}=p_{p-1}=p}
\]

for every odd prime `p`.

## Erdős #289 — 2-adic interval theorem

In any finite interval of consecutive positive integers of length at least two, there is a unique element with maximal `v_2`.
Let `L` be the lcm of the denominators. In

\[
L\sum\frac1n=\sum\frac Ln,
\]

the term corresponding to the unique maximal-`v_2` denominator is odd and every other term is even. Hence the numerator after clearing denominators is odd while `L` is even, so the reciprocal sum is not an integer.

For a finite sum of such interval sums, choose the global maximal `v_2` level. After clearing the global lcm, precisely the blocks attaining that level contribute odd parity. Therefore an integral total requires an **even number of blocks attaining the global maximum**.

## Erdős #243 — eventual divisibility-chain irrationality

If positive integers `a_n` eventually satisfy

\[
a_n\mid a_{n+1},\qquad a_{n+1}/a_n\to\infty,
\]

then

\[
\sum_n1/a_n
\]

is irrational. Subtract the finite rational head and suppose the tail is `u/v`. Choose `M` so far out that the chain holds and every later ratio exceeds a constant larger than `v`. Multiplying the rational identity by `v a_M` makes the rational side and terms through `M` integral, while the remaining positive tail is bounded by a geometric series strictly between 0 and 1, contradiction.

This is a barrier theorem, not a close of #243.

## Erdős #274 — infinite-group cardinality reduction

Suppose an infinite group `G` is exactly partitioned by finitely many cosets with pairwise-distinct cardinalities. A finite union of sets each of cardinality smaller than `|G|` still has cardinality smaller than `|G|`, so some part has size `|G|`; by distinctness it is unique. Write it `aH`.

If `H` is proper, another coset of `H` exists in the complement and also has size `|G|`, but the complement is the finite union of the strictly smaller partition parts, contradiction. Thus `H=G`, making the cover a one-part cover. Therefore no nontrivial finite exact coset partition with pairwise-distinct part cardinalities exists for an infinite group under these hypotheses.

## Erdős #985 — Fermat-prime favorable family

If `p>=5` is a Fermat prime, then `p-1` is a power of two and `p≡5 mod12`. Quadratic reciprocity gives

\[
\left(\frac3p\right)=-1,
\]

so Euler's criterion yields

\[
3^{(p-1)/2}\equiv-1\pmod p.
\]

The order of 3 divides the 2-power `p-1` but does not divide `(p-1)/2`; hence

\[
\boxed{\operatorname{ord}_p(3)=p-1.}
\]

Thus 3 is a primitive root modulo every Fermat prime `p>=5`.

## Historical C(13,6,3) degree-8 proof — superseded, preserved

The source proof sheet also contained the elementary necessary condition `r_x>=8` for a hypothetical 20-block `C(13,6,3)` cover, obtained from pair multiplicity `r_xy>=3`, and the resulting excess identity `Σ_x(r_x-8)=16`.

That mathematics is correct but **superseded** by the later stronger theorem now public at `combinatorial-records/covering-designs/C13-6-3`: the exact value `C(12,5,2)=9` upgrades every point degree to `r_x>=9` and leaves only three possible global point-degree multisets. The weaker proof is retained here only as historical provenance.

## Authority boundary

These sheets preserve exact mathematics and proof repair history. They do not claim that every result is historically new, that every result closes its parent problem, or that every result is Lean-kernel certified. Where a stronger subject-specific public packet exists, that packet is the current authority.

## License

Apache-2.0 for repository-authored material.
