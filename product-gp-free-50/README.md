# Simultaneously product-free and 3-term-GP-free subsets of [50]

**Author:** Jared Wilder  
**Release:** September 2026

Let `A ⊆ {1,...,50}` satisfy both:

1. **product-free:** for every `x,y ∈ A`, including `x=y`, the product `xy` is not in `A`; and
2. **nontrivial 3-term geometric-progression-free:** there are no distinct `a<b<c` in `A` with `b²=ac`.

## Exact result

Every such set has size at most **35**, and this bound is attained.

The finite forbidden-hypergraph classification also yields:

- minimum transversal size: **15**;
- number of maximum sets: **240**;
- forbidden-edge count in the frozen model: **149**;
- extremizer digest: `cea2d1f707e94d388369a9c61030dd3ce9908b8a0b981419bb90f7cfa4721188`.

One maximum witness is

```text
{5,6,9,11,13,14,15,16,17,18,19,20,21,22,23,24,26,27,28,29,31,33,34,35,37,38,39,40,41,42,43,46,47,48,50}
```

## Verification

The frozen Round-8 certificate was independently replayed in two implementations. The independent C search reported maximum 35, minimum transversal 15 and 240 extremizers after 57,726 search nodes. The independent Python replay again returned maximum 35 and 240 extremizers after 60,693 nodes, with the same extremizer digest.

This is an **exact finite classification on `[50]`**. It is not stated as an asymptotic density theorem and does not claim an infinite-family extremal result.

## Historical novelty

A systematic search dated 2026-07-27 did not locate this simultaneous finite classification. The closest literature found treats product-free sets, geometric-progression-free sets, or sum-free-and-product-free sets separately. The historical status is therefore recorded only as `apparently_new_after_systematic_search`; see `NOVELTY.md`.
