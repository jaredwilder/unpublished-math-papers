# Round Ten Novel Result I

## Complete classification of geometric-progression Erdős–Straus solutions

Consider positive integers

\[
0<x<y<z,\qquad y^2=xz,
\]

satisfying

\[
\frac4n=\frac1x+\frac1y+\frac1z.
\]

Every positive integral geometric progression has a unique primitive normalization

\[
(x,y,z)=g(a^2,ab,b^2),
\]

where `g >= 1`, `0 < a < b`, and `gcd(a,b)=1`. Set

\[
D=a^2+ab+b^2.
\]

## Theorem

All positive ordered geometric-progression-denominator solutions of the Erdős–Straus equation, and only those solutions, are

\[
\boxed{x=tDa^2,\quad y=tDab,\quad z=tDb^2,\quad n=4ta^2b^2}
\]

for uniquely determined integers

\[
0<a<b,\qquad \gcd(a,b)=1,\qquad t\ge1.
\]

In particular, no primitive denominator triple exists.

## Proof

The normalized reciprocal sum is

\[
\frac1{ga^2}+\frac1{gab}+\frac1{gb^2}
=\frac{a^2+ab+b^2}{ga^2b^2}
=\frac{D}{ga^2b^2}.
\]

Therefore the Erdős–Straus identity is equivalent to `nD=4ga²b²`. Because `gcd(a,b)=1`, one has `gcd(D,a)=gcd(D,b)=1`; and `D` is odd, so `gcd(D,4a²b²)=1`. Hence `D | g`. Write `g=tD`, giving `n=4ta²b²`. Conversely the displayed formulas substitute directly. The primitive GP normalization uniquely recovers `g,a,b`, then `t=g/D`.

## Independent verification

`verification/erdos_straus_gp_independent.py` imports no MathFire package code and independently checks primitive parameter recovery, the reciprocal identity, the gcd/divisibility lemma, minimal scale, forward construction, and reverse recovery. Its sealed campaign covers 73,064 coprime parameter pairs and 292,256 constructed solutions.

## Authority boundary

This theorem classifies the geometric-progression-denominator subfamily. It does not prove the full Erdős–Straus conjecture.