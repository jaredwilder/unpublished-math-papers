# Erdős #394 — exact prime slice

**Author:** Jared Wilder  
**Public extraction:** 2026-09-11

Let `t_2(p)` be the least positive integer `m` for which the prime `p` divides the product of two consecutive integers

\[
m(m+1).
\]

## Theorem

For every odd prime `p`,

\[
\boxed{t_2(p)=p-1.}
\]

## Proof

For `1<=m<=p-2`, both `m` and `m+1` lie strictly between 0 and `p`, so neither is divisible by `p`. Hence

\[
p\nmid m(m+1).
\]

At `m=p-1`,

\[
m(m+1)=(p-1)p,
\]

which is divisible by `p`. Therefore the least such `m` is `p-1`.

## Formalization boundary

The historical green Lean receipt checked the claim only for primes below 100. The universal proof above is elementary and independent of that finite receipt; it should not be described as universally kernel-certified until a matching universal formalization is pinned.
