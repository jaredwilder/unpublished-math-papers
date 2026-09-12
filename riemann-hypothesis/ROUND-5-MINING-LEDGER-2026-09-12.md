# RH / zeta Round-5 mining and publication ledger — 2026-09-12

**Author:** Jared Wilder  
**Status:** live public mining checkpoint; **not an RH proof**

This round continued the estate-wide publication sweep after Round 4. The rule remains:

> recover -> re-derive -> attack scope -> check current literature -> publish at exact evidence class -> correct publicly when necessary.

---

## R5-1 — public source-audit correction: Polymath 15 conjugation

A contradiction between two internal PTS source audits was resolved against the published Polymath formula.

The earlier `RH_CLOSE_PROOF_ATTEMPT.md` claimed that the second finite Dirichlet polynomial in the Polymath-15 main term used no conjugation at `y=0`. That correction was itself wrong.

The correct structure is

\[
f_t(x)=S_t(x)+\gamma_t(x)\overline{S_t(x)}.
\]

The Round-4 public ledger has been corrected rather than silently rewritten.

Correction commit:

`0f286a396c6f6979782da0135f9b807f37770d2d`

This does **not** prove the old Hardy/value–torque route. It only removes a false reason for killing it; all quantitative transversality/error obligations remain.

---

## R5-2 — finite Hausdorff-to-Schur conditioning theorem

Directory:

`finite-hausdorff-schur-conditioning-2026-09-12/`

Theorem commit:

`23645fd00f13cc69775a8974cc785634f0dba9e7`

Exact-rational replay commit:

`548c61222764018db1de98ae64b05fa73f26147e`

For a finite `m`-atom cloud

\[
y_j\in[\eta,1-\eta],
\qquad
|y_i-y_j|\ge\Delta,
\]

with power sums

\[
p_s=\sum_jy_j^s=\frac14H_{s-1,0},
\]

the inverse power-sum Jacobian obeys an explicit Vandermonde bound

\[
\|J^{-1}\|_\infty
\le
C_m(\eta,\Delta)
:=
\frac{(2-\eta)^{m-1}}{\Delta^{m-1}}.
\]

Transport through

\[
\alpha_j=\frac{y_j}{1-y_j}
\]

and the rectangular-Schur occupancy law gives

\[
\left|
\frac d{dt}\log s_{(r^k)}(\alpha(t))
\right|
\le
\frac{rkC_m(\eta,\Delta)}
{4\eta(1-\eta)}
\max_{0\le n<m}|\dot H_{n,0}(t)|.
\]

Under the explicit smallness/bootstrap condition in the note, endpoint Hausdorff errors therefore give a certified multiplicative determinant-distortion bound.

### Why this matters

The previous finite-spectrum theorem said the first `m` Hausdorff values reconstruct the entire determinant lattice. This theorem adds the missing **condition number**.

It makes the crowding obstruction explicit:

\[
\boxed{
\text{finite reconstruction cost}
\sim \Delta^{-(m-1)}.
}
\]

Thus the infinite RH tail problem cannot be solved responsibly by saying only “take more moments.” High spectral crowding can make arbitrary finite Prony inversion catastrophically ill-conditioned.

### Prior-art boundary

Prony/Vandermonde moment inversion and collision conditioning are classical, including work of Batenkov–Yomdin. No novelty is claimed for that component. The estate synthesis is the exact chain

\[
\text{Hausdorff error}
\to
\text{power-sum node motion}
\to
\text{Xi Möbius motion}
\to
\text{Schur determinant distortion}.
\]

Historical priority for that composition remains unverified.

---

## R5-3 — Laguerre heat-transport hierarchy

Directory:

`laguerre-heat-transport-hierarchy-2026-09-12/`

Commit:

`e55d1663e66f94ead0124b09e66e788eab4f5655`

For any sufficiently smooth real solution of

\[
H_t=-H_{xx},
\]

write `H_n=partial_x^n H` and define

