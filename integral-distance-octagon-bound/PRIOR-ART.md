# Prior-art / literature boundary

**Search refreshed:** 2026-09-11

The central prior source is:

- Tobias Kreisel and Sascha Kurz, *There are integral heptagons, no three points on a line, no four on a circle*, Discrete & Computational Geometry 39(4) (2008), 786–790; arXiv:0804.1303; DOI 10.1007/s00454-007-9038-6.

That paper:

- constructs the two seven-point integral sets used here;
- proves `d_dot(2,7)=22270`;
- states that the diameter-22270 configuration is the only such seven-point set with diameter at most `30000`;
- does not prove maximality against adding an eighth integral-distance point.

The 2026-09-11 search also checked the current OEIS entry A096873. It still lists minimum general-position integral diameters through `n=7` only:

`1,1,1,8,73,174,22270`,

with no `n=8` value.

Searches for combinations of:

- “integral octagon” + `30000`;
- `d_dot(2,8)` / `d(2,8)` + `30000`;
- “Kreisel Kurz” + maximal extension / eighth point;
- the two heptagon diameters `22270` and `66810` with maximality language;

found no prior publication of either:

1. maximality of both specific Kreisel–Kurz heptagons; or
2. the strict lower bound `d_dot(2,8)>30000`.

The public novelty wording is therefore intentionally qualified:

> Apparently new after systematic search; to the best of our knowledge, these exact results were not previously published.

This is not an assertion that unpublished, private, obscure, or unindexed prior work cannot exist.