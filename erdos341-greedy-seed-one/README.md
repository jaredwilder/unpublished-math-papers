# Erdős #341 — exact greedy evolution from the seed `{1}`

**Author:** Jared Wilder  
**Public extraction:** 2026-09-11

Given a finite increasing seed `A={a_1<...<a_k}`, the frozen greedy rule appends the least integer larger than the current maximum which is not representable as `a_i+a_j` using already present terms.

## Theorem

Starting from

\[
A=\{1\},
\]

the greedy sequence is exactly

\[
\boxed{1,3,5,7,9,\ldots},
\]

the positive odd integers. Its gap sequence is therefore constantly 2.

## Proof

Inductively suppose the current set is

\[
\{1,3,5,\ldots,2m-1\}.
\]

Every pair-sum is even. Moreover these pair-sums fill every even integer from 2 through `4m-2`: write `2r=(2i-1)+(2j-1)` with `i+j=r+1` and choose `1<=i,j<=m` whenever `1<=r<=2m-1`.

The next integer after `2m-1` is `2m`, which is represented, while `2m+1` is odd and hence cannot be a pair-sum. Thus the greedy rule appends `2m+1`.

## Scope

This is one exact seed family. The universal question asking whether every finite seed eventually has periodic gaps remains separate and is not claimed solved here.
