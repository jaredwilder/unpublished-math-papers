# Public mathematics archive

**Author:** Jared Wilder  
**First public timestamp:** 2026-09-10  
**Release-day expansion:** 2026-09-11

This repository is the **provenance and intake archive** for pure mathematics extracted from a much larger research estate. It contains papers, theorem writeups, formalization packets, exact finite classifications, reductions, certificates, counterexamples, and research notes.

It is **not intended to be the permanent canonical home for every subject**. Coherent theorem families, formalization corpora, and research programs are promoted into focused repositories when a suitable home exists. See [`SUBJECT-ROUTING.md`](SUBJECT-ROUTING.md).

A reader looking for a finished result should prefer the focused subject repository when one is listed there; the copy here preserves extraction history and provenance.

## Recently routed out of the archive

Several results that first appeared here on 2026-09-11 now have clearer canonical homes:

- Erdős #85 exact small values, #289 p-adic obstruction, #291 harmonic criterion, #313 fixed-`k` finiteness, and #700 semiprime binomial-gcd theorem → [`jaredwilder/erdos-proved-lemmas`](https://github.com/jaredwilder/erdos-proved-lemmas);
- Erdős #52 multiplicative-box sumset theorem → [`jaredwilder/additive-combinatorics-campaigns`](https://github.com/jaredwilder/additive-combinatorics-campaigns);
- Erdős #503 exact one-dimensional value and simplex-midpoint construction → [`jaredwilder/erdos-lean-remainder`](https://github.com/jaredwilder/erdos-lean-remainder), beside the existing formal orthogonal-join development;
- rank-2 hereditary Chvátal theorem / Erdős #701 → [`jaredwilder/combinatorial-records`](https://github.com/jaredwilder/combinatorial-records).

The archive copies remain public so the release chronology is not rewritten after the fact.

## Major subject families still present here

The archive currently includes substantial material on:

- Erdős/Kummer and analytic number theory;
- Ramsey theory and finite-field avoidance;
- additive and multiplicative combinatorics;
- integral-distance geometry;
- formalization packets and theorem banks;
- recurrence and polynomial-dynamics coordinates;
- Lonely Runner;
- covering designs and Turán-type problems;
- structured Erdős–Straus denominator families;
- standalone Erdős problem extractions.

Some of these are already large enough to deserve dedicated repositories. The current promotion queue is recorded in [`SUBJECT-ROUTING.md`](SUBJECT-ROUTING.md), including the 184-entry Stanley-sequence ledger, 76-entry Turán (3,4) extraction, 62-result Erdős #738 theorem bank, Lonely Runner 13-speed program, fiber-coherence/rank-three-kernel program, and several sharp finite classification projects.

## Selected mathematics

Among the public contents are:

- exact AP and GP denominator classifications for the Erdős–Straus equation;
- product-free + nontrivial-GP-free subsets of `[50]`: exact maximum `35`, exactly `240` extremizers;
- simultaneous sum/product avoidance in `F_31^*`: exact maximum `8`, exactly `9` extremizers;
- simultaneous sum/product/3-AP avoidance in `F_73^×`: exact maximum `12`, exactly `3` extremizers;
- integral general-position octagons, if they exist, have diameter strictly greater than `30000`;
- exact rank-three graph/CSP structural reductions;
- a sharp finite theorem and countable analogue for Erdős #949;
- the #1061 primitive-ray construction and its 152,803-row certificate;
- exact modular structure for `a^3+b^3+c^3=114`;
- multiple theorem collections and formalization packets extracted from long-running Erdős campaigns.

## Evidence and scope

Each subject keeps its own evidence status. A theorem remains a theorem, a finite computation remains finite, a conditional result keeps its hypotheses, and a research candidate remains separate from independently established results.

Historical novelty is tracked separately from mathematical correctness.

## Applied-IP boundary

Only pure mathematics is intended for this archive. Mixed biomedical, patent, product, private-data, and proprietary-system material remains outside this release unless separately cleared.

See the publication boundary in [`jaredwilder/open-math-frontier`](https://github.com/jaredwilder/open-math-frontier).

## Wider release

The cross-repository map lives in [`jaredwilder/erdos-release-index`](https://github.com/jaredwilder/erdos-release-index). The larger provenance mine lives in [`jaredwilder/msl-ore-estate`](https://github.com/jaredwilder/msl-ore-estate).

## License

Apache-2.0 for repository-authored material unless a file says otherwise. Upstream material retains its own terms.
