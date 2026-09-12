# Current RH / zeta public release index — 2026-09-12

**Author:** Jared Wilder  
**Purpose:** rapid public provenance and discoverability.  
**Status:** this index contains auxiliary mathematics, structural reductions, corrections, no-go theorems and conditional results. **It does not claim a proof of RH.**

This page indexes the theorem-level releases produced by the repeated forensic re-mining of the research estate. Each linked directory contains its own exact scope and prior-art boundary.

## Highest-priority current releases

### 1. Global determinant-order escape near a hypothetical positive Newman threshold

`positive-newman-threshold-global-order-escape-2026-09-12/`

If `Lambda>0`, the complete nonreal coefficient-spectral angular budget immediately below the threshold is

\[
\Theta(t)=4\mathcal S_\Lambda\sqrt{\Lambda-t}+O(\Lambda-t),
\]

so any negative consecutive coefficient Toeplitz/Schur minor must have order

\[
r\gtrsim\frac{\pi}{8\mathcal S_\Lambda\sqrt{\Lambda-t}}.
\]

For every fixed order cap `R`, all orders `r<=R` and all shifts remain positive in a one-sided interval immediately below a hypothetical positive threshold.

Commits: `7b637321592730ee2d9e0a6c124457c44900d7c7`, `2fc48fe13d7172f7e793f25b5ae5035c893cada6`.

### 2. Finite-multiplicity Hermite collision -> Schur order barrier

`multiple-newman-collision-hermite-order-barrier-2026-09-12/`

Every finite-multiplicity threshold collision unfolds on the universal `sqrt(Lambda-t)` scale with the classical Hermite micro-profile; transporting that cluster through the coefficient spectral map yields an explicit multiplicity-dependent determinant-order lower barrier.

Commit: `09344ed40130b54d04311146c9550ab89784b2d2`.

### 3. Positive threshold is attained at a finite multiple zero

`positive-newman-threshold-finite-multiple-zero-2026-09-12/`

Published high-zero reality/localization + the de Bruijn strip theorem + compactness + the implicit-function theorem give

\[
\Lambda>0\Longrightarrow
\exists x_*\in\mathbb R:
H_\Lambda(x_*)=H_\Lambda'(x_*)=0.
\]

This makes the PTS implication chain explicit.

Commit: `07e185ef1abb1f804eaaa01e6cb74fd40a96101e`.

### 4. Dynamic Desnanot harmonicity

`dynamic-desnanot-harmonicity-2026-09-12/`

For any `C^2` positive determinant homotopy, relative to a fixed positive Desnanot comparison array,

\[
L_D(\partial_tU)=0,
\]

while

\[
L_D(\partial_t^2U)
=-R(\Delta_k^2\partial_tU)^2
-A(\Delta_r^2\partial_tU)^2\le0.
\]

The de Bruijn–Newman coefficient flow is an application; the generic theorem itself does not require the heat PDE.

Commit: `9e6806174af56186f31d5bf0cfec75820168e9e4`.

### 5. Desnanot odds / Fisher-source identity

`desnanot-odds-fisher-source-2026-09-12/`

For determinant log-odds

\[
\ell=\log(A/R),
\]

adaptive harmonicity collapses to

\[
\Delta_k^2V=-A\dot\ell,
\qquad
\Delta_r^2V=R\dot\ell,
\]

and the acceleration source becomes

\[
\boxed{
L_DW=-RA\dot\ell^2
=-\frac{\dot R^2}{R(1-R)}.
}
\]

Thus the static rational-orbit coordinate and dynamic determinant homotopy meet in one scalar log-odds velocity.

Commit: `472ad294dae1c313a2b4ae0b36cd33aef719cbe4`.

### 6. Top-k rectangular Schur distortion theorem

`top-k-schur-distortion-2026-09-12/`

For rectangle `(r^k)` and positive vectors `x,y`,

\[
\left|\log\frac{s_{(r^k)}(x)}{s_{(r^k)}(y)}\right|
\le r\sum_{j=1}^k\delta_j^*,
\]

where `delta_j^*` are the `k` largest values of `|log(x_i/y_i)|`.

This contains the occupancy-cap theorem as its infinitesimal face and proves fixed finite spectral defects disappear from normalized `rk` bulk free energy.

Commit: `a74a0d4dfd9341ebe59be4c024e691349f991f8b`.

### 7. Branch C in equivalent orbit / curvature coordinates

`branch-c-equivalent-coordinates-2026-09-12/`

Inside the positive determinant domain, the live sufficient criterion is exactly equivalent to

\[
Y_{r,k}\ge r/k,
\qquad
Z_{r,k}\ge1,
\qquad
\Delta_k^2\log(D/B)\le0.
\]

This identifies several historically separate campaigns as proof engines for one theorem.

