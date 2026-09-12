# RH re-mining — Round 3 release ledger

**Author:** Jared Wilder  
**Date:** 2026-09-12  
**Purpose:** commit-level provenance for the third full re-mining / hostile publication pass

## Operating rule

Round 3 does **not** assume that the previous 100-round adjudication or the second re-mining found everything.

A result is eligible for prompt public release when it clears four gates:

1. source recovery / independent derivation;
2. hostile scope and boundary audit;
3. targeted prior-art search appropriate to the claim;
4. wording that distinguishes generic mathematics, zeta-specific mathematics, computation, and open RH implications.

Publication is a provenance record, not a claim that literature novelty or legal priority has been finally adjudicated.

---

## New releases

### R3-1 — finite even-moment rigidity

Path:

`finite-moment-rigidity-2026-09-12/README.md`

Public theorem-note commit:

`c018ce00b7193087e85b7b44153f951979993b51`

Verifier:

`finite-moment-rigidity-2026-09-12/verify_finite_moment_rigidity.py`

Verifier commit:

`9f6abfa3983dd51828430905ff7b0a51d258c639`

**Status:** new theorem extracted/strengthened during re-mining; exact finite algebra; no RH claim; novelty preliminary/unsettled.

Main statement: `Q` off-line reflection quadruples cannot be matched through the first `2Q` raw even moments by `2Q` real critical-line pairs unless every off-line displacement vanishes. Newton identities reconstruct the squared-height multiset exactly.

Exact sanity checks pass for `Q=1,2,3,4`.

---

### R3-2 — tilted-theta CGF / Toeplitz coordinate

Path:

`theta-cgf-toeplitz-coordinate-2026-09-12/README.md`

Commit:

`81079bbcbc021bd6fa9f8360b0e2e44dfda9bc74`

**Status:** exact cross-epoch structural synthesis; novelty not asserted; no RH claim.

Main identity:

\[
\frac{a_{k+s}}{a_k}
=
\frac{\Gamma(2k+1)}{\Gamma(2k+2s+1)}
\mathbb E_{\nu_k}e^{sX_k},
\qquad X_k=2\log U.
\]

Thus one CGF `K_k(s)` controls the full normalized consecutive Toeplitz matrix. The campaign's local variance/Turán calculations and its fixed-slope large-deviation problem are two scales of the same coordinate.

---

### R3-3 — determinant-integral sign obstruction

Path:

`determinant-integral-sign-no-go-2026-09-12/README.md`

Commit:

`ed9368aa0e19b41f418dd892c2f47e44c34a7bee`

**Status:** exact route-kill; no general determinant-lift novelty claim; no RH claim.

The natural positive-measure multilinear lift of a consecutive Toeplitz determinant has a sign-changing symmetrized inner kernel already at order two. Therefore positivity of the theta measure alone cannot yield determinant positivity by the most direct pointwise-integrand argument.

---

### R3-4 — no fixed finite H/D sign battery

Path:

`finite-sign-battery-no-go-2026-09-12/README.md`

Commit:

`e362939a80169524467df1f433e43609382c642f`

**Status:** proved generic continuity obstruction; elementary; novelty not asserted; no RH claim.

Any fixed finite collection of strict Hausdorff/finite-difference and consecutive-Toeplitz sign tests that is positive at an all-real interior parameter point remains positive under a sufficiently small conjugate nonreal perturbation. Therefore a fixed finite sign prefix cannot characterize the positive-real spectral cone without an additional tail/rigidity theorem.

---

## Public corrections made during the same hostile pass

### C3-1 — Branch A truncation envelope was not rigorous

The historical Branch-A code computed each quantity called a cell maximum by sampling only 41 points in the cell with ordinary `mpmath` arithmetic. That is not a certified cell supremum and does not support the earlier claim of a rigorous zero-localization envelope.

Corrected public front door:

`riemann-hypothesis/README.md`

Commit:

