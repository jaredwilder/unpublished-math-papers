# Erdős #973 — exact two-point golden-ratio extremum

**Author:** Jared Wilder  
**Recovered from:** September 2026 theorem audit  
**Public extraction:** 2026-09-11

## Exact theorem

After the usual normalization `z_1=1`, the `n=2` minimax problem is

\[
\inf_{|z|\ge1}\max\bigl(|1+z^2|,|1+z^3|\bigr).
\]

Its exact value is

\[
\boxed{
\inf_{|z|\ge1}\max\bigl(|1+z^2|,|1+z^3|\bigr)
=\frac{\sqrt5-1}{2}
=2\cos\frac{2\pi}{5}.
}
\]

The optimum is attained at

\[
z=e^{\pm2\pi i/5}.
\]

## Proof capsule

The recovered analytic proof first reduces radially to `|z|=1`. Writing

\[
z=e^{2iu}
\]

gives

\[
|1+z^2|=2|\cos 2u|,
\qquad
|1+z^3|=2|\cos 3u|.
\]

Hence the problem is

\[
2\min_u\max(|\cos2u|,|\cos3u|).
\]

At the optimum the two active terms balance. The balance occurs at `u=π/5`, equivalently
`z=e^{2πi/5}`, and

\[
2|\cos(2\pi/5)|=\frac{\sqrt5-1}{2}.
\]

The campaign separately checked the witness in exact algebra and recorded the one-dimensional lower
bound / equalization argument as the symbolic optimality proof.

## Consequence for the historical parent formulation

Any historical universal constant `C` whose formulation would require the `n=2` value to exceed
`C^{-2}` is constrained by this exact slice; in the campaign normalization this gives the stated
golden-ratio obstruction `C<sqrt(phi)` (with `phi=(1+sqrt(5))/2`).

This is only an exact finite-dimensional extremum. It does not by itself decide the parent problem.
The parent problem was reported in the 2026 audit as subsequently solved negatively by external work,
so this result is preserved as a standalone exact calculation rather than marketed as the current
frontier.

## Novelty boundary

Targeted searches of the two 2026 parent-solution lines inspected during the audit did not locate an
explicit `n=2` / golden-ratio evaluation. The estate therefore classifies this as a **plausibly
original exact finite extremum**, not a global historical-priority certificate.

## License

Apache-2.0 for repository-authored material.
