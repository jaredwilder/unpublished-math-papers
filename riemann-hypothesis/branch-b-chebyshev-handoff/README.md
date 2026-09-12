# Branch B — arithmetic Chebyshev-error handoff

**Author:** Jared Wilder  
**Campaign snapshot:** 2026-09-12, final round 647

Branch B is the arithmetic/explicit-formula lane left untouched by the 23-epoch campaign until its final round.

Its target is the classical Chebyshev-error formulation of RH: control of

\[
\psi(x)-x
\]

at essentially square-root scale.

The campaign did **not** advance that theorem. Its final action was to screen the lane before spending a new epoch on it.

## Why this lane survived the campaign's screen

The campaign had learned three requirements from the failure of Branches A and C:

1. **Sufficiency:** the proposed criterion must actually imply or be equivalent to the target, not merely be necessary.
2. **Non-tautology:** the working quantity must transport the problem into a genuinely different mathematical representation rather than rename the target.
3. **Informativeness:** the quantity used in computation must be evaluated directly or by an approximant that can discriminate the property of interest.

Branch B passes those methodological checks at the level of its classical formulation:

- the Chebyshev-error criterion is classically equivalent to RH at the appropriate asymptotic scale;
- it transports the analytic zero problem into arithmetic prime-power data;
- finite `psi(x)` values can be computed directly from primes, without a contaminated polynomial truncation.

This says the lane is worth attacking. It says nothing about whether the attack will succeed.

## Finite exact probe

The exported program computed `psi(x)` by direct summation over every prime power up to `x<=200000`.

| x | psi(x)-x | |err|/sqrt(x) | |err|/(sqrt(x) log^2 x) |
|---:|---:|---:|---:|
| 1,000 | -3.3190878 | 0.10495877 | 0.0021996058 |
| 10,000 | 13.396693 | 0.13396693 | 0.0015792332 |
| 50,000 | -14.042261 | 0.062798898 | 0.00053643277 |
| 100,000 | 51.564026 | 0.16305977 | 0.0012301992 |
| 200,000 | 26.938798 | 0.060236983 | 0.00040430705 |

These five finite values are not asymptotic evidence for RH. They are simply a reproducible zero-cost instrument check on the quantity the next campaign would need to study.

## Handoff

At the export boundary:

- Branch C has been refuted as a sufficient route;
- Branch A has a rigorous numerical instrument but no surviving computable sufficient statistic;
- Branch B is screened and untouched.

Therefore Branch B is the honest next lane if the campaign continues.

Source program: `branchB.py`.