# Branch A — de Bruijn–Newman heat-flow instrument and separator audit

**Author:** Jared Wilder  
**Campaign snapshot:** 2026-09-12  
**Forensic correction:** 2026-09-12

Branch A attacks the real-zero problem directly through the de Bruijn–Newman heat deformation. The campaign built a numerically stable finite-window instrument and then used exact controls to kill two candidate separators.

The result is a useful **instrument + negative-theorem packet**, not an RH proof.

## 1. Sized heat-flow zero computation

A high-precision moment-series evaluator was run at `dps=70`, truncation order `K=80`, through `|z|<=85`.

Seven zeros were obtained at each of `t=0.2,0,-0.2`. The pair-energy statistic

\[
E(t)=\sum_{i<j}\frac1{(z_i-z_j)^2}
\]

rose across the three slices:

| t | E(first 6 zeros) | E(all 7 zeros) |
|---:|---:|---:|
| +0.20 | 0.09964308 | 0.13036998 |
| 0.00 | 0.10092331 | 0.13159389 |
| -0.20 | 0.10241583 | 0.13301904 |

The finite trend is a floating-point computation on the stated truncation. It is not a global theorem.

## 2. Truncation-envelope computation — **not a rigorous certificate in its current form**

The historical packet called its 64-piece envelope “rigorous” and printed the following numerical tail/shift estimates:

| z | computed `|H'(z)|` | computed tail estimate | reported zero-shift estimate |
|---:|---:|---:|---:|
| 28.27 | 8.6392409e-5 | 1.1592991e-92 | 1.3418993e-88 |
| 40 | 3.6727516e-6 | 1.5479213e-68 | 4.2146093e-63 |
| 55 | 1.7102818e-8 | 2.1524551e-46 | 1.2585383e-38 |
| 70 | 6.0856702e-11 | 1.2905240e-29 | 2.1205948e-19 |
| 85 | 2.1273686e-13 | 4.2504907e-16 | 1.9980039e-3 |

A later source audit found that the code obtains each quantity named a cell maximum by evaluating the kernel at **41 grid points**:

```python
PM = [
    max(abs(Phi(edges[p] + (edges[p+1]-edges[p])*i/40)) for i in range(41))
    for p in range(P)
]
```

That is a sampled maximum, not a certified upper bound for the supremum on the cell. The moments, derivatives and zero-shift calculations are also ordinary `mpmath` floating-point calculations rather than directed-rounding interval enclosures.

Therefore the table is **numerical evidence only**. The previous claim that it rigorously localized the zeros is retracted.

A rigorous replacement would require at least:

- a certified upper bound for `sup |Phi|` on every cell, or a proved analytic monotonicity bound;
- directed-rounding control of moment and tail arithmetic;
- a certified lower bound for `|H'|` on the localization interval;
- a root-existence/uniqueness argument that converts function/derivative enclosures into a zero enclosure.

Until those are supplied, no finite zero in this packet is advertised as rigorously localized by this envelope.

## 3. Pair energy is not sufficient for real-rootedness

The campaign tested the statistic on exact finite controls where the root geometry is known exactly.

Fresh rerun during public extraction:

| control | verified geometry | pair energy |
|---|---|---:|
| REAL, all roots in [-1,1] | all real | 1.463528208 |
| REAL2, T6 | all real | 5.925769425 |
| COMPLEX, T4+3 | four complex roots | **0.0** |
| MIXED, T4+0.5 | all real | 2.311389502 |

Therefore no simple upper ceiling on this pair energy can certify real-rootedness: an explicitly complex control has energy zero while real controls can have substantially larger values.

That candidate sufficient criterion is dead.

## 4. Hermite minors calibrate correctly on finite controls

A Hermite/minor separator was calibrated on objects whose roots are exactly known.

Fresh rerun:

- roots `{1,2,3}`: minors `3,6,4`, all positive;
- roots `{-1,0,1,4}`: minors `4,56,1448,14400`, all positive;
- roots `{1,i,-i}`: minors `3,-4,-16`, not all positive.

Across the larger finite bench in the historical packet:

- 7 all-real controls;
- 17 controls with complex roots;
- `all minors positive` held exactly on the tested all-real controls.

This is a finite control calibration, not a new Hermite theorem.

## 5. Natural entire-function truncations are contaminated

Applied to polynomial truncations of the actual entire function, the same probe stays negative because those truncations themselves contain many complex roots:

| truncation degree | real roots | all normalized Hermite minors positive? | minimum minor |
|---:|---:|---|---:|
| 10 | 0/10 | no | -22.32367 |
| 16 | 2/16 | no | -33.68952 |
| 22 | 2/22 | no | -43.91052 |
| 26 | 2/26 | no | -50.31204 |
| 30 | 2/30 | no | -56.48672 |
| 34 | 4/34 | no | -62.48664 |

Hence a correct finite-polynomial real-rootedness test can be uninformative on this approximation sequence: the approximants do not preserve the desired root geometry.

This is a route-specific obstruction, not a failure of Hermite theory.

## 6. Current status

The Branch A instrument remains useful for exploratory heat-flow computation. What is missing is a quantity that is simultaneously:

1. sufficient for excluding non-real zeros / collisions;
2. rigorously evaluable or boundable on the actual entire function;
3. stable under the approximation used to compute it.

The pair energy fails (1). The natural Hermite-truncation route fails (3). The historical 64-piece envelope has **not** yet established (2) rigorously.

The exact source programs and historical outputs are preserved because they are useful ore, but their evidence class is now stated correctly.