Commit: `200140e7a598b86f38891883d3ebf1e5311398c9`.

### 8. Finite even-moment rigidity

`finite-moment-rigidity-2026-09-12/`

For `Q` reflection/conjugation off-line quadruples, equality with `2Q` critical-line pairs through the first `2Q` raw even power sums forces the squared-height multiset to equal

\[
\{(t_j+id_j)^2,(t_j-id_j)^2\}_{j=1}^Q,
\]

so real comparison heights force every `d_j=0`.

Theorem commit: `c018ce00b7193087e85b7b44153f951979993b51`.  
Verifier commit: `9f6abfa3983dd51828430905ff7b0a51d258c639`.

## Structural bridges and route-kills

### Hausdorff–Schur Möbius bridge

`hausdorff-schur-mobius-bridge-2026-09-12/`

Exact coordinate identity

\[
\frac1{4\rho(1-\rho)}=\frac{\alpha}{1+\alpha},
\]

plus the common Hausdorff/Beta lattice and the exact first-order angular-blindness identity at the radial saddle.

Commits: `1585ed8fe9a60bc07a126d2381f8336ed01cceca`, `b9e4a09fa63d621d93d6759770b71a5d14612f71`.

### Tilted-theta CGF / Toeplitz coordinate

`theta-cgf-toeplitz-coordinate-2026-09-12/`

Every normalized Toeplitz entry is a factorial correction times a sample of one tilted log-moment generating function. The local Turan/variance and macroscopic fixed-slope programs are two scales of the same object.

Commit: `81079bbcbc021bd6fa9f8360b0e2e44dfda9bc74`.

### Natural determinant-integral sign no-go

`determinant-integral-sign-no-go-2026-09-12/`

The natural positive-measure multilinear lift has a sign-changing inner kernel already at determinant order two, killing the most direct pointwise-positivity shortcut.

Commit: `ed9368aa0e19b41f418dd892c2f47e44c34a7bee`.

### No fixed finite Hausdorff/Toeplitz sign battery

`finite-sign-battery-no-go-2026-09-12/`

Any fixed finite collection of strict sign tests persists under a sufficiently small conjugate nonreal perturbation. A finite prefix cannot characterize the real-positive spectral cone without a separate tail/rigidity theorem.

Commit: `e362939a80169524467df1f433e43609382c642f`.

### Generic double-collision barrier

`newman-collision-determinant-order-barrier-2026-09-12/`

The `m=2` precursor of the Hermite theorem. The public version corrects an internal overclaim: the formula is a **lower barrier**, not an asymptotic equality for the actual first negative determinant.

Commit: `f4a05fc86aeb86e245254f57d432a99a95acb96a`.

## Important earlier surviving theorem candidates

- `encirclement-ii-v-recovered/TOP-K-ANGULAR-BUDGET-THEOREM.md` — exact top-`k` rectangular-Schur phase budget, with the conjugation/reality hypothesis now explicit.
- `ZERO-GAP-CRITICAL-VALUE-MONOTONICITY.md` — exact monotonicity of the renormalized critical-value/gap observable under its canonical-product/zero-dynamics hypotheses.
- `encirclement-ii-v-recovered/DISCRETE-ELLIPTIC-COMPARISON-AND-HOMOTOPY.md` — normalized exponential determinant equation, finite-domain comparison principle and boundary-homotopy positivity theorem.
- `encirclement-ii-v-recovered/DUAL-VERIFIED-POLE-EVENTUAL-POSITIVITY.md` — conditional reciprocal-pole asymptotic positivity, with the Riemann instantiation gate tightened to require an exhaustive initial singularity block.

## Public corrections that are part of the release record

The forensic process also corrected materially overstated claims. In particular:

- the Branch-A 64-piece sampled envelope is numerical instrumentation, **not** a rigorous zero-localization certificate;
- the epoch-24 claim that all real-rootedness is an open condition is false; the full fixed-degree real-rooted locus is closed, while the simple-real-rooted locus is open;
- the top-`k` angular theorem needs a reality/conjugation hypothesis to turn positive real part into `D_(r,k)>0`;
- the critical-value/gap theorem requires the relevant zero-dynamics/canonical-product identities rather than an arbitrary real entire heat solution;
- the dual reciprocal-pole Riemann application requires certification that the poles are genuinely the first singularities in modulus, not merely a list of known critical-line zeros.

## Current non-claims

The repository does **not** claim:

- a proof of RH;
- a proof of the live Branch-C inequality for every Xi index;
- Positive-Time Simplicity;
- a new current simple-zero world record;
- a finite-Weil/operator convergence theorem;
- settled historical novelty for the new generic determinant/Schur theorems.

A public timestamp establishes provenance of this release record. Specialist literature review and mathematical peer review remain separate questions.
