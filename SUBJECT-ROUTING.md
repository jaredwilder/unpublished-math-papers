# Subject routing for the public mathematics archive

Author: Jared Wilder. Adopted 2026-09-11.

This repository is an **archive and intake surface**, not the preferred canonical home for every mathematical subject it contains.

## Routing rule

A coherent mathematical object should be promoted out of this archive when any of the following is true:

1. it is a substantial formalization corpus;
2. it contains a theorem family or research program with its own internal structure;
3. it has multiple proofs, certificates, papers, or verification layers;
4. it is likely to be cited or read independently of the rest of the archive;
5. its directory has become large enough that a reader should not have to navigate an unrelated mega-repository to understand it.

The archive may retain a provenance copy after promotion. The subject repository becomes the preferred reading surface.

## Already routed to dedicated repositories

- 160 formalized Erdős statements → `jaredwilder/erdos152`.
- curated Lean theorem bank → `jaredwilder/erdos-theorems`.
- compact proved Erdős child theorems → `jaredwilder/erdos-proved-lemmas`.
- Erdős #503 formal/geometry material → `jaredwilder/erdos-lean-remainder`.
- Erdős #52 multiplicative-box sumset theorem → `jaredwilder/additive-combinatorics-campaigns`.
- rank-2 Chvátal / Erdős #701 theorem → `jaredwilder/combinatorial-records`.
- Erdős–Straus AP/GP classifications → `jaredwilder/erdos-straus-progressions`.
- integral-octagon bound → `jaredwilder/integral-point-sets`.
- Kreisel–Kurz extension system → `jaredwilder/kreisel-kurz-heptagon-extension`.
- Graham–Alspach sequenceability → the three dedicated Graham/Alspach repositories.
- EG203/Kummer papers and obstruction calculus → dedicated EG203 repositories.
- Erdős #902 tournament program → `jaredwilder/erdos902` and the focused `erdos902-tournament-f4` repository.
- Erdős #595 formal barrier theorem → `jaredwilder/erdos595-barrier-tower`.

## Strong candidates for their own repository

These archive subjects are already large/coherent enough that they should not remain archive-only once repository creation is available:

- `erdos271-stanley/` — 184-entry audited Stanley-sequence theorem/negative ledger;
- `erdos500-turan34/` — 76-entry Erdős #500 / Turán (3,4) theorem extraction;
- `erdos738-theorem-bank/` — 62 proved statements/schemas plus 12 explicit open targets;
- `lonely-runner-13/` — 13-effective-speed Lonely Runner theorem bank and research record;
- `fiber-coherence-theorem-bank/` + `rank-three-kernel/` — coherent graph/CSP structural program;
- `ramsey-r55-circulant-structure/` — standalone structural/certificate program for the 41-vertex circulant `(5,5)` Ramsey graph;
- `riemann-hypothesis/` — distinct analytic-number-theory program, including the separately scoped simple-zero candidate;
- `polynomial-dynamics-coordinates/` — standalone recurrence/coordinate mathematics;
- `product-gp-free-50/` — exact finite extremal classification with 240 extremizers;
- `f31-sum-product-avoidance/` and `f73-mixed-avoidance/` — sharp finite-field classification programs.

## Archive-only material

A directory may remain archive-only when it is chiefly:

- a historical research record;
- a small one-off note that fits an existing canonical subject repository;
- a provenance mirror of material already promoted elsewhere;
- a mixed bundle awaiting extraction or literature review.

## Editorial rule

Promotion is not a claim of novelty or importance. It is information architecture.

A reader should be able to find a coherent body of mathematics without first understanding the history of the whole research estate.
