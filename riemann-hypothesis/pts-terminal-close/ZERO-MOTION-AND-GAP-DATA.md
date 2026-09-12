# Zero motion under the de Bruijn–Newman heat flow — exact local law and recovered finite data

**Author:** Jared Wilder  
**Recovered from:** session export `session-export-04e7fd63-20260911-102113.zip`

This note separates an exact zero-velocity identity from the finite low-zero measurements that completed in the background log after the live state had stopped consuming results.

## 1. Exact simple-zero velocity law

Let `x_i(t)` be a simple real zero of `H_t`:

\[
H_t(x_i(t))=0.
\]

Differentiating in `t` gives

\[
\partial_t H_t(x_i)+H_x(x_i)x_i'(t)=0.
\]

Using the heat equation

\[
\partial_tH_t=-H_{xx},
\]

one obtains the exact local identity

\[
\boxed{
x_i'(t)=\frac{H_{xx}}{H_x}(t,x_i(t)).
}
\]

This identity is independent of any Hadamard-product representation.

## 2. Even-product coordinate

Suppose in addition that an even entire function at the fixed time has the product

\[
H(x)=H(0)\prod_{j\ge1}\left(1-\frac{x^2}{\gamma_j^2}\right)
\]

with simple positive zeros `gamma_j`. At `x=gamma_i`, the same velocity ratio becomes

\[
\boxed{
\frac{H''(\gamma_i)}{H'(\gamma_i)}
=
\frac1{\gamma_i}
+4\gamma_i\sum_{j\ne i}\frac1{\gamma_i^2-\gamma_j^2}.
}
\]

Equivalently,

\[
\frac{H''(\gamma_i)}{H'(\gamma_i)}
=
2\left[
\frac1{2\gamma_i}
+
\sum_{j\ne i}
\left(
\frac1{\gamma_i-\gamma_j}
+
\frac1{\gamma_i+\gamma_j}
\right)
\right].
\]

### Lowest-zero sign criterion

For the lowest positive zero `gamma_1`,

\[
\boxed{
x_1'(t)<0
\iff
\sum_{j\ge2}\frac1{\gamma_j^2-\gamma_1^2}
>
\frac1{4\gamma_1^2}.
}
\]

This is the correct exact sign criterion.

The live state had promoted the negativity of the lowest-zero velocity too early: every `j>=2` pair contribution is negative, but the partner term `1/gamma_1` is positive, so the sign still requires the displayed tail inequality. The finite measurements below support negativity in the tested case but do not replace that analytic condition.

## 3. Direct velocity cross-check at `t=0.2`

For the first two positive zeros, the session independently compared:

1. velocity obtained by relocating the zero at neighboring time values; and
2. `H_xx/H_x` from direct quadrature.

The agreement was:

- zero near `28.1536122884`: velocity `-0.57874858`, relative disagreement `1.38e-10`;
- zero near `41.8933808577`: velocity `-0.75199593`, relative disagreement `9.43e-10`.

Thus the local heat-flow velocity identity is numerically confirmed to roughly ten significant figures at those two zeros.

## 4. Recovered seven-row low-zero geometry

The background log completed all seven requested time values even though the state ledger consumed only the first five.

| t | lowest positive zero | second positive zero | gap |
|---:|---:|---:|---:|
| 0.2 | 28.1536 | 41.8934 | 13.73977 |
| 0.1 | 28.2115 | 41.9687 | 13.75715 |
| 0.05 | 28.2405 | 42.0063 | 13.76587 |
| 0.02 | 28.2579 | 42.0290 | 13.77112 |
| 0.01 | 28.2637 | 42.0365 | 13.77288 |
| 0.005 | 28.2666 | 42.0403 | 13.77375 |
| 0 | 28.2695 | 42.0441 | 13.77463 |

Across this finite sample, the lowest gap **increases monotonically as `t` decreases from `0.2` to `0`**.

This directly corrects the earlier qualitative expectation that the lowest pair should contract under downward time flow.

## 5. Truncated even-product velocity test

The same background computation evaluated the even-product velocity sum at `t=0.2` using truncated zero lists.

With positive zeros below `60`:

- first zero: product prediction `-0.147820`, measured `-0.578749`;
- second zero: product prediction `-0.029884`, measured `-0.751996`.

With positive zeros below `92`:

- first zero: product prediction `-0.277964`, measured `-0.578749`;
- second zero: product prediction `-0.288717`, measured `-0.751996`.

The truncated prediction moves toward the measured negative velocity as more zeros are included, but the omitted tail remains quantitatively important at these cutoffs.

## 6. Mathematical status

Exact:

- `x_i'(t)=H_xx/H_x` at every simple zero;
- the even-product reciprocal-distance formula under the stated product hypothesis;
- the displayed lowest-zero sign criterion.

Computed:

- the two direct velocity cross-checks at `t=0.2`;
- the seven-row low-zero table;
- the two finite truncation comparisons.

The low-zero table is finite evidence about the observed trajectory, not a global theorem about all zeros or all positive times.
