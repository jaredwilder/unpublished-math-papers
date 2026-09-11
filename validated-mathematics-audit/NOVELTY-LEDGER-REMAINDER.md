# Curated theorem ledger — remaining exact / known / benchmark mathematics

**Author:** Jared Wilder  
**Source:** `ERDOS_COMPLETE_NOVELTY_MAGNITUDE_LEDGER_2026-09-02.xlsx`  
**Public extraction:** 2026-09-11

This file externalizes the remaining mathematical rows from the 72-row curated theorem/reduction ledger that are not already better represented by a focused release-day packet or by `REGISTRY-SECONDARY.md`.

These are intentionally not all “novel results.” Several are known, subsumed, benchmark-level, or exact reformulations. Their value here is completeness, provenance, and preserving the exact mathematical content without inflating it.

## Erdős #1 — five-element distinct-subset-sum obstruction

The set

\[
A=\{6,9,11,12,13\}\subseteq[1,13]
\]

has all `2^5=32` subset sums distinct. Therefore, in the frozen strict-constant formulation used by the campaign, any universal constant `C` must satisfy

\[
\boxed{C<13/32.}
\]

This is a finite exact obstruction only and is far below stronger public theory for the parent problem.

## Erdős #33 — square-root counting baseline

If every sufficiently large integer has a representation

\[
n=m^2+a,\qquad a\in A,
\]

then necessarily

\[
\boxed{\liminf_{N\to\infty}\frac{|A\cap[1,N]|}{\sqrt N}\ge1.}
\]

This is a counting baseline, not the stronger constant asked by the problem; stronger public lower bounds are known.

## Erdős #51 — finite certified power-of-two preimage block

The historical campaign certified the finite block

\[
\boxed{n_{2^t}=2^{t+1}\qquad(32\le t\le63)}
\]

under its frozen least-totient-preimage notation. The broader asymptotic bridge in the same historical row was not audited and is not promoted here. The universal preimage-size inequalities are separately published in `REGISTRY-SECONDARY.md`.

## Erdős #82 — Ramsey regular-induced-subgraph baseline

Every `n`-vertex graph has a regular induced subgraph on at least

\[
\boxed{\lfloor\log_4 n\rfloor+1}
\]

vertices. Indeed, standard Ramsey theory guarantees a clique or independent set of that size, and either induced graph is regular.

This is a standard logarithmic baseline; it does not approach the parent target `F(n)/log n→∞`.

## Erdős #155 — one-step monotonicity

For the frozen extremal function,

\[
\boxed{F(N+1)\le F(N)+1.}
\]

This is the `k=1` case of the standard subadditivity relation already present in the public discussion. It is preserved as infrastructure, not novelty.

## Erdős #170 — perfect five-mark ruler endpoint

There is no five-point perfect difference ruler contained in `[0,10]`. This is an exact finite obstruction and a classical Golomb-ruler fact, retained as a finite certificate/regression rather than a new result.

## Erdős #200 — small-prime divisibility in long prime arithmetic progressions

For a sufficiently long arithmetic progression of primes, every sufficiently small prime `q` must divide the common difference `d`, apart from the endpoint exception in which one progression term itself equals `q`.

Reason: if `q∤d`, the progression sweeps distinct residue classes modulo `q`; once long enough, one term is `0 mod q`, forcing that term to equal `q` if it is prime. This is a classical necessary condition only.

## Erdős #236 — logarithmic representation cap

For

\[
f(n)=\#\{k:n=p+2^k\text{ for some prime }p\},
\]

there are at most `floor(log2 n)+1` candidate powers of two. Hence

\[
\boxed{f(n)\le\lfloor\log_2 n\rfloor+1.}
\]

This tautological `O(log n)` bound is only a benchmark; the parent asks for `o(log n)`.

## Erdős #254 — exact rational-parameter characterization

Let `theta=a/q∈(0,1)` be reduced. Then

\[
\boxed{
\sum_{n\in A}\|\theta n\|=\infty
\iff
A\text{ contains infinitely many }n\not\equiv0\pmod q.
}
\]

If `q|n`, the summand is zero. Otherwise `an mod q` is nonzero, so

\[
\|an/q\|\ge1/q.
\]

Thus infinitely many nonmultiples force divergence, while only finitely many nonmultiples leave a finite sum. This characterizes the rational-`theta` hypothesis only; it does not prove the parent subset-sum conclusion.

## Erdős #445 — classical `c>3/4` route

The campaign recovered the standard incomplete-Kloosterman-sum mechanism giving the desired inverse pair in every interval of length

