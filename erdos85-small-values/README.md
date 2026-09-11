# Erdős #85 — exact small values `f(5)=f(6)=f(7)=3`

**Author:** Jared Wilder  
**Release date:** 2026-09-11  
**Evidence class:** elementary proof + exhaustive finite regression  
**Novelty:** not claimed. These values are likely implicit in the classical `R(C4,K_{1,n})` literature; the purpose of this extraction is to make the exact #85 consequence explicit and reproducible.

## Problem

Let `f(n)` be the least integer `d` such that every graph on `n` vertices with minimum degree at least `d` contains a 4-cycle `C4`.

The current Erdős #85 page records `f(4)=2` and asks whether `f(n+1)>=f(n)` for all sufficiently large `n`.

The Day-One MSL ore contained the exact claims `f(5)=f(6)=3`. Rechecking the argument exposes a one-line extension to `n=7`.

## Theorem

For `n=5,6,7`,

`f(n)=3`.

### Lower bound

For each `n=5,6,7`, the cycle graph `C_n` is `C4`-free and has minimum degree `2`.

Therefore `f(n)>=3`.

### Upper bound

Let `G` be a `C4`-free graph and fix a vertex `v`.

For distinct `u,w in N(v)`, the sets

`N(u) \ {v}` and `N(w) \ {v}`

are disjoint. Indeed, a common vertex `x` would give the 4-cycle

`v-u-x-w-v`.

Hence

`sum_{u in N(v)} (deg(u)-1) <= n-1`.

If `delta(G)>=3`, then every summand is at least `2`, so

`2 deg(v) <= n-1`.

For `n=5` or `6`, this contradicts `deg(v)>=3` immediately.

For `n=7`, it gives `deg(v)<=3`. Since `delta(G)>=3`, every vertex must therefore have degree exactly `3`. But a 3-regular graph on 7 vertices cannot exist, because the degree sum would be `7*3=21`, contradicting the handshake lemma.

Thus every graph on 5, 6, or 7 vertices with minimum degree at least 3 contains a `C4`, proving `f(n)<=3`.

Combining both directions gives

`f(5)=f(6)=f(7)=3`.

## Relation to the Ramsey literature

Erdős #85 notes the relation with the star-vs-quadrilateral Ramsey numbers `R(C4,K_{1,n})`, whose small values are classical and tabulated in OEIS A006672. This release does not assert historical priority for the three values. It isolates the consequence directly in the `f(n)` language of #85 and gives a self-contained proof.

## Reproduce

Run:

```bash
python verify.py
```

The verifier independently enumerates every labeled graph on 4, 5, 6, and 7 vertices and confirms

```text
f(4)=2
f(5)=3
f(6)=3
f(7)=3
```

The proof above, not the finite enumeration, is the mathematical certificate for the three released values.

## External pointers

- Erdős #85: https://www.erdosproblems.com/85
- Related Ramsey problem #552: https://www.erdosproblems.com/552
- OEIS A006672: https://oeis.org/A006672

## License

Apache-2.0.
