# Subject routing for the public mathematics archive

Author: Jared Wilder. Adopted 2026-09-11.

This repository is an **archive and intake surface**, not the preferred canonical home for every mathematical subject it contains.

## Routing hierarchy

Use the narrowest coherent public home:

1. **focused subject repository** — preferred when a theorem family, formalization corpus, paper program, or sustained research object has its own identity;
2. **compact theorem bank** — appropriate for finished child theorems that are substantial enough to publish but not yet large enough for a dedicated repository;
3. **provenance / intake archive** — preserves extraction chronology, historical packets, mixed research notes, and material awaiting routing.

A richer focused subject repository supersedes the compact theorem bank as the preferred reading surface; the bank may retain a concise theorem statement and link. The intake archive may retain the original extraction copy for provenance.

## When to promote a subject

A coherent mathematical object should be promoted out of this archive when any of the following is true:

1. it is a substantial formalization corpus;
2. it contains a theorem family or research program with its own internal structure;
3. it has multiple proofs, certificates, papers, or verification layers;
4. it is likely to be cited or read independently of the rest of the archive;
5. its directory has become large enough that a reader should not have to navigate an unrelated mega-repository to understand it.

Promotion is information architecture, not a claim of novelty or importance.

## Already routed

- 160 formalized Erdős statements → `jaredwilder/erdos152`.
- curated Lean theorem bank → `jaredwilder/erdos-theorems`.
- compact proved Erdős child theorems → `jaredwilder/erdos-proved-lemmas`.
- Erdős #503 formal/geometry material → `jaredwilder/erdos-lean-remainder`.
- Erdős #52 multiplicative-box sumset theorem → `jaredwilder/additive-combinatorics-campaigns` as the richer subject home; a compact theorem entry may also appear in `erdos-proved-lemmas`.
- rank-2 Chvátal / Erdős #701 theorem → `jaredwilder/combinatorial-records`.
- Erdős–Straus AP/GP classifications → `jaredwilder/erdos-straus-progressions`.
- integral-octagon bound → `jaredwilder/integral-point-sets`.
- Kreisel–Kurz extension system → `jaredwilder/kreisel-kurz-heptagon-extension`.
- Graham–Alspach sequenceability → the three dedicated Graham/Alspach repositories.
- EG203/Kummer papers and obstruction calculus → dedicated EG203 repositories.
- Erdős #902 tournament program → `jaredwilder/erdos902` and the focused `erdos902-tournament-f4` repository.
- Erdős #595 formal barrier theorem → `jaredwilder/erdos595-barrier-tower`.

## Strong candidates for their own repository

These subjects are already large/coherent enough that they should not remain archive-only once repository creation is available:

- **Erdős #890 ↔ #1093** — large-prime binomial identity, deficiency/excess bridge, admissible LCM divisor-window reduction, finite deficiency engine, and a substantial forensic problem history. Temporary compact theorem surface: `jaredwilder/erdos-proved-lemmas/erdos890-1093-bridge.md`;
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

A reader should be able to find a coherent body of mathematics without first understanding the history of the whole research estate.

Do not create duplicate competing canonical homes. Indices and theorem banks should point toward the richer subject repository when one exists.
