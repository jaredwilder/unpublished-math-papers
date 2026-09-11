# Erdős #949 — sharp finite avoidance and IP-set complement theorems

**Author:** Jared Wilder  
**Recovered synthesis:** 2026-09-02  
**Public extraction:** 2026-09-11

Let `S ⊆ R` be sum-free: there do not exist `x,y,z ∈ S` with `x+y=z`.

This note records three exact partial results recovered from the estate. They do **not** solve the
continuum-cardinality parent problem.

## Theorem 1 — the sharp finite constant is 5

For every sum-free `S ⊆ R`, there exists

\[
q\in\{1,2,3,4,5\}
\]

such that

\[
q\notin S,\qquad 2q\notin S.
\]

Moreover 5 is best possible.

### Proof

Assume for contradiction that for every `q=1,...,5`, at least one of `q,2q` lies in `S`.
Since `S` is sum-free, `1` and `2` cannot both lie in `S`.

**Case 1: `1∈S`.** Then `2∉S`, so the `q=2` condition forces `4∈S`. Since `1+3=4`, we have
`3∉S`, so `q=3` forces `6∈S`. Since `1+4=5`, we have `5∉S`, so `q=5` forces `10∈S`.
But now `4,6,10∈S` and `4+6=10`, contradiction.

**Case 2: `2∈S`.** Then `4∉S`, so `q=4` forces `8∈S`. Since `2+8=10`, we have `10∉S`, so
`q=5` forces `5∈S`. Since `2+3=5`, we have `3∉S`, so `q=3` forces `6∈S`. But now
`2,6,8∈S` and `2+6=8`, contradiction.

Thus some `q≤5` has both `q` and `2q` outside `S`.

For sharpness, take

\[
S=\{1,4,6\}.
\]

It is sum-free, and for each `q=1,2,3,4`, at least one of `q,2q` lies in `S`. Hence no bound
`q≤4` is possible.

## Theorem 2 — complete countable analogue

Every sum-free `S⊆R` admits a countably infinite set

\[
A\subseteq\mathbb N\setminus S
\]

such that

\[
A+A\subseteq\mathbb R\setminus S.
\]

### Proof from Hindman's theorem

Color each positive integer by whether it lies in `S`. Hindman's theorem supplies an infinite
sequence `x_1,x_2,...` whose finite-sums set `FS(x_i)` is monochromatic.

That monochromatic color cannot be "inside `S`": if `x_1`, `x_2`, and `x_1+x_2` all lay in `S`,
sum-freeness would fail. Hence

\[
FS(x_i)\cap S=\varnothing.
\]

Taking `A={x_i:i≥1}` gives `A⊆N\S`, and every sum of two elements of `A` belongs to the finite-sums
set, so `A+A⊆R\S`.

This isolates the unresolved part of the parent problem at the jump from countable size to the
continuum, rather than at the existence of large structured complements in general.

## Theorem 3 — simultaneous finite-real-dilate IP avoidance

Let `D⊆R` be finite. Then there is an infinite sequence `x_1,x_2,...∈N` such that

\[
\boxed{d\,FS(x_i)\cap S=\varnothing\qquad\text{for every }d\in D.}
\]

Equivalently,

\[
D\cdot FS(X)\subseteq\mathbb R\setminus S.
\]

### Proof

Color each `n∈N` by the finite bit vector

\[
c(n)=\bigl(1_S(dn)\bigr)_{d\in D}.
\]

Hindman's theorem gives an infinite sequence whose full finite-sums set is monochromatic for this
finite coloring. Fix `d∈D`. If the `d`-coordinate of the common color were 1, then

\[
dx_1,\quad dx_2,\quad d(x_1+x_2)
\]

would all lie in `S`, while

\[
dx_1+dx_2=d(x_1+x_2),
\]

contradicting sum-freeness. Hence every coordinate is 0. If `d=0`, note that a sum-free set cannot
contain 0.

The same proof packages more abstractly for a finite family of additive homomorphisms into an
additive semigroup; this note keeps the real-dilate form because it is the problem-specific result.

## Novelty boundary

The recovered targeted searches found no exact prior formulation of the countable/IP consequences
for Erdős #949, and no indexed match for the sharp `q≤5` lemma. The finite lemma is elementary, so
folklore risk remains high. The correct wording is **candidate / apparently unrecorded after
targeted search**, not a priority certificate.

Hindman's theorem itself is classical and is used as an external theorem; the candidate novelty is
its problem-specific consequence and the simultaneous-dilate formulation.

## Scope boundary

- The continuum-cardinality parent problem remains open.
- The finite theorem, countable theorem, and IP theorem are separate exact assets.
- No claim here depends on a computational search for mathematical truth.

## License

Apache-2.0 for repository-authored material.
