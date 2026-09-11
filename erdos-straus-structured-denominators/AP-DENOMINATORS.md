# Erdős–Straus solutions with arithmetic-progression denominators

**Author:** Jared Wilder  
**Source:** MathFire 8.0.0, Round Eight  
**Status:** symbolic all-parameter theorem with independent finite replay  
**Novelty posture:** `apparently_new_after_systematic_search` as of 2026-07-27; this is not a claim of absolute historical novelty.

## Theorem

Let positive integers

\[
x<y<z
\]

form an arithmetic progression and satisfy

\[
\frac4n=\frac1x+\frac1y+\frac1z.
\]

Write uniquely

\[
(x,y,z)=g(a-d,a,a+d),
\]

with coprime integers

\[
a>d>0.
\]

Set

\[
D=3a^2-d^2.
\]

Then exactly one of the following parity branches applies:

- if `a,d` have opposite parity,
  \[
  g=tD,
  \qquad
  n=4ta(a^2-d^2),
  \]
  for a unique integer `t≥1`;
- if `a,d` are both odd,
  \[
  g=\frac{tD}{2},
  \qquad
  n=2ta(a^2-d^2),
  \]
  for a unique integer `t≥1`.

Conversely, every choice of coprime `a>d>0` and `t≥1` in the appropriate parity branch gives a positive-integer Erdős–Straus solution with strict arithmetic-progression denominators.

The parameterization is unique.

### Corollary

No strict arithmetic-progression Erdős–Straus denominator triple is primitive:

\[
\gcd(x,y,z)>1.
\]

## Proof

The reciprocal sum is

\[
\frac1{g(a-d)}+\frac1{ga}+\frac1{g(a+d)}
=
\frac{3a^2-d^2}{ga(a^2-d^2)}.
\]

Thus integrality of `n` is equivalent to

\[
D\mid 4ga(a^2-d^2).
\]

Coprimality gives

\[
\gcd(D,a)=1.
\]

Also

\[
D-3(a^2-d^2)=2d^2,
\]

and `gcd(D,d)=1`, so

\[
\gcd(D,a^2-d^2)\mid2.
\]

In fact the exact gcd is

\[
\gcd(D,4a(a^2-d^2))=
\begin{cases}
1,& a,d\text{ of opposite parity},\\
2,& a,d\text{ both odd}.
\end{cases}
\]

Therefore the least possible scale of `g` is respectively `D` or `D/2`, and every valid scale is a positive multiple of that minimum. Substitution gives the displayed formulas for `n`.

The reduced AP parameters are recovered from

\[
g=\gcd(x,y,z),
\qquad
a=y/g,
\qquad
d=(z-y)/g,
\]

which proves uniqueness.

## Independent replay

The independent verifier `erdos_straus_ap_independent.py` was recorded as importing no MathFire package code and checking:

- the reciprocal-sum identity;
- the gcd/parity lemma;
- minimal scale;
- construction;
- parameter recovery;
- **76,115** coprime parameter pairs;
- **456,690** constructed solutions.

The universal authority comes from the symbolic proof above, not from the finite replay.

## Prior-art boundary recorded by the campaign

The 2026-07-27 search examined exact formulas/phrases and nearby literature, including Elsholtz–Tao on general Erdős–Straus solution counts and Jianu–Popescu on Egyptian fractions with arithmetic-progression denominators. No equivalent exact three-term `4/n` classification, parity split, uniqueness theorem, or primitive-triple corollary was located.

That search cannot exclude unpublished, inaccessible, obscure, or poorly indexed prior work. A later collision changes the novelty label, not the mathematical proof.
