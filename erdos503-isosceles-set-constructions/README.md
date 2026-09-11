# Erdős #503 — exact one-dimensional value and a quadratic simplex-midpoint construction

**Author:** Jared Wilder  
**Recovered from:** September 2026 estate synthesis  
**Public extraction:** 2026-09-11

Let `f(d)` denote the largest size of a finite point set in `R^d` for which every triple of distinct points determines an isosceles triangle, under the frozen campaign convention.

This packet records two unconditional results: the exact one-dimensional value and a quadratic construction in every dimension `d>=2`.

## Theorem 1 — exact one-dimensional value

For every line,

\[
\boxed{f(1)=3.}
\]

Three equally spaced points give the lower bound.

For the upper bound, suppose four distinct real points are ordered

\[
a_1<a_2<a_3<a_4.
\]

For each interior point `a_i`, the triple `(a_1,a_i,a_4)` has the unique largest possible side `a_4-a_1`. For that triple to be isosceles, the other two sides must be equal, forcing

\[
a_i-a_1=a_4-a_i,
\]

so

\[
a_i=(a_1+a_4)/2.
\]

Both `a_2` and `a_3` are therefore forced to the same midpoint, contradicting distinctness. Hence four points are impossible.

## Theorem 2 — quadratic lower bound for every `d>=2`

For every integer `d>=2`,

\[
\boxed{f(d)\ge {d+1\choose2}+1.}
\]

### Construction

Take a centered regular `d`-simplex with vertices

\[
u_1,\ldots,u_{d+1}
\]

and include all edge midpoints

\[
m_{ij}=\frac{u_i+u_j}{2},
\qquad 1\le i<j\le d+1.
\]

There are exactly

\[
{d+1\choose2}
\]

such midpoints. Add the simplex center `0`.

### Why every triple is isosceles

For two distinct edge midpoints, their distance depends only on whether the corresponding simplex edges share a vertex or are disjoint. Thus the midpoint set is a **two-distance set**.

Every triangle whose three side lengths are drawn from only two possible values is necessarily isosceles. Therefore every triple consisting solely of edge midpoints is isosceles.

All edge midpoints lie at the same distance from the simplex center. Hence any triple containing the center and two midpoints has two equal center-to-midpoint sides and is also isosceles.

Therefore the midpoint set together with the center has

\[
{d+1\choose2}+1
\]

points and satisfies the required property.

## Two-dimensional note

The same estate contains the separate six-point regular-pentagon-plus-center witness, giving

\[
f(2)\ge6,
\]

which is stronger than the simplex-midpoint formula's value 4 at `d=2`.

## Scope / provenance boundary

The one-dimensional theorem is exact. The simplex-midpoint result is a lower-bound construction only; no matching general upper bound is claimed. The construction emerged in the estate synthesis by combining route fragments and was explicitly kept separate from unsupported exact-value conjectures.

No historical novelty claim is made without a specialist geometry search.

## License

Apache-2.0 for repository-authored material.
