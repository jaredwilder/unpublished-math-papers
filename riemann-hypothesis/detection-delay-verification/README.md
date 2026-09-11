# Verification addendum — determinant detection delay

This directory attaches independent computational checks to the determinant/total-positivity research lane documented in the parent `riemann-hypothesis/` directory.

It was previously published inside the mixed repository `detection-delay-and-a-problem-bridge`, alongside unrelated Erdős #890/#1093 material. The verification belongs here with the zeta-function program.

## Mathematical statement being checked

If exactly one conjugate pair has angular defect `theta` while the remaining zero parameters are positive real, the released Schur-phase argument gives

\[
r|\theta|<\pi/2
\quad\Longrightarrow\quad
D_{r,k}>0
\quad\text{for every }k.
\]

Thus any rectangular Toeplitz minor capable of detecting that pair must have order at least

\[
r\ge \frac{\pi}{2|\theta|}.
\]

As the angular defect tends to zero, the required detection order diverges.

The broader program also records the universal bilinear harmonic mode `L(rk)=0`, the reciprocal nonlinear heat equation, a rectangular-Schur representation in the positive-real-zero phase, and the occupancy bound that no single zero parameter carries more than `1/k` of the normalized logarithmic sensitivity.

## What the verifier checks

`verify_encirclement_v.py` performs six algebraic/combinatorial checks:

1. the reciprocal heat PDE identity;
2. the bilinear harmonic identity;
3. a concrete nonreversible positive-factor example;
4. positivity of several dual-Jacobi–Trudi rectangular determinants;
5. a numerical single-pair phase-budget example;
6. the tableau occupancy cap by exhaustive enumeration on a `2 x 3` rectangle.

The recorded run reports `6/6 PASS`.

## Scope

These checks validate pieces of the released machinery. They do **not** prove the Riemann Hypothesis and do not prove the program's unproved global collision-angle/no-escape condition.

The parent `riemann-hypothesis/README.md` remains the human overview. This directory is evidence, not a competing research program.
