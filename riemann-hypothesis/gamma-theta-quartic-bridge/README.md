# Gamma–theta quartic bridge and exact dispersion

**Author:** Jared Wilder  
**Recovered from live RH campaign result W131:** 2026-09-11

The live campaign observed numerically that the “gamma-variable” route and the first theta-term route were the same object in different coordinates. The relation is exact and elementary.

## Exact coordinate identity

Let

`f(x) = C exp(-pi x^4)`,  `x > 0`,

with normalization

`C = 4 pi^(1/4) / Gamma(1/4)`.

Set

`y = pi x^4`.

Then

`dx = (1/4) pi^(-1/4) y^(-3/4) dy`,

and therefore

`f(x) dx = y^(1/4-1) exp(-y) / Gamma(1/4) dy`.

Thus the quartic theta density is exactly the pullback of a `Gamma(1/4,1)` density.

The constant seen numerically in W131,

`1.3313353638...`,

is exactly

`pi^(1/4) = 1.3313353638003897127...`.

So the two calculations are not merely compatible: they are the same integral in different coordinates.

## Exact moments

For every `q > -1`,

`int_0^infinity x^q exp(-pi x^4) dx = (1/4) pi^(-(q+1)/4) Gamma((q+1)/4)`.

After normalization,

`E[X^q] = pi^(-q/4) Gamma((q+1)/4) / Gamma(1/4)`.

In particular,

`E[X^2] = pi^(-1/2) Gamma(3/4) / Gamma(1/4)`,

and, using `Gamma(5/4)=(1/4)Gamma(1/4)`,

`E[X^4] = 1/(4 pi)`.

Hence the normalized dispersion of `X^2` is exactly

`Disp(X^2) := Var(X^2) / E[X^2]^2`

`= E[X^4]/E[X^2]^2 - 1`

`= Gamma(1/4)^2 / (4 Gamma(3/4)^2) - 1`

`= 1.1884396152264766388367699407...`.

Therefore the quartic theta density satisfies the campaign threshold

`Disp(X^2) < 2`

with a substantial exact margin.

## Why log concavity alone is not the theorem

The campaign also tested whether ordinary log concavity by itself could force the dispersion threshold. It cannot.

For the one-parameter family

`f_p(x) proportional to exp(-pi x^p)` on `x>0`,

the same calculation gives

`Disp_p(X^2) = Gamma(5/p) Gamma(1/p) / Gamma(3/p)^2 - 1`.

Three exact checkpoints are:

- `p=1`: `Disp = 5`;
- `p=2`: `Disp = 2`;
- `p=4`: `Disp = Gamma(1/4)^2/(4 Gamma(3/4)^2)-1 = 1.188439615...`.

Thus a log-concave exponential density can miss the target badly, the Gaussian is exactly on the threshold, and the quartic density lies safely below it.

So the reusable structure is not “log concavity” alone. The first theta-term route carries a quantitatively stronger quartic/super-Gaussian moment profile.

## Concavity is global, not a grid observation

For the quartic density,

`log f(x) = constant - pi x^4`,

so

`(log f)''(x) = -12 pi x^2 <= 0`,

strictly for every `x>0`.

The 25-point numerical log-concavity check in W131 is therefore replaceable by this exact global identity.

## Mathematical significance of W131

The live campaign had been carrying a gamma-variable computation and a theta-kernel computation as if they were two analytic routes. W131 closes that duplication: at this first-term level they are one object under `y=pi x^4`.

It also sharpens the first dispersion rung from a qualitative shape question into a closed-form moment inequality. Any extension from the first theta term to the full kernel should preserve this exact coordinate bridge rather than restart from generic log-concavity estimates.
