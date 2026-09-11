# Erdős–Straus solutions with denominators in arithmetic progression

**Author:** Jared Wilder  
**Release:** September 2026

This directory records a complete parameterization of the positive-integer solutions of

\[
\frac4n=\frac1x+\frac1y+\frac1z
\]

under the additional condition that `x < y < z` are in arithmetic progression.

## The theorem

Let `a>d>0` be coprime integers and `t>=1`. Put

\[
D=3a^2-d^2.
\]

If `a,d` have opposite parity, set `q=D`; if both are odd, set `q=D/2`. Then

\[
(x,y,z)=tq(a-d,a,a+d).
\]

The corresponding `n` is

\[
n=4ta(a^2-d^2)
\]

in the opposite-parity case and

\[
n=2ta(a^2-d^2)
\]

in the odd–odd case.

Conversely, every positive solution whose three denominators form a strict arithmetic progression is obtained uniquely in this way after reducing the progression to coprime center/difference parameters. In particular, no such denominator triple is primitive: `gcd(x,y,z)>1`.

## Derivation

Write an arithmetic progression as

\[
(x,y,z)=g(a-d,a,a+d),\qquad \gcd(a,d)=1.
\]

Then

\[
\frac1{x}+\frac1y+\frac1z
=\frac{3a^2-d^2}{ga(a^2-d^2)}.
\]

Thus

\[
n=\frac{4ga(a^2-d^2)}{3a^2-d^2}.
\]

For coprime `a,d`, `gcd(3a^2-d^2,a)=1`, while

\[
\gcd(3a^2-d^2,a^2-d^2)=
\begin{cases}
1,&a,d\text{ of opposite parity},\\
2,&a,d\text{ both odd}.
\end{cases}
\]

The required divisibility therefore forces the minimal scale `g=D` in the opposite-parity case and `g=D/2` in the odd–odd case. Writing `g=tq` gives the displayed formulas. Dividing any progression by its common gcd recovers `(a,d)`, after which the scale recovers `t`, giving uniqueness.

## Verification and scope

`verify_ap.py` is an independent exact-arithmetic regression verifier. It imports no MathFire code and checks 76,115 coprime parameter pairs with `a<=500`, 456,690 constructed solutions, the gcd/parity lemma, minimal scale, parameter recovery and absence of primitive triples on that validation range.

The theorem is the symbolic all-parameter derivation above. The finite sweep is independent regression evidence, not a finite-to-infinite substitute.

A July 27, 2026 systematic search found no equivalent statement in the searched literature. `NOVELTY.md` preserves the qualified prior-art status; a later collision would alter only that novelty label, not the mathematics.
