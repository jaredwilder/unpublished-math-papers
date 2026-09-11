# Erdős #893 — Mersenne divisor injection and order-sum identities

**Author:** Jared Wilder  
**Recovered from:** September 2026 full-corpus theorem audit  
**Public extraction:** 2026-09-11

This packet records clean universal infrastructure recovered during the #893 campaign. The source
audit explicitly notes that stronger public results exist; nothing here is marketed as the current
frontier.

## Theorem 1 — divisor injection

If

\[
a\mid k,
\]

then

\[
\boxed{2^a-1\mid2^k-1.}
\]

### Proof

Write `k=am`. Then

\[
2^k-1=(2^a)^m-1
=(2^a-1)\bigl(1+2^a+\cdots+2^{a(m-1)}\bigr).
\]

Thus every positive divisor `a` of `k` yields the distinct divisor `2^a-1` of `2^k-1`, so

\[
\boxed{\tau(2^k-1)\ge\tau(k).}
\]

Consequently, if

\[
f(N)=\sum_{k\le N}\tau(2^k-1),
\]

then

\[
f(N)\ge\sum_{k\le N}\tau(k)
=N\log N+(2\gamma-1)N+O(\sqrt N),
\]

using the classical divisor-summatory asymptotic.

## Theorem 2 — multiplicative-order sum identity

Every positive odd integer `d` divides `2^k-1` exactly when

\[
\operatorname{ord}_d(2)\mid k.
\]

Therefore, with the natural convention for `d=1`, double-counting divisor/exponent incidences gives

\[
\boxed{
\sum_{k\le N}\tau(2^k-1)
=
\sum_{\substack{d\ge1\;\text{odd}\\ \operatorname{ord}_d(2)\le N}}
\left\lfloor\frac{N}{\operatorname{ord}_d(2)}\right\rfloor.
}
\]

Only odd `d` with order at most `N` contribute, so the right side is finite for fixed `N`.

## Doubling consequence

The factorization

\[
2^{2m}-1=(2^m-1)(2^m+1)
\]

has coprime factors because both are odd and differ by 2. Hence multiplicativity of `tau` gives

\[
\tau(2^{2m}-1)
=
\tau(2^m-1)\tau(2^m+1)
\ge2\tau(2^m-1).
\]

## Scope and novelty boundary

These are universal exact identities/inequalities and useful analytic infrastructure, not a solution
of the surrounding asymptotic problem. The September audit classifies the divisor injection as
likely classical/derivable and the order-sum representation as likely standard. They are released
for completeness and provenance, not as historical novelty claims.

## License

Apache-2.0 for repository-authored material.
