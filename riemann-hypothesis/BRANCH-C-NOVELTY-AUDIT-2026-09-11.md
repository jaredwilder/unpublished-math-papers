# Branch C novelty audit v2 — statement-level comparison

**Author:** Jared Wilder  
**Date:** 2026-09-11  
**Object audited:** the live Branch C proof architecture, especially the K202 → K208 → K210 → K211 reduction in which one of five RH links is converted from an analytic problem into a finite certification problem.

## Verdict

The first novelty pass was too shallow. It compared Branch C mainly against “second-level concavity” and degree-3 Turán inequalities. The relevant prior-art neighborhood is substantially larger: classical moment inequalities, necessary/sufficient Laguerre–Pólya criteria, Jensen-polynomial hyperbolicity, all-order asymptotic Laguerre inequalities, iterated Laguerre operators, recent theta-kernel concavity, and at least one 2026 moment-inequality proof program claiming an RH route.

After widening the search to those families, the conclusion is sharper:

> **The local technology is heavily pre-existing. The architectural reduction shown by the live Branch C state was not found in the searched literature.**

In particular, none of the sources located below presents the same object now recorded by K211:

> a five-link sufficient chain to RH in which the third link has been reduced to a finite first-rung certification problem, its higher rungs follow from a monotonicity, and the other four links remain analytic.

That is the release-worthy novelty target. It is much stronger and much more specific than claiming novelty for log-concavity, a quartic reduction, a quadratic inequality, a Turán inequality, interval arithmetic, or a monotonicity argument by themselves.

---

## 1. What the live run has actually reduced

The live state visible on 2026-09-11 records the following chain of consequences.

### K202 — dispersion recasting

The earlier plain-log-concavity sufficiency hypothesis is rejected/recast. The live run no longer treats ordinary log-concavity as enough for the relevant dispersion inequality.

This matters because ordinary kernel log-concavity is old mathematics and, by itself, cannot be the new contribution.

### K208 — first rung is a quadratic

The surviving first-rung condition is algebraically reduced to a quadratic condition.

The novelty question is **not** whether quadratic reductions exist in theta-kernel proofs; they do. The novelty question is whether this particular quadratic is exactly equivalent to the first rung of a link that is itself sufficient inside the five-link RH chain.

### K210 — first-rung numbers settled

The live state reports the first rung numerically settled to 22 digits, with roughly a 70% sign margin and an analytic tail below 10^-72. Nine quadrature runs agree. The remaining obligation is not parameter discovery but a rigorous enclosure replacing ordinary quadrature.

### K211 / BN5 — architectural consequence

The live ledger states:

- the third link's first rung is a finite computation;
- its numerical sign is settled;
- its certification is mechanical;
- higher rungs follow from a monotonicity verified through rung 40;
- the other four links remain genuinely analytic.

Therefore the research-state change is:

> **one of five analytic RH links has been converted into a bounded finite proof obligation.**

That is the statement novelty must be tested against.

---

## 2. Prior art that definitely overlaps local ingredients

### 2.1 Csordas–Varga (1988): moment inequalities from kernel concavity

George Csordas and Richard S. Varga, *Moment Inequalities and the Riemann Hypothesis*, Constructive Approximation 4 (1988), 175–198. DOI: 10.1007/BF02075457.

They study

`b_m(lambda) = integral_0^infinity t^(2m) exp(lambda t^2) Phi(t) dt`

and prove Turán-type moment inequalities. A central ingredient is a constructive proof that

`log Phi(sqrt(t))`

is strictly concave. They derive a general class of moment inequalities valid for all real lambda.

**Consequence for priority:** a claim of novelty based merely on kernel log-concavity, moment-ratio inequalities, or deriving Turán inequalities from that concavity is not defensible.

### 2.2 Csordas–Varga (1990): necessary and sufficient RH/real-zero criteria

George Csordas and Richard S. Varga, *Necessary and Sufficient Conditions and the Riemann Hypothesis*, Advances in Applied Mathematics 11 (1990), 328–357. DOI: 10.1016/0196-8858(90)90013-O.

This paper systematically develops necessary and sufficient conditions for Fourier transforms / real entire functions to have only real zeros and applies them to the Riemann xi-function.

**Consequence for priority:** “a chain of inequalities sufficient for real zeros” is not novel as a genre. Branch C has to be compared at the level of its exact five links and exact implications.

### 2.3 Csordas–Dimitrov: double Turán / second-level concavity problem

Csordas and Dimitrov formulate the double Turán inequalities for the Riemann xi coefficients and the concavity problem for

`s(t)=Phi(sqrt(t))`,

`f(t)=s'(t)^2-s(t)s''(t)`,

asking for

`(log f(t))'' < 0`.

