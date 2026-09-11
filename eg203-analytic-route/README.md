# The EG203 analytic route: five papers from a deposit that never happened

These five LaTeX papers sat in a directory named `zenodo-deposits`. Nothing was ever deposited.
They are cited by name inside papers that *were* published, so a reader of those could see the
references and never the documents.

**Author: Jared Wilder.**

Two of the five carried a byline string naming a language model. **That was a session artifact, not
an authorship claim, and it has been corrected.** The tools used in this program include SAT
solvers, the Lean kernel, exact-arithmetic checkers and language models. None of them is an author.

Inside the drafts you will also see internal tags like *"Claude Lemma 9"* and *"GPT R691-R697"* on
individual lemmas. Those are **provenance markers recording which automated pass produced which
step**, the way a lab notebook records which instrument took which measurement. They are left in
place, because removing them would erase the working record and break the documents' own
cross-references.

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
