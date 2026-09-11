# Erdős #1005 — Farey similarly-ordered reduction estate

**Author:** Jared Wilder  
**Recovered public extraction:** 2026-09-11  
**Canonical target status:** **NOT CLAIMED CLOSED HERE**

This directory is a release-day recovery from the estate atlas for the July 25, 2026 Erdős #1005 / Farey campaign. The atlas points to the original internal finding `oracle/ledger/findings/erdos-1005-farey-similarly-ordered-2026-07-25.md`; that complete source artifact was not recovered as a standalone Library file during this extraction. Therefore this is deliberately a **scope-preserving reconstruction of the mathematical assets and retractions visible in the atlas**, not a substitute for the missing full proof packet.

## Unconditional mathematical assets recovered

### Reachability gcd criterion

Write

`b = 3a + rho`.

Then

`gcd(a,b)=gcd(a,rho)`

and

`gcd(a+1,b-1)=gcd(a+1,rho-4)`.

Thus the elementary interval admissibility/reachability constraints reduce to the two small-offset gcd conditions. The source reports this criterion as proved and independently checked on `rho=1..39`, `a=1..599` with zero discrepancies.

### Even-offset exclusion

The same criterion immediately kills `rho=2`: reachability would require both `gcd(a,2)=1` and `gcd(a+1,2)=1`, forcing `a` simultaneously odd and even. For `rho=4`, `gcd(a+1,0)=a+1>1` for every `a>=1`. The source records the broader even-`rho` obstruction as an unconditional arithmetic result.

### Exact lattice-count reparameterization

The campaign substitutes

`q=3p+j`, `b=3a-r`

into the defining Farey interval inequalities and rewrites the count `N(a,b;n)` as a coprime lattice-point count in `(p,j)`. The recovered source summary records the constraints

- `p>=1`,
- `1 <= 3p+j <= n`,
- `gcd(p,j)=1`,
- `-rp-aj > 0`,
- and a second linear window inequality beginning `(r+4)p+(a+1)j > ...`.

Because the atlas summary truncates the final right-hand side, **this release does not invent or complete that formula**. The load-bearing point preserved here is that the change of variables eliminates `b` from the window inequalities and converts the Farey count into an exact lattice-count problem.

### Window-nesting lemma

For `rho=-r in {1,2,3}` and every `p>=1`, the source records a proved strict inclusion

`window(a+1,p) ⊂ window(a,p)`.

The upper endpoint decreases because `rho p/(a+1) < rho p/a`; the lower endpoint moves in the compatible direction exactly for the sharp range `rho<4`. The consequence recorded by the campaign is that, for the corresponding offsets `r in {-1,-2,-3}`, the minimizing admissible `a` occurs at the maximal allowed `a`.

### Small-a density constant

The source records the exact finite arithmetic fact that the relevant local constant

`Phi(a)/(a(a+1))`

has minimum `2/7` at `a=6` over the small-`a` regime used in the `rho>=5` exclusion argument. The campaign explicitly says the remaining difficulty is the rigorous error term needed to turn the asymptotic density heuristic into the required lower bound; the margin is only `1/126` (about 2.9%).

## Finite / computational reduction assets

The atlas records a scaling map

`phi:(a,b,n) -> (a+12,b+36,n+36)`

preserving `r=3a-b` and generating a period-36 / quasi-linear structure in the relevant margin sequence. A prior low-order conjecture-miner refusal was wrong: clearing denominators exposed the period 36, which requires order 37 rather than the previously tried order at most 10.

The campaign further records a finite-computational reduction of the target to a “two-orbit dominance” theorem plus bounded inverse statements / a finite table. The atlas itself labels that dominance statement as the **one real remaining global theorem** after the numerical periodicity was isolated. Therefore this public extraction does **not** promote the finite verification to a global proof.

## Retractions and negative gold

The following errors are part of the release, not deleted history:

1. **False interval-length monotonicity.** “Decreasing `b` lengthens the interval, therefore the Farey count increases” is false. Farey counts are arithmetic; geometric interval length alone does not imply monotonicity. The repaired route uses exact set inclusion in the `(p,j)` windows.
2. **Miner refusal misdiagnosed as irregularity.** Refusal at recurrence/quasi-polynomial order at most 10 was reported as evidence that the margin was irregular. This was retracted after denominator clearing exposed period 36.
3. **Scoped scan reported as global.** At least two campaign retractions shared the error class that a scan on a restricted `n`-window was described with global words such as “exactly” or “only.”
4. **Wrong-variable minimization / one-class lower bound.** The campaign records two self-inflicted lower-bound errors: minimizing a bound in a regime where the true target was not extremal, and treating one residue-class contribution as though it were the entire count.

## Authority boundary

This directory publishes the mathematics that can be recovered exactly enough from the estate atlas. It does **not** claim:

- that Erdős #1005 is closed;
- that the truncated `(p,j)` identity has been reconstructed beyond the visible source text;
- that the finite period-36 verification implies the missing global dominance theorem;
- or that any of these statements are historically novel.

The missing complete source packet remains a provenance-recovery target. If recovered later, it should be added here rather than silently replacing this audit.