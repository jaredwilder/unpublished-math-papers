# Order-one curvature corridor from the published xi coefficient bound

**Author of this corollary:** Jared Wilder  
**External input:** W. Michalowski, *An explicit uniform cubic wedge for consecutive Toeplitz minors of the Riemann xi coefficients*, arXiv:2607.16795, Lemma 2.1.  
**Public extraction:** 2026-09-11

## Statement

Let `(a_k)` be the positive coefficient sequence of

`G(z) = (1/8) xi(1/2 + sqrt(z)/2) = sum_{k>=0} a_k z^k`,

and define

`q_k = a_{k-1} a_{k+1} / a_k^2`,

`tau_k = -log q_k`.

For the normalized determinant-curvature variable

`Z_{r,k} = (r/k) * D_{r,k-1}D_{r,k+1}/(D_{r+1,k}D_{r-1,k})`,

the order-one values satisfy, for every integer `k>=2`,

`1 / [k (exp(4/k)-1)]  <  Z_{1,k}  <  1 / [k (exp(1/(2k))-1)]`.

Consequently

`liminf_{k->infinity} Z_{1,k} >= 1/4`

and

`limsup_{k->infinity} Z_{1,k} <= 2`.

In particular the order-one normalized curvature is rigorously bounded away from zero asymptotically.

## Proof

For determinant order `r=1`,

`D_{1,k}=a_k`.

Hence the shift curvature is exactly

`Q_{1,k}=D_{1,k-1}D_{1,k+1}/D_{1,k}^2=q_k=e^{-tau_k}`.

The exact Desnanot–Jacobi reparameterization established in this directory gives

`Z_{1,k} = (1/k) * Q_{1,k}/(1-Q_{1,k})`

and therefore

`Z_{1,k} = 1 / [k (exp(tau_k)-1)]`.

Michalowski's Lemma 2.1 gives, for every `k>=2`,

`1/(2k) < tau_k < 4/k`.

The map

`x -> 1/(exp(x)-1)`

is strictly decreasing on the positive reals. Substitution therefore yields

`1 / [k (exp(4/k)-1)] < Z_{1,k} < 1 / [k (exp(1/(2k))-1)]`.

Finally, for fixed positive `c`,

`k (exp(c/k)-1) -> c`,

so the lower and upper comparison functions tend respectively to `1/4` and `2`. QED.

## Authority / novelty classification

This is a **derived corollary**, not an independent claim that the curvature window itself is new here. The external ingredient is the published/arXiv curvature window. The transformation from that window to the displayed `Z_{1,k}` corridor is elementary and uses the exact determinant identity in this release.

No statement about general determinant order `r>1` is imported from Lemma 2.1. The result is an order-one anchor only; the fixed-slope `r,k -> infinity` problem remains separate.
