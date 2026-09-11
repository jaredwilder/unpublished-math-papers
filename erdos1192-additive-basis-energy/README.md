# Erdős #1192 — additive bases with linear representation energy

**Author:** Jared Wilder  
**Campaign:** 2026-09-01/02  
**Public human extraction:** 2026-09-11

This directory is the human mathematical front door for a large campaign that previously existed only as raw JSON/transcript material in `jaredwilder/erdos-campaign-archive`.

## The frozen problem

For `A⊂N`, let `f_r(n)` count **ordered** `r`-tuples

\[
(a_1,\ldots,a_r)\in A^r
\]

with repetition allowed and

\[
a_1+\cdots+a_r=n.
\]

The campaign asks whether, for every `r>=2`, there exists one set `A=A_r` which is an asymptotic basis of order `r` and simultaneously satisfies

\[
\boxed{\sum_{n\le x} f_r(n)^2=O(x).}
\]

The hidden constant may depend on `r` and on the chosen `A`, but not on `x`.

The quantifiers are important: the witness may depend on `r`, but for a fixed `r` the **same** `A` must satisfy both the basis condition and the linear second-moment bound.

## Why the problem is structurally sharp

If `A` is an asymptotic basis of order `r`, then all sufficiently large integers have at least one representation. Hence over a long interval the total representation mass is at least linear in the interval length. Cauchy–Schwarz therefore supplies a linear lower floor for

\[
\sum f_r(n)^2.
\]

So the requested `O(x)` bound sits at the smallest possible order of magnitude. The campaign is not merely seeking some finite-energy basis; it is seeking a basis whose ordered representation energy is asymptotically as small as the elementary counting floor permits up to constants.

## Research architectures explored

The route registry contains a genuine multi-route research program rather than one attempted proof. Its principal architectures include:

- layered Erdős–Rényi / randomized thinning constructions;
- Bose–Chowla and Sidon-type modular blocks;
- dyadic scale-separated cascades;
- exact `r`-fold energy reformulations;
- Raikov–Stöhr / block-separation constructions;
- finite integer-programming and exact-window optimization;
- certified finite codegree tables plus proposed finite-to-infinite transfer;
- digital/block constructions and carry-control attempts;
- local-to-global gluing and residue isolation.

Several routes died because their transfer lemmas were false, not because the finite mathematics underneath them was worthless. The campaign is especially valuable as a map of which plausible local-energy mechanisms do **not** automatically produce the required global basis.

## Exact finite theorem — the `[2,8]` order-2 energy minimum

Under the positive-integer convention, among subsets `A` whose two-fold sumset covers every integer in `[2,8]`, the exact minimum of

\[
\sum_{n=2}^{8} f_2(n)^2
\]

is

\[
\boxed{27}.
\]

Modulo elements larger than `7`, which are inert for representations of numbers at most `8`, the two active extremal cores are

\[
\boxed{\{1,2,3,6\},\qquad \{1,2,4,6\}.}
\]

Their ordered representation vectors on `2,...,8` are respectively

\[
(1,2,3,2,1,2,2)
\]

and

\[
(1,2,1,2,2,2,3),
\]

both having square-sum `27`.

The campaign also records that all other active positive-integer cores in the exhaustive search have square-sum at least `31`, while the natural greedy witness `{1,2,3,5}` has square-sum `35`.

### Endpoint correction

One historical repair briefly called `0` an inert element. It is not: adding `0` changes low representations. For example

`A={0,1,2,3,6}`

has the same positive active core but a different energy. The clean finite theorem above therefore uses the positive-integer convention and treats only elements `>=8` as inert for the `[2,8]` window.

## Exact finite identity used throughout

For `A={1,2}` and `r=2`,

\[
f_2(2)=1,\qquad f_2(3)=2,\qquad f_2(4)=1,
\]

so

\[
\sum_{n=2}^{4}f_2(n)^2=6.
\]

This tiny check became a useful semantic regression test because it distinguishes ordered from unordered representations and catches domain drift involving `0`.

## Important negative results / route kills

The campaign preserved several structural failures that should travel with any future attempt:

1. **Finite-window certification does not imply an asymptotic basis theorem.** A verifier covering large finite ranges cannot discharge the full `x→∞` quantifier without a proved transfer theorem.
2. **The same witness must satisfy both conjuncts.** A good finite basis and a separate low-energy set cannot be combined by assertion.
3. **Padding a lower-order basis is not a free route to higher order.** Several attempted `r=2 → r>=3` transfers fail because extra coordinates create too much representation mass or leave the basis property uncontrolled.
4. **Block/digit additivity is sensitive to seam carries.** Source attacks found explicit boundary terms that invalidate naive decomposition of representation energy across digital blocks.
5. **The natural finite optimization already rejects simple greedy behavior.** At the first nontrivial window above, the greedy core is not energy-minimizing.

These are negative mathematical assets: they remove large classes of plausible but invalid proof architectures.

## Source campaign

The full provenance remains public at

`jaredwilder/erdos-campaign-archive/campaigns/erdos1192-campaign-001/`.

That raw package contains approximately:

- 155 KB campaign log;
- 156 KB results file;
- 501 KB transcript;
- 54 KB route registry;
- transfer-evidence record;
- frozen contract.

The raw route statuses should **not** be read as theorem authority by themselves. The campaign repeatedly corrected its own `PROVED`, `FALSE`, and boundary labels. This human extraction promotes only statements that survive direct mathematical reading or exact finite enumeration at the stated scope.

## Current frontier

The unrestricted problem remains open in this release. The surviving load-bearing task is constructive: for each `r>=2`, produce one explicit or rigorously existing asymptotic basis `A_r` together with a proof that its ordered representation energy is linear in `x`.

The program has crossed standalone-repository scale. Until a dedicated `erdos1192` repository shell exists, this directory is the preferred human subject surface; the campaign archive is provenance.
