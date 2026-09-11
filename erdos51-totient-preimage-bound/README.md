# Erdős #51 — elementary size bound for totient preimages

**Author:** Jared Wilder  
**Public extraction:** 2026-09-11  
**Status:** exact universal bound; parent existence question remains open.

Suppose

`phi(n)=a`

and let

`r=omega(n)`

be the number of distinct prime divisors of `n`.

## Theorem

Then

`r! <= a`

and

`n/a <= 2^r`.

Consequently, if

`R(a)=max{r : r!<=a}`,

then every preimage of `a` satisfies

`n <= a * 2^(R(a))`.

## Proof

Write the distinct prime divisors of `n` as `p_1<...<p_r`. Euler's product formula gives

`a=phi(n)=n ∏_{p|n}(1-1/p)`.

Thus

`n/a = ∏_{p|n} p/(p-1) <= 2^r`,

because each factor is at most `2`.

Also

`phi(n)=∏ p_i^(e_i-1)(p_i-1) >= ∏(p_i-1)`.

The `i`-th distinct prime is at least `i+1`, so `p_i-1>=i`. Hence

`a >= ∏_{i=1}^r i = r!`.

Therefore `r<=R(a)`, and substituting into the first estimate yields

`n <= a 2^r <= a 2^(R(a))`.

## Scope

The theorem bounds every totient preimage once one exists. It does not decide which `a` actually occur as totients, nor the parent campaign's canonical existence question.
