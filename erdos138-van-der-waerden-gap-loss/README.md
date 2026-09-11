# Erdős #138 — van der Waerden growth variants and prime-gap loss

This directory is the human-facing entry point for a sorry-free Lean packet comparing three asymptotic growth questions for the two-colour van der Waerden numbers `W(k)`.

The formal source is preserved at
`jaredwilder/erdos-campaign-archive/campaigns/erdos138-close-2026-09-05/E138Fragments.lean`.

## Logical hierarchy of the variants

For an abstract sequence `W : ℕ → ℕ`, the development defines:

- `RootDiv`: `W(k)^(1/k) → ∞`;
- `RatioDiv`: `W(k+1)/W(k) → ∞`;
- `BaseDiv W C`: `W(k)/C^k → ∞`.

Lean proves

\[
\text{RatioDiv}\Longrightarrow\text{RootDiv}
\Longrightarrow\text{BaseDiv}(C)
\]

for every fixed `C>0`, and also proves the converse characterization

\[
\text{RootDiv}
\iff
\forall C>0,\; W(k)/C^k\to\infty.
\]

Thus the root-growth formulation is exactly the assertion that `W(k)` eventually beats every fixed exponential base.

## Exact loss in prime-subsequence transfer

Assume `W` is monotone and one has a lower bound

\[
p\,2^p\le W(p+1).
\]

Writing

\[
k=p+1+g,
\]

Lean proves the transported estimate

\[
\frac{p}{2^{g+1}}
\le
\frac{W(k)}{2^k}.
\]

So the entire loss from moving a lower bound at `p+1` to a general `k` is the explicit factor `2^(g+1)`, where `g` is the gap from `k-1` down to the chosen prime `p`.

Along the prime subsequence itself (`g=0`) this gives

\[
\frac{p}{2}\le \frac{W(p+1)}{2^{p+1}}.
\]

This precisely identifies why a prime-subsequence estimate plus monotonicity is not, by itself, a proof of the all-`k` statement.

## Formal-source mismatch found

The campaign also records a three-way discrepancy in the imported source around the cited Berlekamp lower bound:

- one docstring reading gives `p^(2^p)`;
- the formal statement gives `p * 2^p`;
- the published theorem is recorded as `p(2^p - 1)`.

At `p=3` these are respectively `6561`, `24`, and `21`; Lean proves the three numbers are distinct and that the formal `p*2^p` statement is strictly stronger than `p(2^p-1)` for `p>=1`.

This is a source-audit finding, not a proof of the imported stronger statement.

## Formal trust footprint

The kernel receipt records successful compilation of a sorry-free source and ten named audited declarations. Every recorded theorem has an axiom footprint contained in

`[propext, Classical.choice, Quot.sound]`.

## Topology

This is a compact formal obstruction/relationship packet rather than a standalone-repository-scale program at present. If the project grows into a substantial all-`k` van der Waerden growth program, it should graduate to its own subject repository.
