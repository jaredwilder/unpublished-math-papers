#!/usr/bin/env python3
import sympy as sp

def odds_rhs(y_prev, y_m, y_0, y_p):
    return sp.simplify(
        y_0**2/(1+y_prev)
        * (1+y_m)*(1+y_p)/(y_m*y_p)
    )

def check_rational_orbit():
    r,k,mu,nu = sp.symbols("r k mu nu")
    rhs = odds_rhs(
        (r-1+mu)/(k+nu),
        (r+mu)/(k-1+nu),
        (r+mu)/(k+nu),
        (r+mu)/(k+1+nu),
    )
    target = 1 + (r+1+mu)/(k+nu)
    assert sp.factor(rhs-target) == 0

def check_factorial_determinant():
    for k in range(0,5):
        for r in range(1,6):
            M = sp.Matrix([
                [
                    sp.Rational(1, sp.factorial(k+j-i)) if k+j-i >= 0 else 0
                    for j in range(r)
                ]
                for i in range(r)
            ])
            lhs = sp.simplify(M.det())
            rhs = sp.prod(sp.factorial(j)/sp.factorial(k+j) for j in range(r))
            assert sp.simplify(lhs-rhs) == 0

def check_factorial_odds():
    r,k=sp.symbols("r k", positive=True)
    R = k/(k+r)
    A = r/(k+r)
    assert sp.simplify(R+A-1) == 0
    assert sp.simplify(A/R-r/k) == 0

def check_fixed_slope_solution():
    a=sp.symbols("a", positive=True)
    y=1/a
    p=sp.log(y)
    ode=sp.simplify(
        (a**2*y+1)*sp.diff(p,a,2)
        +2*a*y*sp.diff(p,a)
        +y*(a**2-1)/(y+1)*sp.diff(p,a)**2
    )
    assert sp.simplify(ode) == 0

def check_next_correction():
    a=sp.symbols("a", positive=True)
    A,B=sp.symbols("A B")
    z=A/a+B/a**2
    eq=sp.simplify(a**2*sp.diff(z,a,2)+4*a*sp.diff(z,a)+2*z)
    assert sp.simplify(eq) == 0

def check_raw_jacobian():
    yp,ym,y0,yplus=sp.symbols("yp ym y0 yplus", positive=True)
    F = y0**2/(1+yp)*(1+ym)*(1+yplus)/(ym*yplus)-1
    y=sp.symbols("y", positive=True)
    vals=[
        sp.simplify(sp.diff(F,v).subs({yp:y,ym:y,y0:y,yplus:y}))
        for v in [yp,ym,y0,yplus]
    ]
    assert vals == [-1, -1/y, 2+2/y, -1/y]

def check_quadratic_layer_third_correction():
    a,b=sp.symbols("a b", nonzero=True)
    q=(
        1
        +(1-b**2)/(2*b**3)*a
        -(5*b**2+2)/(2*b**2)*a**2
        +(1/b)*a**3
        +sp.Rational(3,2)*a**4
    )
    P=6*a**4*b**2+28*a**3*b-10*a**2*b**2+26*a**2-22*a*b+4*b**2-7
    lhs=sp.expand(sp.diff(q,a,2)+4*b*sp.diff(q,a)+4*b**2*q)
    assert sp.simplify(lhs-P) == 0

def main():
    checks=[
        check_rational_orbit,
        check_factorial_determinant,
        check_factorial_odds,
        check_fixed_slope_solution,
        check_next_correction,
        check_raw_jacobian,
        check_quadratic_layer_third_correction,
    ]
    for fn in checks:
        fn()
        print("PASS", fn.__name__)
    print(f"PASS {len(checks)}/{len(checks)} terminal algebra checks")

if __name__=="__main__":
    main()
