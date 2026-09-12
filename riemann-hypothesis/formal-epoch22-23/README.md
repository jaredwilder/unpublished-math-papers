# RH epochs 22–23 — recovered formal layer

This directory contains the clean Lean block recovered from the 2026-09-12 session export.

The source file collects 19 successful theorem files from receipt IDs 068–091. It contains zero `sorry` in the recovered source.

The formal statements cover:

- algebraic rearrangements used in the determinant criterion;
- the exponential benchmark identities;
- generic finite-sum and monotonicity lemmas;
- zero-displacement bound shapes;
- the logical sufficiency falsifier used to kill Branch C;
- the generic facts that removing a positive summand lowers a nonnegative sum, an equivalent separator adds no information, and a test constant across approximants cannot discriminate a limiting property.

These are **not formal proofs of RH or zeta-specific analytic estimates**. They seal the algebraic/logical layer around the campaign's computations and falsification logic.

The most consequential statement for the campaign is `msl_rh_necessary_not_sufficient_081`: one witness satisfying a criterion while failing the target property refutes the universal implication. Combined with the exact-rational polynomial witnesses published under `../branch-c-five-link-reduction/`, this is the formal logic behind the Branch C retraction.

Source:

`RH_Epoch22_23_Clean.lean`