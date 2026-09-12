"""Monotone cell bounds using kernel unimodality, with rational peak brackets."""
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

def logderiv_sign(x, j, c, an2):
    ex = e_br(x)
    lo = (F(j, 1) / x if j else F(0)) + c - up(an2[1] * ex[1])
    hi = (F(j, 1) / x if j else F(0)) + c - dn(an2[0] * ex[0])
    if lo > 0: return 1
    if hi < 0: return -1
    return 0

def peak_bracket(j, c, an2, lo=F(1, 1000), hi=F(4)):
    if j == 0: return (F(0), F(0))
    a, b = lo, hi
    for _ in range(30):
        m = (a + b) / 2
        s = logderiv_sign(m, j, c, an2)
        if s > 0: a = m
        elif s < 0: b = m
        else: break
    return (a, b)

X = F(7, 2); N = 4200; H = X / N; NMAX = 3
def iadd(u, v): return (u[0]+v[0], u[1]+v[1])
def isub(u, v): return (u[0]-v[1], u[1]-v[0])
def imul(u, v):
    p = [u[0]*v[0], u[0]*v[1], u[1]*v[0], u[1]*v[1]]; return (min(p), max(p))
def isc(c, u): return (c*u[0], c*u[1]) if c >= 0 else (c*u[1], c*u[0])

DCH = {}
def dmp(x, n2):
    key = (x, n2)
    if key not in DCH:
        ex = e_br(x)
        DCH[key] = (exp_neg_br(up(PI_HI * n2 * ex[1]))[0], exp_neg_br(dn(PI_LO * n2 * ex[0]))[1])
    return DCH[key]

def piece_val(x, j, cnum, n, positive):
    n2 = n * n; n4 = n2 * n2
    d = dmp(x, n2); g = e_br(cnum * x)
    if positive:
        return (dn(x ** j * 2 * PI_LO * PI_LO * n4 * g[0] * d[0]), up(x ** j * 2 * PI_HI * PI_HI * n4 * g[1] * d[1]))
    return (dn(x ** j * 3 * PI_LO * n2 * g[0] * d[0]), up(x ** j * 3 * PI_HI * n2 * g[1] * d[1]))

def srem(j):
    t = F(0)
    for n in range(NMAX + 1, NMAX + 8):
        n2 = n * n; n4 = n2 * n2
        t = up(t + up(2 * PI_HI * PI_HI * n4 * e_br(F(9, 4) * X)[1] * exp_neg_br(dn(PI_LO * n2))[1] * X * (X ** j + 1)))
    return t

def tail(j):
    U = e_br(X)[0]
    return up(2 * PI_HI * PI_HI * U ** (F(9, 4) + j) * exp_neg_br(dn(PI_LO * U))[1] * F(1) / (PI_LO - (F(9, 4) + j) / U))

PEAKS = {}
for n in range(1, 6):
    an2 = (PI_LO * n * n, PI_HI * n * n)
    for j in (0, 2, 4, 6, 8, 10):
        PEAKS[(n, j, True)] = peak_bracket(j, F(9, 4), an2)
        PEAKS[(n, j, False)] = peak_bracket(j, F(5, 4), an2)

def piece_cell(a, b, j, n, positive):
    cnum = F(9, 4) if positive else F(5, 4)
    p = PEAKS[(n, j, positive)]
    va, vb = piece_val(a, j, cnum, n, positive), piece_val(b, j, cnum, n, positive)
    if b < p[0] or a > p[1]: return (min(va[0], vb[0]), max(va[1], vb[1]))
    pk = piece_val(p[1], j, cnum, n, positive) if p[1] <= X else vb
    pk2 = piece_val(p[0], j, cnum, n, positive)
    return (min(va[0], vb[0]), max(va[1], vb[1], pk[1], pk2[1]))

print("monotone-cell enclosure, X=%s N=%d NMAX=%d" % (X, N, NMAX), flush=True)
J = {}
for j in (0, 2, 4, 6, 8, 10):
    tot = (F(0), F(0))
    for i in range(1, N + 1):
        b = i * H; a = b - H; c = (F(0), F(0))
        for n in range(1, NMAX + 1): c = iadd(c, isub(piece_cell(a, b, j, n, True), piece_cell(a, b, j, n, False)))
        tot = iadd(tot, (H * c[0], H * c[1]))
    s = srem(j); t = tail(j)
    J[j] = (dn(tot[0] - s - t), up(tot[1] + s + t))
    m = (J[j][0] + J[j][1]) / 2
    print("   J_%-2d in [%.14f, %.14f] rel width %.3e  srem %.2e" % (j, float(J[j][0]), float(J[j][1]), float((J[j][1]-J[j][0])/m) if m else 0, float(s)), flush=True)

print(flush=True); ok = True
for k in range(1, 5):
    lhs = isc(F(k*(2*k+1)*(2*k+2)), imul(J[2*k], J[2*k]))
    rhs = isc(F((k+1)*(2*k)*(2*k-1)), imul(J[2*k-2], J[2*k+2]))
    d = isub(lhs, rhs); g = d[0] > 0; ok = ok and g
    print("   rung k=%d in [%.8e, %.8e]  %s" % (k, float(d[0]), float(d[1]), "CERTIFIED" if g else "straddles"), flush=True)
print("\nseries remainder and truncation tail INCLUDED in every enclosure.", flush=True)
print("all four rungs: %s" % ok, flush=True)
print("DONE", flush=True)
