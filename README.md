# Public mathematics archive

**Author:** Jared Wilder  
**First public timestamp:** 2026-09-10  
**Release-day expansion:** 2026-09-11

This repository is the **provenance and intake archive** for pure mathematics extracted from a much larger research estate.

It is intentionally broad. It is **not** the permanent canonical home for every subject inside it.

For organization decisions, start with [`SUBJECT-ROUTING.md`](SUBJECT-ROUTING.md). A mathematician looking for a finished result should prefer the focused subject repository when one is listed there; the copy here preserves extraction chronology, historical bytes, and material still awaiting promotion.

## The rule

The release now uses this hierarchy:

> **focused problem/subject repository → compact theorem/records bank → provenance archive**

A problem does not have to be solved before its research program deserves a coherent public home.

This archive should answer “where did this come from?” It should not force readers to learn the entire estate before they can understand one piece of mathematics.

## Repository-scale programs temporarily mirrored here

Several subjects inside this archive are already larger than an intake folder should be.

### Erdős #738 / triangle-free induced-tree frontier

A large theorem/frontier bank with dozens of proved-in-packet statements, explicit targets, recursive data, cross-theorems, a finite verifier and semantic review. A dedicated shell exists at `jaredwilder/erdos738-triangle-free-induced-trees` but currently has no initial commit.

### Erdős–Gyárfás power-of-two cycles

A **202-card** research bank across ten mathematical families, containing proved statements, exact computation, negative theorems, refuted routes and explicit targets.

### Caccetta–Häggkvist

A multi-round directed-triangle program with a 23KB theorem ledger and terminal-defect package covering exact-boundary kernels, escape/bridge/fan structure, fourth-moment machinery and correction history.

### Fiber coherence / cycle rank / rank-three kernel

A **216-record** program across relational coherence, CSP structure, unicyclic/cactus kernels, theta collisions and finite cycle-rank classification. The focused rank-three layer classifies the reduced kernels into `Q4`, `T221`, `D22`, and `K4` and records the associated fixed-rank complexity boundary.

### Erdős #77 / diagonal Ramsey exponential limit

A 23-asset theorem/negative-theorem program around thin off-diagonal corridors, inverse homogeneous-set formulations, tensor/rank identities, polarity/mixer constructions and exact route barriers.

### P6 Erdős–Hajnal

A substantial structural program with 30 theorem assets, crown/defect normal forms, pure-pair statements, candidate/negative banks and bounded exhaustive checks.

### Erdős #142 / progression-free sets

A 53-round audit reconstructing 124 raw records into exact convex-level and mixed-radix constructions, several architecture-specific barriers, a dyadic reciprocal-sum implication and a finite certificate target.

### Erdős #1061 / sigma and aliquot-square solutions

Beyond the compact `(a,2a)` family, the archive contains a primitive-seed generator, ray-scaling theorem, **152,803-seed** exact certificate bank, integer verifier, a second large search and rigorous released lower-bound coefficients.

### Erdős #271 / Stanley sequences and Erdős #500 / Turán (3,4)

The Stanley program has a **184-entry** audited ledger. The Turán program has a **76-record** theorem/finite-target surface. Both are mirrored elsewhere in the estate and are tracked for canonical consolidation.

### Lonely Runner — 13 effective speeds

A late-round theorem bank, terminal normal form, supplements and deeper provenance that now exceed the compact earlier collection in `combinatorial-records`.

### R(5,5) 41-vertex circulant structure

A structural program around the 41-vertex circulant Ramsey graph: affine/multiplier classification, exact graph invariants, automorphisms, one-vertex nonextension, fixed-`k` extension criteria and SAT interface.

## Paper programs

### EG203 / Kummer obstruction program

The canonical paper-series home is `jaredwilder/eg203-kummer-papers`.

Archive material includes recovered analytic-route papers and three formerly anonymous `notes/` TeX sources: the multi-manuscript program roadmap, exact Gamma-fiber local-density note, and a Stepanov auxiliary-polynomial note. These are now indexed from the paper-series repository.

### EG203 V-family sieve draft — audit-first

`sieve-preprint/` is a substantial analytic-number-theory draft, but the release audit found a load-bearing local-density mismatch: the exact triggered density is `1/H_p`, while the draft uses a `1/H_p^2` scale in the thin-sieve argument. Its front-door README records the defect and blocks accidental promotion of the current EG203-closure headline.

### Riemann-zeta research program

`riemann-hypothesis/` contains two distinct lanes: a determinant/total-positivity program ending in a precise open collective-saddle target, and a machine-checked **67.3015452606...%** simple-zero candidate extension whose Arb cross-check remains to be run independently. The directory now has a human root README explaining both lanes.

## Focused subjects that can remain here for now

Not every useful result needs another repository.

Examples:

- `polynomial-dynamics-coordinates/` — a coherent 12-result recurrence/coordinate note;
- `sums-three-cubes-114/` — exact modular/CRT structure for `a^3+b^3+c^3=114`, plus a recorded 15-theorem Lean inventory whose source still needs recovery;
- compact child theorems already routed to `erdos-proved-lemmas`;
- exact finite classifications already routed to `combinatorial-records`.

## Source recovery

Some summaries refer to proof/code/certificate artifacts that are not yet present in the public canonical tree. Those are tracked centrally in:

`jaredwilder/open-math-frontier/SOURCE-RECOVERY-QUEUE.md`.

Current examples include the prime-gap admissibility Lean source, the `k=114` three-cubes Lean module, the full Erdős #1005 Farey packet, and the 17MB Erdős #1061 seed CSV.

A historical source can be missing without the theorem statement being meaningless, but the release should say so explicitly and keep trying to recover the evidence.

## Recently routed to clearer homes

Examples include:

- many compact Erdős child theorems → `jaredwilder/erdos-proved-lemmas`;
- additive/Sidon results (#52, #153, #156, #241) → `jaredwilder/additive-combinatorics-campaigns`;
- rank-2 Chvátal / #701, finite-field classifications, product/GP-free `[50]`, restricted Ramsey-family exhaustions, the conference-switching Ramsey-book theorem and the seven-modulus odd-covering obstruction → `jaredwilder/combinatorial-records`;
- #376 Kummer criterion → `jaredwilder/erdos376-successor-frontier`;
- #503 geometry → `jaredwilder/erdos-lean-remainder`;
- #595 triangle-cover theory → `jaredwilder/erdos595-barrier-tower`;
- #835 SQS(20) theory → `jaredwilder/erdos835-lean-audit`;
- Kirkman/Steiner Lean formalization → `jaredwilder/lean-contributions`;
- EG203 paper program → `jaredwilder/eg203-kummer-papers`.

Archive copies remain public so the release chronology is not rewritten after the fact.

## Evidence and scope

A theorem remains a theorem. A finite computation remains finite. A candidate remains a candidate. A correction affects the claim it corrects rather than poisoning unrelated mathematics around it.

Historical novelty is tracked separately from mathematical correctness.

## Applied-IP boundary

Only pure mathematics is intended for this archive. Mixed biomedical, patent, product, private-data, and proprietary-system material remains outside this release unless separately cleared.

See the publication boundary in `jaredwilder/open-math-frontier`.

## Wider release

- release/navigation hub: `jaredwilder/open-math-frontier`;
- Erdős-facing index: `jaredwilder/erdos-release-index`;
- provenance mine: `jaredwilder/msl-ore-estate`.

## License

Apache-2.0 for repository-authored material unless a file says otherwise. Upstream material retains its own terms.
