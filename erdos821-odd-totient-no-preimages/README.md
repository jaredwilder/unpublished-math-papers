# Erdős #821 — odd totient targets have no preimages

**Author:** Jared Wilder  
**Public extraction:** 2026-09-11  
**Status:** mathematically audited exact domain reduction.

Let

`g(n)=#{ m>=1 : φ(m)=n }`.

## Theorem

For every odd integer `n>1`,

`g(n)=0`.

## Proof

For every `m>=3`, the reduced residue classes modulo `m` pair under

`a -> -a`.

There are no fixed points among units: a fixed point would satisfy `2a≡0 (mod m)`, which for a unit `a` would force `m|2`, impossible for `m>=3`. Therefore the units occur in pairs and `φ(m)` is even.

The only odd totient value arising at the two exceptional inputs is

`φ(1)=φ(2)=1`.

Thus no odd `n>1` lies in the image of Euler's totient function.

## Scope

This is a strong domain filter for the preimage-count problem, not a solution of the remaining even-target questions.
