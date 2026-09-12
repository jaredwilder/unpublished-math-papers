# RH campaign state — 2026-09-12 export

**Author:** Jared Wilder  
**Snapshot:** active session export at absolute MSL round 647

This note records the campaign's current mathematical state after the 2026-09-12 export. It supersedes the earlier screenshot-era Branch C status.

## Headline

The current campaign has **no live RH route**.

- **Branch C:** closed as a route after an exact counterexample audit proved its determinant criterion insufficient for real-rootedness.
- **Branch A:** active in principle, but its best computable candidate quantities were successively falsified or rendered uninformative.
- **Branch B:** the only lane that passed the campaign's current screening laws; it had not yet been attacked beyond a finite Chebyshev-error probe.

RH remains open.

## Branch C — decisive refutation

The determinant criterion

\[
rD_{r,k-1}D_{r,k+1}\le kD_{r+1,k}D_{r-1,k}
\]

was tested on polynomials containing an explicit irreducible quadratic factor and hence a provably non-real conjugate pair.

Fresh rerun from the exported source:

- 3,059 non-real-rooted polynomials tested;
- 1,686 satisfy the criterion.

Full-depth audit:

- 2,284 non-real-rooted polynomials tested;
- 1,445 satisfy the square-free criterion;
- the same 1,445 satisfy the original entry form.

The route's lower identities and certifications survive, but the criterion cannot imply real-rootedness.

A second sufficiency screen tested five nearby coefficient criteria on 900 non-real-rooted positive-coefficient polynomials:

| criterion | admitted false-target objects |
|---|---:|
| ordinary Newton/log-concavity | 899 / 900 |
| sharp Newton | 169 / 900 |
| Hankel depth 3 | 846 / 900 |
| sharp Newton + Hankel depth 3 | 169 / 900 |
| sharp Newton + derivative condition | 169 / 900 |

On this constructed family, stacking the last two conditions adds no exclusion beyond sharp Newton.

## Branch A — heat-flow instruments built and killed

Branch A works directly with the de Bruijn–Newman deformation, so its terminal criterion is equivalent to the target by construction.

### Pair-energy experiment

The campaign constructed a flat-cost moment-series evaluator and derived a precision rule for cancellation. A sized run produced seven zeros at each of `t=0.2,0,-0.2` and found the pair energy

\[
E(t)=\sum_{i<j}\frac1{(z_i-z_j)^2}
\]

rising as the deformation parameter decreased:

- six-zero truncation: `0.09964308 -> 0.10092331 -> 0.10241583`;
- all seven zeros: `0.13036998 -> 0.13159389 -> 0.13301904`.

A 64-piece rigorous moment envelope then bounded the zero displacement caused by truncation; at the hardest reported point `z=85` the shift bound was about `0.001998`, versus spacing of order six.

### Why pair energy died

The quantity is not sufficient for real-rootedness. Exact finite atomic controls show:

- all-real controls can have positive energy (`1.4635`, `5.9258`, ...);
- an all-complex control can have energy exactly `0`.

The campaign also observed the energy rise as a pair approached an edge and then collapse after the pair left, making the proposed ceiling anti-correlated with the desired property.

### Hermite-sequence route

A Hermite/minor criterion cleanly separated finite all-real controls from finite complex controls and was non-tautological on that bench.

Applied to polynomial truncations of the actual entire function, however, it failed uniformly: the truncations themselves contain many spurious complex roots. After normalization, the reported truncations had only `0/10`, `2/16`, `2/22`, `2/26`, `2/30`, and `4/34` real roots, and the Hermite minors remained negative.

Thus the test is uninformative on this approximation sequence even if the underlying entire function were real-rooted.

## Branch B — screened, not solved

The remaining untouched lane is the classical arithmetic Chebyshev-error formulation of RH.

The campaign's finite probe computed `psi(x)-x` exactly from prime powers through `x=200000`:

| x | psi(x)-x | |err|/sqrt(x) |
|---:|---:|---:|
| 1,000 | -3.3190878 | 0.10495877 |
| 10,000 | 13.396693 | 0.13396693 |
| 50,000 | -14.042261 | 0.062798898 |
| 100,000 | 51.564026 | 0.16305977 |
| 200,000 | 26.938798 | 0.060236983 |

These finite values prove nothing about RH. Their purpose was only to verify that Branch B passes the campaign's three methodological screens:

1. the criterion is genuinely sufficient/equivalent rather than merely necessary;
2. it transports the problem into a different arithmetic quantity rather than restating the answer;
3. the quantity can be computed directly rather than inferred from a contaminated approximant.

Branch B is therefore the next campaign lane, not a solved or even substantially advanced RH argument.

## Methodological theorem bank produced by the campaign

The campaign also formalized several reusable laws:

- one false-target witness satisfying a proposed criterion refutes the entire implication;
- a finite sum of nonnegative terms dominates each term;
- removing a positive term lowers such an energy;
- a separator equivalent to the target property adds no information;
- a test constant across every approximant in a family discriminates nothing about the limiting target.

These are proof-engineering laws, not facts about zeta.

## Current handoff

At the export boundary:

\[
\boxed{\text{Branch C dead; Branch A without a usable sufficient quantity; Branch B screened and untouched.}}
\]

The next mathematical work should begin from Branch B or from a genuinely new criterion that passes a false-target sufficiency screen before expensive certification is attempted.