# Erdős #377 — corrected large-prime Kummer interval criterion

**Author:** Jared Wilder  
**Public extraction:** 2026-09-11

## Theorem

Let `p<=n` be prime and assume

\[
\boxed{p>\sqrt{2n}}.
\]

Put

\[
k=\left\lfloor\frac np\right\rfloor.
\]

Then

\[
\boxed{
p\nmid {2n\choose n}
\iff
p>\frac{2n}{2k+1}.
}
\]

## Proof

Because `2n<p^2`, the base-`p` expansion of `n` has at most two digits. Write

\[
n=kp+r,\qquad0\le r<p.
\]

By Kummer's theorem, `p` divides the central binomial coefficient exactly when adding `n+n` in base `p` produces a carry. Under `2n<p^2`, the only possible carry comes from the low digit, so

\[
p\nmid {2n\choose n}
\iff 2r<p.
\]

Substituting `r=n-kp`,

\[
2(n-kp)<p
\iff
2n<(2k+1)p
\iff
p>\frac{2n}{2k+1}.
\]

## Correction record

A historical registry version omitted the hypothesis `p>sqrt(2n)`. That unrestricted version is false because higher base-`p` digits can create additional carries. The theorem above is the corrected scope.
