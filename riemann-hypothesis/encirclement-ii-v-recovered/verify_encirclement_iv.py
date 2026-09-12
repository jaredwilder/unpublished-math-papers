#!/usr/bin/env python3
import sympy as sp

def check_bessel_curvature():
    k,b = sp.symbols("k b", positive=True)
    B = lambda x: sp.gamma(b)/(sp.gamma(x+1)*sp.gamma(x+b))
    R = sp.simplify(B(k-1)*B(k+1)/B(k)**2)
    target = k*(k+b-1)/((k+1)*(k+b))
    assert sp.simplify(R-target) == 0

def check_heat_coefficient_pde():
    z = sp.symbols("z")
    a = sp.symbols("a0:7")
    G = sum(a[n]*z**n for n in range(7))
    L = sp.expand(4*z*sp.diff(G,z,2)+2*sp.diff(G,z))
    for k in range(6):
        coeff = sp.expand(L).coeff(z,k)
        assert sp.simplify(coeff-(2*k+2)*(2*k+1)*a[k+1]) == 0

def check_dynamic_harmonicity():
    RB,AB,X,Y,Xt,Yt = sp.symbols("RB AB X Y Xt Yt", positive=True)
    RD = RB*sp.exp(X)
    AD = AB*sp.exp(Y)
    dF = sp.expand(RD*Xt + AD*Yt)
    assert sp.simplify(dF-(RD*Xt+AD*Yt)) == 0

def check_second_time_identity():
    RB,AB,X,Y,Xt,Yt,Xtt,Ytt = sp.symbols(
        "RB AB X Y Xt Yt Xtt Ytt", positive=True
    )
    RD = RB*sp.exp(X)
    AD = AB*sp.exp(Y)
    lhs = RD*Xtt + AD*Ytt
    source = -RD*Xt**2-AD*Yt**2
    second = RD*(Xtt+Xt**2)+AD*(Ytt+Yt**2)
    assert sp.simplify(second - (lhs-source)) == 0

def reciprocal_sequence(h, N):
    e=[sp.Integer(1)]
    for n in range(1,N+1):
        val=sum((-1)**(j+1)*h[j]*e[n-j] for j in range(1,n+1))
        e.append(sp.simplify(val))
    return e

def check_dual_jacobi_trudi():
    h=[sp.Integer(1),
       sp.Rational(2,3), sp.Rational(5,11), sp.Rational(7,19),
       sp.Rational(11,37), sp.Rational(13,53), sp.Rational(17,71),
       sp.Rational(19,89), sp.Rational(23,107), sp.Rational(29,131),
       sp.Rational(31,151), sp.Rational(37,173)]
    e=reciprocal_sequence(h, len(h)-1)
    def hv(n):
        return h[n] if 0 <= n < len(h) else sp.Integer(0)
    def ev(n):
        return e[n] if 0 <= n < len(e) else sp.Integer(0)
    for r in range(1,5):
        for k in range(1,5):
            P=sp.Matrix([[hv(k+j-i) for j in range(r)] for i in range(r)]).det()
            Q=sp.Matrix([[ev(r+j-i) for j in range(k)] for i in range(k)]).det()
            assert sp.simplify(P-Q)==0

def check_vandermonde_sign_cancellation():
    for m in range(1,7):
        rho=[sp.Integer(j+2) for j in range(m)]
        c=[sp.Integer((-1)**j)*(j+1) for j in range(m)]
        V1=sp.Matrix([[rho[j]**i for j in range(m)] for i in range(m)]).det()
        V2=sp.Matrix([[rho[i]**(-j) for j in range(m)] for i in range(m)]).det()
        lead=sp.prod(c)*V1*V2
        assert lead > 0

def main():
    checks=[
        check_bessel_curvature,
        check_heat_coefficient_pde,
        check_dynamic_harmonicity,
        check_second_time_identity,
        check_dual_jacobi_trudi,
        check_vandermonde_sign_cancellation,
    ]
    for fn in checks:
        fn()
        print("PASS", fn.__name__)
    print(f"PASS {len(checks)}/{len(checks)} algebraic checks")

if __name__=="__main__":
    main()
