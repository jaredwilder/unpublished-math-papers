# Canonical registry — secondary theorem and reduction release

**Author:** Jared Wilder  
**Source:** September 2026 canonical theorem registry  
**Public extraction:** 2026-09-11

This file externalizes the remaining clean mathematical rows from the audited canonical registry that did not warrant their own top-level directory in the first release-day wave. It is intentionally heterogeneous: exact slices, universal reductions, citation-dependent subcases, constructions, corrected criteria, and negative closes keep their source authority class.

A theorem being listed here does **not** mean historical novelty, full parent-problem closure, or universal Lean certification.

## Erdős #376 — Kummer no-carry criterion for `gcd(C(2n,n),105)`

**Status:** `MATHEMATICALLY_AUDITED_LEAN_READY`  
**Scope:** universal equivalence

\[
\boxed{\gcd\!\left({2n\choose n},105\right)=1}
\]

if and only if doubling `n` produces no carries in bases `3,5,7`. Equivalently:

- every base-3 digit of `n` is at most 1;
- every base-5 digit is at most 2;
- every base-7 digit is at most 3.

This is Kummer's theorem: `v_p(C(2n,n))` equals the number of carries in `n+n` in base `p`. The residual infinitude question remains open.

## Erdős #681 — prime-shift witness geometry and fourth-root search window

**Status:** `MATHEMATICALLY_AUDITED_LEAN_READY`  
**Scope:** universal reduction

For the campaign witness condition, `k=1` works exactly when `n+1` is composite. Hence every possible hard input has

\[
n+1=p
\]

prime. On this prime-shift residual, even `k` are eliminated and every remaining witness satisfies

\[
\boxed{k^4<n+k.}
\]

Indeed if `m=n+k` is composite then its least prime factor is at most `sqrt(m)`, while the witness inequality requires that least prime factor to exceed `k^2`; hence `k^4<m=n+k`. This reduces the residual search to `O(p^{1/4})` odd shifts.

## Erdős #238 — complete `c_2<2` parameter slice

**Status:** `MATHEMATICALLY_AUDITED_CITATION_DEPENDENT`  
**Scope:** full restricted parameter slice

For every fixed `c_1>0` and `0<c_2<2`, the requested prime block exists for all sufficiently large `x`.

Distinct odd primes differ by at least 2, so the separation condition is automatic in this range. Standard prime-counting growth supplies more than `c_1 log x` primes eventually. This is a restricted slice, not the full arbitrary-`c_2` problem.

## Erdős #821 — odd totient targets have no preimages

**Status:** `MATHEMATICALLY_AUDITED_LEAN_READY`  
**Scope:** universal domain filter

If

\[
g(n)=\#\{m:\varphi(m)=n\},
\]

then for every odd `n>1`,

\[
\boxed{g(n)=0.}
\]

For `m>=3`, the units modulo `m` pair fixed-point-freely under `a↦-a`, so `φ(m)` is even; the only odd totient value is `φ(1)=φ(2)=1`.

## Erdős #936 — exact mod-9 periodicity

**Status:** `MATHEMATICALLY_AUDITED_LEAN_READY`

\[
\boxed{9\mid2^n+1\iff n\equiv3\pmod6.}
\]

The powers of 2 modulo 9 have period 6:

\[
2,4,8,7,5,1.
\]

Only exponent class 3 gives `-1`. This complements the separately released powerful-number mod-8 restrictions.

## Erdős #406 — recursive 3-adic exponent sieve

**Status:** `MATHEMATICALLY_AUDITED_LEAN_READY`  
**Scope:** universal sieve; **not** the old false close

If the ternary expansion of `2^n` uses only digits `0,1`, then

\[
\boxed{n\pmod{18}\in\{0,2,6,8\}.}
\]

More generally, modulo `3^r`, the admissible exponent set consists of exactly

\[
2^{r-1}
\]

residue classes modulo `2·3^{r-1}`.

Reason: a `{0,1}` ternary residue modulo `3^r` is a Cantor residue. Exactly half of those residues are units. Since 2 is a primitive root modulo `3^r`, every unit corresponds to one exponent class. The historical Senge–Straus-based “close” remains blacklisted.

