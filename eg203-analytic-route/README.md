# The EG203 analytic route: five papers from a deposit that never happened

These five LaTeX papers sat in a directory named `zenodo-deposits`. Nothing was ever deposited.
They are cited by name inside papers that *were* published, so a reader of those could see the
references and never the documents.

**Author: Jared Wilder.**

Two things were removed from these files before publication, both recorded here rather than
done quietly.

**Model names.** The source carried a language model's name in author lines, section headings,
lemma titles and cross-reference labels. Those were artifacts of the sessions that produced the
files, not authorship. A tool is not an author -- the same is true of the SAT solvers, the Lean
kernel and the exact-arithmetic checkers used throughout this program. The names are gone and the
labels were renamed consistently so every cross-reference still resolves. **No mathematics was
altered.** The internal round identifiers (R676, R682, R691 and the rest) are kept, because those
are this program's own provenance and they say which pass produced or corrected which step.

**Patent methodology references.** Two of the files cited a named patent family and claim number
for the methodology. That family is recorded as **draft, not filed**, so the citation is stripped.
It described process rather than mathematics and nothing in the results depends on it.

---

| paper | lines | state |
|---|---|---|
| `R660B-UNIFORM-PROOF.tex` | 333 | **skeleton**, by its own subtitle |
| `R681-SLICE-JET-STEPANOV.tex` | 323 | **skeleton**, by its own subtitle |
| `R682-GAMMA-FIBER-LOCAL-DENSITY.tex` | **671** | advance; credits a character identity found in an external audit |
| `R705-LATTICE-LARGE-SIEVE-FOR-GAMMA-D.tex` | 270 | attempt at a named gap |
| `R712-PAIRWISE-KUMMER-LARGE-SIEVE-CLOSE.tex` | 254 | attempt at a single open gate |

## What each one is

**R660B — R660B-Uniform Jet-Primitive Stepanov Auxiliary Theorem.** Its subtitle calls it a
**"Skeleton — Phase 30+ FINISH LINE, audit-response v0.1"**. A skeleton is not a finished paper and
it does not pretend to be.

**R681 — Slice-Jet Stepanov Auxiliary for Erdős–Graham #203.** Subtitled
**"Skeleton, Phase 30+ post-R680 corrected"** — a correction pass after R680.

**R682 — Exact Γ-Fiber Local Density and the Kummer-Character Remainder.** The longest at 671
lines. Its title page records that a character identity came out of an external audit pass rather
than absorbing it silently, which is the right way to handle an outside contribution to a step.

**R705 — Lattice Large Sieve for Γ_d = ⟨2,3⟩: Closing Gap G of R704.** An attempt at one named gap
left open by R704.

**R712 — Closing the Pairwise Coefficient-Fiber Kummer Large Sieve.** An attempt at the single open
gate left by R711.

## Why these are published as-is

Two are skeletons and two are attempts at specific gaps. That does not make them worthless and it
does not make them finished mathematics, so they ship with their own labels intact rather than
cleaned up into something that reads more complete than it is.

The Erdős–Graham #203 analytic route these belong to is **not closed**. The finished work on that
problem is in [eg203-kummer-papers](https://github.com/jaredwilder/eg203-kummer-papers) and
[erdos203-obstruction-calculus](https://github.com/jaredwilder/erdos203-obstruction-calculus),
including a paper auditing the routes that failed.
