# Erdős #77 — proved/conditional ledger P01–P18

Status labels are load-bearing.

## P01. Thin-Corridor Ramsey Inequality
**Status:** PROVED-IN-SESSION

For integers `n>a>=0`,

`r(n-a,n) <= R(n) <= 4^a r(n-a,n)`.

## P02. Thin-Corridor Equivalence (TCE)
**Status:** PROVED-IN-SESSION

If `a_n=o(n)`, then

`(1/n) log R(n) - (1/n) log r(n-a_n,n) -> 0`.

Hence diagonal and sublinear-corridor sequences have the same exponential limsup and liminf; convergence on any one sublinear corridor is equivalent to convergence on the diagonal.

## P03. Inverse Homogeneous-Set Formulation
**Status:** PROVED-IN-SESSION

Define

`h(N)=min_{|V(G)|=N} max{omega(G),alpha(G)}`.

Then `R(k)>N iff h(N)<k`. For `L>1`,

`R(k)^(1/k) -> L iff h(N)/log N -> 1/log L`.

## P04. Clone Saturation Lemma
**Status:** PROVED-IN-SESSION

Let `G` be a red/blue colouring of `K_{R(k)-1}` with no monochromatic `K_k`. Every vertex lies in a red `K_{k-1}` and in a blue `K_{k-1}`. Equivalently each red neighborhood contains a red `K_{k-2}` and each blue neighborhood contains a blue `K_{k-2}`.

## P05. Weighted Wrong-Pair Inequality
**Status:** PROVED-IN-SESSION

Let `G` have clique number at most `a`. Give vertices nonnegative loads `s_i<=b`, put `t=sum_i s_i`, and let `B` be the weighted sum over nonedges. Then

`B >= t(t-ab)/(2a)`.

## P06. Summable Composition Error Accumulation
**Status:** PROVED-IN-SESSION

Suppose a binary operation on witnesses multiplies vertex counts and satisfies

`m(X*Y) <= m(X)+m(Y)+C(m(X)+m(Y))/log^2(m(X)+m(Y))`

for sufficiently large inputs. Starting from `q` identical witnesses of parameter `K`, the `q`-fold product can be parenthesized so that

`M_q <= qK exp(O(1/log K)) = qK(1+O(1/log K))`

uniformly in `q>=1`.

## P07. Approximate Supermultiplicativity Implies Existence
**Status:** CHECKABLE-CONDITIONAL

Put `A(k)=R(k)-1`. Assume there are constants `C,k0` such that for all `m,n>=k0` there is an integer

`0 <= E(m,n) <= C(m+n)/log^2(m+n)`

with

`A(m+n+E(m,n)) >= A(m)A(n)`.

Then `lim_{k->infty} R(k)^(1/k)` exists.

## P08. Complementary Off-Diagonal Amplification
**Status:** CHECKABLE-CONDITIONAL

Assume a composition theorem combines a witness for `r(s,Cs)` and its colour-swapped copy with multiplicative vertex count and `o(s)` loss in both forbidden parameters. If

`r(s,Cs) >= B(C)^(s+o(s))`,

then

`liminf R(k)^(1/k) >= B(C)^(2/(1+C))`.

## P09. Bradač-Input Optimization Constant
**Status:** PROVED-IN-SESSION algebra; RAMSEY CONCLUSION CONDITIONAL on P08

Using the external fixed-ratio input `r(s,Cs)>=2^((1-1/(2C))s)`, P08 gives exponent

`f(C)=(2-1/C)/(1+C)`.

The unique maximizer is `C*=(1+sqrt(3))/2`, with

`f(C*)=4-2sqrt(3)=0.535898...`,

so the conditional diagonal base is `2^(4-2sqrt(3))=1.449844... > sqrt(2)`.

## P10. Explicit Binary Nonedge-Polarity Digraph and Size Ratio
**Status:** PROVED-IN-SESSION

For `p>=1`, define `D_p` by

`V(D_p)={(a,b) in (F_2^p\{0})^2 : a.b=1}`

and arc `(a,b)->(a',b') iff a.b'=0`.

Then `D_p` is loopless, `T_{p+1}`-free, has exactly

`|D_p|=(2^p-1)2^(p-1)`,

and consequently

`|D_{p1+p2+1}|/(|D_{p1}||D_{p2}|) -> 8`.

## P11. Tagged Direct-Sum / XOR Identity
**Status:** PROVED-IN-SESSION