## Erdős #683 — necessary ceiling on a universal exponent

**Status:** `MATHEMATICALLY_AUDITED_LEAN_READY`  
**Scope:** necessary condition only

Any constant `c` satisfying the frozen binomial largest-prime-factor inequality must obey

\[
\boxed{c\le\log_3(5/3).}
\]

At `(n,k)=(10,3)`,

\[
{10\choose3}=120
\]

has largest prime factor 5, while `n-k+1=8`. Therefore

\[
5\ge\min(8,3^{1+c}),
\]

forcing `3^{1+c}<=5`.

## Erdős #913 — exact `omega=2` stratum

**Status:** `MATHEMATICALLY_AUDITED_CITATION_DEPENDENT`

If `omega(n(n+1))=2` and the two nonzero prime exponents are distinct, then `n` lies in one of exactly three branches:

1. `n=8`;
2. `n=2^a` with `2^a+1` prime (Fermat-prime predecessor branch);
3. `n=2^b-1` with `2^b-1` prime (Mersenne-prime branch).

Coprimality forces `n,n+1` to be prime powers. If both exponents exceed 1, Catalan–Mihăilescu leaves `8,9`; if one exponent is 1, parity forces the other number to be a power of 2. This corrects a raw route that omitted the Mersenne branch.

## Erdős #145 — squarefree-gap moments for `0<=alpha<=1`

**Status:** `MATHEMATICALLY_AUDITED_CITATION_DEPENDENT`

For every fixed

\[
0\le\alpha\le1,
\]

the normalized `alpha`-moment of squarefree gaps has a finite limit; for `alpha=1` the limit is 1.

For each fixed gap, standard finite squarefree-pattern correlation theory supplies a density. For `alpha<1`, truncate the gap at `G` and bound the tail by `G^{alpha-1}` times the telescoping total gap sum. At `alpha=1`, telescope directly.

The separate campaign statement “all squarefree gaps are at most 4” is false by CRT and remains quarantined.

## Erdős #539 — exact base case `h(2)=2`

**Status:** `MATHEMATICALLY_AUDITED_LEAN_READY`

For a two-element set `A={a,b}` and `g=gcd(a,b)`, the frozen quotient set is

\[
\{1,a/g,b/g\},
\]

so its size is 2 or 3. Taking a divisibility pair such as `{1,2}` achieves 2. Hence

\[
\boxed{h(2)=2.}
\]

This exact base case is separate from the campaign's rejected false global close.

## Erdős #168 — two-thirds avoidance construction

**Status:** `MATHEMATICALLY_AUDITED_LEAN_READY`

For the `{n,2n,3n}` avoidance problem,

\[
\boxed{F(N)\ge\lceil2N/3\rceil.}
\]

Take all integers at most `N` not divisible by 3. Every forbidden triple contains `3n`, which is excluded.

## Erdős #120 — complete unbounded-`A` subcase

**Status:** `MATHEMATICALLY_AUDITED_LEAN_READY`

If the frozen set `A` is unbounded, the positive-measure set

\[
E=[0,1]
\]

contains no nondegenerate affine copy `aA+b` with `a≠0`, because every such image of an unbounded set is unbounded. Therefore only bounded infinite `A` remain hard in that formulation.

## Erdős #503 — exact one-dimensional slice

**Status:** `MATHEMATICALLY_AUDITED_LEAN_READY`

In one dimension, the largest set in which every three points determine an isosceles triangle has size exactly

\[
\boxed{3.}
\]

Three equally spaced points work. If `x_1<x_2<x_3<x_4` all triples worked, triples `123` and `124` force

\[
x_1+x_3=2x_2=x_1+x_4,
\]

hence `x_3=x_4`, contradiction.

## Erdős #503 — simplex-midpoint construction in all `d>=2`

**Status:** `MATHEMATICALLY_AUDITED_LEAN_READY`

For every `d>=2`,

\[
\boxed{f(d)\ge {d+1\choose2}+1.}
\]

