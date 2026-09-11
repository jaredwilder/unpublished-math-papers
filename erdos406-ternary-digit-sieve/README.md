# Erdős #406 — 3-adic exponent sieve for powers of two with ternary digits `{0,1}`

**Author:** Jared Wilder  
**Public extraction:** 2026-09-11  
**Status:** mathematically audited exact congruence sieve; no global close claimed.

## Theorem

Suppose every ternary digit of `2^n` is either `0` or `1`. Then

`n mod 18 ∈ {0,2,6,8}`.

More generally, for every `r>=1`, reducing modulo `3^r` shows that the allowed exponents form exactly

`2^(r-1)` residue classes modulo

`φ(3^r)=2·3^(r-1)`.

## Proof

Modulo `3^r`, a number whose first `r` ternary digits are all in `{0,1}` has residue

`ε_0 + ε_1 3 + ... + ε_{r-1}3^(r-1)`,  with each `ε_i∈{0,1}`.

There are `2^r` such residues. Exactly half are units modulo `3^r`, namely those with `ε_0=1`, so there are `2^(r-1)` possible unit residues.

The integer `2` is a primitive root modulo every power `3^r`. Therefore the map

`n mod 2·3^(r-1)  ->  2^n mod 3^r`

is a bijection onto the units. Hence precisely `2^(r-1)` exponent classes survive the ternary `{0,1}` restriction.

For `r=3`, modulo `27`, the four surviving exponent classes are

`n ≡ 0,2,6,8 (mod 18)`.

## Scope boundary

This is a necessary congruence sieve. A stronger Senge–Straus-style close that appeared in the source workflow was blacklisted; this exact finite-level sieve is the surviving theorem.
