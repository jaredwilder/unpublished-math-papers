# RH / zeta Round-4 cross-estate release ledger — 2026-09-12

**Author:** Jared Wilder  
**Status:** public provenance ledger; **not an RH proof**  
**Rule:** recover -> independently derive/source-check -> hostile scope attack -> targeted prior-art check -> publish at exact evidence class -> keep attacking after publication.

This ledger records the releases produced after the Round-3 forensic package. It is a checkpoint, not an exhaustion claim.

---

## R4-1 — Hausdorff–Schur Möbius bridge

Path:

`hausdorff-schur-mobius-bridge-2026-09-12/README.md`

Commit:

`1585ed8fe9a60bc07a126d2381f8336ed01cceca`

Exact replay:

`hausdorff-schur-mobius-bridge-2026-09-12/verify_bridge.py`

Commit:

`b9e4a09fa63d621d93d6759770b71a5d14612f71`

### Surviving mathematics

For the folded-zero coordinate `tau=rho(1-rho)` and the PF/Schur zero parameter `alpha`,

\[
\boxed{
\frac1{4\tau}=\frac{\alpha}{1+\alpha}
}
\]

with inverse `alpha=y/(1-y)`.

Hence the Hausdorff finite-difference lattice can be written directly in the same spectral variables used by the rectangular Schur determinants:

\[
H_{n,q}
=4\sum_j
\frac{\alpha_j^{n+1}}
{(1+\alpha_j)^{n+q+1}}.
\]

For a single Beta/Hausdorff atom, the positive-axis radial logarithmic response equals the first angular phase response at the real axis. At the radial saddle both vanish, giving an exact first-order angular-blindness law.

### Prior-art boundary

General Hausdorff-moment criteria for RH are prior art, including Ruiming Zhang's 2023 work. No novelty claim is made for that criterion. The released object is the exact cross-coordinate synthesis and local sensitivity identity; external novelty remains unresolved.

---

## R4-2 — top-k rectangular Schur distortion theorem

Path:

`top-k-schur-distortion-2026-09-12/README.md`

Commit:

`a74a0d4dfd9341ebe59be4c024e691349f991f8b`

For positive finite vectors `x,y`, rectangle `(r^k)`, and

\[
\delta_i=\log(x_i/y_i),
\]

let `delta_j^*` be the decreasing rearrangement of `|delta_i|`. Then

\[
\boxed{
\left|
\log\frac{s_{(r^k)}(x)}{s_{(r^k)}(y)}
\right|
\le
r\sum_{j=1}^{k}\delta_j^*.
}
\]

It follows from the tableau capacity law `0<=m_i<=r`, `sum m_i=rk`.

The infinitesimal face is the occupancy cap

\[
0\le x_i\partial_{x_i}\log s_{(r^k)}\le r,
\]

and a fixed finite number of bounded multiplicative spectral defects disappears from the normalized `rk`-scale Schur free energy as `k->infinity`.

**Evidence class:** exact elementary theorem, new to this estate; literature priority unresolved.

---

## R4-3 — Branch C is one theorem in three exact coordinates

Path:

`branch-c-equivalent-coordinates-2026-09-12/README.md`

Commit:

`200140e7a598b86f38891883d3ebf1e5311398c9`

Inside the positive determinant domain,

\[
\boxed{
\begin{array}{c}
(k+r)D_{r,k-1}D_{r,k+1}\le kD_{r,k}^2
\\[1mm]\Updownarrow\\[1mm]
Y_{r,k}\ge r/k
\\[1mm]\Updownarrow\\[1mm]
Z_{r,k}\ge1
\\[1mm]\Updownarrow\\[1mm]
\Delta_k^2\log(D/B)\le0.
\end{array}}
\]

This collapses the August rational-orbit program, the discrete-elliptic normalized-potential program, and the September Branch-C determinant criterion into one target with multiple proof engines.

**Evidence class:** exact algebraic synthesis; criterion itself remains unproved globally for Xi.

---

## R4-4 — generic Newman collision gives a determinant-order lower barrier