\[
H=p^c
\]

when

\[
\boxed{c>3/4.}
\]

This is a known theorem architecture and was not reproved from first principles in the release. The hard target is every `c>1/2`.

## Erdős #477 — density necessity for unique polynomial tiling

For a polynomial image `f(Z)` of degree `d>=2`, a hypothetical unique tiling

\[
\mathbb Z=A\oplus f(\mathbb Z)
\]

forces `A` to have the complementary density scale required by counting the sparse polynomial values in long intervals. The historical row is a reduction and requires careful one-/two-tail bookkeeping before being used as a formal theorem.

The exact square-image impossibility theorem is stronger and is released in `../validated-new-gold-ledger/`.

## Erdős #489 — finite-`A` periodic squared-gap formula

For finite `A` with `gcd(A)=1`, let `B` be the integers avoiding divisibility by every `a∈A`. With

\[
M=\operatorname{lcm}(A),
\]

membership in `B` is periodic modulo `M` beyond the frozen cutoff. Therefore the mean squared gap, when defined over consecutive surviving residues, is exactly the cyclic average over one period.

This is a finite-`A` periodicity statement only.

## Erdős #495 — rational-coordinate Littlewood stratum

If either `alpha` or `beta` is rational, then

\[
\boxed{\liminf_{n\to\infty}n\|n\alpha\|\|n\beta\|=0.}
\]

Take multiples of the denominator of the rational coordinate; one distance-to-nearest-integer factor vanishes exactly. The irrational–irrational case is the Littlewood conjecture and remains open.

## Erdős #535 — powers-of-two construction

For every `r>=3`, the powers of two up to `N` form an elementary construction for the frozen equal-pairwise-gcd avoidance condition, giving

\[
\boxed{f_r(N)\ge\lfloor\log_2N\rfloor+1.}
\]

This is a weak classical-style lower construction, far below the known frontier.

## Erdős #595 — countable-graph stratum

Every countable graph is a countable union of triangle-free graphs: enumerate its edges and use one single-edge graph per edge. Therefore any genuinely difficult witness in the parent covering problem must be uncountable.

This is a cardinality reduction only.

## Erdős #602 — countable-family Property B stratum

Every countable family of countably infinite sets with pairwise finite intersections admits a two-colouring under which each member is bichromatic. This is the classical Bernstein-lemma/Property-B countable-family phenomenon and was independently recovered by the campaign.

The uncountable family regime remains separate.

## Erdős #653 — elementary distance-count sandwich

For the frozen quantity `g(n)` maximizing the number of distinct values `R(x_i)` over planar configurations,

\[
\boxed{\lceil n/2\rceil\le g(n)\le n-2\qquad(n\ge7).}
\]

These are weak structural bounds and are subsumed by stronger known results. Historical campaign attempts to use a single regular polygon to upper-bound this **maximum** were quantifier errors and remain quarantined.

## Erdős #689 — incidence double-count condition

If one chooses a residue class `a_p mod p` for every prime `p<=n` and every integer in `[1,n]` is covered at least twice, then necessarily

\[
\boxed{\sum_{p\le n}\left\lceil\frac np\right\rceil\ge2n.}
\]

This follows by counting all residue-class incidences. It is only a necessary condition and is asymptotically too weak to settle the problem.

## Erdős #726 — fractional-part reformulation

The indicator of

\[
n\in(p/2,p)\pmod p
\]

can be rewritten exactly as a residue/fractional-part condition, converting the original counting problem into a weighted equidistribution problem. The rewrite is exact; the required asymptotic equidistribution estimate is not supplied by the campaign.

## Erdős #730 — central-binomial parity

For every `n>=1`,

\[
\boxed{{2n\choose n}\text{ is even}.}
\]

This is an elementary reusable lemma, not frontier progress.

## Erdős #774 — easy direction for proportionately dissociated sets

If

\[
A=A_1\cup\cdots\cup A_k
\]

with each `A_i` dissociated, then every finite `B⊂A` contains a dissociated subset of size at least

\[
\boxed{|B|/k.}
\]

Indeed some colour class `B∩A_i` has at least `|B|/k` elements. This is the easy direction; the parent asks for a converse-type statement.

## Erdős #881 — explicit `k=1` endpoint construction

For the order-1 endpoint, take

\[
A=\mathbb N,
\qquad
B=\{n:n\equiv2\pmod4\}.
\]

Then `A` is a minimal asymptotic basis of order 1 and `A\B` is an asymptotic basis of order 2. The campaign independently recovered this endpoint; a broader 2026 public claim already covers the same stratum, so no novelty is asserted.

