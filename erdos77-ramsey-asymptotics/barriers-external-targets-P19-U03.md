# Erdős #77 — barriers, external feedstock, and live obligations P19–U03

Status labels are load-bearing. Diagnostics are not universal impossibility theorems; external results are feedstock, not re-proved here.

## P19. Uniform-Rank First-Moment Barrier
**Status:** DIAGNOSTIC — exact bookkeeping, not a universal impossibility theorem

Suppose a proof only uses `N^t` candidate ordered tuples with `N=2^(beta t+o(t))`, and at most one independent binary equation per unordered pair, so `R(X)<=binom(t,2)`. Then the strongest raw estimate `N^t 2^(-binom(t,2))` has exponent `(beta-1/2)t^2+o(t^2)`. Thus this raw-count + uniform-rank architecture cannot close for `beta>1/2`.

At the Bradač-complementary optimum `beta=4-2sqrt(3)`, the missing structural entropy dividend is at least `7/2-2sqrt(3)=0.035898...` at quadratic scale.

## P20. Two-Cross-Matrix Bit Ceiling
**Status:** DIAGNOSTIC

For `p1~t/(1+C)`, `p2~Ct/(1+C)`, two cross matrices contain asymptotically `2C/(1+C)^2 t^2` bits. At `C*=(1+sqrt(3))/2`, this coefficient is `0.4880338717...`, versus target candidate exponent `0.5358983848...`; the difference is `0.0478645131...`. This is an information-budget diagnostic only.

## P21. Full Mixed-Product Fiber Obstruction
**Status:** PROVED-IN-SESSION — TERMINAL FALSIFICATION ASSET

Consider the full Cartesian product `D_{p1} x D_{p2}` under P15. Fix `v=(b1,b2)` with `b_i != 0`. The fiber contains all `u=(a1,a2)` satisfying `a_i.b_i=1`, so `|F_v|=2^(p1+p2-2)`. Partition it by the bit `c(u)=u^T Q v`.

Any two vertices in the same class have no arc in either direction. Therefore every fiber contains an edgeless class of size at least `2^(p1+p2-3)`.

Moreover any induced subset `S` whose resulting graph has independence number below `t` must have at most `t-1` vertices in each of the two classes for each fixed `v`. Hence

`|S| <= 2(t-1)(2^p1-1)(2^p2-1)`.

Thus the full mixed Cartesian polarity product cannot preserve a subexponential fraction of all product vertices while forcing independence below `t`. Any viable use must control coordinates sparsely or strengthen the operator enough to destroy these fibers.

## P22. Perfect Matching in the Valid-Pair Incidence Graph
**Status:** PROVED-IN-SESSION

Let `H_p` be the bipartite graph with both sides `F_2^p\{0}` and `a~b iff a.b=1`. Then `H_p` is `2^(p-1)`-regular on both sides and therefore has a perfect matching. Equivalently there exists a bijection

`pi:F_2^p\{0} -> F_2^p\{0}`

such that `a.pi(a)=1` for every `a!=0`.

## P23. Matching-Restricted Polarity Digraph
**Status:** PROVED-IN-SESSION

Let `pi` be any bijection from P22. Define a digraph `D_pi` on `F_2^p\{0}` by

`a -> a' iff a.pi(a')=0`.

Then `D_pi` is loopless and `T_{p+1}`-free. It has exactly `2^p-1` vertices and, unlike the full pair construction, has no repeated `a`- or `b`-coordinate fibers.

## X01–X07. External feedstock
**Status:** EXTERNAL

The session ledger separately records contemporary off-diagonal and diagonal Ramsey inputs used as feedstock, including fixed-`s`, far off-diagonal, fixed-ratio and near-diagonal lower bounds; a fixed-ratio exponential improvement; a Gaussian refinement; and current diagonal upper-bound feedstock. These are external literature inputs and are not claimed as original theorems of this estate.

## U01. Coordinate-Controlled Rank-Distribution / Container Theorem
**Status:** OPEN OBLIGATION

For a sparse factor family with coordinate multiplicities already controlled, prove a weighted bound of the form

`(theta^t/t!) sum_{X in B_t} 2^(-R(X)) << 1`

(or the stronger deletion inequality needed to retain the desired number of vertices), where `R(X)` is given by P17/P18 and `theta=2^(-o(t))` if the composition is to preserve exponential vertex count.

P21 means this theorem cannot hold for the unrestricted full Cartesian polarity product at exponent-preserving density.

## U02. Fiber-Free Correlated Composition Operator
**Status:** OPEN OBLIGATION

Construct an additive-dimension product that mixes enough of both coordinates to eliminate P21-type fibers while preserving:

1. injectivity / near-multiplicative vertex count;
2. diagonal nonorthogonality;
3. `T_{s1+s2+o(s1+s2)}`-freeness;
4. a rank/container estimate with only summably sublinear parameter loss.

P22–P23 provide one fiber-free algebraic search space, but no independent-set theorem was proved.

## U03. Matching-Polarity Ramsey Bound
**Status:** OPEN OBLIGATION

Determine whether one can choose `pi` in P22 so that `D_pi`, after an appropriate ordering/sampling step, has dramatically fewer large forward-independent tuples than a generic/random-like construction. No such bound was proved in the campaign.
