# Erdős #891 — multiplicity variant theorem and canonical scope correction

**Author:** Jared Wilder  
**Public release:** 2026-09-14  
**Canonical problem status:** **OPEN**

## Canonical problem

For `k>=2`, put

\[
P_k=p_1p_2\cdots p_k
\]

for the product of the first `k` primes. Erdős #891 asks whether every sufficiently late interval

\[
[n,n+P_k)
\]

contains an integer having **more than `k` distinct prime divisors**.

Thus the relevant function is

\[
\omega(m)=\#\{p:p\mid m\},
\]

not the multiplicity-counting function

\[
\Omega(m)=\sum_pv_p(m).
\]

The current public problem record explicitly clarifies the distinct-prime interpretation and says the question is unknown even for `k=2`.

## Exact theorem recovered from the estate

The campaign did prove a complete theorem for the `Omega` variant.

### Theorem

For every `k>=2` and every `n>P_k`, there exists

\[
m\in[n,n+P_k)
\]

with

\[
\boxed{\Omega(m)>k}.
\]

### Proof

Every half-open interval of `P_k` consecutive integers contains a unique multiple

\[
m=tP_k.
\]

Since `n>P_k`, one has `t>=2`. Because `P_k` is the product of `k` distinct primes,

\[
\Omega(P_k)=k.
\]

Complete additivity of `Omega` gives

\[
\Omega(m)=\Omega(P_k)+\Omega(t)=k+\Omega(t)\ge k+1.
\]

This proves the theorem.

## The failed bridge to distinct prime factors

A stale campaign row later claimed that the same argument “survives omega-counting via `m=2P_k`.” This is false:

\[
\boxed{\omega(2P_k)=k},
\]

because the extra factor 2 is already among the prime divisors of `P_k`.

For example, at `k=2`,

\[
P_2=6,\qquad2P_2=12=2^2\cdot3,
\]

and

\[
\omega(12)=2,
\]

not 3.

The other recovered route based on multiples of `2^k` has the same scope wall: `Omega(2^kt)` is large because multiplicities count, whereas `omega(2^{k+j})=1`.

Therefore the theorem above is a clean theorem about the **multiplicity variant** and not a solution of Erdős #891.

## Public provenance

The raw Pass-3 high-score stream recovered on Release Day has:

- size `27,277,064` bytes;
- SHA-256 `8990b20d7807e878033a8cc0c403729620a6fb27ca1b838890da11370f42ec71`.

A detailed workflow-status audit, including exact normalized hashes of the contradictory `PROVED` rows, is public in:

`jaredwilder/msl-ore-estate/corrections/ERDOS-891-OMEGA-VS-omega-2026-09-14.md`

## Literature/status boundary

Public status sources checked during release:

- `https://www.erdosproblems.com/891`
- `https://www.erdosproblemaday.com/report/891`

Both use the distinct-prime interpretation; the latter explicitly writes `omega(m)` and discusses why the `Omega` interpretation would trivialize the problem.

No novelty is claimed for the easy multiplicity theorem. Its importance here is provenance and correction: a mathematically valid variant theorem had been incorrectly promoted across a semantic boundary.
