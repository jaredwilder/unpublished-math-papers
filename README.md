# Public mathematics archive

**Author:** Jared Wilder  
**First public timestamp:** 2026-09-10  
**Release-day expansion:** 2026-09-11

This repository is a public subject archive for pure mathematics recovered from a much larger research estate. It contains papers, theorem writeups, exact finite classifications, formalization packets, reductions, computational certificates, counterexamples, and research notes.

Each subject keeps its own evidence status: a theorem remains a theorem, a finite computation remains finite, a conditional result keeps its hypotheses, and a research candidate remains separate from independently confirmed results.

## Current subject directories

| Directory | Contents |
|---|---|
| `caccetta-haggkvist/` | CH3 terminal-defect mathematics and theorem ledger, with conditional and retracted routes marked separately. |
| `circulant-ramsey-family-eliminations/` | Exact restricted-family eliminations: no order-40 circulant `R(3,10)` witness and an order-36 circulant `R(4,6)` elimination. |
| `conference-switching-book-elimination/` | Exact elimination within the symmetric-conference switching construction class for the `N=4m+2` Ramsey-book target. |
| `eg203-analytic-route/` | EG203 analytic-number-theory papers and notes, including gamma-fiber, Stepanov and large-sieve work. |
| `erdos-gyarfas-power-cycle/` | Power-of-two-cycle theorem notes and open follow-up targets. |
| `erdos-selfridge-odd-covering/` | Certified finite obstruction for the dense odd-modulus family `{3,5,7,9,11,13,15}`. |
| `erdos-straus-progressions/` | Complete arithmetic-progression denominator classification with verifier, certificate and literature notes. |
| `erdos-straus-geometric-progressions/` | Complete geometric-progression denominator classification with certificate and literature notes. |
| `erdos-straus-structured-denominators/` | AP/GP denominator writeups collected together. |
| `erdos17-prime-difference-hardness/` | Exact reduction: an affirmative Erdős #17 would force every positive even integer to be a difference of two primes. |
| `erdos156-maximal-sidon-barrier/` | Repaired maximal-Sidon theorem: maximal `A⊂[N]`, `m=|A|`, satisfies `N≤m+m³+m²`, with the missing `2x=a+b` obstruction restored. |
| `erdos197-finite-beautiful-ordering/` | Complete finite analogue: every finite subset of `N` admits an ordering with no monotone 3-term AP, by parity recursion. |
| `erdos243-divisibility-irrationality/` | Eventual divisibility-chain + exploding-ratio criterion forcing `Σ1/a_n` irrational; historical novelty remains uncertain. |
| `erdos247-sparse-binary-irrationality/` | In every integer base `b≥2`, `limsup a_n/n=∞` forces `Σ b^{-a_n}` irrational. |
| `erdos359-reciprocal-prefix-invariant/` | True-greedy-sequence invariant `Σ_{i≤k}1/a_i≥1`, with the earlier wrong-initial-value computation excluded. |
| `erdos413-log-window/` | Exact logarithmic certification-window theorem: all-predecessor conditions reduce to an `O_ε(log n)` terminal window. |
| `erdos486-summable-forbidden-mass/` | Forbidden residue sets with summable mass `Σ|X_n|/n<∞` leave a set of integers with ordinary natural density under the stated activation rule. |
| `erdos501-independent-triple/` | Repaired finite independent-triple lemma using the safe bad-pair bound `≤mN`. |
| `erdos727-k2-obstruction-family/` | Infinite exact `k=2` obstruction family: for prime `p>=7`, `n=2p-2` gives `((n+2)!)^2 ∤ (2n)!`. |
| `erdos893-mersenne-divisor-package/` | Mersenne divisor injection `a|k ⇒ 2^a−1|2^k−1`, `τ(2^k−1)≥τ(k)`, order-sum identity and doubling inequality. |
| `erdos949-sumfree-ip/` | Sharp finite `q≤5` theorem, complete countable analogue, and simultaneous finite-real-dilate IP avoidance for complements of sum-free subsets of `R`. |
| `erdos973-two-point-extremum/` | Exact `n=2` minimax `(√5−1)/2`, attained at fifth roots of unity. |
| `erdos1061-aliquot-square/` | Aliquot-square primitive-seed generator, primitive-ray scaling theorem, exact verifier and SHA-pinned 152,803-row certificate. |
| `erdos1142-order-sieve/` | Multiplicative-order subgroup avoidance theorem, primitive-root divisibility corollary and exact CRT search compression. |
| `erdos1212-isolated-family/` | Infinite family `(2,3^k)` of isolated vertices in the admissible coprime lattice graph. |
| `sums-three-cubes-114/` | Exact mod-7/mod-9 structure for `a³+b³+c³=114`, a `1/343` CRT sieve, and a recovered 15-theorem Lean inventory. |
| `erdos1005-farey/` | Recovered Farey reduction and correction ledger for Erdős #1005; the full source packet has not yet been recovered. |
| `erdos1066-lattice-barriers/` | Lean-certified local barrier theorems for the triangular-lattice/3-colour route to Erdős #1066. |
| `erdos271-stanley/` | 184-entry audited Stanley-sequence theorem/negative ledger. |
| `erdos500-turan34/` | 76-entry Erdős #500 / Turán (3,4) theorem extraction with original evidence states preserved. |
| `erdos595-triangle-cover/` | 65-entry Erdős #595 triangle-cover collection: 60 packet proofs plus compactness, Folkman, conditional and refuted entries. |
| `erdos738-theorem-bank/` | 62 statements/schemas proved in the source packets plus 12 explicitly open targets, with reconstruction data and verifier. |
| `erdos77-ramsey-asymptotics/` | Ramsey asymptotic results, conditional steps, barriers and external targets. |
| `erdos835-sqs20/` | Exact SQS(20) residual-completion graph theorem, 15-pack repair-radius obstruction, one-coordinate rigidity and complete pair-trade geometry. |
| `f31-sum-product-avoidance/` | Sharp `F_31^*` simultaneous sum/product avoidance theorem: maximum 8, exactly 9 extremizers, independently checked in C. |
| `f73-mixed-avoidance/` | Exact simultaneous sum-free/product-free/3-AP-free classification in `F_73^×`. |
| `fiber-coherence-theorem-bank/` | Graph/CSP theorem bank: relational growth, coherence, unicyclic/theta/cactus mechanisms, permutation gluing, rank-three kernels and recursive extensions. |
| `rank-three-kernel/` | Focused cycle-rank-three/K4-free extraction: 22 unconditional results/reductions plus 2 open rank-four targets. |
| `graham-z29-paper/` | Graham/Alspach `Z_29` computational-certificate paper and compiled PDF. |
| `integral-distance-octagon-bound/` | Whole-plane maximality of both Kreisel–Kurz heptagons, strict bound `d(2,8)>30000`, independent-verification audit, and stronger H1 six-vertex octagon obstruction. |
| `kirkman-steiner-lean/` | Provenance record for a complete Lean Bose/Skolem proof of Kirkman's Steiner triple-system existence theorem; the original Lean source bytes still need recovery. |
| `lonely-runner-13/` | 13-effective-speed Lonely Runner theorem bank and reconstructed research record. |
| `mathfire-round8/` | Pure mathematical outputs including AP Erdős–Straus and `[50]` product/GP avoidance, with independent verification. |
| `mathfire-round10/` | Pure mathematical outputs and independent-verification receipts. |
| `mathfire-z31/` | Exact finite-field result and certificate from the Z31 work. |
| `p6-six-vertex-wall/` | P6 / six-vertex-wall theorems, live candidates, negative results and follow-up programs. |
| `polynomial-dynamics-coordinates/` | Standalone recurrence/coordinate mathematics: multiplicative orbit coordinates, invariant subspaces, valuation linearization, finite algebra reconstruction and separator bounds. |
| `prime-gap-admissibility/` | Prime-gap / Hardy–Littlewood admissibility formalization packet. |
| `product-gp-free-50/` | Sharp `[50]` product-free + nontrivial-GP-free classification: maximum 35 and 240 extremizers. |
| `ramsey-r55-circulant-structure/` | Exact structure of the 41-vertex circulant `(5,5)` Ramsey graph, one-vertex nonextension theorem, and circular/fractional/spectral/coding invariants with a reproducible SAT formulation. |
| `riemann-hypothesis/` | RH reductions, identities and failed routes, plus a separately scoped computer-assisted `simple-zero-67.301545-candidate/` research extension. |
| `sieve-preprint/` | Six-source EG203 combinatorial-sieve preprint package; expert review remains pending. |
| `notes/` | Standalone EG203 mathematical notes and program overview. |

