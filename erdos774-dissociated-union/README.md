# Erdős #774 — easy direction for unions of dissociated sets

**Author:** Jared Wilder  
**Public extraction:** 2026-09-11

Suppose

\[
A=A_1\cup\cdots\cup A_k
\]

and every `A_i` is dissociated.

## Theorem

Every finite subset `B⊆A` contains a dissociated subset of size at least

\[
\boxed{|B|/k}.
\]

## Proof

The sets `B∩A_i` cover `B`. By the pigeonhole principle, for some `i`,

\[
|B\cap A_i|\ge |B|/k.
\]

Because `A_i` is dissociated, every subset of `A_i`, in particular `B∩A_i`, is dissociated.

## Scope

This is the easy implication. The converse-type structural direction in the parent problem remains separate.
