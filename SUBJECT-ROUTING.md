# Subject routing for the public mathematics archive

Author: Jared Wilder. Adopted 2026-09-11; refreshed during the release-day topology audit.

This repository is an **archive and intake surface**, not the preferred canonical home for every mathematical subject it contains.

## Routing hierarchy

Use the narrowest coherent public home:

1. **focused problem/subject repository** — preferred once an actively investigated problem has a coherent research surface;
2. **compact theorem or records bank** — appropriate for finished results that are real mathematics but still too small to constitute a research program;
3. **provenance / intake archive** — preserves extraction chronology, historical packets, mixed research notes, and material awaiting routing.

A richer focused repository supersedes the compact bank as the preferred reading surface; the bank may retain a concise theorem statement and link. The intake archive may retain the original extraction copy for provenance.

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

Do **not** create a toy repository for every isolated lemma or compact finite classification. `erdos-proved-lemmas` and `combinatorial-records` exist for those objects until they grow into programs.

## Already routed or consolidated

- 160 formalized Erdős statements → `jaredwilder/erdos152`.
- formal Lean theorem core → `jaredwilder/erdos-theorems/theorems/`; top-level research mirrors in that repository do **not** inherit its 79-declaration kernel-verified label.
- compact proved Erdős child theorems → `jaredwilder/erdos-proved-lemmas`.
- compact exact finite/combinatorial classifications → `jaredwilder/combinatorial-records`.
- Erdős #503 formal/geometry material → `jaredwilder/erdos-lean-remainder`.
- Erdős #376 Kummer carry criterion → `jaredwilder/erdos376-successor-frontier`, beside the 1,006-digit witness it explains.
- Erdős #52 multiplicative-box sumset, #153 Sidon bookkeeping, #156 maximal-Sidon barrier, and #241 triple-sum counting → `jaredwilder/additive-combinatorics-campaigns`.
- rank-2 Chvátal / Erdős #701 theorem → `jaredwilder/combinatorial-records`.
- finite-field classifications `f31-sum-product-avoidance/` and `f73-mixed-avoidance/` → `jaredwilder/combinatorial-records/finite-fields/`.
- `product-gp-free-50/` → `jaredwilder/combinatorial-records/multiplicative/`.
- restricted circulant Ramsey-family eliminations → `jaredwilder/combinatorial-records/ramsey/`.
- Erdős–Straus AP/GP classifications → `jaredwilder/erdos-straus-progressions`.
- integral-octagon bound → `jaredwilder/integral-point-sets`.
- Kreisel–Kurz extension system → `jaredwilder/kreisel-kurz-heptagon-extension`.
- Graham–Alspach sequenceability → the dedicated Graham/Alspach repositories.
- Erdős #902 tournament program → `jaredwilder/erdos902` and `jaredwilder/erdos902-tournament-f4`.
- **Erdős #595** recovered triangle-cover bank → `jaredwilder/erdos595-barrier-tower`; do not create a competing #595 canonical repo merely because another shell exists.
- **Erdős #835** SQS(20) residual completion / rigidity / trade packet → `jaredwilder/erdos835-lean-audit`, now treated as the #835 problem program despite its historical name.
- **EG203 recovered analytic-route papers** → `jaredwilder/eg203-kummer-papers`; archive copies remain provenance.
- compact #243, #247, #289, #885 and similar child theorems → `jaredwilder/erdos-proved-lemmas`, with formal/provenance mirrors retained elsewhere where useful.

## Highest-priority standalone promotions

These are already research programs, not merely folders.

### Tier 1 — initialize/populate as soon as a repository shell is writable

