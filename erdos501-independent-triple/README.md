# Erdős #501 — repaired finite independent-triple lemma

**Author:** Jared Wilder  
**Recovered from:** September 2026 proof-repair audit  
**Public extraction:** 2026-09-11

## Finite theorem

Let `V` be an `N`-element vertex set. Suppose each vertex has a directed forbidden row containing at
most `m` vertices. Declare an unordered pair bad when at least one orientation of that pair is
forbidden.

If

\[
\boxed{6m<N-1,}
\]

then there exist three vertices containing no bad pair: an independent triple.

## Correct proof

The total number of directed forbidden incidences is at most `mN`. Every bad unordered pair accounts
for at least one such directed incidence, so

\[
\#\{\text{bad unordered pairs}\}\le mN.
\]

A fixed bad pair lies in at most `N-2` unordered triples. Therefore the number of triples
contaminated by at least one bad pair is at most

\[
mN(N-2).
\]

Under `6m<N-1`,

\[
mN(N-2)
<
\frac{N(N-1)(N-2)}6
=
\binom N3.
\]

So not every triple is contaminated. At least one triple contains no bad pair.

## Repair record

The raw proof used an unjustified factor-of-two improvement in the bad-pair count. The repaired
argument above uses only the safe bound

\[
\#\text{bad pairs}\le mN,
\]

which is already enough for the stated threshold.

## Scope boundary

This is a finite theorem. The source campaign's larger continuum target requires an additional
finite-to-continuum transfer that is **not** supplied by this lemma. The September audit explicitly
keeps those scopes separate.

No historical novelty claim is made; this is published as a corrected exact lemma and as a proof-
repair record.

## License

Apache-2.0 for repository-authored material.