The literature already understood this as a route to stronger coefficient inequalities.

### 2.4 Dimitrov–Lucas (2011): degree-3 / higher-order Turán inequalities

Dimitar K. Dimitrov and Fabio R. Lucas, *Higher order Turán inequalities for the Riemann xi-function*, Proceedings of the AMS 139 (2011), 1013–1022. DOI: 10.1090/S0002-9939-2010-10515-4.

They prove the higher-order Turán inequalities for the xi coefficient sequence, establishing hyperbolicity of the associated generalized Jensen polynomials of degree three.

**Consequence for priority:** degree-2/3 Jensen or first higher-order Turán positivity is old.

### 2.5 Griffin–Ono–Rolen–Zagier and effective Jensen-polynomial work

Pólya's criterion identifies RH with hyperbolicity of all relevant Jensen polynomials. Griffin–Ono–Rolen–Zagier prove eventual hyperbolicity for every fixed degree; Griffin–Ono–Rolen–Thorner–Tripp–Wagner later make the xi result effective.

Relevant references include:

- Griffin, Ono, Rolen, Zagier, *Jensen polynomials for the Riemann zeta function and other sequences*, PNAS 116 (2019), 11103–11110.
- Griffin, Ono, Rolen, Thorner, Tripp, Wagner, *Jensen polynomials for the Riemann xi-function*, Advances in Mathematics 397 (2022), 108186.

**Consequence for priority:** proving any fixed finite degree or eventual-in-shift hierarchy is not by itself an RH-level novelty. The finite strip / all-degree-all-shift obstruction is the important distinction.

### 2.6 Wang–Yang (2024): any fixed Laguerre order asymptotically

Larry X.W. Wang and Neil N.Y. Yang, *Laguerre inequalities and complete monotonicity for the Riemann Xi-function and the partition function*, Transactions of the AMS 377 (2024), 4703–4725. DOI: 10.1090/tran/9081.

They prove that for every Laguerre order r there is a constant c such that the Xi coefficients satisfy the order-r Laguerre inequality once

`n > c r^3`.

They also establish asymptotic complete-monotonicity statements.

**Consequence for priority:** “higher rungs eventually hold” is known in several coefficient hierarchies. Branch C's possible novelty must be the exact global monotonicity that makes *its* first rung control *all* later rungs in a sufficient RH link, not mere asymptotic fixed-order positivity.

### 2.7 Dou–Tang–Wang (2025/2026): iterated Laguerre-operator inequality

Li-Mei Dou, Hao Tang, and Larry Wang, *Inequality arising from the iterated Laguerre operator for various partitions*, Proceedings of the Edinburgh Mathematical Society, published online 23 October 2025.

They study the explicit iterated-Laguerre inequality

`(a_(n+1)a_(n+2)-a_n a_(n+3))^2`

`- (a_(n+1)^2-a_n a_(n+2))(a_(n+2)^2-a_n a_(n+4)) > 0`

and prove asymptotic satisfaction for the Riemann Xi coefficients.

**Consequence for priority:** an iterated-rung inequality is not automatically new; the exact Branch C rung and propagation theorem must be distinguished from this hierarchy.

### 2.8 Planat–Solé (2026): second-level Xi-kernel concavity

Michel Planat and Patrick Solé, *Second-Level Concavity of the Riemann Xi Kernel*, arXiv:2608.19160, submitted 19 August 2026.

They prove the Csordas–Dimitrov conjecture

`(log(s'^2-s s''))'' < 0`

for the classical Xi theta kernel.

Their proof is especially close *methodologically* to the current live run:

- exact quartic reduction;
- a polynomial shear of a quadratic cone;
- directed interval certification on a compact interval;
- tail bounds;
- a monotonicity theorem closing the remaining domain.

They explicitly state that their theorem implies the associated double Turán inequalities and **does not assert RH**.

**Consequence for priority:** the pattern “reduce to low-degree algebra + certify a finite interval + use monotonicity to close the tail” is definitely not new in September 2026. Branch C must be claimed at the level of the *link it closes*, not at the level of the method used to close it.

---

## 3. A close 2026 proof-program claim that must be audited, not ignored

A 2026 preprint/program by Eugene Sporyshev, *Riemann Hypothesis. A proof program via moment inequalities and the Turán criterion of Csordas–Varga* (Zenodo DOI reported as 10.5281/zenodo.19359460), claims an RH route based on moment-ratio monotonicity / Q-concavity, a bridge identity, finite Arb certification, and the Csordas–Varga criterion.

The discoverable summary states a bridge of the form

`d rho_k / d lambda = rho_k(lambda) * Delta^2 r_k(lambda)`

and claims an RH close after a finite/analytic split.

