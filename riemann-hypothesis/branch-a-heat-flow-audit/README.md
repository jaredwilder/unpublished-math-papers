# Branch A — de Bruijn–Newman heat-flow instrument and separator audit

**Author:** Jared Wilder  
**Campaign snapshot:** 2026-09-12

Branch A attacks the real-zero problem directly through the de Bruijn–Newman heat deformation. The 2026-09-12 campaign built a numerically stable instrument, rigorously validated its finite zero window, and then used exact controls to kill two candidate separators.

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

The finite trend is real for the computed window. It is not a global theorem.

## 2. Rigorous truncation envelope

A 64-piece moment envelope bounds the omitted series tail without assuming RH or zero reality.

The resulting zero-displacement bounds at five representative arguments are:

| z | |H'(z)| | tail bound | zero-shift bound |
|---:|---:|---:|---:|
| 28.27 | 8.6392409e-5 | 1.1592991e-92 | 1.3418993e-88 |
| 40 | 3.6727516e-6 | 1.5479213e-68 | 4.2146093e-63 |
| 55 | 1.7102818e-8 | 2.1524551e-46 | 1.2585383e-38 |
| 70 | 6.0856702e-11 | 1.2905240e-29 | 2.1205948e-19 |
| 85 | 2.1273686e-13 | 4.2504907e-16 | 1.9980039e-3 |

Thus the reported zero window is numerically meaningful at the stated locations; at `z=85` the rigorous shift bound is still about `0.002`, much smaller than the observed spacing scale.

## 3. Pair energy is not sufficient for real-rootedness

The campaign then tested the statistic on exact finite controls where the root geometry is known exactly.

Fresh rerun during public extraction:

| control | verified geometry | pair energy |
|---|---|---:|
| REAL, all roots in [-1,1] | all real | 1.463528208 |
| REAL2, T6 | all real | 5.925769425 |
| COMPLEX, T4+3 | four complex roots | **0.0** |
| MIXED, T4+0.5 | all real | 2.311389502 |

Therefore no simple upper ceiling on this pair energy can certify real-rootedness: an explicitly complex control has energy exactly zero while real controls can have much larger values.

The route is dead as a sufficient criterion.

## 4. Hermite minors calibrate correctly on finite controls

A Hermite/minor separator was then calibrated on objects whose roots are exactly known.

Fresh rerun:

- roots `{1,2,3}`: minors `3,6,4`, all positive;
- roots `{-1,0,1,4}`: minors `4,56,1448,14400`, all positive;
- roots `{1,i,-i}`: minors `3,-4,-16`, not all positive.

Across a larger finite bench:

- 7 all-real controls;
- 17 controls with complex roots;
- `all minors positive` held **exactly** on the all-real controls.

So the theorem/probe itself is informative on finite polynomial objects.

## 5. But the natural entire-function truncations are contaminated

Applied to polynomial truncations of the actual entire function, the same Hermite probe stays negative because the truncations themselves contain many spurious complex roots:

| truncation degree | real roots | all normalized Hermite minors positive? | minimum minor |
|---:|---:|---|---:|
| 10 | 0/10 | no | -22.32367 |
| 16 | 2/16 | no | -33.68952 |
| 22 | 2/22 | no | -43.91052 |
| 26 | 2/26 | no | -50.31204 |
| 30 | 2/30 | no | -56.48672 |
| 34 | 4/34 | no | -62.48664 |

Hence a correct finite-polynomial real-rootedness test is **uninformative on this approximation sequence**: the approximants do not preserve the target geometry closely enough.

This is a structural obstruction to the truncation route, not a failure of the Hermite theorem.

## 6. Current status

The Branch A instrument remains useful for heat-flow computations. What the campaign lacks is a quantity that is simultaneously:

1. sufficient for excluding non-real zeros / collisions;
2. computable or rigorously boundable on the actual entire function;
3. stable under the approximation method used to evaluate it.

The pair energy fails (1). The Hermite-truncation route fails (3).

The exact source programs and historical outputs from this packet should be preserved beside this README.