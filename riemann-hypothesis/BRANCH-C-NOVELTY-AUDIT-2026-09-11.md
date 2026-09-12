# Branch C novelty audit — 2026-09-11

**Author:** Jared Wilder  
**Purpose:** novelty / prior-art firewall for the live RH Branch C reduction visible in the 2026-09-11 run.

## Executive result

The literature neighborhood is **not empty**, and two nearby results must be cited explicitly:

1. **Dimitrov–Lucas (2011), Higher order Turán inequalities for the Riemann xi-function**, Proc. AMS 139 (2011), DOI 10.1090/S0002-9939-2010-10515-4. They prove the degree-3 / higher-order Turán inequalities for the Riemann xi coefficient sequence and hence hyperbolicity of the associated generalized Jensen polynomials of degree three.

2. **Planat–Solé (2026), Second-Level Concavity of the Riemann Xi Kernel**, arXiv:2608.19160, submitted 2026-08-19. They prove the Csordas–Dimitrov conjecture that, for the classical Riemann theta kernel, the first Laguerre expression

   `f(t)=s'(t)^2-s(t)s''(t)`, `s(t)=Phi(sqrt(t))`

   has `log f` strictly concave on `(0,infinity)`. Their proof contains an exact quartic reduction, rigorous finite interval certificates, and a monotonicity close.

These results mean that **log-concavity / second-level-concavity / degree-3 Turán statements, by themselves, are not new claims for this release**.

## What the live Branch C reduction appears to add

The live run shown on 2026-09-11 is organized as a **five-link sufficient chain to RH**, not merely as another proof of the classical low-degree Turán inequalities.

The current state reports:

- one link reduced to a finite first-rung computation;
- the first-rung algebra reduced to a quadratic;
- the numerical sign settled to 22 digits with a large sign margin;
- higher rungs propagated by a monotonicity verified through rung 40;
- the remaining task for that link reduced to a certified enclosure replacing ordinary quadrature;
- four other links remain genuinely analytic.

**That architectural reduction is the object whose novelty matters.**

The current literature search did **not** locate a paper presenting the same five-link RH closure chain or the same statement that one of those five links reduces to this finite certification problem.

That should therefore be treated as a **candidate novel reduction**, subject to exact theorem-by-theorem comparison once the live W/K nodes are exported.

## Important overlap warning

The words “quartic”, “quadratic”, “monotonicity”, “theta kernel”, “interval certificate”, and “higher Turán” occur in the 2026 Planat–Solé paper. Therefore the live run must not claim novelty merely because its proof also contains a quadratic or finite certificate.

The comparison must be at the level of exact mathematical statements:

- What is the precise Branch C link?
- What is the exact first-rung inequality?
- What is the quadratic after reduction?
- What monotonicity propagates the first rung to all higher rungs?
- How does that link sit in the five-link sufficient chain to RH?

If those statements are not equivalent to the Planat–Solé second-level concavity theorem or the Dimitrov–Lucas degree-3 Turán theorem, then the reduction may be genuinely new even though it uses nearby technology.

## Quartic/Gamma bridge

The exact substitution

`y = pi x^4`

maps the normalized quartic density `exp(-pi x^4)` to a `Gamma(1/4,1)` law. The corresponding squared-variable dispersion is

`Gamma(1/4)^2 / (4 Gamma(3/4)^2) - 1 = 1.188439615...`.

This exact identity is elementary special-function mathematics and should **not** be advertised as the principal novelty. Its role is as a coordinate simplification / exact benchmark inside the live Branch C proof.

## Prior-art map

### Known before this run

- ordinary Turán inequalities for the Riemann xi coefficients;
- higher-order / degree-3 Turán inequalities (Dimitrov–Lucas 2011);
- eventual hyperbolicity of fixed-degree Jensen polynomials and effective versions (Griffin–Ono–Rolen–Thorner–Tripp–Wagner and related work);
- first-level kernel log-concavity;
- second-level kernel log-concavity / Csordas–Dimitrov conjecture (Planat–Solé 2026).

### Not found in this search

- the exact five-link Branch C RH sufficient chain visible in the current run;
- the exact finite first-rung certification reduction as a named link in such a chain;
- the exact “one of five links has become a finite settled computation, four remain analytic” decomposition;
- a published theorem matching the current internal K202 → K208 → K210 → K211 progression.

This is **not** a proof that no such prior art exists. It is the current novelty boundary after direct search of the closest known literature.

## Release rule

Do not publish the first-rung result as “new second-level concavity” or “new higher-order Turán inequality” unless the exact statement genuinely exceeds those known theorems.

Publish the exact Branch C contribution at its real scope:

> a reduction inside a five-link sufficient RH architecture, with one link converted from an analytic problem into a finite certifiable inequality, if the exact exported statements survive comparison with Planat–Solé and Dimitrov–Lucas.

That is the claim to defend.
