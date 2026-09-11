# Erdős #968 — exact reformulation of prime-ratio monotonicity

**Author:** Jared Wilder  
**Public extraction:** 2026-09-11  
**Status:** exact algebraic reformulation; density questions remain open.

Let `p_n` be the `n`-th prime and let

`d_n=p_{n+1}-p_n`.

## Theorem

For every `n>=1`,

`p_n/n < p_{n+1}/(n+1)`

if and only if

`n d_n > p_n`,

or equivalently

`d_n > p_n/n`.

## Proof

Since `n(n+1)>0`, cross-multiplication gives

`p_n(n+1) < n p_{n+1}`.

Using `p_{n+1}=p_n+d_n`, this becomes

`np_n+p_n < np_n+n d_n`,

hence exactly

`p_n < n d_n`.

Dividing by `n` gives the final equivalent form.

## Scope

This converts the monotonicity event for `p_n/n` into a prime-gap inequality. It does not prove any positive-density or infinitude statement for those events.