Take all edge midpoints of a regular `d`-simplex and add its center. Distances between distinct edge midpoints depend only on whether the corresponding simplex edges intersect, so the midpoint set is a two-distance set; every triangle formed from it is isosceles. The center is equidistant from all midpoints.

## Erdős #849 — exact representation-multiplicity slices

**Status:** `MATHEMATICALLY_AUDITED_LEAN_READY`

Under `1<=k<=n/2`:

- `2` has exactly one binomial representation;
- `10` has exactly two:
  \[
  {5\choose2}={10\choose1}=10;
  \]
- `120` has exactly three:
  \[
  {10\choose3}={16\choose2}={120\choose1}=120.
  \]

Monotonicity and minimum-binomial bounds rule out additional admissible `k` in these slices.

## Erdős #241 — strong-`B_3` counting bound

**Status:** `MATHEMATICALLY_AUDITED_LEAN_READY`

If `A⊆[N]`, `|A|=m`, and all unordered 3-multiset sums are distinct, then

\[
\boxed{{m+2\choose3}\le3N-2.}
\]

There are `C(m+2,3)` unordered triples with repetition, and their distinct sums all lie in `[3,3N]`, which contains exactly `3N-2` integers. In particular

\[
m^3<18N.
\]

Stronger constants 9 or 6 claimed from the same elementary count were rejected.

## Erdős #930 — exact `r=2` threshold obstruction

**Status:** `MATHEMATICALLY_AUDITED_LEAN_READY`

Any threshold `k` valid for the `r=2` formulation must satisfy

\[
\boxed{k\ge4.}
\]

The two disjoint length-3 intervals

\[
\{1,2,3\},\qquad\{48,49,50\}
\]

have total product

\[
1·2·3·48·49·50=705600=840^2,
\]

so `k<=3` cannot work.

## Erdős #385 — parity baseline and reduction to even `n`

**Status:** `MATHEMATICALLY_AUDITED_LEAN_READY`

For every `n>=5`,

\[
F(n)\ge n,
\]

and for odd `n>=5`,

\[
\boxed{F(n)>n.}
\]

For odd `n`, choose `m=n-1`: it is even composite with least prime factor 2, so `m+p(m)=n+1`. For even `n>=6`, choose `m=n-2`, giving the baseline `n`. Thus the first nontrivial question reduces to even `n`.

## Erdős #341 — exact seed `{1}`

**Status:** `MATHEMATICALLY_AUDITED_LEAN_READY`

Starting the frozen greedy pair-sum process from `A={1}` produces

\[
\boxed{1,3,5,7,\ldots}
\]

with constant gap 2. If the current set is the first `m` odd numbers, its pair sums fill every even integer from 2 through `4m-2`; the least larger integer not represented is the next odd `2m+1`.

## Erdős #579 — common-neighborhood reduction

**Status:** `MATHEMATICALLY_AUDITED_LEAN_READY`

In a `K_{2,2,2}`-free graph, the common neighborhood of any two vertices is `K_{2,2}`-free.

A `K_{2,2}` inside `N(u)∩N(v)`, together with `{u,v}`, is a `K_{2,2,2}`; adjacency between `u,v` is irrelevant because containment is non-induced.

## Erdős #291 — corrected harmonic divisibility criterion

**Status:** `MATHEMATICALLY_AUDITED_LEAN_READY`

Let `p<=n` be prime, let `p^e` be the largest power of `p` not exceeding `n`, and let

\[
q=\lfloor n/p^e\rfloor.
\]

For the campaign harmonic numerator `a_n`,

\[
\boxed{p\mid\gcd(a_n,L_n)}
\]

if and only if the reduced numerator of

\[
H_q=1+1/2+\cdots+1/q
\]

vanishes modulo `p`.

After scaling by `L_n`, modulo `p` every term disappears except denominators with exact `p`-valuation `e`, namely `j p^e`, `1<=j<=q<p`; the surviving common factor is nonzero mod `p` and leaves `Σj^{-1}`. This repairs the corrupted `floor(n/p)` criterion, which fails at `(n,p)=(18,3)`.

