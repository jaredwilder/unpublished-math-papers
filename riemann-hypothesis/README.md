# Riemann zeta research program — determinant geometry, live branch audit, simple-zero bounds, and de Bruijn–Newman simplicity

**Author:** Jared Wilder  
**Campaign dates:** 2026-08-11 through 2026-09-12

This directory is the public subject home for the RH/zeta mathematics recovered from the release estate.

## Current live campaign state

See:

`CURRENT-CAMPAIGN-STATE-2026-09-12.md`

The 2026-09-12 export reaches absolute MSL round 647. Its current campaign verdict is:

- **Branch C:** closed as an RH route after an exact counterexample audit proved its determinant criterion insufficient for real-rootedness;
- **Branch A:** active in principle, but its pair-energy and Hermite/truncation candidates were falsified or rendered uninformative;
- **Branch B:** screened and passing the campaign's current methodological tests, but otherwise untouched;
- **RH:** open.

This supersedes the earlier screenshot-era state in which Branch C looked one finite certification away from closing one of five links.

## 1. Determinant / total-positivity mathematics

Primary historical record:

`RH-TERMINAL-ENCIRCLEMENT-2026-08-11.md`

Recovered Encirclement II–V theorem spine:

`encirclement-ii-v-recovered/`

2026-09-11 determinant-curvature extraction:

`determinant-curvature-2026-09-11/`

Additional exact quartic/Gamma bridge:

`gamma-theta-quartic-bridge/`

### Exact determinant geometry now public

- Desnanot–Jacobi gives `R+A=1` for the two normalized neighboring-minor ratios.
- The nonlinear odds lattice admits the exact rational family `Y_(r,k)=(r+mu)/(k+nu)`; the Toeplitz boundary selects `Y*=r/k`.
- For the factorial comparison determinant,
  `D0_(r,k)=prod_{j=0}^{r-1} j!/(k+j)!`.
- Writing `U=log(D/B)` against a positive comparison determinant array gives the exact nonlinear comparison equation
  `R_B exp(Delta_k^2 U) + A_B exp(Delta_r^2 U) = 1`.
- On finite lattice domains this equation has a strong maximum/comparison principle and a boundary-homotopy positivity theorem.
- Along the de Bruijn–Newman coefficient flow, `V=partial_t U` satisfies
  `R_D Delta_k^2 V + A_D Delta_r^2 V = 0`, while `partial_t^2 U` is superharmonic with an explicit negative quadratic source.
- Dual Jacobi–Trudi gives an exact order/shift swap through the reciprocal series.
- In the real-zero phase, consecutive minors are rectangular Schur polynomials; their normalized zero-parameter sensitivities satisfy `0 <= p_j <= 1/k` and sum to one.
- Sorted angular defects satisfy the sharper top-k criterion
  `r * sum_{j=1}^k theta_j < pi/2  =>  D_(r,k) > 0`.
- Under verified reciprocal-pole hypotheses, fixed-shift dual determinants are eventually strictly positive; combined with the primal large-shift frontier, any hypothetical escaping failure must have both `r -> infinity` and `k -> infinity`.

Fresh public reruns of the recovered Encirclement II–V source verifiers give

**7/7 + 5/5 + 6/6 + 6/6 = 24/24 successful checks.**

### 2026-09-11 curvature results

- exact curvature reparameterization `Z=(r/k) Q/(1-Q)`;
- exact reciprocal duality `Z_a(r,k) Z_b(k,r)=1`;
- exact cross-campaign identification
  `Z = exp(Delta_k^2 U - Delta_r^2 U)`;
- strict positivity of every consecutive Toeplitz minor does **not** imply simple zeros: `(1+z)^2 e^z` has a double zero at `-1` while all consecutive minors are strictly positive;
- rigorous order-one corridor
  `1/[k(exp(4/k)-1)] < Z_(1,k) < 1/[k(exp(1/(2k))-1)]`;
- reproduced fixed-slope finite data at `theta=1/2, 2/3, 3/4` favor a positive-limit model on the available tails.

These exact identities and negative theorems remain valid even though the later Branch C sufficiency criterion was refuted.

## 2. Branch C — historical reduction, now refuted as an RH route

Directory:

`branch-c-five-link-reduction/`

The campaign genuinely reduced and certified a substantial determinant/coefficient criterion. The later sufficiency test is decisive, however:

- 1,686 of 3,059 explicitly non-real-rooted test polynomials satisfy the criterion;
- after full available depth, interior shifts and both criterion forms are imposed, 1,445 of 2,284 still satisfy it.

So the criterion is necessary in the intended real-rooted family but **not sufficient**.

The exact falsifier scripts and outputs are published in the directory. The earlier five-link novelty audit has been superseded accordingly.

## 3. Branch A — de Bruijn–Newman heat-flow instruments

The current campaign built a flat-cost moment-series evaluator, derived a cancellation precision rule, and rigorously validated a finite zero window with a 64-piece truncation envelope.

Its first candidate quantity, pair energy

`E(t)=sum_{i<j} 1/(z_i-z_j)^2`,

was then falsified as a sufficient statistic: exact complex-root controls can have energy zero, and the quantity can fall after a pair leaves the real axis.

A Hermite/minor separator passed finite exact controls but became uninformative on the natural polynomial truncations of the entire function because the truncations themselves carry many spurious complex roots.

See `CURRENT-CAMPAIGN-STATE-2026-09-12.md` for the exact finite results.

## 4. Branch B — arithmetic Chebyshev-error lane

Branch B is the only one of the three current lanes that survives the campaign's sufficiency / non-tautology / informativeness screens.

The current export contains only a finite prime-power probe through `x=200000`; those values are not evidence for RH beyond their stated finite range. The lane is the current handoff, not a solved result.

## 5. Simple-zero proportion candidate

Directory:

`simple-zero-67.301545-candidate/`

The recovered verifier establishes the local inequality for

`q = 29/100000`, `L = 341/100000`

on two independent subdivision grids. The exact propagation algebra then gives the candidate lower bound

`0.673015452606376894...`

for the simple-zero proportion within the stated seven-point stability framework.

## 6. PTS / de Bruijn–Newman interval-certifier program

Directory:

`pts-terminal-close/`

Frozen target:

> For every real `x` and every `t in (0,0.2]`, if `H_t(x)=0`, then `H_t'(x) != 0`.

Recovered material includes the frozen implication chain, ten-mechanism close anatomy, interval-certifier source, derivative/transversality toolkit, repaired real-axis Riemann–Siegel adapter, and the exact threshold-collision implication

`Lambda > 0 => H_Lambda has a finite multiple real zero`.

During public extraction the certifier self-test was rerun from exported source and passed **8/8, exit 0**.

## Release reading rule

Use each result at its actual mathematical scope. Exact determinant identities, comparison theorems, Schur bounds, formal fragments, finite certifications, negative theorems, computational asymptotics and open terminal lemmas are different evidence classes.

A later route refutation does not erase valid lower mathematics; it changes what those results imply.