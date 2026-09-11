# Erdős #413 — exact logarithmic predecessor window

**Author:** Jared Wilder  
**Recovered from:** September 2026 theorem synthesis  
**Public extraction:** 2026-09-11

Let `ω(m)` denote the number of distinct prime divisors of `m`.

## The coefficient-1 theorem

For `n>1`, the condition

\[
\forall m<n,\qquad m+\omega(m)\le n
\]

is equivalent to checking only the terminal predecessor window

\[
\omega(n-1)\le1
\]

and

\[
\omega(n-k)\le k
\qquad
2\le k\le\left\lceil\log_2(n-1)\right\rceil.
\]

All larger `k` are automatic.

### Proof

Put `m=n-k`. The original condition becomes

\[
\omega(n-k)\le k.
\]

For every positive integer `r`,

\[
\omega(r)\le\log_2 r,
\]

because a number with `t` distinct prime divisors is at least the product of `t` distinct primes,
and in particular at least `2^t`.

Thus, whenever

\[
k>\log_2(n-1),
\]

we have

\[
\omega(n-k)\le\log_2(n-k)\le\log_2(n-1)<k.
\]

So only the terminal `O(log n)` window can fail. The `k=1` case is exactly `ω(n-1)<=1`, i.e. `n-1`
is 1 or a prime power under the usual convention.

## Parameterized theorem

More generally, fix `epsilon>0`. The condition

\[
\forall m<n,\qquad m+\varepsilon\,\omega(m)\le n
\]

needs only the terminal window `m=n-k` with

\[
\boxed{1\le k\le\left\lceil\varepsilon\log_2(n-1)\right\rceil.}
\]

Indeed, outside this window,

\[
\varepsilon\omega(n-k)
\le
\varepsilon\log_2(n-1)
<k,
\]

so the inequality is automatic.

## What this accomplishes

This is an exact reduction of each candidate-`n` certification problem from checking `n-1`
predecessors to checking only

\[
O_\varepsilon(\log n)
\]

predecessors. It does not prove that infinitely many qualifying `n` exist; the infinitude clauses of
Erdős #413 remain the hard part.

## Authority boundary

The coefficient-1 reduction was independently recovered in multiple campaign sessions and classified
`MATHEMATICALLY_AUDITED_LEAN_READY`. The epsilon-parameterized form is the late-synthesis
generalization. Neither is represented here as a solution of the parent problem or as a historical
priority claim.

## License

Apache-2.0 for repository-authored material.
