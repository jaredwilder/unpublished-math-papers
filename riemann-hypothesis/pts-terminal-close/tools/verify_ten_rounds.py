#!/usr/bin/env python3
import sympy as sp

def check_mixed_derivative_lattice():
    x,u=sp.symbols("x u", real=True)
    for aa in range(5):
        for bb in range(6):
            lhs=u**(2*aa)*sp.diff(sp.cos(x*u),x,bb)
            rhs=(-1)**aa*sp.diff(sp.cos(x*u),x,2*aa+bb)
            assert sp.simplify(lhs-rhs)==0

def check_track_velocity():
    A,B=sp.symbols("A B", nonzero=True)
    xp=B/A
    assert sp.simplify(-B+A*xp)==0

def check_track_acceleration():
    A,B,C,D=sp.symbols("A B C D", nonzero=True)
    xp=B/A
    Adot=-C+xp*B
    Bdot=-D+xp*C
    xpp=sp.simplify((Bdot*A-B*Adot)/A**2)
    target=-D/A+2*B*C/A**2-B**3/A**3
    assert sp.simplify(xpp-target)==0

def check_co_moving_cancel():
    A,B=sp.symbols("A B", nonzero=True)
    v=B/A
    assert sp.simplify(-B+v*A)==0

def check_q2_product_derivative():
    u,m=sp.symbols("u m", positive=True)
    W=sp.Function("W")(u)
    g=u**m*W
    target=m*(m-1)*u**(m-2)*W+2*m*u**(m-1)*sp.diff(W,u)+u**m*sp.diff(W,u,2)
    assert sp.simplify(sp.diff(g,u,2)-target)==0

def check_W_derivatives():
    u,t=sp.symbols("u t", real=True)
    P=sp.Function("P")(u)
    W=sp.exp(t*u**2)*P
    W1=sp.exp(t*u**2)*(2*t*u*P+sp.diff(P,u))
    W2=sp.exp(t*u**2)*((2*t+4*t**2*u**2)*P+4*t*u*sp.diff(P,u)+sp.diff(P,u,2))
    assert sp.simplify(sp.diff(W,u)-W1)==0
    assert sp.simplify(sp.diff(W,u,2)-W2)==0

def check_rs_sstar_prime():
    t,ap=sp.symbols("t ap", real=True)
    got=-sp.I/2 + t/2*ap*(-sp.I/2)
    target=-sp.I/2*(1+t*ap/2)
    assert sp.simplify(got-target)==0

def check_taylor_remainder_track3_threshold():
    margin=sp.Rational(296,10**10)
    target=margin/10
    assert float(target)==2.96e-9

def main():
    checks=[check_mixed_derivative_lattice,check_track_velocity,check_track_acceleration,
            check_co_moving_cancel,check_q2_product_derivative,check_W_derivatives,
            check_rs_sstar_prime,check_taylor_remainder_track3_threshold]
    for fn in checks:
        fn(); print("PASS",fn.__name__)
    print(f"PASS {len(checks)}/{len(checks)} exact checks")
    print("STATUS: PTS remains UNPROVED; TCR-5 unchanged.")

if __name__=="__main__": main()
