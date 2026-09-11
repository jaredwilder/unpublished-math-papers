# Subject routing for the public mathematics archive

Author: Jared Wilder. Adopted 2026-09-11; refreshed during the live release topology audit.

This repository is an **archive and intake surface**, not the preferred canonical home for every mathematical subject it contains.

## Routing hierarchy

Use the narrowest coherent public home:

1. **focused problem/subject repository** — preferred once an actively investigated problem has a coherent research surface;
2. **compact theorem or records bank** — for finished results that are real mathematics but still too small to constitute a research program;
3. **provenance / intake archive** — preserves extraction chronology, historical packets, mixed notes and material awaiting routing.

A richer focused repository supersedes a compact bank as the preferred reading surface. The bank and archive may retain concise mirrors/provenance links.

## When a problem deserves its own repository

Bias toward a dedicated problem home when any one of the following is present:

- multiple nontrivial results or a dependency chain;
- a substantial formalization corpus;
- dedicated computation, witnesses, certificates or exact search code;
- a live research frontier with explicit obligations;
- a meaningful correction/refutation history;
- a paper or paper series;
- enough material that a mathematician could reasonably follow the problem as a program.

The parent problem does not need to be solved.

Do **not** create a toy repository for every isolated lemma or compact finite classification. `erdos-proved-lemmas` and `combinatorial-records` are the intended compact homes.

## Already routed / consolidated

- 160 formalized Erdős statements → `jaredwilder/erdos152`.
- Lean theorem core → `jaredwilder/erdos-theorems/theorems/`; top-level research mirrors there do not inherit the 79-declaration kernel-verified label.
- compact proved Erdős child theorems → `jaredwilder/erdos-proved-lemmas`.
- compact exact finite/combinatorial classifications → `jaredwilder/combinatorial-records`.
- #503 geometry → `jaredwilder/erdos-lean-remainder`.
- #376 Kummer criterion → `jaredwilder/erdos376-successor-frontier`.
- #52, #153, #156 and #241 additive/Sidon results → `jaredwilder/additive-combinatorics-campaigns`.
- rank-2 Chvátal / #701 → `jaredwilder/combinatorial-records`.
- F31/F73 finite-field classifications, product-GP-free `[50]`, and restricted circulant Ramsey exhaustions → `jaredwilder/combinatorial-records`.
- conference-switching Ramsey-book construction-class theorem → `jaredwilder/combinatorial-records/ramsey/`.
- Erdős–Selfridge seven-modulus odd-covering obstruction → `jaredwilder/combinatorial-records/covering-systems/`.
- Erdős–Straus AP/GP classifications → `jaredwilder/erdos-straus-progressions`.
- integral-octagon bound → `jaredwilder/integral-point-sets`.
- Kreisel–Kurz extension → `jaredwilder/kreisel-kurz-heptagon-extension`.
- Graham–Alspach program → dedicated Graham/Alspach repositories.
- #902 tournament program → `jaredwilder/erdos902` and `jaredwilder/erdos902-tournament-f4`.
- #595 triangle-cover bank → `jaredwilder/erdos595-barrier-tower`.
- #835 SQS(20) completion/rigidity/trades → `jaredwilder/erdos835-lean-audit`.
- EG203 paper program, recovered analytic route, and formerly anonymous technical notes → `jaredwilder/eg203-kummer-papers`.
- compact #243, #247, #289, #885 and similar results → `jaredwilder/erdos-proved-lemmas`.
- Kirkman/Steiner Lean formalization → `jaredwilder/lean-contributions`; `kirkman-steiner-lean/` here is provenance only.

## Repository-scale programs awaiting focused homes

### Highest priority

- **#738 / triangle-free induced trees** — large theorem/frontier bank, verifier, semantic review; zero-commit shell already exists at `jaredwilder/erdos738-triangle-free-induced-trees`.
- **Erdős–Gyárfás power-of-two cycles** — 202 theorem cards across ten families.
- **Caccetta–Häggkvist** — multi-round theorem ledger + terminal-defect package.
- **fiber coherence / cycle rank / rank-three kernel** — 216-record program; rank-three four-kernel classification and CSP complexity layer.
- **#890 ↔ #1093** — bridge theorem, divisor-window reduction, deficiency engine and forensic history.
- **#77 diagonal Ramsey limit** — 23 theorem/negative-theorem assets; empty `diagonal-ramsey-corridor` shell is a plausible but not yet confirmed destination.
- **P6 Erdős–Hajnal** — 30 theorem assets, local normal forms, pure-pair theorem and finite regression checks.
- **#142 progression-free sets** — 124-record / 53-round audited construction/barrier program.
- **#1061 sigma / aliquot-square** — infinite family, primitive-seed generator, ray scaling, 152,803-seed certificate bank, verifiers and stronger lower-bound coefficient work.

### Strong standalone candidates

- **#271 Stanley sequences** — 184-entry audited ledger.
- **#500 Turán (3,4)** — 76-record theorem/finite-target program.
- **Lonely Runner, 13 effective speeds** — late-round theorem bank / terminal normal form / supplements.
- **#949 finite-sums avoidance** — multiple human theorems + 33 clean Lean declarations.
- **#1066 unit-distance independent-set program** — substantial FormalConjectures-style module + proved barrier/API layer + explicit unfinished obligations.
- **R(5,5) 41-vertex circulant structure** — classification, exact invariants, nonextension and SAT interface.

Human entry READMEs now exist for several transitional broad-repo mirrors so mathematics is readable before migration.

## Provenance-blocked programs

- **#1005 Farey** — coherent reductions and period-36 structure survive, but the full source packet is missing and one key formula is truncated. Recover source before promotion.
- **prime-gap admissibility** — multi-module Lean program is described, but the original `.lean` tree is not public and the historical theorem/module counts disagree. Recover and recount before formal-corpus promotion.

See `jaredwilder/open-math-frontier/SOURCE-RECOVERY-QUEUE.md` for exact recovery obligations.

## Audit-first programs

- **`sieve-preprint/`** — paper-scale EG203 analytic route. Release audit found a load-bearing local-density mismatch (`1/H_p` exact triggered density versus `1/H_p^2` used in the draft) plus a sieve-dimension constant issue. Keep public as an audit-first preprint; do not promote the current closure headline.
- **`riemann-hypothesis/`** — coherent zeta-function program with a determinant frontier and a machine-checked 67.301545...% simple-zero candidate extension. Human root README exists; candidate lane still needs the Arb rerun / independent reproduction before stronger promotion.

## Focused archive subjects that do not yet need another repository

- `polynomial-dynamics-coordinates/` — coherent 12-result recurrence/coordinate note, but no larger formal/computational program yet.
- `sums-three-cubes-114/` — exact modular/CRT arithmetic and recorded 15-theorem Lean inventory; keep focused until the missing Lean source is recovered or the program grows.
- isolated compact theorem folders already represented in `erdos-proved-lemmas` or `combinatorial-records`.

## Anti-fragmentation rule

The generous promotion threshold does **not** mean “one new repository per folder.”

If the same problem already has a substantial dedicated repository, enrich it. Organize primarily by **mathematical problem/program**, not by model, proof technology, session, verifier, or extraction pass.

Be especially careful with naming collisions. `r_3` can mean the Roth/3-AP extremal function while “rank-three kernel” is a completely different graph/CSP program.

## Reader test

Ask:

> If a mathematician arrived from a citation, would the repository they land in look like it was built for that mathematics?

If not, route it.
