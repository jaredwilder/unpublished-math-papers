# Simultaneous sum-free, product-free and 3-AP-free subsets of F_73^×

**Author:** Jared Wilder  
**Release:** September 2026

This directory records an exact finite extremal classification in the multiplicative nonzero residue set `F_73^×`.

## Frozen constraints

A subset is required simultaneously to be:

- sum-free under the frozen finite-field interpretation;
- product-free;
- free of nontrivial three-term arithmetic progressions.

## Exact result

Every admissible subset has size at most **12**. Exactly **three** extremizers attain 12:

```text
{13,15,19,31,33,36,37,40,42,54,58,60}
{10,22,24,28,33,36,37,40,45,49,51,63}
{2,3,10,19,24,31,42,49,54,63,70,71}
```

The exact forbidden-hypergraph computation has:

- modulus: `73`;
- vertices: `F_73^×`;
- forbidden-edge count: **7,422**;
- maximum: **12**;
- minimum transversal: **60**;
- extremizer count: **3**;
- search nodes: **271,416**.

## Verification

The frozen Round-10 result was checked by an independent C++ implementation whose source SHA-256 is recorded in `certificate.json`. The exact extremal layer also carries its own SHA-256. The finite result is scoped exactly to the stated three simultaneous constraints in `F_73^×`; no asymptotic or all-primes theorem is implied.

## Historical novelty

The 2026-07-27 search found related literature on sum-free sets in finite abelian groups, product-free subsets of groups, complete 3-term-progression-free sets, simultaneous sum/product avoidance in integers, and finite-field sum-product estimates. It did not locate this exact simultaneous three-condition problem at modulus 73 or the maximum-12/three-extremizer classification. The historical label is therefore only `apparently_new_after_systematic_search`.