For factor vertices `(a1,b1) in D_{p1}`, `(a2,b2) in D_{p2}`, define

`A=(a1,a2,1)`, `B=(b1,b2,1)`.

Then `A.B=1`, and if `e_i(x,y)` is the factor arc bit, the product arc bit satisfies

`e(x,y)=e_1(x,y) XOR e_2(x,y)`.

## P12. Exact Pattern-Collision Identity for XOR Product
**Status:** PROVED-IN-SESSION

For an ordered `t`-tuple `X`, let `F_X` be its upper-triangular arc pattern, and let `c_D(F)` count ordered tuples with pattern `F`. Then

`I_t(D_1 tensor D_2)=sum_F c_{D_1}(F)c_{D_2}(F)`,

where `I_t` counts ordered forward-independent `t`-tuples in the XOR product.

## P13. Pattern Collision Implies Triangular Orthogonality
**Status:** PROVED-IN-SESSION

If two factor tuples have the same arc pattern, then for `i<j`,

`a_i.b_j = a_i'.b_j'`.

With doubled vectors `A_i=(a_i,a_i')` and `B_j=(b_j,b_j')`, one gets

`A_i.B_j=0` for `i<j`.

## P14. Exact Tensor-Flag Rank Formula
**Status:** PROVED-IN-SESSION — TERMINAL ALGEBRA ASSET

Let `L_1 subseteq ... subseteq L_t subseteq U` be a nested flag and `b_1,...,b_t in W`. Choose a basis `e_1,...,e_d` of `L_t` adapted to the flag and let `tau_r=min{j:e_r in L_j}`. Then

`dim(sum_j L_j tensor <b_j>) = sum_r dim span{b_j:j>=tau_r}`.

## P15. Mixed Bilinear Product Theorem
**Status:** PROVED-IN-SESSION algebraically

Let factor vertices satisfy `a_i.b_i=1` in dimensions `p1,p2`. Put `u=(a1,a2)`, `v=(b1,b2)`, choose

`Q=[[I,M],[N,I]]`,

and define `u_hat=(u,1)`, `v_hat=(v,1+u^TQv)`. On dimension `d=p1+p2+1`, use the bilinear form

`B_tilde((u,t),(v,z))=u^TQv+tz`.

Then `B_tilde(u_hat,v_hat)=1` for every product vertex, the Cartesian-product map is injective, and the digraph with arc `x->y iff B_tilde(u_hat_x,v_hat_y)=0` is `T_{p1+p2+2}`-free.

## P16. One-Sided Mixer Affine Equations
**Status:** PROVED-IN-SESSION

Set `N=0` in P15 and retain only `M`. For an ordered product tuple `x_1,...,x_t`, forward-independence requires, for every `i<j`,

`(a_{1i}+a_{1j})^T M b_{2j} = a_{1i}.b_{1j}+a_{2i}.b_{2j}`.

The coefficient tensor is `(a_{1i}+a_{1j}) tensor b_{2j}`.

## P17. Exact Mixer Rank via Affine Prefix Flags
**Status:** PROVED-IN-SESSION

For P16 define

`L_j=span{a_{1i}+a_{1j}:i<j}`.

These are the direction spaces of the affine hulls of the prefixes. The span of all mixer coefficient tensors is `sum_j L_j tensor <b_{2j}>`. Thus P14 gives

`R_M(X)=sum_r rank{b_{2j}:j>=tau_r}`.

If `d_j=dim L_j` and `rho_j=rank{b_{2l}:l>=j}`, then for every `j`,

`R_M(X)>=d_j rho_j`.

## P18. Rank-Weighted Mixer First Moment
**Status:** PROVED-IN-SESSION

Let mixer entries be independent uniform bits. For each injective ordered candidate tuple `X`, let `R(X)` be the rank of its affine mixer system. If inconsistent, survival probability is zero; if consistent,

`Pr[X survives]=2^(-R(X))`.

Hence

`E_M I_t(M) <= sum_X 2^(-R(X))`.

After random permutation the expected number of independent `t`-sets is at most `(1/t!) sum_X 2^(-R(X))`. If vertices are then retained independently with probability `theta`, the expected surviving count is at most `(theta^t/t!) sum_X 2^(-R(X))`.

The realistic terminal inequality must include any sampling/permutation factors used by the construction; requiring the raw sum itself to be below one is only a strong sufficient condition, not the correct general target.