## Erdős #377 — corrected large-prime Kummer interval criterion

**Status:** `MATHEMATICALLY_AUDITED_LEAN_READY`

Let `p<=n` be prime with

\[
p>\sqrt{2n},
\]

and put `k=floor(n/p)`. Then

\[
\boxed{p\nmid {2n\choose n}\iff p>\frac{2n}{2k+1}.}
\]

Since `2n<p^2`, the base-`p` expansion of `n` has at most two digits. Write `n=kp+r`. Kummer says divisibility by `p` occurs exactly when doubling causes a carry; no carry is `2r<p`, equivalent to the displayed inequality. The unrestricted raw ledger version omitted the `p>sqrt(2n)` hypothesis and is false.

## Erdős #394 — universal prime slice

**Status:** `MATHEMATICALLY_AUDITED_LEAN_READY`  
**Formal note:** existing green receipt checks primes below 100 only

For every odd prime `p`,

\[
\boxed{t_2(p)=p-1.}
\]

For `1<=m<=p-2`, neither `m` nor `m+1` is divisible by `p`; at `m=p-1`, the product `(p-1)p` is divisible by `p`.

## Erdős #887 — explicit two-nearby-divisor family

**Status:** `MATHEMATICALLY_AUDITED_LEAN_READY`

For every `m>=2`, let

\[
n=m(m-1)(m+1)(m+2).
\]

Then the two divisors

\[
d_1=m^2+m,\qquad d_2=m^2+2m
\]

both lie in

\[
\boxed{(\sqrt n,\sqrt n+2n^{1/4}).}
\]

Both divide `n`; squaring proves each exceeds `sqrt n`, and `(d-sqrt n)=(d^2-n)/(d+sqrt n)` gives the stated upper excess.

## Erdős #359 — quadratic upper bound for the true greedy sequence

**Status:** `MATHEMATICALLY_AUDITED_LEAN_READY`

For the true `n=1` greedy consecutive-block-sum sequence,

\[
\boxed{a_{k+1}\le\frac{k(k+1)}2+1.}
\]

Among `k` earlier terms there are at most `k(k+1)/2` contiguous blocks and therefore at most that many represented positive integers; the least missing positive integer is no larger than one plus this count. The green receipt that encoded `a_2=5` remains quarantined.

## Erdős #153 — Sidon sumset bookkeeping and gap inequality

**Status:** `MATHEMATICALLY_AUDITED_LEAN_READY`

If `A` is a finite Sidon set, `|A|=n`, and

\[
A+A=\{s_1<\cdots<s_t\},
\]

then

\[
\boxed{t=\frac{n(n+1)}2}
\]

and

\[
\boxed{(s_t-s_1)^2\le(t-1)\sum_{i<t}(s_{i+1}-s_i)^2.}
\]

The first identity is uniqueness of unordered pair sums with repetition; the second is Cauchy–Schwarz on the positive gaps.

## Erdős #51 — elementary totient-preimage size bound

**Status:** `MATHEMATICALLY_AUDITED_LEAN_READY`

If `phi(n)=a` and `r=omega(n)`, then

\[
\boxed{r!\le a,\qquad n/a\le2^r.}
\]

Hence

\[
\boxed{n\le a\,2^{R(a)}},
\]

where `R(a)=max{r:r!<=a}`.

Indeed

\[
\frac n{\varphi(n)}=\prod_{p\mid n}\frac p{p-1}\le2^r,
\]

while the `i`-th distinct prime is at least `i+1`, yielding

\[
\varphi(n)\ge\prod_{i=1}^r(p_i-1)\ge r!.
\]

This bounds every preimage but does not settle existence.

## Erdős #313 — finiteness for every fixed number of primes

**Status:** `MATHEMATICALLY_AUDITED_LEAN_READY`

For every fixed `k`, the equation

\[
\sum_{i=1}^k\frac1{p_i}=1-\frac1m
\]

with distinct primes has only finitely many solutions. Any infinite family must therefore have unbounded `k`.