## Newly added on 2026-09-11

A long-tail extraction added standalone public packets for #17, #156, #197, #243, #247, #359, #413, #486, #501, #727, #893, #949, #973, #1061, #1142, #1212 and the `k=114` sums-of-three-cubes modular package.

Only pure-mathematics portions were extracted. Mixed biomedical, patent, product and proprietary-system source material remains outside this archive.

## Selected exact results

- Complete AP-denominator classification for the Erdős–Straus equation, with uniqueness/parity split and no primitive denominator triple.
- Complete GP-denominator classification for the Erdős–Straus equation, with unique coprime parameterization and no primitive denominator triple.
- Product-free + nontrivial three-term-GP-free subsets of `[50]`: exact maximum `35`, exactly `240` extremizers.
- Simultaneous sum/product avoidance in `F_31^*`: exact maximum `8`, exactly `9` extremizers.
- Simultaneous sum/product/3-AP avoidance in `F_73^×`: exact maximum `12`, exactly `3` extremizers.
- Cycle-rank-three 2-connected suppression classification into exactly `Q4`, `T221`, `D22`, `K4`, with the induced exact CSP mechanisms.
- Polynomial-size K4-free realization of finite binary CSPs and the corresponding fixed-rank-tractable / unbounded-rank-NP-complete fiber-coherence boundary, at the evidence level stated in its source packet.
- Integral general-position octagons, if they exist, have diameter strictly greater than `30000`; the two known Kreisel–Kurz heptagons are whole-plane maximal against an eighth integral-distance point.
- Completion of a partial pack of pairwise-disjoint SQS(v) to a large set is exactly a graph-colouring problem in the residual block graph; the explicit SQS(20) 15-pack has repair radius at least three and exact local rigidity/trade certificates.
- The unique 41-vertex circulant `(5,5)` Ramsey graph cannot be retained intact and extended by one arbitrary new vertex to a 42-vertex `(5,5)` Ramsey graph.
- Sparse positions with `limsup a_n/n=∞` force irrationality of `Σ b^{-a_n}` in every integer base `b≥2`.
- For every prime `p>=7`, `n=2p-2` gives an exact `k=2` obstruction for Erdős #727.
- Every sum-free `S⊂R` has a `q≤5` with `q,2q∉S`, and its complement contains a countable IP structure with simultaneous avoidance under any finite prescribed set of real dilates.
- The #1061 aliquot-square formula `q=σ(a)-a`, `b=q²-a` produces primitive seeds under explicit primality conditions; the 152,803-row certificate verifies an ordered coefficient floor `2.295492576177`.
- The exact two-point #973 minimax is `(√5−1)/2`, attained at fifth roots of unity.
- Every solution of `a³+b³+c³=114`, if one exists, has exactly one variable divisible by 7 and all three variables congruent to 2 modulo 3.

