# PTS / de Bruijn–Newman interval-certifier program

**Author:** Jared Wilder  
**Campaign date:** 2026-08-11  
**Public extraction:** 2026-09-11

This directory recovers a third Riemann-zeta research lane that existed internally but was absent from the public RH front door.

The target is the following positive-time simplicity statement for the de Bruijn–Newman heat flow:

> **PTS.** For every real `x` and every `t in (0, 0.2]`, if `H_t(x)=0`, then `H_t'(x) != 0`.

The internal campaign treats PTS as a **terminal sufficient theorem** for its RH route. PTS itself is **unproved**. Nothing in this directory is an announcement of a proof of RH.

## What is recovered here

This public extraction contains:

- `TCI-PTS-FROZEN.md` — the frozen target and closure-chain record;
- `ANATOMY-CAMPAIGN-CONTRACT.md` — the ten-mechanism attack ledger and exact claim ceilings;
- `interval_ht.py` — the interval-arithmetic certifier used for the small-`x` program.

The certifier uses `mpmath.iv` outward-rounded interval arithmetic together with explicit quadrature and tail bounds encoded in the source.

## Independent rerun performed during extraction

On 2026-09-11 the recovered `interval_ht.py` was executed from the exported bytes with

```bash
python interval_ht.py --selftest
```

and returned all eight built-in gates as `OK`, ending with:

```text
Selftest: ALL OK
```

Those gates check containment for derivative orders 0, 1 and 2, refinement narrowing, overlap of refinements, the expected `h^2` convergence ratio, refusal of a bracket without a certified sign change, and a sanity bound for the third-derivative envelope.

## Claim ceiling of this extraction

The internal campaign records three point certificates at `t=0.2` and three uniform `t`-box certificates over `t in [0.1,0.2]`. Those claims are described in `ANATOMY-CAMPAIGN-CONTRACT.md`.

However, the session export used for this public recovery did **not** carry all 23 original receipt JSON files as named public artifacts. The full `--certify-tbox` rerun also exceeds the short extraction-time execution window used for this pass.

Therefore this directory currently establishes:

1. the exact target and campaign provenance;
2. the certifier source code;
3. a fresh successful rerun of its built-in self-test;
4. the historical certificate claims exactly as recorded by the source campaign.

It does **not** present the missing receipt bundle as independently reproduced evidence. A future complete packet should add those original receipt JSONs or regenerate them from the certifier.

## Why the lane matters

The program is not a pile of finite zero checks. Its mathematical object is the collision question for the heat-evolved xi flow. The finite certificates are local territory inside that program; the global target remains PTS.

The campaign itself also identifies the practical wall: direct interval quadrature becomes exponentially expensive with `x`, so any global attack requires a different large-`x` representation rather than simply adding panels.

## Reading rule

Cite the exact level of evidence:

- **target theorem:** PTS, unproved;
- **certifier method:** executable source recovered here;
- **self-test:** freshly rerun, 8/8;
- **historical point / t-box certificates:** recorded by the internal campaign, full receipt bundle not yet recovered into this public directory.

That is enough to make the program visible without inflating finite certified territory into a global theorem.
