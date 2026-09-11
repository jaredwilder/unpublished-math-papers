# Erdős #700 — exact semiprime binomial-gcd formula

**Author:** Jared Wilder  
**Recovered status:** `MATHEMATICALLY_AUDITED_LEAN_READY`  
**Public extraction:** 2026-09-11

## Theorem

For `n>=2`, define

\[
f(n)=\min_{1<k\le n/2}\gcd\!\left(n,{n\choose k}\right).
\]

If

\[
n=pq
\]

with primes `p<=q`, then

\[
\boxed{f(pq)=p.}
\]

Thus the complete semiprime stratum is exact.

## Lower bound

Use

\[
k{n\choose k}=n{n-1\choose k-1}.
\]

It follows that

\[
\frac{n}{\gcd(n,{n\choose k})}\mid k.
\]

If `gcd(n,C(n,k))=1`, then `n|k`, impossible when

\[
1<k\le n/2.
\]

For `n=pq`, every nontrivial divisor of `n` is at least `p`, so

\[
\gcd\!\left(pq,{pq\choose k}\right)\ge p
\]

for every admissible `k`. Hence

\[
f(pq)\ge p.
\]

## Matching upper bound

Take

\[
k=q.
\]

Then

\[
{pq\choose q}=p{pq-1\choose q-1}.
\]

Modulo `q`, Lucas' theorem gives

\[
{pq-1\choose q-1}\equiv1\pmod q,
\]

so `q` does not divide `C(pq,q)`, while the displayed identity shows that `p` does divide it. Therefore

\[
\gcd\!\left(pq,{pq\choose q}\right)=p.
\]

Combining the two directions yields

\[
\boxed{f(pq)=p.}
\]

The case `p=q` is included: taking `k=p` gives the same exact value `p` by the corresponding elementary `p`-adic/Lucas calculation.

## Regression values recovered in the audit

```text
f(21)=3
f(33)=3
f(35)=5
f(49)=7
f(77)=7
```

These are checks of the general theorem, not its proof.

## Scope / novelty boundary

This is the exact semiprime slice of the surrounding Erdős problem. It does not settle the behavior on integers with three or more prime factors. The estate audit did not grant a historical novelty claim; the theorem is published here for exact provenance and reuse.

## License

Apache-2.0 for repository-authored material.
