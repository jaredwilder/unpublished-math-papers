# 67.3015452606% simple-zero proportion — machine-checked candidate extension

**Author:** Jared Wilder  
**Campaign date:** 2026-08-11  
**Public estate release:** 2026-09-11  
**Status:** research result / computer-assisted candidate extension; **not a proof of the Riemann Hypothesis and not a peer-reviewed theorem announcement**.

This packet records a machine-checked extension of a seven-point Gram-stability argument for simple zeros of the Riemann zeta function.

## Finite local inequality

For every six-tuple of nonnegative gaps `g_1,...,g_6`, define

```text
F_q(g)
 = q * sum_i g_i
 + sum_{r=1}^6 [2/(7-r)] * sum_{i=1}^{7-r}
     w(g_i + ... + g_{i+r-1}),
```

where `w=k^2` is the normalized Montgomery--Taylor overlap kernel.

The terminal certificate uses

```text
q = 29/100000,
L = 341/100000.
```

The included verifier established

```text
F_q(g_1,...,g_6) >= L
```

for all `g_i >= 0`.

Two different grid resolutions passed:

- grid 1000: 905,465 visited boxes, 452,368 splits, maximum depth 37, zero terminal failures;
- grid 2000: 901,897 visited boxes, 450,584 splits, maximum depth 38, zero terminal failures.

The verifier uses high-precision interval enclosures for the transcendental kernel and its derivatives, outward-rounded IEEE-754 bounds downstream, range-minimum tables, exhaustive subdivision, and an outward-rounded interval LDL test for Hessian positivity before convex-tangent pruning.

`verify_seven_generalized_numba.py` is the exact recovered source used for those two runs.

An Arb/python-flint implementation, `verify_seven_q29_arb.py`, was mechanically adapted from the public 67.30085% seven-point verifier. In the source campaign it was syntax-checked but **not executed**, because `python-flint` could not be installed in that sandbox. Publication-grade parity with that public draft therefore still requires rerunning the Arb version in a compatible environment.

## Analytic propagation

Let

```text
H_MT = 3/2 - (1/sqrt(2)) cot(1/sqrt(2))
     = 0.6725007036794116457...
```

The stability refinement used by the packet gives

```text
N_0^s(T,2T)
  >= H_MT N(T,2T) + D(M°) - o(N(T,2T)),
```

where `D` is the convex Gram defect of the retained simple-zero vectors.

### Generalized seven-point block lemma

Suppose the local inequality holds for arbitrary `q>0`, `L>0`. For `m>=7` ordered normalized simple-zero ordinates

`y_1 < ... < y_m`,

summing over all `m-6` consecutive seven-point windows gives

```text
E_m + 6q(y_m-y_1) >= L(m-6),
```

where

```text
E_m = 2 * sum_{1<=i<j<=m} w(y_j-y_i).
```

A pair spanning `r` gaps occurs in at most `7-r` windows, cancelling the coefficient `2/(7-r)`, while each single gap occurs in at most six windows.

Put

`A=L(m-6)`.

When `A<1`, the same block-defect inequality used in the public stability proof yields

```text
D(M°)
 >= [A/m] N_0^s(T,2T)
    - [6q(m-1)/m] N(T,2T)
    - o(N(T,2T)).
```

Substitution gives the exact transfer formula

```text
kappa(q,L,m)
 = [m H_MT - 6q(m-1)] / [m - L(m-6)]
```

for fixed `m>=7` with `L(m-6)<1`.

## Terminal parameters and candidate bound

Take

```text
q = 29/100000,
L = 341/100000,
m = 299.
```

Then

```text
L(m-6) = 99913/100000 < 1,
6q(m-1) = 51852/100000.
```

The packet therefore obtains

```text
liminf_{T->infinity} N_0^s(T,2T)/N(T,2T)
 >= [29,900,000 H_MT - 51,852] / 29,800,087
 = 0.673015452606376894384837055845...
```

or

> **67.3015452606376894...%**

for the simple-zero proportion in the precise framework and notation of the underlying stability argument.

## Comparison recorded by the source campaign

The packet compares this constant with:

- `67.250070367941...%` from the earlier Claude/Anthropic Theorem D line;
- `67.300852792778...%` from the same-day public seven-point stability draft.

The numerical increment over the latter is about

`0.0006924678597` percentage points.

Those comparisons are historical context from the source packet, not a claim that the surrounding draft literature has completed peer review.

## What is actually closed in this packet

1. The transfer algebra from a seven-point local inequality `(q,L)` to the displayed global constant is exact inside the stated argument.
2. The local inequality for `q=29/100000`, `L=341/100000` passed exhaustive outward-rounded interval verification on two distinct grids in the recovered verifier.
3. The resulting constant is the exact expression displayed above.
4. The Arb trust-base implementation exists but was not executed in the source environment.
5. The surrounding result remains a research candidate pending independent reproduction and expert/peer review.

## Reproduction

Recovered terminal verifier:

```bash
python verify_seven_generalized_numba.py 1000 29 100000 341 100000
python verify_seven_generalized_numba.py 2000 29 100000 341 100000
```

For the Arb route, `verify_seven_q29_arb.py` expects the `kernel.py`, `rounding.py`, and `report.py` modules from the public `zeta_simple_zeros` verifier package and requires `python-flint`.

## Claim ceiling

This directory does **not** claim:

- the Riemann Hypothesis;
- a new theorem about all zeros without the hypotheses/framework of the underlying stability argument;
- independent third-party reproduction;
- peer review;
- historical priority beyond the dated campaign artifact.

It is released because the underlying mathematics and verifier are real estate assets and should not remain buried in a private transcript.