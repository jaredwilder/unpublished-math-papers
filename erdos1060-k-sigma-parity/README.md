# Erdős #1060 — parity structure and an explicit collision for `k sigma(k)`

**Author:** Jared Wilder  
**Public extraction:** 2026-09-11  
**Status:** exact structural theorem plus finite collision; representation-multiplicity problem remains open.

## Theorem 1 — parity characterization

For every positive integer `k`,

`k sigma(k)` is odd

if and only if

`k` is an odd square.

### Proof

The product `k sigma(k)` is odd exactly when both factors are odd, so `k` must be odd and `sigma(k)` must be odd.

The classical parity characterization of the divisor-sum function says `sigma(k)` is odd exactly when `k` is a square or twice a square. Under the already-forced condition that `k` is odd, only the square case remains. Thus `k` is an odd square.

Conversely, if `k` is an odd square then `k` is odd and `sigma(k)` is odd, so their product is odd.

## Theorem 2 — noninjectivity

The map

`k -> k sigma(k)`

is not injective. Indeed,

`sigma(12)=28`, `sigma(14)=24`,

so

`12 sigma(12)=14 sigma(14)=336`.

## Scope

These facts constrain the representation problem but do not provide the requested global upper bound on the number of representations of a given value.
