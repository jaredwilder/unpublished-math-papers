# CLOSE-ANATOMY CAMPAIGN CONTRACT — PTS BOX PROGRAM

Filed under `oracle/doctrine/encirclement-terminal-close/TERMINAL-ADJUDICATION-CONTRACT.md`.
This campaign is CLOSE ANATOMY for the frozen terminal theorem
(`oracle/rh/TCI-PTS-FROZEN.md`). Nothing here can move the finish line;
its products are banked theorems and killed routes.

### CAMPAIGN OBJECTIVE (anatomy objective, not the terminal close)

`O' = a machine-certified box theorem: every real zero of H_t with
      t ∈ [t₀, 0.2], |x| ≤ X(t₀) is simple — which with the published
      tail control forces Λ < t₀, a strict de Bruijn–Newman improvement.`

### CLOSURE CHAIN FOR O', EVERY ARROW MARKED

```
box certificate [t₀,0.2]×[−X,X]                      [MACHINE-CERTIFIED: in progress, small x only]
  -> zeros with |x| > X real+simple for t ≥ t₀       [PUBLISHED for specific (t₀,X) pairs only:
                                                      Polymath15 barrier + RH verification height.
                                                      For NEW t₀ this arrow is [UNPROVED] until a
                                                      barrier-scale computation at X ~ 10^10 exists]
  -> no multiple real zero in (t₀, 0.2]              [follows]
  -> Λ ∉ (t₀, 0.2]                                   [DERIVED: packet claim A, audited 5/5]
  -> Λ < t₀                                          [with PUBLISHED Λ ≤ 0.2]
```

**Honest reading of the chain:** the small-x certificates being produced today
are load-bearing tooling rungs, not yet a Λ improvement. The second arrow is
the expensive one: a new t₀ needs certification out to barrier scale
(x ~ 10¹⁰), which direct quadrature can never reach (see KILLED below) and the
effective-approximation certifier (Attack 4) is being built to reach.

### ATTACK BUDGET

`N = 10` independent mechanisms against O'. Frozen now, before results are
seen. Counted attacks must differ in governing mechanism (doctrine §6).

### ATTACK LEDGER

## Attack 1 / 10 — Direct interval quadrature (small x)

**Mechanism:** midpoint-rule interval enclosure of the oscillatory integral
with rigorous h³/24 remainder; proven series and integral tails.

**Why independent:** direct evaluation of the defining integral; no
asymptotic approximation, no published error bounds consumed.

**Result:** `BANKED THEOREM` + `KILLED (large-x arm)`

- **BANKED (machine-certified, receipt
  `receipts/simple-zero-t0.2-20260811-152935.json`):**
  H_{0.2} has exactly one zero in [28.03361229, 28.27361229] and it is
  simple. Endpoint enclosures ±sign-separated at width 9.4·10⁻⁷; H′ negative
  across all ten sub-brackets. Trust base: mpmath.iv outward rounding +
  module tail inequalities. 72 s.
- **KILLED with evidence (calibration receipts, campaign JSONL):** direct
  quadrature beyond x ≈ 50. Measured edge values fall as the ξ envelope
  e^{−πx/8}: 1.1·10⁻⁵ (x=28) → 3.3·10⁻¹¹ (x=66); required panels grow
  e^{πx/16}: 12.5k → 13.5M across five zeros. An exponential cost curve
  against a fixed target is a wall, not a tuning problem. This kill is
  PERMANENT for the large-x arm; small-x arm remains alive.

**Reopen predicate fired?** NONE (anatomy campaign; kill is banked knowledge).

## Attack 2 / 10 — Calibrated small-x sweep (rescue pass)

**Mechanism:** same integral, per-zero panel counts sized from each zero's own
measured endpoint magnitudes (machine-spoken calibration, not guesses).

**Why independent of Attack 1's kill:** it operates strictly inside the
regime Attack 1 proved viable; it tests how far the small-x arm truly
reaches, which the naive linear scaling mis-sized.

**Result:** `BANKED THEOREM ×2`
- Zero #2 (receipt `simple-zero-t0.2-x41.8934-RESCUE-...json`): H_{0.2} has
  exactly one zero in [41.7734, 42.0134] and it is simple. Values separated
  at the 10⁻⁷ scale. 180k panels, 588 s.
- Zero #3 (receipt `simple-zero-t0.2-x49.9044-RESCUE-...json`): H_{0.2} has
  exactly one zero in [49.7844, 50.0244] and it is simple. Values separated
  at the 10⁻⁸ scale. 700k panels, 1,599 s.
- Calibration law confirmed: edge values fall as the ξ envelope e^{−πx/8};
  the arm is 3-for-3 exactly where the calibration said it reaches.

## Attack 3 / 10 — Uniform-in-t interval certificate (t-box)

**Mechanism:** t enters the enclosure as an interval [0.1, 0.2]; a single
certificate then covers every t in the box simultaneously. This is the exact
shape O' requires in t.

**Why independent:** changes the governing quantifier structure (pointwise-in-t
→ uniform-in-t), not the representation.

**Result:** `KILLED (naive form) -> BANKED THEOREM (heat-equation form)`
- Naive t-interval evaluation: UNDECIDED in 25 s. Measured cost of the t-box
  taken naively: 4.7·10⁻⁵ of enclosure width — 50× the quadrature width,
  swamping the 10⁻⁵ values. The naive form is KILLED with that number.
- The failure receipt exposed the exact repair: for this integral
  ∂H/∂t = −H″ (the heat equation, term by term; the packet's audited
  check_heat_identity). Centred form in t with point-enclosed H″ prices the
  same box at 2.7·10⁻⁶ — 17× cheaper — because H″ near a zero is value-scale,
  not integrand-scale.
