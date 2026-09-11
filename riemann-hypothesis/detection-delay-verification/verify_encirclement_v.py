#!/usr/bin/env python3
import sympy as sp
import cmath, itertools, math


def elementary(xs):
    e = [sp.Integer(1)]
    for x in xs:
        e.append(sp.Integer(0))
        for j in range(len(e) - 1, 0, -1):
            e[j] = sp.expand(e[j] + x * e[j - 1])
    return e


def det_from_coeff(a, r, k):
    return sp.Matrix([
        [a[k + j - i] if 0 <= k + j - i < len(a) else 0 for j in range(r)]
        for i in range(r)
    ]).det()


def check_reciprocal_heat_pde():
    z = sp.symbols("z")
    E = sp.Function("E")(z)
    H = 1 / E
    rhs = sp.simplify((4 * z * sp.diff(H, z, 2) + 2 * sp.diff(H, z)) * E**2)
    target = -4 * z * sp.diff(E, z, 2) - 2 * sp.diff(E, z) + 8 * z * sp.diff(E, z)**2 / E
    assert sp.simplify(rhs - target) == 0


def check_bilinear_harmonic():
    r, k = sp.symbols("r k", integer=True)
    f = r * k
    dk = sp.expand(f.subs(k, k + 1) - 2 * f + f.subs(k, k - 1))
    dr = sp.expand(f.subs(r, r + 1) - 2 * f + f.subs(r, r - 1))
    assert dk == 0 and dr == 0


def check_nonreversible_pf_example():
    xs = [sp.Integer(x) for x in [1, 2, 3, 5, 7, 11, 13, 17]]
    a = elementary(xs)

    def D(r, k):
        if r == 0:
            return sp.Integer(1)
        return sp.factor(det_from_coeff(a, r, k))

    def R(r, k):
        return sp.simplify(D(r, k - 1) * D(r, k + 1) / D(r, k)**2)

    def A(r, k):
        return sp.simplify(D(r - 1, k) * D(r + 1, k) / D(r, k)**2)

    r = k = 2
    path1 = sp.simplify(R(r, k) / R(r, k + 1) * A(r, k + 1) / A(r + 1, k + 1))
    path2 = sp.simplify(A(r, k) / A(r + 1, k) * R(r + 1, k) / R(r + 1, k + 1))
    assert sp.simplify(path1 - path2) != 0


def check_dual_jt_schur_numeric():
    xs = [sp.Rational(1, 2), sp.Rational(1, 3), sp.Rational(1, 5),
          sp.Rational(1, 7), sp.Rational(1, 11)]
    a = elementary(xs)
    for r in range(1, 4):
        for k in range(1, 4):
            assert sp.simplify(det_from_coeff(a, r, k)) > 0


def check_phase_budget_example():
    theta = 0.08
    rho = 0.2
    xs = [rho * cmath.exp(1j * theta), rho * cmath.exp(-1j * theta),
          0.12, 0.09, 0.05, 0.03]
    a = [1 + 0j]
    for x in xs:
        a.append(0j)
        for j in range(len(a) - 1, 0, -1):
            a[j] += x * a[j - 1]
    for r in [1, 2, 3, 4, 5]:
        assert r * theta < math.pi / 2
        for k in [1, 2, 3]:
            M = sp.Matrix([
                [complex(a[k + j - i]) if 0 <= k + j - i < len(a) else 0j
                 for j in range(r)]
                for i in range(r)
            ])
            val = complex(M.det())
            assert abs(val.imag) < 1e-8
            assert val.real > 0


def check_occupancy_cap_bruteforce():
    rows, cols, maxsym = 2, 3, 4
    count = 0
    max_occ = [0] * (maxsym + 1)
    vals = range(1, maxsym + 1)
    for entries in itertools.product(vals, repeat=rows * cols):
        T = [entries[i * cols:(i + 1) * cols] for i in range(rows)]
        if any(T[i][j] > T[i][j + 1] for i in range(rows) for j in range(cols - 1)):
            continue
        if any(T[0][j] >= T[1][j] for j in range(cols)):
            continue
        count += 1
        for s in vals:
            occ = sum(v == s for v in entries)
            max_occ[s] = max(max_occ[s], occ)
    assert count > 0
    assert max(max_occ) <= cols


def main():
    checks = [
        check_reciprocal_heat_pde,
        check_bilinear_harmonic,
        check_nonreversible_pf_example,
        check_dual_jt_schur_numeric,
        check_phase_budget_example,
        check_occupancy_cap_bruteforce,
    ]
    for fn in checks:
        fn()
        print("PASS", fn.__name__)
    print(f"PASS {len(checks)}/{len(checks)} algebraic/combinatorial checks")
    print("NOTE: These checks do not prove RH or the global collision-angle condition.")


if __name__ == "__main__":
    main()
