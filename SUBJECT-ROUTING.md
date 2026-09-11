# Subject routing for the public mathematics archive

Author: Jared Wilder. Adopted 2026-09-11.

This repository is an **archive and intake surface**, not the preferred canonical home for every mathematical subject it contains.

## Routing hierarchy

Use the narrowest coherent public home:

1. **focused problem/subject repository** — preferred once an actively investigated problem has a coherent research surface;
2. **compact theorem bank** — appropriate for finished child theorems that are real results but still too small to constitute a research program;
3. **provenance / intake archive** — preserves extraction chronology, historical packets, mixed research notes, and material awaiting routing.

A richer focused repository supersedes the compact theorem bank as the preferred reading surface; the bank may retain a concise theorem statement and link. The intake archive may retain the original extraction copy for provenance.

## Generous promotion rule

Bias toward a dedicated problem home when **any one** of the following is present:

- multiple nontrivial results or a dependency chain;
- a substantial formalization corpus;
- dedicated computation, witnesses, certificates, or exact search code;
- a live research frontier with explicit obligations;
- a meaningful correction/refutation history;
- a paper or paper series;
- enough material that a mathematician could reasonably follow the problem as a program.

The parent problem does not have to be solved. Open-problem research deserves a coherent home too.

Do **not** create a toy repository for every isolated lemma. `erdos-proved-lemmas` exists for compact finished child theorems until they grow into a program.

## Already routed or consolidated

- 160 formalized Erdős statements → `jaredwilder/erdos152`.
- curated Lean theorem bank → `jaredwilder/erdos-theorems`.
- compact proved Erdős child theorems → `jaredwilder/erdos-proved-lemmas`.
- Erdős #503 formal/geometry material → `jaredwilder/erdos-lean-remainder`.
- Erdős #376 Kummer carry criterion → `jaredwilder/erdos376-successor-frontier`, beside the 1,006-digit witness it explains.
- Erdős #52 multiplicative-box sumset, #153 Sidon bookkeeping, and #241 triple-sum counting → `jaredwilder/additive-combinatorics-campaigns` as the richer subject home.
- rank-2 Chvátal / Erdős #701 theorem → `jaredwilder/combinatorial-records`.
- Erdős–Straus AP/GP classifications → `jaredwilder/erdos-straus-progressions`.
- integral-octagon bound → `jaredwilder/integral-point-sets`.
- Kreisel–Kurz extension system → `jaredwilder/kreisel-kurz-heptagon-extension`.
- Graham–Alspach sequenceability → the dedicated Graham/Alspach repositories.
- Erdős #902 tournament program → `jaredwilder/erdos902` and the focused `erdos902-tournament-f4` repository.
- **Erdős #595** recovered 65-card triangle-cover theorem bank → promoted into `jaredwilder/erdos595-barrier-tower`; do not create a competing canonical #595 repo merely because another empty shell exists.
- **Erdős #835** SQS(20) residual completion / rigidity / trade packet → promoted into `jaredwilder/erdos835-lean-audit`, whose front door now treats the repository as the #835 problem program rather than only a Lean audit.
- **EG203 recovered analytic-route papers** → indexed from `jaredwilder/eg203-kummer-papers`; the source files remain in this archive as historical/provenance copies rather than creating another #203 silo.

## Highest-priority standalone promotions

These are already research programs, not merely folders.

### Tier 1 — initialize/populate as soon as a repository shell is writable

- **Erdős #738 / triangle-free Gyárfás–Sumner** — `erdos738-theorem-bank/`: 62 proved-in-packet statements/schemas, 12 explicit targets, 45,301-byte human theorem bank, finite verifier and manifests. A public shell already exists at `jaredwilder/erdos738-triangle-free-induced-trees`, but it currently has no initial commit and cannot yet be populated through the connected Contents API.
- **Erdős–Gyárfás power-of-two cycle conjecture** — `erdos-gyarfas-power-cycle/`: 202 theorem cards across ten coherent families: 120 proved-in-packet, 16 computationally certified, 9 proved negative theorems, 9 refuted routes, 34 explicit targets, plus conditional/source-derived material. This plainly exceeds theorem-bank scale.
- **Caccetta–Häggkvist directed-triangle program** — `caccetta-haggkvist/`: 23KB theorem ledger plus an 8.5KB terminal-defect package, with a long exact-boundary program covering escape, bridge, fan, matrix/fourth-moment and defect structure, plus proposals and retractions.
- **Erdős #890 ↔ #1093** — large-prime binomial identity, deficiency/excess bridge, admissible LCM divisor-window reduction, finite deficiency engine and forensic problem history. Temporary summary remains in `erdos-proved-lemmas` until a dedicated home is initialized.

### Tier 2 — strong standalone candidates already visible in intake

- `erdos271-stanley/` — 184-entry audited Stanley-sequence theorem/negative ledger;
- `erdos500-turan34/` — 76-entry Erdős #500 / Turán (3,4) extraction;
- `lonely-runner-13/` — 13-effective-speed Lonely Runner theorem bank and research record;
- `fiber-coherence-theorem-bank/` + `rank-three-kernel/` — coherent graph/CSP structural program;
- `ramsey-r55-circulant-structure/` — structural/certificate program for the 41-vertex circulant `(5,5)` Ramsey graph;
- `polynomial-dynamics-coordinates/` — recurrence/coordinate mathematics;
- `product-gp-free-50/` — exact finite extremal classification with 240 extremizers;
- `f31-sum-product-avoidance/` and `f73-mixed-avoidance/` — sharp finite-field classification programs.

### Audit-first candidates

Some archive folders are clearly large enough for a standalone home but should **not be amplified before claim-quality review**. `riemann-hypothesis/` is the clearest example: size alone is not a reason to elevate an unaudited high-stakes claim surface.

## Archive-only material

A directory may remain archive-only when it is chiefly:

- a historical research record;
- a small one-off note that fits an existing canonical subject repository;
- a provenance mirror of material already promoted elsewhere;
- a mixed bundle awaiting extraction or literature review;
- process/tooling debris whose mathematical outputs have already been routed elsewhere.

## Anti-fragmentation rule

The generous promotion threshold does not mean “one new repository per folder.”

If the same problem already has a substantial dedicated repository, enrich it. Organize primarily by **mathematical problem/program**, not by which proof technology, model, session, or extraction pass generated the artifact.

## Reader test

A reader should be able to find and follow a coherent body of mathematics without first understanding the history of the whole research estate.

Ask:

> If a mathematician arrived from a citation, would the repository they land in look like it was built for that mathematics?

If not, route it.
