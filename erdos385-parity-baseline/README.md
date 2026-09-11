# Erdős #385 — parity baseline and reduction to even n

**Author:** Jared Wilder  
**Public extraction:** 2026-09-11

For composite `m`, let `p(m)` be its least prime divisor and define

\[
F(n)=\max_{\substack{m<n\\m\text{ composite}}}(m+p(m)).
\]

## Theorem

For every `n>=5`,

\[
\boxed{F(n)\ge n.}
\]

For every odd `n>=5`, in fact

\[
\boxed{F(n)>n.}
\]

Thus the first question `F(n)>n` reduces completely to even `n`.

## Proof

If `n>=5` is odd, take `m=n-1`. Then `m` is even and composite, so its least prime factor is 2. Hence

\[
m+p(m)=n-1+2=n+1>n.
\]

If `n>=6` is even, take `m=n-2`. This is even and at least 4, hence composite with least prime factor 2. Thus

\[
m+p(m)=n-2+2=n.
\]

The remaining case `n=5` is covered by the odd argument.

## Scope

This does not prove `F(n)>n` for all sufficiently large even `n`, and it does not address whether `F(n)-n\to\infty`. It is an exact structural reduction of the parent question.
