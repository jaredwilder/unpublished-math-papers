#!/usr/bin/env python3
"""Exact sanity checks for finite even-moment rigidity.

This is not the proof. It checks the Newton-identity reconstruction for exact
rational choices at Q=1..4 and verifies the triangular raw-to-centered step.
"""
import sympy as sp

x = sp.symbols("x")


def elementary_from_power_sums(ps):
    # Newton: m e_m = sum_{i=1}^m (-1)^(i-1) e_{m-i} p_i, e_0=1.
    e = [sp.Integer(1)]
    for m in range(1, len(ps) + 1):
        em = sum(((-1) ** (i - 1)) * e[m - i] * ps[i - 1]
                 for i in range(1, m + 1)) / m
        e.append(sp.simplify(em))
    return e


def monic_from_power_sums(ps):
    e = elementary_from_power_sums(ps)
    n = len(ps)
    return sp.expand(sum(((-1) ** m) * e[m] * x ** (n - m)
                         for m in range(n + 1)))


def centered_even_quad(d, t, m):
    pts = [d + sp.I*t, d - sp.I*t, -d - sp.I*t, -d + sp.I*t]
    return sp.expand(sum(z ** (2*m) for z in pts))


def raw_even_quad(d, t, m):
    h = sp.Rational(1, 2)
    pts = [h + d + sp.I*t, h + d - sp.I*t,
           h - d - sp.I*t, h - d + sp.I*t]
    return sp.expand(sum(z ** (2*m) for z in pts))


def centered_from_raw_even(raw, count):
    # raw[m-1] = sum (1/2+x)^(2m); centered odd sums vanish.
    centered = {0: sp.Integer(count)}
    for m in range(1, len(raw) + 1):
        known = sp.Integer(0)
        for j in range(m):
            known += (sp.binomial(2*m, 2*j)
                      * sp.Rational(1, 2) ** (2*m - 2*j)
                      * centered[j])
        centered[m] = sp.simplify(raw[m-1] - known)
    return [centered[m] for m in range(1, len(raw) + 1)]


cases = {
    1: [(sp.Rational(2, 3), sp.Rational(5, 4))],
    2: [(sp.Rational(1, 3), sp.Rational(7, 5)),
        (sp.Rational(2, 5), sp.Rational(4, 3))],
    3: [(sp.Rational(1, 4), sp.Rational(5, 3)),
        (sp.Rational(3, 7), sp.Rational(9, 5)),
        (sp.Rational(2, 9), sp.Rational(7, 4))],
    4: [(sp.Rational(1, 5), sp.Rational(4, 3)),
        (sp.Rational(2, 7), sp.Rational(8, 5)),
        (sp.Rational(3, 11), sp.Rational(5, 2)),
        (sp.Rational(4, 13), sp.Rational(7, 3))],
}

print("FINITE MOMENT RIGIDITY — EXACT SANITY CHECK")
print("===========================================")
for Q, pairs in cases.items():
    N = 2 * Q
    raw = [sp.expand(sum(raw_even_quad(d, t, m) for d, t in pairs))
           for m in range(1, N + 1)]
    centered = centered_from_raw_even(raw, 4*Q)
    direct_centered = [sp.expand(sum(centered_even_quad(d, t, m)
                                     for d, t in pairs))
                       for m in range(1, N + 1)]
    tri_ok = all(sp.simplify(a-b) == 0
                 for a, b in zip(centered, direct_centered))

    U = []
    for d, t in pairs:
        U += [(t + sp.I*d)**2, (t - sp.I*d)**2]

    ps = [sp.simplify(centered[m-1] / (2*((-1)**m)))
          for m in range(1, N + 1)]
    direct_ps = [sp.expand(sum(u**m for u in U))
                 for m in range(1, N + 1)]
    ps_ok = all(sp.simplify(a-b) == 0 for a, b in zip(ps, direct_ps))

    p_newton = sp.factor(monic_from_power_sums(ps), extension=sp.I)
    p_direct = sp.factor(sp.prod(x-u for u in U), extension=sp.I)
    poly_ok = sp.simplify(sp.expand(p_newton-p_direct)) == 0

    all_nonneg_real = all(
        sp.im(sp.N(u)) == 0 and sp.re(sp.N(u)) >= 0 for u in U
    )

    print(
        f"Q={Q}: triangular_raw_to_centered={tri_ok}; "
        f"power_sums={ps_ok}; Newton_reconstruction={poly_ok}; "
        f"RHS_all_nonnegative_real={all_nonneg_real}"
    )
    assert tri_ok and ps_ok and poly_ok and not all_nonneg_real

print("PASS: Q=1..4 exact checks agree with the general proof.")
