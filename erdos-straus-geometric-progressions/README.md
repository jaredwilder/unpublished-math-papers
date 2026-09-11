# Erdős–Straus solutions with denominators in geometric progression

**Author:** Jared Wilder  
**Release:** September 2026

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

where `g>=1`, `0<a<b`, and `gcd(a,b)=1`. Put

\[
D=a^2+ab+b^2.
\]

## Theorem

All positive ordered GP-denominator solutions, and only those solutions, are

\[
x=tDa^2,\qquad y=tDab,\qquad z=tDb^2,\qquad n=4ta^2b^2
\]

for uniquely determined coprime integers `0<a<b` and `t>=1`.

In particular, no primitive denominator triple exists.

## Proof

The reciprocal sum is

\[
\frac1{ga^2}+\frac1{gab}+\frac1{gb^2}=\frac{a^2+ab+b^2}{ga^2b^2}=\frac{D}{ga^2b^2}.
\]

Hence the Erdős–Straus identity is equivalent to

\[
nD=4ga^2b^2.
\]

Because `gcd(a,b)=1`, one has `gcd(D,a)=gcd(D,b)=1`. Also `D` is odd: if exactly one of `a,b` is even the claim is immediate, while if both are odd then `D` is a sum of three odd terms. Thus

\[
\gcd(D,4a^2b^2)=1.
\]

Therefore `D|g`; writing `g=tD` gives `n=4ta²b²` and the displayed parameterization. Conversely, substitution verifies the identity. Primitive GP normalization uniquely recovers `g,a,b`, and then `t=g/D`, proving uniqueness. Since `D>=3`, every denominator triple has nontrivial common gcd.

## Independent verification

The independent exact-arithmetic verifier imports no MathFire implementation code. Its sealed regression campaign checked:

- **73,064** coprime parameter pairs;
- **292,256** constructed solutions;
- **292,256** reverse parameter recoveries;
- the gcd lemma;
- minimal scale;
- sampled if-and-only-if reconstruction.

The universal theorem is the symbolic argument above; the finite sweep is independent regression evidence, not a finite-to-infinite inference.

This classifies only the geometric-progression-denominator subfamily. It does **not** prove the full Erdős–Straus conjecture.
