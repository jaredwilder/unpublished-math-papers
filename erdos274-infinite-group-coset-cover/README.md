# Erdős #274 — finite exact coset covers of infinite groups

**Author:** Jared Wilder  
**Public extraction:** 2026-09-11  
**Status:** exact cardinality reduction.

## Theorem

Let an infinite group `G` be partitioned into finitely many left cosets

`G = C_1 ⊔ ... ⊔ C_t`,

and suppose the cardinalities `|C_i|` are pairwise distinct. Then `t=1`.

Equivalently, any nontrivial finite exact coset cover whose parts have pairwise-distinct cardinalities must occur in a finite group.

## Proof

Because `G` is infinite, a finite union of subsets each having cardinality strictly smaller than `|G|` still has cardinality strictly smaller than `|G|`. Hence at least one coset, say `C_i=gH`, has

`|H|=|C_i|=|G|`.

If `H` is proper, choose `x∉gH`. The coset of `H` containing `x` is disjoint from `gH` and has the same cardinality `|H|=|G|`. Since the displayed cosets partition all of `G`, that second `H`-coset must be covered by some of the remaining finitely many parts. A finite union of parts all of cardinality `<|G|` cannot cover a set of cardinality `|G|`; therefore some other part also has cardinality `|G|`, contradicting pairwise distinctness.

Thus `H=G`, so `gH=G` is already the whole group and the partition has only one part.

## Scope

This is a reduction theorem. It does not classify the finite-group case.
