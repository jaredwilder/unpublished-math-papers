# Verification audit

The mathematical claim is computer-assisted, so the verification story is part of the theorem.

## Producer

The original closure program enumerated a finite set of integer distance-difference cells. For a chosen base vertex `P_b`, every candidate extension `X` determines integers

`c_j = |XP_b|-|XP_j|`

with `|c_j|<=d(P_b,P_j)` by the triangle inequality. This removes any need for a coordinate/height cutoff. Each admissible cell was reduced to exact algebraic equations.

Recorded producer sweeps:

| configuration | cells | role |
|---|---:|---|
| H1 | 136,801,313 | exact sweep, base triple 1 |
| H1 | 205,982,337 | exact sweep, independent base triple |
| H2 | 1,335,425,575 | exact sweep |

Each producer sweep recovered the known vertices and found no nontrivial extension.

## Why that was not enough

Running the same code with different base triples is useful but is still self-verification. The proof court therefore refused to mark the maximality theorem independent until a separate checker existed.

Two earlier evidence chains that had treated the producer's own recovery gate as independent were retracted. This changed the **verification status**, not the mathematical statement.

## Independent checker

The independent checker used a different derivation:

1. subtract pairs of squared-distance equations;
2. solve an exact `2×2` linear system for the unknown point;
3. reconstruct the candidate point in exact arithmetic;
4. verify every required distance and reject anything outside the complete distance-difference cell enumeration.

It did not import the producer implementation and did not assume membership of the unknown point in `Q(sqrt(2002))`; that field membership emerges from the exact solve when appropriate.

Recorded independent results:

| configuration | cells | base / partners | verdict |
|---|---:|---|---|
| H1 | 136,801,313 | base P4; partners P5,P6 | PASS — exactly the 7 listed vertices |
| H2 | 1,335,425,575 | base P4; partners P2,P5 | PASS — exactly the 7 listed vertices |

## Bugs caught by the independent-verification gate

The independent checker caught two genuine implementation defects during development:

1. a `q > 0` condition accidentally discarded all listed points, which would have made a recovery test vacuous;
2. a degenerate cell path silently returned “no roots.”

Both defects were fixed before the final receipts above were accepted. They are recorded here because a computational theorem is stronger when failed proof attempts and soundness defects are preserved rather than erased.

## Logical dependence of the 30,000 bound

Theorem `d_dot(2,8)>30000` depends on two inputs only:

1. the published Kreisel–Kurz classification that H1 is the unique seven-point general-position integral set of diameter at most 30000;
2. the independently verified maximality of H1 above.

No claim about H2 is needed for the 30,000 lower bound; H2 maximality is an additional closure result.