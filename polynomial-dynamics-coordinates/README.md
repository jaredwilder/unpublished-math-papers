# Polynomial dynamics coordinate identities and finite closure principles

**Author:** Jared Wilder  
**Source campaign date:** 2026-08  
**Public extraction:** 2026-09-11

This directory extracts the **standalone mathematics** from a larger representation/search research packet. System architecture, learned-search hypotheses, routing logic and product-specific machinery are intentionally omitted. The source itself explicitly states that no item is asserted globally novel; several results are elementary or standard. This release preserves that boundary.

## 1. Multiplicative shadow of the recurrence `x_{n+1}=x_n^2-x_n+1`

Let

`x_{n+1}=x_n^2-x_n+1`.

Then for every `n>=1`,

`x_{n+1}-1 = (x_1-1) prod_{j=1}^n x_j`.

Indeed, `x_{n+1}-1=x_n(x_n-1)`, and induction telescopes the factorization.

Consequently, for `i<j`, `x_i | (x_j-1)`, so the orbit terms are pairwise coprime. For seed `x_1=2`,

`x_{n+1}=1+prod_{j=1}^n x_j`,

with initial terms `2,3,7,43,1807,3263443,...`.

## 2. General telescoping-transform principle

Let `x_{n+1}=f(x_n)`. If functions `T,A` satisfy

`T(f(x))=A(x)T(x)`

on the orbit domain, then

`T(x_n)=T(x_1) prod_{j=1}^{n-1} A(x_j)`.

This is simply iteration of the one-step multiplicative-coordinate identity.

## 3. Fixed-point coordinates

Let `K` be a field, `f in K[x]`, and let `c` be a fixed point: `f(c)=c`. Then

`x-c | f(x)-c`.

Hence there is `A_c in K[x]` with

`f(x)-c=(x-c)A_c(x)`.

Thus every polynomial fixed point produces a multiplicatively evolving coordinate `T_c(x)=x-c`.

## 4. Finite forward-invariant-set coordinates

Let `S={c_1,...,c_r}` be a finite set of distinct field elements satisfying `f(S) subseteq S`, and define

`T_S(x)=prod_{c in S}(x-c)`.

Every `c in S` is a root of `T_S(f(x))`, hence

`T_S(x) | T_S(f(x))`.

So

`T_S(f(x))=A_S(x)T_S(x)`

for some polynomial `A_S`.

## 5. Universal periodic coordinate

Let `R` be a commutative ring, `f in R[x]`, and `k>=1`. Define

`T_k(x)=f^{∘k}(x)-x`.

Then

`T_k(x) | T_k(f(x))`.

Proof: `u-v | f(u)-f(v)` over any commutative coefficient ring. Substitute `u=f^{∘k}(x)` and `v=x`.

Therefore every iterate period produces an automatically generated multiplicative coordinate.

## 6. Explicit difference-quotient cofactor

For

`f(z)=sum_{m=0}^d a_m z^m`,

one has

`(f(u)-f(v))/(u-v) = sum_{m=1}^d a_m sum_{ell=0}^{m-1} u^{m-1-ell} v^ell`.

Combined with the periodic-coordinate theorem, this gives an explicit cofactor in the identity `T_k(f(x))=A_k(x)T_k(x)`.

## 7. Valuation linearization

Whenever integer/rational quantities satisfy

`T(x_{n+1})=A(x_n)T(x_n)`

and the relevant `p`-adic valuations are defined,

`v_p(T(x_{n+1}))=v_p(T(x_n))+v_p(A(x_n))`,

and therefore

`v_p(T(x_n))=v_p(T(x_1))+sum_{j=1}^{n-1}v_p(A(x_j))`.

A multiplicative coordinate thus becomes additive after valuation.

## 8. Finite-dictionary invariant-subspace closure

Let `V` be an `N`-dimensional vector space of functions over a field, and let the pullback operator be

`U_f(T)=T∘f`.

Define

`V_0=V`,

`V_{n+1}={T in V_n : U_f(T) in V_n}`.

The descending chain stabilizes after at most `N` strict dimension drops. At stabilization `V_infty`,

`U_f(V_infty) subseteq V_infty`,

and `V_infty` is the largest `U_f`-invariant subspace contained in `V`.

This is an exact terminal result **inside the declared finite dictionary**.

## 9. Residual-lift closure

Let `V_0` be a seed function space and define

`V_{n+1}=V_n+U_f(V_n)`.

Then

`V_n = span(V_0,U_f(V_0),...,U_f^n(V_0))`.

If `V_{r+1}=V_r`, then `V_r` is `U_f`-invariant and is the smallest invariant subspace containing `V_0`.

Thus finite-dimensional pullback closure is discoverable by repeated residual lifting.

## 10. Finite operation reconstruction

Let `X` be finite and `R subseteq X^3` satisfy

`for all a,b in X, there exists a unique c in X with R(a,b,c)`.

Then `R` defines a unique binary operation `star:X×X->X` by

`a star b=c iff R(a,b,c)`.

Associativity, identity, inverses, commutativity, idempotence and any other finite first-order table law are decidable by exhaustive checking.

## 11. Finite congruence / quotient decidability

For a finite operation table `(X,star)`, a proposed equivalence relation `~` is a congruence exactly when

`a~a' and b~b' => a star b ~ a' star b'`.

When this holds, `star` descends to a well-defined operation on `X/~`. Exhaustive partition enumeration is finite, although generally expensive.

## 12. Syndrome-separator bound

Let `S` contain `N` distinct syndromes and let `P` be binary probes such that every pair of syndromes is separated by at least one probe. Then some subfamily of at most

`N-1`

probes separates all syndromes.

Proof: begin with one partition block containing all syndromes. Each chosen separating probe strictly refines at least one nonsingleton block, increasing the number of nonempty blocks by at least one. Starting from one block, at most `N-1` refinements are required to reach `N` singleton blocks.

A logarithmic bound requires an additional balanced-separator hypothesis and is **not** asserted here.

## Authority boundary

These statements were marked `EXACT` or `ALGORITHMIC` in the source ledger. Publication here does not assert historical novelty, Lean formalization, or relevance to any particular application. The source's system-level theorems and research hypotheses were deliberately excluded from this public extraction.