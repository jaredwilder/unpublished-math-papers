# Structural supplement — integral-distance octagon campaign

This supplement records additional **unconditional** mathematical assets recovered from the estate atlas after the first public octagon-bound release. It preserves the exact scope visible in the source rather than inventing missing implementation details.

## 1. Rational-distance versus integral-distance existence

General position is invariant under nonzero scaling, and all distances scale linearly. Therefore:

> There exists a general-position eight-point planar set with all pairwise distances rational **if and only if** there exists one with all pairwise distances integral.

The nontrivial direction is immediate by multiplying all coordinates/distances by a common denominator of the finitely many rational pairwise distances.

This is a search-space correction: a rational-distance octagon would already settle the integral-existence question after scaling.

## 2. Exact node structure of the known extension solutions

For the heptagon extension surface written in the campaign coordinates as

`V = { 2002 t_i^2 = Q_i(x,w) }`,

the seven trivial solutions corresponding to the existing vertices are singular points. The source records:

- Jacobian rank `6`, not `7`, at every trivial solution `X=P_j`;
- the `j`-th row vanishes identically there;
- tangent-space dimension `3`, larger than the surface dimension `2`.

Thus the known solutions are **nodes / singular points rather than first-order rigid points**. This killed a naive local-rigidity route and motivated quotienting/blowing up the trivial sections before further algebraic-geometric analysis.

## 3. Triangle-inequality parameterization is genuinely height-free

For a candidate extension point `X` and a fixed base triple `(P_b;P_j,P_k)`, define

`c_j = |XP_b| - |XP_j|`,

`c_k = |XP_b| - |XP_k|`.

If all relevant distances are integral, then `c_j,c_k` are integers. By the triangle inequality,

`|c_j| <= |P_bP_j|`,

`|c_k| <= |P_bP_k|`.

Therefore the extension search reduces to a **finite** set of integer difference cells whose ranges depend only on the fixed heptagon—not on the distance of `X` from the origin or on any externally imposed height bound.

This is the structural reason the H1/H2 maximality computation is an unconditional whole-plane enumeration rather than a bounded search.

## 4. Stronger six-vertex obstruction inside H1

The estate atlas records a theorem stronger than H1 maximality:

> **No general-position integral octagon contains any six-vertex subset congruent to a six-vertex subset of H1.**

Equivalently, deleting any one vertex from H1 and attempting to add **two** new points cannot produce an integral octagon in general position.

This has **no diameter ceiling**. It is strictly stronger than the statement “H1 itself has no eighth integral-distance extension,” because an octagon might contain six vertices of H1 without containing all seven.

The source classifies this result as:

- outcome: `worked`;
- boundary: `unconditional`;
- proof mode/tags: case exhaustion, finite certificate, independent verification, exact verifier.

The original exact-verifier artifact for this stronger six-vertex theorem has not yet been separately recovered into the ChatGPT Library/public GitHub surface, so this file publishes the theorem and provenance class without fabricating a numerical receipt.

## 5. Remaining exclusion ladder

The campaign explicitly identified the next increasingly strong rungs:

- exclude octagons containing a pentagon of H1 plus three new points;
- then a quadrilateral of H1 plus four new points;
- then a triangle of H1 plus five new points.

Those later rungs were not all recorded as closed. They remain a computational/classification frontier and are **not promoted here**.

## Authority boundary

Sections 1–4 above are recorded in the estate as unconditional/worked results. This supplement does not claim the global `n=8` existence problem is solved. It also does not upgrade the unfinished lower rungs of the subconfiguration-exclusion ladder.