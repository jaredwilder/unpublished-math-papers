# Erdős #291 — corrected leading-base-p harmonic divisibility criterion

**Author:** Jared Wilder  
**Recovered status:** `MATHEMATICALLY_AUDITED_LEAN_READY`  
**Public extraction:** 2026-09-11

This packet publishes the repaired p-adic criterion from the #291 campaign and preserves the fact that an earlier registry version used the wrong harmonic index.

## Setup

Let

\[
L_n=\operatorname{lcm}(1,2,\ldots,n)
\]

and

\[
a_n=\sum_{k=1}^{n}\frac{L_n}{k}.
\]

Thus

\[
H_n=\sum_{k=1}^n\frac1k=\frac{a_n}{L_n}
\]

before final fraction reduction.

Fix a prime `p<=n`. Let `p^e` be the largest power of `p` not exceeding `n`, and put

\[
q=\left\lfloor\frac{n}{p^e}\right\rfloor.
\]

Since `p^e<=n<p^{e+1}`, one has

\[
1\le q<p.
\]

## Theorem

Let `num(H_q)` denote the numerator of `H_q` in lowest terms. Then

\[
\boxed{
p\mid\gcd(a_n,L_n)
\iff
p\mid\operatorname{num}(H_q).
}
\]

Equivalently, because the denominator of `H_q` is prime to `p`,

\[
p\mid a_n
\iff
H_q\equiv0\pmod p.
\]

## Proof

Because `p<=n`, the lcm `L_n` is divisible by `p`, so

\[
p\mid\gcd(a_n,L_n)\iff p\mid a_n.
\]

Also

\[
v_p(L_n)=e.
\]

Reduce

\[
a_n=\sum_{k=1}^n L_n/k
\]

modulo `p`.

If

\[
v_p(k)<e,
\]

then `L_n/k` still contains a factor of `p`, so that summand vanishes modulo `p`.

The only surviving denominators therefore have exact p-adic valuation `e`. Since `k<=n`, they are exactly

\[
k=p^e j,
\qquad 1\le j\le q.
\]

Because `q<p`, none of these `j` is divisible by `p`. Write

\[
C=\frac{L_n}{p^e}.
\]

Then `p∤C`, and modulo `p`,

\[
\frac{L_n}{p^e j}\equiv Cj^{-1}.
\]

Hence

\[
a_n\equiv C\sum_{j=1}^qj^{-1}\equiv C H_q\pmod p.
\]

Since `C` is nonzero modulo `p`,

\[
p\mid a_n
\iff
H_q\equiv0\pmod p.
\]

Finally `q<p`, so the reduced denominator of `H_q` is not divisible by `p`. Therefore `H_q≡0 mod p` exactly when its reduced numerator is divisible by `p`.

This proves the criterion.

## Why the index matters

The earlier campaign registry contained the superficially similar criterion using

\[
H_{\lfloor n/p\rfloor}.
\]

That statement is false in general because the terms surviving modulo `p` are controlled by the **largest power `p^e<=n`**, not merely by the first power `p`.

The corrected index is

\[
\boxed{q=\lfloor n/p^e\rfloor.}
\]

The audit retained `n=18,p=3` and `n=20,p=3` as regression cases separating the corrupted criterion from the repaired one.

## Finite verifier history

The recovered campaign also contains a deterministic exact-integer verifier checking the repaired equivalence for all

\[
1\le n\le37,
\qquad p\le n\text{ prime},
\]

with fail-closed arithmetic. That finite run is a regression check only; the theorem above is proved for all `n,p` analytically.

## Scope boundary

This criterion reformulates one p-adic divisibility component of Erdős #291. It does **not** prove the campaign's open infinitude statement concerning `gcd(a_n,L_n)=1`.

The false superseded `floor(n/p)` criterion remains part of the public correction history and should not be cited as a theorem.

## License

Apache-2.0 for repository-authored material.
