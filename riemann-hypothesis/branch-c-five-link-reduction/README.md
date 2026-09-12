# Branch C — five-link RH reduction

**Author:** Jared Wilder  
**Live state date:** 2026-09-11  
**Public extraction:** 2026-09-11

## Result

The current Branch C program is organized as a **five-link sufficient chain to the Riemann Hypothesis**. In the live state, one of those five links has been reduced from an open analytic problem to a **finite certification problem**.

The state recorded on 2026-09-11 is:

- the five-link implication chain is sealed in the project’s formal layer (`epoch_twenty_chain_sealed`, node K172, recorded as `CLOSED` / `KERNEL_CHECKED`);
- the third link was recast after an earlier dispersion formulation was rejected;
- the surviving first rung was reduced algebraically to a quadratic condition (`first_rung_is_a_quadratic`, K208, `CLOSED`);
- the first-rung numerical values were settled to 22 digits with a large sign margin (`first_rung_numbers_settled`, K210, `CLOSED`);
- the analytic tail was bounded below the numerical error scale recorded by the run;
- higher rungs are propagated by a monotonicity mechanism verified through rung 40;
- the remaining obligation for this link is **certified enclosure** replacing ordinary numerical quadrature.

The live bottleneck record K211 / BN5 therefore summarizes the architecture as:

> **one of the five links is a finite settled computation awaiting certification; the other four remain open analytic problems.**

Equivalently, the Branch C frontier has changed from five analytic obligations to

\[
\boxed{4\text{ open analytic links}+1\text{ finite certification job}.}
\]

That reduction is the result recorded here.

## What this is not

This is not a claim that RH is proved.

It is not a claim that the finite first-rung computation is already certified merely because multiple ordinary quadratures agree.

It is also not being presented as a new proof of ordinary log-concavity, second-level concavity, or the classical low-degree Turán inequalities. Those surrounding results have substantial prior literature.

The mathematical contribution isolated here is the **collapse of one full link in a five-link sufficient RH architecture from an analytic theorem problem to a bounded certification problem**.

## Current proof-state spine

The live state records the following sequence:

1. **K172 — chain sealed.**  
   `epoch_twenty_chain_sealed` — `CLOSED`, `KERNEL_CHECKED`.

2. **K202 — dispersion route repaired/recast.**  
   The earlier formulation is not carried forward as the active criterion; the replacement branch is the one used below.

3. **K208 — first rung reduced to a quadratic.**  
   `first_rung_is_a_quadratic` — `CLOSED`.

4. **K210 — first-rung numerical content settled.**  
   `first_rung_numbers_settled` — `CLOSED`.
   The live state reports 22 settled digits, roughly 70% sign margin, and an analytic tail beneath the displayed numerical uncertainty.

5. **K211 / BN5 — architectural consequence.**  
   The first rung is finite and settled numerically; its certification is mechanical. Higher rungs follow from a monotonicity checked through rung 40. The other four links remain genuinely analytic.

The exact node formulas and formal artifacts should be appended here from the next session export so the entire chain can be audited statement-by-statement outside the live environment.

## Prior-art position

A direct novelty audit was performed against the closest known families, including:

- Csordas–Varga moment and concavity criteria;
- Dimitrov–Lucas higher-order Turán inequalities for the Riemann xi function;
- Jensen-polynomial / Laguerre–Pólya programs for Xi coefficients;
- later arbitrary-fixed-order Laguerre-inequality results;
- iterated Laguerre-operator inequalities;
- Planat–Solé’s 2026 proof of the Csordas–Dimitrov second-level-concavity conjecture for the Riemann Xi kernel, which already uses exact low-degree reduction, interval certification and monotonicity.

Those results overlap the surrounding machinery and therefore must be cited where relevant.

The search did **not** locate the same five-link sufficient RH architecture together with the same K202 → K208 → K210 → K211 reduction in which one whole link is converted to a finite certification problem.

Accordingly the present novelty target is not a low-level concavity or Turán statement. It is the **proof-architecture reduction itself**.

See:

`../BRANCH-C-NOVELTY-AUDIT-2026-09-11.md`

for the current prior-art firewall.

## Release status

The reduction is public now.

What remains to complete this packet is not to decide whether the result is worth releasing; it is to attach the exact exported statements, formal files, the certified enclosure, and the monotonicity proof/receipt when those bytes are available.

The public mathematical status as of 2026-09-11 is therefore:

\[
\boxed{\text{One of five RH-sufficient links has been reduced to finite certification.}}
\]