Path:

`newman-collision-determinant-order-barrier-2026-09-12/README.md`

Commit:

`f4a05fc86aeb86e245254f57d432a99a95acb96a`

For a generic double collision at a hypothetical positive threshold,

\[
x_\pm(t)
=x_*\pm i\sqrt{2(\Lambda-t)}+O(\Lambda-t).
\]

The coefficient/PF spectral angle is of square-root size. The existing Schur phase theorem therefore yields the lower barrier

\[
r
\gtrsim
\frac{\pi|x_*|}
{4\sqrt{2(\Lambda-t)}}.
\]

### Important correction made during publication

The internal canonical Pass-4 draft called this the asymptotic of the **actual first negative determinant order**. The argument proves only a **forbidden region / lower barrier**: below it negativity is impossible. It does not prove negativity appears when the barrier is crossed.

The public note contains the corrected theorem.

---

## R4-5 — finite-multiplicity Hermite collision transport

Path:

`multiple-newman-collision-hermite-order-barrier-2026-09-12/README.md`

Commit:

`09344ed40130b54d04311146c9550ab89784b2d2`

For an `m`-fold threshold zero,

\[
\delta^{-m/2}
H_{\Lambda-\delta}(x_*+\sqrt\delta\,v)
\to
\frac{H_\Lambda^{(m)}(x_*)}{m!}
\,i^mH_m\!\left(\frac{v}{2i}\right).
\]

Thus local zeros split at

\[
x_j=x_*+2i\xi_{m,j}\sqrt\delta+O(\delta),
\]

where `xi_(m,j)` are the real zeros of the physicists' Hermite polynomial.

If `S_m` is the sum of its positive zeros, the Schur angular budget gives

\[
r
\ge
\frac{\pi|x_*|}
{8S_m\sqrt{\Lambda-t}}
(1+O(\sqrt{\Lambda-t}))
\]

as a lower barrier on sign-detecting determinant order.

### Prior-art boundary

Hermite scaling of multiple zeros under the one-dimensional heat equation is classical. The released estate synthesis is the transport of that profile through `alpha=1/x^2` into the coefficient-Schur angular/order barrier. Literature priority for that transport is unresolved.

---

## R4-6 — positive threshold implies a finite multiple zero

Path:

`positive-newman-threshold-finite-multiple-zero-2026-09-12/README.md`

Commit:

`07e185ef1abb1f804eaaa01e6cb74fd40a96101e`

Using published positive-time high-zero reality/localization, the de Bruijn strip bound, compactness, and the analytic implicit-function theorem:

\[
\boxed{
\Lambda>0
\Longrightarrow
\exists x_*\in\mathbb R:
H_\Lambda(x_*)=H_\Lambda'(x_*)=0.
}
\]

Therefore Positive-Time Simplicity on `0<t<=0.2`, together with the known bounds `0<=Lambda<=0.2`, would imply `Lambda=0` and RH.

**Evidence class:** exact reduction from published ingredients; novelty not asserted.

---

## R4-7 — global determinant-order escape near a positive threshold

Path:

`positive-newman-threshold-global-order-escape-2026-09-12/README.md`

Initial commit:

`7b637321592730ee2d9e0a6c124457c44900d7c7`

Fixed-order corollary update:

`2fc48fe13d7172f7e793f25b5ae5035c893cada6`

Assume `Lambda>0`. Let `x_a>0` be the finitely many positive multiple threshold zeros, with multiplicities `m_a`, and define

\[
\mathcal S_\Lambda
=
\sum_a\frac{S_{m_a}}{x_a}.
\]

The full nonreal coefficient-spectral angular budget immediately below the threshold satisfies

\[
\boxed{
\Theta(t)
=
4\mathcal S_\Lambda\sqrt{\Lambda-t}
+O(\Lambda-t).
}
\]

Hence any negative consecutive coefficient Toeplitz/Schur minor must have