## Results still awaiting independent confirmation or stronger closure

- `riemann-hypothesis/simple-zero-67.301545-candidate/` contains a computer-assisted candidate extension yielding `67.3015452606376894...%` inside a seven-point Gram-stability framework. The local inequality passed two outward-rounded exhaustive verifier grids; the recovered Arb variant was not run in the original environment. Treat this as a research candidate pending independent reproduction and peer review.
- `jaredwilder/erdos902/f4-ge49-candidate/` contains a computer-assisted candidate proof of `f(4)>=49` with the DRT(23) catalogue audit. The candidate depends on completing the analytic reduction and independently securing the external classification dependency.

## Evidence and scope

Historical novelty is tracked separately from mathematical correctness. Not every ordinary proof in the archive has been Lean-checked, and a theorem inside a larger open problem has exactly the scope stated by that theorem.

Likewise, the Riemann-hypothesis candidate is not presented as a proof of RH; restricted Ramsey-family eliminations do not become unrestricted Ramsey bounds; and finite/conditional results remain finite/conditional.

## Wider release

This is one repository in the larger 2026-09-10/11 mathematics release. The cross-repository map lives in `jaredwilder/erdos-release-index`; the larger provenance archive lives in `jaredwilder/msl-ore-estate`.

## License

Apache-2.0 for repository-authored material unless a file says otherwise. Upstream material retains its own terms.