## Erdős #886 — easy `epsilon>=1/2` endpoint

If

\[
\varepsilon\ge1/2,
\]

then the interval

\[
(\sqrt n,\sqrt n+n^{1/2-\varepsilon})
\]

has length at most 1. Hence it contains at most one integer and

\[
\boxed{K=1}
\]

works on this easy parameter range. The hard regime is `0<epsilon<1/2`.

## Erdős #912 — exponent-one primes in `n!`

For a prime `p`,

\[
\boxed{v_p(n!)=1\iff n/2<p\le n.}
\]

Therefore the number of distinct primes appearing to exponent exactly one in `n!` is

\[
\boxed{\pi(n)-\pi(\lfloor n/2\rfloor).}
\]

This is exact Legendre bookkeeping, not the parent asymptotic for the number of distinct exponent values.

## Erdős #968 — prime-ratio monotonicity rewrite

Let

\[
u_n=p_n/n,\qquad d_n=p_{n+1}-p_n.
\]

Then

\[
\boxed{u_n<u_{n+1}\iff nd_n>p_n\iff d_n>p_n/n.}
\]

This is exact algebra. The positive-density question remains a prime-gap problem.

## Erdős #979 — parity obstruction and exact finite collision

Under the campaign's unordered-multiset convention for the `k=2` representation count:

- if `n≡3 mod4`, then
  \[
  \boxed{f_2(n)=0};
  \]
- at
  \[
  n=410,
  \]
  there are at least two representations, witnessed by
  \[
  \{7,19\},\qquad\{11,17\}.
  \]

These are finite/structural facts only; the `k=2` asymptotic problem is already settled in the public record.

## Erdős #1055 — class-1 smooth-shift barrier

A class-1 prime is exactly a prime `p` satisfying

\[
\boxed{p+1=2^a3^b.}
\]

Thus the infinitude clause already contains the open problem of infinitely many primes one below a 3-smooth number. This is direct definition unpacking / hardness context, not progress on the infinitude question.

## Erdős #1060 — parity characterization and exact collision

For every positive integer `k`,

\[
\boxed{k\sigma(k)\text{ is odd}\iff k\text{ is an odd square}.}
\]

This uses the classical criterion that `sigma(k)` is odd iff `k` is a square or twice a square.

The map is not injective:

\[
\boxed{12\sigma(12)=14\sigma(14)=336.}
\]

These facts do not give the parent representation-multiplicity bound.

## Erdős #1085 — known quadratic regime for `d>=4`

For every fixed `d>=4`, the standard Lenz construction gives

\[
\lfloor n/2\rfloor\lceil n/2\rceil\le f_d(n),
\]

while trivially

\[
f_d(n)\le{n\choose2}.
\]

Hence

\[
\boxed{f_d(n)=\Theta(n^2)}
\]

for fixed `d>=4`. This is known public mathematics, included to preserve the campaign's correct dimensional slicing.

## Erdős #1094 — Sylvester prime-factor theorem

For

\[
n\ge2k,
\]

Sylvester's classical theorem gives a prime factor

\[
\boxed{p>k}
\]

of

\[
{n\choose k}.
\]

This is background only; the canonical problem asks for a least-prime-factor upper bound.

## Erdős #1104 — monotonicity of triangle-free chromatic extremum

Let `f(n)` be the maximum chromatic number of a triangle-free graph on `n` vertices. Then

\[
\boxed{f(n+1)\ge f(n)}.
\]

Append an isolated vertex to an extremal `n`-vertex graph. This is bookkeeping, not asymptotic progress.

## Erdős #1192 — Sidon sets cannot be order-2 asymptotic bases

An order-2 asymptotic basis must satisfy the counting lower bound

\[
A(x)\ge(\sqrt2-o(1))\sqrt x,
\]

whereas a Sidon set satisfies

\[
A(x)\le(1+o(1))\sqrt x.
\]

Therefore no Sidon set is an asymptotic basis of order 2. This is standard density-counting context; the square-sum condition in the parent problem is weaker than being Sidon.

## Authority boundary

The source novelty ledger explicitly distinguishes `KNOWN`, `SUBSUMED`, `BENCHMARK_ONLY`, `APPARENTLY_UNRECORDED_*`, and candidate-novel statuses. This release preserves those distinctions. A known theorem is included because it was part of the mathematical estate, not because the campaign claims priority for it.

## License

Apache-2.0 for repository-authored material.
