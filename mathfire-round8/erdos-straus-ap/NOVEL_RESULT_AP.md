# Result A — Erdős–Straus solutions with AP denominators

## Theorem

Let positive integers `x<y<z` form an arithmetic progression and satisfy

\[
\frac4n=\frac1x+\frac1y+\frac1z.
\]

Write uniquely

\[
(x,y,z)=g(a-d,a,a+d),
\]

with coprime integers `a>d>0`. Set `D=3a²-d²`.

- If `a,d` have opposite parity, then `g=tD` and `n=4ta(a²-d²)`.
- If `a,d` are both odd, then `g=tD/2` and `n=2ta(a²-d²)`.

Conversely, every such choice of coprime `a>d>0` and `t≥1` gives a solution. The parameterization is unique. No primitive denominator triple (`gcd(x,y,z)=1`) occurs.

## Proof

The reciprocal sum is

\[
\frac1{g(a-d)}+\frac1{ga}+\frac1{g(a+d)}
=\frac{3a^2-d^2}{ga(a^2-d^2)}.
\]

Thus integrality of `n` is equivalent to

\[
D\mid 4ga(a^2-d^2).
\]

Coprimality gives `gcd(D,a)=1`. Also

\[
D-3(a^2-d^2)=2d^2,
\]

and `gcd(D,d)=1`, so `gcd(D,a²-d²)` divides 2. The exact gcd

\[
\gcd(D,4a(a^2-d^2))
\]

is 1 for opposite parity and 2 for odd–odd parity. Hence the least possible scale is `D` or `D/2`, and every scale is a positive multiple thereof. Substitution gives the displayed formula for `n`.

The reduced AP parameters are recovered from `g=gcd(x,y,z)`, `a=y/g`, and `d=(z-y)/g`, proving uniqueness.

## Independent replay

`verification/erdos_straus_ap_independent.py` imports no MathFire package code and checks the identities, gcd lemma, minimal scale, construction, and recovery over 76,115 coprime parameter pairs and 456,690 solutions.