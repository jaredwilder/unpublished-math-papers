# Erdős #479 — infinite power-congruence family

**Author:** Jared Wilder  
**Public extraction:** 2026-09-11  
**Status:** mathematically audited exact family; no claim that it resolves the full parent problem.

## Theorem

Fix an integer `j>=0` and set

`k = 2^(2^j)`.

For every odd prime `p`, let

`n = 2^j p`.

Then

`2^n ≡ k (mod n)`.

Therefore every `k` in the infinite family

`k = 2,4,16,256,... = 2^(2^j)`

has infinitely many corresponding integers `n` satisfying the congruence.

## Proof

Modulo `p`, Fermat's theorem gives

`2^(p-1) ≡ 1 (mod p)`.

The two exponents `2^j p` and `2^j` differ by `2^j(p-1)`, so

`2^(2^j p) ≡ 2^(2^j) (mod p)`.

Modulo `2^j`, both powers vanish for `j>=1`; for `j=0` the modulus is `1` and the statement is vacuous. Since `gcd(2^j,p)=1`, the Chinese remainder theorem gives

`2^n ≡ 2^(2^j) = k (mod 2^j p)= (mod n)`.

Varying the odd prime `p` gives infinitely many `n` for each fixed `j`.

## Scope

This is a constructive infinite subfamily. It does not classify all `k` for which infinitely many solutions exist.