- **Erdős #738 / triangle-free Gyárfás–Sumner** — 62 proved-in-packet statements/schemas, 12 explicit targets, a 45KB human theorem bank, recursive/cross-theorem material, finite verifier and semantic review. A public shell already exists at `jaredwilder/erdos738-triangle-free-induced-trees`, but it currently has no initial commit and cannot yet be populated through the connected Contents API.
- **Erdős–Gyárfás power-of-two cycle conjecture** — 202 theorem cards across ten coherent families: 120 proved-in-packet, 16 computationally certified, 9 proved negative theorems, 9 refuted routes, 34 explicit targets, plus conditional/source-derived material.
- **Caccetta–Häggkvist directed-triangle program** — 23KB theorem ledger plus an 8.5KB terminal-defect package, with exact-boundary work on escape, bridge, fan, matrix/fourth-moment and defect structure, plus proposals and retractions.
- **Fiber coherence / cycle-rank program** — 216 records across nine mathematical layers; the rank-three extraction alone gives 24 theorem/target cards, the four-kernel cycle-rank-three classification, finite K4-free binary-CSP realization, fixed-rank tractability / unbounded-rank NP-completeness, and rank-four next targets. Do not confuse this with the unrelated Roth-function `r_3` in `ck-gold-and-r3-envelope`.
- **Erdős #890 ↔ #1093** — large-prime binomial identity, deficiency/excess bridge, admissible LCM divisor-window reduction, finite deficiency engine and forensic problem history.
- **Erdős #77 / diagonal Ramsey exponential limit** — 23 theorem/negative-theorem assets including thin-corridor equivalence, inverse homogeneous-set formulation, tensor/rank machinery, polarity/mixer constructions and explicit architecture falsifiers. The empty shell `diagonal-ramsey-corridor` is a plausible destination but remains unconfirmed until initialized or source-linked.
- **P6 Erdős–Hajnal** — 30 theorem assets, exact crown/defect/pure-pair structure, negative/candidate companion bank and exhaustive stable-matrix checks through `4×4`.
- **Erdős #142 / progression-free sets** — 124 raw records across 53 rounds; exact convex-level construction, carry-free mixed-radix transfer, several architecture-specific barriers, a dyadic implication to reciprocal sums, a false-route bank and an exact finite certificate target. `ck-gold-and-r3-envelope` is one finite-computation lane, not the canonical home for the full program.

### Tier 2 — strong standalone candidates already visible in intake or formal mirrors

- **Erdős #271 / Stanley sequences** — 184-entry audited theorem/negative ledger and a terminal reduction through reflection support / mean multiplicity.
- **Erdős #500 / Turán (3,4)** — 76-record program with exact finite classifications, structural identities, an equivalence, analytic work and explicit targets; currently duplicated across broad mirrors.
- **Lonely Runner, 13 effective speeds** — late-round theorem bank, terminal normal form, structured supplements and deeper provenance. `combinatorial-records/lonely-runner/` remains a compact earlier home until graduation.
- **Erdős #949 / sum-free finite-sums program** — three exact human theorems plus **33 clean Lean declarations** across core/Hindman/full-finite-sums files.
- **Erdős #1066 / unit-distance independent-set program** — substantial FormalConjectures-style Lean statement/API, many proved local barrier declarations with measured clean axiom footprints, and explicitly separated unfinished/published-input `sorry` statements.
- **R(5,5), 41-vertex circulant structure** — one circulant isomorphism class, exact chromatic/circular/fractional data, automorphism group, one-vertex nonextension and a fixed-`k` extension criterion.
- **polynomial-dynamics-coordinates/** — inspect as a potential standalone recurrence/coordinate program before assigning a permanent home.

Human READMEs have been added to several transitional mirrors so the mathematics is readable before repository migration: #142, #500, #595 coherence/fiber coherence, #738, #77 and P6.

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

Be especially careful with naming collisions. `r_3` can mean the Roth/3-term-AP extremal function in one repository while “rank-three kernel” is a completely different graph/CSP program. Similar notation is not evidence of common subject matter.

## Reader test

A reader should be able to find and follow a coherent body of mathematics without first understanding the history of the whole research estate.

Ask:

> If a mathematician arrived from a citation, would the repository they land in look like it was built for that mathematics?

If not, route it.
