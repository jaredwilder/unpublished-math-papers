# Erdős #289 — all-prime p-adic obstructions for integral reciprocal sums

**Author:** Jared Wilder  
**Recovered campaign:** `erdos289-campaign-001`  
**Public extraction:** 2026-09-11

This packet collects the strongest clean universal arithmetic extracted from the #289 campaign: an all-prime p-adic obstruction, the classical 2-adic consecutive-interval consequence, and a finite certified head/tail reduction. These are necessary conditions and structural reductions, not a close of the full problem.

## Theorem 1 — all-prime p-adic obstruction

Let

\[
S\subseteq\{2,3,4,\ldots\}
\]

be finite and suppose

\[
T=\sum_{n\in S}\frac1n\in\mathbb Z.
\]

Fix a prime `p`. Define

\[
U_p
=
\sum_{\substack{n\in S\\p\mid n}}\frac{p}{n}.
\]

Then

\[
\boxed{v_p(U_p)\ge1.}
\]

Equivalently, the rational number formed from the `p`-divisible denominators after removing one factor of `p` must itself be p-adically divisible by `p`.

### Proof

Split

\[
T=
\sum_{\substack{n\in S\\p\mid n}}\frac1n
+
\sum_{\substack{n\in S\\p\nmid n}}\frac1n
=
\frac{U_p}{p}+V_p.
\]

Every denominator occurring in `V_p` is prime to `p`, so

\[
v_p(V_p)\ge0.
\]

Because `T` is an integer,

\[
v_p(T)\ge0.
\]

Thus

\[
\frac{U_p}{p}=T-V_p
\]

is p-adically integral, giving

\[
v_p(U_p)-1\ge0.
\]

Hence `v_p(U_p)>=1`.

This theorem is the all-prime version of the valuation obstruction that the historical campaign first exploited at `p=2`.

## Corollary 2 — no nontrivial consecutive reciprocal interval is integral

Let

\[
I=\{a,a+1,\ldots,b\},
\qquad b>a\ge1.
\]

Then

\[
\boxed{\sum_{n=a}^{b}\frac1n\notin\mathbb Z.}
\]

### 2-adic proof

Among consecutive integers there is a unique denominator having maximal 2-adic valuation. Let `L` be the lcm of all denominators in the interval. After multiplying by `L`, the contribution from that unique maximal-`v_2` denominator is odd, while every other contribution is even. Therefore

\[
L\sum_{n=a}^{b}\frac1n
\]

is odd, whereas `L` itself is even. The reciprocal sum cannot be an integer.

This is the Kürschák mechanism recovered by the campaign.

## Corollary 3 — top-level parity across interval blocks

Suppose a finite sum of reciprocal interval-block sums is integral. Attach to each interval the maximal `v_2` attained by one of its denominators, and let `E` be the global maximum of those levels.

After clearing the global lcm, precisely the blocks attaining level `E` contribute odd parity at the top 2-adic level. Hence

\[
\boxed{\text{the number of interval blocks attaining the global maximal }v_2\text{ level must be even}.}
\]

The audit also records the sharper warning that **only the top level is decided by this count**. Below the maximal level, p-adic carries matter; parity counting alone is not a valid replacement for the full local state.

## Forced `[2,3]` head and `1/6` tail

A separate exact reduction concerns decompositions of 1 into reciprocal consecutive runs. If an admissible decomposition contains the denominator 2, the run containing 2 is forced to be

\[
[2,3],
\]

because

\[
\frac12+rac13=\frac56<1,
\qquad
\frac12+rac13+rac14>1.
\]

Therefore the remaining runs must sum exactly

\[
\boxed{1/6}
\]

and begin at denominator at least 5.

The recovered Lean/certificate fragment additionally establishes:

> no single run `[a,b]` with `5<=a<b<=60` has reciprocal sum exactly `1/6`.

The source artifact was recorded as `kernel/Erdos289Head.lean` with theorem names
`F1_head_forced`, `F1_tail_value`, `W4_nat_fragment`, `W4_bridge`, and `W4_fragment`; its recorded axiom footprint was the ordinary Mathlib footprint `{propext, Classical.choice, Quot.sound}`. The finite `b<=60` scope must not be promoted to an unbounded theorem.

## Search consequence

The all-prime theorem means exact search cannot track only real-valued mass. For each relevant prime it must preserve the local p-adic state of the p-divisible denominators. The campaign called this the `STATEFUL_ELIMINATION` requirement.

This is mathematical content rather than a software claim: two candidate partial sums with the same ordinary rational mass may have different admissibility because their local p-adic states differ.

## Scope / authority boundary

- The all-prime p-adic obstruction is an unconditional elementary theorem.
- The consecutive-interval obstruction is unconditional/classical.
- The top-level parity theorem is unconditional.
- The `[2,3]` head / `1/6` tail is exact.
- The no-single-tail statement is certified only for `5<=a<b<=60`.
- The full Erdős #289 problem is **not** claimed closed.

The estate labels the all-prime theorem as a high-priority formalization target; it was not represented as universally kernel-checked at the time of recovery.

## License

Apache-2.0 for repository-authored material.
