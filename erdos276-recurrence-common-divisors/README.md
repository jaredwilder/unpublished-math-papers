# Erdős #276 — common divisors of Fibonacci/Lucas-type recurrences

**Author:** Jared Wilder  
**Public extraction:** 2026-09-11  
**Status:** kernel-checked theorem recovered from the formalization estate.

## Theorem

Let `a : N -> N` satisfy

`a(n+2) = a(n+1) + a(n)`

for every `n`. Then, for every positive integer `d`,

`d | a(n) for every n   <=>   d | gcd(a(0),a(1))`.

Equivalently, the common divisors of the whole recurrence are exactly the common divisors of its first two terms.

## Proof

If `d` divides every term, it divides `a(0)` and `a(1)`, hence their gcd.

Conversely, if `d | gcd(a(0),a(1))`, then `d|a(0)` and `d|a(1)`. The recurrence and closure of divisibility under addition give

`d|a(n), d|a(n+1)  =>  d|a(n+2)`.

Two-step induction proves divisibility of every term.

## Formal receipt

Recovered receipt: `fmz-erdos276-campaign-001-R004-L1.cable.json`.

The September audit classified the theorem as `KERNEL_CHECKED` with the listed theorem scope matching the formal artifact. Recorded axiom footprint: `{Quot.sound, propext}`.

## Scope

This is the exact recurrence-divisor lemma only. No stronger claim about the parent Erdős problem is implied here.
