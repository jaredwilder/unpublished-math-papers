# Adversarial audit of the 2026-09-11 RH session export

**Author:** Jared Wilder  
**Audit / public extraction:** 2026-09-11

This note records what survived a second-pass audit of the uploaded active MSL session export. It is not a transcript summary. It is an authority ledger: what is exact, what is formal, what is computational, what was repaired, and what was rejected.

## 1. Snapshot integrity

The export is an **active snapshot**, not a completed 100-round run.

Observed session scale:

- 30 recorded MSL rounds;
- 1,048 transcript records;
- 198 assistant turns;
- 152 tool uses / 151 tool results;
- 329 semantic-state objects.

Byte/archive integrity and artifact-closure checks passed. The semantic-state conformance layer did not: it reported retraction-materialization / unknown-retraction-target errors and one rebirth-after-retraction condition. Consequently the state machine's `PROVED` labels were treated as claims to audit, not as authority.

## 2. New public lane recovered: PTS / de Bruijn–Newman simplicity

The public RH directory previously exposed two lanes. The export contained a third:

> `PTS`: for every real `x` and every `t in (0,0.2]`, `H_t(x)=0` implies `H_t'(x) != 0`.

PTS remains unproved.

Recovered into `riemann-hypothesis/pts-terminal-close/`:

- frozen terminal-close record;
- ten-mechanism close-anatomy contract;
- interval-arithmetic certifier source with hashes and reconstruction instructions;
- fresh self-test receipt.

Fresh extraction-time rerun:

`python interval_ht.py --selftest`

returned **8/8 OK, exit 0**.

The source export did not carry all historical point/t-box receipt JSONs as named artifacts, and full certificate regeneration exceeded the short extraction-time run window. Historical finite certificates are therefore preserved as source-campaign records, not relabeled as freshly reproduced.

## 3. Exact determinant results that survive

### 3.1 Desnanot–Jacobi curvature coordinate

For

`D_{r,k}=det[a_{k+j-i}]`

and

`Q_{r,k}=D_{r,k-1}D_{r,k+1}/D_{r,k}^2`,

Desnanot–Jacobi gives exactly

`Z_{r,k}=(r/k) Q_{r,k}/(1-Q_{r,k})`.

No fitted asymptotics enter this identity.

### 3.2 Reciprocal / transposed-rectangle duality

Under the standard reciprocal Jacobi–Trudi coefficient duality,

`D_{r,k}(a)=D_{k,r}(b)`

and therefore

`Z_a(r,k) Z_b(k,r)=1`.

At compactified ratio `theta=k/(k+r)`, order/shift exchange sends `theta` to `1-theta`. Hence, wherever both limits exist,

`A_a(theta) A_b(1-theta)=1`.

### 3.3 Fixed-slope equivalence restored from false staleness

One exact state node had been marked stale because it cited a later-retracted numerical extrapolation. That dependency was non-load-bearing.

On `k=mr`, the exact identity is simply

`Z=(1/m)Q/(1-Q)`.

Therefore, if a fixed-slope limit exists,

- `Z -> A>0` iff `Q -> mA/(1+mA)` in `(0,1)`;
- `Z -> 0` iff `Q -> 0`.

This is exact algebra and survives independently of every numerical fit.

## 4. The finite repeated-zero witness was upgraded to a theorem

The source state K12 claimed that strict positivity of all consecutive Toeplitz minors is blind to zero multiplicity, but its direct computation W9 checked only 24 minors.

The intended witness can in fact be proved globally:

`F(z)=(1+z)^2 e^z`.

`F` has a double zero at `-1`, while for every `r>=1` and `k>=0`,

`D_{r,k}(F)>0`.

The proof now published in

`determinant-curvature-2026-09-11/MULTIPLICITY-BLINDNESS-THEOREM.md`

uses:

1. Toeplitz factorization `T_F=T_{e^z}T_{(1+z)^2}`;
2. total nonnegativity of both factors;
3. the exact positive exponential minor
   `D_{r,k}(e^z)=prod_{j=0}^{r-1} j! / prod_{j=0}^{r-1}(k+j)!`;
4. Cauchy–Binet, whose `K=J` term is already strictly positive.

An independent exact-rational regression sweep checked 104 pairs

`1<=r<=8`, `0<=k<=12`

with no mismatch in the exponential closed form and no nonpositive repeated-zero minor.

**Conclusion:** strict positivity of every consecutive Toeplitz minor, taken as a property by itself, does not imply simple zeros.

The abstract Lean falsifier from the export is therefore now backed by a genuine global analytic witness rather than only a finite tested block.

## 5. Published coefficient curvature gives a rigorous order-one anchor

