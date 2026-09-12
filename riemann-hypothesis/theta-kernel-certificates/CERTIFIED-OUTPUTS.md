# Certificate outputs recovered from the 2026-09-12 export

These are the terminal numerical intervals printed by the exported exact-rational certificate programs.

## `certify_first_rung.py`

- `A_0 in [0.122695423796950240, 0.123520930027222045]`
- `A_2 in [0.019627019535230553, 0.019871962530565775]`
- `A_4 in [0.009502788367715110, 0.009647585933581126]`
- `B_0 in [0.014631979695418750, 0.014711873377158603]`
- `B_2 in [0.001698512064802113, 0.001718261285851078]`
- `B_4 in [0.000671933974798517, 0.000681508967975423]`

and

`P(3) in [1.487365741170569e-06, 8.824883179857477e-05]`.

The exported run concludes `P(3)>0`.

## `certify_full_kernel.py`

- `I_0 in [0.2477225997132910, 0.2493989671244238]`
- `I_2 in [0.0457009591900428, 0.0461872448158320]`
- `I_4 in [0.0235433319892390, 0.0238625728791416]`

and

`3 I_2^2 - I_0 I_4 in [3.144319836807e-04, 5.675693447454e-04]`.

## `certify_four_rungs.py`

- `k=1: [1.56335252e-03, 1.96426203e-03]`
- `k=2: [1.73415563e-03, 2.24619876e-03]`
- `k=3: [2.72502080e-03, 3.63976614e-03]`
- `k=4: [5.87924581e-03, 8.13406217e-03]`

The exported run states that series remainder and truncation tail are included in every enclosure.

## `certify_curvature.py`

The threshold test is certified at

`m = 2,4,6,8,10,12,16,24`.

The rational thresholds are

`(m-1)/(4(m+1)) = 1/12, 3/20, 5/28, 7/36, 9/44, 11/52, 15/68, 23/100`.

At every listed index the stationarity left side at that threshold is strictly less than `m+1`.

## `certify_tail.py`

- tail upper bound at `u=0`: `1.101398903229127086e-03`
- first theta term lower bound: `0.445726971317994769`
- `Phi(0)` lower bound: `0.444625572414765635`
- certified relative tail: `2.477138004562849053e-03 < 1/300`.

## Gaussian-normalized moment row

For

\[
J_k=I_{2k}/\Gamma(k+1/2),
\]

the exported finite ratios

\[
J_{k+1}J_{k-1}/J_k^2
\]

for `k=1,...,9` are approximately

`0.9303676, 0.9409607, 0.9484936, 0.9541525, 0.9585775, 0.9621443, 0.9650886, 0.9675657, 0.9696824`.

The algebraic equivalence between the weighted moment row and log-concavity of `J_k` is exact; these nine ratios are finite numerical observations.