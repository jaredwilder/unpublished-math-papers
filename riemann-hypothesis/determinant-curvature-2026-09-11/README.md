# Riemann-zeta determinant curvature — exact identities and a computational fixed-slope frontier

**Author:** Jared Wilder  
**Campaign snapshot:** 2026-09-11  
**Public extraction:** 2026-09-11

This directory extracts the strongest surviving mathematics from an **active 30-round snapshot** of a larger MSL attack on the Riemann Hypothesis. The source request asked for 100 rounds; the exported state contains 30 recorded rounds and is not represented here as a completed 100-round campaign.

The useful output splits sharply into two authority classes:

1. **exact algebraic identities** for consecutive Toeplitz minors and their reciprocal/Jacobi–Trudi duals;
2. **finite numerical evidence** for a positive fixed-slope limit of a normalized determinant-curvature quantity.

The second class is not upgraded into an asymptotic theorem.

## 1. Exact curvature identity

For a coefficient sequence `a=(a_0,a_1,...)`, write

`D_{r,k} = det[a_{k+j-i}]_{i,j=0}^{r-1}`

whenever the displayed minors are defined and nonzero. Define

`Q_{r,k} = D_{r,k-1} D_{r,k+1} / D_{r,k}^2`.

Desnanot–Jacobi gives

`D_{r+1,k} D_{r-1,k} = D_{r,k}^2 - D_{r,k-1} D_{r,k+1}`,

hence exactly

`D_{r,k-1}D_{r,k+1} / (D_{r+1,k}D_{r-1,k}) = Q_{r,k}/(1-Q_{r,k})`.

The campaign quantity

`Z_{r,k} = (r/k) * D_{r,k-1}D_{r,k+1}/(D_{r+1,k}D_{r-1,k})`

therefore satisfies the exact identity

`Z_{r,k} = (r/k) * Q_{r,k}/(1-Q_{r,k})`.

There is no asymptotic input here: `Z` is simply a reparameterization of shift-direction Toeplitz curvature.

### Fixed slope

On `k = m r`,

`Z = (1/m) Q/(1-Q)`.

Thus, whenever a fixed-slope limit exists,

- `Z -> A > 0` iff `Q -> mA/(1+mA)` in `(0,1)`;
- `Z -> 0` iff `Q -> 0`.

The source state accidentally marked this equivalence stale because it inherited an unnecessary dependency on a retracted numerical extrapolation. The derivation above uses only the exact Desnanot–Jacobi identity and is re-banked here independently of that bookkeeping edge.

## 2. Exact reciprocal / transposed-rectangle duality

Let `b` be the reciprocal/Jacobi–Trudi dual coefficient sequence corresponding to `a` (with nonzero leading term, under the standard normalized formal-series setup used by the campaign). The rectangular dual Jacobi–Trudi identity exchanges order and shift:

`D_{r,k}(a) = D_{k,r}(b)`.

Applying the same exchange to the four minors in the odds quotient gives

`Z_a(r,k) * Z_b(k,r) = 1`.

The campaign checked the determinant transpose relation at 16 exact rational test points and the normalized reciprocal product at six exact lattice points; the identity itself is algebraic.

### Complementary-ratio corollary

The compactified ratio

`theta = k/(k+r)`

becomes `1-theta` after `(r,k)` is exchanged. Therefore, at ratios where both limits exist,

`A_a(theta) * A_b(1-theta) = 1`.

So small-ratio behavior for a sequence is dual to large-ratio behavior for its reciprocal sequence; vanishing on one side corresponds to blow-up on the other.

## 3. Kernel-checked formal fragments

The export contains five successful Lean declarations retained here under `formal/`:

| file | mathematical role | axiom footprint in receipt |
|---|---|---|
| `msl_rh-pts-chain-001.lean` | abstract implication chain from assumed DBN equivalence + lower bound + PTS-style hypothesis | `Classical.choice`, `Quot.sound`, `propext` |
| `msl_rh-pointwise-coordinate-restates-001.lean` | pointwise equivalence between positivity of a nonnegative coordinate and simplicity, under the supplied zero-coordinate equivalence | `Classical.choice`, `Quot.sound`, `propext` |
| `msl_rh-benchmark-telescope-core-002.lean` | factorial-product telescope core | `propext` |
| `msl_rh-determinant-does-not-imply-simplicity-003.lean` | one counterexample refutes a universal determinant-positivity => simplicity implication | empty |
| `msl_rh-benchmark-shift-telescope-006.lean` | shifted factorial telescope | `Quot.sound`, `propext` |