\[
\boxed{
r
\ge
\frac{\pi}
{8\mathcal S_\Lambda\sqrt{\Lambda-t}}
(1+O(\sqrt{\Lambda-t})).
}
\]

### Fixed-order positivity-neighborhood corollary

For every finite `R`, there is an `epsilon_R>0` such that under the hypothetical `Lambda>0`,

\[
\boxed{
D_{r,k}(t)>0
}
\]

for **every** `1<=r<=R`, **every** shift `k`, and every

\[
\Lambda-\varepsilon_R<t<\Lambda.
\]

Thus every fixed-order truncation of the coefficient determinant hierarchy becomes completely positive on a one-sided neighborhood **below** a hypothetical positive failure threshold. Any determinant proof of RH must therefore use genuinely uniform-in-order information; checking any fixed finite set of orders cannot see the threshold arbitrarily close from below.

### Why this is global rather than a local toy

- the Xi kernel is positive at `x=0`, so no collision site is at the singular spectral point;
- positive-time high zeros are uniformly real/simple near a positive threshold;
- only finitely many threshold zeros can be multiple;
- simple threshold zeros remain real locally by the implicit-function theorem;
- therefore every nonreal zero sufficiently close below the threshold belongs to one of finitely many Hermite collision clusters;
- the complete angular budget is the sum over those clusters.

**Evidence class:** conditional zeta-specific cross-representation theorem; no claim that `Lambda>0` or that a negative determinant exists after the barrier.

---

## R4-8 — public hygiene / killed route check

The PTS source packet records that an older Encirclement-VIII `value–torque` / `Hardy tangency` route used an incorrect conjugation pattern in the Polymath-15 main term. The exact `y=0` formula has the second finite sum proportional to the same sum rather than its conjugate.

A public-repository search during this pass found no live theorem note carrying the killed `value–torque` / `Hardy tangency` language, so no correction commit was needed in the public tree.

---

## R4-9 — simple-zero campaign disposition

The estate's historical `67.301545...%` candidate is **not promoted as a current record**.

The parameter-to-block transfer algebra remains useful, but the same seven-point Gram-stability mechanism is now public and has been repeatedly retuned/generalized in later August 2026 drafts to stronger numerical candidate bounds. The old decimal should therefore be treated as a historical reproducibility/certificate asset, not a current headline.

This pass did **not** create a redundant novelty note for the parameterized transfer formula.

---

## R4-10 — finite Weil/operator route disposition

Current 2026 external work has already made the finite-prime / Guinand–Weil operator route concrete:

- finite approximants live on the critical line;
- numerical approximations to Riemann zeros are extremely accurate;
- exact finite zero-sum dictionaries and explicit archimedean-tail budgets exist.

The estate search did **not** recover a proof of the missing finite-to-infinite convergence / positivity-transport theorem. Therefore no estate-owned operator theorem was published merely because the route is promising.

---

# Current mathematical map after Round 4

The strongest surviving terminal programs remain distinct:

1. **Branch C / determinant orbit-curvature:** prove the global Xi criterion in the critical two-scale region.
2. **PTS / de Bruijn–Newman transversality:** exclude every positive-time multiple real zero with a low/moderate-`x` plus high-`x` splice.
3. **Finite Weil/operator convergence:** prove a transport theorem from finite prime/operator objects to the infinite zeta/Weil object.
4. **Hausdorff / Poisson-binomial reconstruction:** companion coordinate whose missing theorem is quantitative infinite-tail stability.

The new cross-route result changes the scheduling logic:

> Near a hypothetical positive Newman threshold, bounded determinant order is provably the wrong coordinate: every fixed order remains positive sufficiently close below the threshold. PTS keeps the same obstruction finite in physical `x`-space.

That does not demote the determinant route globally. It tells the two programs to stop duplicating each other's badly conditioned representation.

---

# Release rule preserved

A public timestamp is evidence of public provenance, not proof of literature novelty or legal priority.

No item in this ledger claims RH is solved. The re-mining continues, and every item above remains open to later correction if a stronger source, counterexample, hidden hypothesis, or exact literature collision is found.
