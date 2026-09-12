#!/usr/bin/env python3
"""Reproduce the gamma-theta quartic constants in high precision."""
import mpmath as mp

mp.mp.dps = 80
pi = mp.pi
q = mp.mpf(1) / 4

pi_quarter = pi**q
E2 = pi**(-mp.mpf(1)/2) * mp.gamma(mp.mpf(3)/4) / mp.gamma(q)
E4 = 1 / (4*pi)
D4 = E4 / (E2*E2) - 1

print("pi^(1/4) =", mp.nstr(pi_quarter, 60))
print("E[X^2]   =", mp.nstr(E2, 60))
print("E[X^4]   =", mp.nstr(E4, 60))
print("Disp4     =", mp.nstr(D4, 60))

# Generic exp(-pi x^p) family.
def disp(p):
    p = mp.mpf(p)
    return mp.gamma(5/p)*mp.gamma(1/p)/(mp.gamma(3/p)**2)-1

for p in (1, 2, 4):
    print(f"p={p}: Disp =", mp.nstr(disp(p), 60))

assert abs(pi_quarter - mp.mpf('1.3313353638003897127975349179502808533093662238181')) < mp.mpf('1e-49')
assert abs(disp(1)-5) < mp.mpf('1e-70')
assert abs(disp(2)-2) < mp.mpf('1e-70')
assert D4 < 2
print("ALL CHECKS OK")
