#!/usr/bin/env python3
"""
Corrected Polymath-15 real-axis main term and x-derivative.
For y=0: f = S + gamma*conj(S), not (1+gamma)*S.
High-precision experimental code; a proof requires interval evaluation and rigorous error bounds.
"""
import argparse
import mpmath as mp

def Log(z): return mp.log(z)

def alpha(s):
    return 1/(2*s)+1/(s-1)+mp.mpf("0.5")*Log(s/(2*mp.pi))

def alpha_prime(s):
    return -1/(2*s*s)-1/((s-1)*(s-1))+1/(2*s)

def M0(s):
    return (mp.mpf(1)/16)*s*(s-1)*mp.pi**(-s/2)*mp.sqrt(2*mp.pi)*mp.e**(
        (s/2-mp.mpf("0.5"))*Log(s/2)-s/2
    )

def Mt(s,t):
    return mp.e**(t*alpha(s)**2/4)*M0(s)

def beta(s,t):
    return alpha(s)+(t/2)*alpha(s)*alpha_prime(s)

def params(t,x):
    a=(1-1j*x)/2
    abar=(1+1j*x)/2
    sstar=a+(t/2)*alpha(a)
    sp=-0.5j*(1+(t/2)*alpha_prime(a))
    gamma=Mt(abar,t)/Mt(a,t)
    gp=0.5j*gamma*(beta(abar,t)+beta(a,t))
    N=int(mp.floor(mp.sqrt(x/(4*mp.pi)+t/16)))
    return a,sstar,sp,gamma,gp,N

def main_and_derivative(t,x):
    a,sstar,sp,gamma,gp,N=params(t,x)
    S=0; T1=0
    for n in range(1,N+1):
        ln=mp.log(n)
        b=mp.e**(t*ln*ln/4)
        term=b*mp.e**(-sstar*ln)
        S+=term; T1+=ln*term
    Sp=-sp*T1
    f=S+gamma*mp.conj(S)
    fp=Sp+gp*mp.conj(S)+gamma*mp.conj(Sp)
    return f,fp,N,gamma,S

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--t",type=float,default=0.2)
    ap.add_argument("--x",type=float,required=True)
    ap.add_argument("--dps",type=int,default=80)
    args=ap.parse_args()
    mp.mp.dps=args.dps
    f,fp,N,gamma,S=main_and_derivative(mp.mpf(args.t),mp.mpf(args.x))
    print("N =",N)
    print("|gamma|-1 =",mp.nstr(abs(gamma)-1,30))
    print("f =",mp.nstr(f,40))
    print("f'=",mp.nstr(fp,40))
    print("|f| =",mp.nstr(abs(f),30))
    print("|f'|=",mp.nstr(abs(fp),30))

if __name__=="__main__": main()
