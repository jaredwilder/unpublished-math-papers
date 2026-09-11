# Erdős #68 — exact geometric-series reformulation

**Author:** Jared Wilder  
**Public extraction:** 2026-09-11

For every integer `n>=2`,

\[
\boxed{
\frac1{n!-1}=\sum_{j=1}^{\infty}(n!)^{-j}.
}
\]

## Proof

Put `x=n!>1`. Then

\[
\sum_{j=1}^{\infty}x^{-j}
=\frac{x^{-1}}{1-x^{-1}}
=\frac1{x-1}.
\]

Therefore the claimed identity follows with `x=n!`.

For every finite truncation at `J`, the remainder is exactly

\[
\boxed{
\frac{x^{-(J+1)}}{1-x^{-1}}>0.
}
\]

Thus the reformulation has an explicit positive geometric tail at every stage.

## Scope

This is an exact reformulation only. It does not prove the irrationality statement in the surrounding parent problem.