Let `P=∏p_i`. Clearing denominators modulo each `p_i` forces every `p_i|m`, while the cleared equation also gives `m|P`; hence `m=P` and

\[
\sum_i1/p_i+1/P=1.
\]

Now `p_1<=k+1`. After fixing `p_1,...,p_j`, a positive residual `R_j` obeys

\[
R_j\le\frac{k-j+1}{p_{j+1}},
\]

so

\[
p_{j+1}\le\frac{k-j+1}{R_j},
\]

leaving finite branching at every stage.

## Erdős #371 — consecutive largest-prime-factor ties are impossible

**Status:** `MATHEMATICALLY_AUDITED_LEAN_READY`

For every `n>=2`,

\[
\boxed{P(n)\ne P(n+1).}
\]

If the same prime were the largest prime divisor of both, it would divide `gcd(n,n+1)=1`. The density-half question remains open.

## Erdős #412 — sigma orbits are strictly increasing above 1

**Status:** `MATHEMATICALLY_AUDITED_LEAN_READY`

For every `n>=2`,

\[
\sigma(n)\ge n+1>n.
\]

Hence every forward sigma orbit starting above 1 is strictly increasing and repetition-free. This alone does not prove two distinct sigma orbits intersect.

## Erdős #655 — literal frozen distance statement is false

**Status:** `MATHEMATICALLY_CLOSED_NEGATIVE_LITERAL`  
**Formal note:** archived green receipt checked only a finite proxy

For every `n>=3`, a regular `n`-gon satisfies the frozen circle condition and determines exactly

\[
\boxed{\lfloor n/2\rfloor}
\]

distinct distances. Thus no `c>0` can make the literal lower bound `(1+c)n/2` hold eventually.

From a fixed vertex, each chord length occurs at at most the two mirror offsets `j,n-j`, so no centered circle contains three other vertices. The chord lengths `2R sin(pi j/n)`, `1<=j<=floor(n/2)`, are distinct.

This is a mathematical negation of the literal frozen wording; it is not represented as a new historical discovery or as proof that an intended stronger/general-position version was false.

## Erdős #68 — exact geometric-series reformulation

**Status:** `MATHEMATICALLY_AUDITED_LEAN_READY`

For `n>=2`,

\[
\boxed{\frac1{n!-1}=\sum_{j\ge1}(n!)^{-j}.}
\]

Every finite truncation has an exact positive geometric remainder. This is a reformulation only; the irrationality target remains open.

## Erdős #25 — summable-reciprocal density theorem

**Status:** `MATHEMATICALLY_AUDITED_LEAN_READY`

Under the frozen cutoff convention, if

\[
\sum_i1/n_i<\infty,
\]

then the surviving congruence-avoiding set has ordinary natural density and therefore logarithmic density. Finite truncations are eventually periodic; tail exclusions on `[1,X]` contribute at most a constant multiple of `X Σ_{i>m}1/n_i`, and upper/lower densities squeeze together.

This is subsumed by the stronger arbitrary-forbidden-residue-set theorem in `../erdos486-summable-forbidden-mass/`.

## Erdős #390 — factorial envelope and lower-bound package

**Status:** `MATHEMATICALLY_AUDITED_LEAN_READY`

Any admissible factorization whose largest selected factor is `m` satisfies

\[
\boxed{m!\ge(n!)^2.}
\]

Consequently Stirling inversion gives

\[
\boxed{f(n)\ge2n-(2\log2+o(1))\,n/\log n.}
\]

Also, if `n/2<p<=n` is prime, then

\[
\boxed{f(n)\ge2p.}
\]

The chosen factors lie in `{n+1,...,m}`, so their product divisibility yields the factorial envelope. For the prime carrier, `v_p(n!)=1`, so one chosen factor must be a multiple at least `2p`.

## Authority boundary

The source registry contains exact status and formal-scope fields. This release preserves the mathematical statements and their corrections but does not turn `LEAN_READY` into `KERNEL_CHECKED`, a citation-dependent row into an independent proof of its imported theorem, or a restricted slice into a parent close.

## License

Apache-2.0 for repository-authored material.