- **BANKED THEOREM (receipt `tbox-0.1-0.2-x28.1826-...json`): for EVERY
  t ∈ [0.1, 0.2], H_t has exactly one zero in [28.0626, 28.3026], and it is
  simple.** Uniform endpoint enclosures [+1.6, +7.3]·10⁻⁶ and
  [−7.1, −1.6]·10⁻⁶; uniform H′ hull [−9.8, −7.9]·10⁻⁵, all ten sub-brackets
  negative. 318 s. This is the first certified two-dimensional patch of PTS
  territory: a rectangle in the (t,x) plane containing exactly one simple-zero
  track and no collision point. The box theorem's shape, first instance.

## Prediction ledger (graded, all called before the machine spoke)

| Call | Odds given | Outcome |
|---|---|---|
| Rescue #2 certifies | 90% | CERTIFIED ✓ |
| Rescue #3 certifies | 80% | CERTIFIED ✓ |
| Naive t-box certifies | 15% (against) | UNDECIDED ✓ |
| Heat-equation t-box certifies | 75% | CERTIFIED ✓ |

## Falsification scout (packet tool, not a counted attack)

`direct_collision_scan` 10×100 grid over (0.01–0.2)×(0–100), dps 50:
COMPLETE, zero double-zero candidates. Smallest ‖(H,H′)‖ points are the ξ
envelope noise floor at x≈100 (~10⁻¹⁶), not near-collisions. A finite negative
scan proves nothing about PTS (packet claim ceiling); the measurement it set
out to make, it made.

## Attack 4 / 10 — Effective-approximation certifier (large x)

**Mechanism:** certify via the Polymath 15 Theorem 1.3 representation
(f_t main sum + PUBLISHED explicit error bounds; the packet's
`polymath_main_scan` already exercises the non-rigorous version, and its
`cor1.4_nonzero` flags show the published bounds certifying nonvanishing at
individual points). The derivative analog certifies simplicity where
|f_t′|-type main terms beat their error budgets.

**Why independent:** consumes published effective bounds instead of direct
quadrature; the cost is polynomial in x, not exponential.

**Result:** `NOT STARTED` — this is the load-bearing arm for any new Λ bound.

## Attack 5 / 10 — IBP envelope arm (Sol Round 3)

**Mechanism:** integration by parts, |H^(m)(x)| ≤ J_{m,q}/x^q, to replace the
x-independent crude bounds B_m in the t-ladder.

**Result:** `KILLED BY ARITHMETIC, ZERO LINES BUILT.` The requirement decays
exponentially (ξ envelope, ~10⁻¹⁷ at x=100); IBP supplies polynomial decay,
and J carries full integrand scale: J₅,₂/x² ≈ 10⁻³ at x=50 — WORSE than the
crude B₅ = 2·10⁻⁵ it would replace. Wins only near x~10³, where endpoint
evaluation is unreachable anyway. Usable for coarse region bounds, never for
certificates. The direct engine's true ceiling stands at x ≈ 60.

## Attack 6 / 10 — Corrected Riemann–Siegel engine (Sol Round 10)

**Mechanism:** Polymath Thm 1.3 main term f = S + γ·conj(S) (corrected form)
+ Cauchy disjunction |f|>ε₀ OR |f′|>ε₁ as a large-x transversality
certificate.

**Result so far:** `STRUCTURALLY VALIDATED / CERTIFICATE VIABILITY OPEN.`
- Float cross-validation vs dps-120 quadrature: sign + order agreement
  through **80 orders of magnitude** of decay (x=500: both ~1.4·10⁻⁸²,
  14% apart). The corrected implementation is real.
- **Map correction (measured):** the engines' regimes are DISJOINT. RS wakes
  at N≥2 (x>50), is stated for x≥200; direct dies at x≈60. The planned
  overlap cross-validation zone [30,50] does not exist (N=1 there — the sum
  is the constant 1). No-man's-land: x ∈ (60, 200).
- Open: rel err 14–150% at N ≤ 6; near a zero |f|→0, so certificates at
  x ~ 200–10³ require the rigorous e_A+e_B+e_C budgets to be small vs the
  local main term. Blocked on the published explicit bounds (research agent
  fetching); Polymath's own use was at x~6·10¹⁰ where N~10⁵.

## Rung-4 note (Λ < 0.2 arbitrage)

Platt–Trudgian's Λ ≤ 0.2 consumed the RH-verification height available at
the time; verification has since reached ~3·10¹². Whether re-running their
own pipeline at today's height yields Λ < 0.2 is decidable from their
published parameter dependence BEFORE any compute is spent. Costing in
progress; no claim of any kind until that arithmetic lands.

## Attacks 7–10 — UNSPENT

Candidate mechanisms (must differ in kind, per §6): argument-principle zero
counting on rectangles; Turán-style positivity criteria; heat-flow dynamics
bounds (zero velocity control); Hermite–Biehler/de Branges structure;
adaptive bracket placement at H′ extrema; distributed barrier computation.

### INDEPENDENCE STANDARD

Per doctrine §6. More panels is NOT a new attack (Attack 2 counts only
because the calibration source changed from guess to measurement — if the
adjudicator disagrees, strike it and the budget is 9 remaining, not refilled).

### WHAT THIS CAMPAIGN MAY NEVER DO

- Claim PTS from any finite stack of certificates.
- Call a certificate "progress on RH" without the chain above attached.
- Count a rescout/re-run as an independent attack.
- Weaken the certifier's refusal verdicts to raise the certified count.

### LANGUAGE (doctrine §12)

"Zero #k is certified simple" — allowed, it is a theorem.
"PTS is closer to proved" — forbidden; PTS is UNPROVED until it is proved.
"The anatomy map deepened" — the correct sentence.
