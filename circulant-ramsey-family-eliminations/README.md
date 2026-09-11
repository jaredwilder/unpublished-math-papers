# Circulant Ramsey family eliminations

**Author:** Jared Wilder  
**Public estate release:** 2026-09-11

This directory records exact negative results **inside the circulant graph family**. These are restricted-construction theorems, not global Ramsey bounds.

## 1. No order-40 circulant witness for the R(3,10) lower-bound target

The estate's `frontier/ramsey_circulant` lane exhaustively enumerated the inverse-closed connection-set family on 40 vertices for the `R(3,10)` target.

Recorded receipt state:

- `found = false`;
- `exhausted = true`;
- candidates tried: **1,048,575 = 2^20-1**;
- source status: `PROVED / VALID / NOT_TARGETED / EXHAUSTIVE`.

Therefore:

> **There is no circulant two-colouring on 40 vertices witnessing `R(3,10)>40`.**

The source's own boundary line is load-bearing: this says nothing about arbitrary non-circulant graphs and therefore is **not** a lower or upper bound on `R(3,10)`.

The historical receipt was `tasks/bh0kn8wi1.output`; that standalone task artifact has not yet been recovered into the public repository surface.

## 2. No order-36 circulant witness for the R(4,6) lower-bound target

The August-2 mathematical recovery dossier records a second closed family result:

> **No circulant witness on 36 vertices exists for the `R(4,6)>36` construction target.**

The dossier classifies this together with the order-40 result as an **exact family elimination only; not the full Ramsey bound**.

Unlike the `R(3,10)` result above, the low-level standalone enumeration receipt for this `R(4,6)` sweep was not recovered during the current release pass. The result is therefore published with its source-dossier authority and an explicit provenance-recovery obligation rather than a fabricated candidate count or certificate.

## Why these results matter mathematically

Restricted construction families are not monotone proxies for the ambient Ramsey problem. The same estate later exhibited this dramatically for `(5,5)` circulants:

- no witness at 39;
- witnesses at 40 and 41;
- no circulant witness at 42.

So a family-level null must remain a family-level null. Exhaustion is meaningful because it eliminates a concrete algebraic construction class, but it cannot be silently upgraded into an unrestricted Ramsey statement.

## Claim ceiling

This release claims only:

- exact nonexistence in the stated circulant families;
- explicit preservation of the construction-family scope;
- no historical-novelty claim unless separately cleared.

It does **not** claim either ambient Ramsey number is determined.