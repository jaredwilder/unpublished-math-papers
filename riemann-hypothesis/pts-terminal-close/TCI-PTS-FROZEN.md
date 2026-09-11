# TCI-PTS — FROZEN TERMINAL CLOSE RECORD

Per `oracle/doctrine/encirclement-terminal-close/ENCIRCLEMENT-TERMINAL-CLOSE-PROTOCOL.md` §10.
Filled from `TERMINAL-ADJUDICATION-CONTRACT.md`.

## ORIGINAL OBJECTIVE

`O = The Riemann Hypothesis.`

## CANDIDATE TERMINAL CLOSE (FROZEN)

> **TCI-PTS:** For every real \(x\) and every \(t\in(0,0.2]\): if \(H_t(x)=0\) then
> \(H_t'(x)\ne0\). (Every real zero of the heat-evolved \(\xi\) flow is simple on
> the interval \((0,0.2]\).)
>
> **Truth status:** UNPROVED
> **Terminality status:** FROZEN
> **Reopen only under:** R1–R5

## CLOSURE CHAIN

```
PTS
  -> [DERIVED, machine-audited 5/5: RH-PROVE-IT-NOW-2026-08-11 verify_close_algebra.py]
     If Λ>0 then H_Λ attains a finite multiple real zero    (claim A; from K1,K4)
  -> [PUBLISHED: Platt–Trudgian arXiv:2004.09765]  Λ ≤ 0.2, so that zero lies in (0,0.2]
  -> PTS forbids it, hence Λ ≤ 0
  -> [PUBLISHED: Rodgers–Tao arXiv:1801.05914]     Λ ≥ 0, hence Λ = 0
  -> [PUBLISHED: de Bruijn–Newman]                 RH ⟺ Λ ≤ 0
  -> O  (RH)
```

No substantive theorem after PTS is `[UNPROVED]`. PTS is terminal for this program.

## STATUS

- `TCR = 5` — TERMINAL CLOSE IDENTIFIED, declared by the originating doctrine session
  (2026-08-11) after the Encirclement-VIII retraction (`CORRECTIONS.md`) survived
  re-audit. Adopted here with the packet's audit reproduced on this machine
  (SHA256 9/9 OK, `verify_close_algebra.py` 5/5 PASS, 2026-08-11).
- Bank card: `oracle/atlas/bank/C_target.jsonl` (PTS, status UNPROVED).
- Known retreat-inadmissible facts: PTS being "equivalent to RH in disguise" is a
  COORDINATE (§10); the t→0⁺ hardness being "where RH really lives" is CLOSE
  ANATOMY (§9). Neither revokes TCR-5.

## FROZEN REOPEN PREDICATES

- [ ] R1 NEW WALL — independent obstruction not implied by PTS
- [ ] R2 BYPASS — route to RH avoiding every equivalent of PTS
- [ ] R3 BROKEN PREMISE — K1/K2/K3/K4 or claim A falsified
      (note: the packet already exercised R3 once, killing VIII_HARDY — banked in
      `D_negative.jsonl`; the terminal chain does not use it)
- [ ] R4 ORPHAN REGION — a regime of (t,x) not governed by the chain
- [ ] R5 NOT SUFFICIENT — a substantive unproved theorem after PTS

None fired as of 2026-08-11.

## POST-TERMINAL CLASSIFICATION OF CURRENT WORK

| Item | Type |
|---|---|
| Interval certifier `oracle/rh/interval_ht.py` | CLOSE ANATOMY (proof strategy) |
| Finite-box simplicity certificates [t₀,0.2]×[−X,X] | CLOSE ANATOMY (sufficient sublemmas; each yields Λ<t₀, a banked theorem, not a revocation) |
| Float scanners (packet) | CLOSE ANATOMY (falsification scouts) |
| A hypothetical found double zero at t∈(0,0.2] | REOPENING STRUCTURE via R3 (breaks K2-consistency of the chain's target: proves Λ≥t>0, resolving O NEGATIVELY) |

**After terminality, the burden of proof belongs to retreat.**
