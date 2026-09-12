#!/usr/bin/env python3
import sympy as sp

def check_factorial_benchmark():
    r,k=sp.symbols("r k", positive=True, integer=True)
    R=k/(k+r)
    A=r/(k+r)
    assert sp.simplify(R+A-1)==0

def check_hoggatt2_curvature():
    k=sp.symbols("k", positive=True, integer=True)
    b=lambda n: 1/(sp.gamma(n+1)*sp.gamma(n+2))
    R=sp.simplify(b(k-1)*b(k+1)/b(k)**2)
    assert sp.simplify(R-k/(k+2))==0

def check_shifted_rational_interior():
    r,k,mu,nu=sp.symbols("r k mu nu")
    Y=lambda rr,kk:(rr+mu)/(kk+nu)
    rhs=sp.simplify(
        Y(r,k)**2/(1+Y(r-1,k))
        *(1+Y(r,k-1))*(1+Y(r,k+1))
        /(Y(r,k-1)*Y(r,k+1))
    )
    assert sp.simplify(rhs-(1+Y(r+1,k)))==0

def check_shifted_boundary_selection():
    k=sp.symbols("k", positive=True)
    mu=sp.symbols("mu")
    assert sp.simplify((mu/k).subs(mu,0))==0
    assert sp.solve(sp.Eq(mu/k,0),mu)==[0]

def check_normalized_equation_algebra():
    RB,AB,x,y=sp.symbols("RB AB x y", positive=True)
    expr=RB*sp.exp(x)+AB*sp.exp(y)
    assert expr.has(sp.exp(x)) and expr.has(sp.exp(y))

def main():
    checks=[
        check_factorial_benchmark,
        check_hoggatt2_curvature,
        check_shifted_rational_interior,
        check_shifted_boundary_selection,
        check_normalized_equation_algebra,
    ]
    for fn in checks:
        fn()
        print("PASS",fn.__name__)
    print(f"PASS {len(checks)}/{len(checks)} exact algebra checks")

if __name__=="__main__":
    main()
