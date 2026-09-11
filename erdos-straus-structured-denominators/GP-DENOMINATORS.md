# Erdős–Straus solutions with geometric-progression denominators

**Author:** Jared Wilder  
**Source:** MathFire Round Ten  
**Status:** symbolic all-parameter theorem with independent finite replay  
**Novelty posture:** `apparently_new_after_systematic_search` as of 2026-07-27; absolute historical novelty is not claimed.

## Theorem

Let positive integers

\[
0<x<y<z,
\qquad y^2=xz,
\]

satisfy

\[
\frac4n=\frac1x+\frac1y+\frac1z.
\]

Every positive integral geometric progression has a unique primitive normalization

\[
(x,y,z)=g(a^2,ab,b^2),
\]

where

\[
g\ge1,\qquad 0<a<b,\qquad \gcd(a,b)=1.
\]

Set

\[
D=a^2+ab+b^2.
\]

Then all positive ordered geometric-progression-denominator solutions, and only those solutions, are

\[
\boxed{
 x=tDa^2,
 \quad y=tDab,
 \quad z=tDb^2,
 \quad n=4ta^2b^2
}
\]

for uniquely determined integers

\[
0<a<b,\qquad \gcd(a,b)=1,\qquad t\ge1.
\]

In particular, no primitive denominator triple exists.

## Proof

The normalized reciprocal sum is

\[
\frac1{ga^2}+rac1{gab}+rac1{gb^2}
=
\frac{a^2+ab+b^2}{ga^2b^2}
=
\frac{D}{ga^2b^2}.
\]

Therefore the Erdős–Straus identity is equivalent to

\[
nD=4ga^2b^2.
\]

Because `gcd(a,b)=1`,

\[
\gcd(D,a)=\gcd(b^2,a)=1,
\qquad
\gcd(D,b)=\gcd(a^2,b)=1.
\]

Also `D` is odd. If one of `a,b` is even, the other is odd; if both are odd, `D` is the sum of three odd integers. Thus

\[
\gcd(D,4a^2b^2)=1.
\]

Hence `D|g`. Write `g=tD`; then necessarily

\[
n=4ta^2b^2.
\]

Conversely, substituting the displayed formulas gives

\[
\frac1x+\frac1y+\frac1z
=
\frac{D}{tDa^2b^2}
=
\frac1{ta^2b^2}
=
\frac4{4ta^2b^2}
=
\frac4n.
\]

The primitive GP normalization uniquely recovers `g,a,b`, and then `t=g/D`, proving uniqueness. Since `D≥3`, every solution has common denominator gcd at least three.

## Independent verification

The independent verifier `verification/erdos_straus_gp_independent.py` was recorded as sharing no MathFire package code. The sealed campaign checked:

- primitive parameter recovery;
- the reciprocal identity;
- `gcd(D,4a²b²)=1`;
- minimality of `g=D`;
- forward construction;
- reverse recovery;
- **73,064** coprime parameter pairs;
- **292,256** constructed solutions.

A separate earlier replay recorded **76,115** coprime pairs, **380,575** constructed solutions, and a bounded exhaustion of **122,962** strict integral GP triples. These computations support the symbolic proof; they are not the source of its universal authority.

## Claim boundary

This theorem classifies only the geometric-progression denominator subfamily. It does not prove the full Erdős–Straus conjecture.
