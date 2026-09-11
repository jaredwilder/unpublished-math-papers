# Formal authority audit

Source: 2026-09-11 active MSL session export. Only successful kernel-checked declarations promoted here.

| declaration | backend | kernel result | axiom footprint | note |
|---|---|---|---|---|
| `msl_rh_pts_chain_001` | WSL / Mathlib | VERIFIED | `propext`, `Classical.choice`, `Quot.sound` | abstract implication chain; PTS remains a hypothesis |
| `msl_rh_pointwise_coordinate_restates_001` | WSL / Mathlib | VERIFIED | `propext`, `Classical.choice`, `Quot.sound` | abstract pointwise coordinate equivalence |
| `msl_rh_benchmark_telescope_core_002` | Windows / no Mathlib import | VERIFIED | `propext` | factorial-product telescope core |
| `msl_rh_determinant_does_not_imply_simplicity_003` | Windows / no Mathlib import | VERIFIED | empty | purely logical universal-implication falsifier |
| `msl_rh_benchmark_shift_telescope_006` | Windows / no Mathlib import | VERIFIED | `propext`, `Quot.sound` | shifted factorial telescope |

Receipt timestamps in the source export range from `2026-09-11T14:38:34Z` through `2026-09-11T15:48:44Z`.

## Excluded formal attempts

The export also contains formalization attempts that were not promoted:

- one supplied proof failed and acquired a `sorryAx` authority leak;
- two other obligations ended resource-undecided rather than mathematically refuted.

Neither a failed proof attempt nor a timeout is evidence against the underlying mathematical statement. They are therefore excluded from the positive formal inventory rather than rebranded as negative mathematics.

## Claim ceiling

These Lean files verify exactly the declarations they contain. In particular they do **not** kernel-check:

- the Riemann Hypothesis;
- PTS;
- existence or positivity of the asymptotic fixed-slope limit `A(theta)`;
- the full determinant / zero-simplicity bridge needed for a close.
