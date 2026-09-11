"""A(theta): the limit of the normalized odds variable across compactified ratios.

Attacks RD1 / the ratio-uniformity gap with the methodology validated at theta = 1/2:
tail-window power-law fit, held-out prediction, nested-window stability, and an
in-run benchmark calibration against the kernel-verified orbit identity.

Coefficients are CACHED to disk so later rounds never recompute them.
"""
import json
import os
from mpmath import mp, mpf, exp, pi, quad, factorial, matrix, det
import numpy as np
from scipy.optimize import curve_fit

COEF_DPS = 200
KMAX = 46
PANELS = [0, 0.4, 0.8, 1.2, 1.6, 2.0, 2.6]
CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "coeffs_dps200_k46.json")

mp.dps = COEF_DPS


def Phi(u):
    s = mpf(0)
    for n in range(1, 26):
        n2 = mpf(n) ** 2
        s += (2 * pi ** 2 * n2 ** 2 * exp(9 * u) - 3 * pi * n2 * exp(5 * u)) * exp(-pi * n2 * exp(4 * u))
    return s


if os.path.exists(CACHE):
    print("loading cached coefficients from %s" % CACHE, flush=True)
    a = [mpf(s) for s in json.load(open(CACHE))]
    print("loaded %d coefficients" % len(a), flush=True)
else:
    print("computing %d coefficient moments at dps=%d ..." % (KMAX, COEF_DPS), flush=True)
    a = []
    for k in range(KMAX):
        a.append(quad(lambda u: u ** (2 * k) * Phi(u), PANELS) / factorial(2 * k))
        if k % 8 == 0:
            print("   a[%d] done" % k, flush=True)
    json.dump([mp.nstr(v, 210) for v in a], open(CACHE, "w"))
    print("coefficients computed and cached", flush=True)

bench = [mpf(1) / factorial(k) for k in range(KMAX)]


def D(c, r, k):
    if r == 0:
        return mpf(1)
    M = matrix(r, r)
    for i in range(r):
        for j in range(r):
            idx = k + j - i
            M[i, j] = c[idx] if 0 <= idx < len(c) else mpf(0)
    return det(M)


def Z(c, r, k):
    den = D(c, r + 1, k) * D(c, r - 1, k)
    if den == 0:
        return None
    return (mpf(r) / k) * (D(c, r, k - 1) * D(c, r, k + 1) / den)


def m3(rr, A, B, p):
    return A + B * rr ** (-p)


def m2(rr, B, p):
    return B * rr ** (-p)


print(flush=True)
print("CALIBRATION: benchmark orbit must return Z == 1 on every slice used below", flush=True)
worst = 0.0
for (m, r) in ((1, 20), (2, 14), (3, 10), (4, 8), (5, 6)):
    k = m * r
    if k + r + 1 >= KMAX:
        continue
    d = float(abs(Z(bench, r, k) - 1))
    worst = max(worst, d)
    print("   m=%d r=%2d k=%2d  |Zbench-1| = %.3e" % (m, r, k, d), flush=True)
print("   WORST = %.3e" % worst, flush=True)

print(flush=True)
print("A(theta) ACROSS RATIOS   k = m r,  theta = m/(m+1)", flush=True)
results = {}
for m in (1, 2, 3, 4, 5):
    theta = m / (m + 1.0)
    rs, zs = [], []
    r = 1
    while True:
        k = m * r
        if k + r + 1 >= KMAX:
            break
        z = Z(a, r, k)
        if z is None:
            break
        rs.append(float(r))
        zs.append(float(z))
        r += 1
    if len(rs) < 6:
        print("   theta=%.4f  only %d orders, skipped" % (theta, len(rs)), flush=True)
        continue
    R = np.array(rs)
    ZZ = np.array(zs)
    cut = len(rs) // 2
    tail = R >= R[cut]
    out = {}
    for f, p0, lab in ((m3, [0.28, 0.67, 0.37], "pos"), (m2, [0.83, 0.17], "zero")):
        po, _ = curve_fit(f, R[tail], ZZ[tail], p0=p0, maxfev=800000)
        res = ZZ[tail] - f(R[tail], *po)
        out[lab] = (po, float(max(abs(res))))
    A, B, p = out["pos"][0]
    print("   theta=%.4f  orders 1..%d  tail r>=%d (n=%d)" % (theta, int(R[-1]), int(R[cut]), int(tail.sum())), flush=True)
    print("       Z(last) = %.8f" % zs[-1], flush=True)
    print("       positive-limit  A=%.6f  B=%.6f  p=%.6f   max|res|=%.2e" % (A, B, p, out["pos"][1]), flush=True)
    print("       zero-limit                        p=%.6f   max|res|=%.2e" % (out["zero"][0][1], out["zero"][1]), flush=True)
    print("       selection ratio (zero/pos residual) = %.1f" % (out["zero"][1] / out["pos"][1]), flush=True)
    results[theta] = (A, p, out["zero"][1] / out["pos"][1], int(R[-1]))
    print(flush=True)

print("SUMMARY  theta -> fitted limit A, exponent p, selection ratio, depth", flush=True)
for th in sorted(results):
    A, p, sel, depth = results[th]
    print("   %.4f   A=%.6f   p=%.6f   sel=%.1f   orders=%d" % (th, A, p, sel, depth), flush=True)
print(flush=True)
print("DONE", flush=True)
