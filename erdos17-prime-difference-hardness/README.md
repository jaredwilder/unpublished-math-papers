# Erdős #17 — prime-difference hardness reduction

**Author:** Jared Wilder  
**Recovered from:** September 2026 full-corpus theorem audit  
**Public extraction:** 2026-09-11

## Reduction

Write `P(p)` for the Erdős #17 property appearing in the recovered campaign:

> for every even `n <= p-3`, there exist primes `q1,q2 <= p` with `q1-q2=n`.

If infinitely many primes `p` satisfy `P(p)`, then **every positive even integer is the difference
of two primes**.

### Proof

Fix any positive even integer `n`. Since the set of good primes is infinite, choose a good prime
`p>n+3`. Then `n<=p-3`, so `P(p)` supplies primes `q1,q2<=p` with

\[
q_1-q_2=n.
\]

Because `n` was arbitrary, every positive even integer occurs as a difference of two primes.

## Why this matters

The conclusion is the classical Maillet-type prime-difference problem and is itself open. Thus an
affirmative solution of the frozen #17 formulation automatically crosses a major open-problem
strength barrier. This is a **hardness reduction**, not progress toward proving #17.

A tempting stronger statement in the raw campaign—claiming the reduction immediately implies
infinitely many twin primes by setting `n=2`—was rejected. The same pair `5-3=2` may serve for
arbitrarily many good `p`; the reduction proves existence of a representation of each even
integer, not infinitely many representations of each fixed difference.

The September novelty audit labelled this reduction `APPARENTLY_UNRECORDED_REDUCTION` with medium
confidence: it was not located on the #17 tracker in the targeted search, but specialist historical
review is still required before any priority claim.

## License

Apache-2.0 for repository-authored material.
