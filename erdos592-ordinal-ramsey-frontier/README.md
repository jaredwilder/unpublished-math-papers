# Erdős #592 — kernel-checked ordinal Ramsey frontier

**Author:** Jared Wilder  
**Formal campaign:** 2026-09-05  
**Human extraction:** 2026-09-11

This is the human subject front door for the Lean development previously buried inside `erdos-campaign-archive/campaigns/erdos592-close-2026-09-05/`.

The formal corpus consists of three Lean files plus build receipts. The main development is approximately 21 KB and is sorry-free in the recorded campaign build.

## Problem

For a countable ordinal `β`, write

\[
P(β):\qquad \omega^β\to(\omega^β,3)^2.
\]

Erdős #592 asks for the countable ordinals `β` satisfying `P(β)`.

The formal development uses the same ordinal/cardinal Ramsey predicate as the FormalConjectures encoding rather than a simplified surrogate.

## Five-way frontier decomposition

The Lean file defines five disjoint classes of ordinals `β` according to the known literature structure:

- **Class A:** `β<3`;
- **Class B:** `β>=3` but `β` is not additively indecomposable;
- **Class C:** `β=ω^γ` where the Cantor-normal-form indecomposable count of `γ` is at most two;
- **Class D:** `β=ω^γ` where that count is exactly three;
- **Class E:** `β=ω^γ` where that count is at least four.

The formal development proves outright, in Lean:

\[
\boxed{\text{every ordinal lies in at least one of A--E}}
\]

and

\[
\boxed{\text{the five classes are mutually exclusive}.}
\]

The corresponding theorem names are `frontier_exhaustive` and `frontier_exclusive`.

## Least unresolved class member

The campaign formalizes the Cantor-normal-form summand count `indecCount` and proves

\[
\operatorname{indecCount}(3)=3.
\]

Hence

\[
\beta=\omega^3
\]

belongs to Class D. More strongly, Lean proves

\[
\boxed{\omega^3\le \beta\qquad\text{for every }\beta\in\mathrm{ClassD}.}
\]

Thus, under the literature identification of Class D as the unresolved region, the least unresolved instance is the partition relation

\[
\boxed{\omega^{\omega^3}\to(\omega^{\omega^3},3)^2\ ?}
\]

The formal theorem is `omega_pow_three_least`; `ClassD_least` packages membership and minimality together.

## Exact reduction to the three-summand class

A separate Lean file carries the settled literature regions as **explicit hypotheses**:

- Class A positive;
- Class B negative;
- Class C positive;
- Class E negative.

It then proves that all remaining uncertainty is exactly the restriction of `P` to Class D:

`erdos592_reduces_to_ClassD`.

This distinction is load-bearing. Lean proves the logical reduction and ordinal classification. It does **not** reprove Specker, Chang, Galvin–Larson or Schipperus from first principles; their verdicts enter the reduction as named assumptions.

## Galvin–Larson answer warning

The formal-conjecture TODO historically points toward the Galvin–Larson condition. The campaign makes the literature correction explicit.

Define the Galvin–Larson conjectured answer set by

\[
β<3\quad\text{or}\quad β=\omega^γ.
\]

The Lean reduction proves that, **assuming Schipperus' negative verdict on Class E**, this proposed answer is false. The explicit formal witness is

\[
\boxed{β=\omega^4,}
\]

which lies in the conjectured answer set but in Class E.

This is theorem `galvin_larson_conjecture_false'`. Again, the Schipperus verdict is an explicit premise, not hidden inside the kernel proof.

## No monotonicity bridge

The formal development also proves a useful structural negative theorem. Assuming the three small literature facts

\[
P(2),\qquad \neg P(3),\qquad P(\omega),
\]

the answer set is neither upward nor downward closed in the ordinal order. Thus no bare monotonicity principle can bridge the known positive and negative regions into Class D.

The theorem is `no_monotone_bridge`.

## Unconditional formal assets

Independent of the external literature verdicts, the main file proves several reusable facts, including:

- monotonicity in the blue-cardinality parameter;
- the triangle-free-neighbourhood lemma converting absence of a blue triangle into a red clique neighbourhood;
- the `β=0` instance `P_zero` outright;
- ordinal/Cantor-normal-form arithmetic used to classify the five regions;
- membership of `ω`, `ω^2`, `ω^3`, `ω^4` in the appropriate classes;
- exhaustiveness, exclusivity, nonemptiness and least-element facts for the unresolved class.

## Formal source

Canonical provenance currently remains in:

```text
jaredwilder/erdos-campaign-archive/
  campaigns/erdos592-close-2026-09-05/
    Erdos592Frontier.lean
    Erdos592Reduction.lean
    Erdos592Audit.lean
    receipts/
```

The campaign archive records **28 kernel-checked theorems** across this program.

## Repository status

This program is unquestionably standalone-repository scale: a coherent open problem, a multi-file Lean development, a complete formal frontier partition, an exact least-unresolved-instance theorem, a literature-aware reduction, and receipts.

Until a dedicated `erdos592` repository shell exists, this directory is the preferred human reading/citation surface and the campaign archive is the byte-level provenance source.
