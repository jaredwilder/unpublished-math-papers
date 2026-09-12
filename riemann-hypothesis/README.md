# Riemann zeta research program — determinant geometry, Branch C reduction, simple-zero bounds, and de Bruijn–Newman simplicity

**Author:** Jared Wilder  
**Campaign dates:** 2026-08-11 and 2026-09-11  
**Public extraction:** 2026-09-11

This directory is the public subject home for the RH/zeta mathematics recovered from the current release estate.

## 1. Determinant / total-positivity program

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
- The induced nonlinear odds lattice admits the exact rational family
  `Y_(r,k)=(r+mu)/(k+nu)`; the Toeplitz boundary selects the factorial orbit `Y*=r/k`.
- For the factorial comparison determinant,
  `D0_(r,k)=prod_{j=0}^{r-1} j!/(k+j)!`.
- Writing `U=log(D/B)` against any positive comparison determinant array gives the exact nonlinear comparison equation
  `R_B exp(Delta_k^2 U) + A_B exp(Delta_r^2 U) = 1`.
- On finite lattice domains this equation has a strong maximum/comparison principle and a boundary-homotopy positivity theorem.
- Along the de Bruijn–Newman coefficient flow, `V=partial_t U` satisfies the exact adaptive harmonic equation
  `R_D Delta_k^2 V + A_D Delta_r^2 V = 0`, while `partial_t^2 U` is superharmonic with an explicit negative quadratic source.
- Consequently a first loss of consecutive-minor positivity cannot nucleate at a bounded lattice point with positive surrounding boundary; any first-loss sequence must escape in index space.
- Dual Jacobi–Trudi gives an exact order/shift swap through the reciprocal series.
- In the real-zero phase, consecutive minors are rectangular Schur polynomials. Their normalized zero-parameter sensitivities satisfy `0 <= p_j <= 1/k` and sum to one.
- Sparse complex angular defects obey the exact phase criterion
  `r * sum |theta_j| < pi/2  =>  D_(r,k) > 0`.
- For a single conjugate pair, any detecting determinant order must satisfy
  `r >= pi/(2|theta|)`.

The recovered verifier packets report **7/7 + 5/5 + 6/6 + 6/6** successful algebraic/combinatorial checks across Encirclement II–V. See `encirclement-ii-v-recovered/VERIFIER-SUMMARY.md`.

### 2026-09-11 curvature results

- exact curvature reparameterization `Z=(r/k) Q/(1-Q)`;
- exact reciprocal duality `Z_a(r,k) Z_b(k,r)=1`;
- strict positivity of every consecutive Toeplitz minor does **not** imply simple zeros: `(1+z)^2 e^z` has a double zero at `-1` while all consecutive minors are strictly positive;
- rigorous order-one corridor
  `1/[k(exp(4/k)-1)] < Z_(1,k) < 1/[k(exp(1/(2k))-1)]`;
- reproduced fixed-slope data at `theta=1/2, 2/3, 3/4` strongly select a positive-limit model on the available tails;
- five successful kernel-checked Lean fragments from the exported run.

The fixed-slope numerical extrapolation remains a computational frontier; the exact identities above are independent of that extrapolation.

## 2. Branch C — five-link sufficient reduction

Directory:

`branch-c-five-link-reduction/`

The live Branch C state records a five-link sufficient chain to RH and the following reduction of its third link:

- `epoch_twenty_chain_sealed` — CLOSED / KERNEL_CHECKED;
- the earlier dispersion formulation was recast;
- `first_rung_is_a_quadratic` — CLOSED;
- `first_rung_numbers_settled` — CLOSED, 22-digit numerical settlement with large sign margin;
- higher-rung propagation is supported by a monotonicity computation through rung 40;
- the remaining obligation for that link is a certified enclosure replacing ordinary quadrature.

The live bottleneck K211 / BN5 therefore records:

`4 open analytic links + 1 finite certification job`.

The dedicated novelty audit is `BRANCH-C-NOVELTY-AUDIT-2026-09-11.md`.

## 3. Simple-zero proportion candidate

Directory:

`simple-zero-67.301545-candidate/`

The recovered verifier establishes the local inequality for

`q = 29/100000`, `L = 341/100000`

on two independent subdivision grids. The exact propagation algebra then gives the candidate lower bound

`0.673015452606376894...`

for the simple-zero proportion within the stated seven-point stability framework.

The packet includes the generalized block lemma, the exact transfer formula, two successful outward-rounded interval runs, and an Arb/python-flint second-trust-base verifier that was written but not executed in the source environment.

## 4. PTS / de Bruijn–Newman interval-certifier program

Directory:

`pts-terminal-close/`

Frozen target:

> For every real `x` and every `t in (0,0.2]`, if `H_t(x)=0`, then `H_t'(x) != 0`.

Recovered material includes the frozen implication chain, ten-mechanism close anatomy, the interval-arithmetic certifier, and the direct-quadrature scaling wall.

During public extraction the certifier's built-in self-test was rerun from the exported source and passed **8/8, exit 0**. The original export did not carry the complete historical 23-receipt bundle, so the historical finite certificate claims remain distinguished from freshly reproduced receipts.

## 5. Release reading rule

Use each result at its actual mathematical scope. Exact determinant identities, comparison theorems, Schur bounds, formal fragments, finite certified inequalities, computational asymptotics and open terminal lemmas are different evidence classes; none needs to be rhetorically shrunk merely because RH itself remains open.