This source is not being treated here as established literature authority merely because it claims a proof. It **is** being treated as a serious priority/overlap risk because its architecture — moment inequalities + monotonicity + finite certification + a classical sufficient criterion — is close in spirit to Branch C.

Before a paper-level novelty claim is finalized, the exact Branch C five-link statements should be compared directly against Sporyshev's definitions and theorem dependencies.

---

## 4. What is already known and must not be sold as the novelty

The following are **not** the headline contribution of Branch C:

- strict log-concavity of `Phi(sqrt(t))`;
- ordinary Turán inequalities for the xi coefficients;
- degree-3 / higher-order Turán inequalities;
- second-level Xi-kernel concavity;
- double Turán inequalities;
- fixed-degree eventual Jensen hyperbolicity;
- asymptotic fixed-order Laguerre inequalities;
- generic iterated Laguerre inequalities;
- the substitution `y=pi x^4` and the Gamma(1/4) coordinate for the quartic model;
- use of a quadratic/quartic reduction;
- use of rigorous interval arithmetic;
- use of a monotonicity theorem after a finite certificate.

Those are context, tools, benchmarks, or neighboring theorems.

---

## 5. The statement not found in the literature search

The search was deliberately widened from keyword matching to the actual surrounding theorem families: moment inequalities, Laguerre–Pólya criteria, Jensen hyperbolicity, higher/iterated Laguerre inequalities, theta-kernel concavity, finite-strip obstruction work, and 2026 moment-inequality proof programs.

Within that search, I did **not** find a source proving or formulating the following combined statement:

> There is a five-link sufficient chain to RH such that the third link admits a monotonicity reduction to a single first-rung inequality; that first rung is algebraically quadratic; its sign is separated from zero by a large finite margin; and therefore the entire third link is reduced to one rigorous finite enclosure, leaving exactly four genuinely analytic links.

Nor did I find a source matching the live internal dependency chain

`K172 -> K202 -> K208 -> K210 -> K211`

as a mathematical architecture.

### Current novelty verdict

**The strongest defensible novelty target is the reduction itself.**

Not:

> “a new Turán inequality.”

Not:

> “a new concavity theorem.”

Not:

> “a new quartic/quadratic certificate.”

But:

> **A sufficient RH architecture in which one entire analytic link is reduced to a single finite certification obligation by an exact first-rung reduction and a propagation theorem.**

That is a materially different claim from the closest located literature.

---

## 6. What must be compared as soon as the live nodes are exported

The screenshot/state record is enough to identify the novelty target, but paper-level priority requires the exact formulas. The next export should be mined for these five objects first:

1. **K172 / `epoch_twenty_chain_sealed`** — exact five-link theorem and proof that the five links are sufficient for RH. This is reported `KERNEL_CHECKED`; preserve the formal statement and axiom footprint.
2. **K202 / `dispersion_recasting`** — exact third-link statement after the rejected log-concavity formulation is replaced.
3. **K208 / `first_rung_is_a_quadratic`** — exact quadratic and equivalence proof.
4. **K210 / `first_rung_numbers_settled`** — exact numerical inequality, normalization, interval/tail decomposition, and sign margin.
5. **The monotonicity theorem used by K211** — exact statement showing the first rung controls all higher rungs, not merely the 40 checked rungs.

For each one, run equivalence tests against:

- Csordas–Varga 1988 moment inequalities;
- Csordas–Varga 1990 necessary/sufficient criteria;
- Csordas–Dimitrov double Turán hierarchy;
- Dimitrov–Lucas degree-3 Turán;
- Wang–Yang all-order asymptotic Laguerre inequalities;
- Dou–Tang–Wang iterated Laguerre inequality;
- Planat–Solé second-level kernel concavity;
- Sporyshev's 2026 moment-inequality proof program.

If the exact exported statements survive those equivalence checks, the novelty claim becomes strong rather than merely keyword-distinct.

---

## 7. Release wording

The result should be written around the mathematical reduction, not around the historical agent state.

A suitable headline, assuming the certified enclosure and exact K172/K202/K208 propagation statements survive audit, is:

> **One link in a five-condition sufficient criterion for the Riemann Hypothesis is reduced to a finite certified inequality.**

Then state the theorem chain and the finite inequality explicitly.

Do not headline model names, round numbers, “70% margin,” or internal K/W identifiers. Those belong in provenance.

---

## Bottom line

The deeper novelty check makes the result **more interesting, not less**.

The neighborhood is crowded with strong old and very recent theorems, so there is no novelty in the local ingredients. But that search also sharpens the genuinely distinctive object:

> **the collapse of a whole sufficient RH link from analytic research to finite certification inside a five-link chain.**

No matching theorem or proof architecture was found in the searched literature. That is the object to certify, formalize, compare statement-for-statement, and release.
