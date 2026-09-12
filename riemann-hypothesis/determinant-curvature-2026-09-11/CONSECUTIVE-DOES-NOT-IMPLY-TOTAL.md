# Consecutive Toeplitz positivity does not imply total positivity

## Theorem

For the finite coefficient sequence

\[
a=(1,0,0,0,0,1),
\]

all tested consecutive Toeplitz minors are nonnegative, but a non-consecutive Toeplitz minor is negative.

In particular, for rows \(\{0,1\}\) and columns \(\{1,5\}\),

\[
\det\begin{pmatrix}
a_1 & a_5\\
a_0 & a_4
\end{pmatrix}
=a_1a_4-a_5a_0=-1.
\]

Therefore

\[
\boxed{\text{consecutive-minor nonnegativity does not imply total positivity}.}
\]

The generating polynomial is

\[
G(z)=1+z^5,
\]

which has non-real zeros as expected.

## Why it matters

A historical RH route in this project had silently compressed the implication

\[
\text{consecutive minors positive}
\Longrightarrow
\text{total positivity}
\Longrightarrow
\text{real negative zeros}.
\]

The first arrow is false. Classical PF/ASW/Edrei theorems require total positivity of the full Toeplitz matrix, not merely the consecutive sublattice studied by the campaign.

This counterexample is independent of the later Branch C sufficiency refutation; it kills an earlier bridge even before one asks whether the specific lattice criterion characterizes real-rootedness.

## Reproducibility

The recovered exhaustive integer-box search found six counterexamples almost immediately. The first six were:

- `(1,0,0,0,0,1)` with minor `-1`;
- `(1,0,0,0,0,2)` with minor `-2`;
- `(1,0,0,0,0,3)` with minor `-3`;
- `(1,0,0,0,0,4)` with minor `-4`;
- `(1,0,0,0,0,6)` with minor `-6`;
- `(1,0,0,0,1,0)` with a non-consecutive minor `-1`.

The exact search script is published as `verify_consecutive_not_total.py`.