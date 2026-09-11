# Complete curated witness ledger — 21 independently validated finite objects

**Author:** Jared Wilder  
**Source:** `ERDOS_COMPLETE_NOVELTY_MAGNITUDE_LEDGER_2026-09-02.xlsx`, `Witness_21` tab  
**Public extraction:** 2026-09-11

The September curated release contained **21 / 21 validated witness rows**. This file gives every row a public disposition. A witness proves only its exact finite statement; it does not inherit a stronger campaign status.

Where the original object bytes or full coordinate/block list already have a better public home, this ledger points there rather than creating another conflicting copy.

| ID | source name | exact object / claim | validation | public meaning |
|---|---|---|---|---|
| W001 | `run5_english_sidon35` | 35-element Sidon subset of `[1,2000]` | independently valid | benchmark only; no record claim |
| W002 | `run5_english_apfree512` | 512-element 3AP-free subset of `[1,10000]` | independently valid | ternary-style known construction family |
| W003 | `run5_msl_sidon35` | same 35-element Sidon object as W001 | valid | duplicate benchmark used for MSL/English reproducibility |
| W004 | `run5_msl_apfree512` | same 512-element 3AP-free object as W002 | valid | duplicate benchmark |
| W005 | `run8_english_sidon22` | 22-element Sidon subset of `[1,500]` | valid | below known exact maximum 26 |
| W006 | `run8_msl_sidon21` | 21-element Sidon subset of `[1,500]` | valid | below known exact maximum 26 |
| W007 | `run9_english_apfree150` | 150-element 3AP-free subset of `[1,2000]` | valid | benchmark/search object |
| W008 | `run9_msl_apfree150` | second 150-element 3AP-free subset of `[1,2000]` | valid | benchmark/search object |
| W009 | `run20_C13_6_3_cover21` | 21-block `(13,6,3)` covering | all 286 triples covered | candidate data novelty; full block list public in `jaredwilder/combinatorial-records/covering-designs/C13-6-3/` |
| W010 | `run23b_C13_6_3_cover21` | second 21-block `(13,6,3)` covering | all 286 triples covered | candidate data novelty; full block list public in the same covering-design packet |
| W011 | `run11_distinct_subset_sums14` | 14-element distinct-subset-sum set, powers-of-two calibration construction | valid | mathematically trivial calibration witness |
| W012 | `run19_sidon8_size4` | size-4 Sidon subset of `[1,8]` | valid + optimality receipt | known exact small optimum; upper half kernel-certified elsewhere |
| W013 | `erdos979_f2_410_collision` | two unordered two-prime-square representations at `n=410`: `{7,19}`, `{11,17}` | exact recheck | finite collision only |
| W014 | `erdos930_k2_square_product` | exact `r=2,k=2` square-product witness | exact recheck | subsumed by infinite Pell family |
| W015 | `erdos930_k3_square_product` | exact `r=2,k=3` square-product witness | exact recheck | proves threshold cannot be <=3 |
| W016 | `ab_distinct_distances_4x3_grid` | 12-point `4×3` integer grid with exactly 8 distinct nonzero squared distances | exact recheck | A/B benchmark, no record claim |
| W017 | `erdos1_sumdistinct_5_N13` | `{6,9,11,12,13}` has all 32 subset sums distinct | exhaustive recheck | forces `C<13/32` in frozen strict formulation |
| W018 | `erdos213_n4_general_position_integer_distances` | four planar points, all six distances integral, no three collinear, not concyclic | exact recheck | solves finite `n=4` slice only; known constructions go farther |
| W019 | `erdos389_n2_k5_divisibility` | `720 | 55440`, quotient 77, frozen `n=2,k=5` witness | exact | known/public finite witness |
| W020 | `erdos1142_R001_L1_counterexample` | `n=21,p=5`: `21-2,21-4,21-8,21-16 = 19,17,13,5` all prime but `5∤21` | exact | internal regression killing an overstrong campaign lemma, **not** a counterexample to #1142 |
| W021 | `erdos930_pell_family_prefix` | six sampled members of the exact `r=2,k=2` Pell family | recurrence recheck | duplicate evidence for the theorem asset, not separate novelty |

## Two covering witnesses — exact public status

The two `C(13,6,3)` objects are the only rows in this witness ledger carrying serious candidate data-novelty status. Both are at the current best-known 21-block upper size and were found non-isomorphic to each other and to the displayed benchmark representative under the campaign's incidence/isomorphism checks. Global archival class novelty is **not** certified until comparison against the full design archive is complete.

The stronger target-20 structural theorem is maintained separately in `jaredwilder/combinatorial-records/covering-designs/C13-6-3/`. No 20-block UNSAT certificate is currently claimed.

## Regression witnesses are first-class public mathematics

W020 is deliberately retained even though it is a counterexample to an internal lemma rather than a parent problem. It is an exact falsifier:

\[
21-2=19,\quad21-4=17,\quad21-8=13,\quad21-16=5.
\]

Thus any theorem claiming that `Good(n)`, `p<=n/2`, and `ord_p(2)=p-1` force `p|n` without the repaired strict threshold is false. The corrected theorem is public in `../erdos1142-order-sieve/`.

## Scope / novelty discipline

The original witness ledger classifies most rows as benchmark, known, duplicate, or subsumed. This release preserves that. Validation means the finite object satisfies the stated predicate; it does not mean the object is historically new or extremal.

## License

Apache-2.0 for repository-authored material. Underlying upstream benchmark objects retain any source-specific provenance recorded by their original campaign files.
