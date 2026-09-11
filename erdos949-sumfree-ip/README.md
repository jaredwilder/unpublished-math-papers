# Erdős #949 — sharp finite avoidance and IP-set complement theorems

**Author:** Jared Wilder  
**Recovered synthesis:** 2026-09-02  
**Public extraction:** 2026-09-11  
**Pass-2 structural upgrade / formal-receipt promotion:** 2026-09-11

Let `S⊆R` be sum-free: there do not exist `x,y,z∈S` with `x+y=z`.

This note records the exact theorem cluster recovered from the estate. It does **not** solve the continuum-cardinality parent problem.

## Theorem 1 — the sharp finite constant is 5

For every sum-free `S⊆R`, there exists

\[
q\in\{1,2,3,4,5\}
\]

such that

\[
q\notin S,\qquad2q\notin S.
\]

Moreover 5 is best possible.

### Proof

Assume for contradiction that for every `q=1,...,5`, at least one of `q,2q` lies in `S`. Since `S` is sum-free, `1` and `2` cannot both lie in `S`.

**Case 1: `1∈S`.** Then `2∉S`, so `q=2` forces `4∈S`. Since `1+3=4`, `3∉S`, so `q=3` forces `6∈S`. Since `1+4=5`, `5∉S`, so `q=5` forces `10∈S`. But `4+6=10` with all three in `S`, contradiction.

**Case 2: `2∈S`.** Then `4∉S`, so `q=4` forces `8∈S`. Since `2+8=10`, `10∉S`, so `q=5` forces `5∈S`. Since `2+3=5`, `3∉S`, so `q=3` forces `6∈S`. But `2+6=8`, contradiction.

Thus some `q<=5` has both `q` and `2q` outside `S`.

For sharpness, take

\[
S=\{1,4,6\}.
\]

It is sum-free, and for each `q=1,2,3,4`, at least one of `q,2q` lies in `S`. Hence no bound `q<=4` is possible.

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

Color each positive integer by whether it lies in `S`. Hindman's theorem supplies an infinite sequence `x_1,x_2,...` whose finite-sums set `FS(x_i)` is monochromatic.

That monochromatic color cannot be “inside `S`”: if `x_1`, `x_2`, and `x_1+x_2` all lay in `S`, sum-freeness would fail. Hence

\[
FS(x_i)\cap S=\varnothing.
\]

Taking `A={x_i:i>=1}` gives `A⊆N\S`, and every sum of two elements of `A` belongs to the finite-sums set.

## Theorem 3 — simultaneous finite-real-dilate IP avoidance

Let `D⊆R` be finite. Then there is an infinite sequence `x_1,x_2,...∈N` such that

\[
\boxed{d\,FS(x_i)\cap S=\varnothing\qquad\text{for every }d\in D.}
\]

### Proof

Color each `n∈N` by the finite bit vector

\[
c(n)=\bigl(1_S(dn)\bigr)_{d\in D}.
\]

Hindman's theorem gives an infinite sequence whose full finite-sums set is monochromatic for this finite coloring. Fix `d∈D`. If the `d`-coordinate of the common color were 1, then

\[
dx_1,\quad dx_2,\quad d(x_1+x_2)
\]

would all lie in `S`, while

\[
dx_1+dx_2=d(x_1+x_2),
\]

contradicting sum-freeness. Hence every coordinate is 0. If `d=0`, a sum-free set cannot contain 0.

## Theorem 4 — finite-homomorphism IP envelope

The previous theorem is a special case of a more abstract statement recovered in the Pass-2 synthesis.

Let `T` be an additive semigroup, let `S⊆T` be sum-free, and let

\[
\phi_1,\ldots,\phi_m:(\mathbb N,+)\to T
\]

be finitely many additive homomorphisms. Then there is an infinite sequence `x_1,x_2,...` such that

\[
\boxed{
\phi_j(FS(x_i))\cap S=\varnothing
\qquad(1\le j\le m).
}
\]

### Proof

Color `n∈N` by

\[
\bigl(1_S(\phi_1(n)),\ldots,1_S(\phi_m(n))\bigr).
\]

Hindman's theorem produces an infinite finite-sums set on which this finite coloring is constant. If coordinate `j` of the common color were 1, then

\[
\phi_j(x_1),\quad\phi_j(x_2),\quad\phi_j(x_1+x_2)
\]

would all be in `S`. But additivity gives

\[
\phi_j(x_1+x_2)=\phi_j(x_1)+\phi_j(x_2),
\]

contradicting sum-freeness. Therefore every coordinate is 0.

Taking `T=R` and `phi_d(n)=dn` recovers the finite-real-dilate theorem.

## Formal verification receipts

The formal-artifact audit recovered two green Lean files:

### `Erdos949Core.lean`

```text
status=VERIFIED
exitCode=0
seconds=76.5
```

Verified declarations:

```text
erdos949_finite_core
erdos949_universal
erdos949_five_sharp
erdos949_five_sharp_real
```

All were reported clean with the ordinary Mathlib footprint `[propext, Classical.choice, Quot.sound]`, with no `sorryAx`.

### `Erdos949Hindman.lean`

```text
status=VERIFIED
exitCode=0
seconds=71.8
```

Fourteen declarations were verified, including

```text
erdos949_countable_analogue
erdos949_countable_analogue_control
```

with ordinary Mathlib footprints and no `sorryAx`.

The exact receipt ledger is public in `jaredwilder/erdos-theorems/erdos949-sumfree-ip/KERNEL-RECEIPTS.md`. The original standalone `.lean` bytes still need exact source recovery/mirroring; the receipts are published without inventing those missing bytes.

## Novelty boundary

The recovered targeted searches found no exact prior formulation of the countable/IP consequences for Erdős #949 and no indexed match for the sharp `q<=5` lemma. The finite lemma is elementary, so folklore risk remains high. The problem-specific cluster is therefore best described as **candidate / apparently unrecorded after targeted search**, not as a global priority certificate.

The abstract finite-homomorphism envelope has still higher general-folklore risk and is published primarily as the natural mathematical closure of the problem-specific IP argument.

Hindman's theorem itself is classical and imported.

## Scope boundary

- The continuum-cardinality parent problem remains open.
- The finite theorem, countable theorem, real-dilate theorem and homomorphism envelope are separate exact assets.
- The green Lean receipts establish formal verification at their recorded environment; they do not establish historical novelty.

## License

Apache-2.0 for repository-authored material.