`249787cf320ba2e3b5d09763cd5e9f369c6aaf3e`

Corrected Branch-A packet:

`branch-a-heat-flow-audit/README.md`

Commit:

`d1d4fb8b72dd3629995c53d754019e3d7ea194f3`

Corrected canonical campaign-state note:

`CURRENT-CAMPAIGN-STATE-2026-09-12.md`

Commit:

`6cd1ecc50f6e9cce44e1b297c70f9625d1031980`

**Correct evidence class:** useful numerical instrumentation / finite evidence, not interval-certified zero localization.

---

### C3-2 — real-rootedness topology / criterion-space closure

Path:

`forensic-corrections-2026-09-12/REAL-ROOTEDNESS-TOPOLOGY-CORRECTION.md`

Commit:

`8622b2ec8297af42a7c6ba89d8e97c2784b7f85b`

The internal epoch-24 state (`K568` onward) said that real-rootedness is an open property and inferred that every equivalent criterion must be a margin inequality.

Correct statement for fixed-degree real polynomials:

- all-real-rooted locus: **closed**;
- distinct/simple-real-rooted locus: **open**.

Therefore the campaign's claimed closure of the entire criterion space does not follow. Instrument-specific margin results survive only at their own scopes.

---

### C3-3 — top-k angular theorem needed an explicit reality hypothesis

Path:

`encirclement-ii-v-recovered/TOP-K-ANGULAR-BUDGET-THEOREM.md`

Correction commit:

`5355fd34571646a90bf4d1e4f1c0c834c103e9bb`

The phase argument unconditionally gives

\[
\operatorname{Re}s_{(r^k)}(\alpha)>0
\]

when the top-`k` angular budget is below `pi/2`. To conclude the ordered real statement `D_{r,k}>0`, the determinant must be real, e.g. because the parameter multiset is conjugation invariant. The corrected note now states that hypothesis explicitly.

---

### C3-4 — critical-value/gap theorem had been stated too generically

Path:

`ZERO-GAP-CRITICAL-VALUE-MONOTONICITY.md`

Correction commit:

`6ef0cf004d783e749dcf44d5ef0645ea3bbf3cb3`

The algebraic monotonicity proof is sound once the zero ODE and logarithmic-derivative sum are available. The previous phrase “real entire solution” was broader than those identities justify automatically.

The note now states the theorem for finite polynomial heat flows and for canonical-product heat flows, including the standard de Bruijn–Newman real-zero setting, when the required sums/identities are justified.

---

## Literature collision banked in Round 2 / enforced in Round 3

The order-one theta-moment inequality

\[
\frac{m_{2k-2}m_{2k+2}}{m_{2k}^2}
\le
\frac{2k+1}{2k-1}
\]

is classical: Csordas & Varga, *Moment Inequalities and the Riemann Hypothesis*, Constructive Approximation **4** (1988), 175–198, prove the relevant Turán moment inequality in a stronger deformed-family setting.

Therefore the campaign's finite first-row certificates are reproducibility/certification assets, **not** a novelty headline, and the earlier description of the row as full “sub-Gaussianity” is withdrawn.

---

## What has NOT been claimed

Round 3 has not established:

- RH;
- the Branch-C determinant inequality for the actual xi coefficients at every `(r,k)`;
- PTS;
- a rigorous Branch-A zero-localization certificate;
- literature novelty of every structural note;
- that the estate is exhausted.

The third item matters operationally: repeated sweeps have already found both new mathematics and new corrections missed by earlier sweeps. No single adjudication layer is being treated as exhaustive.

## Next release gate

Priority remains:

1. zeta/theta-specific exact theorems with complete source chains;
2. genuinely new generic theorems with plausible independent publication value;
3. route-killing negative results that prevent large future compute waste;
4. corrections to any public statement whose evidence class is stronger than its source.

The sweep continues from the raw 413-node proved-candidate layer and the 1,476-object closed byte denominator.
