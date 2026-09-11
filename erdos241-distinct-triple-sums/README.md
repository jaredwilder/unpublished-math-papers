# Erdős #241 — exact counting bound for distinct 3-multiset sums

**Author:** Jared Wilder  
**Public extraction:** 2026-09-11  
**Status:** elementary exact counting theorem.

## Theorem

Let `A⊂{1,...,N}` have `|A|=m`. Suppose all sums

`a+b+c`

are distinct when `{a,b,c}` ranges over unordered triples from `A` with repetition allowed. Then

`C(m+2,3) <= 3N-2`.

In particular,

`m^3 < 18N`.

## Proof

The number of unordered triples with repetition drawn from an `m`-element set is

`C(m+2,3)`.

By hypothesis they give that many distinct integer sums. Every such sum lies between `3` and `3N`, inclusive, an interval containing exactly `3N-2` integers. Therefore

`C(m+2,3) <= 3N-2`.

Also

`C(m+2,3)=m(m+1)(m+2)/6 > m^3/6`,

so `m^3/6 < 3N`, hence `m^3<18N`.

## Authority note

The estate contained stronger constants attributed to the same counting argument. Those were quarantined. This release preserves the exact constant that follows from the argument above.
