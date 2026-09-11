# EG203 V-family sieve preprint — audit status and reading guide

**Author:** Jared Wilder  
**Public release:** 2026-09-11  
**Current status:** **substantial preprint under mathematical audit; do not cite it as a proof of Erdős–Graham #203 closure in its present form.**

This directory contains a large analytic-number-theory preprint program around

`V(m,k,l) = m * 2^k * 3^l + 1`, `gcd(m,6)=1`,

including an assembled manuscript and working adversarial/repair memos.

The source set is substantial:

- `wilder-2026-V-family-rosser-iwaniec.tex` — assembled preprint;
- `01-intro-and-kappa.tex` — introduction and sieve-dimension argument;
- `02-kappa-adversarial-and-repair.tex` — working adversarial audit of the sieve-dimension section;
- `03-BV-and-Iwaniec.tex` — level-of-distribution / sieve material;
- `04-BV-Iwaniec-adversarial-and-repair.tex` — working audit of that material;
- `05-almost-prime-and-constants.tex` — singular-series, almost-prime and constants material.

## Blocking mathematical defect found during the release audit

The current manuscript uses the local-density scale

`g_V(p,m) <= 1 / H_p^2`,

where

`H_p = |<2,3> mod p|`.

That bound is incompatible with the exact finite-group counting.

Let

`d_2 = ord_p(2)` and `d_3 = ord_p(3)`.

The map

`phi : Z/d_2 Z x Z/d_3 Z -> <2,3>`,

`phi(k,l) = 2^k 3^l (mod p)`,

is a surjective homomorphism onto a group of size `H_p`. Its domain has size `d_2 d_3`, so every element of the image has exactly

`d_2 d_3 / H_p`

preimages. Therefore, when `-m^(-1)` lies in `<2,3>`, the exact local density is

`g_V(p,m) = 1 / H_p`,

and otherwise it is `0`.

Thus `1/H_p^2` is not a valid pointwise upper bound for triggered primes when `H_p>1`.

The working adversarial memo itself contains both assertions: it discusses the actual triggered density as `1/H_p` while simultaneously relying on `1/H_p^2` as a uniform upper bound. The latter does not follow from the former.

This defect is load-bearing because the claimed thin-sieve / `kappa_V=0` argument is built around the stronger `1/H_p^2` decay.

## Second audit issue: the sieve-dimension constant

The working repair memo defines sieve dimension using an inequality of the form

`sum g(p) log p <= kappa log(z/w) + A`

with an absolute constant `A`, then argues that an `o(log z)` remainder is compatible with `kappa=0` because the implicit constant may depend on `z`.

Under the stated definition, `A` is fixed; it cannot absorb an unbounded `o(log z)` function merely because that function grows sublinearly. This step therefore also requires repair or a different precisely stated sieve-dimension hypothesis.

## Consequence for the headline theorem

The assembled manuscript presently states an effective lower bound for the number of prime values and says Erdős–Graham #203 follows. That headline is **not currently supported by the released proof as written** because the local-density step above must first be repaired and the subsequent sieve argument re-derived with the correct density.

This README does not assert that no corrected proof is possible. It records the exact point that blocks promotion of the current manuscript.

## What remains valuable

The directory should remain public. It contains:

- a serious attempted analytic route;
- explicit adversarial-review memos;
- finite-group structure that can be repaired exactly;
- level-of-distribution and sieve calculations that can be re-examined after correcting the local density;
- empirical data and formal interfaces whose authority should be considered separately from the analytic proof;
- a useful record of where the route succeeds, where it depends on literature, and where the current proof fails.

The correct next mathematical question is not whether the prose can be softened. It is whether a valid sieve argument survives after replacing `1/H_p^2` by the exact triggered density `1/H_p` and imposing a legitimate averaged distribution theorem on the triggered primes.

## Repository topology

This is a **paper-scale research program**, but it should not be promoted into a headline standalone "EG203 solved" repository until the blocking mathematics above is resolved. Keep this directory public as an audit-first preprint/provenance home and route any surviving repaired theorem into the existing EG203 subject repositories with its exact scope.
