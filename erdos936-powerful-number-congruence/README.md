# Erdős #936 — square-cube form and mod-8 restriction for odd powerful numbers

**Author:** Jared Wilder  
**Public extraction:** 2026-09-11  
**Status:** exact structural lemma and congruence consequence; parent problem remains open.

## Lemma 1 — square-cube representation

Every odd powerful integer `m` can be written

`m=a^2 b^3`

with `b` squarefree.

### Proof

Write

`m=∏ p^{e_p}`

with every `e_p>=2`. Each exponent has a unique decomposition

`e_p = 2q_p + 3r_p`,  with `r_p∈{0,1}`.

Put the `p^{q_p}` factors into `a` and put into `b` exactly those primes for which `r_p=1`. Then `b` is squarefree and `m=a²b³`.

## Lemma 2 — mod-8 reduction

If `m` is odd and powerful and `m=a²b³` as above, then

`m ≡ b (mod 8)`.

Indeed, odd `a` satisfies `a²≡1 mod8`, while odd `b` satisfies `b³≡b mod8`.

## Consequences for `2^n±1`

For `n>=3`, both `2^n-1` and `2^n+1` are odd, with

`2^n-1 ≡ 7 (mod8)`,

`2^n+1 ≡ 1 (mod8)`.

Therefore, if either number is powerful and is written in square-cube form with squarefree cube part `b`, then respectively

- `b≡7 (mod8)` for `2^n-1`;
- `b≡1 (mod8)` for `2^n+1`.

## Scope

These are necessary structural conditions only. They do not classify all powerful values of `2^n±1`.
