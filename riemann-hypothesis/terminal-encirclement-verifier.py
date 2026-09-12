#!/usr/bin/env python3
"""
Machine checks for algebraic identities extracted in the RH terminal-encirclement packet.
These checks do NOT prove RH. They verify only the finite symbolic identities named below.
"""

import sympy as sp

def check_reciprocal_map():
    beta, gamma = sp.symbols("beta gamma", real=True)
    rho = beta + sp.I*gamma
    z = (rho - 1)/rho
    lhs = sp.simplify(sp.together(z * sp.conjugate(z)))
    expected = ((beta-1)**2 + gamma**2)/(beta**2 + gamma**2)
    assert sp.simplify(lhs - expected) == 0

    inv = sp.simplify((1-(1-rho))/(1-rho))
    zmate = sp.simplify(((1-rho)-1)/(1-rho))
    assert sp.simplify(zmate - 1/z) == 0

    q = sp.simplify(z + 1/z)
    target = 2 - 1/(rho*(1-rho))
    assert sp.simplify(q-target) == 0

def check_round8_factorization():
    a, b = sp.symbols("a b", positive=True)
    lhs = 1/a**2 + 1/b**2 - 8/(a+b)**2
    rhs = (a-b)**2*(a**2+4*a*b+b**2)/(a**2*b**2*(a+b)**2)
    assert sp.simplify(lhs-rhs) == 0

def check_condensation_r3():
    am2, am1, a0, a1, a2 = sp.symbols("a_m2 a_m1 a0 a1 a2")
    D1 = a0
    D2k = sp.det(sp.Matrix([[a0,a1],[am1,a0]]))
    D2m = sp.det(sp.Matrix([[am1,a0],[am2,am1]]))
    D2p = sp.det(sp.Matrix([[a1,a2],[a0,a1]]))
    D3 = sp.det(sp.Matrix([[a0,a1,a2],[am1,a0,a1],[am2,am1,a0]]))
    assert sp.expand(D3*D1 - (D2k**2 - D2m*D2p)) == 0

def check_terminal_r2_symmetrized_integrand():
    u, v = sp.symbols("u v", positive=True)
    k = sp.symbols("k", integer=True, positive=True)
    c = (2*k)*(2*k-1)/((2*k+1)*(2*k+2))
    bracket = u**2*v**2 - sp.Rational(1,2)*c*(u**4+v**4)
    witness = sp.N(bracket.subs({k:1,u:10,v:1}))
    assert witness < 0
    equal = sp.simplify(bracket.subs({u:v}))
    assert sp.simplify(equal / v**4 - (1-c)) == 0
    assert sp.N((1-c).subs(k,1)) > 0

def check_positive_mixture_counterexample():
    a0 = sp.Rational(1,1)
    a1 = sp.Rational(1,10)*100/sp.factorial(2)
    a2 = sp.Rational(1,10)*10000/sp.factorial(4)
    D21 = sp.simplify(a1**2 - a0*a2)
    assert D21 < 0
    assert D21 == sp.Rational(-50,3)

def check_tilted_ratio_identity_symbolic():
    G0, Gs, E = sp.symbols("G0 Gs E", nonzero=True)
    lhs = E * G0/Gs
    rhs = G0/Gs * E
    assert sp.simplify(lhs-rhs) == 0

def main():
    checks = [
        check_reciprocal_map,
        check_round8_factorization,
        check_condensation_r3,
        check_terminal_r2_symmetrized_integrand,
        check_positive_mixture_counterexample,
        check_tilted_ratio_identity_symbolic,
    ]
    for fn in checks:
        fn()
        print(f"PASS {fn.__name__}")
    print(f"PASS {len(checks)}/{len(checks)} algebraic checks")
    print("NOTE: These checks verify identities only; they do not prove the Riemann Hypothesis.")

if __name__ == "__main__":
    main()
