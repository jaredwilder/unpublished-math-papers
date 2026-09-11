# Conference-matrix switching cannot realize the target book-avoidance family

**Author:** Jared Wilder  
**Campaign date:** 2026-07-22  
**Public estate release:** 2026-09-11

## The construction-class theorem

Let `N=4m+2`, and let `C` be any symmetric conference matrix of order `N`. Consider every graph obtained from the corresponding Seidel/conference construction after arbitrary diagonal `±1` switching.

The recovered Round-5 theorem states:

> **No such switched conference construction yields a graph avoiding the book `B_m` while its complement avoids `B_{m+1}`.**

Thus the entire symmetric-conference switching construction class is eliminated for the corresponding Ramsey-book target.

For the concrete campaign instance `N=398=4·99+2`, this gives:

> No graph obtained from any switching of any symmetric conference matrix of order 398 can simultaneously avoid `B_99` and have complement avoiding `B_100`.

This is a **construction-class impossibility theorem**, not a solution of the ambient Ramsey-book existence problem.

## Proof / certificate character

The source package describes the proof as an **exact row-sum contradiction**, valid uniformly for every symmetric conference matrix of order `4m+2` at the stated book bounds. It is not a solver timeout and does not enumerate individual switchings.

The historical package records:

- producer: `code/eliminate_conference_switching.py`;
- independent replay: `code/verify_conference_elimination_certificate.py`;
- one-command court: `python run_round5_verification.py`;
- verification receipt: `evidence/ROUND5-VERIFICATION.json`;
- original release archive SHA-256: `97388bb06c6965527678c740279162ae0d487c550bc015e839350209134a498b`.

The original archive bytes themselves were not recovered into the current Library/public-GitHub sweep, so this public extraction does not fabricate those files. Their recovery remains a provenance task.

## Other Round-5 negative results

The source package also records, at lower headline level:

1. a Goethals–Seidel length-199 finite-field route was falsified: every tested sign convention missed the required weights and failed the original 398-vertex verifier with excess 12 or 13;
2. the best recovered two-block circulant seed remained an **invalid near-candidate** with maximum book-bound excess 2;
3. that seed was a strict one-swap local optimum inside the exact cross-annihilation manifold.

Those facts are preserved as negative/search knowledge and are not promoted into a global nonexistence statement.

## Novelty boundary

The source explicitly says global literature novelty was **not certified**. Targeted searches had found no exact prior statement, but expert review was still required. This release therefore claims the mathematical construction-class elimination and its campaign provenance, not historical priority.