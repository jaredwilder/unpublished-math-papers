"""Exact rational certificate for the higher-theta-term tail at u=0."""
from fractions import Fraction as F
DEN=10**30
def dn(x): return F(int(x*DEN)-1,DEN)
def up(x): return F(int(x*DEN)+2,DEN)
def atan_inv(n,t):
    lo=F(0); s=1; x=F(1,n)
    for k in range(t):
        lo += s*x/(2*k+1); x/=F(n*n); s=-s
    rem=F(1,n)**(2*t+1)/(2*t+1)
    return (lo-rem, lo+rem)
a5=atan_inv(5,60); a239=atan_inv(239,25)
PI_LO=16*a5[0]-4*a239[1]; PI_HI=16*a5[1]-4*a239[0]
def exp_br(z,n=120):
    S=F(0); t=F(1)
    for k in range(n+1):
        S+=t; t*=z/(k+1)
    tail=t/(1-z/(n+2))
    return (S, S+tail)
def exp_neg_br(z):
    lo,hi=exp_br(z); return (1/hi, 1/lo)

print("   pi in [%.30f, %.30f]"%(float(PI_LO),float(PI_HI)),flush=True)
TAIL_HI=F(0)
for n in range(2,40):
    lo,hi=exp_neg_br(PI_LO*n*n)
    TAIL_HI += F(2)*PI_HI*PI_HI*F(n)**4*hi
print("   tail upper bound at u=0 : %.18e"%float(TAIL_HI),flush=True)
ep_lo,ep_hi=exp_neg_br(PI_HI)
n1_lo = (F(2)*PI_LO*PI_LO - F(3)*PI_HI)*ep_lo
PHI_LO = n1_lo - TAIL_HI
print("   n=1 term lower bound    : %.18f"%float(n1_lo),flush=True)
print("   Phi(0) lower bound      : %.18f"%float(PHI_LO),flush=True)
rel = TAIL_HI/PHI_LO
print("   CERTIFIED relative tail : %.18e"%float(rel),flush=True)
print("\n   is the certified relative tail below 1/100 ?  %s"%(rel < F(1,100)),flush=True)
print("   is it below 1/300 ?                          %s"%(rel < F(1,300)),flush=True)
print("\nDONE",flush=True)