The export's K23 cited W. Michalowski, arXiv:2607.16795, but the state authority binding incorrectly left an adapter pending.

For determinant order `r=1`, no general-order adapter is needed. The paper's Lemma 2.1 gives for the same xi coefficient sequence

`1/(2k) < tau_k=-log q_k < 4/k`,  `k>=2`.

Since

`Z_{1,k}=1/[k(exp(tau_k)-1)]`,

one obtains rigorously

`1/[k(exp(4/k)-1)] < Z_{1,k} < 1/[k(exp(1/(2k))-1)]`.

Thus

`liminf Z_{1,k} >= 1/4`,

`limsup Z_{1,k} <= 2`.

This is published separately as a **derived corollary**, not claimed as an independent new curvature theorem.

## 6. Reproduced computational fixed-slope frontier

The session carried `ratio_uniformity.py` plus its coefficient cache. The experiment was rerun during extraction and reproduced the logged table exactly.

Factorial benchmark calibration, where exact theory gives `Z=1`, had worst displayed deviation

`2.012e-183`.

Adequately deep slices:

| theta | orders | tail n | fitted A in `A+B r^-p` | p | positive-fit max residual | zero-limit max residual | ratio |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 1/2 | 1..22 | 11 | 0.278934 | 0.370821 | 3.03e-06 | 5.13e-04 | 169.0 |
| 2/3 | 1..14 | 7 | 0.397941 | 0.345180 | 2.25e-06 | 3.58e-04 | 158.9 |
| 3/4 | 1..11 | 6 | 0.444954 | 0.338330 | 2.73e-06 | 3.72e-04 | 136.6 |

This is strong finite evidence that the tested slices are better described by a positive limiting constant than by a vanishing pure power law. It is not a proof that the limits exist or that positivity is uniform over all ratios.

The shallower `theta=0.8` and `5/6` slices had only four fitted tail points each and are not used for the headline inference.

## 7. Formal authority recovered

Five successful Lean declarations were preserved under

`determinant-curvature-2026-09-11/formal/`.

Their recorded footprints are:

- PTS implication-chain schema: `propext`, `Classical.choice`, `Quot.sound`;
- pointwise simplicity-coordinate restatement: same footprint;
- factorial telescope core: `propext`;
- universal implication falsifier: **empty axiom footprint**;
- shifted factorial telescope: `propext`, `Quot.sound`.

One supplied formal proof that leaked `sorryAx` and two resource-undecided attempts were excluded from the positive formal inventory.

## 8. Source claims rejected or repaired

### 8.1 Global pointwise gamma-envelope claim — rejected

The source promoted an expression of the shape

`log |H_0(x)| = C + (7/4)log x - pi x/8`

to a global pointwise asymptotic. Stirling controls the gamma-factor envelope, but the critical-line zeta factor fluctuates and vanishes. The global pointwise claim is not banked.

### 8.2 Lowest-zero velocity negativity — rejected as a global theorem

At a simple zero of a heat-flow solution with `partial_t H=-H_xx`, the local identity

`x'(t)=H_xx/H_x`

is exact.

But the source then upgraded a tested sign pattern for the lowest zero into a global negativity theorem. In the even zero-pair factorization the self-partner term is positive, while the higher-pair terms are negative; the source established dominance only numerically in its tested range. The global sign statement is not banked.

### 8.3 Precision-control wording — repaired

A follow-up raised determinant arithmetic precision after loading coefficients already computed/cached at 200 digits. It is useful arithmetic-precision evidence, but it is not an independent 320-digit recomputation of the coefficient quadrature.

### 8.4 K12 finite-to-universal leap — repaired by proof

The original state called the all-minors multiplicity-blindness claim proved on the strength of a 24-minor test. The claim itself was salvageable and is now genuinely proved, but the original provenance was insufficient.

## 9. Remaining mathematical frontier

After the audit, the central determinant problem is sharper rather than smaller.

Known now:

- exact curvature reparameterization;
- exact reciprocal ratio duality;
- rigorous positive order-one anchor;
- a global theorem showing consecutive-minor strict positivity does not encode zero simplicity;
- finite fixed-slope evidence for positive limiting curvature on three tested ratios.

Still missing:

> a ratio-uniform theorem controlling `Q_{r,k}` / `Z_{r,k}` as `r,k -> infinity` together, strong enough to establish the required positivity across the critical bounded-ratio region.

The PTS program is a distinct lane with a distinct missing theorem: global positive-time zero simplicity.

The export therefore yielded real mathematics, a recovered certifier program, two theorem-level upgrades, and several state corrections — but not an RH proof.
