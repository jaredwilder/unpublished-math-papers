"""Close the three residual inputs: tail DERIVED, pi DERIVED, everything in one file.

1. pi from the Machin formula  pi/4 = 4 arctan(1/5) - arctan(1/239)  with the alternating series
   remainder bound: truncating arctan(1/k) after the term in k^{-(2m+1)} leaves a remainder of at
   most the next term, and the series alternates, so partial sums bracket the value.

2. tail beyond X derived in code:  for x >= X,
        F_j(x) = x^j e^{cx} (2 pi e^x)^e exp(-pi e^x)
   With u = e^x >= e^X =: U and x <= u, so
        x^j <= u^j,  e^{cx} = u^c,
   and the tail reduces to an explicit incomplete-gamma-style bound.
"""
from fractions import Fraction as F

D = 10 ** 45
def dn(q):
    r = F(q).limit_denominator(D); return r if r <= q else r - F(1, D)
def up(q):
    r = F(q).limit_denominator(D); return r if r >= q else r + F(1, D)

def arctan_inv(k, m):
    s = F(0); lo = None; hi = None
    for n in range(m):
        t = F((-1) ** n, (2 * n + 1) * k ** (2 * n + 1))
        s += t
        if n % 2 == 0: hi = s
        else: lo = s
    return lo, hi

def pi_bracket(m=40):
    a5lo, a5hi = arctan_inv(5, m)
    a239lo, a239hi = arctan_inv(239, m)
    lo = 4 * (4 * a5lo - a239hi)
    hi = 4 * (4 * a5hi - a239lo)
    return dn(lo), up(hi)

PI_LO, PI_HI = pi_bracket()
print("pi derived by Machin: [%.30f, %.30f]  width %.3e" % (float(PI_LO), float(PI_HI), float(PI_HI - PI_LO)), flush=True)

def exp_br(z):
    n = max(30, int(2 * float(z)) + 20)
    S = F(0); term = F(1)
    for k in range(n + 1):
        S = up(S + term); term = up(term * z / (k + 1))
    assert z < n + 2
    return dn(S - term), up(S + up(term / (1 - z / (n + 2))))

def exp_neg_br(z):
    lo, hi = exp_br(z); return dn(F(1) / hi), up(F(1) / lo)

X = F(3)
U_LO = exp_br(X)[0]
def tail_bound(j, extra):
    c = F(5, 4); e = 1 if extra else 0
    p = j + c + e - 1
    U = U_LO
    pref = (2 * PI_HI) ** e
    damp = exp_neg_br(dn(PI_LO * U))[1]
    corr = F(1) / (PI_LO - p / U)
    return up(pref * U ** p * damp * corr)

for j in (0, 2, 4):
    for extra in (True, False):
        print("   tail j=%d extra=%s  <= %.3e" % (j, extra, float(tail_bound(j, extra))), flush=True)

EC = {}
def e_br(z):
    if z not in EC: EC[z] = exp_br(z)
    return EC[z]
DC = {}
def damp_br(x):
    if x not in DC:
        ex = e_br(x)
        DC[x] = (exp_neg_br(up(PI_HI * ex[1]))[0], exp_neg_br(dn(PI_LO * ex[0]))[1])
    return DC[x]

N = 3000; H = X / N; C = F(5, 4)
def cell_bounds(a, b, j, extra):
    ea, eb = e_br(a), e_br(b)
    ga, gb = e_br(C * a), e_br(C * b)
    da, db = damp_br(a), damp_br(b)
    lo = dn(a ** j * ga[0] * db[0]); hi = up(b ** j * gb[1] * da[1])
    if extra:
        lo = dn(lo * 2 * PI_LO * ea[0]); hi = up(hi * 2 * PI_HI * eb[1])
    return lo, hi

EN = {}
print(flush=True)
for extra, nm in ((True, "A"), (False, "B")):
    for j in (0, 2, 4):
        lo = hi = F(0)
        for i in range(1, N + 1):
            b = i * H; a = b - H
            cl, ch = cell_bounds(a, b, j, extra)
            lo += H * cl; hi += H * ch
        t = tail_bound(j, extra)
        lo = dn(lo); hi = up(hi + t)
        EN[(nm, j)] = (lo, hi)
        print("   %s_%d in [%.18f, %.18f] width %.3e" % (nm, j, float(lo), float(hi), float(hi - lo)), flush=True)

def imul(u, v):
    pr = [u[0]*v[0], u[0]*v[1], u[1]*v[0], u[1]*v[1]]; return (min(pr), max(pr))
def iadd(u, v): return (u[0]+v[0], u[1]+v[1])
def isub(u, v): return (u[0]-v[1], u[1]-v[0])
def isc(c, u): return (c*u[0], c*u[1]) if c >= 0 else (c*u[1], c*u[0])
A0,A2,A4 = EN[("A",0)],EN[("A",2)],EN[("A",4)]
B0,B2,B4 = EN[("B",0)],EN[("B",2)],EN[("B",4)]
q2 = isub(isc(F(3), imul(B2,B2)), imul(B0,B4))
q1 = iadd(iadd(isc(F(-6), imul(A2,B2)), imul(A0,B4)), imul(A4,B0))
q0 = isub(isc(F(3), imul(A2,A2)), imul(A0,A4))
P3 = iadd(iadd(isc(F(9),q2), isc(F(3),q1)), q0)
print(flush=True)
for nm,iv in (("q2",q2),("q1",q1),("q0",q0),("P(3)",P3)):
    print("   %-5s in [%.15e, %.15e]" % (nm, float(iv[0]), float(iv[1])), flush=True)
print(flush=True)
if P3[0] > 0:
    print("*** SELF-CONTAINED CERTIFICATION: P(3) >= %.12e > 0" % float(P3[0]), flush=True)
    print("    pi derived by Machin in-file; tail derived in-file; all arithmetic exact rational.", flush=True)
else:
    print("straddles zero", flush=True)
print("DONE", flush=True)
