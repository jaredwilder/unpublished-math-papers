# Erdős #593 — obligatory 3-uniform hypergraphs

**Author:** Jared Wilder  
**Formal campaign:** 2026-09-05  
**Human extraction:** 2026-09-11

This is the human subject front door for the Lean development previously buried inside `erdos-campaign-archive/campaigns/erdos593-close-2026-09-05/`.

The formal corpus consists of three Lean files plus receipts. The main frontier file is approximately 21 KB and was recorded sorry-free in the campaign build.

## Problem

A finite 3-uniform hypergraph `F` is **obligatory** when it appears in every 3-uniform hypergraph of chromatic cardinal greater than `aleph_0`.

Erdős #593 asks for a characterization of the obligatory finite 3-uniform hypergraphs.

The FormalConjectures file historically recorded the natural guess that obligatory might be equivalent to 2-colourable / Property B. This program formalizes why that characterization is not the correct frontier.

## Exact finite witnesses formalized in Lean

The development defines and proves properties of several explicit finite 3-uniform hypergraphs.

### `C_3^(3)` — expansion of a triangle

Lean proves outright that the 3-uniform triangle expansion is

- 3-partite;
- linear;
- therefore 2-colourable.

Given the published Erdős–Galvin–Hajnal theorem that this hypergraph is non-obligatory, it becomes an explicit counterexample to the proposed sufficiency of Property B.

### `K_4^(3)`

Lean proves outright that the complete 3-uniform hypergraph on four vertices is

- 2-colourable;
- not 3-partite;
- not linear.

Therefore Property B is strictly weaker than either of the two known necessary structural conditions.

## Three independent formal refutations of the proposed sufficiency direction

The Lean file states the literature inputs as explicit hypotheses and proves three separate implications:

1. **Erdős–Galvin–Hajnal input:** if `C_3^(3)` is non-obligatory, then “2-colourable implies obligatory” is false.
2. **Komjáth input:** if obligatory hypergraphs are 3-partite, then the same sufficiency direction is false because `K_4^(3)` is 2-colourable but not 3-partite.
3. **Erdős–Hajnal–Rothschild input:** if obligatory hypergraphs are linear, the sufficiency direction is false because `K_4^(3)` is 2-colourable but not linear.

The corresponding formal theorems are

- `sufficientDirection_false_of_EGH`;
- `sufficientDirection_false_of_Komjath`;
- `sufficientDirection_false_of_EHR`.

The full equivalence recorded as the conjectural FormalConjectures answer is likewise formally refuted from each of those published inputs.

## The necessary direction survives

The program also proves that, **assuming Komjáth's theorem that obligatory 3-uniform hypergraphs are 3-partite**, obligatory implies 2-colourable.

The containment

\[
\text{3-partite}\Longrightarrow\text{2-colourable}
\]

is proved outright in Lean by merging two of the three parts.

Thus the logical state of the old Property-B characterization is asymmetric: the necessary direction follows from the published 3-partite theorem, while the sufficient direction is false.

## Frontier sandwich

The formalized structural picture is

\[
\text{loose forests}
\subseteq
\text{OBLIGATORY}
\subseteq
(\text{linear}\cap\text{3-partite})
\subsetneq
\text{2-colourable}.
\]

The program gives explicit finite witnesses showing that the outer containment into 2-colourable is strict. Given the EGH non-obligatory result for `C_3^(3)`, it also shows that even **linear + 3-partite is not sufficient**.

So the remaining characterization problem genuinely lives inside the middle structural gap rather than at Property B.

## One nondegenerate obligatory example proved outright

The development proves, with no external literature premise, that any 3-uniform hypergraph of uncountable chromatic cardinal has an edge. From this it constructs an embedding of the one-edge 3-uniform hypergraph and obtains

\[
\boxed{\text{a single 3-edge is obligatory}.}
\]

The theorem is `oneEdge_obligatory`.

This is a genuine nondegenerate positive instance proved directly in Lean rather than imported from the literature.

## Formal source

Canonical provenance currently remains in:

```text
jaredwilder/erdos-campaign-archive/
  campaigns/erdos593-close-2026-09-05/
    Erdos593Frontier.lean
    Erdos593Forest.lean
    Erdos593Audit.lean
    receipts/
```

The source deliberately keeps published structural theorems as named hypotheses at the point of use. Kernel checking certifies the finite witness mathematics and logical reductions; it does not convert citations into internally proved literature theorems.

## Repository status

This program is standalone-repository scale: one named open problem, a substantial multi-file Lean development, several explicit finite witness hypergraphs, three independent literature-to-counterexample reductions, a strict frontier sandwich, and a positive obligatory instance proved outright.

Until a dedicated `erdos593` repository shell exists, this directory is the preferred human reading/citation surface and the campaign archive remains the byte-level provenance source.
