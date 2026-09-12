# Fixed-slope determinant-curvature profile — repaired state and full finite data

**Author:** Jared Wilder  
**Source run:** 2026-09-11 MSL RH session export

This note repairs two state-graph artifacts in the original live ledger and collects the full fixed-slope computation in one place.

## 1. Exact curvature equivalence

Let

\[
Q_{r,k}=\frac{D_{r,k-1}D_{r,k+1}}{D_{r,k}^2}
\]

and

\[
Z_{r,k}=\frac rk\frac{D_{r,k-1}D_{r,k+1}}{D_{r+1,k}D_{r-1,k}}.
\]

Desnanot–Jacobi gives

\[
D_{r+1,k}D_{r-1,k}=D_{r,k}^2-D_{r,k-1}D_{r,k+1},
\]

so exactly

\[
\boxed{Z_{r,k}=\frac rk\frac{Q_{r,k}}{1-Q_{r,k}}.}
\]

On a fixed slope `k = m r`,

\[
\boxed{Z=\frac1m\frac{Q}{1-Q}.}
\]

Therefore, whenever a fixed-slope limit exists,

\[
Z\to A>0
\iff
Q\to \frac{mA}{1+mA}\in(0,1),
\]

while

\[
Z\to0\iff Q\to0.
\]

This equivalence was marked `stale_dependency` in the original state only because the node cited an earlier extrapolation that was later retracted. The derivation above uses only the exact determinant identity and is independent of that extrapolation.

## 2. Deep `theta=1/2` slice

At `k=r`, with 200-digit coefficient arithmetic and a determinant benchmark calibration better than `2.1e-183`, the run obtained:

| r | Z |
|---:|---:|
| 1 | 0.869801285242 |
| 2 | 0.777223604021 |
| 3 | 0.716345770890 |
| 4 | 0.674925854890 |
| 5 | 0.644725478343 |
| 6 | 0.621418611423 |
| 7 | 0.602701457161 |
| 8 | 0.587226521954 |
| 9 | 0.574141814642 |
| 10 | 0.562879339895 |
| 11 | 0.553044500500 |
| 12 | 0.544353451035 |
| 13 | 0.536595972757 |
| 14 | 0.529612550073 |
| 15 | 0.523279629195 |
| 16 | 0.517499800199 |
| 17 | 0.512195068714 |
| 18 | 0.507302132082 |
| 19 | 0.502768990797 |
| 20 | 0.498552470444 |
| 21 | 0.494616378023 |
| 22 | 0.490930109029 |

The last three orders were recomputed with the determinant arithmetic raised from 200 to 320 digits and printed zero difference at the reported precision.

### Tail-model comparison on `r=12..22`

Positive-limit model:

\[
Z(r)=A+Br^{-p}
\]

fit:

\[
A=0.278934,\qquad B=0.666993,\qquad p=0.370821,
\]

with maximum residual

\[
3.03\times10^{-6}.
\]

Zero-limit model:

\[
Z(r)=Br^{-p}
\]

had maximum residual

\[
5.13\times10^{-4}.
\]

Thus, on this finite tail, the zero-limit model's maximum residual is about **169 times larger**.

Nested positive-limit fits starting at `r=6,8,10,12,14` returned

`0.268740, 0.274093, 0.277077, 0.278934, 0.280172`,

while the maximum residual decreased from `8.18e-05` to `9.07e-07`.

## 3. Multi-ratio profile

The completed ratio run used `k=m r`, `theta=m/(m+1)`.

| theta | order depth | fitted A | fitted p | positive-limit max residual | zero-limit max residual | ratio |
|---:|---:|---:|---:|---:|---:|---:|
| 1/2 | 22 | 0.278934 | 0.370821 | 3.03e-06 | 5.13e-04 | 169.0 |
| 2/3 | 14 | 0.397941 | 0.345180 | 2.25e-06 | 3.58e-04 | 158.9 |
| 3/4 | 11 | 0.444954 | 0.338330 | 2.73e-06 | 3.72e-04 | 136.6 |
| 4/5 | 8 | 0.469390 | 0.334268 | 1.09e-06 | 2.14e-04 | 197.3 |
| 5/6 | 7 | 0.484707 | 0.332146 | 1.76e-06 | 3.03e-04 | 172.6 |

The first three slices have six or more tail points and were used by the source run as the adequately supported comparison set. The last two have only four tail points each and are retained here as raw finite evidence rather than promoted to the same inferential status.

Across the displayed fits, the approach exponent decreases toward approximately `1/3` as `theta` increases. That pattern is a numerical observation, not an asymptotic theorem.

## 4. Benchmark calibration

For the exact factorial benchmark orbit, the same implementation should return `Z=1`.

The completed run reported:

- `theta=1/2`, `r=20`: `|Zbench-1| = 2.012e-183`;
- `theta=2/3`, `r=14`: `2.258e-184`;
- `theta=3/4`, `r=10`: `3.212e-188`;
- `theta=4/5`, `r=8`: `1.040e-190`;
- `theta=5/6`, `r=6`: `2.369e-193`.

The worst displayed benchmark deviation was `2.012e-183`.

## 5. State repair

Two source nodes were mechanically marked stale by dependency propagation:

- the exact curvature-equivalence node;
- a later computation-supported positive-profile node.

The first is rebuilt above from the exact identity alone. The second is rebuilt directly from the completed W37 computation. Neither requires the earlier retracted small-order extrapolation.

The mathematical distinction is therefore:

- **exact:** the `Z <-> Q` reparameterization;
- **computed:** the displayed finite fixed-slope values and model comparisons;
- **open:** existence and uniform positivity of the asymptotic profile across the full ratio interval.
