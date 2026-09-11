# Erdős Problem #271 — Stanley Sequences

Public release of the audited 2026-08-06 Encirclement campaign on greedy Stanley sequences, with central attention to `A(4)`.

## Claim boundary

**The flagship problem is not closed.** Historical novelty is not asserted by this release. Every statement keeps its audited status: proved, proved-with-correction, conditional, finite-only, target/conjecture, external dependency, exploratory, or retired/refuted.

The audited master ledger contains **184 entries**:

- 111 `RETAINED_PROVED`
- 27 `RETAINED_PROVED_WITH_CORRECTION`
- 1 `RETAINED_PROVED_SUBSUMED`
- 13 `CONDITIONAL_THEOREM`
- 18 `CONJECTURE_OR_TARGET`
- 7 `REFUTED_OR_RETIRED`
- 4 `COMPUTATIONALLY_VERIFIED_FINITE`
- 2 `EXPLORATORY_UNVERIFIED`
- 1 `EXTERNAL_DEPENDENCY`

## Terminal retained reduction

For a Stanley prefix `A_k={a_0,...,a_k}`, define the oriented reflection support

`U_k = {2 a_j - a_i : 0 <= i < j < k}`

and mean multiplicity

`mu_k = binom(k,2) / |U_k|`.

The campaign reduces fixed-seed growth to

`a_k = Theta(k + k^2 / mu_k)`.

Using superlinearity of infinite Stanley sequences, this becomes

`a_k = Theta(k^2 / mu_k)`.

For `A(4)`, the historic target

`a_k = Theta(k^2 / log k)`

is therefore equivalent, within the campaign reduction, to

`mu_k = Theta(log k)`

and to

`|U_k| = Theta(k^2 / log k)`.

The proposed Ternary Scale Mixing Lemma did **not** survive audit as proved; it remains outside the theorem layer.

## Files

The full audited ledger is split only for navigability:

- `ledger-001-046.md`
- `ledger-047-092.md`
- `ledger-093-138.md`
- `ledger-139-184.md`

Status labels and audit corrections are load-bearing. Later corrected formulations supersede earlier overstrong versions.

## Strong recurring structures

The ledger develops exact greedy dynamics through difference sets, decimated correlations, hole ancestry, reflection supports, first-killer partitions, multiplicity fibers, support-utilization bounds, and finite computation. Negative results and failed closure mechanisms are retained because they constrain future attacks.
