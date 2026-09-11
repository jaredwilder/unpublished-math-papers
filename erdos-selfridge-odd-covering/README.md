# Erdős–Selfridge odd covering systems — finite certified obstruction

**Author:** Jared Wilder  
**Campaign date:** 2026-07-24  
**Public estate release:** 2026-09-11

## Global problem — still open

The Erdős–Selfridge / Guy B21 question asks whether the integers admit a covering system

`Z = ⋃_i (a_i mod n_i)`

whose moduli `n_i` are all:

- greater than one,
- odd,
- and pairwise distinct.

**No global solution is claimed here.**

The source campaign explicitly warns that inferring “some modulus must be even” from currently known examples would simply restate the open conjecture; it is not a proof.

## Exact finite result

For the fixed seven-modulus family

`{3,5,7,9,11,13,15}`,

there is **no choice of one residue class modulo each modulus** whose union covers every integer.

Equivalently, after reduction modulo

`lcm(3,5,7,9,11,13,15) = 45045`,

no selection

`a_3 mod 3, a_5 mod 5, ..., a_15 mod 15`

covers all `45045` residue classes.

This family is nontrivial from the elementary density viewpoint because

`1/3 + 1/5 + 1/7 + 1/9 + 1/11 + 1/13 + 1/15 ≈ 1.0218004218 > 1`.

Thus the elementary density necessary condition does not rule it out, but the exact residue-incidence constraints do.

## Verification status

The recovered estate state records this fixed-family impossibility as certified independently by **two complete solvers**:

- a CP-SAT formulation;
- a PySAT formulation.

The original standalone solver/certificate files were not recovered in the current Library/public-repo sweep, so this release does not fabricate them. Their recovery is an explicit provenance obligation.

## Elementary density condition

Every finite covering system with distinct moduli must satisfy

`Σ_i 1/n_i >= 1`.

The campaign re-derived this necessary condition as part of its finite search machinery. It is classical and is **not** presented as new mathematics.

## Scope boundary

This result says only that this particular dense seven-modulus candidate is impossible. It does **not** imply that every finite odd distinct-modulus family is impossible, and it does not settle the Erdős–Selfridge conjecture.