These formalize the displayed abstract/algebraic fragments. They do not formalize RH, PTS, or the numerical fixed-slope extrapolation.

## 4. Reproduced fixed-slope computation

The included `ratio_uniformity.py` was rerun during extraction against the coefficient cache carried in the session export. It reproduced the logged table exactly.

The in-run calibration uses the factorial benchmark orbit, for which `Z=1`; the worst displayed deviation was

`2.012e-183`.

For `k=m r`, with `theta=m/(m+1)`, the three slices with at least six tail points were:

| theta | orders | tail points | last Z | fitted positive limit A | fitted p | max residual, positive-limit fit | max residual, zero-limit fit | residual ratio |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1/2 | 1..22 | 11 | 0.49093011 | 0.278934 | 0.370821 | 3.03e-06 | 5.13e-04 | 169.0 |
| 2/3 | 1..14 | 7 | 0.58690671 | 0.397941 | 0.345180 | 2.25e-06 | 3.58e-04 | 158.9 |
| 3/4 | 1..11 | 6 | 0.61805274 | 0.444954 | 0.338330 | 2.73e-06 | 3.72e-04 | 136.6 |

The model compared

`Z(r) = A + B r^{-p}`

against the zero-limit class

`Z(r) = B r^{-p}`.

On these finite slices the positive-limit model is selected very strongly by residual. This is evidence for a positive fixed-slope limit across the tested range; it is **not** a proof that the limit exists, remains positive for all ratios, or supplies the missing uniform theorem needed for an RH close.

The shallower `theta=0.8` and `theta=5/6` slices had only four tail points each. They are retained in the raw output but excluded from the three-slice headline because that depth is too underdetermined for the same inference.

## 5. What the extraction corrected

The active state was useful ore, but it was not accepted as an authority ledger without review.

### A. A gamma-envelope statement was overclaimed

One source node wrote a pointwise asymptotic of the form

`log |H_0(x)| = C + (7/4) log x - pi x/8`.

Stirling's formula supplies the exponential/polynomial **gamma-factor envelope scale**, but the critical-line zeta factor fluctuates and vanishes at zeros. The global pointwise statement is therefore not carried here as a theorem. The safe reusable information is the gamma/envelope scale, with the zeta factor left explicit.

### B. The zero-velocity identity survives; a global sign claim does not

At a simple real zero `x(t)` of a heat-flow solution with

`partial_t H = - partial_x^2 H`,

differentiating `H_t(x(t))=0` gives the exact local identity

`x'(t) = H_xx/H_x`

at the zero.

The source then tried to upgrade a tested sign pattern for the lowest zero into a general negativity theorem. Its own derivation only established that the positive partner/reciprocal terms were smaller **in the tested range**. That global sign claim is not published here. The local velocity identity is.

### C. State staleness was partly bookkeeping, not mathematics

The state engine retracted an earlier extrapolation node and automatically marked later nodes stale by dependency propagation. One exact fixed-slope equivalence had cited that extrapolation even though its proof uses only the Desnanot–Jacobi identity. This release removes the non-load-bearing dependency and states the equivalence directly.

The numerical fixed-slope results remain computational evidence, not theorem, even after that dependency repair.

### D. The advertised precision control was narrower than a fresh coefficient recomputation

One follow-up raised determinant arithmetic precision after loading coefficients already computed/cached at 200 digits. That is a useful arithmetic-precision check, but it is not an independent 320-digit recomputation of the coefficient quadrature. This release does not describe it as one.

## 6. Snapshot / integrity status

The session export passed byte-level archive checks and artifact-closure checks, but its semantic-state conformance checker reported bookkeeping failures involving retraction materialization/targets and one rebirth-after-retraction condition. For that reason this directory is an **adversarial extraction from the source objects**, not a republication of every object carrying a `PROVED` label.

The exported campaign is also explicitly an active snapshot: 30 recorded rounds from a requested 100-round run.

## Frontier

The exact identities sharpen the live mathematical question to a ratio-uniform curvature problem: prove enough control on `Q_{r,k}` (equivalently `Z_{r,k}`) as `(r,k)` grow together to obtain a positive bound uniformly across the compactified ratio, then connect that bound to the relevant total-positivity / zero-simplicity criterion without assuming the conclusion.

The finite computation says the tested fixed-slope slices are compatible with a positive limit. The exact duality says the two ends of the ratio interval are coupled by reciprocal-series transposition. Neither statement supplies the missing uniform theorem.