\[
\mathcal L_n
=H_n^2-H_{n-1}H_{n+1}.
\]

Then

\[
\boxed{
(\partial_t+\partial_x^2)\mathcal L_n
=2\mathcal L_{n+1}.
}
\]

Likewise

\[
Q_n=H_n^2
\]

obeys

\[
\boxed{
(\partial_t+\partial_x^2)Q_n
=2Q_{n+1}.
}
\]

The exponential generating functions in derivative order therefore satisfy first-order transport equations in the new derivative-order variable.

For the PTS transversality energy,

\[
Q_0+\lambda Q_1=H^2+\lambda H_x^2,
\]

one gets

\[
(\partial_t+\partial_x^2)(H^2+\lambda H_x^2)
=2H_x^2+2\lambda H_{xx}^2\ge0.
\]

### Prior-art boundary

The first Laguerre difference

\[
H_x^2-HH_{xx}
\]

and its application to the de Bruijn–Newman family are classical; Csordas–Ruttan–Varga used it in 1991. This note makes **no novelty claim** for the first rung or for classical Laguerre inequalities. The all-order transport packaging is published for structural reuse and provenance; historical priority remains unresolved.

---

## R5-4 — reciprocal-pole asymptotic theorem: valid, but not republished as novelty

The archive's dual theorem remains mathematically valid under its corrected hypothesis: if the first `m+1` reciprocal singularities in modulus form a certified ordered block of simple positive poles with no competitor, then Cauchy–Binet plus alternating residues/Vandermonde signs give eventual positivity of the fixed-shift dual Toeplitz determinant.

However, current 2026 external work has already pushed this exact dual-pole/Jacobi–Trudi mechanism farther for the actual Xi coefficients, proving all-rank nonnegativity for the first fifteen shifts.

Disposition:

> **surviving estate mechanism; no redundant novelty publication.**

---

## R5-5 — Branch-B extreme-ray wording flagged

The epoch-24 arithmetic/Weil ledger says that the extreme rays of the cone of “nonnegative even functions” are point masses.

Literally stated, this mixes the function cone with the measure/distribution cone: point masses are not ordinary functions. A valid reduction may be recoverable after reformulating the domain as the appropriate cone of nonnegative even measures/distributions or after specifying an approximation/closure argument, but the archived sentence is not accepted as a theorem as written.

A public-repository search found no live standalone theorem carrying that wording, so no public correction commit was needed.

Disposition:

> **quarantined until the functional-analytic domain is written correctly.**

---

## R5-6 — publication decisions deliberately refused

This round did **not** publish:

- the generic reciprocal-pole theorem as a novelty result, because current literature already occupies the Xi-specific lane;
- the first Laguerre inequality as estate novelty, because it is classical;
- the Branch-B extreme-ray reduction, because its function/measure domain is not yet clean;
- any numerical simple-zero headline merely because an old certificate exists.

The publication standard remains mathematical scope first, volume second.

---

# Frontier impact

Round 5 sharpened two live programs.

### Hausdorff / reconstruction

The missing object is now not merely “tail-controlled reconstruction.” It must beat an explicit finite-spectrum conditioning law whose naive cost deteriorates like

\[
\Delta^{-(m-1)}.
\]

A serious infinite theorem should exploit zeta-specific high-zero geometry rather than treating the tail as an arbitrary growing Prony system.

### PTS

The local certifiers

\[
H^2+H_x^2,
\qquad
H_x^2-HH_{xx},
\qquad
\text{higher derivative tests}
\]

sit inside exact heat-transport ladders. This gives a principled way to ask whether higher-rung positivity can reduce interval subdivision or strengthen transversality boxes without pretending it already proves global PTS.

---

# Status

RH remains open. PTS remains open. Branch C remains an open sufficient criterion. The finite Weil/operator convergence theorem remains open.

Round 5 adds one quantitative finite reconstruction theorem, one exact PTS transport hierarchy, one public source correction, and two important non-publication decisions.