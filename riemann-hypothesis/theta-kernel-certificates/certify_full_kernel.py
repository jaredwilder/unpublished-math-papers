"""Exact-rational enclosure for the full Riemann Xi theta kernel first moment inequality."""
from fractions import Fraction as F

D = 10 ** 35
def dn(q):
    r = F(q).limit_denominator(D); return r if r <= q else r - F(1, D)
def up(q):
    r = F(q).limit_denominator(D); return r if r >= q else r + F(1, D)

def arctan_inv(k, m=30):
    s = F(0); lo = hi = None
    for n in range(m):
        s += F((-1) ** n, (2 * n + 1) * k ** (2 * n + 1))
        if n % 2 == 0: hi = s
        else: lo = s
    return lo, hi

a5l, a5h = arctan_inv(5); a2l, a2h = arctan_inv(239)
PI_LO, PI_HI = dn(4 * (4 * a5l - a2h)), up(4 * (4 * a5h - a2l))

def exp_br(z):
    n = max(25, int(2 * float(z)) + 22)
    S = F(0); term = F(1)
    for k in range(n + 1):
        S = up(S + term); term = up(term * z / (k + 1))
    assert z < n + 2
    return dn(S - term), up(S + up(term / (1 - z / (n + 2))))

def exp_neg_br(z):
    lo, hi = exp_br(z); return dn(F(1) / hi), up(F(1) / lo)

EC = {}
def e_br(z):
    if z not in EC: EC[z] = exp_br(z)
    return EC[z]
DC = {}
def damp_br(x, n2):
    key = (x, n2)
    if key not in DC:
        ex = e_br(x)
        DC[key] = (exp_neg_br(up(PI_HI * n2 * ex[1]))[0], exp_neg_br(dn(PI_LO * n2 * ex[0]))[1])
    return DC[key]

X = F(5, 2); N = 5000; H = X / N; NMAX = 2
def iadd(u, v): return (u[0]+v[0], u[1]+v[1])
def isub(u, v): return (u[0]-v[1], u[1]-v[0])
def imul(u, v):
    p = [u[0]*v[0], u[0]*v[1], u[1]*v[0], u[1]*v[1]]; return (min(p), max(p))
def isc(c, u): return (c*u[0], c*u[1]) if c >= 0 else (c*u[1], c*u[0])

def cell(a, b, j, n):
    n2 = n * n; n4 = n2 * n2
    da, db = damp_br(a, n2), damp_br(b, n2)
    g9a, g9b = e_br(F(9, 4) * a), e_br(F(9, 4) * b)
    g5a, g5b = e_br(F(5, 4) * a), e_br(F(5, 4) * b)
    plo = dn(a ** j * 2 * PI_LO * PI_LO * n4 * g9a[0] * db[0])
    phi_ = up(b ** j * 2 * PI_HI * PI_HI * n4 * g9b[1] * da[1])
    mlo = dn(a ** j * 3 * PI_LO * n2 * g5a[0] * db[0])
    mhi = up(b ** j * 3 * PI_HI * n2 * g5b[1] * da[1])
    return isub((plo, phi_), (mlo, mhi))

def series_rem(j):
    tot = F(0)
    for n in range(NMAX + 1, NMAX + 10):
        n2 = n * n; n4 = n2 * n2
        tot = up(tot + up(2 * PI_HI * PI_HI * n4 * e_br(F(9, 4) * X)[1]
                          * exp_neg_br(dn(PI_LO * n2))[1] * X * (X ** j + 1)))
    return tot

def tail(j):
    U = e_br(X)[0]
    return up(2 * PI_HI * PI_HI * U ** (F(9, 4) + j) * exp_neg_br(dn(PI_LO * U))[1]
              * F(1) / (PI_LO - (F(9, 4) + j) / U))

print("X=%s N=%d NMAX=%d  pi width %.2e" % (X, N, NMAX, float(PI_HI - PI_LO)), flush=True)
EN = {}
for j in (0, 2, 4):
    tot = (F(0), F(0))
    for i in range(1, N + 1):
        b = i * H; a = b - H
        c = (F(0), F(0))
        for n in range(1, NMAX + 1): c = iadd(c, cell(a, b, j, n))
        tot = iadd(tot, (H * c[0], H * c[1]))
    sr = series_rem(j); tl = tail(j)
    lo = dn(tot[0] - sr - tl); hi = up(tot[1] + sr + tl)
    EN[j] = (lo, hi)
    m = (lo + hi) / 2
    print("   I_%d in [%.16f, %.16f]  rel width %.3e  (srem %.2e tail %.2e)" % (j, float(lo), float(hi), float((hi - lo) / m), float(sr), float(tl)), flush=True)

lhs = imul(EN[0], EN[4]); rhs = isc(F(3), imul(EN[2], EN[2])); d = isub(rhs, lhs)
print("\n   3 I_2^2 - I_0 I_4 in [%.12e, %.12e]" % (float(d[0]), float(d[1])), flush=True)
if d[0] > 0: print("*** CERTIFIED FOR THE FULL KERNEL: >= %.10e > 0" % float(d[0]), flush=True)
else: print("straddles zero", flush=True)
print("DONE", flush=True)
